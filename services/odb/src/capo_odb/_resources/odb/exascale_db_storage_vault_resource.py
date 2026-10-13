from __future__ import annotations

import uuid
from typing import TYPE_CHECKING, Optional

from capo_odb._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationLogging,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_odb.types.create_exascale_db_storage_vault_input
    import capo_odb.types.create_exascale_db_storage_vault_output
    import capo_odb.types.delete_exascale_db_storage_vault_input
    import capo_odb.types.delete_exascale_db_storage_vault_output
    import capo_odb.types.exascale_db_storage_vault_summary
    import capo_odb.types.general_input_string
    import capo_odb.types.get_exascale_db_storage_vault_input
    import capo_odb.types.get_exascale_db_storage_vault_output
    import capo_odb.types.list_exascale_db_storage_vaults_input
    import capo_odb.types.list_exascale_db_storage_vaults_output
    import capo_odb.types.request_tag_map
    import capo_odb.types.resource_display_name
    import capo_odb.types.resource_id_or_arn
    import capo_odb.types.update_exascale_db_storage_vault_input
    import capo_odb.types.update_exascale_db_storage_vault_output
    from capo_odb._services.async_odb import AsyncodbClient, AsyncodbClientConfig
    from capo_odb._services.odb import odbClient, odbClientConfig


