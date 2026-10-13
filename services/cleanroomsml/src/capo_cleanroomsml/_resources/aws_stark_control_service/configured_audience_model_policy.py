from __future__ import annotations

from typing import TYPE_CHECKING, Optional

import capo_cleanroomsml._auth._signers
import capo_cleanroomsml._auth._sigv4
from capo_cleanroomsml._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationLogging,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_cleanroomsml.types.configured_audience_model_arn
    import capo_cleanroomsml.types.delete_configured_audience_model_policy_request
    import capo_cleanroomsml.types.get_configured_audience_model_policy_request
    import capo_cleanroomsml.types.get_configured_audience_model_policy_response
    import capo_cleanroomsml.types.hash
    import capo_cleanroomsml.types.policy_existence_condition
    import capo_cleanroomsml.types.put_configured_audience_model_policy_request
    import capo_cleanroomsml.types.put_configured_audience_model_policy_response
    import capo_cleanroomsml.types.resource_policy
    from capo_cleanroomsml._services.async_clean_rooms_ml import (
        AsyncCleanRoomsMLClient,
        AsyncCleanRoomsMLClientConfig,
    )
    from capo_cleanroomsml._services.clean_rooms_ml import (
        CleanRoomsMLClient,
        CleanRoomsMLClientConfig,
    )


