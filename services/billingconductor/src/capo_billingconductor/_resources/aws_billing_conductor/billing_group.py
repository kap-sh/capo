from __future__ import annotations

import uuid
from typing import TYPE_CHECKING, Any, Optional

import capo_billingconductor._auth._signers
import capo_billingconductor._auth._sigv4
from capo_billingconductor._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationLogging,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_billingconductor.types.account_grouping
    import capo_billingconductor.types.account_id
    import capo_billingconductor.types.account_id_list
    import capo_billingconductor.types.associate_accounts_input
    import capo_billingconductor.types.associate_accounts_output
    import capo_billingconductor.types.billing_group_arn
    import capo_billingconductor.types.billing_group_description
    import capo_billingconductor.types.billing_group_list_element
    import capo_billingconductor.types.billing_group_name
    import capo_billingconductor.types.billing_group_status
    import capo_billingconductor.types.billing_period
    import capo_billingconductor.types.client_token
    import capo_billingconductor.types.computation_preference
    import capo_billingconductor.types.create_billing_group_input
    import capo_billingconductor.types.create_billing_group_output
    import capo_billingconductor.types.delete_billing_group_input
    import capo_billingconductor.types.delete_billing_group_output
    import capo_billingconductor.types.disassociate_accounts_input
    import capo_billingconductor.types.disassociate_accounts_output
    import capo_billingconductor.types.list_billing_groups_filter
    import capo_billingconductor.types.list_billing_groups_input
    import capo_billingconductor.types.list_billing_groups_output
    import capo_billingconductor.types.max_billing_group_results
    import capo_billingconductor.types.tag_map
    import capo_billingconductor.types.token
    import capo_billingconductor.types.update_billing_group_account_grouping
    import capo_billingconductor.types.update_billing_group_input
    import capo_billingconductor.types.update_billing_group_output
    from capo_billingconductor._services.async_billingconductor import (
        AsyncbillingconductorClient,
        AsyncbillingconductorClientConfig,
    )
    from capo_billingconductor._services.billingconductor import (
        billingconductorClient,
        billingconductorClientConfig,
    )


