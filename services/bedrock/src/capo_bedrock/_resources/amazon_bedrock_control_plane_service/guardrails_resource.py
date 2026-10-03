from __future__ import annotations

import uuid
from typing import TYPE_CHECKING, Optional

import capo_bedrock._auth._signers
import capo_bedrock._auth._sigv4
from capo_bedrock._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_bedrock.types.create_guardrail_request
    import capo_bedrock.types.create_guardrail_response
    import capo_bedrock.types.create_guardrail_version_request
    import capo_bedrock.types.create_guardrail_version_response
    import capo_bedrock.types.delete_guardrail_request
    import capo_bedrock.types.delete_guardrail_response
    import capo_bedrock.types.get_guardrail_request
    import capo_bedrock.types.get_guardrail_response
    import capo_bedrock.types.guardrail_automated_reasoning_policy_config
    import capo_bedrock.types.guardrail_blocked_messaging
    import capo_bedrock.types.guardrail_content_policy_config
    import capo_bedrock.types.guardrail_contextual_grounding_policy_config
    import capo_bedrock.types.guardrail_cross_region_config
    import capo_bedrock.types.guardrail_description
    import capo_bedrock.types.guardrail_identifier
    import capo_bedrock.types.guardrail_name
    import capo_bedrock.types.guardrail_numerical_version
    import capo_bedrock.types.guardrail_sensitive_information_policy_config
    import capo_bedrock.types.guardrail_summary
    import capo_bedrock.types.guardrail_topic_policy_config
    import capo_bedrock.types.guardrail_version
    import capo_bedrock.types.guardrail_word_policy_config
    import capo_bedrock.types.idempotency_token
    import capo_bedrock.types.kms_key_id
    import capo_bedrock.types.list_guardrails_request
    import capo_bedrock.types.list_guardrails_response
    import capo_bedrock.types.max_results
    import capo_bedrock.types.pagination_token
    import capo_bedrock.types.tag_list
    import capo_bedrock.types.update_guardrail_request
    import capo_bedrock.types.update_guardrail_response
    from capo_bedrock._services.async_bedrock import (
        AsyncBedrockClient,
        AsyncBedrockClientConfig,
    )
    from capo_bedrock._services.bedrock import BedrockClient, BedrockClientConfig


