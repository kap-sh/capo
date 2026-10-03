from __future__ import annotations

from typing import TYPE_CHECKING, Optional

import capo_controltower._auth._signers
import capo_controltower._auth._sigv4
from capo_controltower._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_controltower.types.create_landing_zone_input
    import capo_controltower.types.create_landing_zone_output
    import capo_controltower.types.delete_landing_zone_input
    import capo_controltower.types.delete_landing_zone_output
    import capo_controltower.types.get_landing_zone_input
    import capo_controltower.types.get_landing_zone_output
    import capo_controltower.types.landing_zone_summary
    import capo_controltower.types.landing_zone_version
    import capo_controltower.types.list_landing_zones_input
    import capo_controltower.types.list_landing_zones_max_results
    import capo_controltower.types.list_landing_zones_output
    import capo_controltower.types.manifest
    import capo_controltower.types.remediation_types
    import capo_controltower.types.reset_landing_zone_input
    import capo_controltower.types.reset_landing_zone_output
    import capo_controltower.types.tag_map
    import capo_controltower.types.update_landing_zone_input
    import capo_controltower.types.update_landing_zone_output
    from capo_controltower._services.async_control_tower import (
        AsyncControlTowerClient,
        AsyncControlTowerClientConfig,
    )
    from capo_controltower._services.control_tower import (
        ControlTowerClient,
        ControlTowerClientConfig,
    )