class BillingGroup:
    def __init__(self, service: billingconductorClient) -> None:
        self._service = service

    def create(
        self,
        name: "capo_billingconductor.types.billing_group_name.BillingGroupName",
        account_grouping: "capo_billingconductor.types.account_grouping.AccountGrouping",
        computation_preference: "capo_billingconductor.types.computation_preference.ComputationPreference",
        *,
        config_overrides: Optional[billingconductorClientConfig] = None,
        client_token: Optional[
            "capo_billingconductor.types.client_token.ClientToken"
        ] = None,
        primary_account_id: Optional[
            "capo_billingconductor.types.account_id.AccountId"
        ] = None,
        description: Optional[
            "capo_billingconductor.types.billing_group_description.BillingGroupDescription"
        ] = None,
        tags: Optional["capo_billingconductor.types.tag_map.TagMap"] = None,
    ) -> "capo_billingconductor.types.create_billing_group_output.CreateBillingGroupOutput":
        """<p> Creates a billing group that resembles a consolidated billing family that Amazon Web Services charges, based off of the predefined pricing plan computation. </p>

        Args:
            client_token: <p>A unique, case-sensitive identifier that you specify to ensure idempotency of the request. Idempotency ensures that an API request completes no more than one time. With an idempotent request, if the original request completes successfully, any subsequent retries complete successfully without performing any further actions.</p>
            name: <p> The billing group name. The names must be unique. </p>
            account_grouping: <p> The set of accounts that will be under the billing group. The set of accounts resemble the linked accounts in a consolidated billing family. </p>
            computation_preference: <p> The preferences and settings that will be used to compute the Amazon Web Services charges for a billing group. </p>
            primary_account_id: <p> The account ID that serves as the main account in a billing group. </p>
            description: <p>The description of the billing group. </p>
            tags: <p> A map that contains tag keys and tag values that are attached to a billing group. This feature isn't available during the beta. </p>

        Raises:
            capo_billingconductor.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action. </p>
            capo_billingconductor.errors.conflict_exception.ConflictException: <p>You can cause an inconsistent state by updating or deleting a resource. </p>
            capo_billingconductor.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing a request. </p>
            capo_billingconductor.errors.service_limit_exceeded_exception.ServiceLimitExceededException: <p>The request would cause a service limit to exceed. </p>
            capo_billingconductor.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. </p>
            capo_billingconductor.errors.validation_exception.ValidationException: <p>The input doesn't match with the constraints specified by Amazon Web Services services.</p>
            capo_billingconductor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_billingconductor.types.create_billing_group_input.CreateBillingGroupInput]",
        ) -> OperationResponse[
            "capo_billingconductor.types.create_billing_group_output.CreateBillingGroupOutput"
        ]:
            import capo_billingconductor._operations.aws_billing_conductor.create_billing_group

            output, http_response = (
                capo_billingconductor._operations.aws_billing_conductor.create_billing_group.create_billing_group(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_billingconductor.types.create_billing_group_input.CreateBillingGroupInput",
        ) -> dict[str, Any]:
            import capo_billingconductor.types.create_billing_group_input

            return (
                capo_billingconductor.types.create_billing_group_input.redact_sensitive(
                    input_
                )
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("CreateBillingGroup", redact_input=_redact_input),
        )
        input_: capo_billingconductor.types.create_billing_group_input.CreateBillingGroupInput = {
            "name": name,
            "account_grouping": account_grouping,
            "computation_preference": computation_preference,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if primary_account_id is not None:
            input_["primary_account_id"] = primary_account_id
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

    def update(
        self,
        arn: "capo_billingconductor.types.billing_group_arn.BillingGroupArn",
        *,
        config_overrides: Optional[billingconductorClientConfig] = None,
        name: Optional[
            "capo_billingconductor.types.billing_group_name.BillingGroupName"
        ] = None,
        status: Optional[
            "capo_billingconductor.types.billing_group_status.BillingGroupStatus"
        ] = None,
        computation_preference: Optional[
            "capo_billingconductor.types.computation_preference.ComputationPreference"
        ] = None,
        description: Optional[
            "capo_billingconductor.types.billing_group_description.BillingGroupDescription"
        ] = None,
        account_grouping: Optional[
            "capo_billingconductor.types.update_billing_group_account_grouping.UpdateBillingGroupAccountGrouping"
        ] = None,
    ) -> "capo_billingconductor.types.update_billing_group_output.UpdateBillingGroupOutput":
        """<p>This updates an existing billing group. </p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the billing group being updated. </p>
            name: <p>The name of the billing group. The names must be unique to each billing group. </p>
            status: <p>The status of the billing group. Only one of the valid values can be used. </p>
            computation_preference: <p> The preferences and settings that will be used to compute the Amazon Web Services charges for a billing group. </p>
            description: <p>A description of the billing group. </p>
            account_grouping: <p>Specifies if the billing group has automatic account association (<code>AutoAssociate</code>) enabled.</p>

        Raises:
            capo_billingconductor.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action. </p>
            capo_billingconductor.errors.conflict_exception.ConflictException: <p>You can cause an inconsistent state by updating or deleting a resource. </p>
            capo_billingconductor.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing a request. </p>
            capo_billingconductor.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that doesn't exist. </p>
            capo_billingconductor.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. </p>
            capo_billingconductor.errors.validation_exception.ValidationException: <p>The input doesn't match with the constraints specified by Amazon Web Services services.</p>
            capo_billingconductor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_billingconductor.types.update_billing_group_input.UpdateBillingGroupInput]",
        ) -> OperationResponse[
            "capo_billingconductor.types.update_billing_group_output.UpdateBillingGroupOutput"
        ]:
            import capo_billingconductor._operations.aws_billing_conductor.update_billing_group

            output, http_response = (
                capo_billingconductor._operations.aws_billing_conductor.update_billing_group.update_billing_group(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_billingconductor.types.update_billing_group_input.UpdateBillingGroupInput",
        ) -> dict[str, Any]:
            import capo_billingconductor.types.update_billing_group_input

            return (
                capo_billingconductor.types.update_billing_group_input.redact_sensitive(
                    input_
                )
            )

        def _redact_output(
            output: "capo_billingconductor.types.update_billing_group_output.UpdateBillingGroupOutput",
        ) -> dict[str, Any]:
            import capo_billingconductor.types.update_billing_group_output

            return capo_billingconductor.types.update_billing_group_output.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "UpdateBillingGroup",
                redact_input=_redact_input,
                redact_output=_redact_output,
            ),
        )
        input_: capo_billingconductor.types.update_billing_group_input.UpdateBillingGroupInput = {
            "arn": arn
        }
        if name is not None:
            input_["name"] = name
        if status is not None:
            input_["status"] = status
        if computation_preference is not None:
            input_["computation_preference"] = computation_preference
        if description is not None:
            input_["description"] = description
        if account_grouping is not None:
            input_["account_grouping"] = account_grouping

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete(
        self,
        arn: "capo_billingconductor.types.billing_group_arn.BillingGroupArn",
        *,
        config_overrides: Optional[billingconductorClientConfig] = None,
    ) -> "capo_billingconductor.types.delete_billing_group_output.DeleteBillingGroupOutput":
        """<p> Deletes a billing group. </p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the billing group that you're deleting.</p>

        Raises:
            capo_billingconductor.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action. </p>
            capo_billingconductor.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing a request. </p>
            capo_billingconductor.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. </p>
            capo_billingconductor.errors.validation_exception.ValidationException: <p>The input doesn't match with the constraints specified by Amazon Web Services services.</p>
            capo_billingconductor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_billingconductor.types.delete_billing_group_input.DeleteBillingGroupInput]",
        ) -> OperationResponse[
            "capo_billingconductor.types.delete_billing_group_output.DeleteBillingGroupOutput"
        ]:
            import capo_billingconductor._operations.aws_billing_conductor.delete_billing_group

            output, http_response = (
                capo_billingconductor._operations.aws_billing_conductor.delete_billing_group.delete_billing_group(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteBillingGroup")
        )
        input_: capo_billingconductor.types.delete_billing_group_input.DeleteBillingGroupInput = {
            "arn": arn
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
        config_overrides: Optional[billingconductorClientConfig] = None,
        billing_period: Optional[
            "capo_billingconductor.types.billing_period.BillingPeriod"
        ] = None,
        max_results: Optional[
            "capo_billingconductor.types.max_billing_group_results.MaxBillingGroupResults"
        ] = None,
        next_token: Optional["capo_billingconductor.types.token.Token"] = None,
        filters: Optional[
            "capo_billingconductor.types.list_billing_groups_filter.ListBillingGroupsFilter"
        ] = None,
    ) -> (
        "capo_billingconductor.types.list_billing_groups_output.ListBillingGroupsOutput"
    ):
        """<p>A paginated call to retrieve a list of billing groups for the given billing period. If you don't provide a billing group, the current billing period is used.</p>

        Args:
            billing_period: <p>The preferred billing period to get billing groups. </p>
            max_results: <p>The maximum number of billing groups to retrieve. </p>
            next_token: <p>The pagination token that's used on subsequent calls to get billing groups. </p>
            filters: <p>A <code>ListBillingGroupsFilter</code> that specifies the billing group and pricing plan to retrieve billing group information. </p>

        Raises:
            capo_billingconductor.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action. </p>
            capo_billingconductor.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing a request. </p>
            capo_billingconductor.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that doesn't exist. </p>
            capo_billingconductor.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. </p>
            capo_billingconductor.errors.validation_exception.ValidationException: <p>The input doesn't match with the constraints specified by Amazon Web Services services.</p>
            capo_billingconductor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_billingconductor.types.list_billing_groups_input.ListBillingGroupsInput]",
        ) -> OperationResponse[
            "capo_billingconductor.types.list_billing_groups_output.ListBillingGroupsOutput"
        ]:
            import capo_billingconductor._operations.aws_billing_conductor.list_billing_groups

            output, http_response = (
                capo_billingconductor._operations.aws_billing_conductor.list_billing_groups.list_billing_groups(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_billingconductor.types.list_billing_groups_output.ListBillingGroupsOutput",
        ) -> dict[str, Any]:
            import capo_billingconductor.types.list_billing_groups_output

            return (
                capo_billingconductor.types.list_billing_groups_output.redact_sensitive(
                    output
                )
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("ListBillingGroups", redact_output=_redact_output),
        )
        input_: capo_billingconductor.types.list_billing_groups_input.ListBillingGroupsInput = {}
        if billing_period is not None:
            input_["billing_period"] = billing_period
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if filters is not None:
            input_["filters"] = filters

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def associate_accounts(
        self,
        arn: "capo_billingconductor.types.billing_group_arn.BillingGroupArn",
        account_ids: "capo_billingconductor.types.account_id_list.AccountIdList",
        *,
        config_overrides: Optional[billingconductorClientConfig] = None,
    ) -> (
        "capo_billingconductor.types.associate_accounts_output.AssociateAccountsOutput"
    ):
        """<p>Connects an array of account IDs in a consolidated billing family to a predefined billing group. The account IDs must be a part of the consolidated billing family during the current month, and not already associated with another billing group. The maximum number of accounts that can be associated in one call is 30. </p>

        Args:
            arn: <p> The Amazon Resource Name (ARN) of the billing group that associates the array of account IDs. </p>
            account_ids: <p> The associating array of account IDs. </p>

        Raises:
            capo_billingconductor.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action. </p>
            capo_billingconductor.errors.conflict_exception.ConflictException: <p>You can cause an inconsistent state by updating or deleting a resource. </p>
            capo_billingconductor.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing a request. </p>
            capo_billingconductor.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that doesn't exist. </p>
            capo_billingconductor.errors.service_limit_exceeded_exception.ServiceLimitExceededException: <p>The request would cause a service limit to exceed. </p>
            capo_billingconductor.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. </p>
            capo_billingconductor.errors.validation_exception.ValidationException: <p>The input doesn't match with the constraints specified by Amazon Web Services services.</p>
            capo_billingconductor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_billingconductor.types.associate_accounts_input.AssociateAccountsInput]",
        ) -> OperationResponse[
            "capo_billingconductor.types.associate_accounts_output.AssociateAccountsOutput"
        ]:
            import capo_billingconductor._operations.aws_billing_conductor.associate_accounts

            output, http_response = (
                capo_billingconductor._operations.aws_billing_conductor.associate_accounts.associate_accounts(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("AssociateAccounts")
        )
        input_: capo_billingconductor.types.associate_accounts_input.AssociateAccountsInput = {
            "arn": arn,
            "account_ids": account_ids,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def disassociate_accounts(
        self,
        arn: "capo_billingconductor.types.billing_group_arn.BillingGroupArn",
        account_ids: "capo_billingconductor.types.account_id_list.AccountIdList",
        *,
        config_overrides: Optional[billingconductorClientConfig] = None,
    ) -> "capo_billingconductor.types.disassociate_accounts_output.DisassociateAccountsOutput":
        """<p>Removes the specified list of account IDs from the given billing group. </p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the billing group that the array of account IDs will disassociate from. </p>
            account_ids: <p>The array of account IDs to disassociate. </p>

        Raises:
            capo_billingconductor.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action. </p>
            capo_billingconductor.errors.conflict_exception.ConflictException: <p>You can cause an inconsistent state by updating or deleting a resource. </p>
            capo_billingconductor.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing a request. </p>
            capo_billingconductor.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that doesn't exist. </p>
            capo_billingconductor.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. </p>
            capo_billingconductor.errors.validation_exception.ValidationException: <p>The input doesn't match with the constraints specified by Amazon Web Services services.</p>
            capo_billingconductor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_billingconductor.types.disassociate_accounts_input.DisassociateAccountsInput]",
        ) -> OperationResponse[
            "capo_billingconductor.types.disassociate_accounts_output.DisassociateAccountsOutput"
        ]:
            import capo_billingconductor._operations.aws_billing_conductor.disassociate_accounts

            output, http_response = (
                capo_billingconductor._operations.aws_billing_conductor.disassociate_accounts.disassociate_accounts(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DisassociateAccounts")
        )
        input_: capo_billingconductor.types.disassociate_accounts_input.DisassociateAccountsInput = {
            "arn": arn,
            "account_ids": account_ids,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncBillingGroup:
    def __init__(self, service: AsyncbillingconductorClient) -> None:
        self._service = service

    async def create(
        self,
        name: "capo_billingconductor.types.billing_group_name.BillingGroupName",
        account_grouping: "capo_billingconductor.types.account_grouping.AccountGrouping",
        computation_preference: "capo_billingconductor.types.computation_preference.ComputationPreference",
        *,
        config_overrides: Optional[AsyncbillingconductorClientConfig] = None,
        client_token: Optional[
            "capo_billingconductor.types.client_token.ClientToken"
        ] = None,
        primary_account_id: Optional[
            "capo_billingconductor.types.account_id.AccountId"
        ] = None,
        description: Optional[
            "capo_billingconductor.types.billing_group_description.BillingGroupDescription"
        ] = None,
        tags: Optional["capo_billingconductor.types.tag_map.TagMap"] = None,
    ) -> "capo_billingconductor.types.create_billing_group_output.CreateBillingGroupOutput":
        """<p> Creates a billing group that resembles a consolidated billing family that Amazon Web Services charges, based off of the predefined pricing plan computation. </p>

        Args:
            client_token: <p>A unique, case-sensitive identifier that you specify to ensure idempotency of the request. Idempotency ensures that an API request completes no more than one time. With an idempotent request, if the original request completes successfully, any subsequent retries complete successfully without performing any further actions.</p>
            name: <p> The billing group name. The names must be unique. </p>
            account_grouping: <p> The set of accounts that will be under the billing group. The set of accounts resemble the linked accounts in a consolidated billing family. </p>
            computation_preference: <p> The preferences and settings that will be used to compute the Amazon Web Services charges for a billing group. </p>
            primary_account_id: <p> The account ID that serves as the main account in a billing group. </p>
            description: <p>The description of the billing group. </p>
            tags: <p> A map that contains tag keys and tag values that are attached to a billing group. This feature isn't available during the beta. </p>

        Raises:
            capo_billingconductor.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action. </p>
            capo_billingconductor.errors.conflict_exception.ConflictException: <p>You can cause an inconsistent state by updating or deleting a resource. </p>
            capo_billingconductor.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing a request. </p>
            capo_billingconductor.errors.service_limit_exceeded_exception.ServiceLimitExceededException: <p>The request would cause a service limit to exceed. </p>
            capo_billingconductor.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. </p>
            capo_billingconductor.errors.validation_exception.ValidationException: <p>The input doesn't match with the constraints specified by Amazon Web Services services.</p>
            capo_billingconductor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_billingconductor.types.create_billing_group_input.CreateBillingGroupInput]",
        ) -> AsyncOperationResponse[
            "capo_billingconductor.types.create_billing_group_output.CreateBillingGroupOutput"
        ]:
            import capo_billingconductor._operations.aws_billing_conductor.create_billing_group

            (
                output,
                http_response,
            ) = await capo_billingconductor._operations.aws_billing_conductor.create_billing_group.async_create_billing_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_billingconductor.types.create_billing_group_input.CreateBillingGroupInput",
        ) -> dict[str, Any]:
            import capo_billingconductor.types.create_billing_group_input

            return (
                capo_billingconductor.types.create_billing_group_input.redact_sensitive(
                    input_
                )
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("CreateBillingGroup", redact_input=_redact_input),
        )
        input_: capo_billingconductor.types.create_billing_group_input.CreateBillingGroupInput = {
            "name": name,
            "account_grouping": account_grouping,
            "computation_preference": computation_preference,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if primary_account_id is not None:
            input_["primary_account_id"] = primary_account_id
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

    async def update(
        self,
        arn: "capo_billingconductor.types.billing_group_arn.BillingGroupArn",
        *,
        config_overrides: Optional[AsyncbillingconductorClientConfig] = None,
        name: Optional[
            "capo_billingconductor.types.billing_group_name.BillingGroupName"
        ] = None,
        status: Optional[
            "capo_billingconductor.types.billing_group_status.BillingGroupStatus"
        ] = None,
        computation_preference: Optional[
            "capo_billingconductor.types.computation_preference.ComputationPreference"
        ] = None,
        description: Optional[
            "capo_billingconductor.types.billing_group_description.BillingGroupDescription"
        ] = None,
        account_grouping: Optional[
            "capo_billingconductor.types.update_billing_group_account_grouping.UpdateBillingGroupAccountGrouping"
        ] = None,
    ) -> "capo_billingconductor.types.update_billing_group_output.UpdateBillingGroupOutput":
        """<p>This updates an existing billing group. </p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the billing group being updated. </p>
            name: <p>The name of the billing group. The names must be unique to each billing group. </p>
            status: <p>The status of the billing group. Only one of the valid values can be used. </p>
            computation_preference: <p> The preferences and settings that will be used to compute the Amazon Web Services charges for a billing group. </p>
            description: <p>A description of the billing group. </p>
            account_grouping: <p>Specifies if the billing group has automatic account association (<code>AutoAssociate</code>) enabled.</p>

        Raises:
            capo_billingconductor.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action. </p>
            capo_billingconductor.errors.conflict_exception.ConflictException: <p>You can cause an inconsistent state by updating or deleting a resource. </p>
            capo_billingconductor.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing a request. </p>
            capo_billingconductor.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that doesn't exist. </p>
            capo_billingconductor.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. </p>
            capo_billingconductor.errors.validation_exception.ValidationException: <p>The input doesn't match with the constraints specified by Amazon Web Services services.</p>
            capo_billingconductor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_billingconductor.types.update_billing_group_input.UpdateBillingGroupInput]",
        ) -> AsyncOperationResponse[
            "capo_billingconductor.types.update_billing_group_output.UpdateBillingGroupOutput"
        ]:
            import capo_billingconductor._operations.aws_billing_conductor.update_billing_group

            (
                output,
                http_response,
            ) = await capo_billingconductor._operations.aws_billing_conductor.update_billing_group.async_update_billing_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_billingconductor.types.update_billing_group_input.UpdateBillingGroupInput",
        ) -> dict[str, Any]:
            import capo_billingconductor.types.update_billing_group_input

            return (
                capo_billingconductor.types.update_billing_group_input.redact_sensitive(
                    input_
                )
            )

        def _redact_output(
            output: "capo_billingconductor.types.update_billing_group_output.UpdateBillingGroupOutput",
        ) -> dict[str, Any]:
            import capo_billingconductor.types.update_billing_group_output

            return capo_billingconductor.types.update_billing_group_output.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "UpdateBillingGroup",
                redact_input=_redact_input,
                redact_output=_redact_output,
            ),
        )
        input_: capo_billingconductor.types.update_billing_group_input.UpdateBillingGroupInput = {
            "arn": arn
        }
        if name is not None:
            input_["name"] = name
        if status is not None:
            input_["status"] = status
        if computation_preference is not None:
            input_["computation_preference"] = computation_preference
        if description is not None:
            input_["description"] = description
        if account_grouping is not None:
            input_["account_grouping"] = account_grouping

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete(
        self,
        arn: "capo_billingconductor.types.billing_group_arn.BillingGroupArn",
        *,
        config_overrides: Optional[AsyncbillingconductorClientConfig] = None,
    ) -> "capo_billingconductor.types.delete_billing_group_output.DeleteBillingGroupOutput":
        """<p> Deletes a billing group. </p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the billing group that you're deleting.</p>

        Raises:
            capo_billingconductor.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action. </p>
            capo_billingconductor.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing a request. </p>
            capo_billingconductor.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. </p>
            capo_billingconductor.errors.validation_exception.ValidationException: <p>The input doesn't match with the constraints specified by Amazon Web Services services.</p>
            capo_billingconductor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_billingconductor.types.delete_billing_group_input.DeleteBillingGroupInput]",
        ) -> AsyncOperationResponse[
            "capo_billingconductor.types.delete_billing_group_output.DeleteBillingGroupOutput"
        ]:
            import capo_billingconductor._operations.aws_billing_conductor.delete_billing_group

            (
                output,
                http_response,
            ) = await capo_billingconductor._operations.aws_billing_conductor.delete_billing_group.async_delete_billing_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteBillingGroup")
        )
        input_: capo_billingconductor.types.delete_billing_group_input.DeleteBillingGroupInput = {
            "arn": arn
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
        config_overrides: Optional[AsyncbillingconductorClientConfig] = None,
        billing_period: Optional[
            "capo_billingconductor.types.billing_period.BillingPeriod"
        ] = None,
        max_results: Optional[
            "capo_billingconductor.types.max_billing_group_results.MaxBillingGroupResults"
        ] = None,
        next_token: Optional["capo_billingconductor.types.token.Token"] = None,
        filters: Optional[
            "capo_billingconductor.types.list_billing_groups_filter.ListBillingGroupsFilter"
        ] = None,
    ) -> (
        "capo_billingconductor.types.list_billing_groups_output.ListBillingGroupsOutput"
    ):
        """<p>A paginated call to retrieve a list of billing groups for the given billing period. If you don't provide a billing group, the current billing period is used.</p>

        Args:
            billing_period: <p>The preferred billing period to get billing groups. </p>
            max_results: <p>The maximum number of billing groups to retrieve. </p>
            next_token: <p>The pagination token that's used on subsequent calls to get billing groups. </p>
            filters: <p>A <code>ListBillingGroupsFilter</code> that specifies the billing group and pricing plan to retrieve billing group information. </p>

        Raises:
            capo_billingconductor.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action. </p>
            capo_billingconductor.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing a request. </p>
            capo_billingconductor.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that doesn't exist. </p>
            capo_billingconductor.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. </p>
            capo_billingconductor.errors.validation_exception.ValidationException: <p>The input doesn't match with the constraints specified by Amazon Web Services services.</p>
            capo_billingconductor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_billingconductor.types.list_billing_groups_input.ListBillingGroupsInput]",
        ) -> AsyncOperationResponse[
            "capo_billingconductor.types.list_billing_groups_output.ListBillingGroupsOutput"
        ]:
            import capo_billingconductor._operations.aws_billing_conductor.list_billing_groups

            (
                output,
                http_response,
            ) = await capo_billingconductor._operations.aws_billing_conductor.list_billing_groups.async_list_billing_groups(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_billingconductor.types.list_billing_groups_output.ListBillingGroupsOutput",
        ) -> dict[str, Any]:
            import capo_billingconductor.types.list_billing_groups_output

            return (
                capo_billingconductor.types.list_billing_groups_output.redact_sensitive(
                    output
                )
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("ListBillingGroups", redact_output=_redact_output),
        )
        input_: capo_billingconductor.types.list_billing_groups_input.ListBillingGroupsInput = {}
        if billing_period is not None:
            input_["billing_period"] = billing_period
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if filters is not None:
            input_["filters"] = filters

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def associate_accounts(
        self,
        arn: "capo_billingconductor.types.billing_group_arn.BillingGroupArn",
        account_ids: "capo_billingconductor.types.account_id_list.AccountIdList",
        *,
        config_overrides: Optional[AsyncbillingconductorClientConfig] = None,
    ) -> (
        "capo_billingconductor.types.associate_accounts_output.AssociateAccountsOutput"
    ):
        """<p>Connects an array of account IDs in a consolidated billing family to a predefined billing group. The account IDs must be a part of the consolidated billing family during the current month, and not already associated with another billing group. The maximum number of accounts that can be associated in one call is 30. </p>

        Args:
            arn: <p> The Amazon Resource Name (ARN) of the billing group that associates the array of account IDs. </p>
            account_ids: <p> The associating array of account IDs. </p>

        Raises:
            capo_billingconductor.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action. </p>
            capo_billingconductor.errors.conflict_exception.ConflictException: <p>You can cause an inconsistent state by updating or deleting a resource. </p>
            capo_billingconductor.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing a request. </p>
            capo_billingconductor.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that doesn't exist. </p>
            capo_billingconductor.errors.service_limit_exceeded_exception.ServiceLimitExceededException: <p>The request would cause a service limit to exceed. </p>
            capo_billingconductor.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. </p>
            capo_billingconductor.errors.validation_exception.ValidationException: <p>The input doesn't match with the constraints specified by Amazon Web Services services.</p>
            capo_billingconductor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_billingconductor.types.associate_accounts_input.AssociateAccountsInput]",
        ) -> AsyncOperationResponse[
            "capo_billingconductor.types.associate_accounts_output.AssociateAccountsOutput"
        ]:
            import capo_billingconductor._operations.aws_billing_conductor.associate_accounts

            (
                output,
                http_response,
            ) = await capo_billingconductor._operations.aws_billing_conductor.associate_accounts.async_associate_accounts(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("AssociateAccounts")
        )
        input_: capo_billingconductor.types.associate_accounts_input.AssociateAccountsInput = {
            "arn": arn,
            "account_ids": account_ids,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def disassociate_accounts(
        self,
        arn: "capo_billingconductor.types.billing_group_arn.BillingGroupArn",
        account_ids: "capo_billingconductor.types.account_id_list.AccountIdList",
        *,
        config_overrides: Optional[AsyncbillingconductorClientConfig] = None,
    ) -> "capo_billingconductor.types.disassociate_accounts_output.DisassociateAccountsOutput":
        """<p>Removes the specified list of account IDs from the given billing group. </p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the billing group that the array of account IDs will disassociate from. </p>
            account_ids: <p>The array of account IDs to disassociate. </p>

        Raises:
            capo_billingconductor.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action. </p>
            capo_billingconductor.errors.conflict_exception.ConflictException: <p>You can cause an inconsistent state by updating or deleting a resource. </p>
            capo_billingconductor.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing a request. </p>
            capo_billingconductor.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that doesn't exist. </p>
            capo_billingconductor.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. </p>
            capo_billingconductor.errors.validation_exception.ValidationException: <p>The input doesn't match with the constraints specified by Amazon Web Services services.</p>
            capo_billingconductor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_billingconductor.types.disassociate_accounts_input.DisassociateAccountsInput]",
        ) -> AsyncOperationResponse[
            "capo_billingconductor.types.disassociate_accounts_output.DisassociateAccountsOutput"
        ]:
            import capo_billingconductor._operations.aws_billing_conductor.disassociate_accounts

            (
                output,
                http_response,
            ) = await capo_billingconductor._operations.aws_billing_conductor.disassociate_accounts.async_disassociate_accounts(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DisassociateAccounts")
        )
        input_: capo_billingconductor.types.disassociate_accounts_input.DisassociateAccountsInput = {
            "arn": arn,
            "account_ids": account_ids,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
