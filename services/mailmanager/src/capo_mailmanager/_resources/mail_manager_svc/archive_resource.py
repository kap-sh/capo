from __future__ import annotations

import uuid
from typing import TYPE_CHECKING, Optional

from capo_mailmanager._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_mailmanager.types.archive
    import capo_mailmanager.types.archive_id_string
    import capo_mailmanager.types.archive_name_string
    import capo_mailmanager.types.archive_retention
    import capo_mailmanager.types.create_archive_request
    import capo_mailmanager.types.create_archive_response
    import capo_mailmanager.types.delete_archive_request
    import capo_mailmanager.types.delete_archive_response
    import capo_mailmanager.types.get_archive_request
    import capo_mailmanager.types.get_archive_response
    import capo_mailmanager.types.idempotency_token
    import capo_mailmanager.types.kms_key_arn
    import capo_mailmanager.types.list_archives_request
    import capo_mailmanager.types.list_archives_response
    import capo_mailmanager.types.page_size
    import capo_mailmanager.types.pagination_token
    import capo_mailmanager.types.tag_list
    import capo_mailmanager.types.update_archive_request
    import capo_mailmanager.types.update_archive_response
    from capo_mailmanager._services.async_mail_manager import (
        AsyncMailManagerClient,
        AsyncMailManagerClientConfig,
    )
    from capo_mailmanager._services.mail_manager import (
        MailManagerClient,
        MailManagerClientConfig,
    )