class LandingZoneResource:
    def __init__(self, service: ControlTowerClient) -> None:
        self._service = service

    def create(
        self,
        version: "capo_controltower.types.landing_zone_version.LandingZoneVersion",
        *,
        config_overrides: Optional[ControlTowerClientConfig] = None,
        remediation_types: Optional[
            "capo_controltower.types.remediation_types.RemediationTypes"
        ] = None,
        tags: Optional["capo_controltower.types.tag_map.TagMap"] = None,
        manifest: Optional["capo_controltower.types.manifest.Manifest"] = None,
    ) -> "capo_controltower.types.create_landing_zone_output.CreateLandingZoneOutput":
        """<p>Creates a new landing zone. This API call starts an asynchronous operation that creates and configures a landing zone, based on the parameters specified in the manifest JSON file.</p>

        Args:
            version: <p>The landing zone version, for example, 3.0.</p>
            remediation_types: <p>Specifies the types of remediation actions to apply when creating the landing zone, such as automatic drift correction or compliance enforcement.</p>
            tags: <p>Tags to be applied to the landing zone. </p>
            manifest: <p>The manifest JSON file is a text file that describes your Amazon Web Services resources. For examples, review <a href="https://docs.aws.amazon.com/controltower/latest/userguide/lz-api-launch">Launch your landing zone</a>. </p>

        Raises:
            capo_controltower.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_controltower.errors.conflict_exception.ConflictException: <p>Updating or deleting the resource can cause an inconsistent state.</p>
            capo_controltower.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during processing of a request.</p>
            capo_controltower.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_controltower.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_controltower.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_controltower.types.create_landing_zone_input.CreateLandingZoneInput]",
        ) -> OperationResponse[
            "capo_controltower.types.create_landing_zone_output.CreateLandingZoneOutput"
        ]:
            import capo_controltower._operations.aws_control_tower_apis.create_landing_zone

            output, http_response = (
                capo_controltower._operations.aws_control_tower_apis.create_landing_zone.create_landing_zone(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_controltower.types.create_landing_zone_input.CreateLandingZoneInput = {
            "version": version
        }
        if remediation_types is not None:
            input_["remediation_types"] = remediation_types
        if tags is not None:
            input_["tags"] = tags
        if manifest is not None:
            input_["manifest"] = manifest

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def read(
        self,
        landing_zone_identifier: str,
        *,
        config_overrides: Optional[ControlTowerClientConfig] = None,
    ) -> "capo_controltower.types.get_landing_zone_output.GetLandingZoneOutput":
        """<p>Returns details about the landing zone. Displays a message in case of error.</p>

        Args:
            landing_zone_identifier: <p>The unique identifier of the landing zone.</p>

        Raises:
            capo_controltower.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_controltower.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during processing of a request.</p>
            capo_controltower.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist.</p>
            capo_controltower.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_controltower.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_controltower.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_controltower.types.get_landing_zone_input.GetLandingZoneInput]",
        ) -> OperationResponse[
            "capo_controltower.types.get_landing_zone_output.GetLandingZoneOutput"
        ]:
            import capo_controltower._operations.aws_control_tower_apis.get_landing_zone

            output, http_response = (
                capo_controltower._operations.aws_control_tower_apis.get_landing_zone.get_landing_zone(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_controltower.types.get_landing_zone_input.GetLandingZoneInput = {
            "landing_zone_identifier": landing_zone_identifier
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
        version: "capo_controltower.types.landing_zone_version.LandingZoneVersion",
        landing_zone_identifier: str,
        *,
        config_overrides: Optional[ControlTowerClientConfig] = None,
        remediation_types: Optional[
            "capo_controltower.types.remediation_types.RemediationTypes"
        ] = None,
        manifest: Optional["capo_controltower.types.manifest.Manifest"] = None,
    ) -> "capo_controltower.types.update_landing_zone_output.UpdateLandingZoneOutput":
        """<p>This API call updates the landing zone. It starts an asynchronous operation that updates the landing zone based on the new landing zone version, or on the changed parameters specified in the updated manifest file. </p>

        Args:
            version: <p>The landing zone version, for example, 3.2.</p>
            remediation_types: <p>Specifies the types of remediation actions to apply when updating the landing zone configuration.</p>
            landing_zone_identifier: <p>The unique identifier of the landing zone.</p>
            manifest: <p>The manifest file (JSON) is a text file that describes your Amazon Web Services resources. For an example, review <a href="https://docs.aws.amazon.com/controltower/latest/userguide/lz-api-launch">Launch your landing zone</a>. The example manifest file contains each of the available parameters. The schema for the landing zone's JSON manifest file is not published, by design.</p>

        Raises:
            capo_controltower.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_controltower.errors.conflict_exception.ConflictException: <p>Updating or deleting the resource can cause an inconsistent state.</p>
            capo_controltower.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during processing of a request.</p>
            capo_controltower.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist.</p>
            capo_controltower.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_controltower.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_controltower.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_controltower.types.update_landing_zone_input.UpdateLandingZoneInput]",
        ) -> OperationResponse[
            "capo_controltower.types.update_landing_zone_output.UpdateLandingZoneOutput"
        ]:
            import capo_controltower._operations.aws_control_tower_apis.update_landing_zone

            output, http_response = (
                capo_controltower._operations.aws_control_tower_apis.update_landing_zone.update_landing_zone(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_controltower.types.update_landing_zone_input.UpdateLandingZoneInput = {
            "version": version,
            "landing_zone_identifier": landing_zone_identifier,
        }
        if remediation_types is not None:
            input_["remediation_types"] = remediation_types
        if manifest is not None:
            input_["manifest"] = manifest

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete(
        self,
        landing_zone_identifier: str,
        *,
        config_overrides: Optional[ControlTowerClientConfig] = None,
    ) -> "capo_controltower.types.delete_landing_zone_output.DeleteLandingZoneOutput":
        """<p>Decommissions a landing zone. This API call starts an asynchronous operation that deletes Amazon Web Services Control Tower resources deployed in accounts managed by Amazon Web Services Control Tower.</p> <p>Decommissioning a landing zone is a process with significant consequences, and it cannot be undone. We strongly recommend that you perform this decommissioning process only if you intend to stop using your landing zone.</p>

        Args:
            landing_zone_identifier: <p>The unique identifier of the landing zone.</p>

        Raises:
            capo_controltower.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_controltower.errors.conflict_exception.ConflictException: <p>Updating or deleting the resource can cause an inconsistent state.</p>
            capo_controltower.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during processing of a request.</p>
            capo_controltower.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist.</p>
            capo_controltower.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_controltower.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_controltower.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_controltower.types.delete_landing_zone_input.DeleteLandingZoneInput]",
        ) -> OperationResponse[
            "capo_controltower.types.delete_landing_zone_output.DeleteLandingZoneOutput"
        ]:
            import capo_controltower._operations.aws_control_tower_apis.delete_landing_zone

            output, http_response = (
                capo_controltower._operations.aws_control_tower_apis.delete_landing_zone.delete_landing_zone(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_controltower.types.delete_landing_zone_input.DeleteLandingZoneInput = {
            "landing_zone_identifier": landing_zone_identifier
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
        config_overrides: Optional[ControlTowerClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[
            "capo_controltower.types.list_landing_zones_max_results.ListLandingZonesMaxResults"
        ] = None,
    ) -> "capo_controltower.types.list_landing_zones_output.ListLandingZonesOutput":
        """<p>Returns the landing zone ARN for the landing zone deployed in your managed account. This API also creates an ARN for existing accounts that do not yet have a landing zone ARN. </p> <p>Returns one landing zone ARN.</p>

        Args:
            next_token: <p>The token to continue the list from a previous API call with the same parameters.</p>
            max_results: <p>The maximum number of returned landing zone ARNs, which is one.</p>

        Raises:
            capo_controltower.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_controltower.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during processing of a request.</p>
            capo_controltower.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_controltower.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_controltower.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_controltower.types.list_landing_zones_input.ListLandingZonesInput]",
        ) -> OperationResponse[
            "capo_controltower.types.list_landing_zones_output.ListLandingZonesOutput"
        ]:
            import capo_controltower._operations.aws_control_tower_apis.list_landing_zones

            output, http_response = (
                capo_controltower._operations.aws_control_tower_apis.list_landing_zones.list_landing_zones(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_controltower.types.list_landing_zones_input.ListLandingZonesInput = {}
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

    def reset_landing_zone(
        self,
        landing_zone_identifier: str,
        *,
        config_overrides: Optional[ControlTowerClientConfig] = None,
    ) -> "capo_controltower.types.reset_landing_zone_output.ResetLandingZoneOutput":
        """<p>This API call resets a landing zone. It starts an asynchronous operation that resets the landing zone to the parameters specified in the original configuration, which you specified in the manifest file. Nothing in the manifest file's original landing zone configuration is changed during the reset process, by default. This API is not the same as a rollback of a landing zone version, which is not a supported operation.</p>

        Args:
            landing_zone_identifier: <p>The unique identifier of the landing zone.</p>

        Raises:
            capo_controltower.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_controltower.errors.conflict_exception.ConflictException: <p>Updating or deleting the resource can cause an inconsistent state.</p>
            capo_controltower.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during processing of a request.</p>
            capo_controltower.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist.</p>
            capo_controltower.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_controltower.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_controltower.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_controltower.types.reset_landing_zone_input.ResetLandingZoneInput]",
        ) -> OperationResponse[
            "capo_controltower.types.reset_landing_zone_output.ResetLandingZoneOutput"
        ]:
            import capo_controltower._operations.aws_control_tower_apis.reset_landing_zone

            output, http_response = (
                capo_controltower._operations.aws_control_tower_apis.reset_landing_zone.reset_landing_zone(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_controltower.types.reset_landing_zone_input.ResetLandingZoneInput = {
            "landing_zone_identifier": landing_zone_identifier
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncLandingZoneResource:
    def __init__(self, service: AsyncControlTowerClient) -> None:
        self._service = service

    async def create(
        self,
        version: "capo_controltower.types.landing_zone_version.LandingZoneVersion",
        *,
        config_overrides: Optional[AsyncControlTowerClientConfig] = None,
        remediation_types: Optional[
            "capo_controltower.types.remediation_types.RemediationTypes"
        ] = None,
        tags: Optional["capo_controltower.types.tag_map.TagMap"] = None,
        manifest: Optional["capo_controltower.types.manifest.Manifest"] = None,
    ) -> "capo_controltower.types.create_landing_zone_output.CreateLandingZoneOutput":
        """<p>Creates a new landing zone. This API call starts an asynchronous operation that creates and configures a landing zone, based on the parameters specified in the manifest JSON file.</p>

        Args:
            version: <p>The landing zone version, for example, 3.0.</p>
            remediation_types: <p>Specifies the types of remediation actions to apply when creating the landing zone, such as automatic drift correction or compliance enforcement.</p>
            tags: <p>Tags to be applied to the landing zone. </p>
            manifest: <p>The manifest JSON file is a text file that describes your Amazon Web Services resources. For examples, review <a href="https://docs.aws.amazon.com/controltower/latest/userguide/lz-api-launch">Launch your landing zone</a>. </p>

        Raises:
            capo_controltower.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_controltower.errors.conflict_exception.ConflictException: <p>Updating or deleting the resource can cause an inconsistent state.</p>
            capo_controltower.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during processing of a request.</p>
            capo_controltower.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_controltower.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_controltower.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_controltower.types.create_landing_zone_input.CreateLandingZoneInput]",
        ) -> AsyncOperationResponse[
            "capo_controltower.types.create_landing_zone_output.CreateLandingZoneOutput"
        ]:
            import capo_controltower._operations.aws_control_tower_apis.create_landing_zone

            (
                output,
                http_response,
            ) = await capo_controltower._operations.aws_control_tower_apis.create_landing_zone.async_create_landing_zone(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_controltower.types.create_landing_zone_input.CreateLandingZoneInput = {
            "version": version
        }
        if remediation_types is not None:
            input_["remediation_types"] = remediation_types
        if tags is not None:
            input_["tags"] = tags
        if manifest is not None:
            input_["manifest"] = manifest

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def read(
        self,
        landing_zone_identifier: str,
        *,
        config_overrides: Optional[AsyncControlTowerClientConfig] = None,
    ) -> "capo_controltower.types.get_landing_zone_output.GetLandingZoneOutput":
        """<p>Returns details about the landing zone. Displays a message in case of error.</p>

        Args:
            landing_zone_identifier: <p>The unique identifier of the landing zone.</p>

        Raises:
            capo_controltower.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_controltower.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during processing of a request.</p>
            capo_controltower.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist.</p>
            capo_controltower.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_controltower.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_controltower.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_controltower.types.get_landing_zone_input.GetLandingZoneInput]",
        ) -> AsyncOperationResponse[
            "capo_controltower.types.get_landing_zone_output.GetLandingZoneOutput"
        ]:
            import capo_controltower._operations.aws_control_tower_apis.get_landing_zone

            (
                output,
                http_response,
            ) = await capo_controltower._operations.aws_control_tower_apis.get_landing_zone.async_get_landing_zone(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_controltower.types.get_landing_zone_input.GetLandingZoneInput = {
            "landing_zone_identifier": landing_zone_identifier
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
        version: "capo_controltower.types.landing_zone_version.LandingZoneVersion",
        landing_zone_identifier: str,
        *,
        config_overrides: Optional[AsyncControlTowerClientConfig] = None,
        remediation_types: Optional[
            "capo_controltower.types.remediation_types.RemediationTypes"
        ] = None,
        manifest: Optional["capo_controltower.types.manifest.Manifest"] = None,
    ) -> "capo_controltower.types.update_landing_zone_output.UpdateLandingZoneOutput":
        """<p>This API call updates the landing zone. It starts an asynchronous operation that updates the landing zone based on the new landing zone version, or on the changed parameters specified in the updated manifest file. </p>

        Args:
            version: <p>The landing zone version, for example, 3.2.</p>
            remediation_types: <p>Specifies the types of remediation actions to apply when updating the landing zone configuration.</p>
            landing_zone_identifier: <p>The unique identifier of the landing zone.</p>
            manifest: <p>The manifest file (JSON) is a text file that describes your Amazon Web Services resources. For an example, review <a href="https://docs.aws.amazon.com/controltower/latest/userguide/lz-api-launch">Launch your landing zone</a>. The example manifest file contains each of the available parameters. The schema for the landing zone's JSON manifest file is not published, by design.</p>

        Raises:
            capo_controltower.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_controltower.errors.conflict_exception.ConflictException: <p>Updating or deleting the resource can cause an inconsistent state.</p>
            capo_controltower.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during processing of a request.</p>
            capo_controltower.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist.</p>
            capo_controltower.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_controltower.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_controltower.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_controltower.types.update_landing_zone_input.UpdateLandingZoneInput]",
        ) -> AsyncOperationResponse[
            "capo_controltower.types.update_landing_zone_output.UpdateLandingZoneOutput"
        ]:
            import capo_controltower._operations.aws_control_tower_apis.update_landing_zone

            (
                output,
                http_response,
            ) = await capo_controltower._operations.aws_control_tower_apis.update_landing_zone.async_update_landing_zone(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_controltower.types.update_landing_zone_input.UpdateLandingZoneInput = {
            "version": version,
            "landing_zone_identifier": landing_zone_identifier,
        }
        if remediation_types is not None:
            input_["remediation_types"] = remediation_types
        if manifest is not None:
            input_["manifest"] = manifest

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete(
        self,
        landing_zone_identifier: str,
        *,
        config_overrides: Optional[AsyncControlTowerClientConfig] = None,
    ) -> "capo_controltower.types.delete_landing_zone_output.DeleteLandingZoneOutput":
        """<p>Decommissions a landing zone. This API call starts an asynchronous operation that deletes Amazon Web Services Control Tower resources deployed in accounts managed by Amazon Web Services Control Tower.</p> <p>Decommissioning a landing zone is a process with significant consequences, and it cannot be undone. We strongly recommend that you perform this decommissioning process only if you intend to stop using your landing zone.</p>

        Args:
            landing_zone_identifier: <p>The unique identifier of the landing zone.</p>

        Raises:
            capo_controltower.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_controltower.errors.conflict_exception.ConflictException: <p>Updating or deleting the resource can cause an inconsistent state.</p>
            capo_controltower.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during processing of a request.</p>
            capo_controltower.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist.</p>
            capo_controltower.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_controltower.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_controltower.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_controltower.types.delete_landing_zone_input.DeleteLandingZoneInput]",
        ) -> AsyncOperationResponse[
            "capo_controltower.types.delete_landing_zone_output.DeleteLandingZoneOutput"
        ]:
            import capo_controltower._operations.aws_control_tower_apis.delete_landing_zone

            (
                output,
                http_response,
            ) = await capo_controltower._operations.aws_control_tower_apis.delete_landing_zone.async_delete_landing_zone(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_controltower.types.delete_landing_zone_input.DeleteLandingZoneInput = {
            "landing_zone_identifier": landing_zone_identifier
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
        config_overrides: Optional[AsyncControlTowerClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[
            "capo_controltower.types.list_landing_zones_max_results.ListLandingZonesMaxResults"
        ] = None,
    ) -> "capo_controltower.types.list_landing_zones_output.ListLandingZonesOutput":
        """<p>Returns the landing zone ARN for the landing zone deployed in your managed account. This API also creates an ARN for existing accounts that do not yet have a landing zone ARN. </p> <p>Returns one landing zone ARN.</p>

        Args:
            next_token: <p>The token to continue the list from a previous API call with the same parameters.</p>
            max_results: <p>The maximum number of returned landing zone ARNs, which is one.</p>

        Raises:
            capo_controltower.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_controltower.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during processing of a request.</p>
            capo_controltower.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_controltower.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_controltower.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_controltower.types.list_landing_zones_input.ListLandingZonesInput]",
        ) -> AsyncOperationResponse[
            "capo_controltower.types.list_landing_zones_output.ListLandingZonesOutput"
        ]:
            import capo_controltower._operations.aws_control_tower_apis.list_landing_zones

            (
                output,
                http_response,
            ) = await capo_controltower._operations.aws_control_tower_apis.list_landing_zones.async_list_landing_zones(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_controltower.types.list_landing_zones_input.ListLandingZonesInput = {}
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def reset_landing_zone(
        self,
        landing_zone_identifier: str,
        *,
        config_overrides: Optional[AsyncControlTowerClientConfig] = None,
    ) -> "capo_controltower.types.reset_landing_zone_output.ResetLandingZoneOutput":
        """<p>This API call resets a landing zone. It starts an asynchronous operation that resets the landing zone to the parameters specified in the original configuration, which you specified in the manifest file. Nothing in the manifest file's original landing zone configuration is changed during the reset process, by default. This API is not the same as a rollback of a landing zone version, which is not a supported operation.</p>

        Args:
            landing_zone_identifier: <p>The unique identifier of the landing zone.</p>

        Raises:
            capo_controltower.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_controltower.errors.conflict_exception.ConflictException: <p>Updating or deleting the resource can cause an inconsistent state.</p>
            capo_controltower.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during processing of a request.</p>
            capo_controltower.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist.</p>
            capo_controltower.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_controltower.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_controltower.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_controltower.types.reset_landing_zone_input.ResetLandingZoneInput]",
        ) -> AsyncOperationResponse[
            "capo_controltower.types.reset_landing_zone_output.ResetLandingZoneOutput"
        ]:
            import capo_controltower._operations.aws_control_tower_apis.reset_landing_zone

            (
                output,
                http_response,
            ) = await capo_controltower._operations.aws_control_tower_apis.reset_landing_zone.async_reset_landing_zone(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_controltower.types.reset_landing_zone_input.ResetLandingZoneInput = {
            "landing_zone_identifier": landing_zone_identifier
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
