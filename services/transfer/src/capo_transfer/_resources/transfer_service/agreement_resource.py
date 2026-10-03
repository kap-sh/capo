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
    import capo_transfer.types.agreement_id
    import capo_transfer.types.agreement_status_type
    import capo_transfer.types.create_agreement_request
    import capo_transfer.types.create_agreement_response
    import capo_transfer.types.custom_directories_type
    import capo_transfer.types.delete_agreement_request
    import capo_transfer.types.describe_agreement_request
    import capo_transfer.types.describe_agreement_response
    import capo_transfer.types.description
    import capo_transfer.types.enforce_message_signing_type
    import capo_transfer.types.home_directory
    import capo_transfer.types.list_agreements_request
    import capo_transfer.types.list_agreements_response
    import capo_transfer.types.listed_agreement
    import capo_transfer.types.max_results
    import capo_transfer.types.next_token
    import capo_transfer.types.preserve_filename_type
    import capo_transfer.types.profile_id
    import capo_transfer.types.role
    import capo_transfer.types.server_id
    import capo_transfer.types.tags
    import capo_transfer.types.update_agreement_request
    import capo_transfer.types.update_agreement_response
    from capo_transfer._services.async_transfer import (
        AsyncTransferClient,
        AsyncTransferClientConfig,
    )
    from capo_transfer._services.transfer import TransferClient, TransferClientConfig


