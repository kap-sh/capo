from __future__ import annotations

from typing import TYPE_CHECKING, Optional

import capo_aiops._auth._signers
import capo_aiops._auth._sigv4
from capo_aiops._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_aiops.types.delete_investigation_group_policy_output
    import capo_aiops.types.delete_investigation_group_policy_request
    import capo_aiops.types.get_investigation_group_policy_request
    import capo_aiops.types.get_investigation_group_policy_response
    import capo_aiops.types.investigation_group_identifier
    import capo_aiops.types.investigation_group_policy_document
    import capo_aiops.types.put_investigation_group_policy_request
    import capo_aiops.types.put_investigation_group_policy_response
    from capo_aiops._services.ai_ops import AIOpsClient, AIOpsClientConfig
    from capo_aiops._services.async_ai_ops import (
        AsyncAIOpsClient,
        AsyncAIOpsClientConfig,
    )


class InvestigationGroupPolicy:
    def __init__(self, service: AIOpsClient) -> None:
        self._service = service

    def put(
        self,
        identifier: "capo_aiops.types.investigation_group_identifier.InvestigationGroupIdentifier",
        policy: "capo_aiops.types.investigation_group_policy_document.InvestigationGroupPolicyDocument",
        *,
        config_overrides: Optional[AIOpsClientConfig] = None,
    ) -> "capo_aiops.types.put_investigation_group_policy_response.PutInvestigationGroupPolicyResponse":
        """<p>Creates an IAM resource policy and assigns it to the specified investigation group.</p> <p>If you create your investigation group with <code>CreateInvestigationGroup</code> and you want to enable CloudWatch alarms to create investigations and add events to investigations, you must use this operation to create a policy similar to this example.</p> <p> <code> { "Version": "2008-10-17", "Statement": [ { "Effect": "Allow", "Principal": { "Service": "aiops.alarms.cloudwatch.amazonaws.com" }, "Action": [ "aiops:CreateInvestigation", "aiops:CreateInvestigationEvent" ], "Resource": "*", "Condition": { "StringEquals": { "aws:SourceAccount": "account-id" }, "ArnLike": { "aws:SourceArn": "arn:aws:cloudwatch:region:account-id:alarm:*" } } } ] } </code> </p>

        Args:
            identifier: <p>Specify either the name or the ARN of the investigation group that you want to assign the policy to.</p>
            policy: <p>The policy, in JSON format.</p>

        Raises:
            capo_aiops.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permissions to perform this action.</p>
            capo_aiops.errors.conflict_exception.ConflictException: <p>This operation couldn't be completed because of a conflict in resource states.</p>
            capo_aiops.errors.forbidden_exception.ForbiddenException: <p>Access id denied for this operation, or this operation is not valid for the specified resource.</p>
            capo_aiops.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. You can try again later.</p>
            capo_aiops.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource doesn't exist.</p>
            capo_aiops.errors.validation_exception.ValidationException: <p>This operation or its parameters aren't formatted correctly.</p>
            capo_aiops.errors.throttling_exception.ThrottlingException: <p>The request was throttled because of quota limits. You can try again later.</p>
            capo_aiops.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_aiops.types.put_investigation_group_policy_request.PutInvestigationGroupPolicyRequest]",
        ) -> OperationResponse[
            "capo_aiops.types.put_investigation_group_policy_response.PutInvestigationGroupPolicyResponse"
        ]:
            import capo_aiops._operations.ai_ops.put_investigation_group_policy

            output, http_response = (
                capo_aiops._operations.ai_ops.put_investigation_group_policy.put_investigation_group_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_aiops.types.put_investigation_group_policy_request.PutInvestigationGroupPolicyRequest = {
            "identifier": identifier,
            "policy": policy,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def read(
        self,
        identifier: "capo_aiops.types.investigation_group_identifier.InvestigationGroupIdentifier",
        *,
        config_overrides: Optional[AIOpsClientConfig] = None,
    ) -> "capo_aiops.types.get_investigation_group_policy_response.GetInvestigationGroupPolicyResponse":
        r"""<p>Returns the JSON of the IAM resource policy associated with the specified investigation group in a string. For example, <code>{\"Version\":\"2012-10-17\",\"Statement\":[{\"Effect\":\"Allow\",\"Principal\":{\"Service\":\"aiops.alarms.cloudwatch.amazonaws.com\"},\"Action\":[\"aiops:CreateInvestigation\",\"aiops:CreateInvestigationEvent\"],\"Resource\":\"*\",\"Condition\":{\"StringEquals\":{\"aws:SourceAccount\":\"111122223333\"},\"ArnLike\":{\"aws:SourceArn\":\"arn:aws:cloudwatch:us-east-1:111122223333:alarm:*\"}}}]}</code>.</p>

        Args:
            identifier: <p>Specify either the name or the ARN of the investigation group that you want to view the policy of.</p>

        Raises:
            capo_aiops.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permissions to perform this action.</p>
            capo_aiops.errors.conflict_exception.ConflictException: <p>This operation couldn't be completed because of a conflict in resource states.</p>
            capo_aiops.errors.forbidden_exception.ForbiddenException: <p>Access id denied for this operation, or this operation is not valid for the specified resource.</p>
            capo_aiops.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. You can try again later.</p>
            capo_aiops.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource doesn't exist.</p>
            capo_aiops.errors.validation_exception.ValidationException: <p>This operation or its parameters aren't formatted correctly.</p>
            capo_aiops.errors.throttling_exception.ThrottlingException: <p>The request was throttled because of quota limits. You can try again later.</p>
            capo_aiops.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_aiops.types.get_investigation_group_policy_request.GetInvestigationGroupPolicyRequest]",
        ) -> OperationResponse[
            "capo_aiops.types.get_investigation_group_policy_response.GetInvestigationGroupPolicyResponse"
        ]:
            import capo_aiops._operations.ai_ops.get_investigation_group_policy

            output, http_response = (
                capo_aiops._operations.ai_ops.get_investigation_group_policy.get_investigation_group_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_aiops.types.get_investigation_group_policy_request.GetInvestigationGroupPolicyRequest = {
            "identifier": identifier
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete(
        self,
        identifier: "capo_aiops.types.investigation_group_identifier.InvestigationGroupIdentifier",
        *,
        config_overrides: Optional[AIOpsClientConfig] = None,
    ) -> "capo_aiops.types.delete_investigation_group_policy_output.DeleteInvestigationGroupPolicyOutput":
        """<p>Removes the IAM resource policy from being associated with the investigation group that you specify.</p>

        Args:
            identifier: <p>Specify either the name or the ARN of the investigation group that you want to remove the policy from.</p>

        Raises:
            capo_aiops.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permissions to perform this action.</p>
            capo_aiops.errors.conflict_exception.ConflictException: <p>This operation couldn't be completed because of a conflict in resource states.</p>
            capo_aiops.errors.forbidden_exception.ForbiddenException: <p>Access id denied for this operation, or this operation is not valid for the specified resource.</p>
            capo_aiops.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. You can try again later.</p>
            capo_aiops.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource doesn't exist.</p>
            capo_aiops.errors.validation_exception.ValidationException: <p>This operation or its parameters aren't formatted correctly.</p>
            capo_aiops.errors.throttling_exception.ThrottlingException: <p>The request was throttled because of quota limits. You can try again later.</p>
            capo_aiops.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_aiops.types.delete_investigation_group_policy_request.DeleteInvestigationGroupPolicyRequest]",
        ) -> OperationResponse[
            "capo_aiops.types.delete_investigation_group_policy_output.DeleteInvestigationGroupPolicyOutput"
        ]:
            import capo_aiops._operations.ai_ops.delete_investigation_group_policy

            output, http_response = (
                capo_aiops._operations.ai_ops.delete_investigation_group_policy.delete_investigation_group_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_aiops.types.delete_investigation_group_policy_request.DeleteInvestigationGroupPolicyRequest = {
            "identifier": identifier
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncInvestigationGroupPolicy:
    def __init__(self, service: AsyncAIOpsClient) -> None:
        self._service = service

    async def put(
        self,
        identifier: "capo_aiops.types.investigation_group_identifier.InvestigationGroupIdentifier",
        policy: "capo_aiops.types.investigation_group_policy_document.InvestigationGroupPolicyDocument",
        *,
        config_overrides: Optional[AsyncAIOpsClientConfig] = None,
    ) -> "capo_aiops.types.put_investigation_group_policy_response.PutInvestigationGroupPolicyResponse":
        """<p>Creates an IAM resource policy and assigns it to the specified investigation group.</p> <p>If you create your investigation group with <code>CreateInvestigationGroup</code> and you want to enable CloudWatch alarms to create investigations and add events to investigations, you must use this operation to create a policy similar to this example.</p> <p> <code> { "Version": "2008-10-17", "Statement": [ { "Effect": "Allow", "Principal": { "Service": "aiops.alarms.cloudwatch.amazonaws.com" }, "Action": [ "aiops:CreateInvestigation", "aiops:CreateInvestigationEvent" ], "Resource": "*", "Condition": { "StringEquals": { "aws:SourceAccount": "account-id" }, "ArnLike": { "aws:SourceArn": "arn:aws:cloudwatch:region:account-id:alarm:*" } } } ] } </code> </p>

        Args:
            identifier: <p>Specify either the name or the ARN of the investigation group that you want to assign the policy to.</p>
            policy: <p>The policy, in JSON format.</p>

        Raises:
            capo_aiops.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permissions to perform this action.</p>
            capo_aiops.errors.conflict_exception.ConflictException: <p>This operation couldn't be completed because of a conflict in resource states.</p>
            capo_aiops.errors.forbidden_exception.ForbiddenException: <p>Access id denied for this operation, or this operation is not valid for the specified resource.</p>
            capo_aiops.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. You can try again later.</p>
            capo_aiops.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource doesn't exist.</p>
            capo_aiops.errors.validation_exception.ValidationException: <p>This operation or its parameters aren't formatted correctly.</p>
            capo_aiops.errors.throttling_exception.ThrottlingException: <p>The request was throttled because of quota limits. You can try again later.</p>
            capo_aiops.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_aiops.types.put_investigation_group_policy_request.PutInvestigationGroupPolicyRequest]",
        ) -> AsyncOperationResponse[
            "capo_aiops.types.put_investigation_group_policy_response.PutInvestigationGroupPolicyResponse"
        ]:
            import capo_aiops._operations.ai_ops.put_investigation_group_policy

            (
                output,
                http_response,
            ) = await capo_aiops._operations.ai_ops.put_investigation_group_policy.async_put_investigation_group_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_aiops.types.put_investigation_group_policy_request.PutInvestigationGroupPolicyRequest = {
            "identifier": identifier,
            "policy": policy,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def read(
        self,
        identifier: "capo_aiops.types.investigation_group_identifier.InvestigationGroupIdentifier",
        *,
        config_overrides: Optional[AsyncAIOpsClientConfig] = None,
    ) -> "capo_aiops.types.get_investigation_group_policy_response.GetInvestigationGroupPolicyResponse":
        r"""<p>Returns the JSON of the IAM resource policy associated with the specified investigation group in a string. For example, <code>{\"Version\":\"2012-10-17\",\"Statement\":[{\"Effect\":\"Allow\",\"Principal\":{\"Service\":\"aiops.alarms.cloudwatch.amazonaws.com\"},\"Action\":[\"aiops:CreateInvestigation\",\"aiops:CreateInvestigationEvent\"],\"Resource\":\"*\",\"Condition\":{\"StringEquals\":{\"aws:SourceAccount\":\"111122223333\"},\"ArnLike\":{\"aws:SourceArn\":\"arn:aws:cloudwatch:us-east-1:111122223333:alarm:*\"}}}]}</code>.</p>

        Args:
            identifier: <p>Specify either the name or the ARN of the investigation group that you want to view the policy of.</p>

        Raises:
            capo_aiops.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permissions to perform this action.</p>
            capo_aiops.errors.conflict_exception.ConflictException: <p>This operation couldn't be completed because of a conflict in resource states.</p>
            capo_aiops.errors.forbidden_exception.ForbiddenException: <p>Access id denied for this operation, or this operation is not valid for the specified resource.</p>
            capo_aiops.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. You can try again later.</p>
            capo_aiops.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource doesn't exist.</p>
            capo_aiops.errors.validation_exception.ValidationException: <p>This operation or its parameters aren't formatted correctly.</p>
            capo_aiops.errors.throttling_exception.ThrottlingException: <p>The request was throttled because of quota limits. You can try again later.</p>
            capo_aiops.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_aiops.types.get_investigation_group_policy_request.GetInvestigationGroupPolicyRequest]",
        ) -> AsyncOperationResponse[
            "capo_aiops.types.get_investigation_group_policy_response.GetInvestigationGroupPolicyResponse"
        ]:
            import capo_aiops._operations.ai_ops.get_investigation_group_policy

            (
                output,
                http_response,
            ) = await capo_aiops._operations.ai_ops.get_investigation_group_policy.async_get_investigation_group_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_aiops.types.get_investigation_group_policy_request.GetInvestigationGroupPolicyRequest = {
            "identifier": identifier
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete(
        self,
        identifier: "capo_aiops.types.investigation_group_identifier.InvestigationGroupIdentifier",
        *,
        config_overrides: Optional[AsyncAIOpsClientConfig] = None,
    ) -> "capo_aiops.types.delete_investigation_group_policy_output.DeleteInvestigationGroupPolicyOutput":
        """<p>Removes the IAM resource policy from being associated with the investigation group that you specify.</p>

        Args:
            identifier: <p>Specify either the name or the ARN of the investigation group that you want to remove the policy from.</p>

        Raises:
            capo_aiops.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permissions to perform this action.</p>
            capo_aiops.errors.conflict_exception.ConflictException: <p>This operation couldn't be completed because of a conflict in resource states.</p>
            capo_aiops.errors.forbidden_exception.ForbiddenException: <p>Access id denied for this operation, or this operation is not valid for the specified resource.</p>
            capo_aiops.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. You can try again later.</p>
            capo_aiops.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource doesn't exist.</p>
            capo_aiops.errors.validation_exception.ValidationException: <p>This operation or its parameters aren't formatted correctly.</p>
            capo_aiops.errors.throttling_exception.ThrottlingException: <p>The request was throttled because of quota limits. You can try again later.</p>
            capo_aiops.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_aiops.types.delete_investigation_group_policy_request.DeleteInvestigationGroupPolicyRequest]",
        ) -> AsyncOperationResponse[
            "capo_aiops.types.delete_investigation_group_policy_output.DeleteInvestigationGroupPolicyOutput"
        ]:
            import capo_aiops._operations.ai_ops.delete_investigation_group_policy

            (
                output,
                http_response,
            ) = await capo_aiops._operations.ai_ops.delete_investigation_group_policy.async_delete_investigation_group_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_aiops.types.delete_investigation_group_policy_request.DeleteInvestigationGroupPolicyRequest = {
            "identifier": identifier
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
