from __future__ import annotations

from typing import TYPE_CHECKING, Any, Optional

import capo_datazone._auth._signers
import capo_datazone._auth._sigv4
from capo_datazone._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationLogging,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_datazone.types.asset_type_identifier
    import capo_datazone.types.create_asset_type_input
    import capo_datazone.types.create_asset_type_output
    import capo_datazone.types.delete_asset_type_input
    import capo_datazone.types.delete_asset_type_output
    import capo_datazone.types.description
    import capo_datazone.types.domain_id
    import capo_datazone.types.forms_input_map
    import capo_datazone.types.get_asset_type_input
    import capo_datazone.types.get_asset_type_output
    import capo_datazone.types.project_id
    import capo_datazone.types.revision
    import capo_datazone.types.type_name
    from capo_datazone._services.async_data_zone import (
        AsyncDataZoneClient,
        AsyncDataZoneClientConfig,
    )
    from capo_datazone._services.data_zone import DataZoneClient, DataZoneClientConfig


class AssetType:
    def __init__(self, service: DataZoneClient) -> None:
        self._service = service

    def create(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        name: "capo_datazone.types.type_name.TypeName",
        forms_input: "capo_datazone.types.forms_input_map.FormsInputMap",
        owning_project_identifier: "capo_datazone.types.project_id.ProjectId",
        *,
        config_overrides: Optional[DataZoneClientConfig] = None,
        description: Optional["capo_datazone.types.description.Description"] = None,
    ) -> "capo_datazone.types.create_asset_type_output.CreateAssetTypeOutput":
        """<p>Creates a custom asset type.</p> <p>Prerequisites:</p> <ul> <li> <p>The <code>formsInput</code> field is required, however, can be passed as empty (e.g. <code>-forms-input {})</code>. </p> </li> <li> <p>You must have <code>CreateAssetType</code> permissions.</p> </li> <li> <p>The domain-identifier and owning-project-identifier must be valid and active.</p> </li> <li> <p>The name of the asset type must be unique within the domain — duplicate names will cause failure.</p> </li> <li> <p>JSON input must be valid — incorrect formatting causes Invalid JSON errors.</p> </li> </ul>

        Args:
            domain_identifier: <p>The unique identifier of the Amazon DataZone domain where the custom asset type is being created.</p>
            name: <p>The name of the custom asset type.</p>
            description: <p>The descripton of the custom asset type.</p>
            forms_input: <p>The metadata forms that are to be attached to the custom asset type.</p>
            owning_project_identifier: <p>The identifier of the Amazon DataZone project that is to own the custom asset type.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.conflict_exception.ConflictException: <p>There is a conflict while performing this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request has exceeded the specified service quota.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_datazone.types.create_asset_type_input.CreateAssetTypeInput]",
        ) -> OperationResponse[
            "capo_datazone.types.create_asset_type_output.CreateAssetTypeOutput"
        ]:
            import capo_datazone._operations.data_zone.create_asset_type

            output, http_response = (
                capo_datazone._operations.data_zone.create_asset_type.create_asset_type(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_datazone.types.create_asset_type_input.CreateAssetTypeInput",
        ) -> dict[str, Any]:
            import capo_datazone.types.create_asset_type_input

            return capo_datazone.types.create_asset_type_input.redact_sensitive(input_)

        def _redact_output(
            output: "capo_datazone.types.create_asset_type_output.CreateAssetTypeOutput",
        ) -> dict[str, Any]:
            import capo_datazone.types.create_asset_type_output

            return capo_datazone.types.create_asset_type_output.redact_sensitive(output)

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "CreateAssetType",
                redact_input=_redact_input,
                redact_output=_redact_output,
            ),
        )
        input_: capo_datazone.types.create_asset_type_input.CreateAssetTypeInput = {
            "domain_identifier": domain_identifier,
            "name": name,
            "forms_input": forms_input,
            "owning_project_identifier": owning_project_identifier,
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

    def delete_asset_type(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        identifier: "capo_datazone.types.asset_type_identifier.AssetTypeIdentifier",
        *,
        config_overrides: Optional[DataZoneClientConfig] = None,
    ) -> "capo_datazone.types.delete_asset_type_output.DeleteAssetTypeOutput":
        """<p>Deletes an asset type in Amazon DataZone.</p> <p>Prerequisites:</p> <ul> <li> <p>The asset type must exist in the domain. </p> </li> <li> <p>You must have DeleteAssetType permission.</p> </li> <li> <p>The asset type must not be in use (e.g., assigned to any asset). If used, deletion will fail.</p> </li> <li> <p>You should retrieve the asset type using get-asset-type to confirm its presence before deletion.</p> </li> </ul>

        Args:
            domain_identifier: <p>The ID of the Amazon DataZone domain in which the asset type is deleted.</p>
            identifier: <p>The identifier of the asset type that is deleted.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.conflict_exception.ConflictException: <p>There is a conflict while performing this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_datazone.types.delete_asset_type_input.DeleteAssetTypeInput]",
        ) -> OperationResponse[
            "capo_datazone.types.delete_asset_type_output.DeleteAssetTypeOutput"
        ]:
            import capo_datazone._operations.data_zone.delete_asset_type

            output, http_response = (
                capo_datazone._operations.data_zone.delete_asset_type.delete_asset_type(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteAssetType")
        )
        input_: capo_datazone.types.delete_asset_type_input.DeleteAssetTypeInput = {
            "domain_identifier": domain_identifier,
            "identifier": identifier,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_asset_type(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        identifier: "capo_datazone.types.asset_type_identifier.AssetTypeIdentifier",
        *,
        config_overrides: Optional[DataZoneClientConfig] = None,
        revision: Optional["capo_datazone.types.revision.Revision"] = None,
    ) -> "capo_datazone.types.get_asset_type_output.GetAssetTypeOutput":
        """<p>Gets an Amazon DataZone asset type.</p> <p>Asset types define the categories and characteristics of different kinds of data assets within Amazon DataZone.. They determine what metadata fields are required, what operations are possible, and how the asset integrates with other Amazon Web Services services. Asset types can range from built-in types like Amazon S3 buckets and Amazon Web Services Glue tables to custom types defined for specific organizational needs. Understanding asset types is crucial for properly organizing and managing different kinds of data resources.</p> <p>Prerequisites:</p> <ul> <li> <p>The asset type with identifier must exist in the domain. ResourceNotFoundException.</p> </li> <li> <p>You must have the GetAssetType permission.</p> </li> <li> <p>Ensure the domain-identifier value is correct and accessible.</p> </li> </ul>

        Args:
            domain_identifier: <p>The ID of the Amazon DataZone domain in which the asset type exists.</p>
            identifier: <p>The ID of the asset type.</p>
            revision: <p>The revision of the asset type.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_datazone.types.get_asset_type_input.GetAssetTypeInput]",
        ) -> OperationResponse[
            "capo_datazone.types.get_asset_type_output.GetAssetTypeOutput"
        ]:
            import capo_datazone._operations.data_zone.get_asset_type

            output, http_response = (
                capo_datazone._operations.data_zone.get_asset_type.get_asset_type(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_datazone.types.get_asset_type_output.GetAssetTypeOutput",
        ) -> dict[str, Any]:
            import capo_datazone.types.get_asset_type_output

            return capo_datazone.types.get_asset_type_output.redact_sensitive(output)

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("GetAssetType", redact_output=_redact_output),
        )
        input_: capo_datazone.types.get_asset_type_input.GetAssetTypeInput = {
            "domain_identifier": domain_identifier,
            "identifier": identifier,
        }
        if revision is not None:
            input_["revision"] = revision

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncAssetType:
    def __init__(self, service: AsyncDataZoneClient) -> None:
        self._service = service

    async def create(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        name: "capo_datazone.types.type_name.TypeName",
        forms_input: "capo_datazone.types.forms_input_map.FormsInputMap",
        owning_project_identifier: "capo_datazone.types.project_id.ProjectId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        description: Optional["capo_datazone.types.description.Description"] = None,
    ) -> "capo_datazone.types.create_asset_type_output.CreateAssetTypeOutput":
        """<p>Creates a custom asset type.</p> <p>Prerequisites:</p> <ul> <li> <p>The <code>formsInput</code> field is required, however, can be passed as empty (e.g. <code>-forms-input {})</code>. </p> </li> <li> <p>You must have <code>CreateAssetType</code> permissions.</p> </li> <li> <p>The domain-identifier and owning-project-identifier must be valid and active.</p> </li> <li> <p>The name of the asset type must be unique within the domain — duplicate names will cause failure.</p> </li> <li> <p>JSON input must be valid — incorrect formatting causes Invalid JSON errors.</p> </li> </ul>

        Args:
            domain_identifier: <p>The unique identifier of the Amazon DataZone domain where the custom asset type is being created.</p>
            name: <p>The name of the custom asset type.</p>
            description: <p>The descripton of the custom asset type.</p>
            forms_input: <p>The metadata forms that are to be attached to the custom asset type.</p>
            owning_project_identifier: <p>The identifier of the Amazon DataZone project that is to own the custom asset type.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.conflict_exception.ConflictException: <p>There is a conflict while performing this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request has exceeded the specified service quota.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_datazone.types.create_asset_type_input.CreateAssetTypeInput]",
        ) -> AsyncOperationResponse[
            "capo_datazone.types.create_asset_type_output.CreateAssetTypeOutput"
        ]:
            import capo_datazone._operations.data_zone.create_asset_type

            (
                output,
                http_response,
            ) = await capo_datazone._operations.data_zone.create_asset_type.async_create_asset_type(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_datazone.types.create_asset_type_input.CreateAssetTypeInput",
        ) -> dict[str, Any]:
            import capo_datazone.types.create_asset_type_input

            return capo_datazone.types.create_asset_type_input.redact_sensitive(input_)

        def _redact_output(
            output: "capo_datazone.types.create_asset_type_output.CreateAssetTypeOutput",
        ) -> dict[str, Any]:
            import capo_datazone.types.create_asset_type_output

            return capo_datazone.types.create_asset_type_output.redact_sensitive(output)

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "CreateAssetType",
                redact_input=_redact_input,
                redact_output=_redact_output,
            ),
        )
        input_: capo_datazone.types.create_asset_type_input.CreateAssetTypeInput = {
            "domain_identifier": domain_identifier,
            "name": name,
            "forms_input": forms_input,
            "owning_project_identifier": owning_project_identifier,
        }
        if description is not None:
            input_["description"] = description

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_asset_type(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        identifier: "capo_datazone.types.asset_type_identifier.AssetTypeIdentifier",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
    ) -> "capo_datazone.types.delete_asset_type_output.DeleteAssetTypeOutput":
        """<p>Deletes an asset type in Amazon DataZone.</p> <p>Prerequisites:</p> <ul> <li> <p>The asset type must exist in the domain. </p> </li> <li> <p>You must have DeleteAssetType permission.</p> </li> <li> <p>The asset type must not be in use (e.g., assigned to any asset). If used, deletion will fail.</p> </li> <li> <p>You should retrieve the asset type using get-asset-type to confirm its presence before deletion.</p> </li> </ul>

        Args:
            domain_identifier: <p>The ID of the Amazon DataZone domain in which the asset type is deleted.</p>
            identifier: <p>The identifier of the asset type that is deleted.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.conflict_exception.ConflictException: <p>There is a conflict while performing this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_datazone.types.delete_asset_type_input.DeleteAssetTypeInput]",
        ) -> AsyncOperationResponse[
            "capo_datazone.types.delete_asset_type_output.DeleteAssetTypeOutput"
        ]:
            import capo_datazone._operations.data_zone.delete_asset_type

            (
                output,
                http_response,
            ) = await capo_datazone._operations.data_zone.delete_asset_type.async_delete_asset_type(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteAssetType")
        )
        input_: capo_datazone.types.delete_asset_type_input.DeleteAssetTypeInput = {
            "domain_identifier": domain_identifier,
            "identifier": identifier,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_asset_type(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        identifier: "capo_datazone.types.asset_type_identifier.AssetTypeIdentifier",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        revision: Optional["capo_datazone.types.revision.Revision"] = None,
    ) -> "capo_datazone.types.get_asset_type_output.GetAssetTypeOutput":
        """<p>Gets an Amazon DataZone asset type.</p> <p>Asset types define the categories and characteristics of different kinds of data assets within Amazon DataZone.. They determine what metadata fields are required, what operations are possible, and how the asset integrates with other Amazon Web Services services. Asset types can range from built-in types like Amazon S3 buckets and Amazon Web Services Glue tables to custom types defined for specific organizational needs. Understanding asset types is crucial for properly organizing and managing different kinds of data resources.</p> <p>Prerequisites:</p> <ul> <li> <p>The asset type with identifier must exist in the domain. ResourceNotFoundException.</p> </li> <li> <p>You must have the GetAssetType permission.</p> </li> <li> <p>Ensure the domain-identifier value is correct and accessible.</p> </li> </ul>

        Args:
            domain_identifier: <p>The ID of the Amazon DataZone domain in which the asset type exists.</p>
            identifier: <p>The ID of the asset type.</p>
            revision: <p>The revision of the asset type.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_datazone.types.get_asset_type_input.GetAssetTypeInput]",
        ) -> AsyncOperationResponse[
            "capo_datazone.types.get_asset_type_output.GetAssetTypeOutput"
        ]:
            import capo_datazone._operations.data_zone.get_asset_type

            (
                output,
                http_response,
            ) = await capo_datazone._operations.data_zone.get_asset_type.async_get_asset_type(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_datazone.types.get_asset_type_output.GetAssetTypeOutput",
        ) -> dict[str, Any]:
            import capo_datazone.types.get_asset_type_output

            return capo_datazone.types.get_asset_type_output.redact_sensitive(output)

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("GetAssetType", redact_output=_redact_output),
        )
        input_: capo_datazone.types.get_asset_type_input.GetAssetTypeInput = {
            "domain_identifier": domain_identifier,
            "identifier": identifier,
        }
        if revision is not None:
            input_["revision"] = revision

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