class ArchiveResource:
    def __init__(self, service: MailManagerClient) -> None:
        self._service = service

    def create(
        self,
        archive_name: "capo_mailmanager.types.archive_name_string.ArchiveNameString",
        *,
        config_overrides: Optional[MailManagerClientConfig] = None,
        client_token: Optional[
            "capo_mailmanager.types.idempotency_token.IdempotencyToken"
        ] = None,
        retention: Optional[
            "capo_mailmanager.types.archive_retention.ArchiveRetention"
        ] = None,
        kms_key_arn: Optional["capo_mailmanager.types.kms_key_arn.KmsKeyArn"] = None,
        tags: Optional["capo_mailmanager.types.tag_list.TagList"] = None,
    ) -> "capo_mailmanager.types.create_archive_response.CreateArchiveResponse":
        """<p>Creates a new email archive resource for storing and retaining emails.</p>

        Args:
            client_token: <p>A unique token Amazon SES uses to recognize retries of this request.</p>
            archive_name: <p>A unique name for the new archive.</p>
            retention: <p>The period for retaining emails in the archive before automatic deletion.</p>
            kms_key_arn: <p>The Amazon Resource Name (ARN) of the KMS key for encrypting emails in the archive.</p>
            tags: <p>The tags used to organize, track, or control access for the resource. For example, { "tags": {"key1":"value1", "key2":"value2"} }.</p>

        Raises:
            capo_mailmanager.errors.access_denied_exception.AccessDeniedException: <p>Occurs when a user is denied access to a specific resource or action.</p>
            capo_mailmanager.errors.conflict_exception.ConflictException: <p>The request configuration has conflicts. For details, see the accompanying error message.</p>
            capo_mailmanager.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Occurs when an operation exceeds a predefined service quota or limit.</p>
            capo_mailmanager.errors.throttling_exception.ThrottlingException: <p>Occurs when a service's request rate limit is exceeded, resulting in throttling of further requests.</p>
            capo_mailmanager.errors.validation_exception.ValidationException: <p>The request validation has failed. For details, see the accompanying error message.</p>
            capo_mailmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mailmanager.types.create_archive_request.CreateArchiveRequest]",
        ) -> OperationResponse[
            "capo_mailmanager.types.create_archive_response.CreateArchiveResponse"
        ]:
            import capo_mailmanager._operations.mail_manager_svc.create_archive

            output, http_response = (
                capo_mailmanager._operations.mail_manager_svc.create_archive.create_archive(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_mailmanager.types.create_archive_request.CreateArchiveRequest = {
            "archive_name": archive_name
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if retention is not None:
            input_["retention"] = retention
        if kms_key_arn is not None:
            input_["kms_key_arn"] = kms_key_arn
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
        archive_id: "capo_mailmanager.types.archive_id_string.ArchiveIdString",
        *,
        config_overrides: Optional[MailManagerClientConfig] = None,
    ) -> "capo_mailmanager.types.get_archive_response.GetArchiveResponse":
        """<p>Retrieves the full details and current state of a specified email archive.</p>

        Args:
            archive_id: <p>The identifier of the archive to retrieve.</p>

        Raises:
            capo_mailmanager.errors.access_denied_exception.AccessDeniedException: <p>Occurs when a user is denied access to a specific resource or action.</p>
            capo_mailmanager.errors.resource_not_found_exception.ResourceNotFoundException: <p>Occurs when a requested resource is not found.</p>
            capo_mailmanager.errors.throttling_exception.ThrottlingException: <p>Occurs when a service's request rate limit is exceeded, resulting in throttling of further requests.</p>
            capo_mailmanager.errors.validation_exception.ValidationException: <p>The request validation has failed. For details, see the accompanying error message.</p>
            capo_mailmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mailmanager.types.get_archive_request.GetArchiveRequest]",
        ) -> OperationResponse[
            "capo_mailmanager.types.get_archive_response.GetArchiveResponse"
        ]:
            import capo_mailmanager._operations.mail_manager_svc.get_archive

            output, http_response = (
                capo_mailmanager._operations.mail_manager_svc.get_archive.get_archive(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_mailmanager.types.get_archive_request.GetArchiveRequest = {
            "archive_id": archive_id
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
        archive_id: "capo_mailmanager.types.archive_id_string.ArchiveIdString",
        *,
        config_overrides: Optional[MailManagerClientConfig] = None,
        archive_name: Optional[
            "capo_mailmanager.types.archive_name_string.ArchiveNameString"
        ] = None,
        retention: Optional[
            "capo_mailmanager.types.archive_retention.ArchiveRetention"
        ] = None,
    ) -> "capo_mailmanager.types.update_archive_response.UpdateArchiveResponse":
        """<p>Updates the attributes of an existing email archive.</p>

        Args:
            archive_id: <p>The identifier of the archive to update.</p>
            archive_name: <p>A new, unique name for the archive.</p>
            retention: <p>A new retention period for emails in the archive.</p>

        Raises:
            capo_mailmanager.errors.access_denied_exception.AccessDeniedException: <p>Occurs when a user is denied access to a specific resource or action.</p>
            capo_mailmanager.errors.conflict_exception.ConflictException: <p>The request configuration has conflicts. For details, see the accompanying error message.</p>
            capo_mailmanager.errors.resource_not_found_exception.ResourceNotFoundException: <p>Occurs when a requested resource is not found.</p>
            capo_mailmanager.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Occurs when an operation exceeds a predefined service quota or limit.</p>
            capo_mailmanager.errors.throttling_exception.ThrottlingException: <p>Occurs when a service's request rate limit is exceeded, resulting in throttling of further requests.</p>
            capo_mailmanager.errors.validation_exception.ValidationException: <p>The request validation has failed. For details, see the accompanying error message.</p>
            capo_mailmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mailmanager.types.update_archive_request.UpdateArchiveRequest]",
        ) -> OperationResponse[
            "capo_mailmanager.types.update_archive_response.UpdateArchiveResponse"
        ]:
            import capo_mailmanager._operations.mail_manager_svc.update_archive

            output, http_response = (
                capo_mailmanager._operations.mail_manager_svc.update_archive.update_archive(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_mailmanager.types.update_archive_request.UpdateArchiveRequest = {
            "archive_id": archive_id
        }
        if archive_name is not None:
            input_["archive_name"] = archive_name
        if retention is not None:
            input_["retention"] = retention

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete(
        self,
        archive_id: "capo_mailmanager.types.archive_id_string.ArchiveIdString",
        *,
        config_overrides: Optional[MailManagerClientConfig] = None,
    ) -> "capo_mailmanager.types.delete_archive_response.DeleteArchiveResponse":
        """<p>Initiates deletion of an email archive. This changes the archive state to pending deletion. In this state, no new emails can be added, and existing archived emails become inaccessible (search, export, download). The archive and all of its contents will be permanently deleted 30 days after entering the pending deletion state, regardless of the configured retention period. </p>

        Args:
            archive_id: <p>The identifier of the archive to delete.</p>

        Raises:
            capo_mailmanager.errors.access_denied_exception.AccessDeniedException: <p>Occurs when a user is denied access to a specific resource or action.</p>
            capo_mailmanager.errors.conflict_exception.ConflictException: <p>The request configuration has conflicts. For details, see the accompanying error message.</p>
            capo_mailmanager.errors.throttling_exception.ThrottlingException: <p>Occurs when a service's request rate limit is exceeded, resulting in throttling of further requests.</p>
            capo_mailmanager.errors.validation_exception.ValidationException: <p>The request validation has failed. For details, see the accompanying error message.</p>
            capo_mailmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mailmanager.types.delete_archive_request.DeleteArchiveRequest]",
        ) -> OperationResponse[
            "capo_mailmanager.types.delete_archive_response.DeleteArchiveResponse"
        ]:
            import capo_mailmanager._operations.mail_manager_svc.delete_archive

            output, http_response = (
                capo_mailmanager._operations.mail_manager_svc.delete_archive.delete_archive(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_mailmanager.types.delete_archive_request.DeleteArchiveRequest = {
            "archive_id": archive_id
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
        config_overrides: Optional[MailManagerClientConfig] = None,
        next_token: Optional[
            "capo_mailmanager.types.pagination_token.PaginationToken"
        ] = None,
        page_size: Optional["capo_mailmanager.types.page_size.PageSize"] = None,
    ) -> "capo_mailmanager.types.list_archives_response.ListArchivesResponse":
        """<p>Returns a list of all email archives in your account.</p>

        Args:
            next_token: <p>If NextToken is returned, there are more results available. The value of NextToken is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. </p>
            page_size: <p>The maximum number of archives that are returned per call. You can use NextToken to obtain further pages of archives. </p>

        Raises:
            capo_mailmanager.errors.access_denied_exception.AccessDeniedException: <p>Occurs when a user is denied access to a specific resource or action.</p>
            capo_mailmanager.errors.throttling_exception.ThrottlingException: <p>Occurs when a service's request rate limit is exceeded, resulting in throttling of further requests.</p>
            capo_mailmanager.errors.validation_exception.ValidationException: <p>The request validation has failed. For details, see the accompanying error message.</p>
            capo_mailmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mailmanager.types.list_archives_request.ListArchivesRequest]",
        ) -> OperationResponse[
            "capo_mailmanager.types.list_archives_response.ListArchivesResponse"
        ]:
            import capo_mailmanager._operations.mail_manager_svc.list_archives

            output, http_response = (
                capo_mailmanager._operations.mail_manager_svc.list_archives.list_archives(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_mailmanager.types.list_archives_request.ListArchivesRequest = {}
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


class AsyncArchiveResource:
    def __init__(self, service: AsyncMailManagerClient) -> None:
        self._service = service

    async def create(
        self,
        archive_name: "capo_mailmanager.types.archive_name_string.ArchiveNameString",
        *,
        config_overrides: Optional[AsyncMailManagerClientConfig] = None,
        client_token: Optional[
            "capo_mailmanager.types.idempotency_token.IdempotencyToken"
        ] = None,
        retention: Optional[
            "capo_mailmanager.types.archive_retention.ArchiveRetention"
        ] = None,
        kms_key_arn: Optional["capo_mailmanager.types.kms_key_arn.KmsKeyArn"] = None,
        tags: Optional["capo_mailmanager.types.tag_list.TagList"] = None,
    ) -> "capo_mailmanager.types.create_archive_response.CreateArchiveResponse":
        """<p>Creates a new email archive resource for storing and retaining emails.</p>

        Args:
            client_token: <p>A unique token Amazon SES uses to recognize retries of this request.</p>
            archive_name: <p>A unique name for the new archive.</p>
            retention: <p>The period for retaining emails in the archive before automatic deletion.</p>
            kms_key_arn: <p>The Amazon Resource Name (ARN) of the KMS key for encrypting emails in the archive.</p>
            tags: <p>The tags used to organize, track, or control access for the resource. For example, { "tags": {"key1":"value1", "key2":"value2"} }.</p>

        Raises:
            capo_mailmanager.errors.access_denied_exception.AccessDeniedException: <p>Occurs when a user is denied access to a specific resource or action.</p>
            capo_mailmanager.errors.conflict_exception.ConflictException: <p>The request configuration has conflicts. For details, see the accompanying error message.</p>
            capo_mailmanager.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Occurs when an operation exceeds a predefined service quota or limit.</p>
            capo_mailmanager.errors.throttling_exception.ThrottlingException: <p>Occurs when a service's request rate limit is exceeded, resulting in throttling of further requests.</p>
            capo_mailmanager.errors.validation_exception.ValidationException: <p>The request validation has failed. For details, see the accompanying error message.</p>
            capo_mailmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mailmanager.types.create_archive_request.CreateArchiveRequest]",
        ) -> AsyncOperationResponse[
            "capo_mailmanager.types.create_archive_response.CreateArchiveResponse"
        ]:
            import capo_mailmanager._operations.mail_manager_svc.create_archive

            (
                output,
                http_response,
            ) = await capo_mailmanager._operations.mail_manager_svc.create_archive.async_create_archive(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_mailmanager.types.create_archive_request.CreateArchiveRequest = {
            "archive_name": archive_name
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if retention is not None:
            input_["retention"] = retention
        if kms_key_arn is not None:
            input_["kms_key_arn"] = kms_key_arn
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
        archive_id: "capo_mailmanager.types.archive_id_string.ArchiveIdString",
        *,
        config_overrides: Optional[AsyncMailManagerClientConfig] = None,
    ) -> "capo_mailmanager.types.get_archive_response.GetArchiveResponse":
        """<p>Retrieves the full details and current state of a specified email archive.</p>

        Args:
            archive_id: <p>The identifier of the archive to retrieve.</p>

        Raises:
            capo_mailmanager.errors.access_denied_exception.AccessDeniedException: <p>Occurs when a user is denied access to a specific resource or action.</p>
            capo_mailmanager.errors.resource_not_found_exception.ResourceNotFoundException: <p>Occurs when a requested resource is not found.</p>
            capo_mailmanager.errors.throttling_exception.ThrottlingException: <p>Occurs when a service's request rate limit is exceeded, resulting in throttling of further requests.</p>
            capo_mailmanager.errors.validation_exception.ValidationException: <p>The request validation has failed. For details, see the accompanying error message.</p>
            capo_mailmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mailmanager.types.get_archive_request.GetArchiveRequest]",
        ) -> AsyncOperationResponse[
            "capo_mailmanager.types.get_archive_response.GetArchiveResponse"
        ]:
            import capo_mailmanager._operations.mail_manager_svc.get_archive

            (
                output,
                http_response,
            ) = await capo_mailmanager._operations.mail_manager_svc.get_archive.async_get_archive(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_mailmanager.types.get_archive_request.GetArchiveRequest = {
            "archive_id": archive_id
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
        archive_id: "capo_mailmanager.types.archive_id_string.ArchiveIdString",
        *,
        config_overrides: Optional[AsyncMailManagerClientConfig] = None,
        archive_name: Optional[
            "capo_mailmanager.types.archive_name_string.ArchiveNameString"
        ] = None,
        retention: Optional[
            "capo_mailmanager.types.archive_retention.ArchiveRetention"
        ] = None,
    ) -> "capo_mailmanager.types.update_archive_response.UpdateArchiveResponse":
        """<p>Updates the attributes of an existing email archive.</p>

        Args:
            archive_id: <p>The identifier of the archive to update.</p>
            archive_name: <p>A new, unique name for the archive.</p>
            retention: <p>A new retention period for emails in the archive.</p>

        Raises:
            capo_mailmanager.errors.access_denied_exception.AccessDeniedException: <p>Occurs when a user is denied access to a specific resource or action.</p>
            capo_mailmanager.errors.conflict_exception.ConflictException: <p>The request configuration has conflicts. For details, see the accompanying error message.</p>
            capo_mailmanager.errors.resource_not_found_exception.ResourceNotFoundException: <p>Occurs when a requested resource is not found.</p>
            capo_mailmanager.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Occurs when an operation exceeds a predefined service quota or limit.</p>
            capo_mailmanager.errors.throttling_exception.ThrottlingException: <p>Occurs when a service's request rate limit is exceeded, resulting in throttling of further requests.</p>
            capo_mailmanager.errors.validation_exception.ValidationException: <p>The request validation has failed. For details, see the accompanying error message.</p>
            capo_mailmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mailmanager.types.update_archive_request.UpdateArchiveRequest]",
        ) -> AsyncOperationResponse[
            "capo_mailmanager.types.update_archive_response.UpdateArchiveResponse"
        ]:
            import capo_mailmanager._operations.mail_manager_svc.update_archive

            (
                output,
                http_response,
            ) = await capo_mailmanager._operations.mail_manager_svc.update_archive.async_update_archive(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_mailmanager.types.update_archive_request.UpdateArchiveRequest = {
            "archive_id": archive_id
        }
        if archive_name is not None:
            input_["archive_name"] = archive_name
        if retention is not None:
            input_["retention"] = retention

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete(
        self,
        archive_id: "capo_mailmanager.types.archive_id_string.ArchiveIdString",
        *,
        config_overrides: Optional[AsyncMailManagerClientConfig] = None,
    ) -> "capo_mailmanager.types.delete_archive_response.DeleteArchiveResponse":
        """<p>Initiates deletion of an email archive. This changes the archive state to pending deletion. In this state, no new emails can be added, and existing archived emails become inaccessible (search, export, download). The archive and all of its contents will be permanently deleted 30 days after entering the pending deletion state, regardless of the configured retention period. </p>

        Args:
            archive_id: <p>The identifier of the archive to delete.</p>

        Raises:
            capo_mailmanager.errors.access_denied_exception.AccessDeniedException: <p>Occurs when a user is denied access to a specific resource or action.</p>
            capo_mailmanager.errors.conflict_exception.ConflictException: <p>The request configuration has conflicts. For details, see the accompanying error message.</p>
            capo_mailmanager.errors.throttling_exception.ThrottlingException: <p>Occurs when a service's request rate limit is exceeded, resulting in throttling of further requests.</p>
            capo_mailmanager.errors.validation_exception.ValidationException: <p>The request validation has failed. For details, see the accompanying error message.</p>
            capo_mailmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mailmanager.types.delete_archive_request.DeleteArchiveRequest]",
        ) -> AsyncOperationResponse[
            "capo_mailmanager.types.delete_archive_response.DeleteArchiveResponse"
        ]:
            import capo_mailmanager._operations.mail_manager_svc.delete_archive

            (
                output,
                http_response,
            ) = await capo_mailmanager._operations.mail_manager_svc.delete_archive.async_delete_archive(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_mailmanager.types.delete_archive_request.DeleteArchiveRequest = {
            "archive_id": archive_id
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
        config_overrides: Optional[AsyncMailManagerClientConfig] = None,
        next_token: Optional[
            "capo_mailmanager.types.pagination_token.PaginationToken"
        ] = None,
        page_size: Optional["capo_mailmanager.types.page_size.PageSize"] = None,
    ) -> "capo_mailmanager.types.list_archives_response.ListArchivesResponse":
        """<p>Returns a list of all email archives in your account.</p>

        Args:
            next_token: <p>If NextToken is returned, there are more results available. The value of NextToken is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. </p>
            page_size: <p>The maximum number of archives that are returned per call. You can use NextToken to obtain further pages of archives. </p>

        Raises:
            capo_mailmanager.errors.access_denied_exception.AccessDeniedException: <p>Occurs when a user is denied access to a specific resource or action.</p>
            capo_mailmanager.errors.throttling_exception.ThrottlingException: <p>Occurs when a service's request rate limit is exceeded, resulting in throttling of further requests.</p>
            capo_mailmanager.errors.validation_exception.ValidationException: <p>The request validation has failed. For details, see the accompanying error message.</p>
            capo_mailmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mailmanager.types.list_archives_request.ListArchivesRequest]",
        ) -> AsyncOperationResponse[
            "capo_mailmanager.types.list_archives_response.ListArchivesResponse"
        ]:
            import capo_mailmanager._operations.mail_manager_svc.list_archives

            (
                output,
                http_response,
            ) = await capo_mailmanager._operations.mail_manager_svc.list_archives.async_list_archives(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_mailmanager.types.list_archives_request.ListArchivesRequest = {}
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