class ExascaleDbStorageVaultResource:
    def __init__(self, service: odbClient) -> None:
        self._service = service

    def create(
        self,
        display_name: "capo_odb.types.resource_display_name.ResourceDisplayName",
        high_capacity_database_storage_total_size_in_g_bs: int,
        *,
        config_overrides: Optional[odbClientConfig] = None,
        additional_flash_cache_in_percent: Optional[int] = None,
        autoscale_limit_in_g_bs: Optional[int] = None,
        availability_zone_id: Optional[str] = None,
        availability_zone: Optional[str] = None,
        description: Optional[str] = None,
        is_autoscale_enabled: Optional[bool] = None,
        tags: Optional["capo_odb.types.request_tag_map.RequestTagMap"] = None,
        time_zone: Optional[str] = None,
        client_token: Optional[
            "capo_odb.types.general_input_string.GeneralInputString"
        ] = None,
    ) -> "capo_odb.types.create_exascale_db_storage_vault_output.CreateExascaleDbStorageVaultOutput":
        """<p>Creates an Exascale storage vault.</p>

        Args:
            display_name: <p>A user-friendly name for the Exascale storage vault.</p>
            high_capacity_database_storage_total_size_in_g_bs: <p>The total size of the high-capacity database storage, in gigabytes (GB), for the Exascale storage vault.</p>
            additional_flash_cache_in_percent: <p>The additional flash cache percentage for the Exascale storage vault.</p>
            autoscale_limit_in_g_bs: <p>The autoscale limit in gigabytes (GB) for the Exascale storage vault.</p>
            availability_zone_id: <p>The Availability Zone ID for the Exascale storage vault.</p>
            availability_zone: <p>The Availability Zone for the Exascale storage vault.</p>
            description: <p>A description of the Exascale storage vault.</p>
            is_autoscale_enabled: <p>Specifies whether autoscaling is enabled for the Exascale storage vault.</p>
            tags: <p>The list of resource tags to apply to the Exascale storage vault.</p>
            time_zone: <p>The time zone for the Exascale storage vault.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure that the operation completes no more than one time. If you submit the same request twice with the same client token, the service ignores the second request and returns the result of the first. If you don't specify a client token, the AWS SDK automatically generates one. The client token is valid for up to 24 hours after it's first used.</p>

        Raises:
            capo_odb.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action. Make sure you have the required permissions and try again.</p>
            capo_odb.errors.conflict_exception.ConflictException: <p>Occurs when a conflict with the current status of your resource. Fix any inconsistencies with your resource and try again.</p>
            capo_odb.errors.internal_server_exception.InternalServerException: <p>Occurs when there is an internal failure in the Oracle Database@Amazon Web Services service. Wait and try again.</p>
            capo_odb.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You have exceeded the service quota.</p>
            capo_odb.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_odb.errors.validation_exception.ValidationException: <p>The request has failed validation because it is missing required fields or has invalid inputs.</p>
            capo_odb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_odb.types.create_exascale_db_storage_vault_input.CreateExascaleDbStorageVaultInput]",
        ) -> OperationResponse[
            "capo_odb.types.create_exascale_db_storage_vault_output.CreateExascaleDbStorageVaultOutput"
        ]:
            import capo_odb._operations.odb.create_exascale_db_storage_vault

            output, http_response = (
                capo_odb._operations.odb.create_exascale_db_storage_vault.create_exascale_db_storage_vault(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("CreateExascaleDbStorageVault")
        )
        input_: capo_odb.types.create_exascale_db_storage_vault_input.CreateExascaleDbStorageVaultInput = {
            "display_name": display_name,
            "high_capacity_database_storage_total_size_in_g_bs": high_capacity_database_storage_total_size_in_g_bs,
        }
        if additional_flash_cache_in_percent is not None:
            input_["additional_flash_cache_in_percent"] = (
                additional_flash_cache_in_percent
            )
        if autoscale_limit_in_g_bs is not None:
            input_["autoscale_limit_in_g_bs"] = autoscale_limit_in_g_bs
        if availability_zone_id is not None:
            input_["availability_zone_id"] = availability_zone_id
        if availability_zone is not None:
            input_["availability_zone"] = availability_zone
        if description is not None:
            input_["description"] = description
        if is_autoscale_enabled is not None:
            input_["is_autoscale_enabled"] = is_autoscale_enabled
        if tags is not None:
            input_["tags"] = tags
        if time_zone is not None:
            input_["time_zone"] = time_zone
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

    def read(
        self,
        exascale_db_storage_vault_id: "capo_odb.types.resource_id_or_arn.ResourceIdOrArn",
        *,
        config_overrides: Optional[odbClientConfig] = None,
    ) -> "capo_odb.types.get_exascale_db_storage_vault_output.GetExascaleDbStorageVaultOutput":
        """<p>Returns information about the specified Exascale storage vault.</p>

        Args:
            exascale_db_storage_vault_id: <p>The unique identifier of the Exascale storage vault.</p>

        Raises:
            capo_odb.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action. Make sure you have the required permissions and try again.</p>
            capo_odb.errors.internal_server_exception.InternalServerException: <p>Occurs when there is an internal failure in the Oracle Database@Amazon Web Services service. Wait and try again.</p>
            capo_odb.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a resource that doesn't exist. Make sure you provided the correct resource and try again.</p>
            capo_odb.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_odb.errors.validation_exception.ValidationException: <p>The request has failed validation because it is missing required fields or has invalid inputs.</p>
            capo_odb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_odb.types.get_exascale_db_storage_vault_input.GetExascaleDbStorageVaultInput]",
        ) -> OperationResponse[
            "capo_odb.types.get_exascale_db_storage_vault_output.GetExascaleDbStorageVaultOutput"
        ]:
            import capo_odb._operations.odb.get_exascale_db_storage_vault

            output, http_response = (
                capo_odb._operations.odb.get_exascale_db_storage_vault.get_exascale_db_storage_vault(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetExascaleDbStorageVault")
        )
        input_: capo_odb.types.get_exascale_db_storage_vault_input.GetExascaleDbStorageVaultInput = {
            "exascale_db_storage_vault_id": exascale_db_storage_vault_id
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
        exascale_db_storage_vault_id: "capo_odb.types.resource_id_or_arn.ResourceIdOrArn",
        *,
        config_overrides: Optional[odbClientConfig] = None,
        additional_flash_cache_in_percent: Optional[int] = None,
        autoscale_limit_in_g_bs: Optional[int] = None,
        description: Optional[str] = None,
        display_name: Optional[
            "capo_odb.types.resource_display_name.ResourceDisplayName"
        ] = None,
        high_capacity_database_storage_total_size_in_g_bs: Optional[int] = None,
        is_autoscale_enabled: Optional[bool] = None,
    ) -> "capo_odb.types.update_exascale_db_storage_vault_output.UpdateExascaleDbStorageVaultOutput":
        """<p>Updates the specified Exascale storage vault.</p>

        Args:
            exascale_db_storage_vault_id: <p>The unique identifier of the Exascale storage vault to update.</p>
            additional_flash_cache_in_percent: <p>The additional flash cache percentage for the Exascale storage vault.</p>
            autoscale_limit_in_g_bs: <p>The autoscale limit in gigabytes (GB) for the Exascale storage vault.</p>
            description: <p>A new description for the Exascale storage vault.</p>
            display_name: <p>A new user-friendly name for the Exascale storage vault.</p>
            high_capacity_database_storage_total_size_in_g_bs: <p>The total size of the high-capacity database storage, in gigabytes (GB), for the Exascale storage vault.</p>
            is_autoscale_enabled: <p>Specifies whether autoscaling is enabled for the Exascale storage vault.</p>

        Raises:
            capo_odb.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action. Make sure you have the required permissions and try again.</p>
            capo_odb.errors.conflict_exception.ConflictException: <p>Occurs when a conflict with the current status of your resource. Fix any inconsistencies with your resource and try again.</p>
            capo_odb.errors.internal_server_exception.InternalServerException: <p>Occurs when there is an internal failure in the Oracle Database@Amazon Web Services service. Wait and try again.</p>
            capo_odb.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a resource that doesn't exist. Make sure you provided the correct resource and try again.</p>
            capo_odb.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_odb.errors.validation_exception.ValidationException: <p>The request has failed validation because it is missing required fields or has invalid inputs.</p>
            capo_odb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_odb.types.update_exascale_db_storage_vault_input.UpdateExascaleDbStorageVaultInput]",
        ) -> OperationResponse[
            "capo_odb.types.update_exascale_db_storage_vault_output.UpdateExascaleDbStorageVaultOutput"
        ]:
            import capo_odb._operations.odb.update_exascale_db_storage_vault

            output, http_response = (
                capo_odb._operations.odb.update_exascale_db_storage_vault.update_exascale_db_storage_vault(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("UpdateExascaleDbStorageVault")
        )
        input_: capo_odb.types.update_exascale_db_storage_vault_input.UpdateExascaleDbStorageVaultInput = {
            "exascale_db_storage_vault_id": exascale_db_storage_vault_id
        }
        if additional_flash_cache_in_percent is not None:
            input_["additional_flash_cache_in_percent"] = (
                additional_flash_cache_in_percent
            )
        if autoscale_limit_in_g_bs is not None:
            input_["autoscale_limit_in_g_bs"] = autoscale_limit_in_g_bs
        if description is not None:
            input_["description"] = description
        if display_name is not None:
            input_["display_name"] = display_name
        if high_capacity_database_storage_total_size_in_g_bs is not None:
            input_["high_capacity_database_storage_total_size_in_g_bs"] = (
                high_capacity_database_storage_total_size_in_g_bs
            )
        if is_autoscale_enabled is not None:
            input_["is_autoscale_enabled"] = is_autoscale_enabled

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete(
        self,
        exascale_db_storage_vault_id: "capo_odb.types.resource_id_or_arn.ResourceIdOrArn",
        *,
        config_overrides: Optional[odbClientConfig] = None,
    ) -> "capo_odb.types.delete_exascale_db_storage_vault_output.DeleteExascaleDbStorageVaultOutput":
        """<p>Deletes the specified Exascale storage vault.</p>

        Args:
            exascale_db_storage_vault_id: <p>The unique identifier of the Exascale storage vault to delete.</p>

        Raises:
            capo_odb.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action. Make sure you have the required permissions and try again.</p>
            capo_odb.errors.conflict_exception.ConflictException: <p>Occurs when a conflict with the current status of your resource. Fix any inconsistencies with your resource and try again.</p>
            capo_odb.errors.internal_server_exception.InternalServerException: <p>Occurs when there is an internal failure in the Oracle Database@Amazon Web Services service. Wait and try again.</p>
            capo_odb.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a resource that doesn't exist. Make sure you provided the correct resource and try again.</p>
            capo_odb.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_odb.errors.validation_exception.ValidationException: <p>The request has failed validation because it is missing required fields or has invalid inputs.</p>
            capo_odb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_odb.types.delete_exascale_db_storage_vault_input.DeleteExascaleDbStorageVaultInput]",
        ) -> OperationResponse[
            "capo_odb.types.delete_exascale_db_storage_vault_output.DeleteExascaleDbStorageVaultOutput"
        ]:
            import capo_odb._operations.odb.delete_exascale_db_storage_vault

            output, http_response = (
                capo_odb._operations.odb.delete_exascale_db_storage_vault.delete_exascale_db_storage_vault(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteExascaleDbStorageVault")
        )
        input_: capo_odb.types.delete_exascale_db_storage_vault_input.DeleteExascaleDbStorageVaultInput = {
            "exascale_db_storage_vault_id": exascale_db_storage_vault_id
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
        config_overrides: Optional[odbClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
    ) -> "capo_odb.types.list_exascale_db_storage_vaults_output.ListExascaleDbStorageVaultsOutput":
        """<p>Returns information about the Exascale storage vaults owned by your Amazon Web Services account.</p>

        Args:
            max_results: <p>The maximum number of items to return for this request. To get the next page of items, make another request with the token returned in the output.</p>
            next_token: <p>The token returned from a previous paginated request. Pagination continues from the end of the items returned by the previous request.</p>

        Raises:
            capo_odb.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action. Make sure you have the required permissions and try again.</p>
            capo_odb.errors.internal_server_exception.InternalServerException: <p>Occurs when there is an internal failure in the Oracle Database@Amazon Web Services service. Wait and try again.</p>
            capo_odb.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_odb.errors.validation_exception.ValidationException: <p>The request has failed validation because it is missing required fields or has invalid inputs.</p>
            capo_odb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_odb.types.list_exascale_db_storage_vaults_input.ListExascaleDbStorageVaultsInput]",
        ) -> OperationResponse[
            "capo_odb.types.list_exascale_db_storage_vaults_output.ListExascaleDbStorageVaultsOutput"
        ]:
            import capo_odb._operations.odb.list_exascale_db_storage_vaults

            output, http_response = (
                capo_odb._operations.odb.list_exascale_db_storage_vaults.list_exascale_db_storage_vaults(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListExascaleDbStorageVaults")
        )
        input_: capo_odb.types.list_exascale_db_storage_vaults_input.ListExascaleDbStorageVaultsInput = {}
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


class AsyncExascaleDbStorageVaultResource:
    def __init__(self, service: AsyncodbClient) -> None:
        self._service = service

    async def create(
        self,
        display_name: "capo_odb.types.resource_display_name.ResourceDisplayName",
        high_capacity_database_storage_total_size_in_g_bs: int,
        *,
        config_overrides: Optional[AsyncodbClientConfig] = None,
        additional_flash_cache_in_percent: Optional[int] = None,
        autoscale_limit_in_g_bs: Optional[int] = None,
        availability_zone_id: Optional[str] = None,
        availability_zone: Optional[str] = None,
        description: Optional[str] = None,
        is_autoscale_enabled: Optional[bool] = None,
        tags: Optional["capo_odb.types.request_tag_map.RequestTagMap"] = None,
        time_zone: Optional[str] = None,
        client_token: Optional[
            "capo_odb.types.general_input_string.GeneralInputString"
        ] = None,
    ) -> "capo_odb.types.create_exascale_db_storage_vault_output.CreateExascaleDbStorageVaultOutput":
        """<p>Creates an Exascale storage vault.</p>

        Args:
            display_name: <p>A user-friendly name for the Exascale storage vault.</p>
            high_capacity_database_storage_total_size_in_g_bs: <p>The total size of the high-capacity database storage, in gigabytes (GB), for the Exascale storage vault.</p>
            additional_flash_cache_in_percent: <p>The additional flash cache percentage for the Exascale storage vault.</p>
            autoscale_limit_in_g_bs: <p>The autoscale limit in gigabytes (GB) for the Exascale storage vault.</p>
            availability_zone_id: <p>The Availability Zone ID for the Exascale storage vault.</p>
            availability_zone: <p>The Availability Zone for the Exascale storage vault.</p>
            description: <p>A description of the Exascale storage vault.</p>
            is_autoscale_enabled: <p>Specifies whether autoscaling is enabled for the Exascale storage vault.</p>
            tags: <p>The list of resource tags to apply to the Exascale storage vault.</p>
            time_zone: <p>The time zone for the Exascale storage vault.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure that the operation completes no more than one time. If you submit the same request twice with the same client token, the service ignores the second request and returns the result of the first. If you don't specify a client token, the AWS SDK automatically generates one. The client token is valid for up to 24 hours after it's first used.</p>

        Raises:
            capo_odb.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action. Make sure you have the required permissions and try again.</p>
            capo_odb.errors.conflict_exception.ConflictException: <p>Occurs when a conflict with the current status of your resource. Fix any inconsistencies with your resource and try again.</p>
            capo_odb.errors.internal_server_exception.InternalServerException: <p>Occurs when there is an internal failure in the Oracle Database@Amazon Web Services service. Wait and try again.</p>
            capo_odb.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You have exceeded the service quota.</p>
            capo_odb.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_odb.errors.validation_exception.ValidationException: <p>The request has failed validation because it is missing required fields or has invalid inputs.</p>
            capo_odb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_odb.types.create_exascale_db_storage_vault_input.CreateExascaleDbStorageVaultInput]",
        ) -> AsyncOperationResponse[
            "capo_odb.types.create_exascale_db_storage_vault_output.CreateExascaleDbStorageVaultOutput"
        ]:
            import capo_odb._operations.odb.create_exascale_db_storage_vault

            (
                output,
                http_response,
            ) = await capo_odb._operations.odb.create_exascale_db_storage_vault.async_create_exascale_db_storage_vault(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("CreateExascaleDbStorageVault")
        )
        input_: capo_odb.types.create_exascale_db_storage_vault_input.CreateExascaleDbStorageVaultInput = {
            "display_name": display_name,
            "high_capacity_database_storage_total_size_in_g_bs": high_capacity_database_storage_total_size_in_g_bs,
        }
        if additional_flash_cache_in_percent is not None:
            input_["additional_flash_cache_in_percent"] = (
                additional_flash_cache_in_percent
            )
        if autoscale_limit_in_g_bs is not None:
            input_["autoscale_limit_in_g_bs"] = autoscale_limit_in_g_bs
        if availability_zone_id is not None:
            input_["availability_zone_id"] = availability_zone_id
        if availability_zone is not None:
            input_["availability_zone"] = availability_zone
        if description is not None:
            input_["description"] = description
        if is_autoscale_enabled is not None:
            input_["is_autoscale_enabled"] = is_autoscale_enabled
        if tags is not None:
            input_["tags"] = tags
        if time_zone is not None:
            input_["time_zone"] = time_zone
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def read(
        self,
        exascale_db_storage_vault_id: "capo_odb.types.resource_id_or_arn.ResourceIdOrArn",
        *,
        config_overrides: Optional[AsyncodbClientConfig] = None,
    ) -> "capo_odb.types.get_exascale_db_storage_vault_output.GetExascaleDbStorageVaultOutput":
        """<p>Returns information about the specified Exascale storage vault.</p>

        Args:
            exascale_db_storage_vault_id: <p>The unique identifier of the Exascale storage vault.</p>

        Raises:
            capo_odb.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action. Make sure you have the required permissions and try again.</p>
            capo_odb.errors.internal_server_exception.InternalServerException: <p>Occurs when there is an internal failure in the Oracle Database@Amazon Web Services service. Wait and try again.</p>
            capo_odb.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a resource that doesn't exist. Make sure you provided the correct resource and try again.</p>
            capo_odb.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_odb.errors.validation_exception.ValidationException: <p>The request has failed validation because it is missing required fields or has invalid inputs.</p>
            capo_odb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_odb.types.get_exascale_db_storage_vault_input.GetExascaleDbStorageVaultInput]",
        ) -> AsyncOperationResponse[
            "capo_odb.types.get_exascale_db_storage_vault_output.GetExascaleDbStorageVaultOutput"
        ]:
            import capo_odb._operations.odb.get_exascale_db_storage_vault

            (
                output,
                http_response,
            ) = await capo_odb._operations.odb.get_exascale_db_storage_vault.async_get_exascale_db_storage_vault(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetExascaleDbStorageVault")
        )
        input_: capo_odb.types.get_exascale_db_storage_vault_input.GetExascaleDbStorageVaultInput = {
            "exascale_db_storage_vault_id": exascale_db_storage_vault_id
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
        exascale_db_storage_vault_id: "capo_odb.types.resource_id_or_arn.ResourceIdOrArn",
        *,
        config_overrides: Optional[AsyncodbClientConfig] = None,
        additional_flash_cache_in_percent: Optional[int] = None,
        autoscale_limit_in_g_bs: Optional[int] = None,
        description: Optional[str] = None,
        display_name: Optional[
            "capo_odb.types.resource_display_name.ResourceDisplayName"
        ] = None,
        high_capacity_database_storage_total_size_in_g_bs: Optional[int] = None,
        is_autoscale_enabled: Optional[bool] = None,
    ) -> "capo_odb.types.update_exascale_db_storage_vault_output.UpdateExascaleDbStorageVaultOutput":
        """<p>Updates the specified Exascale storage vault.</p>

        Args:
            exascale_db_storage_vault_id: <p>The unique identifier of the Exascale storage vault to update.</p>
            additional_flash_cache_in_percent: <p>The additional flash cache percentage for the Exascale storage vault.</p>
            autoscale_limit_in_g_bs: <p>The autoscale limit in gigabytes (GB) for the Exascale storage vault.</p>
            description: <p>A new description for the Exascale storage vault.</p>
            display_name: <p>A new user-friendly name for the Exascale storage vault.</p>
            high_capacity_database_storage_total_size_in_g_bs: <p>The total size of the high-capacity database storage, in gigabytes (GB), for the Exascale storage vault.</p>
            is_autoscale_enabled: <p>Specifies whether autoscaling is enabled for the Exascale storage vault.</p>

        Raises:
            capo_odb.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action. Make sure you have the required permissions and try again.</p>
            capo_odb.errors.conflict_exception.ConflictException: <p>Occurs when a conflict with the current status of your resource. Fix any inconsistencies with your resource and try again.</p>
            capo_odb.errors.internal_server_exception.InternalServerException: <p>Occurs when there is an internal failure in the Oracle Database@Amazon Web Services service. Wait and try again.</p>
            capo_odb.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a resource that doesn't exist. Make sure you provided the correct resource and try again.</p>
            capo_odb.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_odb.errors.validation_exception.ValidationException: <p>The request has failed validation because it is missing required fields or has invalid inputs.</p>
            capo_odb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_odb.types.update_exascale_db_storage_vault_input.UpdateExascaleDbStorageVaultInput]",
        ) -> AsyncOperationResponse[
            "capo_odb.types.update_exascale_db_storage_vault_output.UpdateExascaleDbStorageVaultOutput"
        ]:
            import capo_odb._operations.odb.update_exascale_db_storage_vault

            (
                output,
                http_response,
            ) = await capo_odb._operations.odb.update_exascale_db_storage_vault.async_update_exascale_db_storage_vault(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("UpdateExascaleDbStorageVault")
        )
        input_: capo_odb.types.update_exascale_db_storage_vault_input.UpdateExascaleDbStorageVaultInput = {
            "exascale_db_storage_vault_id": exascale_db_storage_vault_id
        }
        if additional_flash_cache_in_percent is not None:
            input_["additional_flash_cache_in_percent"] = (
                additional_flash_cache_in_percent
            )
        if autoscale_limit_in_g_bs is not None:
            input_["autoscale_limit_in_g_bs"] = autoscale_limit_in_g_bs
        if description is not None:
            input_["description"] = description
        if display_name is not None:
            input_["display_name"] = display_name
        if high_capacity_database_storage_total_size_in_g_bs is not None:
            input_["high_capacity_database_storage_total_size_in_g_bs"] = (
                high_capacity_database_storage_total_size_in_g_bs
            )
        if is_autoscale_enabled is not None:
            input_["is_autoscale_enabled"] = is_autoscale_enabled

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete(
        self,
        exascale_db_storage_vault_id: "capo_odb.types.resource_id_or_arn.ResourceIdOrArn",
        *,
        config_overrides: Optional[AsyncodbClientConfig] = None,
    ) -> "capo_odb.types.delete_exascale_db_storage_vault_output.DeleteExascaleDbStorageVaultOutput":
        """<p>Deletes the specified Exascale storage vault.</p>

        Args:
            exascale_db_storage_vault_id: <p>The unique identifier of the Exascale storage vault to delete.</p>

        Raises:
            capo_odb.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action. Make sure you have the required permissions and try again.</p>
            capo_odb.errors.conflict_exception.ConflictException: <p>Occurs when a conflict with the current status of your resource. Fix any inconsistencies with your resource and try again.</p>
            capo_odb.errors.internal_server_exception.InternalServerException: <p>Occurs when there is an internal failure in the Oracle Database@Amazon Web Services service. Wait and try again.</p>
            capo_odb.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a resource that doesn't exist. Make sure you provided the correct resource and try again.</p>
            capo_odb.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_odb.errors.validation_exception.ValidationException: <p>The request has failed validation because it is missing required fields or has invalid inputs.</p>
            capo_odb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_odb.types.delete_exascale_db_storage_vault_input.DeleteExascaleDbStorageVaultInput]",
        ) -> AsyncOperationResponse[
            "capo_odb.types.delete_exascale_db_storage_vault_output.DeleteExascaleDbStorageVaultOutput"
        ]:
            import capo_odb._operations.odb.delete_exascale_db_storage_vault

            (
                output,
                http_response,
            ) = await capo_odb._operations.odb.delete_exascale_db_storage_vault.async_delete_exascale_db_storage_vault(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteExascaleDbStorageVault")
        )
        input_: capo_odb.types.delete_exascale_db_storage_vault_input.DeleteExascaleDbStorageVaultInput = {
            "exascale_db_storage_vault_id": exascale_db_storage_vault_id
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
        config_overrides: Optional[AsyncodbClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
    ) -> "capo_odb.types.list_exascale_db_storage_vaults_output.ListExascaleDbStorageVaultsOutput":
        """<p>Returns information about the Exascale storage vaults owned by your Amazon Web Services account.</p>

        Args:
            max_results: <p>The maximum number of items to return for this request. To get the next page of items, make another request with the token returned in the output.</p>
            next_token: <p>The token returned from a previous paginated request. Pagination continues from the end of the items returned by the previous request.</p>

        Raises:
            capo_odb.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action. Make sure you have the required permissions and try again.</p>
            capo_odb.errors.internal_server_exception.InternalServerException: <p>Occurs when there is an internal failure in the Oracle Database@Amazon Web Services service. Wait and try again.</p>
            capo_odb.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_odb.errors.validation_exception.ValidationException: <p>The request has failed validation because it is missing required fields or has invalid inputs.</p>
            capo_odb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_odb.types.list_exascale_db_storage_vaults_input.ListExascaleDbStorageVaultsInput]",
        ) -> AsyncOperationResponse[
            "capo_odb.types.list_exascale_db_storage_vaults_output.ListExascaleDbStorageVaultsOutput"
        ]:
            import capo_odb._operations.odb.list_exascale_db_storage_vaults

            (
                output,
                http_response,
            ) = await capo_odb._operations.odb.list_exascale_db_storage_vaults.async_list_exascale_db_storage_vaults(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListExascaleDbStorageVaults")
        )
        input_: capo_odb.types.list_exascale_db_storage_vaults_input.ListExascaleDbStorageVaultsInput = {}
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
