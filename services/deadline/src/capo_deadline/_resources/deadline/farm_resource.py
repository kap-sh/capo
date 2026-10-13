from __future__ import annotations

import uuid
from typing import TYPE_CHECKING, Any, Optional

import capo_deadline._auth._signers
import capo_deadline._auth._sigv4
from capo_deadline._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationLogging,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_deadline.types.amount_requirement_name
    import capo_deadline.types.associate_member_to_farm_request
    import capo_deadline.types.associate_member_to_farm_response
    import capo_deadline.types.client_token
    import capo_deadline.types.cost_scale_factor
    import capo_deadline.types.create_farm_request
    import capo_deadline.types.create_farm_response
    import capo_deadline.types.create_limit_request
    import capo_deadline.types.create_limit_response
    import capo_deadline.types.create_storage_profile_request
    import capo_deadline.types.create_storage_profile_response
    import capo_deadline.types.deadline_principal_type
    import capo_deadline.types.delete_farm_request
    import capo_deadline.types.delete_farm_response
    import capo_deadline.types.delete_limit_request
    import capo_deadline.types.delete_limit_response
    import capo_deadline.types.delete_storage_profile_request
    import capo_deadline.types.delete_storage_profile_response
    import capo_deadline.types.description
    import capo_deadline.types.disassociate_member_from_farm_request
    import capo_deadline.types.disassociate_member_from_farm_response
    import capo_deadline.types.farm_id
    import capo_deadline.types.farm_member
    import capo_deadline.types.farm_summary
    import capo_deadline.types.file_system_locations_list
    import capo_deadline.types.get_farm_request
    import capo_deadline.types.get_farm_response
    import capo_deadline.types.get_limit_request
    import capo_deadline.types.get_limit_response
    import capo_deadline.types.get_storage_profile_request
    import capo_deadline.types.get_storage_profile_response
    import capo_deadline.types.identity_center_principal_id
    import capo_deadline.types.identity_store_id
    import capo_deadline.types.kms_key_arn
    import capo_deadline.types.limit_id
    import capo_deadline.types.limit_summary
    import capo_deadline.types.list_farm_members_request
    import capo_deadline.types.list_farm_members_response
    import capo_deadline.types.list_farms_request
    import capo_deadline.types.list_farms_response
    import capo_deadline.types.list_limits_request
    import capo_deadline.types.list_limits_response
    import capo_deadline.types.list_storage_profiles_request
    import capo_deadline.types.list_storage_profiles_response
    import capo_deadline.types.max_count
    import capo_deadline.types.max_results
    import capo_deadline.types.membership_level
    import capo_deadline.types.next_token
    import capo_deadline.types.region
    import capo_deadline.types.resource_name
    import capo_deadline.types.storage_profile_id
    import capo_deadline.types.storage_profile_operating_system_family
    import capo_deadline.types.storage_profile_summary
    import capo_deadline.types.tags
    import capo_deadline.types.update_farm_request
    import capo_deadline.types.update_farm_response
    import capo_deadline.types.update_limit_request
    import capo_deadline.types.update_limit_response
    import capo_deadline.types.update_storage_profile_request
    import capo_deadline.types.update_storage_profile_response
    from capo_deadline._services.async_deadline import (
        AsyncdeadlineClient,
        AsyncdeadlineClientConfig,
    )
    from capo_deadline._services.deadline import deadlineClient, deadlineClientConfig