class ConfiguredAudienceModelPolicy:
    def __init__(self, service: CleanRoomsMLClient) -> None:
        self._service = service

    def put(
        self,
        configured_audience_model_arn: "capo_cleanroomsml.types.configured_audience_model_arn.ConfiguredAudienceModelArn",
        configured_audience_model_policy: "capo_cleanroomsml.types.resource_policy.ResourcePolicy",
        *,
        config_overrides: Optional[CleanRoomsMLClientConfig] = None,
        previous_policy_hash: Optional["capo_cleanroomsml.types.hash.Hash"] = None,
        policy_existence_condition: Optional[
            "capo_cleanroomsml.types.policy_existence_condition.PolicyExistenceCondition"
        ] = None,
    ) -> "capo_cleanroomsml.types.put_configured_audience_model_policy_response.PutConfiguredAudienceModelPolicyResponse":
        """<p>Create or update the resource policy for a configured audience model.</p>

        Args:
            configured_audience_model_arn: <p>The Amazon Resource Name (ARN) of the configured audience model that the resource policy will govern.</p>
            configured_audience_model_policy: <p>The IAM resource policy.</p>
            previous_policy_hash: <p>A cryptographic hash of the contents of the policy used to prevent unexpected concurrent modification of the policy.</p>
            policy_existence_condition: <p>Use this to prevent unexpected concurrent modification of the policy.</p>

        Raises:
            capo_cleanroomsml.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_cleanroomsml.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource you are requesting does not exist.</p>
            capo_cleanroomsml.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_cleanroomsml.errors.validation_exception.ValidationException: <p>The request parameters for this request are incorrect.</p>
            capo_cleanroomsml.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cleanroomsml.types.put_configured_audience_model_policy_request.PutConfiguredAudienceModelPolicyRequest]",
        ) -> OperationResponse[
            "capo_cleanroomsml.types.put_configured_audience_model_policy_response.PutConfiguredAudienceModelPolicyResponse"
        ]:
            import capo_cleanroomsml._operations.aws_stark_control_service.put_configured_audience_model_policy

            output, http_response = (
                capo_cleanroomsml._operations.aws_stark_control_service.put_configured_audience_model_policy.put_configured_audience_model_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("PutConfiguredAudienceModelPolicy")
        )
        input_: capo_cleanroomsml.types.put_configured_audience_model_policy_request.PutConfiguredAudienceModelPolicyRequest = {
            "configured_audience_model_arn": configured_audience_model_arn,
            "configured_audience_model_policy": configured_audience_model_policy,
        }
        if previous_policy_hash is not None:
            input_["previous_policy_hash"] = previous_policy_hash
        if policy_existence_condition is not None:
            input_["policy_existence_condition"] = policy_existence_condition

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def read(
        self,
        configured_audience_model_arn: "capo_cleanroomsml.types.configured_audience_model_arn.ConfiguredAudienceModelArn",
        *,
        config_overrides: Optional[CleanRoomsMLClientConfig] = None,
    ) -> "capo_cleanroomsml.types.get_configured_audience_model_policy_response.GetConfiguredAudienceModelPolicyResponse":
        """<p>Returns information about a configured audience model policy.</p>

        Args:
            configured_audience_model_arn: <p>The Amazon Resource Name (ARN) of the configured audience model that you are interested in.</p>

        Raises:
            capo_cleanroomsml.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_cleanroomsml.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource you are requesting does not exist.</p>
            capo_cleanroomsml.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_cleanroomsml.errors.validation_exception.ValidationException: <p>The request parameters for this request are incorrect.</p>
            capo_cleanroomsml.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cleanroomsml.types.get_configured_audience_model_policy_request.GetConfiguredAudienceModelPolicyRequest]",
        ) -> OperationResponse[
            "capo_cleanroomsml.types.get_configured_audience_model_policy_response.GetConfiguredAudienceModelPolicyResponse"
        ]:
            import capo_cleanroomsml._operations.aws_stark_control_service.get_configured_audience_model_policy

            output, http_response = (
                capo_cleanroomsml._operations.aws_stark_control_service.get_configured_audience_model_policy.get_configured_audience_model_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetConfiguredAudienceModelPolicy")
        )
        input_: capo_cleanroomsml.types.get_configured_audience_model_policy_request.GetConfiguredAudienceModelPolicyRequest = {
            "configured_audience_model_arn": configured_audience_model_arn
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
        configured_audience_model_arn: "capo_cleanroomsml.types.configured_audience_model_arn.ConfiguredAudienceModelArn",
        *,
        config_overrides: Optional[CleanRoomsMLClientConfig] = None,
    ) -> None:
        """<p>Deletes the specified configured audience model policy.</p>

        Args:
            configured_audience_model_arn: <p>The Amazon Resource Name (ARN) of the configured audience model policy that you want to delete.</p>

        Raises:
            capo_cleanroomsml.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_cleanroomsml.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource you are requesting does not exist.</p>
            capo_cleanroomsml.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_cleanroomsml.errors.validation_exception.ValidationException: <p>The request parameters for this request are incorrect.</p>
            capo_cleanroomsml.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cleanroomsml.types.delete_configured_audience_model_policy_request.DeleteConfiguredAudienceModelPolicyRequest]",
        ) -> OperationResponse[None]:
            import capo_cleanroomsml._operations.aws_stark_control_service.delete_configured_audience_model_policy

            output, http_response = (
                capo_cleanroomsml._operations.aws_stark_control_service.delete_configured_audience_model_policy.delete_configured_audience_model_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteConfiguredAudienceModelPolicy")
        )
        input_: capo_cleanroomsml.types.delete_configured_audience_model_policy_request.DeleteConfiguredAudienceModelPolicyRequest = {
            "configured_audience_model_arn": configured_audience_model_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncConfiguredAudienceModelPolicy:
    def __init__(self, service: AsyncCleanRoomsMLClient) -> None:
        self._service = service

    async def put(
        self,
        configured_audience_model_arn: "capo_cleanroomsml.types.configured_audience_model_arn.ConfiguredAudienceModelArn",
        configured_audience_model_policy: "capo_cleanroomsml.types.resource_policy.ResourcePolicy",
        *,
        config_overrides: Optional[AsyncCleanRoomsMLClientConfig] = None,
        previous_policy_hash: Optional["capo_cleanroomsml.types.hash.Hash"] = None,
        policy_existence_condition: Optional[
            "capo_cleanroomsml.types.policy_existence_condition.PolicyExistenceCondition"
        ] = None,
    ) -> "capo_cleanroomsml.types.put_configured_audience_model_policy_response.PutConfiguredAudienceModelPolicyResponse":
        """<p>Create or update the resource policy for a configured audience model.</p>

        Args:
            configured_audience_model_arn: <p>The Amazon Resource Name (ARN) of the configured audience model that the resource policy will govern.</p>
            configured_audience_model_policy: <p>The IAM resource policy.</p>
            previous_policy_hash: <p>A cryptographic hash of the contents of the policy used to prevent unexpected concurrent modification of the policy.</p>
            policy_existence_condition: <p>Use this to prevent unexpected concurrent modification of the policy.</p>

        Raises:
            capo_cleanroomsml.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_cleanroomsml.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource you are requesting does not exist.</p>
            capo_cleanroomsml.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_cleanroomsml.errors.validation_exception.ValidationException: <p>The request parameters for this request are incorrect.</p>
            capo_cleanroomsml.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanroomsml.types.put_configured_audience_model_policy_request.PutConfiguredAudienceModelPolicyRequest]",
        ) -> AsyncOperationResponse[
            "capo_cleanroomsml.types.put_configured_audience_model_policy_response.PutConfiguredAudienceModelPolicyResponse"
        ]:
            import capo_cleanroomsml._operations.aws_stark_control_service.put_configured_audience_model_policy

            (
                output,
                http_response,
            ) = await capo_cleanroomsml._operations.aws_stark_control_service.put_configured_audience_model_policy.async_put_configured_audience_model_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("PutConfiguredAudienceModelPolicy")
        )
        input_: capo_cleanroomsml.types.put_configured_audience_model_policy_request.PutConfiguredAudienceModelPolicyRequest = {
            "configured_audience_model_arn": configured_audience_model_arn,
            "configured_audience_model_policy": configured_audience_model_policy,
        }
        if previous_policy_hash is not None:
            input_["previous_policy_hash"] = previous_policy_hash
        if policy_existence_condition is not None:
            input_["policy_existence_condition"] = policy_existence_condition

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def read(
        self,
        configured_audience_model_arn: "capo_cleanroomsml.types.configured_audience_model_arn.ConfiguredAudienceModelArn",
        *,
        config_overrides: Optional[AsyncCleanRoomsMLClientConfig] = None,
    ) -> "capo_cleanroomsml.types.get_configured_audience_model_policy_response.GetConfiguredAudienceModelPolicyResponse":
        """<p>Returns information about a configured audience model policy.</p>

        Args:
            configured_audience_model_arn: <p>The Amazon Resource Name (ARN) of the configured audience model that you are interested in.</p>

        Raises:
            capo_cleanroomsml.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_cleanroomsml.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource you are requesting does not exist.</p>
            capo_cleanroomsml.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_cleanroomsml.errors.validation_exception.ValidationException: <p>The request parameters for this request are incorrect.</p>
            capo_cleanroomsml.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanroomsml.types.get_configured_audience_model_policy_request.GetConfiguredAudienceModelPolicyRequest]",
        ) -> AsyncOperationResponse[
            "capo_cleanroomsml.types.get_configured_audience_model_policy_response.GetConfiguredAudienceModelPolicyResponse"
        ]:
            import capo_cleanroomsml._operations.aws_stark_control_service.get_configured_audience_model_policy

            (
                output,
                http_response,
            ) = await capo_cleanroomsml._operations.aws_stark_control_service.get_configured_audience_model_policy.async_get_configured_audience_model_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetConfiguredAudienceModelPolicy")
        )
        input_: capo_cleanroomsml.types.get_configured_audience_model_policy_request.GetConfiguredAudienceModelPolicyRequest = {
            "configured_audience_model_arn": configured_audience_model_arn
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
        configured_audience_model_arn: "capo_cleanroomsml.types.configured_audience_model_arn.ConfiguredAudienceModelArn",
        *,
        config_overrides: Optional[AsyncCleanRoomsMLClientConfig] = None,
    ) -> None:
        """<p>Deletes the specified configured audience model policy.</p>

        Args:
            configured_audience_model_arn: <p>The Amazon Resource Name (ARN) of the configured audience model policy that you want to delete.</p>

        Raises:
            capo_cleanroomsml.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_cleanroomsml.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource you are requesting does not exist.</p>
            capo_cleanroomsml.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_cleanroomsml.errors.validation_exception.ValidationException: <p>The request parameters for this request are incorrect.</p>
            capo_cleanroomsml.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanroomsml.types.delete_configured_audience_model_policy_request.DeleteConfiguredAudienceModelPolicyRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_cleanroomsml._operations.aws_stark_control_service.delete_configured_audience_model_policy

            (
                output,
                http_response,
            ) = await capo_cleanroomsml._operations.aws_stark_control_service.delete_configured_audience_model_policy.async_delete_configured_audience_model_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteConfiguredAudienceModelPolicy")
        )
        input_: capo_cleanroomsml.types.delete_configured_audience_model_policy_request.DeleteConfiguredAudienceModelPolicyRequest = {
            "configured_audience_model_arn": configured_audience_model_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