class AgreementResource:
    def __init__(self, service: TransferClient) -> None:
        self._service = service

    def create(
        self,
        server_id: "capo_transfer.types.server_id.ServerId",
        local_profile_id: "capo_transfer.types.profile_id.ProfileId",
        partner_profile_id: "capo_transfer.types.profile_id.ProfileId",
        access_role: "capo_transfer.types.role.Role",
        *,
        config_overrides: Optional[TransferClientConfig] = None,
        description: Optional["capo_transfer.types.description.Description"] = None,
        base_directory: Optional[
            "capo_transfer.types.home_directory.HomeDirectory"
        ] = None,
        status: Optional[
            "capo_transfer.types.agreement_status_type.AgreementStatusType"
        ] = None,
        tags: Optional["capo_transfer.types.tags.Tags"] = None,
        preserve_filename: Optional[
            "capo_transfer.types.preserve_filename_type.PreserveFilenameType"
        ] = None,
        enforce_message_signing: Optional[
            "capo_transfer.types.enforce_message_signing_type.EnforceMessageSigningType"
        ] = None,
        custom_directories: Optional[
            "capo_transfer.types.custom_directories_type.CustomDirectoriesType"
        ] = None,
    ) -> "capo_transfer.types.create_agreement_response.CreateAgreementResponse":
        """<p>Creates an agreement. An agreement is a bilateral trading partner agreement, or partnership, between an Transfer Family server and an AS2 process. The agreement defines the file and message transfer relationship between the server and the AS2 process. To define an agreement, Transfer Family combines a server, local profile, partner profile, certificate, and other attributes.</p> <p>The partner is identified with the <code>PartnerProfileId</code>, and the AS2 process is identified with the <code>LocalProfileId</code>.</p> <note> <p>Specify <i>either</i> <code>BaseDirectory</code> or <code>CustomDirectories</code>, but not both. Specifying both causes the command to fail.</p> </note>

        Args:
            description: <p>A name or short description to identify the agreement. </p>
            server_id: <p>A system-assigned unique identifier for a server instance. This is the specific server that the agreement uses.</p>
            local_profile_id: <p>A unique identifier for the AS2 local profile.</p>
            partner_profile_id: <p>A unique identifier for the partner profile used in the agreement.</p>
            base_directory: <p>The landing directory (folder) for files transferred by using the AS2 protocol.</p> <p>A <code>BaseDirectory</code> example is <code>/<i>amzn-s3-demo-bucket</i>/home/mydirectory</code>.</p>
            access_role: <p>Connectors are used to send files using either the AS2 or SFTP protocol. For the access role, provide the Amazon Resource Name (ARN) of the Identity and Access Management role to use.</p> <p> <b>For AS2 connectors</b> </p> <p>With AS2, you can send files by calling <code>StartFileTransfer</code> and specifying the file paths in the request parameter, <code>SendFilePaths</code>. We use the file’s parent directory (for example, for <code>--send-file-paths /bucket/dir/file.txt</code>, parent directory is <code>/bucket/dir/</code>) to temporarily store a processed AS2 message file, store the MDN when we receive them from the partner, and write a final JSON file containing relevant metadata of the transmission. So, the <code>AccessRole</code> needs to provide read and write access to the parent directory of the file location used in the <code>StartFileTransfer</code> request. Additionally, you need to provide read and write access to the parent directory of the files that you intend to send with <code>StartFileTransfer</code>.</p> <p>If you are using Basic authentication for your AS2 connector, the access role requires the <code>secretsmanager:GetSecretValue</code> permission for the secret. If the secret is encrypted using a customer-managed key instead of the Amazon Web Services managed key in Secrets Manager, then the role also needs the <code>kms:Decrypt</code> permission for that key.</p> <p> <b>For SFTP connectors</b> </p> <p>Make sure that the access role provides read and write access to the parent directory of the file location that's used in the <code>StartFileTransfer</code> request. Additionally, make sure that the role provides <code>secretsmanager:GetSecretValue</code> permission to Secrets Manager.</p>
            status: <p>The status of the agreement. The agreement can be either <code>ACTIVE</code> or <code>INACTIVE</code>.</p>
            tags: <p>Key-value pairs that can be used to group and search for agreements.</p>
            preserve_filename: <p> Determines whether or not Transfer Family appends a unique string of characters to the end of the AS2 message payload filename when saving it. </p> <ul> <li> <p> <code>ENABLED</code>: the filename provided by your trading parter is preserved when the file is saved.</p> </li> <li> <p> <code>DISABLED</code> (default value): when Transfer Family saves the file, the filename is adjusted, as described in <a href="https://docs.aws.amazon.com/transfer/latest/userguide/send-as2-messages.html#file-names-as2">File names and locations</a>.</p> </li> </ul>
            enforce_message_signing: <p> Determines whether or not unsigned messages from your trading partners will be accepted. </p> <ul> <li> <p> <code>ENABLED</code>: Transfer Family rejects unsigned messages from your trading partner.</p> </li> <li> <p> <code>DISABLED</code> (default value): Transfer Family accepts unsigned messages from your trading partner.</p> </li> </ul>
            custom_directories: <p>A <code>CustomDirectoriesType</code> structure. This structure specifies custom directories for storing various AS2 message files. You can specify directories for the following types of files.</p> <ul> <li> <p>Failed files</p> </li> <li> <p>MDN files</p> </li> <li> <p>Payload files</p> </li> <li> <p>Status files</p> </li> <li> <p>Temporary files</p> </li> </ul>

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
            req: "OperationRequest[capo_transfer.types.create_agreement_request.CreateAgreementRequest]",
        ) -> OperationResponse[
            "capo_transfer.types.create_agreement_response.CreateAgreementResponse"
        ]:
            import capo_transfer._operations.transfer_service.create_agreement

            output, http_response = (
                capo_transfer._operations.transfer_service.create_agreement.create_agreement(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_transfer.types.create_agreement_request.CreateAgreementRequest = {
            "server_id": server_id,
            "local_profile_id": local_profile_id,
            "partner_profile_id": partner_profile_id,
            "access_role": access_role,
        }
        if description is not None:
            input_["description"] = description
        if base_directory is not None:
            input_["base_directory"] = base_directory
        if status is not None:
            input_["status"] = status
        if tags is not None:
            input_["tags"] = tags
        if preserve_filename is not None:
            input_["preserve_filename"] = preserve_filename
        if enforce_message_signing is not None:
            input_["enforce_message_signing"] = enforce_message_signing
        if custom_directories is not None:
            input_["custom_directories"] = custom_directories

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def read(
        self,
        agreement_id: "capo_transfer.types.agreement_id.AgreementId",
        server_id: "capo_transfer.types.server_id.ServerId",
        *,
        config_overrides: Optional[TransferClientConfig] = None,
    ) -> "capo_transfer.types.describe_agreement_response.DescribeAgreementResponse":
        """<p>Describes the agreement that's identified by the <code>AgreementId</code>.</p>

        Args:
            agreement_id: <p>A unique identifier for the agreement. This identifier is returned when you create an agreement.</p>
            server_id: <p>The server identifier that's associated with the agreement.</p>

        Raises:
            capo_transfer.errors.internal_service_error.InternalServiceError: <p>This exception is thrown when an error occurs in the Transfer Family service.</p>
            capo_transfer.errors.invalid_request_exception.InvalidRequestException: <p>This exception is thrown when the client submits a malformed request.</p>
            capo_transfer.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource is not found by the Amazon Web ServicesTransfer Family service.</p>
            capo_transfer.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request has failed because the Amazon Web ServicesTransfer Family service is not available.</p>
            capo_transfer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_transfer.types.describe_agreement_request.DescribeAgreementRequest]",
        ) -> OperationResponse[
            "capo_transfer.types.describe_agreement_response.DescribeAgreementResponse"
        ]:
            import capo_transfer._operations.transfer_service.describe_agreement

            output, http_response = (
                capo_transfer._operations.transfer_service.describe_agreement.describe_agreement(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_transfer.types.describe_agreement_request.DescribeAgreementRequest = {
            "agreement_id": agreement_id,
            "server_id": server_id,
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
        agreement_id: "capo_transfer.types.agreement_id.AgreementId",
        server_id: "capo_transfer.types.server_id.ServerId",
        *,
        config_overrides: Optional[TransferClientConfig] = None,
        description: Optional["capo_transfer.types.description.Description"] = None,
        status: Optional[
            "capo_transfer.types.agreement_status_type.AgreementStatusType"
        ] = None,
        local_profile_id: Optional["capo_transfer.types.profile_id.ProfileId"] = None,
        partner_profile_id: Optional["capo_transfer.types.profile_id.ProfileId"] = None,
        base_directory: Optional[
            "capo_transfer.types.home_directory.HomeDirectory"
        ] = None,
        access_role: Optional["capo_transfer.types.role.Role"] = None,
        preserve_filename: Optional[
            "capo_transfer.types.preserve_filename_type.PreserveFilenameType"
        ] = None,
        enforce_message_signing: Optional[
            "capo_transfer.types.enforce_message_signing_type.EnforceMessageSigningType"
        ] = None,
        custom_directories: Optional[
            "capo_transfer.types.custom_directories_type.CustomDirectoriesType"
        ] = None,
    ) -> "capo_transfer.types.update_agreement_response.UpdateAgreementResponse":
        """<p>Updates some of the parameters for an existing agreement. Provide the <code>AgreementId</code> and the <code>ServerId</code> for the agreement that you want to update, along with the new values for the parameters to update.</p> <note> <p>Specify <i>either</i> <code>BaseDirectory</code> or <code>CustomDirectories</code>, but not both. Specifying both causes the command to fail.</p> <p>If you update an agreement from using base directory to custom directories, the base directory is no longer used. Similarly, if you change from custom directories to a base directory, the custom directories are no longer used.</p> </note>

        Args:
            agreement_id: <p>A unique identifier for the agreement. This identifier is returned when you create an agreement.</p>
            server_id: <p>A system-assigned unique identifier for a server instance. This is the specific server that the agreement uses.</p>
            description: <p>To replace the existing description, provide a short description for the agreement. </p>
            status: <p>You can update the status for the agreement, either activating an inactive agreement or the reverse.</p>
            local_profile_id: <p>A unique identifier for the AS2 local profile.</p> <p>To change the local profile identifier, provide a new value here.</p>
            partner_profile_id: <p>A unique identifier for the partner profile. To change the partner profile identifier, provide a new value here.</p>
            base_directory: <p>To change the landing directory (folder) for files that are transferred, provide the bucket folder that you want to use; for example, <code>/<i>amzn-s3-demo-bucket</i>/<i>home</i>/<i>mydirectory</i> </code>.</p>
            access_role: <p>Connectors are used to send files using either the AS2 or SFTP protocol. For the access role, provide the Amazon Resource Name (ARN) of the Identity and Access Management role to use.</p> <p> <b>For AS2 connectors</b> </p> <p>With AS2, you can send files by calling <code>StartFileTransfer</code> and specifying the file paths in the request parameter, <code>SendFilePaths</code>. We use the file’s parent directory (for example, for <code>--send-file-paths /bucket/dir/file.txt</code>, parent directory is <code>/bucket/dir/</code>) to temporarily store a processed AS2 message file, store the MDN when we receive them from the partner, and write a final JSON file containing relevant metadata of the transmission. So, the <code>AccessRole</code> needs to provide read and write access to the parent directory of the file location used in the <code>StartFileTransfer</code> request. Additionally, you need to provide read and write access to the parent directory of the files that you intend to send with <code>StartFileTransfer</code>.</p> <p>If you are using Basic authentication for your AS2 connector, the access role requires the <code>secretsmanager:GetSecretValue</code> permission for the secret. If the secret is encrypted using a customer-managed key instead of the Amazon Web Services managed key in Secrets Manager, then the role also needs the <code>kms:Decrypt</code> permission for that key.</p> <p> <b>For SFTP connectors</b> </p> <p>Make sure that the access role provides read and write access to the parent directory of the file location that's used in the <code>StartFileTransfer</code> request. Additionally, make sure that the role provides <code>secretsmanager:GetSecretValue</code> permission to Secrets Manager.</p>
            preserve_filename: <p> Determines whether or not Transfer Family appends a unique string of characters to the end of the AS2 message payload filename when saving it. </p> <ul> <li> <p> <code>ENABLED</code>: the filename provided by your trading parter is preserved when the file is saved.</p> </li> <li> <p> <code>DISABLED</code> (default value): when Transfer Family saves the file, the filename is adjusted, as described in <a href="https://docs.aws.amazon.com/transfer/latest/userguide/send-as2-messages.html#file-names-as2">File names and locations</a>.</p> </li> </ul>
            enforce_message_signing: <p> Determines whether or not unsigned messages from your trading partners will be accepted. </p> <ul> <li> <p> <code>ENABLED</code>: Transfer Family rejects unsigned messages from your trading partner.</p> </li> <li> <p> <code>DISABLED</code> (default value): Transfer Family accepts unsigned messages from your trading partner.</p> </li> </ul>
            custom_directories: <p>A <code>CustomDirectoriesType</code> structure. This structure specifies custom directories for storing various AS2 message files. You can specify directories for the following types of files.</p> <ul> <li> <p>Failed files</p> </li> <li> <p>MDN files</p> </li> <li> <p>Payload files</p> </li> <li> <p>Status files</p> </li> <li> <p>Temporary files</p> </li> </ul>

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
            req: "OperationRequest[capo_transfer.types.update_agreement_request.UpdateAgreementRequest]",
        ) -> OperationResponse[
            "capo_transfer.types.update_agreement_response.UpdateAgreementResponse"
        ]:
            import capo_transfer._operations.transfer_service.update_agreement

            output, http_response = (
                capo_transfer._operations.transfer_service.update_agreement.update_agreement(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_transfer.types.update_agreement_request.UpdateAgreementRequest = {
            "agreement_id": agreement_id,
            "server_id": server_id,
        }
        if description is not None:
            input_["description"] = description
        if status is not None:
            input_["status"] = status
        if local_profile_id is not None:
            input_["local_profile_id"] = local_profile_id
        if partner_profile_id is not None:
            input_["partner_profile_id"] = partner_profile_id
        if base_directory is not None:
            input_["base_directory"] = base_directory
        if access_role is not None:
            input_["access_role"] = access_role
        if preserve_filename is not None:
            input_["preserve_filename"] = preserve_filename
        if enforce_message_signing is not None:
            input_["enforce_message_signing"] = enforce_message_signing
        if custom_directories is not None:
            input_["custom_directories"] = custom_directories

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete(
        self,
        agreement_id: "capo_transfer.types.agreement_id.AgreementId",
        server_id: "capo_transfer.types.server_id.ServerId",
        *,
        config_overrides: Optional[TransferClientConfig] = None,
    ) -> None:
        """<p>Delete the agreement that's specified in the provided <code>AgreementId</code>.</p>

        Args:
            agreement_id: <p>A unique identifier for the agreement. This identifier is returned when you create an agreement.</p>
            server_id: <p>The server identifier associated with the agreement that you are deleting.</p>

        Raises:
            capo_transfer.errors.internal_service_error.InternalServiceError: <p>This exception is thrown when an error occurs in the Transfer Family service.</p>
            capo_transfer.errors.invalid_request_exception.InvalidRequestException: <p>This exception is thrown when the client submits a malformed request.</p>
            capo_transfer.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource is not found by the Amazon Web ServicesTransfer Family service.</p>
            capo_transfer.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request has failed because the Amazon Web ServicesTransfer Family service is not available.</p>
            capo_transfer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_transfer.types.delete_agreement_request.DeleteAgreementRequest]",
        ) -> OperationResponse[None]:
            import capo_transfer._operations.transfer_service.delete_agreement

            output, http_response = (
                capo_transfer._operations.transfer_service.delete_agreement.delete_agreement(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_transfer.types.delete_agreement_request.DeleteAgreementRequest = {
            "agreement_id": agreement_id,
            "server_id": server_id,
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
        server_id: "capo_transfer.types.server_id.ServerId",
        *,
        config_overrides: Optional[TransferClientConfig] = None,
        max_results: Optional["capo_transfer.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_transfer.types.next_token.NextToken"] = None,
    ) -> "capo_transfer.types.list_agreements_response.ListAgreementsResponse":
        """<p>Returns a list of the agreements for the server that's identified by the <code>ServerId</code> that you supply. If you want to limit the results to a certain number, supply a value for the <code>MaxResults</code> parameter. If you ran the command previously and received a value for <code>NextToken</code>, you can supply that value to continue listing agreements from where you left off.</p>

        Args:
            max_results: <p>The maximum number of items to return.</p>
            next_token: <p>When you can get additional results from the <code>ListAgreements</code> call, a <code>NextToken</code> parameter is returned in the output. You can then pass in a subsequent command to the <code>NextToken</code> parameter to continue listing additional agreements.</p>
            server_id: <p>The identifier of the server for which you want a list of agreements.</p>

        Raises:
            capo_transfer.errors.internal_service_error.InternalServiceError: <p>This exception is thrown when an error occurs in the Transfer Family service.</p>
            capo_transfer.errors.invalid_next_token_exception.InvalidNextTokenException: <p>The <code>NextToken</code> parameter that was passed is invalid.</p>
            capo_transfer.errors.invalid_request_exception.InvalidRequestException: <p>This exception is thrown when the client submits a malformed request.</p>
            capo_transfer.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource is not found by the Amazon Web ServicesTransfer Family service.</p>
            capo_transfer.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request has failed because the Amazon Web ServicesTransfer Family service is not available.</p>
            capo_transfer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_transfer.types.list_agreements_request.ListAgreementsRequest]",
        ) -> OperationResponse[
            "capo_transfer.types.list_agreements_response.ListAgreementsResponse"
        ]:
            import capo_transfer._operations.transfer_service.list_agreements

            output, http_response = (
                capo_transfer._operations.transfer_service.list_agreements.list_agreements(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_transfer.types.list_agreements_request.ListAgreementsRequest = {
            "server_id": server_id
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


class AsyncAgreementResource:
    def __init__(self, service: AsyncTransferClient) -> None:
        self._service = service

    async def create(
        self,
        server_id: "capo_transfer.types.server_id.ServerId",
        local_profile_id: "capo_transfer.types.profile_id.ProfileId",
        partner_profile_id: "capo_transfer.types.profile_id.ProfileId",
        access_role: "capo_transfer.types.role.Role",
        *,
        config_overrides: Optional[AsyncTransferClientConfig] = None,
        description: Optional["capo_transfer.types.description.Description"] = None,
        base_directory: Optional[
            "capo_transfer.types.home_directory.HomeDirectory"
        ] = None,
        status: Optional[
            "capo_transfer.types.agreement_status_type.AgreementStatusType"
        ] = None,
        tags: Optional["capo_transfer.types.tags.Tags"] = None,
        preserve_filename: Optional[
            "capo_transfer.types.preserve_filename_type.PreserveFilenameType"
        ] = None,
        enforce_message_signing: Optional[
            "capo_transfer.types.enforce_message_signing_type.EnforceMessageSigningType"
        ] = None,
        custom_directories: Optional[
            "capo_transfer.types.custom_directories_type.CustomDirectoriesType"
        ] = None,
    ) -> "capo_transfer.types.create_agreement_response.CreateAgreementResponse":
        """<p>Creates an agreement. An agreement is a bilateral trading partner agreement, or partnership, between an Transfer Family server and an AS2 process. The agreement defines the file and message transfer relationship between the server and the AS2 process. To define an agreement, Transfer Family combines a server, local profile, partner profile, certificate, and other attributes.</p> <p>The partner is identified with the <code>PartnerProfileId</code>, and the AS2 process is identified with the <code>LocalProfileId</code>.</p> <note> <p>Specify <i>either</i> <code>BaseDirectory</code> or <code>CustomDirectories</code>, but not both. Specifying both causes the command to fail.</p> </note>

        Args:
            description: <p>A name or short description to identify the agreement. </p>
            server_id: <p>A system-assigned unique identifier for a server instance. This is the specific server that the agreement uses.</p>
            local_profile_id: <p>A unique identifier for the AS2 local profile.</p>
            partner_profile_id: <p>A unique identifier for the partner profile used in the agreement.</p>
            base_directory: <p>The landing directory (folder) for files transferred by using the AS2 protocol.</p> <p>A <code>BaseDirectory</code> example is <code>/<i>amzn-s3-demo-bucket</i>/home/mydirectory</code>.</p>
            access_role: <p>Connectors are used to send files using either the AS2 or SFTP protocol. For the access role, provide the Amazon Resource Name (ARN) of the Identity and Access Management role to use.</p> <p> <b>For AS2 connectors</b> </p> <p>With AS2, you can send files by calling <code>StartFileTransfer</code> and specifying the file paths in the request parameter, <code>SendFilePaths</code>. We use the file’s parent directory (for example, for <code>--send-file-paths /bucket/dir/file.txt</code>, parent directory is <code>/bucket/dir/</code>) to temporarily store a processed AS2 message file, store the MDN when we receive them from the partner, and write a final JSON file containing relevant metadata of the transmission. So, the <code>AccessRole</code> needs to provide read and write access to the parent directory of the file location used in the <code>StartFileTransfer</code> request. Additionally, you need to provide read and write access to the parent directory of the files that you intend to send with <code>StartFileTransfer</code>.</p> <p>If you are using Basic authentication for your AS2 connector, the access role requires the <code>secretsmanager:GetSecretValue</code> permission for the secret. If the secret is encrypted using a customer-managed key instead of the Amazon Web Services managed key in Secrets Manager, then the role also needs the <code>kms:Decrypt</code> permission for that key.</p> <p> <b>For SFTP connectors</b> </p> <p>Make sure that the access role provides read and write access to the parent directory of the file location that's used in the <code>StartFileTransfer</code> request. Additionally, make sure that the role provides <code>secretsmanager:GetSecretValue</code> permission to Secrets Manager.</p>
            status: <p>The status of the agreement. The agreement can be either <code>ACTIVE</code> or <code>INACTIVE</code>.</p>
            tags: <p>Key-value pairs that can be used to group and search for agreements.</p>
            preserve_filename: <p> Determines whether or not Transfer Family appends a unique string of characters to the end of the AS2 message payload filename when saving it. </p> <ul> <li> <p> <code>ENABLED</code>: the filename provided by your trading parter is preserved when the file is saved.</p> </li> <li> <p> <code>DISABLED</code> (default value): when Transfer Family saves the file, the filename is adjusted, as described in <a href="https://docs.aws.amazon.com/transfer/latest/userguide/send-as2-messages.html#file-names-as2">File names and locations</a>.</p> </li> </ul>
            enforce_message_signing: <p> Determines whether or not unsigned messages from your trading partners will be accepted. </p> <ul> <li> <p> <code>ENABLED</code>: Transfer Family rejects unsigned messages from your trading partner.</p> </li> <li> <p> <code>DISABLED</code> (default value): Transfer Family accepts unsigned messages from your trading partner.</p> </li> </ul>
            custom_directories: <p>A <code>CustomDirectoriesType</code> structure. This structure specifies custom directories for storing various AS2 message files. You can specify directories for the following types of files.</p> <ul> <li> <p>Failed files</p> </li> <li> <p>MDN files</p> </li> <li> <p>Payload files</p> </li> <li> <p>Status files</p> </li> <li> <p>Temporary files</p> </li> </ul>

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
            req: "AsyncOperationRequest[capo_transfer.types.create_agreement_request.CreateAgreementRequest]",
        ) -> AsyncOperationResponse[
            "capo_transfer.types.create_agreement_response.CreateAgreementResponse"
        ]:
            import capo_transfer._operations.transfer_service.create_agreement

            (
                output,
                http_response,
            ) = await capo_transfer._operations.transfer_service.create_agreement.async_create_agreement(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_transfer.types.create_agreement_request.CreateAgreementRequest = {
            "server_id": server_id,
            "local_profile_id": local_profile_id,
            "partner_profile_id": partner_profile_id,
            "access_role": access_role,
        }
        if description is not None:
            input_["description"] = description
        if base_directory is not None:
            input_["base_directory"] = base_directory
        if status is not None:
            input_["status"] = status
        if tags is not None:
            input_["tags"] = tags
        if preserve_filename is not None:
            input_["preserve_filename"] = preserve_filename
        if enforce_message_signing is not None:
            input_["enforce_message_signing"] = enforce_message_signing
        if custom_directories is not None:
            input_["custom_directories"] = custom_directories

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def read(
        self,
        agreement_id: "capo_transfer.types.agreement_id.AgreementId",
        server_id: "capo_transfer.types.server_id.ServerId",
        *,
        config_overrides: Optional[AsyncTransferClientConfig] = None,
    ) -> "capo_transfer.types.describe_agreement_response.DescribeAgreementResponse":
        """<p>Describes the agreement that's identified by the <code>AgreementId</code>.</p>

        Args:
            agreement_id: <p>A unique identifier for the agreement. This identifier is returned when you create an agreement.</p>
            server_id: <p>The server identifier that's associated with the agreement.</p>

        Raises:
            capo_transfer.errors.internal_service_error.InternalServiceError: <p>This exception is thrown when an error occurs in the Transfer Family service.</p>
            capo_transfer.errors.invalid_request_exception.InvalidRequestException: <p>This exception is thrown when the client submits a malformed request.</p>
            capo_transfer.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource is not found by the Amazon Web ServicesTransfer Family service.</p>
            capo_transfer.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request has failed because the Amazon Web ServicesTransfer Family service is not available.</p>
            capo_transfer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_transfer.types.describe_agreement_request.DescribeAgreementRequest]",
        ) -> AsyncOperationResponse[
            "capo_transfer.types.describe_agreement_response.DescribeAgreementResponse"
        ]:
            import capo_transfer._operations.transfer_service.describe_agreement

            (
                output,
                http_response,
            ) = await capo_transfer._operations.transfer_service.describe_agreement.async_describe_agreement(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_transfer.types.describe_agreement_request.DescribeAgreementRequest = {
            "agreement_id": agreement_id,
            "server_id": server_id,
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
        agreement_id: "capo_transfer.types.agreement_id.AgreementId",
        server_id: "capo_transfer.types.server_id.ServerId",
        *,
        config_overrides: Optional[AsyncTransferClientConfig] = None,
        description: Optional["capo_transfer.types.description.Description"] = None,
        status: Optional[
            "capo_transfer.types.agreement_status_type.AgreementStatusType"
        ] = None,
        local_profile_id: Optional["capo_transfer.types.profile_id.ProfileId"] = None,
        partner_profile_id: Optional["capo_transfer.types.profile_id.ProfileId"] = None,
        base_directory: Optional[
            "capo_transfer.types.home_directory.HomeDirectory"
        ] = None,
        access_role: Optional["capo_transfer.types.role.Role"] = None,
        preserve_filename: Optional[
            "capo_transfer.types.preserve_filename_type.PreserveFilenameType"
        ] = None,
        enforce_message_signing: Optional[
            "capo_transfer.types.enforce_message_signing_type.EnforceMessageSigningType"
        ] = None,
        custom_directories: Optional[
            "capo_transfer.types.custom_directories_type.CustomDirectoriesType"
        ] = None,
    ) -> "capo_transfer.types.update_agreement_response.UpdateAgreementResponse":
        """<p>Updates some of the parameters for an existing agreement. Provide the <code>AgreementId</code> and the <code>ServerId</code> for the agreement that you want to update, along with the new values for the parameters to update.</p> <note> <p>Specify <i>either</i> <code>BaseDirectory</code> or <code>CustomDirectories</code>, but not both. Specifying both causes the command to fail.</p> <p>If you update an agreement from using base directory to custom directories, the base directory is no longer used. Similarly, if you change from custom directories to a base directory, the custom directories are no longer used.</p> </note>

        Args:
            agreement_id: <p>A unique identifier for the agreement. This identifier is returned when you create an agreement.</p>
            server_id: <p>A system-assigned unique identifier for a server instance. This is the specific server that the agreement uses.</p>
            description: <p>To replace the existing description, provide a short description for the agreement. </p>
            status: <p>You can update the status for the agreement, either activating an inactive agreement or the reverse.</p>
            local_profile_id: <p>A unique identifier for the AS2 local profile.</p> <p>To change the local profile identifier, provide a new value here.</p>
            partner_profile_id: <p>A unique identifier for the partner profile. To change the partner profile identifier, provide a new value here.</p>
            base_directory: <p>To change the landing directory (folder) for files that are transferred, provide the bucket folder that you want to use; for example, <code>/<i>amzn-s3-demo-bucket</i>/<i>home</i>/<i>mydirectory</i> </code>.</p>
            access_role: <p>Connectors are used to send files using either the AS2 or SFTP protocol. For the access role, provide the Amazon Resource Name (ARN) of the Identity and Access Management role to use.</p> <p> <b>For AS2 connectors</b> </p> <p>With AS2, you can send files by calling <code>StartFileTransfer</code> and specifying the file paths in the request parameter, <code>SendFilePaths</code>. We use the file’s parent directory (for example, for <code>--send-file-paths /bucket/dir/file.txt</code>, parent directory is <code>/bucket/dir/</code>) to temporarily store a processed AS2 message file, store the MDN when we receive them from the partner, and write a final JSON file containing relevant metadata of the transmission. So, the <code>AccessRole</code> needs to provide read and write access to the parent directory of the file location used in the <code>StartFileTransfer</code> request. Additionally, you need to provide read and write access to the parent directory of the files that you intend to send with <code>StartFileTransfer</code>.</p> <p>If you are using Basic authentication for your AS2 connector, the access role requires the <code>secretsmanager:GetSecretValue</code> permission for the secret. If the secret is encrypted using a customer-managed key instead of the Amazon Web Services managed key in Secrets Manager, then the role also needs the <code>kms:Decrypt</code> permission for that key.</p> <p> <b>For SFTP connectors</b> </p> <p>Make sure that the access role provides read and write access to the parent directory of the file location that's used in the <code>StartFileTransfer</code> request. Additionally, make sure that the role provides <code>secretsmanager:GetSecretValue</code> permission to Secrets Manager.</p>
            preserve_filename: <p> Determines whether or not Transfer Family appends a unique string of characters to the end of the AS2 message payload filename when saving it. </p> <ul> <li> <p> <code>ENABLED</code>: the filename provided by your trading parter is preserved when the file is saved.</p> </li> <li> <p> <code>DISABLED</code> (default value): when Transfer Family saves the file, the filename is adjusted, as described in <a href="https://docs.aws.amazon.com/transfer/latest/userguide/send-as2-messages.html#file-names-as2">File names and locations</a>.</p> </li> </ul>
            enforce_message_signing: <p> Determines whether or not unsigned messages from your trading partners will be accepted. </p> <ul> <li> <p> <code>ENABLED</code>: Transfer Family rejects unsigned messages from your trading partner.</p> </li> <li> <p> <code>DISABLED</code> (default value): Transfer Family accepts unsigned messages from your trading partner.</p> </li> </ul>
            custom_directories: <p>A <code>CustomDirectoriesType</code> structure. This structure specifies custom directories for storing various AS2 message files. You can specify directories for the following types of files.</p> <ul> <li> <p>Failed files</p> </li> <li> <p>MDN files</p> </li> <li> <p>Payload files</p> </li> <li> <p>Status files</p> </li> <li> <p>Temporary files</p> </li> </ul>

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
            req: "AsyncOperationRequest[capo_transfer.types.update_agreement_request.UpdateAgreementRequest]",
        ) -> AsyncOperationResponse[
            "capo_transfer.types.update_agreement_response.UpdateAgreementResponse"
        ]:
            import capo_transfer._operations.transfer_service.update_agreement

            (
                output,
                http_response,
            ) = await capo_transfer._operations.transfer_service.update_agreement.async_update_agreement(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_transfer.types.update_agreement_request.UpdateAgreementRequest = {
            "agreement_id": agreement_id,
            "server_id": server_id,
        }
        if description is not None:
            input_["description"] = description
        if status is not None:
            input_["status"] = status
        if local_profile_id is not None:
            input_["local_profile_id"] = local_profile_id
        if partner_profile_id is not None:
            input_["partner_profile_id"] = partner_profile_id
        if base_directory is not None:
            input_["base_directory"] = base_directory
        if access_role is not None:
            input_["access_role"] = access_role
        if preserve_filename is not None:
            input_["preserve_filename"] = preserve_filename
        if enforce_message_signing is not None:
            input_["enforce_message_signing"] = enforce_message_signing
        if custom_directories is not None:
            input_["custom_directories"] = custom_directories

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete(
        self,
        agreement_id: "capo_transfer.types.agreement_id.AgreementId",
        server_id: "capo_transfer.types.server_id.ServerId",
        *,
        config_overrides: Optional[AsyncTransferClientConfig] = None,
    ) -> None:
        """<p>Delete the agreement that's specified in the provided <code>AgreementId</code>.</p>

        Args:
            agreement_id: <p>A unique identifier for the agreement. This identifier is returned when you create an agreement.</p>
            server_id: <p>The server identifier associated with the agreement that you are deleting.</p>

        Raises:
            capo_transfer.errors.internal_service_error.InternalServiceError: <p>This exception is thrown when an error occurs in the Transfer Family service.</p>
            capo_transfer.errors.invalid_request_exception.InvalidRequestException: <p>This exception is thrown when the client submits a malformed request.</p>
            capo_transfer.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource is not found by the Amazon Web ServicesTransfer Family service.</p>
            capo_transfer.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request has failed because the Amazon Web ServicesTransfer Family service is not available.</p>
            capo_transfer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_transfer.types.delete_agreement_request.DeleteAgreementRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_transfer._operations.transfer_service.delete_agreement

            (
                output,
                http_response,
            ) = await capo_transfer._operations.transfer_service.delete_agreement.async_delete_agreement(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_transfer.types.delete_agreement_request.DeleteAgreementRequest = {
            "agreement_id": agreement_id,
            "server_id": server_id,
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
        server_id: "capo_transfer.types.server_id.ServerId",
        *,
        config_overrides: Optional[AsyncTransferClientConfig] = None,
        max_results: Optional["capo_transfer.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_transfer.types.next_token.NextToken"] = None,
    ) -> "capo_transfer.types.list_agreements_response.ListAgreementsResponse":
        """<p>Returns a list of the agreements for the server that's identified by the <code>ServerId</code> that you supply. If you want to limit the results to a certain number, supply a value for the <code>MaxResults</code> parameter. If you ran the command previously and received a value for <code>NextToken</code>, you can supply that value to continue listing agreements from where you left off.</p>

        Args:
            max_results: <p>The maximum number of items to return.</p>
            next_token: <p>When you can get additional results from the <code>ListAgreements</code> call, a <code>NextToken</code> parameter is returned in the output. You can then pass in a subsequent command to the <code>NextToken</code> parameter to continue listing additional agreements.</p>
            server_id: <p>The identifier of the server for which you want a list of agreements.</p>

        Raises:
            capo_transfer.errors.internal_service_error.InternalServiceError: <p>This exception is thrown when an error occurs in the Transfer Family service.</p>
            capo_transfer.errors.invalid_next_token_exception.InvalidNextTokenException: <p>The <code>NextToken</code> parameter that was passed is invalid.</p>
            capo_transfer.errors.invalid_request_exception.InvalidRequestException: <p>This exception is thrown when the client submits a malformed request.</p>
            capo_transfer.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource is not found by the Amazon Web ServicesTransfer Family service.</p>
            capo_transfer.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request has failed because the Amazon Web ServicesTransfer Family service is not available.</p>
            capo_transfer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_transfer.types.list_agreements_request.ListAgreementsRequest]",
        ) -> AsyncOperationResponse[
            "capo_transfer.types.list_agreements_response.ListAgreementsResponse"
        ]:
            import capo_transfer._operations.transfer_service.list_agreements

            (
                output,
                http_response,
            ) = await capo_transfer._operations.transfer_service.list_agreements.async_list_agreements(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_transfer.types.list_agreements_request.ListAgreementsRequest = {
            "server_id": server_id
        }
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