class FarmResource:
    def __init__(self, service: deadlineClient) -> None:
        self._service = service

    def create(
        self,
        display_name: "capo_deadline.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
        client_token: Optional["capo_deadline.types.client_token.ClientToken"] = None,
        description: Optional["capo_deadline.types.description.Description"] = None,
        kms_key_arn: Optional["capo_deadline.types.kms_key_arn.KmsKeyArn"] = None,
        cost_scale_factor: Optional[
            "capo_deadline.types.cost_scale_factor.CostScaleFactor"
        ] = None,
        tags: Optional["capo_deadline.types.tags.Tags"] = None,
    ) -> "capo_deadline.types.create_farm_response.CreateFarmResponse":
        """<p>Creates a farm to allow space for queues and fleets. Farms are the space where the components of your renders gather and are pieced together in the cloud. Farms contain budgets and allow you to enforce permissions. Deadline Cloud farms are a useful container for large projects.</p>

        Args:
            client_token: <p>The unique token which the server uses to recognize retries of the same request.</p>
            display_name: <p>The display name of the farm.</p> <important> <p>This field can store any content. Escape or encode this content before displaying it on a webpage or any other system that might interpret the content of this field.</p> </important>
            description: <p>The description of the farm.</p> <important> <p>This field can store any content. Escape or encode this content before displaying it on a webpage or any other system that might interpret the content of this field.</p> </important>
            kms_key_arn: <p>The ARN of the KMS key to use on the farm.</p>
            cost_scale_factor: <p>A multiplier applied to the farm's calculated costs for usage data and budget tracking. A value less than 1 represents a discount, a value greater than 1 represents a premium, and a value of 1 represents no adjustment. The default value is 1.</p>
            tags: <p>The tags to add to your farm. Each tag consists of a tag key and a tag value. Tag keys and values are both required, but tag values can be empty strings.</p>

        Raises:
            capo_deadline.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action.</p>
            capo_deadline.errors.internal_server_error_exception.InternalServerErrorException: <p>Deadline Cloud can't process your request right now. Try again later.</p>
            capo_deadline.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_deadline.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You exceeded your service quota. Service quotas, also referred to as limits, are the maximum number of service resources or operations for your Amazon Web Services account.</p>
            capo_deadline.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a request rate quota.</p>
            capo_deadline.errors.validation_exception.ValidationException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.</p>
            capo_deadline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_deadline.types.create_farm_request.CreateFarmRequest]",
        ) -> OperationResponse[
            "capo_deadline.types.create_farm_response.CreateFarmResponse"
        ]:
            import capo_deadline._operations.deadline.create_farm

            output, http_response = (
                capo_deadline._operations.deadline.create_farm.create_farm(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_deadline.types.create_farm_request.CreateFarmRequest",
        ) -> dict[str, Any]:
            import capo_deadline.types.create_farm_request

            return capo_deadline.types.create_farm_request.redact_sensitive(input_)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("CreateFarm", redact_input=_redact_input)
        )
        input_: capo_deadline.types.create_farm_request.CreateFarmRequest = {
            "display_name": display_name
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if description is not None:
            input_["description"] = description
        if kms_key_arn is not None:
            input_["kms_key_arn"] = kms_key_arn
        if cost_scale_factor is not None:
            input_["cost_scale_factor"] = cost_scale_factor
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
        farm_id: "capo_deadline.types.farm_id.FarmId",
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
    ) -> "capo_deadline.types.get_farm_response.GetFarmResponse":
        """<p>Get a farm.</p>

        Args:
            farm_id: <p>The farm ID of the farm.</p>

        Raises:
            capo_deadline.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action.</p>
            capo_deadline.errors.internal_server_error_exception.InternalServerErrorException: <p>Deadline Cloud can't process your request right now. Try again later.</p>
            capo_deadline.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_deadline.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a request rate quota.</p>
            capo_deadline.errors.validation_exception.ValidationException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.</p>
            capo_deadline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_deadline.types.get_farm_request.GetFarmRequest]",
        ) -> OperationResponse["capo_deadline.types.get_farm_response.GetFarmResponse"]:
            import capo_deadline._operations.deadline.get_farm

            output, http_response = (
                capo_deadline._operations.deadline.get_farm.get_farm(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_deadline.types.get_farm_response.GetFarmResponse",
        ) -> dict[str, Any]:
            import capo_deadline.types.get_farm_response

            return capo_deadline.types.get_farm_response.redact_sensitive(output)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetFarm", redact_output=_redact_output)
        )
        input_: capo_deadline.types.get_farm_request.GetFarmRequest = {
            "farm_id": farm_id
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
        farm_id: "capo_deadline.types.farm_id.FarmId",
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
        display_name: Optional["capo_deadline.types.resource_name.ResourceName"] = None,
        description: Optional["capo_deadline.types.description.Description"] = None,
        cost_scale_factor: Optional[
            "capo_deadline.types.cost_scale_factor.CostScaleFactor"
        ] = None,
    ) -> "capo_deadline.types.update_farm_response.UpdateFarmResponse":
        """<p>Updates a farm.</p>

        Args:
            farm_id: <p>The farm ID to update.</p>
            display_name: <p>The display name of the farm to update.</p> <important> <p>This field can store any content. Escape or encode this content before displaying it on a webpage or any other system that might interpret the content of this field.</p> </important>
            description: <p>The description of the farm to update.</p> <important> <p>This field can store any content. Escape or encode this content before displaying it on a webpage or any other system that might interpret the content of this field.</p> </important>
            cost_scale_factor: <p>A multiplier applied to the farm's calculated costs for usage data and budget tracking. A value less than 1 represents a discount, a value greater than 1 represents a premium, and a value of 1 represents no adjustment.</p>

        Raises:
            capo_deadline.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action.</p>
            capo_deadline.errors.internal_server_error_exception.InternalServerErrorException: <p>Deadline Cloud can't process your request right now. Try again later.</p>
            capo_deadline.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_deadline.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a request rate quota.</p>
            capo_deadline.errors.validation_exception.ValidationException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.</p>
            capo_deadline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_deadline.types.update_farm_request.UpdateFarmRequest]",
        ) -> OperationResponse[
            "capo_deadline.types.update_farm_response.UpdateFarmResponse"
        ]:
            import capo_deadline._operations.deadline.update_farm

            output, http_response = (
                capo_deadline._operations.deadline.update_farm.update_farm(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_deadline.types.update_farm_request.UpdateFarmRequest",
        ) -> dict[str, Any]:
            import capo_deadline.types.update_farm_request

            return capo_deadline.types.update_farm_request.redact_sensitive(input_)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("UpdateFarm", redact_input=_redact_input)
        )
        input_: capo_deadline.types.update_farm_request.UpdateFarmRequest = {
            "farm_id": farm_id
        }
        if display_name is not None:
            input_["display_name"] = display_name
        if description is not None:
            input_["description"] = description
        if cost_scale_factor is not None:
            input_["cost_scale_factor"] = cost_scale_factor

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete(
        self,
        farm_id: "capo_deadline.types.farm_id.FarmId",
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
    ) -> "capo_deadline.types.delete_farm_response.DeleteFarmResponse":
        """<p>Deletes a farm.</p>

        Args:
            farm_id: <p>The farm ID of the farm to delete.</p>

        Raises:
            capo_deadline.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action.</p>
            capo_deadline.errors.internal_server_error_exception.InternalServerErrorException: <p>Deadline Cloud can't process your request right now. Try again later.</p>
            capo_deadline.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_deadline.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a request rate quota.</p>
            capo_deadline.errors.validation_exception.ValidationException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.</p>
            capo_deadline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_deadline.types.delete_farm_request.DeleteFarmRequest]",
        ) -> OperationResponse[
            "capo_deadline.types.delete_farm_response.DeleteFarmResponse"
        ]:
            import capo_deadline._operations.deadline.delete_farm

            output, http_response = (
                capo_deadline._operations.deadline.delete_farm.delete_farm(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteFarm")
        )
        input_: capo_deadline.types.delete_farm_request.DeleteFarmRequest = {
            "farm_id": farm_id
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
        config_overrides: Optional[deadlineClientConfig] = None,
        next_token: Optional["capo_deadline.types.next_token.NextToken"] = None,
        max_results: Optional["capo_deadline.types.max_results.MaxResults"] = None,
        principal_id: Optional[
            "capo_deadline.types.identity_center_principal_id.IdentityCenterPrincipalId"
        ] = None,
    ) -> "capo_deadline.types.list_farms_response.ListFarmsResponse":
        """<p>Lists farms.</p>

        Args:
            next_token: <p>The token for the next set of results, or <code>null</code> to start from the beginning.</p>
            max_results: <p>The maximum number of results to return. Use this parameter with <code>NextToken</code> to get results as a set of sequential pages.</p>
            principal_id: <p>The principal ID of the member to list on the farm.</p>

        Raises:
            capo_deadline.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action.</p>
            capo_deadline.errors.internal_server_error_exception.InternalServerErrorException: <p>Deadline Cloud can't process your request right now. Try again later.</p>
            capo_deadline.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a request rate quota.</p>
            capo_deadline.errors.validation_exception.ValidationException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.</p>
            capo_deadline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_deadline.types.list_farms_request.ListFarmsRequest]",
        ) -> OperationResponse[
            "capo_deadline.types.list_farms_response.ListFarmsResponse"
        ]:
            import capo_deadline._operations.deadline.list_farms

            output, http_response = (
                capo_deadline._operations.deadline.list_farms.list_farms(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListFarms")
        )
        input_: capo_deadline.types.list_farms_request.ListFarmsRequest = {}
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if principal_id is not None:
            input_["principal_id"] = principal_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def associate_member_to_farm(
        self,
        farm_id: "capo_deadline.types.farm_id.FarmId",
        principal_type: "capo_deadline.types.deadline_principal_type.DeadlinePrincipalType",
        identity_store_id: "capo_deadline.types.identity_store_id.IdentityStoreId",
        membership_level: "capo_deadline.types.membership_level.MembershipLevel",
        principal_id: "capo_deadline.types.identity_center_principal_id.IdentityCenterPrincipalId",
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
        identity_center_region: Optional["capo_deadline.types.region.Region"] = None,
    ) -> "capo_deadline.types.associate_member_to_farm_response.AssociateMemberToFarmResponse":
        """<p>Assigns a farm membership level to a member.</p>

        Args:
            farm_id: <p>The ID of the farm to associate with the member.</p>
            principal_type: <p>The principal type of the member to associate with the farm.</p>
            identity_store_id: <p>The identity store ID of the member to associate with the farm.</p>
            membership_level: <p>The principal's membership level for the associated farm.</p>
            principal_id: <p>The member's principal ID to associate with the farm.</p>
            identity_center_region: <p>The Region of the IAM Identity Center instance. If not provided, the service defaults to the Region of the farm.</p>

        Raises:
            capo_deadline.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action.</p>
            capo_deadline.errors.internal_server_error_exception.InternalServerErrorException: <p>Deadline Cloud can't process your request right now. Try again later.</p>
            capo_deadline.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_deadline.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You exceeded your service quota. Service quotas, also referred to as limits, are the maximum number of service resources or operations for your Amazon Web Services account.</p>
            capo_deadline.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a request rate quota.</p>
            capo_deadline.errors.validation_exception.ValidationException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.</p>
            capo_deadline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_deadline.types.associate_member_to_farm_request.AssociateMemberToFarmRequest]",
        ) -> OperationResponse[
            "capo_deadline.types.associate_member_to_farm_response.AssociateMemberToFarmResponse"
        ]:
            import capo_deadline._operations.deadline.associate_member_to_farm

            output, http_response = (
                capo_deadline._operations.deadline.associate_member_to_farm.associate_member_to_farm(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("AssociateMemberToFarm")
        )
        input_: capo_deadline.types.associate_member_to_farm_request.AssociateMemberToFarmRequest = {
            "farm_id": farm_id,
            "principal_type": principal_type,
            "identity_store_id": identity_store_id,
            "membership_level": membership_level,
            "principal_id": principal_id,
        }
        if identity_center_region is not None:
            input_["identity_center_region"] = identity_center_region

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_limit(
        self,
        farm_id: "capo_deadline.types.farm_id.FarmId",
        display_name: "capo_deadline.types.resource_name.ResourceName",
        amount_requirement_name: "capo_deadline.types.amount_requirement_name.AmountRequirementName",
        max_count: "capo_deadline.types.max_count.MaxCount",
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
        client_token: Optional["capo_deadline.types.client_token.ClientToken"] = None,
        description: Optional["capo_deadline.types.description.Description"] = None,
    ) -> "capo_deadline.types.create_limit_response.CreateLimitResponse":
        """<p>Creates a limit that manages the distribution of shared resources, such as floating licenses. A limit can throttle work assignments, help manage workloads, and track current usage. Before you use a limit, you must associate the limit with one or more queues. </p> <p>You must add the <code>amountRequirementName</code> to a step in a job template to declare the limit requirement.</p>

        Args:
            farm_id: <p>The farm ID of the farm that contains the limit.</p>
            client_token: <p>The unique token which the server uses to recognize retries of the same request.</p>
            display_name: <p>The display name of the limit.</p> <important> <p>This field can store any content. Escape or encode this content before displaying it on a webpage or any other system that might interpret the content of this field.</p> </important>
            amount_requirement_name: <p>The value that you specify as the <code>name</code> in the <code>amounts</code> field of the <code>hostRequirements</code> in a step of a job template to declare the limit requirement.</p>
            max_count: <p>The maximum number of resources constrained by this limit. When all of the resources are in use, steps that require the limit won't be scheduled until the resource is available.</p> <p>The <code>maxCount</code> must not be 0. If the value is -1, there is no restriction on the number of resources that can be acquired for this limit.</p>
            description: <p>A description of the limit. A description helps you identify the purpose of the limit.</p> <important> <p>This field can store any content. Escape or encode this content before displaying it on a webpage or any other system that might interpret the content of this field.</p> </important>

        Raises:
            capo_deadline.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action.</p>
            capo_deadline.errors.internal_server_error_exception.InternalServerErrorException: <p>Deadline Cloud can't process your request right now. Try again later.</p>
            capo_deadline.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_deadline.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You exceeded your service quota. Service quotas, also referred to as limits, are the maximum number of service resources or operations for your Amazon Web Services account.</p>
            capo_deadline.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a request rate quota.</p>
            capo_deadline.errors.validation_exception.ValidationException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.</p>
            capo_deadline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_deadline.types.create_limit_request.CreateLimitRequest]",
        ) -> OperationResponse[
            "capo_deadline.types.create_limit_response.CreateLimitResponse"
        ]:
            import capo_deadline._operations.deadline.create_limit

            output, http_response = (
                capo_deadline._operations.deadline.create_limit.create_limit(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_deadline.types.create_limit_request.CreateLimitRequest",
        ) -> dict[str, Any]:
            import capo_deadline.types.create_limit_request

            return capo_deadline.types.create_limit_request.redact_sensitive(input_)

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("CreateLimit", redact_input=_redact_input),
        )
        input_: capo_deadline.types.create_limit_request.CreateLimitRequest = {
            "farm_id": farm_id,
            "display_name": display_name,
            "amount_requirement_name": amount_requirement_name,
            "max_count": max_count,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if description is not None:
            input_["description"] = description

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_storage_profile(
        self,
        farm_id: "capo_deadline.types.farm_id.FarmId",
        display_name: "capo_deadline.types.resource_name.ResourceName",
        os_family: "capo_deadline.types.storage_profile_operating_system_family.StorageProfileOperatingSystemFamily",
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
        client_token: Optional["capo_deadline.types.client_token.ClientToken"] = None,
        file_system_locations: Optional[
            "capo_deadline.types.file_system_locations_list.FileSystemLocationsList"
        ] = None,
    ) -> "capo_deadline.types.create_storage_profile_response.CreateStorageProfileResponse":
        """<p>Creates a storage profile that specifies the operating system, file type, and file location of resources used on a farm.</p>

        Args:
            farm_id: <p>The farm ID of the farm to connect to the storage profile.</p>
            client_token: <p>The unique token which the server uses to recognize retries of the same request.</p>
            display_name: <p>The display name of the storage profile.</p> <important> <p>This field can store any content. Escape or encode this content before displaying it on a webpage or any other system that might interpret the content of this field.</p> </important>
            os_family: <p>The type of operating system (OS) for the storage profile.</p>
            file_system_locations: <p>File system paths to include in the storage profile.</p>

        Raises:
            capo_deadline.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action.</p>
            capo_deadline.errors.internal_server_error_exception.InternalServerErrorException: <p>Deadline Cloud can't process your request right now. Try again later.</p>
            capo_deadline.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_deadline.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You exceeded your service quota. Service quotas, also referred to as limits, are the maximum number of service resources or operations for your Amazon Web Services account.</p>
            capo_deadline.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a request rate quota.</p>
            capo_deadline.errors.validation_exception.ValidationException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.</p>
            capo_deadline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_deadline.types.create_storage_profile_request.CreateStorageProfileRequest]",
        ) -> OperationResponse[
            "capo_deadline.types.create_storage_profile_response.CreateStorageProfileResponse"
        ]:
            import capo_deadline._operations.deadline.create_storage_profile

            output, http_response = (
                capo_deadline._operations.deadline.create_storage_profile.create_storage_profile(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_deadline.types.create_storage_profile_request.CreateStorageProfileRequest",
        ) -> dict[str, Any]:
            import capo_deadline.types.create_storage_profile_request

            return capo_deadline.types.create_storage_profile_request.redact_sensitive(
                input_
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("CreateStorageProfile", redact_input=_redact_input),
        )
        input_: capo_deadline.types.create_storage_profile_request.CreateStorageProfileRequest = {
            "farm_id": farm_id,
            "display_name": display_name,
            "os_family": os_family,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if file_system_locations is not None:
            input_["file_system_locations"] = file_system_locations

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_limit(
        self,
        farm_id: "capo_deadline.types.farm_id.FarmId",
        limit_id: "capo_deadline.types.limit_id.LimitId",
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
    ) -> "capo_deadline.types.delete_limit_response.DeleteLimitResponse":
        """<p>Removes a limit from the specified farm. Before you delete a limit you must use the <code>DeleteQueueLimitAssociation</code> operation to remove the association with any queues. </p>

        Args:
            farm_id: <p>The unique identifier of the farm that contains the limit to delete.</p>
            limit_id: <p>The unique identifier of the limit to delete.</p>

        Raises:
            capo_deadline.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action.</p>
            capo_deadline.errors.internal_server_error_exception.InternalServerErrorException: <p>Deadline Cloud can't process your request right now. Try again later.</p>
            capo_deadline.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a request rate quota.</p>
            capo_deadline.errors.validation_exception.ValidationException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.</p>
            capo_deadline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_deadline.types.delete_limit_request.DeleteLimitRequest]",
        ) -> OperationResponse[
            "capo_deadline.types.delete_limit_response.DeleteLimitResponse"
        ]:
            import capo_deadline._operations.deadline.delete_limit

            output, http_response = (
                capo_deadline._operations.deadline.delete_limit.delete_limit(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteLimit")
        )
        input_: capo_deadline.types.delete_limit_request.DeleteLimitRequest = {
            "farm_id": farm_id,
            "limit_id": limit_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_storage_profile(
        self,
        farm_id: "capo_deadline.types.farm_id.FarmId",
        storage_profile_id: "capo_deadline.types.storage_profile_id.StorageProfileId",
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
    ) -> "capo_deadline.types.delete_storage_profile_response.DeleteStorageProfileResponse":
        """<p>Deletes a storage profile.</p>

        Args:
            farm_id: <p>The farm ID of the farm from which to remove the storage profile.</p>
            storage_profile_id: <p>The storage profile ID of the storage profile to delete.</p>

        Raises:
            capo_deadline.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action.</p>
            capo_deadline.errors.internal_server_error_exception.InternalServerErrorException: <p>Deadline Cloud can't process your request right now. Try again later.</p>
            capo_deadline.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a request rate quota.</p>
            capo_deadline.errors.validation_exception.ValidationException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.</p>
            capo_deadline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_deadline.types.delete_storage_profile_request.DeleteStorageProfileRequest]",
        ) -> OperationResponse[
            "capo_deadline.types.delete_storage_profile_response.DeleteStorageProfileResponse"
        ]:
            import capo_deadline._operations.deadline.delete_storage_profile

            output, http_response = (
                capo_deadline._operations.deadline.delete_storage_profile.delete_storage_profile(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteStorageProfile")
        )
        input_: capo_deadline.types.delete_storage_profile_request.DeleteStorageProfileRequest = {
            "farm_id": farm_id,
            "storage_profile_id": storage_profile_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def disassociate_member_from_farm(
        self,
        farm_id: "capo_deadline.types.farm_id.FarmId",
        principal_id: "capo_deadline.types.identity_center_principal_id.IdentityCenterPrincipalId",
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
    ) -> "capo_deadline.types.disassociate_member_from_farm_response.DisassociateMemberFromFarmResponse":
        """<p>Disassociates a member from a farm.</p>

        Args:
            farm_id: <p>The farm ID of the farm to disassociate from the member.</p>
            principal_id: <p>A member's principal ID to disassociate from a farm.</p>

        Raises:
            capo_deadline.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action.</p>
            capo_deadline.errors.internal_server_error_exception.InternalServerErrorException: <p>Deadline Cloud can't process your request right now. Try again later.</p>
            capo_deadline.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_deadline.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a request rate quota.</p>
            capo_deadline.errors.validation_exception.ValidationException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.</p>
            capo_deadline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_deadline.types.disassociate_member_from_farm_request.DisassociateMemberFromFarmRequest]",
        ) -> OperationResponse[
            "capo_deadline.types.disassociate_member_from_farm_response.DisassociateMemberFromFarmResponse"
        ]:
            import capo_deadline._operations.deadline.disassociate_member_from_farm

            output, http_response = (
                capo_deadline._operations.deadline.disassociate_member_from_farm.disassociate_member_from_farm(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DisassociateMemberFromFarm")
        )
        input_: capo_deadline.types.disassociate_member_from_farm_request.DisassociateMemberFromFarmRequest = {
            "farm_id": farm_id,
            "principal_id": principal_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_limit(
        self,
        farm_id: "capo_deadline.types.farm_id.FarmId",
        limit_id: "capo_deadline.types.limit_id.LimitId",
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
    ) -> "capo_deadline.types.get_limit_response.GetLimitResponse":
        """<p>Gets information about a specific limit.</p>

        Args:
            farm_id: <p>The unique identifier of the farm that contains the limit.</p>
            limit_id: <p>The unique identifier of the limit to return.</p>

        Raises:
            capo_deadline.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action.</p>
            capo_deadline.errors.internal_server_error_exception.InternalServerErrorException: <p>Deadline Cloud can't process your request right now. Try again later.</p>
            capo_deadline.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_deadline.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a request rate quota.</p>
            capo_deadline.errors.validation_exception.ValidationException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.</p>
            capo_deadline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_deadline.types.get_limit_request.GetLimitRequest]",
        ) -> OperationResponse[
            "capo_deadline.types.get_limit_response.GetLimitResponse"
        ]:
            import capo_deadline._operations.deadline.get_limit

            output, http_response = (
                capo_deadline._operations.deadline.get_limit.get_limit(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_deadline.types.get_limit_response.GetLimitResponse",
        ) -> dict[str, Any]:
            import capo_deadline.types.get_limit_response

            return capo_deadline.types.get_limit_response.redact_sensitive(output)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetLimit", redact_output=_redact_output)
        )
        input_: capo_deadline.types.get_limit_request.GetLimitRequest = {
            "farm_id": farm_id,
            "limit_id": limit_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_storage_profile(
        self,
        farm_id: "capo_deadline.types.farm_id.FarmId",
        storage_profile_id: "capo_deadline.types.storage_profile_id.StorageProfileId",
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
    ) -> "capo_deadline.types.get_storage_profile_response.GetStorageProfileResponse":
        """<p>Gets a storage profile.</p>

        Args:
            farm_id: <p>The farm ID for the storage profile.</p>
            storage_profile_id: <p>The storage profile ID.</p>

        Raises:
            capo_deadline.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action.</p>
            capo_deadline.errors.internal_server_error_exception.InternalServerErrorException: <p>Deadline Cloud can't process your request right now. Try again later.</p>
            capo_deadline.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_deadline.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a request rate quota.</p>
            capo_deadline.errors.validation_exception.ValidationException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.</p>
            capo_deadline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_deadline.types.get_storage_profile_request.GetStorageProfileRequest]",
        ) -> OperationResponse[
            "capo_deadline.types.get_storage_profile_response.GetStorageProfileResponse"
        ]:
            import capo_deadline._operations.deadline.get_storage_profile

            output, http_response = (
                capo_deadline._operations.deadline.get_storage_profile.get_storage_profile(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_deadline.types.get_storage_profile_response.GetStorageProfileResponse",
        ) -> dict[str, Any]:
            import capo_deadline.types.get_storage_profile_response

            return capo_deadline.types.get_storage_profile_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("GetStorageProfile", redact_output=_redact_output),
        )
        input_: capo_deadline.types.get_storage_profile_request.GetStorageProfileRequest = {
            "farm_id": farm_id,
            "storage_profile_id": storage_profile_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_farm_members(
        self,
        farm_id: "capo_deadline.types.farm_id.FarmId",
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
        next_token: Optional["capo_deadline.types.next_token.NextToken"] = None,
        max_results: Optional["capo_deadline.types.max_results.MaxResults"] = None,
    ) -> "capo_deadline.types.list_farm_members_response.ListFarmMembersResponse":
        """<p>Lists the members of a farm.</p>

        Args:
            farm_id: <p>The farm ID.</p>
            next_token: <p>The token for the next set of results, or <code>null</code> to start from the beginning.</p>
            max_results: <p>The maximum number of results to return. Use this parameter with <code>NextToken</code> to get results as a set of sequential pages.</p>

        Raises:
            capo_deadline.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action.</p>
            capo_deadline.errors.internal_server_error_exception.InternalServerErrorException: <p>Deadline Cloud can't process your request right now. Try again later.</p>
            capo_deadline.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_deadline.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a request rate quota.</p>
            capo_deadline.errors.validation_exception.ValidationException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.</p>
            capo_deadline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_deadline.types.list_farm_members_request.ListFarmMembersRequest]",
        ) -> OperationResponse[
            "capo_deadline.types.list_farm_members_response.ListFarmMembersResponse"
        ]:
            import capo_deadline._operations.deadline.list_farm_members

            output, http_response = (
                capo_deadline._operations.deadline.list_farm_members.list_farm_members(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListFarmMembers")
        )
        input_: capo_deadline.types.list_farm_members_request.ListFarmMembersRequest = {
            "farm_id": farm_id
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

    def list_limits(
        self,
        farm_id: "capo_deadline.types.farm_id.FarmId",
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
        next_token: Optional["capo_deadline.types.next_token.NextToken"] = None,
        max_results: Optional["capo_deadline.types.max_results.MaxResults"] = None,
    ) -> "capo_deadline.types.list_limits_response.ListLimitsResponse":
        """<p>Gets a list of limits defined in the specified farm.</p>

        Args:
            farm_id: <p>The unique identifier of the farm that contains the limits.</p>
            next_token: <p>The token for the next set of results, or <code>null</code> to start from the beginning.</p>
            max_results: <p>The maximum number of limits to return in each page of results.</p>

        Raises:
            capo_deadline.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action.</p>
            capo_deadline.errors.internal_server_error_exception.InternalServerErrorException: <p>Deadline Cloud can't process your request right now. Try again later.</p>
            capo_deadline.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_deadline.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a request rate quota.</p>
            capo_deadline.errors.validation_exception.ValidationException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.</p>
            capo_deadline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_deadline.types.list_limits_request.ListLimitsRequest]",
        ) -> OperationResponse[
            "capo_deadline.types.list_limits_response.ListLimitsResponse"
        ]:
            import capo_deadline._operations.deadline.list_limits

            output, http_response = (
                capo_deadline._operations.deadline.list_limits.list_limits(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListLimits")
        )
        input_: capo_deadline.types.list_limits_request.ListLimitsRequest = {
            "farm_id": farm_id
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

    def list_storage_profiles(
        self,
        farm_id: "capo_deadline.types.farm_id.FarmId",
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
        next_token: Optional["capo_deadline.types.next_token.NextToken"] = None,
        max_results: Optional["capo_deadline.types.max_results.MaxResults"] = None,
    ) -> (
        "capo_deadline.types.list_storage_profiles_response.ListStorageProfilesResponse"
    ):
        """<p>Lists storage profiles.</p>

        Args:
            farm_id: <p>The farm ID of the storage profile.</p>
            next_token: <p>The token for the next set of results, or <code>null</code> to start from the beginning.</p>
            max_results: <p>The maximum number of results to return. Use this parameter with <code>NextToken</code> to get results as a set of sequential pages.</p>

        Raises:
            capo_deadline.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action.</p>
            capo_deadline.errors.internal_server_error_exception.InternalServerErrorException: <p>Deadline Cloud can't process your request right now. Try again later.</p>
            capo_deadline.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_deadline.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a request rate quota.</p>
            capo_deadline.errors.validation_exception.ValidationException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.</p>
            capo_deadline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_deadline.types.list_storage_profiles_request.ListStorageProfilesRequest]",
        ) -> OperationResponse[
            "capo_deadline.types.list_storage_profiles_response.ListStorageProfilesResponse"
        ]:
            import capo_deadline._operations.deadline.list_storage_profiles

            output, http_response = (
                capo_deadline._operations.deadline.list_storage_profiles.list_storage_profiles(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListStorageProfiles")
        )
        input_: capo_deadline.types.list_storage_profiles_request.ListStorageProfilesRequest = {
            "farm_id": farm_id
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

    def update_limit(
        self,
        farm_id: "capo_deadline.types.farm_id.FarmId",
        limit_id: "capo_deadline.types.limit_id.LimitId",
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
        display_name: Optional["capo_deadline.types.resource_name.ResourceName"] = None,
        description: Optional["capo_deadline.types.description.Description"] = None,
        max_count: Optional["capo_deadline.types.max_count.MaxCount"] = None,
    ) -> "capo_deadline.types.update_limit_response.UpdateLimitResponse":
        """<p>Updates the properties of the specified limit. </p>

        Args:
            farm_id: <p>The unique identifier of the farm that contains the limit.</p>
            limit_id: <p>The unique identifier of the limit to update.</p>
            display_name: <p>The new display name of the limit.</p> <important> <p>This field can store any content. Escape or encode this content before displaying it on a webpage or any other system that might interpret the content of this field.</p> </important>
            description: <p>The new description of the limit.</p> <important> <p>This field can store any content. Escape or encode this content before displaying it on a webpage or any other system that might interpret the content of this field.</p> </important>
            max_count: <p>The maximum number of resources constrained by this limit. When all of the resources are in use, steps that require the limit won't be scheduled until the resource is available.</p> <p>If more than the new maximum number is currently in use, running jobs finish but no new jobs are started until the number of resources in use is below the new maximum number.</p> <p>The <code>maxCount</code> must not be 0. If the value is -1, there is no restriction on the number of resources that can be acquired for this limit.</p>

        Raises:
            capo_deadline.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action.</p>
            capo_deadline.errors.internal_server_error_exception.InternalServerErrorException: <p>Deadline Cloud can't process your request right now. Try again later.</p>
            capo_deadline.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_deadline.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a request rate quota.</p>
            capo_deadline.errors.validation_exception.ValidationException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.</p>
            capo_deadline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_deadline.types.update_limit_request.UpdateLimitRequest]",
        ) -> OperationResponse[
            "capo_deadline.types.update_limit_response.UpdateLimitResponse"
        ]:
            import capo_deadline._operations.deadline.update_limit

            output, http_response = (
                capo_deadline._operations.deadline.update_limit.update_limit(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_deadline.types.update_limit_request.UpdateLimitRequest",
        ) -> dict[str, Any]:
            import capo_deadline.types.update_limit_request

            return capo_deadline.types.update_limit_request.redact_sensitive(input_)

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("UpdateLimit", redact_input=_redact_input),
        )
        input_: capo_deadline.types.update_limit_request.UpdateLimitRequest = {
            "farm_id": farm_id,
            "limit_id": limit_id,
        }
        if display_name is not None:
            input_["display_name"] = display_name
        if description is not None:
            input_["description"] = description
        if max_count is not None:
            input_["max_count"] = max_count

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_storage_profile(
        self,
        farm_id: "capo_deadline.types.farm_id.FarmId",
        storage_profile_id: "capo_deadline.types.storage_profile_id.StorageProfileId",
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
        client_token: Optional["capo_deadline.types.client_token.ClientToken"] = None,
        display_name: Optional["capo_deadline.types.resource_name.ResourceName"] = None,
        os_family: Optional[
            "capo_deadline.types.storage_profile_operating_system_family.StorageProfileOperatingSystemFamily"
        ] = None,
        file_system_locations_to_add: Optional[
            "capo_deadline.types.file_system_locations_list.FileSystemLocationsList"
        ] = None,
        file_system_locations_to_remove: Optional[
            "capo_deadline.types.file_system_locations_list.FileSystemLocationsList"
        ] = None,
    ) -> "capo_deadline.types.update_storage_profile_response.UpdateStorageProfileResponse":
        """<p>Updates a storage profile.</p>

        Args:
            farm_id: <p>The farm ID to update.</p>
            storage_profile_id: <p>The storage profile ID to update.</p>
            client_token: <p>The unique token which the server uses to recognize retries of the same request.</p>
            display_name: <p>The display name of the storage profile to update.</p> <important> <p>This field can store any content. Escape or encode this content before displaying it on a webpage or any other system that might interpret the content of this field.</p> </important>
            os_family: <p>The OS system to update.</p>
            file_system_locations_to_add: <p>The file system location names to add.</p>
            file_system_locations_to_remove: <p>The file system location names to remove.</p>

        Raises:
            capo_deadline.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action.</p>
            capo_deadline.errors.internal_server_error_exception.InternalServerErrorException: <p>Deadline Cloud can't process your request right now. Try again later.</p>
            capo_deadline.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_deadline.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a request rate quota.</p>
            capo_deadline.errors.validation_exception.ValidationException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.</p>
            capo_deadline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_deadline.types.update_storage_profile_request.UpdateStorageProfileRequest]",
        ) -> OperationResponse[
            "capo_deadline.types.update_storage_profile_response.UpdateStorageProfileResponse"
        ]:
            import capo_deadline._operations.deadline.update_storage_profile

            output, http_response = (
                capo_deadline._operations.deadline.update_storage_profile.update_storage_profile(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_deadline.types.update_storage_profile_request.UpdateStorageProfileRequest",
        ) -> dict[str, Any]:
            import capo_deadline.types.update_storage_profile_request

            return capo_deadline.types.update_storage_profile_request.redact_sensitive(
                input_
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("UpdateStorageProfile", redact_input=_redact_input),
        )
        input_: capo_deadline.types.update_storage_profile_request.UpdateStorageProfileRequest = {
            "farm_id": farm_id,
            "storage_profile_id": storage_profile_id,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if display_name is not None:
            input_["display_name"] = display_name
        if os_family is not None:
            input_["os_family"] = os_family
        if file_system_locations_to_add is not None:
            input_["file_system_locations_to_add"] = file_system_locations_to_add
        if file_system_locations_to_remove is not None:
            input_["file_system_locations_to_remove"] = file_system_locations_to_remove

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncFarmResource:
    def __init__(self, service: AsyncdeadlineClient) -> None:
        self._service = service

    async def create(
        self,
        display_name: "capo_deadline.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AsyncdeadlineClientConfig] = None,
        client_token: Optional["capo_deadline.types.client_token.ClientToken"] = None,
        description: Optional["capo_deadline.types.description.Description"] = None,
        kms_key_arn: Optional["capo_deadline.types.kms_key_arn.KmsKeyArn"] = None,
        cost_scale_factor: Optional[
            "capo_deadline.types.cost_scale_factor.CostScaleFactor"
        ] = None,
        tags: Optional["capo_deadline.types.tags.Tags"] = None,
    ) -> "capo_deadline.types.create_farm_response.CreateFarmResponse":
        """<p>Creates a farm to allow space for queues and fleets. Farms are the space where the components of your renders gather and are pieced together in the cloud. Farms contain budgets and allow you to enforce permissions. Deadline Cloud farms are a useful container for large projects.</p>

        Args:
            client_token: <p>The unique token which the server uses to recognize retries of the same request.</p>
            display_name: <p>The display name of the farm.</p> <important> <p>This field can store any content. Escape or encode this content before displaying it on a webpage or any other system that might interpret the content of this field.</p> </important>
            description: <p>The description of the farm.</p> <important> <p>This field can store any content. Escape or encode this content before displaying it on a webpage or any other system that might interpret the content of this field.</p> </important>
            kms_key_arn: <p>The ARN of the KMS key to use on the farm.</p>
            cost_scale_factor: <p>A multiplier applied to the farm's calculated costs for usage data and budget tracking. A value less than 1 represents a discount, a value greater than 1 represents a premium, and a value of 1 represents no adjustment. The default value is 1.</p>
            tags: <p>The tags to add to your farm. Each tag consists of a tag key and a tag value. Tag keys and values are both required, but tag values can be empty strings.</p>

        Raises:
            capo_deadline.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action.</p>
            capo_deadline.errors.internal_server_error_exception.InternalServerErrorException: <p>Deadline Cloud can't process your request right now. Try again later.</p>
            capo_deadline.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_deadline.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You exceeded your service quota. Service quotas, also referred to as limits, are the maximum number of service resources or operations for your Amazon Web Services account.</p>
            capo_deadline.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a request rate quota.</p>
            capo_deadline.errors.validation_exception.ValidationException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.</p>
            capo_deadline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_deadline.types.create_farm_request.CreateFarmRequest]",
        ) -> AsyncOperationResponse[
            "capo_deadline.types.create_farm_response.CreateFarmResponse"
        ]:
            import capo_deadline._operations.deadline.create_farm

            (
                output,
                http_response,
            ) = await capo_deadline._operations.deadline.create_farm.async_create_farm(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_deadline.types.create_farm_request.CreateFarmRequest",
        ) -> dict[str, Any]:
            import capo_deadline.types.create_farm_request

            return capo_deadline.types.create_farm_request.redact_sensitive(input_)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("CreateFarm", redact_input=_redact_input)
        )
        input_: capo_deadline.types.create_farm_request.CreateFarmRequest = {
            "display_name": display_name
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if description is not None:
            input_["description"] = description
        if kms_key_arn is not None:
            input_["kms_key_arn"] = kms_key_arn
        if cost_scale_factor is not None:
            input_["cost_scale_factor"] = cost_scale_factor
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
        farm_id: "capo_deadline.types.farm_id.FarmId",
        *,
        config_overrides: Optional[AsyncdeadlineClientConfig] = None,
    ) -> "capo_deadline.types.get_farm_response.GetFarmResponse":
        """<p>Get a farm.</p>

        Args:
            farm_id: <p>The farm ID of the farm.</p>

        Raises:
            capo_deadline.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action.</p>
            capo_deadline.errors.internal_server_error_exception.InternalServerErrorException: <p>Deadline Cloud can't process your request right now. Try again later.</p>
            capo_deadline.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_deadline.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a request rate quota.</p>
            capo_deadline.errors.validation_exception.ValidationException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.</p>
            capo_deadline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_deadline.types.get_farm_request.GetFarmRequest]",
        ) -> AsyncOperationResponse[
            "capo_deadline.types.get_farm_response.GetFarmResponse"
        ]:
            import capo_deadline._operations.deadline.get_farm

            (
                output,
                http_response,
            ) = await capo_deadline._operations.deadline.get_farm.async_get_farm(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_deadline.types.get_farm_response.GetFarmResponse",
        ) -> dict[str, Any]:
            import capo_deadline.types.get_farm_response

            return capo_deadline.types.get_farm_response.redact_sensitive(output)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetFarm", redact_output=_redact_output)
        )
        input_: capo_deadline.types.get_farm_request.GetFarmRequest = {
            "farm_id": farm_id
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
        farm_id: "capo_deadline.types.farm_id.FarmId",
        *,
        config_overrides: Optional[AsyncdeadlineClientConfig] = None,
        display_name: Optional["capo_deadline.types.resource_name.ResourceName"] = None,
        description: Optional["capo_deadline.types.description.Description"] = None,
        cost_scale_factor: Optional[
            "capo_deadline.types.cost_scale_factor.CostScaleFactor"
        ] = None,
    ) -> "capo_deadline.types.update_farm_response.UpdateFarmResponse":
        """<p>Updates a farm.</p>

        Args:
            farm_id: <p>The farm ID to update.</p>
            display_name: <p>The display name of the farm to update.</p> <important> <p>This field can store any content. Escape or encode this content before displaying it on a webpage or any other system that might interpret the content of this field.</p> </important>
            description: <p>The description of the farm to update.</p> <important> <p>This field can store any content. Escape or encode this content before displaying it on a webpage or any other system that might interpret the content of this field.</p> </important>
            cost_scale_factor: <p>A multiplier applied to the farm's calculated costs for usage data and budget tracking. A value less than 1 represents a discount, a value greater than 1 represents a premium, and a value of 1 represents no adjustment.</p>

        Raises:
            capo_deadline.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action.</p>
            capo_deadline.errors.internal_server_error_exception.InternalServerErrorException: <p>Deadline Cloud can't process your request right now. Try again later.</p>
            capo_deadline.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_deadline.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a request rate quota.</p>
            capo_deadline.errors.validation_exception.ValidationException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.</p>
            capo_deadline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_deadline.types.update_farm_request.UpdateFarmRequest]",
        ) -> AsyncOperationResponse[
            "capo_deadline.types.update_farm_response.UpdateFarmResponse"
        ]:
            import capo_deadline._operations.deadline.update_farm

            (
                output,
                http_response,
            ) = await capo_deadline._operations.deadline.update_farm.async_update_farm(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_deadline.types.update_farm_request.UpdateFarmRequest",
        ) -> dict[str, Any]:
            import capo_deadline.types.update_farm_request

            return capo_deadline.types.update_farm_request.redact_sensitive(input_)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("UpdateFarm", redact_input=_redact_input)
        )
        input_: capo_deadline.types.update_farm_request.UpdateFarmRequest = {
            "farm_id": farm_id
        }
        if display_name is not None:
            input_["display_name"] = display_name
        if description is not None:
            input_["description"] = description
        if cost_scale_factor is not None:
            input_["cost_scale_factor"] = cost_scale_factor

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete(
        self,
        farm_id: "capo_deadline.types.farm_id.FarmId",
        *,
        config_overrides: Optional[AsyncdeadlineClientConfig] = None,
    ) -> "capo_deadline.types.delete_farm_response.DeleteFarmResponse":
        """<p>Deletes a farm.</p>

        Args:
            farm_id: <p>The farm ID of the farm to delete.</p>

        Raises:
            capo_deadline.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action.</p>
            capo_deadline.errors.internal_server_error_exception.InternalServerErrorException: <p>Deadline Cloud can't process your request right now. Try again later.</p>
            capo_deadline.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_deadline.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a request rate quota.</p>
            capo_deadline.errors.validation_exception.ValidationException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.</p>
            capo_deadline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_deadline.types.delete_farm_request.DeleteFarmRequest]",
        ) -> AsyncOperationResponse[
            "capo_deadline.types.delete_farm_response.DeleteFarmResponse"
        ]:
            import capo_deadline._operations.deadline.delete_farm

            (
                output,
                http_response,
            ) = await capo_deadline._operations.deadline.delete_farm.async_delete_farm(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteFarm")
        )
        input_: capo_deadline.types.delete_farm_request.DeleteFarmRequest = {
            "farm_id": farm_id
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
        config_overrides: Optional[AsyncdeadlineClientConfig] = None,
        next_token: Optional["capo_deadline.types.next_token.NextToken"] = None,
        max_results: Optional["capo_deadline.types.max_results.MaxResults"] = None,
        principal_id: Optional[
            "capo_deadline.types.identity_center_principal_id.IdentityCenterPrincipalId"
        ] = None,
    ) -> "capo_deadline.types.list_farms_response.ListFarmsResponse":
        """<p>Lists farms.</p>

        Args:
            next_token: <p>The token for the next set of results, or <code>null</code> to start from the beginning.</p>
            max_results: <p>The maximum number of results to return. Use this parameter with <code>NextToken</code> to get results as a set of sequential pages.</p>
            principal_id: <p>The principal ID of the member to list on the farm.</p>

        Raises:
            capo_deadline.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action.</p>
            capo_deadline.errors.internal_server_error_exception.InternalServerErrorException: <p>Deadline Cloud can't process your request right now. Try again later.</p>
            capo_deadline.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a request rate quota.</p>
            capo_deadline.errors.validation_exception.ValidationException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.</p>
            capo_deadline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_deadline.types.list_farms_request.ListFarmsRequest]",
        ) -> AsyncOperationResponse[
            "capo_deadline.types.list_farms_response.ListFarmsResponse"
        ]:
            import capo_deadline._operations.deadline.list_farms

            (
                output,
                http_response,
            ) = await capo_deadline._operations.deadline.list_farms.async_list_farms(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListFarms")
        )
        input_: capo_deadline.types.list_farms_request.ListFarmsRequest = {}
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if principal_id is not None:
            input_["principal_id"] = principal_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def associate_member_to_farm(
        self,
        farm_id: "capo_deadline.types.farm_id.FarmId",
        principal_type: "capo_deadline.types.deadline_principal_type.DeadlinePrincipalType",
        identity_store_id: "capo_deadline.types.identity_store_id.IdentityStoreId",
        membership_level: "capo_deadline.types.membership_level.MembershipLevel",
        principal_id: "capo_deadline.types.identity_center_principal_id.IdentityCenterPrincipalId",
        *,
        config_overrides: Optional[AsyncdeadlineClientConfig] = None,
        identity_center_region: Optional["capo_deadline.types.region.Region"] = None,
    ) -> "capo_deadline.types.associate_member_to_farm_response.AssociateMemberToFarmResponse":
        """<p>Assigns a farm membership level to a member.</p>

        Args:
            farm_id: <p>The ID of the farm to associate with the member.</p>
            principal_type: <p>The principal type of the member to associate with the farm.</p>
            identity_store_id: <p>The identity store ID of the member to associate with the farm.</p>
            membership_level: <p>The principal's membership level for the associated farm.</p>
            principal_id: <p>The member's principal ID to associate with the farm.</p>
            identity_center_region: <p>The Region of the IAM Identity Center instance. If not provided, the service defaults to the Region of the farm.</p>

        Raises:
            capo_deadline.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action.</p>
            capo_deadline.errors.internal_server_error_exception.InternalServerErrorException: <p>Deadline Cloud can't process your request right now. Try again later.</p>
            capo_deadline.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_deadline.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You exceeded your service quota. Service quotas, also referred to as limits, are the maximum number of service resources or operations for your Amazon Web Services account.</p>
            capo_deadline.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a request rate quota.</p>
            capo_deadline.errors.validation_exception.ValidationException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.</p>
            capo_deadline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_deadline.types.associate_member_to_farm_request.AssociateMemberToFarmRequest]",
        ) -> AsyncOperationResponse[
            "capo_deadline.types.associate_member_to_farm_response.AssociateMemberToFarmResponse"
        ]:
            import capo_deadline._operations.deadline.associate_member_to_farm

            (
                output,
                http_response,
            ) = await capo_deadline._operations.deadline.associate_member_to_farm.async_associate_member_to_farm(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("AssociateMemberToFarm")
        )
        input_: capo_deadline.types.associate_member_to_farm_request.AssociateMemberToFarmRequest = {
            "farm_id": farm_id,
            "principal_type": principal_type,
            "identity_store_id": identity_store_id,
            "membership_level": membership_level,
            "principal_id": principal_id,
        }
        if identity_center_region is not None:
            input_["identity_center_region"] = identity_center_region

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_limit(
        self,
        farm_id: "capo_deadline.types.farm_id.FarmId",
        display_name: "capo_deadline.types.resource_name.ResourceName",
        amount_requirement_name: "capo_deadline.types.amount_requirement_name.AmountRequirementName",
        max_count: "capo_deadline.types.max_count.MaxCount",
        *,
        config_overrides: Optional[AsyncdeadlineClientConfig] = None,
        client_token: Optional["capo_deadline.types.client_token.ClientToken"] = None,
        description: Optional["capo_deadline.types.description.Description"] = None,
    ) -> "capo_deadline.types.create_limit_response.CreateLimitResponse":
        """<p>Creates a limit that manages the distribution of shared resources, such as floating licenses. A limit can throttle work assignments, help manage workloads, and track current usage. Before you use a limit, you must associate the limit with one or more queues. </p> <p>You must add the <code>amountRequirementName</code> to a step in a job template to declare the limit requirement.</p>

        Args:
            farm_id: <p>The farm ID of the farm that contains the limit.</p>
            client_token: <p>The unique token which the server uses to recognize retries of the same request.</p>
            display_name: <p>The display name of the limit.</p> <important> <p>This field can store any content. Escape or encode this content before displaying it on a webpage or any other system that might interpret the content of this field.</p> </important>
            amount_requirement_name: <p>The value that you specify as the <code>name</code> in the <code>amounts</code> field of the <code>hostRequirements</code> in a step of a job template to declare the limit requirement.</p>
            max_count: <p>The maximum number of resources constrained by this limit. When all of the resources are in use, steps that require the limit won't be scheduled until the resource is available.</p> <p>The <code>maxCount</code> must not be 0. If the value is -1, there is no restriction on the number of resources that can be acquired for this limit.</p>
            description: <p>A description of the limit. A description helps you identify the purpose of the limit.</p> <important> <p>This field can store any content. Escape or encode this content before displaying it on a webpage or any other system that might interpret the content of this field.</p> </important>

        Raises:
            capo_deadline.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action.</p>
            capo_deadline.errors.internal_server_error_exception.InternalServerErrorException: <p>Deadline Cloud can't process your request right now. Try again later.</p>
            capo_deadline.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_deadline.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You exceeded your service quota. Service quotas, also referred to as limits, are the maximum number of service resources or operations for your Amazon Web Services account.</p>
            capo_deadline.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a request rate quota.</p>
            capo_deadline.errors.validation_exception.ValidationException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.</p>
            capo_deadline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_deadline.types.create_limit_request.CreateLimitRequest]",
        ) -> AsyncOperationResponse[
            "capo_deadline.types.create_limit_response.CreateLimitResponse"
        ]:
            import capo_deadline._operations.deadline.create_limit

            (
                output,
                http_response,
            ) = await capo_deadline._operations.deadline.create_limit.async_create_limit(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_deadline.types.create_limit_request.CreateLimitRequest",
        ) -> dict[str, Any]:
            import capo_deadline.types.create_limit_request

            return capo_deadline.types.create_limit_request.redact_sensitive(input_)

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("CreateLimit", redact_input=_redact_input),
        )
        input_: capo_deadline.types.create_limit_request.CreateLimitRequest = {
            "farm_id": farm_id,
            "display_name": display_name,
            "amount_requirement_name": amount_requirement_name,
            "max_count": max_count,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if description is not None:
            input_["description"] = description

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_storage_profile(
        self,
        farm_id: "capo_deadline.types.farm_id.FarmId",
        display_name: "capo_deadline.types.resource_name.ResourceName",
        os_family: "capo_deadline.types.storage_profile_operating_system_family.StorageProfileOperatingSystemFamily",
        *,
        config_overrides: Optional[AsyncdeadlineClientConfig] = None,
        client_token: Optional["capo_deadline.types.client_token.ClientToken"] = None,
        file_system_locations: Optional[
            "capo_deadline.types.file_system_locations_list.FileSystemLocationsList"
        ] = None,
    ) -> "capo_deadline.types.create_storage_profile_response.CreateStorageProfileResponse":
        """<p>Creates a storage profile that specifies the operating system, file type, and file location of resources used on a farm.</p>

        Args:
            farm_id: <p>The farm ID of the farm to connect to the storage profile.</p>
            client_token: <p>The unique token which the server uses to recognize retries of the same request.</p>
            display_name: <p>The display name of the storage profile.</p> <important> <p>This field can store any content. Escape or encode this content before displaying it on a webpage or any other system that might interpret the content of this field.</p> </important>
            os_family: <p>The type of operating system (OS) for the storage profile.</p>
            file_system_locations: <p>File system paths to include in the storage profile.</p>

        Raises:
            capo_deadline.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action.</p>
            capo_deadline.errors.internal_server_error_exception.InternalServerErrorException: <p>Deadline Cloud can't process your request right now. Try again later.</p>
            capo_deadline.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_deadline.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You exceeded your service quota. Service quotas, also referred to as limits, are the maximum number of service resources or operations for your Amazon Web Services account.</p>
            capo_deadline.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a request rate quota.</p>
            capo_deadline.errors.validation_exception.ValidationException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.</p>
            capo_deadline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_deadline.types.create_storage_profile_request.CreateStorageProfileRequest]",
        ) -> AsyncOperationResponse[
            "capo_deadline.types.create_storage_profile_response.CreateStorageProfileResponse"
        ]:
            import capo_deadline._operations.deadline.create_storage_profile

            (
                output,
                http_response,
            ) = await capo_deadline._operations.deadline.create_storage_profile.async_create_storage_profile(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_deadline.types.create_storage_profile_request.CreateStorageProfileRequest",
        ) -> dict[str, Any]:
            import capo_deadline.types.create_storage_profile_request

            return capo_deadline.types.create_storage_profile_request.redact_sensitive(
                input_
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("CreateStorageProfile", redact_input=_redact_input),
        )
        input_: capo_deadline.types.create_storage_profile_request.CreateStorageProfileRequest = {
            "farm_id": farm_id,
            "display_name": display_name,
            "os_family": os_family,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if file_system_locations is not None:
            input_["file_system_locations"] = file_system_locations

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_limit(
        self,
        farm_id: "capo_deadline.types.farm_id.FarmId",
        limit_id: "capo_deadline.types.limit_id.LimitId",
        *,
        config_overrides: Optional[AsyncdeadlineClientConfig] = None,
    ) -> "capo_deadline.types.delete_limit_response.DeleteLimitResponse":
        """<p>Removes a limit from the specified farm. Before you delete a limit you must use the <code>DeleteQueueLimitAssociation</code> operation to remove the association with any queues. </p>

        Args:
            farm_id: <p>The unique identifier of the farm that contains the limit to delete.</p>
            limit_id: <p>The unique identifier of the limit to delete.</p>

        Raises:
            capo_deadline.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action.</p>
            capo_deadline.errors.internal_server_error_exception.InternalServerErrorException: <p>Deadline Cloud can't process your request right now. Try again later.</p>
            capo_deadline.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a request rate quota.</p>
            capo_deadline.errors.validation_exception.ValidationException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.</p>
            capo_deadline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_deadline.types.delete_limit_request.DeleteLimitRequest]",
        ) -> AsyncOperationResponse[
            "capo_deadline.types.delete_limit_response.DeleteLimitResponse"
        ]:
            import capo_deadline._operations.deadline.delete_limit

            (
                output,
                http_response,
            ) = await capo_deadline._operations.deadline.delete_limit.async_delete_limit(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteLimit")
        )
        input_: capo_deadline.types.delete_limit_request.DeleteLimitRequest = {
            "farm_id": farm_id,
            "limit_id": limit_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_storage_profile(
        self,
        farm_id: "capo_deadline.types.farm_id.FarmId",
        storage_profile_id: "capo_deadline.types.storage_profile_id.StorageProfileId",
        *,
        config_overrides: Optional[AsyncdeadlineClientConfig] = None,
    ) -> "capo_deadline.types.delete_storage_profile_response.DeleteStorageProfileResponse":
        """<p>Deletes a storage profile.</p>

        Args:
            farm_id: <p>The farm ID of the farm from which to remove the storage profile.</p>
            storage_profile_id: <p>The storage profile ID of the storage profile to delete.</p>

        Raises:
            capo_deadline.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action.</p>
            capo_deadline.errors.internal_server_error_exception.InternalServerErrorException: <p>Deadline Cloud can't process your request right now. Try again later.</p>
            capo_deadline.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a request rate quota.</p>
            capo_deadline.errors.validation_exception.ValidationException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.</p>
            capo_deadline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_deadline.types.delete_storage_profile_request.DeleteStorageProfileRequest]",
        ) -> AsyncOperationResponse[
            "capo_deadline.types.delete_storage_profile_response.DeleteStorageProfileResponse"
        ]:
            import capo_deadline._operations.deadline.delete_storage_profile

            (
                output,
                http_response,
            ) = await capo_deadline._operations.deadline.delete_storage_profile.async_delete_storage_profile(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteStorageProfile")
        )
        input_: capo_deadline.types.delete_storage_profile_request.DeleteStorageProfileRequest = {
            "farm_id": farm_id,
            "storage_profile_id": storage_profile_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def disassociate_member_from_farm(
        self,
        farm_id: "capo_deadline.types.farm_id.FarmId",
        principal_id: "capo_deadline.types.identity_center_principal_id.IdentityCenterPrincipalId",
        *,
        config_overrides: Optional[AsyncdeadlineClientConfig] = None,
    ) -> "capo_deadline.types.disassociate_member_from_farm_response.DisassociateMemberFromFarmResponse":
        """<p>Disassociates a member from a farm.</p>

        Args:
            farm_id: <p>The farm ID of the farm to disassociate from the member.</p>
            principal_id: <p>A member's principal ID to disassociate from a farm.</p>

        Raises:
            capo_deadline.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action.</p>
            capo_deadline.errors.internal_server_error_exception.InternalServerErrorException: <p>Deadline Cloud can't process your request right now. Try again later.</p>
            capo_deadline.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_deadline.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a request rate quota.</p>
            capo_deadline.errors.validation_exception.ValidationException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.</p>
            capo_deadline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_deadline.types.disassociate_member_from_farm_request.DisassociateMemberFromFarmRequest]",
        ) -> AsyncOperationResponse[
            "capo_deadline.types.disassociate_member_from_farm_response.DisassociateMemberFromFarmResponse"
        ]:
            import capo_deadline._operations.deadline.disassociate_member_from_farm

            (
                output,
                http_response,
            ) = await capo_deadline._operations.deadline.disassociate_member_from_farm.async_disassociate_member_from_farm(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DisassociateMemberFromFarm")
        )
        input_: capo_deadline.types.disassociate_member_from_farm_request.DisassociateMemberFromFarmRequest = {
            "farm_id": farm_id,
            "principal_id": principal_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_limit(
        self,
        farm_id: "capo_deadline.types.farm_id.FarmId",
        limit_id: "capo_deadline.types.limit_id.LimitId",
        *,
        config_overrides: Optional[AsyncdeadlineClientConfig] = None,
    ) -> "capo_deadline.types.get_limit_response.GetLimitResponse":
        """<p>Gets information about a specific limit.</p>

        Args:
            farm_id: <p>The unique identifier of the farm that contains the limit.</p>
            limit_id: <p>The unique identifier of the limit to return.</p>

        Raises:
            capo_deadline.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action.</p>
            capo_deadline.errors.internal_server_error_exception.InternalServerErrorException: <p>Deadline Cloud can't process your request right now. Try again later.</p>
            capo_deadline.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_deadline.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a request rate quota.</p>
            capo_deadline.errors.validation_exception.ValidationException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.</p>
            capo_deadline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_deadline.types.get_limit_request.GetLimitRequest]",
        ) -> AsyncOperationResponse[
            "capo_deadline.types.get_limit_response.GetLimitResponse"
        ]:
            import capo_deadline._operations.deadline.get_limit

            (
                output,
                http_response,
            ) = await capo_deadline._operations.deadline.get_limit.async_get_limit(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_deadline.types.get_limit_response.GetLimitResponse",
        ) -> dict[str, Any]:
            import capo_deadline.types.get_limit_response

            return capo_deadline.types.get_limit_response.redact_sensitive(output)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetLimit", redact_output=_redact_output)
        )
        input_: capo_deadline.types.get_limit_request.GetLimitRequest = {
            "farm_id": farm_id,
            "limit_id": limit_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_storage_profile(
        self,
        farm_id: "capo_deadline.types.farm_id.FarmId",
        storage_profile_id: "capo_deadline.types.storage_profile_id.StorageProfileId",
        *,
        config_overrides: Optional[AsyncdeadlineClientConfig] = None,
    ) -> "capo_deadline.types.get_storage_profile_response.GetStorageProfileResponse":
        """<p>Gets a storage profile.</p>

        Args:
            farm_id: <p>The farm ID for the storage profile.</p>
            storage_profile_id: <p>The storage profile ID.</p>

        Raises:
            capo_deadline.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action.</p>
            capo_deadline.errors.internal_server_error_exception.InternalServerErrorException: <p>Deadline Cloud can't process your request right now. Try again later.</p>
            capo_deadline.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_deadline.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a request rate quota.</p>
            capo_deadline.errors.validation_exception.ValidationException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.</p>
            capo_deadline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_deadline.types.get_storage_profile_request.GetStorageProfileRequest]",
        ) -> AsyncOperationResponse[
            "capo_deadline.types.get_storage_profile_response.GetStorageProfileResponse"
        ]:
            import capo_deadline._operations.deadline.get_storage_profile

            (
                output,
                http_response,
            ) = await capo_deadline._operations.deadline.get_storage_profile.async_get_storage_profile(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_deadline.types.get_storage_profile_response.GetStorageProfileResponse",
        ) -> dict[str, Any]:
            import capo_deadline.types.get_storage_profile_response

            return capo_deadline.types.get_storage_profile_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("GetStorageProfile", redact_output=_redact_output),
        )
        input_: capo_deadline.types.get_storage_profile_request.GetStorageProfileRequest = {
            "farm_id": farm_id,
            "storage_profile_id": storage_profile_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_farm_members(
        self,
        farm_id: "capo_deadline.types.farm_id.FarmId",
        *,
        config_overrides: Optional[AsyncdeadlineClientConfig] = None,
        next_token: Optional["capo_deadline.types.next_token.NextToken"] = None,
        max_results: Optional["capo_deadline.types.max_results.MaxResults"] = None,
    ) -> "capo_deadline.types.list_farm_members_response.ListFarmMembersResponse":
        """<p>Lists the members of a farm.</p>

        Args:
            farm_id: <p>The farm ID.</p>
            next_token: <p>The token for the next set of results, or <code>null</code> to start from the beginning.</p>
            max_results: <p>The maximum number of results to return. Use this parameter with <code>NextToken</code> to get results as a set of sequential pages.</p>

        Raises:
            capo_deadline.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action.</p>
            capo_deadline.errors.internal_server_error_exception.InternalServerErrorException: <p>Deadline Cloud can't process your request right now. Try again later.</p>
            capo_deadline.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_deadline.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a request rate quota.</p>
            capo_deadline.errors.validation_exception.ValidationException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.</p>
            capo_deadline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_deadline.types.list_farm_members_request.ListFarmMembersRequest]",
        ) -> AsyncOperationResponse[
            "capo_deadline.types.list_farm_members_response.ListFarmMembersResponse"
        ]:
            import capo_deadline._operations.deadline.list_farm_members

            (
                output,
                http_response,
            ) = await capo_deadline._operations.deadline.list_farm_members.async_list_farm_members(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListFarmMembers")
        )
        input_: capo_deadline.types.list_farm_members_request.ListFarmMembersRequest = {
            "farm_id": farm_id
        }
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

    async def list_limits(
        self,
        farm_id: "capo_deadline.types.farm_id.FarmId",
        *,
        config_overrides: Optional[AsyncdeadlineClientConfig] = None,
        next_token: Optional["capo_deadline.types.next_token.NextToken"] = None,
        max_results: Optional["capo_deadline.types.max_results.MaxResults"] = None,
    ) -> "capo_deadline.types.list_limits_response.ListLimitsResponse":
        """<p>Gets a list of limits defined in the specified farm.</p>

        Args:
            farm_id: <p>The unique identifier of the farm that contains the limits.</p>
            next_token: <p>The token for the next set of results, or <code>null</code> to start from the beginning.</p>
            max_results: <p>The maximum number of limits to return in each page of results.</p>

        Raises:
            capo_deadline.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action.</p>
            capo_deadline.errors.internal_server_error_exception.InternalServerErrorException: <p>Deadline Cloud can't process your request right now. Try again later.</p>
            capo_deadline.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_deadline.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a request rate quota.</p>
            capo_deadline.errors.validation_exception.ValidationException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.</p>
            capo_deadline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_deadline.types.list_limits_request.ListLimitsRequest]",
        ) -> AsyncOperationResponse[
            "capo_deadline.types.list_limits_response.ListLimitsResponse"
        ]:
            import capo_deadline._operations.deadline.list_limits

            (
                output,
                http_response,
            ) = await capo_deadline._operations.deadline.list_limits.async_list_limits(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListLimits")
        )
        input_: capo_deadline.types.list_limits_request.ListLimitsRequest = {
            "farm_id": farm_id
        }
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

    async def list_storage_profiles(
        self,
        farm_id: "capo_deadline.types.farm_id.FarmId",
        *,
        config_overrides: Optional[AsyncdeadlineClientConfig] = None,
        next_token: Optional["capo_deadline.types.next_token.NextToken"] = None,
        max_results: Optional["capo_deadline.types.max_results.MaxResults"] = None,
    ) -> (
        "capo_deadline.types.list_storage_profiles_response.ListStorageProfilesResponse"
    ):
        """<p>Lists storage profiles.</p>

        Args:
            farm_id: <p>The farm ID of the storage profile.</p>
            next_token: <p>The token for the next set of results, or <code>null</code> to start from the beginning.</p>
            max_results: <p>The maximum number of results to return. Use this parameter with <code>NextToken</code> to get results as a set of sequential pages.</p>

        Raises:
            capo_deadline.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action.</p>
            capo_deadline.errors.internal_server_error_exception.InternalServerErrorException: <p>Deadline Cloud can't process your request right now. Try again later.</p>
            capo_deadline.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_deadline.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a request rate quota.</p>
            capo_deadline.errors.validation_exception.ValidationException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.</p>
            capo_deadline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_deadline.types.list_storage_profiles_request.ListStorageProfilesRequest]",
        ) -> AsyncOperationResponse[
            "capo_deadline.types.list_storage_profiles_response.ListStorageProfilesResponse"
        ]:
            import capo_deadline._operations.deadline.list_storage_profiles

            (
                output,
                http_response,
            ) = await capo_deadline._operations.deadline.list_storage_profiles.async_list_storage_profiles(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListStorageProfiles")
        )
        input_: capo_deadline.types.list_storage_profiles_request.ListStorageProfilesRequest = {
            "farm_id": farm_id
        }
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

    async def update_limit(
        self,
        farm_id: "capo_deadline.types.farm_id.FarmId",
        limit_id: "capo_deadline.types.limit_id.LimitId",
        *,
        config_overrides: Optional[AsyncdeadlineClientConfig] = None,
        display_name: Optional["capo_deadline.types.resource_name.ResourceName"] = None,
        description: Optional["capo_deadline.types.description.Description"] = None,
        max_count: Optional["capo_deadline.types.max_count.MaxCount"] = None,
    ) -> "capo_deadline.types.update_limit_response.UpdateLimitResponse":
        """<p>Updates the properties of the specified limit. </p>

        Args:
            farm_id: <p>The unique identifier of the farm that contains the limit.</p>
            limit_id: <p>The unique identifier of the limit to update.</p>
            display_name: <p>The new display name of the limit.</p> <important> <p>This field can store any content. Escape or encode this content before displaying it on a webpage or any other system that might interpret the content of this field.</p> </important>
            description: <p>The new description of the limit.</p> <important> <p>This field can store any content. Escape or encode this content before displaying it on a webpage or any other system that might interpret the content of this field.</p> </important>
            max_count: <p>The maximum number of resources constrained by this limit. When all of the resources are in use, steps that require the limit won't be scheduled until the resource is available.</p> <p>If more than the new maximum number is currently in use, running jobs finish but no new jobs are started until the number of resources in use is below the new maximum number.</p> <p>The <code>maxCount</code> must not be 0. If the value is -1, there is no restriction on the number of resources that can be acquired for this limit.</p>

        Raises:
            capo_deadline.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action.</p>
            capo_deadline.errors.internal_server_error_exception.InternalServerErrorException: <p>Deadline Cloud can't process your request right now. Try again later.</p>
            capo_deadline.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_deadline.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a request rate quota.</p>
            capo_deadline.errors.validation_exception.ValidationException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.</p>
            capo_deadline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_deadline.types.update_limit_request.UpdateLimitRequest]",
        ) -> AsyncOperationResponse[
            "capo_deadline.types.update_limit_response.UpdateLimitResponse"
        ]:
            import capo_deadline._operations.deadline.update_limit

            (
                output,
                http_response,
            ) = await capo_deadline._operations.deadline.update_limit.async_update_limit(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_deadline.types.update_limit_request.UpdateLimitRequest",
        ) -> dict[str, Any]:
            import capo_deadline.types.update_limit_request

            return capo_deadline.types.update_limit_request.redact_sensitive(input_)

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("UpdateLimit", redact_input=_redact_input),
        )
        input_: capo_deadline.types.update_limit_request.UpdateLimitRequest = {
            "farm_id": farm_id,
            "limit_id": limit_id,
        }
        if display_name is not None:
            input_["display_name"] = display_name
        if description is not None:
            input_["description"] = description
        if max_count is not None:
            input_["max_count"] = max_count

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_storage_profile(
        self,
        farm_id: "capo_deadline.types.farm_id.FarmId",
        storage_profile_id: "capo_deadline.types.storage_profile_id.StorageProfileId",
        *,
        config_overrides: Optional[AsyncdeadlineClientConfig] = None,
        client_token: Optional["capo_deadline.types.client_token.ClientToken"] = None,
        display_name: Optional["capo_deadline.types.resource_name.ResourceName"] = None,
        os_family: Optional[
            "capo_deadline.types.storage_profile_operating_system_family.StorageProfileOperatingSystemFamily"
        ] = None,
        file_system_locations_to_add: Optional[
            "capo_deadline.types.file_system_locations_list.FileSystemLocationsList"
        ] = None,
        file_system_locations_to_remove: Optional[
            "capo_deadline.types.file_system_locations_list.FileSystemLocationsList"
        ] = None,
    ) -> "capo_deadline.types.update_storage_profile_response.UpdateStorageProfileResponse":
        """<p>Updates a storage profile.</p>

        Args:
            farm_id: <p>The farm ID to update.</p>
            storage_profile_id: <p>The storage profile ID to update.</p>
            client_token: <p>The unique token which the server uses to recognize retries of the same request.</p>
            display_name: <p>The display name of the storage profile to update.</p> <important> <p>This field can store any content. Escape or encode this content before displaying it on a webpage or any other system that might interpret the content of this field.</p> </important>
            os_family: <p>The OS system to update.</p>
            file_system_locations_to_add: <p>The file system location names to add.</p>
            file_system_locations_to_remove: <p>The file system location names to remove.</p>

        Raises:
            capo_deadline.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action.</p>
            capo_deadline.errors.internal_server_error_exception.InternalServerErrorException: <p>Deadline Cloud can't process your request right now. Try again later.</p>
            capo_deadline.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_deadline.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a request rate quota.</p>
            capo_deadline.errors.validation_exception.ValidationException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.</p>
            capo_deadline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_deadline.types.update_storage_profile_request.UpdateStorageProfileRequest]",
        ) -> AsyncOperationResponse[
            "capo_deadline.types.update_storage_profile_response.UpdateStorageProfileResponse"
        ]:
            import capo_deadline._operations.deadline.update_storage_profile

            (
                output,
                http_response,
            ) = await capo_deadline._operations.deadline.update_storage_profile.async_update_storage_profile(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_deadline.types.update_storage_profile_request.UpdateStorageProfileRequest",
        ) -> dict[str, Any]:
            import capo_deadline.types.update_storage_profile_request

            return capo_deadline.types.update_storage_profile_request.redact_sensitive(
                input_
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("UpdateStorageProfile", redact_input=_redact_input),
        )
        input_: capo_deadline.types.update_storage_profile_request.UpdateStorageProfileRequest = {
            "farm_id": farm_id,
            "storage_profile_id": storage_profile_id,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if display_name is not None:
            input_["display_name"] = display_name
        if os_family is not None:
            input_["os_family"] = os_family
        if file_system_locations_to_add is not None:
            input_["file_system_locations_to_add"] = file_system_locations_to_add
        if file_system_locations_to_remove is not None:
            input_["file_system_locations_to_remove"] = file_system_locations_to_remove

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