class GuardrailsResource:
    def __init__(self, service: BedrockClient) -> None:
        self._service = service

    def create(
        self,
        name: "capo_bedrock.types.guardrail_name.GuardrailName",
        blocked_input_messaging: "capo_bedrock.types.guardrail_blocked_messaging.GuardrailBlockedMessaging",
        blocked_outputs_messaging: "capo_bedrock.types.guardrail_blocked_messaging.GuardrailBlockedMessaging",
        *,
        config_overrides: Optional[BedrockClientConfig] = None,
        description: Optional[
            "capo_bedrock.types.guardrail_description.GuardrailDescription"
        ] = None,
        topic_policy_config: Optional[
            "capo_bedrock.types.guardrail_topic_policy_config.GuardrailTopicPolicyConfig"
        ] = None,
        content_policy_config: Optional[
            "capo_bedrock.types.guardrail_content_policy_config.GuardrailContentPolicyConfig"
        ] = None,
        word_policy_config: Optional[
            "capo_bedrock.types.guardrail_word_policy_config.GuardrailWordPolicyConfig"
        ] = None,
        sensitive_information_policy_config: Optional[
            "capo_bedrock.types.guardrail_sensitive_information_policy_config.GuardrailSensitiveInformationPolicyConfig"
        ] = None,
        contextual_grounding_policy_config: Optional[
            "capo_bedrock.types.guardrail_contextual_grounding_policy_config.GuardrailContextualGroundingPolicyConfig"
        ] = None,
        automated_reasoning_policy_config: Optional[
            "capo_bedrock.types.guardrail_automated_reasoning_policy_config.GuardrailAutomatedReasoningPolicyConfig"
        ] = None,
        cross_region_config: Optional[
            "capo_bedrock.types.guardrail_cross_region_config.GuardrailCrossRegionConfig"
        ] = None,
        kms_key_id: Optional["capo_bedrock.types.kms_key_id.KmsKeyId"] = None,
        tags: Optional["capo_bedrock.types.tag_list.TagList"] = None,
        client_request_token: Optional[
            "capo_bedrock.types.idempotency_token.IdempotencyToken"
        ] = None,
    ) -> "capo_bedrock.types.create_guardrail_response.CreateGuardrailResponse":
        """<p>Creates a guardrail to block topics and to implement safeguards for your generative AI applications.</p> <p>You can configure the following policies in a guardrail to avoid undesirable and harmful content, filter out denied topics and words, and remove sensitive information for privacy protection.</p> <ul> <li> <p> <b>Content filters</b> - Adjust filter strengths to block input prompts or model responses containing harmful content.</p> </li> <li> <p> <b>Denied topics</b> - Define a set of topics that are undesirable in the context of your application. These topics will be blocked if detected in user queries or model responses.</p> </li> <li> <p> <b>Word filters</b> - Configure filters to block undesirable words, phrases, and profanity. Such words can include offensive terms, competitor names etc.</p> </li> <li> <p> <b>Sensitive information filters</b> - Block or mask sensitive information such as personally identifiable information (PII) or custom regex in user inputs and model responses.</p> </li> </ul> <p>In addition to the above policies, you can also configure the messages to be returned to the user if a user input or model response is in violation of the policies defined in the guardrail.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails.html">Amazon Bedrock Guardrails</a> in the <i>Amazon Bedrock User Guide</i>.</p>

        Args:
            name: <p>The name to give the guardrail.</p>
            description: <p>A description of the guardrail.</p>
            topic_policy_config: <p>The topic policies to configure for the guardrail.</p>
            content_policy_config: <p>The content filter policies to configure for the guardrail.</p>
            word_policy_config: <p>The word policy you configure for the guardrail.</p>
            sensitive_information_policy_config: <p>The sensitive information policy to configure for the guardrail.</p>
            contextual_grounding_policy_config: <p>The contextual grounding policy configuration used to create a guardrail.</p>
            automated_reasoning_policy_config: <p>Optional configuration for integrating Automated Reasoning policies with the new guardrail.</p>
            cross_region_config: <p>The system-defined guardrail profile that you're using with your guardrail. Guardrail profiles define the destination Amazon Web Services Regions where guardrail inference requests can be automatically routed.</p> <p>For more information, see the <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-cross-region.html">Amazon Bedrock User Guide</a>.</p>
            blocked_input_messaging: <p>The message to return when the guardrail blocks a prompt.</p>
            blocked_outputs_messaging: <p>The message to return when the guardrail blocks a model response.</p>
            kms_key_id: <p>The ARN of the KMS key that you use to encrypt the guardrail.</p>
            tags: <p>The tags that you want to attach to the guardrail. </p>
            client_request_token: <p>A unique, case-sensitive identifier to ensure that the API request completes no more than once. If this token matches a previous request, Amazon Bedrock ignores the request, but does not return an error. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html">Ensuring idempotency</a> in the <i>Amazon S3 User Guide</i>.</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.conflict_exception.ConflictException: <p>Error occurred because of a conflict while performing an operation.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The number of requests exceeds the service quota. Resubmit your request later.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.too_many_tags_exception.TooManyTagsException: <p>The request contains more tags than can be associated with a resource (50 tags per resource). The maximum number of tags includes both existing tags and those included in your current request. </p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock.types.create_guardrail_request.CreateGuardrailRequest]",
        ) -> OperationResponse[
            "capo_bedrock.types.create_guardrail_response.CreateGuardrailResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.create_guardrail

            output, http_response = (
                capo_bedrock._operations.amazon_bedrock_control_plane_service.create_guardrail.create_guardrail(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock.types.create_guardrail_request.CreateGuardrailRequest = {
            "name": name,
            "blocked_input_messaging": blocked_input_messaging,
            "blocked_outputs_messaging": blocked_outputs_messaging,
        }
        if description is not None:
            input_["description"] = description
        if topic_policy_config is not None:
            input_["topic_policy_config"] = topic_policy_config
        if content_policy_config is not None:
            input_["content_policy_config"] = content_policy_config
        if word_policy_config is not None:
            input_["word_policy_config"] = word_policy_config
        if sensitive_information_policy_config is not None:
            input_["sensitive_information_policy_config"] = (
                sensitive_information_policy_config
            )
        if contextual_grounding_policy_config is not None:
            input_["contextual_grounding_policy_config"] = (
                contextual_grounding_policy_config
            )
        if automated_reasoning_policy_config is not None:
            input_["automated_reasoning_policy_config"] = (
                automated_reasoning_policy_config
            )
        if cross_region_config is not None:
            input_["cross_region_config"] = cross_region_config
        if kms_key_id is not None:
            input_["kms_key_id"] = kms_key_id
        if tags is not None:
            input_["tags"] = tags
        if client_request_token is None:
            client_request_token = str(uuid.uuid4())
        input_["client_request_token"] = client_request_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def read(
        self,
        guardrail_identifier: "capo_bedrock.types.guardrail_identifier.GuardrailIdentifier",
        *,
        config_overrides: Optional[BedrockClientConfig] = None,
        guardrail_version: Optional[
            "capo_bedrock.types.guardrail_version.GuardrailVersion"
        ] = None,
    ) -> "capo_bedrock.types.get_guardrail_response.GetGuardrailResponse":
        """<p>Gets details about a guardrail. If you don't specify a version, the response returns details for the <code>DRAFT</code> version.</p>

        Args:
            guardrail_identifier: <p>The unique identifier of the guardrail for which to get details. This can be an ID or the ARN.</p>
            guardrail_version: <p>The version of the guardrail for which to get details. If you don't specify a version, the response returns details for the <code>DRAFT</code> version.</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock.types.get_guardrail_request.GetGuardrailRequest]",
        ) -> OperationResponse[
            "capo_bedrock.types.get_guardrail_response.GetGuardrailResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.get_guardrail

            output, http_response = (
                capo_bedrock._operations.amazon_bedrock_control_plane_service.get_guardrail.get_guardrail(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock.types.get_guardrail_request.GetGuardrailRequest = {
            "guardrail_identifier": guardrail_identifier
        }
        if guardrail_version is not None:
            input_["guardrail_version"] = guardrail_version

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update(
        self,
        guardrail_identifier: "capo_bedrock.types.guardrail_identifier.GuardrailIdentifier",
        name: "capo_bedrock.types.guardrail_name.GuardrailName",
        blocked_input_messaging: "capo_bedrock.types.guardrail_blocked_messaging.GuardrailBlockedMessaging",
        blocked_outputs_messaging: "capo_bedrock.types.guardrail_blocked_messaging.GuardrailBlockedMessaging",
        *,
        config_overrides: Optional[BedrockClientConfig] = None,
        description: Optional[
            "capo_bedrock.types.guardrail_description.GuardrailDescription"
        ] = None,
        topic_policy_config: Optional[
            "capo_bedrock.types.guardrail_topic_policy_config.GuardrailTopicPolicyConfig"
        ] = None,
        content_policy_config: Optional[
            "capo_bedrock.types.guardrail_content_policy_config.GuardrailContentPolicyConfig"
        ] = None,
        word_policy_config: Optional[
            "capo_bedrock.types.guardrail_word_policy_config.GuardrailWordPolicyConfig"
        ] = None,
        sensitive_information_policy_config: Optional[
            "capo_bedrock.types.guardrail_sensitive_information_policy_config.GuardrailSensitiveInformationPolicyConfig"
        ] = None,
        contextual_grounding_policy_config: Optional[
            "capo_bedrock.types.guardrail_contextual_grounding_policy_config.GuardrailContextualGroundingPolicyConfig"
        ] = None,
        automated_reasoning_policy_config: Optional[
            "capo_bedrock.types.guardrail_automated_reasoning_policy_config.GuardrailAutomatedReasoningPolicyConfig"
        ] = None,
        cross_region_config: Optional[
            "capo_bedrock.types.guardrail_cross_region_config.GuardrailCrossRegionConfig"
        ] = None,
        kms_key_id: Optional["capo_bedrock.types.kms_key_id.KmsKeyId"] = None,
    ) -> "capo_bedrock.types.update_guardrail_response.UpdateGuardrailResponse":
        """<p>Updates a guardrail with the values you specify.</p> <ul> <li> <p>Specify a <code>name</code> and optional <code>description</code>.</p> </li> <li> <p>Specify messages for when the guardrail successfully blocks a prompt or a model response in the <code>blockedInputMessaging</code> and <code>blockedOutputsMessaging</code> fields.</p> </li> <li> <p>Specify topics for the guardrail to deny in the <code>topicPolicyConfig</code> object. Each <a href="https://docs.aws.amazon.com/bedrock/latest/APIReference/API_GuardrailTopicConfig.html">GuardrailTopicConfig</a> object in the <code>topicsConfig</code> list pertains to one topic.</p> <ul> <li> <p>Give a <code>name</code> and <code>description</code> so that the guardrail can properly identify the topic.</p> </li> <li> <p>Specify <code>DENY</code> in the <code>type</code> field.</p> </li> <li> <p>(Optional) Provide up to five prompts that you would categorize as belonging to the topic in the <code>examples</code> list.</p> </li> </ul> </li> <li> <p>Specify filter strengths for the harmful categories defined in Amazon Bedrock in the <code>contentPolicyConfig</code> object. Each <a href="https://docs.aws.amazon.com/bedrock/latest/APIReference/API_GuardrailContentFilterConfig.html">GuardrailContentFilterConfig</a> object in the <code>filtersConfig</code> list pertains to a harmful category. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-content-filters">Content filters</a>. For more information about the fields in a content filter, see <a href="https://docs.aws.amazon.com/bedrock/latest/APIReference/API_GuardrailContentFilterConfig.html">GuardrailContentFilterConfig</a>.</p> <ul> <li> <p>Specify the category in the <code>type</code> field.</p> </li> <li> <p>Specify the strength of the filter for prompts in the <code>inputStrength</code> field and for model responses in the <code>strength</code> field of the <a href="https://docs.aws.amazon.com/bedrock/latest/APIReference/API_GuardrailContentFilterConfig.html">GuardrailContentFilterConfig</a>.</p> </li> </ul> </li> <li> <p>(Optional) For security, include the ARN of a KMS key in the <code>kmsKeyId</code> field.</p> </li> </ul>

        Args:
            guardrail_identifier: <p>The unique identifier of the guardrail. This can be an ID or the ARN.</p>
            name: <p>A name for the guardrail.</p>
            description: <p>A description of the guardrail.</p>
            topic_policy_config: <p>The topic policy to configure for the guardrail.</p>
            content_policy_config: <p>The content policy to configure for the guardrail.</p>
            word_policy_config: <p>The word policy to configure for the guardrail.</p>
            sensitive_information_policy_config: <p>The sensitive information policy to configure for the guardrail.</p>
            contextual_grounding_policy_config: <p>The contextual grounding policy configuration used to update a guardrail.</p>
            automated_reasoning_policy_config: <p>Updated configuration for Automated Reasoning policies associated with the guardrail.</p>
            cross_region_config: <p>The system-defined guardrail profile that you're using with your guardrail. Guardrail profiles define the destination Amazon Web Services Regions where guardrail inference requests can be automatically routed.</p> <p>For more information, see the <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-cross-region.html">Amazon Bedrock User Guide</a>.</p>
            blocked_input_messaging: <p>The message to return when the guardrail blocks a prompt.</p>
            blocked_outputs_messaging: <p>The message to return when the guardrail blocks a model response.</p>
            kms_key_id: <p>The ARN of the KMS key with which to encrypt the guardrail.</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.conflict_exception.ConflictException: <p>Error occurred because of a conflict while performing an operation.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The number of requests exceeds the service quota. Resubmit your request later.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock.types.update_guardrail_request.UpdateGuardrailRequest]",
        ) -> OperationResponse[
            "capo_bedrock.types.update_guardrail_response.UpdateGuardrailResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.update_guardrail

            output, http_response = (
                capo_bedrock._operations.amazon_bedrock_control_plane_service.update_guardrail.update_guardrail(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock.types.update_guardrail_request.UpdateGuardrailRequest = {
            "guardrail_identifier": guardrail_identifier,
            "name": name,
            "blocked_input_messaging": blocked_input_messaging,
            "blocked_outputs_messaging": blocked_outputs_messaging,
        }
        if description is not None:
            input_["description"] = description
        if topic_policy_config is not None:
            input_["topic_policy_config"] = topic_policy_config
        if content_policy_config is not None:
            input_["content_policy_config"] = content_policy_config
        if word_policy_config is not None:
            input_["word_policy_config"] = word_policy_config
        if sensitive_information_policy_config is not None:
            input_["sensitive_information_policy_config"] = (
                sensitive_information_policy_config
            )
        if contextual_grounding_policy_config is not None:
            input_["contextual_grounding_policy_config"] = (
                contextual_grounding_policy_config
            )
        if automated_reasoning_policy_config is not None:
            input_["automated_reasoning_policy_config"] = (
                automated_reasoning_policy_config
            )
        if cross_region_config is not None:
            input_["cross_region_config"] = cross_region_config
        if kms_key_id is not None:
            input_["kms_key_id"] = kms_key_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete(
        self,
        guardrail_identifier: "capo_bedrock.types.guardrail_identifier.GuardrailIdentifier",
        *,
        config_overrides: Optional[BedrockClientConfig] = None,
        guardrail_version: Optional[
            "capo_bedrock.types.guardrail_numerical_version.GuardrailNumericalVersion"
        ] = None,
    ) -> "capo_bedrock.types.delete_guardrail_response.DeleteGuardrailResponse":
        """<p>Deletes a guardrail.</p> <ul> <li> <p>To delete a guardrail, only specify the ARN of the guardrail in the <code>guardrailIdentifier</code> field. If you delete a guardrail, all of its versions will be deleted.</p> </li> <li> <p>To delete a version of a guardrail, specify the ARN of the guardrail in the <code>guardrailIdentifier</code> field and the version in the <code>guardrailVersion</code> field.</p> </li> </ul>

        Args:
            guardrail_identifier: <p>The unique identifier of the guardrail. This can be an ID or the ARN.</p>
            guardrail_version: <p>The version of the guardrail.</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.conflict_exception.ConflictException: <p>Error occurred because of a conflict while performing an operation.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.resource_in_use_exception.ResourceInUseException: <p>Thrown when attempting to delete or modify a resource that is currently being used by other resources or operations. For example, trying to delete an Automated Reasoning policy that is referenced by an active guardrail.</p>
            capo_bedrock.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock.types.delete_guardrail_request.DeleteGuardrailRequest]",
        ) -> OperationResponse[
            "capo_bedrock.types.delete_guardrail_response.DeleteGuardrailResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.delete_guardrail

            output, http_response = (
                capo_bedrock._operations.amazon_bedrock_control_plane_service.delete_guardrail.delete_guardrail(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock.types.delete_guardrail_request.DeleteGuardrailRequest = {
            "guardrail_identifier": guardrail_identifier
        }
        if guardrail_version is not None:
            input_["guardrail_version"] = guardrail_version

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
        config_overrides: Optional[BedrockClientConfig] = None,
        guardrail_identifier: Optional[
            "capo_bedrock.types.guardrail_identifier.GuardrailIdentifier"
        ] = None,
        max_results: Optional["capo_bedrock.types.max_results.MaxResults"] = None,
        next_token: Optional[
            "capo_bedrock.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "capo_bedrock.types.list_guardrails_response.ListGuardrailsResponse":
        """<p>Lists details about all the guardrails in an account. To list the <code>DRAFT</code> version of all your guardrails, don't specify the <code>guardrailIdentifier</code> field. To list all versions of a guardrail, specify the ARN of the guardrail in the <code>guardrailIdentifier</code> field.</p> <p>You can set the maximum number of results to return in a response in the <code>maxResults</code> field. If there are more results than the number you set, the response returns a <code>nextToken</code> that you can send in another <code>ListGuardrails</code> request to see the next batch of results.</p>

        Args:
            guardrail_identifier: <p>The unique identifier of the guardrail. This can be an ID or the ARN.</p>
            max_results: <p>The maximum number of results to return in the response.</p>
            next_token: <p>If there are more results than were returned in the response, the response returns a <code>nextToken</code> that you can send in another <code>ListGuardrails</code> request to see the next batch of results.</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock.types.list_guardrails_request.ListGuardrailsRequest]",
        ) -> OperationResponse[
            "capo_bedrock.types.list_guardrails_response.ListGuardrailsResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.list_guardrails

            output, http_response = (
                capo_bedrock._operations.amazon_bedrock_control_plane_service.list_guardrails.list_guardrails(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock.types.list_guardrails_request.ListGuardrailsRequest = {}
        if guardrail_identifier is not None:
            input_["guardrail_identifier"] = guardrail_identifier
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

    def create_guardrail_version(
        self,
        guardrail_identifier: "capo_bedrock.types.guardrail_identifier.GuardrailIdentifier",
        *,
        config_overrides: Optional[BedrockClientConfig] = None,
        description: Optional[
            "capo_bedrock.types.guardrail_description.GuardrailDescription"
        ] = None,
        client_request_token: Optional[
            "capo_bedrock.types.idempotency_token.IdempotencyToken"
        ] = None,
    ) -> "capo_bedrock.types.create_guardrail_version_response.CreateGuardrailVersionResponse":
        """<p>Creates a version of the guardrail. Use this API to create a snapshot of the guardrail when you are satisfied with a configuration, or to compare the configuration with another version.</p>

        Args:
            guardrail_identifier: <p>The unique identifier of the guardrail. This can be an ID or the ARN.</p>
            description: <p>A description of the guardrail version.</p>
            client_request_token: <p>A unique, case-sensitive identifier to ensure that the API request completes no more than once. If this token matches a previous request, Amazon Bedrock ignores the request, but does not return an error. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html">Ensuring idempotency</a> in the <i>Amazon S3 User Guide</i>.</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.conflict_exception.ConflictException: <p>Error occurred because of a conflict while performing an operation.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The number of requests exceeds the service quota. Resubmit your request later.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock.types.create_guardrail_version_request.CreateGuardrailVersionRequest]",
        ) -> OperationResponse[
            "capo_bedrock.types.create_guardrail_version_response.CreateGuardrailVersionResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.create_guardrail_version

            output, http_response = (
                capo_bedrock._operations.amazon_bedrock_control_plane_service.create_guardrail_version.create_guardrail_version(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock.types.create_guardrail_version_request.CreateGuardrailVersionRequest = {
            "guardrail_identifier": guardrail_identifier
        }
        if description is not None:
            input_["description"] = description
        if client_request_token is None:
            client_request_token = str(uuid.uuid4())
        input_["client_request_token"] = client_request_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncGuardrailsResource:
    def __init__(self, service: AsyncBedrockClient) -> None:
        self._service = service

    async def create(
        self,
        name: "capo_bedrock.types.guardrail_name.GuardrailName",
        blocked_input_messaging: "capo_bedrock.types.guardrail_blocked_messaging.GuardrailBlockedMessaging",
        blocked_outputs_messaging: "capo_bedrock.types.guardrail_blocked_messaging.GuardrailBlockedMessaging",
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
        description: Optional[
            "capo_bedrock.types.guardrail_description.GuardrailDescription"
        ] = None,
        topic_policy_config: Optional[
            "capo_bedrock.types.guardrail_topic_policy_config.GuardrailTopicPolicyConfig"
        ] = None,
        content_policy_config: Optional[
            "capo_bedrock.types.guardrail_content_policy_config.GuardrailContentPolicyConfig"
        ] = None,
        word_policy_config: Optional[
            "capo_bedrock.types.guardrail_word_policy_config.GuardrailWordPolicyConfig"
        ] = None,
        sensitive_information_policy_config: Optional[
            "capo_bedrock.types.guardrail_sensitive_information_policy_config.GuardrailSensitiveInformationPolicyConfig"
        ] = None,
        contextual_grounding_policy_config: Optional[
            "capo_bedrock.types.guardrail_contextual_grounding_policy_config.GuardrailContextualGroundingPolicyConfig"
        ] = None,
        automated_reasoning_policy_config: Optional[
            "capo_bedrock.types.guardrail_automated_reasoning_policy_config.GuardrailAutomatedReasoningPolicyConfig"
        ] = None,
        cross_region_config: Optional[
            "capo_bedrock.types.guardrail_cross_region_config.GuardrailCrossRegionConfig"
        ] = None,
        kms_key_id: Optional["capo_bedrock.types.kms_key_id.KmsKeyId"] = None,
        tags: Optional["capo_bedrock.types.tag_list.TagList"] = None,
        client_request_token: Optional[
            "capo_bedrock.types.idempotency_token.IdempotencyToken"
        ] = None,
    ) -> "capo_bedrock.types.create_guardrail_response.CreateGuardrailResponse":
        """<p>Creates a guardrail to block topics and to implement safeguards for your generative AI applications.</p> <p>You can configure the following policies in a guardrail to avoid undesirable and harmful content, filter out denied topics and words, and remove sensitive information for privacy protection.</p> <ul> <li> <p> <b>Content filters</b> - Adjust filter strengths to block input prompts or model responses containing harmful content.</p> </li> <li> <p> <b>Denied topics</b> - Define a set of topics that are undesirable in the context of your application. These topics will be blocked if detected in user queries or model responses.</p> </li> <li> <p> <b>Word filters</b> - Configure filters to block undesirable words, phrases, and profanity. Such words can include offensive terms, competitor names etc.</p> </li> <li> <p> <b>Sensitive information filters</b> - Block or mask sensitive information such as personally identifiable information (PII) or custom regex in user inputs and model responses.</p> </li> </ul> <p>In addition to the above policies, you can also configure the messages to be returned to the user if a user input or model response is in violation of the policies defined in the guardrail.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails.html">Amazon Bedrock Guardrails</a> in the <i>Amazon Bedrock User Guide</i>.</p>

        Args:
            name: <p>The name to give the guardrail.</p>
            description: <p>A description of the guardrail.</p>
            topic_policy_config: <p>The topic policies to configure for the guardrail.</p>
            content_policy_config: <p>The content filter policies to configure for the guardrail.</p>
            word_policy_config: <p>The word policy you configure for the guardrail.</p>
            sensitive_information_policy_config: <p>The sensitive information policy to configure for the guardrail.</p>
            contextual_grounding_policy_config: <p>The contextual grounding policy configuration used to create a guardrail.</p>
            automated_reasoning_policy_config: <p>Optional configuration for integrating Automated Reasoning policies with the new guardrail.</p>
            cross_region_config: <p>The system-defined guardrail profile that you're using with your guardrail. Guardrail profiles define the destination Amazon Web Services Regions where guardrail inference requests can be automatically routed.</p> <p>For more information, see the <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-cross-region.html">Amazon Bedrock User Guide</a>.</p>
            blocked_input_messaging: <p>The message to return when the guardrail blocks a prompt.</p>
            blocked_outputs_messaging: <p>The message to return when the guardrail blocks a model response.</p>
            kms_key_id: <p>The ARN of the KMS key that you use to encrypt the guardrail.</p>
            tags: <p>The tags that you want to attach to the guardrail. </p>
            client_request_token: <p>A unique, case-sensitive identifier to ensure that the API request completes no more than once. If this token matches a previous request, Amazon Bedrock ignores the request, but does not return an error. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html">Ensuring idempotency</a> in the <i>Amazon S3 User Guide</i>.</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.conflict_exception.ConflictException: <p>Error occurred because of a conflict while performing an operation.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The number of requests exceeds the service quota. Resubmit your request later.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.too_many_tags_exception.TooManyTagsException: <p>The request contains more tags than can be associated with a resource (50 tags per resource). The maximum number of tags includes both existing tags and those included in your current request. </p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock.types.create_guardrail_request.CreateGuardrailRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock.types.create_guardrail_response.CreateGuardrailResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.create_guardrail

            (
                output,
                http_response,
            ) = await capo_bedrock._operations.amazon_bedrock_control_plane_service.create_guardrail.async_create_guardrail(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock.types.create_guardrail_request.CreateGuardrailRequest = {
            "name": name,
            "blocked_input_messaging": blocked_input_messaging,
            "blocked_outputs_messaging": blocked_outputs_messaging,
        }
        if description is not None:
            input_["description"] = description
        if topic_policy_config is not None:
            input_["topic_policy_config"] = topic_policy_config
        if content_policy_config is not None:
            input_["content_policy_config"] = content_policy_config
        if word_policy_config is not None:
            input_["word_policy_config"] = word_policy_config
        if sensitive_information_policy_config is not None:
            input_["sensitive_information_policy_config"] = (
                sensitive_information_policy_config
            )
        if contextual_grounding_policy_config is not None:
            input_["contextual_grounding_policy_config"] = (
                contextual_grounding_policy_config
            )
        if automated_reasoning_policy_config is not None:
            input_["automated_reasoning_policy_config"] = (
                automated_reasoning_policy_config
            )
        if cross_region_config is not None:
            input_["cross_region_config"] = cross_region_config
        if kms_key_id is not None:
            input_["kms_key_id"] = kms_key_id
        if tags is not None:
            input_["tags"] = tags
        if client_request_token is None:
            client_request_token = str(uuid.uuid4())
        input_["client_request_token"] = client_request_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def read(
        self,
        guardrail_identifier: "capo_bedrock.types.guardrail_identifier.GuardrailIdentifier",
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
        guardrail_version: Optional[
            "capo_bedrock.types.guardrail_version.GuardrailVersion"
        ] = None,
    ) -> "capo_bedrock.types.get_guardrail_response.GetGuardrailResponse":
        """<p>Gets details about a guardrail. If you don't specify a version, the response returns details for the <code>DRAFT</code> version.</p>

        Args:
            guardrail_identifier: <p>The unique identifier of the guardrail for which to get details. This can be an ID or the ARN.</p>
            guardrail_version: <p>The version of the guardrail for which to get details. If you don't specify a version, the response returns details for the <code>DRAFT</code> version.</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock.types.get_guardrail_request.GetGuardrailRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock.types.get_guardrail_response.GetGuardrailResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.get_guardrail

            (
                output,
                http_response,
            ) = await capo_bedrock._operations.amazon_bedrock_control_plane_service.get_guardrail.async_get_guardrail(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock.types.get_guardrail_request.GetGuardrailRequest = {
            "guardrail_identifier": guardrail_identifier
        }
        if guardrail_version is not None:
            input_["guardrail_version"] = guardrail_version

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update(
        self,
        guardrail_identifier: "capo_bedrock.types.guardrail_identifier.GuardrailIdentifier",
        name: "capo_bedrock.types.guardrail_name.GuardrailName",
        blocked_input_messaging: "capo_bedrock.types.guardrail_blocked_messaging.GuardrailBlockedMessaging",
        blocked_outputs_messaging: "capo_bedrock.types.guardrail_blocked_messaging.GuardrailBlockedMessaging",
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
        description: Optional[
            "capo_bedrock.types.guardrail_description.GuardrailDescription"
        ] = None,
        topic_policy_config: Optional[
            "capo_bedrock.types.guardrail_topic_policy_config.GuardrailTopicPolicyConfig"
        ] = None,
        content_policy_config: Optional[
            "capo_bedrock.types.guardrail_content_policy_config.GuardrailContentPolicyConfig"
        ] = None,
        word_policy_config: Optional[
            "capo_bedrock.types.guardrail_word_policy_config.GuardrailWordPolicyConfig"
        ] = None,
        sensitive_information_policy_config: Optional[
            "capo_bedrock.types.guardrail_sensitive_information_policy_config.GuardrailSensitiveInformationPolicyConfig"
        ] = None,
        contextual_grounding_policy_config: Optional[
            "capo_bedrock.types.guardrail_contextual_grounding_policy_config.GuardrailContextualGroundingPolicyConfig"
        ] = None,
        automated_reasoning_policy_config: Optional[
            "capo_bedrock.types.guardrail_automated_reasoning_policy_config.GuardrailAutomatedReasoningPolicyConfig"
        ] = None,
        cross_region_config: Optional[
            "capo_bedrock.types.guardrail_cross_region_config.GuardrailCrossRegionConfig"
        ] = None,
        kms_key_id: Optional["capo_bedrock.types.kms_key_id.KmsKeyId"] = None,
    ) -> "capo_bedrock.types.update_guardrail_response.UpdateGuardrailResponse":
        """<p>Updates a guardrail with the values you specify.</p> <ul> <li> <p>Specify a <code>name</code> and optional <code>description</code>.</p> </li> <li> <p>Specify messages for when the guardrail successfully blocks a prompt or a model response in the <code>blockedInputMessaging</code> and <code>blockedOutputsMessaging</code> fields.</p> </li> <li> <p>Specify topics for the guardrail to deny in the <code>topicPolicyConfig</code> object. Each <a href="https://docs.aws.amazon.com/bedrock/latest/APIReference/API_GuardrailTopicConfig.html">GuardrailTopicConfig</a> object in the <code>topicsConfig</code> list pertains to one topic.</p> <ul> <li> <p>Give a <code>name</code> and <code>description</code> so that the guardrail can properly identify the topic.</p> </li> <li> <p>Specify <code>DENY</code> in the <code>type</code> field.</p> </li> <li> <p>(Optional) Provide up to five prompts that you would categorize as belonging to the topic in the <code>examples</code> list.</p> </li> </ul> </li> <li> <p>Specify filter strengths for the harmful categories defined in Amazon Bedrock in the <code>contentPolicyConfig</code> object. Each <a href="https://docs.aws.amazon.com/bedrock/latest/APIReference/API_GuardrailContentFilterConfig.html">GuardrailContentFilterConfig</a> object in the <code>filtersConfig</code> list pertains to a harmful category. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-content-filters">Content filters</a>. For more information about the fields in a content filter, see <a href="https://docs.aws.amazon.com/bedrock/latest/APIReference/API_GuardrailContentFilterConfig.html">GuardrailContentFilterConfig</a>.</p> <ul> <li> <p>Specify the category in the <code>type</code> field.</p> </li> <li> <p>Specify the strength of the filter for prompts in the <code>inputStrength</code> field and for model responses in the <code>strength</code> field of the <a href="https://docs.aws.amazon.com/bedrock/latest/APIReference/API_GuardrailContentFilterConfig.html">GuardrailContentFilterConfig</a>.</p> </li> </ul> </li> <li> <p>(Optional) For security, include the ARN of a KMS key in the <code>kmsKeyId</code> field.</p> </li> </ul>

        Args:
            guardrail_identifier: <p>The unique identifier of the guardrail. This can be an ID or the ARN.</p>
            name: <p>A name for the guardrail.</p>
            description: <p>A description of the guardrail.</p>
            topic_policy_config: <p>The topic policy to configure for the guardrail.</p>
            content_policy_config: <p>The content policy to configure for the guardrail.</p>
            word_policy_config: <p>The word policy to configure for the guardrail.</p>
            sensitive_information_policy_config: <p>The sensitive information policy to configure for the guardrail.</p>
            contextual_grounding_policy_config: <p>The contextual grounding policy configuration used to update a guardrail.</p>
            automated_reasoning_policy_config: <p>Updated configuration for Automated Reasoning policies associated with the guardrail.</p>
            cross_region_config: <p>The system-defined guardrail profile that you're using with your guardrail. Guardrail profiles define the destination Amazon Web Services Regions where guardrail inference requests can be automatically routed.</p> <p>For more information, see the <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-cross-region.html">Amazon Bedrock User Guide</a>.</p>
            blocked_input_messaging: <p>The message to return when the guardrail blocks a prompt.</p>
            blocked_outputs_messaging: <p>The message to return when the guardrail blocks a model response.</p>
            kms_key_id: <p>The ARN of the KMS key with which to encrypt the guardrail.</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.conflict_exception.ConflictException: <p>Error occurred because of a conflict while performing an operation.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The number of requests exceeds the service quota. Resubmit your request later.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock.types.update_guardrail_request.UpdateGuardrailRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock.types.update_guardrail_response.UpdateGuardrailResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.update_guardrail

            (
                output,
                http_response,
            ) = await capo_bedrock._operations.amazon_bedrock_control_plane_service.update_guardrail.async_update_guardrail(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock.types.update_guardrail_request.UpdateGuardrailRequest = {
            "guardrail_identifier": guardrail_identifier,
            "name": name,
            "blocked_input_messaging": blocked_input_messaging,
            "blocked_outputs_messaging": blocked_outputs_messaging,
        }
        if description is not None:
            input_["description"] = description
        if topic_policy_config is not None:
            input_["topic_policy_config"] = topic_policy_config
        if content_policy_config is not None:
            input_["content_policy_config"] = content_policy_config
        if word_policy_config is not None:
            input_["word_policy_config"] = word_policy_config
        if sensitive_information_policy_config is not None:
            input_["sensitive_information_policy_config"] = (
                sensitive_information_policy_config
            )
        if contextual_grounding_policy_config is not None:
            input_["contextual_grounding_policy_config"] = (
                contextual_grounding_policy_config
            )
        if automated_reasoning_policy_config is not None:
            input_["automated_reasoning_policy_config"] = (
                automated_reasoning_policy_config
            )
        if cross_region_config is not None:
            input_["cross_region_config"] = cross_region_config
        if kms_key_id is not None:
            input_["kms_key_id"] = kms_key_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete(
        self,
        guardrail_identifier: "capo_bedrock.types.guardrail_identifier.GuardrailIdentifier",
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
        guardrail_version: Optional[
            "capo_bedrock.types.guardrail_numerical_version.GuardrailNumericalVersion"
        ] = None,
    ) -> "capo_bedrock.types.delete_guardrail_response.DeleteGuardrailResponse":
        """<p>Deletes a guardrail.</p> <ul> <li> <p>To delete a guardrail, only specify the ARN of the guardrail in the <code>guardrailIdentifier</code> field. If you delete a guardrail, all of its versions will be deleted.</p> </li> <li> <p>To delete a version of a guardrail, specify the ARN of the guardrail in the <code>guardrailIdentifier</code> field and the version in the <code>guardrailVersion</code> field.</p> </li> </ul>

        Args:
            guardrail_identifier: <p>The unique identifier of the guardrail. This can be an ID or the ARN.</p>
            guardrail_version: <p>The version of the guardrail.</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.conflict_exception.ConflictException: <p>Error occurred because of a conflict while performing an operation.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.resource_in_use_exception.ResourceInUseException: <p>Thrown when attempting to delete or modify a resource that is currently being used by other resources or operations. For example, trying to delete an Automated Reasoning policy that is referenced by an active guardrail.</p>
            capo_bedrock.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock.types.delete_guardrail_request.DeleteGuardrailRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock.types.delete_guardrail_response.DeleteGuardrailResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.delete_guardrail

            (
                output,
                http_response,
            ) = await capo_bedrock._operations.amazon_bedrock_control_plane_service.delete_guardrail.async_delete_guardrail(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock.types.delete_guardrail_request.DeleteGuardrailRequest = {
            "guardrail_identifier": guardrail_identifier
        }
        if guardrail_version is not None:
            input_["guardrail_version"] = guardrail_version

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
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
        guardrail_identifier: Optional[
            "capo_bedrock.types.guardrail_identifier.GuardrailIdentifier"
        ] = None,
        max_results: Optional["capo_bedrock.types.max_results.MaxResults"] = None,
        next_token: Optional[
            "capo_bedrock.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "capo_bedrock.types.list_guardrails_response.ListGuardrailsResponse":
        """<p>Lists details about all the guardrails in an account. To list the <code>DRAFT</code> version of all your guardrails, don't specify the <code>guardrailIdentifier</code> field. To list all versions of a guardrail, specify the ARN of the guardrail in the <code>guardrailIdentifier</code> field.</p> <p>You can set the maximum number of results to return in a response in the <code>maxResults</code> field. If there are more results than the number you set, the response returns a <code>nextToken</code> that you can send in another <code>ListGuardrails</code> request to see the next batch of results.</p>

        Args:
            guardrail_identifier: <p>The unique identifier of the guardrail. This can be an ID or the ARN.</p>
            max_results: <p>The maximum number of results to return in the response.</p>
            next_token: <p>If there are more results than were returned in the response, the response returns a <code>nextToken</code> that you can send in another <code>ListGuardrails</code> request to see the next batch of results.</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock.types.list_guardrails_request.ListGuardrailsRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock.types.list_guardrails_response.ListGuardrailsResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.list_guardrails

            (
                output,
                http_response,
            ) = await capo_bedrock._operations.amazon_bedrock_control_plane_service.list_guardrails.async_list_guardrails(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock.types.list_guardrails_request.ListGuardrailsRequest = {}
        if guardrail_identifier is not None:
            input_["guardrail_identifier"] = guardrail_identifier
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

    async def create_guardrail_version(
        self,
        guardrail_identifier: "capo_bedrock.types.guardrail_identifier.GuardrailIdentifier",
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
        description: Optional[
            "capo_bedrock.types.guardrail_description.GuardrailDescription"
        ] = None,
        client_request_token: Optional[
            "capo_bedrock.types.idempotency_token.IdempotencyToken"
        ] = None,
    ) -> "capo_bedrock.types.create_guardrail_version_response.CreateGuardrailVersionResponse":
        """<p>Creates a version of the guardrail. Use this API to create a snapshot of the guardrail when you are satisfied with a configuration, or to compare the configuration with another version.</p>

        Args:
            guardrail_identifier: <p>The unique identifier of the guardrail. This can be an ID or the ARN.</p>
            description: <p>A description of the guardrail version.</p>
            client_request_token: <p>A unique, case-sensitive identifier to ensure that the API request completes no more than once. If this token matches a previous request, Amazon Bedrock ignores the request, but does not return an error. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html">Ensuring idempotency</a> in the <i>Amazon S3 User Guide</i>.</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.conflict_exception.ConflictException: <p>Error occurred because of a conflict while performing an operation.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The number of requests exceeds the service quota. Resubmit your request later.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock.types.create_guardrail_version_request.CreateGuardrailVersionRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock.types.create_guardrail_version_response.CreateGuardrailVersionResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.create_guardrail_version

            (
                output,
                http_response,
            ) = await capo_bedrock._operations.amazon_bedrock_control_plane_service.create_guardrail_version.async_create_guardrail_version(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock.types.create_guardrail_version_request.CreateGuardrailVersionRequest = {
            "guardrail_identifier": guardrail_identifier
        }
        if description is not None:
            input_["description"] = description
        if client_request_token is None:
            client_request_token = str(uuid.uuid4())
        input_["client_request_token"] = client_request_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
