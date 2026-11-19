from __future__ import annotations

from typing import TYPE_CHECKING, Optional

import capo_elementalinference._auth._signers
import capo_elementalinference._auth._sigv4
from capo_elementalinference._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationLogging,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_elementalinference.types.choose_one_question_list
    import capo_elementalinference.types.create_question_set_request
    import capo_elementalinference.types.create_question_set_response
    import capo_elementalinference.types.create_question_set_version_request
    import capo_elementalinference.types.create_question_set_version_response
    import capo_elementalinference.types.delete_question_set_request
    import capo_elementalinference.types.delete_question_set_response
    import capo_elementalinference.types.delete_question_set_version_request
    import capo_elementalinference.types.delete_question_set_version_response
    import capo_elementalinference.types.get_question_set_request
    import capo_elementalinference.types.get_question_set_response
    import capo_elementalinference.types.list_question_set_versions_request
    import capo_elementalinference.types.list_question_set_versions_response
    import capo_elementalinference.types.list_question_sets_request
    import capo_elementalinference.types.list_question_sets_response
    import capo_elementalinference.types.published_question_set_version
    import capo_elementalinference.types.question_set_id
    import capo_elementalinference.types.question_set_sha256
    import capo_elementalinference.types.question_set_summary
    import capo_elementalinference.types.question_set_version
    import capo_elementalinference.types.question_set_version_description
    import capo_elementalinference.types.question_set_version_summary
    import capo_elementalinference.types.resource_name
    import capo_elementalinference.types.tag_map
    import capo_elementalinference.types.update_question_set_request
    import capo_elementalinference.types.update_question_set_response
    import capo_elementalinference.types.yes_no_per_option_question_list
    import capo_elementalinference.types.yes_no_question_list
    from capo_elementalinference._services.async_elemental_inference import (
        AsyncElementalInferenceClient,
        AsyncElementalInferenceClientConfig,
    )
    from capo_elementalinference._services.elemental_inference import (
        ElementalInferenceClient,
        ElementalInferenceClientConfig,
    )


class QuestionSetResource:
    def __init__(self, service: ElementalInferenceClient) -> None:
        self._service = service

    def create(
        self,
        name: "capo_elementalinference.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[ElementalInferenceClientConfig] = None,
        yes_no: Optional[
            "capo_elementalinference.types.yes_no_question_list.YesNoQuestionList"
        ] = None,
        yes_no_per_option: Optional[
            "capo_elementalinference.types.yes_no_per_option_question_list.YesNoPerOptionQuestionList"
        ] = None,
        choose_one: Optional[
            "capo_elementalinference.types.choose_one_question_list.ChooseOneQuestionList"
        ] = None,
        tags: Optional["capo_elementalinference.types.tag_map.TagMap"] = None,
    ) -> "capo_elementalinference.types.create_question_set_response.CreateQuestionSetResponse":
        """<p>Creates a question set. Use a question set to get answers about content that's specific to your business, in addition to the built-in contextual metadata classifications. A question set contains your own questions. You ask Elemental Inference these questions about each shot or scene of the media in a contextual metadata output, and Elemental Inference answers each question with scores. To use a question set, reference it in the customQuestions property of the contextual metadata configuration of a feed output. </p> <p>CreateQuestionSet creates the question set with a DRAFT version that contains the questions in the request. To change DRAFT, use UpdateQuestionSet. To publish DRAFT as a numbered version, use CreateQuestionSetVersion. You can't change a published version. </p> <p>A question set can contain the following types of questions. You must specify at least one question. </p> <ul> <li> <p>yesNo – Elemental Inference answers yes or no.</p> </li> <li> <p>yesNoPerOption – Elemental Inference answers yes or no for each option.</p> </li> <li> <p>chooseOne – Elemental Inference chooses one of the options.</p> </li> </ul> <p>A version can contain up to 100 scored items, where each yesNo question, each option of a yesNoPerOption question, and each chooseOne question counts as one item. The name of each question must be unique across all three types. </p>

        Args:
            yes_no: <p>An array of questions that Elemental Inference answers with yes or no. You can specify up to 50 yesNo questions. An empty array is the same as omitting this property. </p>
            yes_no_per_option: <p>An array of questions that you ask about each of their options. Elemental Inference answers yes or no for each option. You can specify up to 10 yesNoPerOption questions. An empty array is the same as omitting this property. </p>
            choose_one: <p>An array of questions that Elemental Inference answers by choosing one of their options. You can specify up to 10 chooseOne questions. An empty array is the same as omitting this property. </p>
            name: <p>A user-friendly name for this question set.</p>
            tags: <p>Optional tags to associate with the question set. You can also add tags later, using TagResource. </p>

        Raises:
            capo_elementalinference.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_elementalinference.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict.</p>
            capo_elementalinference.errors.internal_server_error_exception.InternalServerErrorException: <p>An internal server error occurred. This is a temporary condition and the request can be retried. If the problem persists, contact AWS Support. </p>
            capo_elementalinference.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request was rejected because it would exceed one or more service quotas for your account. Review your service quotas and either delete unused resources or request a quota increase. </p>
            capo_elementalinference.errors.too_many_request_exception.TooManyRequestException: <p>The request was denied due to request throttling. Too many requests have been made within a given time period. Reduce the frequency of requests and use exponential backoff when retrying. </p>
            capo_elementalinference.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service. Check the error message for details about which parameter or field is invalid and correct the request before retrying. </p>
            capo_elementalinference.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_elementalinference.types.create_question_set_request.CreateQuestionSetRequest]",
        ) -> OperationResponse[
            "capo_elementalinference.types.create_question_set_response.CreateQuestionSetResponse"
        ]:
            import capo_elementalinference._operations.elemental_inference.create_question_set

            output, http_response = (
                capo_elementalinference._operations.elemental_inference.create_question_set.create_question_set(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("CreateQuestionSet")
        )
        input_: capo_elementalinference.types.create_question_set_request.CreateQuestionSetRequest = {
            "name": name
        }
        if yes_no is not None:
            input_["yes_no"] = yes_no
        if yes_no_per_option is not None:
            input_["yes_no_per_option"] = yes_no_per_option
        if choose_one is not None:
            input_["choose_one"] = choose_one
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
        id: "capo_elementalinference.types.question_set_id.QuestionSetId",
        *,
        config_overrides: Optional[ElementalInferenceClientConfig] = None,
        question_set_version: Optional[
            "capo_elementalinference.types.question_set_version.QuestionSetVersion"
        ] = None,
    ) -> (
        "capo_elementalinference.types.get_question_set_response.GetQuestionSetResponse"
    ):
        """<p>Retrieves information about the specified question set at one version. By default, GetQuestionSet returns the DRAFT version. To retrieve a published version, specify questionSetVersion. </p>

        Args:
            id: <p>The ID of the question set to retrieve.</p>
            question_set_version: <p>The version of the question set to retrieve: DRAFT or the number of a published version. If you don't specify a version, Elemental Inference returns DRAFT. </p>

        Raises:
            capo_elementalinference.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_elementalinference.errors.internal_server_error_exception.InternalServerErrorException: <p>An internal server error occurred. This is a temporary condition and the request can be retried. If the problem persists, contact AWS Support. </p>
            capo_elementalinference.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the action doesn't exist.</p>
            capo_elementalinference.errors.too_many_request_exception.TooManyRequestException: <p>The request was denied due to request throttling. Too many requests have been made within a given time period. Reduce the frequency of requests and use exponential backoff when retrying. </p>
            capo_elementalinference.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service. Check the error message for details about which parameter or field is invalid and correct the request before retrying. </p>
            capo_elementalinference.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_elementalinference.types.get_question_set_request.GetQuestionSetRequest]",
        ) -> OperationResponse[
            "capo_elementalinference.types.get_question_set_response.GetQuestionSetResponse"
        ]:
            import capo_elementalinference._operations.elemental_inference.get_question_set

            output, http_response = (
                capo_elementalinference._operations.elemental_inference.get_question_set.get_question_set(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetQuestionSet")
        )
        input_: capo_elementalinference.types.get_question_set_request.GetQuestionSetRequest = {
            "id": id
        }
        if question_set_version is not None:
            input_["question_set_version"] = question_set_version

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update(
        self,
        id: "capo_elementalinference.types.question_set_id.QuestionSetId",
        *,
        config_overrides: Optional[ElementalInferenceClientConfig] = None,
        yes_no: Optional[
            "capo_elementalinference.types.yes_no_question_list.YesNoQuestionList"
        ] = None,
        yes_no_per_option: Optional[
            "capo_elementalinference.types.yes_no_per_option_question_list.YesNoPerOptionQuestionList"
        ] = None,
        choose_one: Optional[
            "capo_elementalinference.types.choose_one_question_list.ChooseOneQuestionList"
        ] = None,
        name: Optional[
            "capo_elementalinference.types.resource_name.ResourceName"
        ] = None,
    ) -> "capo_elementalinference.types.update_question_set_response.UpdateQuestionSetResponse":
        """<p>Updates the DRAFT version of the specified question set. UpdateQuestionSet doesn't create a version and doesn't change published versions. To publish the updated DRAFT as a new version, use CreateQuestionSetVersion. </p> <p>UpdateQuestionSet replaces questions one type at a time. For each of yesNo, yesNoPerOption, and chooseOne: if you omit the array, DRAFT keeps its questions of that type. If you include the array, it replaces all the questions of that type in DRAFT. If you include an empty array, DRAFT no longer has questions of that type. The updated DRAFT must follow the same rules as in CreateQuestionSet, and Elemental Inference applies those rules to the questions that DRAFT keeps as well as to the questions in the request. </p> <p>Feeds that reference the DRAFT version use the updated questions. To make sure that the questions for a feed don't change, reference a published version instead. </p>

        Args:
            id: <p>The ID of the question set to update.</p>
            yes_no: <p>An array of questions that Elemental Inference answers with yes or no, to replace all the yesNo questions in DRAFT. You can specify up to 50 yesNo questions. If not specified, the yesNo questions are not changed. To remove all the yesNo questions, specify an empty array. </p>
            yes_no_per_option: <p>An array of questions that you ask about each of their options, to replace all the yesNoPerOption questions in DRAFT. You can specify up to 10 yesNoPerOption questions. If not specified, the yesNoPerOption questions are not changed. To remove all the yesNoPerOption questions, specify an empty array. </p>
            choose_one: <p>An array of questions that Elemental Inference answers by choosing one of their options, to replace all the chooseOne questions in DRAFT. You can specify up to 10 chooseOne questions. If not specified, the chooseOne questions are not changed. To remove all the chooseOne questions, specify an empty array. </p>
            name: <p>A new name for the question set. If not specified, the name is not changed.</p>

        Raises:
            capo_elementalinference.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_elementalinference.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict.</p>
            capo_elementalinference.errors.internal_server_error_exception.InternalServerErrorException: <p>An internal server error occurred. This is a temporary condition and the request can be retried. If the problem persists, contact AWS Support. </p>
            capo_elementalinference.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the action doesn't exist.</p>
            capo_elementalinference.errors.too_many_request_exception.TooManyRequestException: <p>The request was denied due to request throttling. Too many requests have been made within a given time period. Reduce the frequency of requests and use exponential backoff when retrying. </p>
            capo_elementalinference.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service. Check the error message for details about which parameter or field is invalid and correct the request before retrying. </p>
            capo_elementalinference.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_elementalinference.types.update_question_set_request.UpdateQuestionSetRequest]",
        ) -> OperationResponse[
            "capo_elementalinference.types.update_question_set_response.UpdateQuestionSetResponse"
        ]:
            import capo_elementalinference._operations.elemental_inference.update_question_set

            output, http_response = (
                capo_elementalinference._operations.elemental_inference.update_question_set.update_question_set(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("UpdateQuestionSet")
        )
        input_: capo_elementalinference.types.update_question_set_request.UpdateQuestionSetRequest = {
            "id": id
        }
        if yes_no is not None:
            input_["yes_no"] = yes_no
        if yes_no_per_option is not None:
            input_["yes_no_per_option"] = yes_no_per_option
        if choose_one is not None:
            input_["choose_one"] = choose_one
        if name is not None:
            input_["name"] = name

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete(
        self,
        id: "capo_elementalinference.types.question_set_id.QuestionSetId",
        *,
        config_overrides: Optional[ElementalInferenceClientConfig] = None,
    ) -> "capo_elementalinference.types.delete_question_set_response.DeleteQuestionSetResponse":
        """<p>Deletes the specified question set, including its DRAFT version and all its published versions. You can't delete a question set while any feed references any of its versions, including an archived feed. You must first remove the question set from the customQuestions configuration of each feed output that references it, or delete those feeds. </p>

        Args:
            id: <p>The ID of the question set to delete.</p>

        Raises:
            capo_elementalinference.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_elementalinference.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict.</p>
            capo_elementalinference.errors.internal_server_error_exception.InternalServerErrorException: <p>An internal server error occurred. This is a temporary condition and the request can be retried. If the problem persists, contact AWS Support. </p>
            capo_elementalinference.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the action doesn't exist.</p>
            capo_elementalinference.errors.too_many_request_exception.TooManyRequestException: <p>The request was denied due to request throttling. Too many requests have been made within a given time period. Reduce the frequency of requests and use exponential backoff when retrying. </p>
            capo_elementalinference.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service. Check the error message for details about which parameter or field is invalid and correct the request before retrying. </p>
            capo_elementalinference.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_elementalinference.types.delete_question_set_request.DeleteQuestionSetRequest]",
        ) -> OperationResponse[
            "capo_elementalinference.types.delete_question_set_response.DeleteQuestionSetResponse"
        ]:
            import capo_elementalinference._operations.elemental_inference.delete_question_set

            output, http_response = (
                capo_elementalinference._operations.elemental_inference.delete_question_set.delete_question_set(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteQuestionSet")
        )
        input_: capo_elementalinference.types.delete_question_set_request.DeleteQuestionSetRequest = {
            "id": id
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
        config_overrides: Optional[ElementalInferenceClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
    ) -> "capo_elementalinference.types.list_question_sets_response.ListQuestionSetsResponse":
        """<p>Lists the question sets in your account. The response doesn't include the questions in each question set. To retrieve them, use GetQuestionSet. </p>

        Args:
            max_results: <p>The maximum number of results to return per API request. Valid range: 1 to 100.</p>
            next_token: <p>The token that identifies the next batch of results to return.</p>

        Raises:
            capo_elementalinference.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_elementalinference.errors.internal_server_error_exception.InternalServerErrorException: <p>An internal server error occurred. This is a temporary condition and the request can be retried. If the problem persists, contact AWS Support. </p>
            capo_elementalinference.errors.too_many_request_exception.TooManyRequestException: <p>The request was denied due to request throttling. Too many requests have been made within a given time period. Reduce the frequency of requests and use exponential backoff when retrying. </p>
            capo_elementalinference.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service. Check the error message for details about which parameter or field is invalid and correct the request before retrying. </p>
            capo_elementalinference.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_elementalinference.types.list_question_sets_request.ListQuestionSetsRequest]",
        ) -> OperationResponse[
            "capo_elementalinference.types.list_question_sets_response.ListQuestionSetsResponse"
        ]:
            import capo_elementalinference._operations.elemental_inference.list_question_sets

            output, http_response = (
                capo_elementalinference._operations.elemental_inference.list_question_sets.list_question_sets(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListQuestionSets")
        )
        input_: capo_elementalinference.types.list_question_sets_request.ListQuestionSetsRequest = {}
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

    def create_question_set_version(
        self,
        id: "capo_elementalinference.types.question_set_id.QuestionSetId",
        *,
        config_overrides: Optional[ElementalInferenceClientConfig] = None,
        sha256: Optional[
            "capo_elementalinference.types.question_set_sha256.QuestionSetSha256"
        ] = None,
        description: Optional[
            "capo_elementalinference.types.question_set_version_description.QuestionSetVersionDescription"
        ] = None,
    ) -> "capo_elementalinference.types.create_question_set_version_response.CreateQuestionSetVersionResponse":
        """<p>Publishes the DRAFT version of the specified question set as a new version. The new version has the same name and questions as DRAFT, and you can't change it. DRAFT doesn't change, so you can continue to update it. </p> <p>Version numbers start at 1, and each new version has the next number. Elemental Inference never reuses a version number, even after you delete that version. </p> <p>If DRAFT hasn't changed since the latest published version, Elemental Inference doesn't create a version. Instead, it returns the latest version. A change to the name of the question set counts as a change to DRAFT. </p> <p>A question set can have a limited number of versions. If the question set already has the maximum number of versions, Elemental Inference returns ServiceQuotaExceededException. To free space for a new version, delete a version that you no longer need, or create a new question set. </p>

        Args:
            id: <p>The ID of the question set whose DRAFT version you want to publish.</p>
            sha256: <p>The SHA-256 hash of the DRAFT version that you want to publish, as returned by GetQuestionSet or UpdateQuestionSet. If you specify this value, Elemental Inference publishes DRAFT only if its current hash matches. If it doesn't match, because DRAFT changed after you retrieved it, the request fails with ConflictException. </p> <p>If you don't specify this value, Elemental Inference publishes DRAFT as it is when it receives the request. </p>
            description: <p>A description of the new version. You can't change the description after Elemental Inference publishes the version. If DRAFT hasn't changed since the latest version, Elemental Inference ignores this value and returns the latest version with its existing description. </p> <p>The description can be up to 256 characters. It can contain the letters A-Z and a-z, the digits 0-9, underscores, spaces, and the following characters: <code>- . ' , @ : ;</code>. </p>

        Raises:
            capo_elementalinference.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_elementalinference.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict.</p>
            capo_elementalinference.errors.internal_server_error_exception.InternalServerErrorException: <p>An internal server error occurred. This is a temporary condition and the request can be retried. If the problem persists, contact AWS Support. </p>
            capo_elementalinference.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the action doesn't exist.</p>
            capo_elementalinference.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request was rejected because it would exceed one or more service quotas for your account. Review your service quotas and either delete unused resources or request a quota increase. </p>
            capo_elementalinference.errors.too_many_request_exception.TooManyRequestException: <p>The request was denied due to request throttling. Too many requests have been made within a given time period. Reduce the frequency of requests and use exponential backoff when retrying. </p>
            capo_elementalinference.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service. Check the error message for details about which parameter or field is invalid and correct the request before retrying. </p>
            capo_elementalinference.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_elementalinference.types.create_question_set_version_request.CreateQuestionSetVersionRequest]",
        ) -> OperationResponse[
            "capo_elementalinference.types.create_question_set_version_response.CreateQuestionSetVersionResponse"
        ]:
            import capo_elementalinference._operations.elemental_inference.create_question_set_version

            output, http_response = (
                capo_elementalinference._operations.elemental_inference.create_question_set_version.create_question_set_version(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("CreateQuestionSetVersion")
        )
        input_: capo_elementalinference.types.create_question_set_version_request.CreateQuestionSetVersionRequest = {
            "id": id
        }
        if sha256 is not None:
            input_["sha256"] = sha256
        if description is not None:
            input_["description"] = description

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_question_set_version(
        self,
        id: "capo_elementalinference.types.question_set_id.QuestionSetId",
        question_set_version: "capo_elementalinference.types.published_question_set_version.PublishedQuestionSetVersion",
        *,
        config_overrides: Optional[ElementalInferenceClientConfig] = None,
    ) -> "capo_elementalinference.types.delete_question_set_version_response.DeleteQuestionSetVersionResponse":
        """<p>Deletes a published version of the specified question set. You can't delete a version while a feed references it, including an archived feed. You can't restore a deleted version, and Elemental Inference doesn't reuse its number. </p> <p>You can't delete the DRAFT version on its own. To delete DRAFT, delete the question set by using DeleteQuestionSet. </p> <p>Deleting a version doesn't change the latestVersion of the question set, even if you delete the highest version. </p>

        Args:
            id: <p>The ID of the question set that contains the version.</p>
            question_set_version: <p>The number of the published version to delete. You can't specify DRAFT.</p>

        Raises:
            capo_elementalinference.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_elementalinference.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict.</p>
            capo_elementalinference.errors.internal_server_error_exception.InternalServerErrorException: <p>An internal server error occurred. This is a temporary condition and the request can be retried. If the problem persists, contact AWS Support. </p>
            capo_elementalinference.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the action doesn't exist.</p>
            capo_elementalinference.errors.too_many_request_exception.TooManyRequestException: <p>The request was denied due to request throttling. Too many requests have been made within a given time period. Reduce the frequency of requests and use exponential backoff when retrying. </p>
            capo_elementalinference.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service. Check the error message for details about which parameter or field is invalid and correct the request before retrying. </p>
            capo_elementalinference.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_elementalinference.types.delete_question_set_version_request.DeleteQuestionSetVersionRequest]",
        ) -> OperationResponse[
            "capo_elementalinference.types.delete_question_set_version_response.DeleteQuestionSetVersionResponse"
        ]:
            import capo_elementalinference._operations.elemental_inference.delete_question_set_version

            output, http_response = (
                capo_elementalinference._operations.elemental_inference.delete_question_set_version.delete_question_set_version(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteQuestionSetVersion")
        )
        input_: capo_elementalinference.types.delete_question_set_version_request.DeleteQuestionSetVersionRequest = {
            "id": id,
            "question_set_version": question_set_version,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_question_set_versions(
        self,
        id: "capo_elementalinference.types.question_set_id.QuestionSetId",
        *,
        config_overrides: Optional[ElementalInferenceClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
    ) -> "capo_elementalinference.types.list_question_set_versions_response.ListQuestionSetVersionsResponse":
        """<p>Lists the versions of the specified question set. The list starts with the DRAFT version, followed by the published versions from the highest version number to the lowest. The list doesn't include deleted versions. </p> <p>The response doesn't include the questions in each version. To retrieve them, use GetQuestionSet and specify questionSetVersion. </p>

        Args:
            id: <p>The ID of the question set whose versions you want to list.</p>
            max_results: <p>The maximum number of results to return per API request. Valid range: 1 to 100.</p>
            next_token: <p>The token that identifies the next batch of results to return.</p>

        Raises:
            capo_elementalinference.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_elementalinference.errors.internal_server_error_exception.InternalServerErrorException: <p>An internal server error occurred. This is a temporary condition and the request can be retried. If the problem persists, contact AWS Support. </p>
            capo_elementalinference.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the action doesn't exist.</p>
            capo_elementalinference.errors.too_many_request_exception.TooManyRequestException: <p>The request was denied due to request throttling. Too many requests have been made within a given time period. Reduce the frequency of requests and use exponential backoff when retrying. </p>
            capo_elementalinference.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service. Check the error message for details about which parameter or field is invalid and correct the request before retrying. </p>
            capo_elementalinference.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_elementalinference.types.list_question_set_versions_request.ListQuestionSetVersionsRequest]",
        ) -> OperationResponse[
            "capo_elementalinference.types.list_question_set_versions_response.ListQuestionSetVersionsResponse"
        ]:
            import capo_elementalinference._operations.elemental_inference.list_question_set_versions

            output, http_response = (
                capo_elementalinference._operations.elemental_inference.list_question_set_versions.list_question_set_versions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListQuestionSetVersions")
        )
        input_: capo_elementalinference.types.list_question_set_versions_request.ListQuestionSetVersionsRequest = {
            "id": id
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


class AsyncQuestionSetResource:
    def __init__(self, service: AsyncElementalInferenceClient) -> None:
        self._service = service

    async def create(
        self,
        name: "capo_elementalinference.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AsyncElementalInferenceClientConfig] = None,
        yes_no: Optional[
            "capo_elementalinference.types.yes_no_question_list.YesNoQuestionList"
        ] = None,
        yes_no_per_option: Optional[
            "capo_elementalinference.types.yes_no_per_option_question_list.YesNoPerOptionQuestionList"
        ] = None,
        choose_one: Optional[
            "capo_elementalinference.types.choose_one_question_list.ChooseOneQuestionList"
        ] = None,
        tags: Optional["capo_elementalinference.types.tag_map.TagMap"] = None,
    ) -> "capo_elementalinference.types.create_question_set_response.CreateQuestionSetResponse":
        """<p>Creates a question set. Use a question set to get answers about content that's specific to your business, in addition to the built-in contextual metadata classifications. A question set contains your own questions. You ask Elemental Inference these questions about each shot or scene of the media in a contextual metadata output, and Elemental Inference answers each question with scores. To use a question set, reference it in the customQuestions property of the contextual metadata configuration of a feed output. </p> <p>CreateQuestionSet creates the question set with a DRAFT version that contains the questions in the request. To change DRAFT, use UpdateQuestionSet. To publish DRAFT as a numbered version, use CreateQuestionSetVersion. You can't change a published version. </p> <p>A question set can contain the following types of questions. You must specify at least one question. </p> <ul> <li> <p>yesNo – Elemental Inference answers yes or no.</p> </li> <li> <p>yesNoPerOption – Elemental Inference answers yes or no for each option.</p> </li> <li> <p>chooseOne – Elemental Inference chooses one of the options.</p> </li> </ul> <p>A version can contain up to 100 scored items, where each yesNo question, each option of a yesNoPerOption question, and each chooseOne question counts as one item. The name of each question must be unique across all three types. </p>

        Args:
            yes_no: <p>An array of questions that Elemental Inference answers with yes or no. You can specify up to 50 yesNo questions. An empty array is the same as omitting this property. </p>
            yes_no_per_option: <p>An array of questions that you ask about each of their options. Elemental Inference answers yes or no for each option. You can specify up to 10 yesNoPerOption questions. An empty array is the same as omitting this property. </p>
            choose_one: <p>An array of questions that Elemental Inference answers by choosing one of their options. You can specify up to 10 chooseOne questions. An empty array is the same as omitting this property. </p>
            name: <p>A user-friendly name for this question set.</p>
            tags: <p>Optional tags to associate with the question set. You can also add tags later, using TagResource. </p>

        Raises:
            capo_elementalinference.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_elementalinference.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict.</p>
            capo_elementalinference.errors.internal_server_error_exception.InternalServerErrorException: <p>An internal server error occurred. This is a temporary condition and the request can be retried. If the problem persists, contact AWS Support. </p>
            capo_elementalinference.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request was rejected because it would exceed one or more service quotas for your account. Review your service quotas and either delete unused resources or request a quota increase. </p>
            capo_elementalinference.errors.too_many_request_exception.TooManyRequestException: <p>The request was denied due to request throttling. Too many requests have been made within a given time period. Reduce the frequency of requests and use exponential backoff when retrying. </p>
            capo_elementalinference.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service. Check the error message for details about which parameter or field is invalid and correct the request before retrying. </p>
            capo_elementalinference.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_elementalinference.types.create_question_set_request.CreateQuestionSetRequest]",
        ) -> AsyncOperationResponse[
            "capo_elementalinference.types.create_question_set_response.CreateQuestionSetResponse"
        ]:
            import capo_elementalinference._operations.elemental_inference.create_question_set

            (
                output,
                http_response,
            ) = await capo_elementalinference._operations.elemental_inference.create_question_set.async_create_question_set(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("CreateQuestionSet")
        )
        input_: capo_elementalinference.types.create_question_set_request.CreateQuestionSetRequest = {
            "name": name
        }
        if yes_no is not None:
            input_["yes_no"] = yes_no
        if yes_no_per_option is not None:
            input_["yes_no_per_option"] = yes_no_per_option
        if choose_one is not None:
            input_["choose_one"] = choose_one
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
        id: "capo_elementalinference.types.question_set_id.QuestionSetId",
        *,
        config_overrides: Optional[AsyncElementalInferenceClientConfig] = None,
        question_set_version: Optional[
            "capo_elementalinference.types.question_set_version.QuestionSetVersion"
        ] = None,
    ) -> (
        "capo_elementalinference.types.get_question_set_response.GetQuestionSetResponse"
    ):
        """<p>Retrieves information about the specified question set at one version. By default, GetQuestionSet returns the DRAFT version. To retrieve a published version, specify questionSetVersion. </p>

        Args:
            id: <p>The ID of the question set to retrieve.</p>
            question_set_version: <p>The version of the question set to retrieve: DRAFT or the number of a published version. If you don't specify a version, Elemental Inference returns DRAFT. </p>

        Raises:
            capo_elementalinference.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_elementalinference.errors.internal_server_error_exception.InternalServerErrorException: <p>An internal server error occurred. This is a temporary condition and the request can be retried. If the problem persists, contact AWS Support. </p>
            capo_elementalinference.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the action doesn't exist.</p>
            capo_elementalinference.errors.too_many_request_exception.TooManyRequestException: <p>The request was denied due to request throttling. Too many requests have been made within a given time period. Reduce the frequency of requests and use exponential backoff when retrying. </p>
            capo_elementalinference.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service. Check the error message for details about which parameter or field is invalid and correct the request before retrying. </p>
            capo_elementalinference.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_elementalinference.types.get_question_set_request.GetQuestionSetRequest]",
        ) -> AsyncOperationResponse[
            "capo_elementalinference.types.get_question_set_response.GetQuestionSetResponse"
        ]:
            import capo_elementalinference._operations.elemental_inference.get_question_set

            (
                output,
                http_response,
            ) = await capo_elementalinference._operations.elemental_inference.get_question_set.async_get_question_set(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetQuestionSet")
        )
        input_: capo_elementalinference.types.get_question_set_request.GetQuestionSetRequest = {
            "id": id
        }
        if question_set_version is not None:
            input_["question_set_version"] = question_set_version

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update(
        self,
        id: "capo_elementalinference.types.question_set_id.QuestionSetId",
        *,
        config_overrides: Optional[AsyncElementalInferenceClientConfig] = None,
        yes_no: Optional[
            "capo_elementalinference.types.yes_no_question_list.YesNoQuestionList"
        ] = None,
        yes_no_per_option: Optional[
            "capo_elementalinference.types.yes_no_per_option_question_list.YesNoPerOptionQuestionList"
        ] = None,
        choose_one: Optional[
            "capo_elementalinference.types.choose_one_question_list.ChooseOneQuestionList"
        ] = None,
        name: Optional[
            "capo_elementalinference.types.resource_name.ResourceName"
        ] = None,
    ) -> "capo_elementalinference.types.update_question_set_response.UpdateQuestionSetResponse":
        """<p>Updates the DRAFT version of the specified question set. UpdateQuestionSet doesn't create a version and doesn't change published versions. To publish the updated DRAFT as a new version, use CreateQuestionSetVersion. </p> <p>UpdateQuestionSet replaces questions one type at a time. For each of yesNo, yesNoPerOption, and chooseOne: if you omit the array, DRAFT keeps its questions of that type. If you include the array, it replaces all the questions of that type in DRAFT. If you include an empty array, DRAFT no longer has questions of that type. The updated DRAFT must follow the same rules as in CreateQuestionSet, and Elemental Inference applies those rules to the questions that DRAFT keeps as well as to the questions in the request. </p> <p>Feeds that reference the DRAFT version use the updated questions. To make sure that the questions for a feed don't change, reference a published version instead. </p>

        Args:
            id: <p>The ID of the question set to update.</p>
            yes_no: <p>An array of questions that Elemental Inference answers with yes or no, to replace all the yesNo questions in DRAFT. You can specify up to 50 yesNo questions. If not specified, the yesNo questions are not changed. To remove all the yesNo questions, specify an empty array. </p>
            yes_no_per_option: <p>An array of questions that you ask about each of their options, to replace all the yesNoPerOption questions in DRAFT. You can specify up to 10 yesNoPerOption questions. If not specified, the yesNoPerOption questions are not changed. To remove all the yesNoPerOption questions, specify an empty array. </p>
            choose_one: <p>An array of questions that Elemental Inference answers by choosing one of their options, to replace all the chooseOne questions in DRAFT. You can specify up to 10 chooseOne questions. If not specified, the chooseOne questions are not changed. To remove all the chooseOne questions, specify an empty array. </p>
            name: <p>A new name for the question set. If not specified, the name is not changed.</p>

        Raises:
            capo_elementalinference.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_elementalinference.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict.</p>
            capo_elementalinference.errors.internal_server_error_exception.InternalServerErrorException: <p>An internal server error occurred. This is a temporary condition and the request can be retried. If the problem persists, contact AWS Support. </p>
            capo_elementalinference.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the action doesn't exist.</p>
            capo_elementalinference.errors.too_many_request_exception.TooManyRequestException: <p>The request was denied due to request throttling. Too many requests have been made within a given time period. Reduce the frequency of requests and use exponential backoff when retrying. </p>
            capo_elementalinference.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service. Check the error message for details about which parameter or field is invalid and correct the request before retrying. </p>
            capo_elementalinference.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_elementalinference.types.update_question_set_request.UpdateQuestionSetRequest]",
        ) -> AsyncOperationResponse[
            "capo_elementalinference.types.update_question_set_response.UpdateQuestionSetResponse"
        ]:
            import capo_elementalinference._operations.elemental_inference.update_question_set

            (
                output,
                http_response,
            ) = await capo_elementalinference._operations.elemental_inference.update_question_set.async_update_question_set(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("UpdateQuestionSet")
        )
        input_: capo_elementalinference.types.update_question_set_request.UpdateQuestionSetRequest = {
            "id": id
        }
        if yes_no is not None:
            input_["yes_no"] = yes_no
        if yes_no_per_option is not None:
            input_["yes_no_per_option"] = yes_no_per_option
        if choose_one is not None:
            input_["choose_one"] = choose_one
        if name is not None:
            input_["name"] = name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete(
        self,
        id: "capo_elementalinference.types.question_set_id.QuestionSetId",
        *,
        config_overrides: Optional[AsyncElementalInferenceClientConfig] = None,
    ) -> "capo_elementalinference.types.delete_question_set_response.DeleteQuestionSetResponse":
        """<p>Deletes the specified question set, including its DRAFT version and all its published versions. You can't delete a question set while any feed references any of its versions, including an archived feed. You must first remove the question set from the customQuestions configuration of each feed output that references it, or delete those feeds. </p>

        Args:
            id: <p>The ID of the question set to delete.</p>

        Raises:
            capo_elementalinference.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_elementalinference.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict.</p>
            capo_elementalinference.errors.internal_server_error_exception.InternalServerErrorException: <p>An internal server error occurred. This is a temporary condition and the request can be retried. If the problem persists, contact AWS Support. </p>
            capo_elementalinference.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the action doesn't exist.</p>
            capo_elementalinference.errors.too_many_request_exception.TooManyRequestException: <p>The request was denied due to request throttling. Too many requests have been made within a given time period. Reduce the frequency of requests and use exponential backoff when retrying. </p>
            capo_elementalinference.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service. Check the error message for details about which parameter or field is invalid and correct the request before retrying. </p>
            capo_elementalinference.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_elementalinference.types.delete_question_set_request.DeleteQuestionSetRequest]",
        ) -> AsyncOperationResponse[
            "capo_elementalinference.types.delete_question_set_response.DeleteQuestionSetResponse"
        ]:
            import capo_elementalinference._operations.elemental_inference.delete_question_set

            (
                output,
                http_response,
            ) = await capo_elementalinference._operations.elemental_inference.delete_question_set.async_delete_question_set(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteQuestionSet")
        )
        input_: capo_elementalinference.types.delete_question_set_request.DeleteQuestionSetRequest = {
            "id": id
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
        config_overrides: Optional[AsyncElementalInferenceClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
    ) -> "capo_elementalinference.types.list_question_sets_response.ListQuestionSetsResponse":
        """<p>Lists the question sets in your account. The response doesn't include the questions in each question set. To retrieve them, use GetQuestionSet. </p>

        Args:
            max_results: <p>The maximum number of results to return per API request. Valid range: 1 to 100.</p>
            next_token: <p>The token that identifies the next batch of results to return.</p>

        Raises:
            capo_elementalinference.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_elementalinference.errors.internal_server_error_exception.InternalServerErrorException: <p>An internal server error occurred. This is a temporary condition and the request can be retried. If the problem persists, contact AWS Support. </p>
            capo_elementalinference.errors.too_many_request_exception.TooManyRequestException: <p>The request was denied due to request throttling. Too many requests have been made within a given time period. Reduce the frequency of requests and use exponential backoff when retrying. </p>
            capo_elementalinference.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service. Check the error message for details about which parameter or field is invalid and correct the request before retrying. </p>
            capo_elementalinference.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_elementalinference.types.list_question_sets_request.ListQuestionSetsRequest]",
        ) -> AsyncOperationResponse[
            "capo_elementalinference.types.list_question_sets_response.ListQuestionSetsResponse"
        ]:
            import capo_elementalinference._operations.elemental_inference.list_question_sets

            (
                output,
                http_response,
            ) = await capo_elementalinference._operations.elemental_inference.list_question_sets.async_list_question_sets(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListQuestionSets")
        )
        input_: capo_elementalinference.types.list_question_sets_request.ListQuestionSetsRequest = {}
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

    async def create_question_set_version(
        self,
        id: "capo_elementalinference.types.question_set_id.QuestionSetId",
        *,
        config_overrides: Optional[AsyncElementalInferenceClientConfig] = None,
        sha256: Optional[
            "capo_elementalinference.types.question_set_sha256.QuestionSetSha256"
        ] = None,
        description: Optional[
            "capo_elementalinference.types.question_set_version_description.QuestionSetVersionDescription"
        ] = None,
    ) -> "capo_elementalinference.types.create_question_set_version_response.CreateQuestionSetVersionResponse":
        """<p>Publishes the DRAFT version of the specified question set as a new version. The new version has the same name and questions as DRAFT, and you can't change it. DRAFT doesn't change, so you can continue to update it. </p> <p>Version numbers start at 1, and each new version has the next number. Elemental Inference never reuses a version number, even after you delete that version. </p> <p>If DRAFT hasn't changed since the latest published version, Elemental Inference doesn't create a version. Instead, it returns the latest version. A change to the name of the question set counts as a change to DRAFT. </p> <p>A question set can have a limited number of versions. If the question set already has the maximum number of versions, Elemental Inference returns ServiceQuotaExceededException. To free space for a new version, delete a version that you no longer need, or create a new question set. </p>

        Args:
            id: <p>The ID of the question set whose DRAFT version you want to publish.</p>
            sha256: <p>The SHA-256 hash of the DRAFT version that you want to publish, as returned by GetQuestionSet or UpdateQuestionSet. If you specify this value, Elemental Inference publishes DRAFT only if its current hash matches. If it doesn't match, because DRAFT changed after you retrieved it, the request fails with ConflictException. </p> <p>If you don't specify this value, Elemental Inference publishes DRAFT as it is when it receives the request. </p>
            description: <p>A description of the new version. You can't change the description after Elemental Inference publishes the version. If DRAFT hasn't changed since the latest version, Elemental Inference ignores this value and returns the latest version with its existing description. </p> <p>The description can be up to 256 characters. It can contain the letters A-Z and a-z, the digits 0-9, underscores, spaces, and the following characters: <code>- . ' , @ : ;</code>. </p>

        Raises:
            capo_elementalinference.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_elementalinference.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict.</p>
            capo_elementalinference.errors.internal_server_error_exception.InternalServerErrorException: <p>An internal server error occurred. This is a temporary condition and the request can be retried. If the problem persists, contact AWS Support. </p>
            capo_elementalinference.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the action doesn't exist.</p>
            capo_elementalinference.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request was rejected because it would exceed one or more service quotas for your account. Review your service quotas and either delete unused resources or request a quota increase. </p>
            capo_elementalinference.errors.too_many_request_exception.TooManyRequestException: <p>The request was denied due to request throttling. Too many requests have been made within a given time period. Reduce the frequency of requests and use exponential backoff when retrying. </p>
            capo_elementalinference.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service. Check the error message for details about which parameter or field is invalid and correct the request before retrying. </p>
            capo_elementalinference.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_elementalinference.types.create_question_set_version_request.CreateQuestionSetVersionRequest]",
        ) -> AsyncOperationResponse[
            "capo_elementalinference.types.create_question_set_version_response.CreateQuestionSetVersionResponse"
        ]:
            import capo_elementalinference._operations.elemental_inference.create_question_set_version

            (
                output,
                http_response,
            ) = await capo_elementalinference._operations.elemental_inference.create_question_set_version.async_create_question_set_version(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("CreateQuestionSetVersion")
        )
        input_: capo_elementalinference.types.create_question_set_version_request.CreateQuestionSetVersionRequest = {
            "id": id
        }
        if sha256 is not None:
            input_["sha256"] = sha256
        if description is not None:
            input_["description"] = description

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_question_set_version(
        self,
        id: "capo_elementalinference.types.question_set_id.QuestionSetId",
        question_set_version: "capo_elementalinference.types.published_question_set_version.PublishedQuestionSetVersion",
        *,
        config_overrides: Optional[AsyncElementalInferenceClientConfig] = None,
    ) -> "capo_elementalinference.types.delete_question_set_version_response.DeleteQuestionSetVersionResponse":
        """<p>Deletes a published version of the specified question set. You can't delete a version while a feed references it, including an archived feed. You can't restore a deleted version, and Elemental Inference doesn't reuse its number. </p> <p>You can't delete the DRAFT version on its own. To delete DRAFT, delete the question set by using DeleteQuestionSet. </p> <p>Deleting a version doesn't change the latestVersion of the question set, even if you delete the highest version. </p>

        Args:
            id: <p>The ID of the question set that contains the version.</p>
            question_set_version: <p>The number of the published version to delete. You can't specify DRAFT.</p>

        Raises:
            capo_elementalinference.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_elementalinference.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict.</p>
            capo_elementalinference.errors.internal_server_error_exception.InternalServerErrorException: <p>An internal server error occurred. This is a temporary condition and the request can be retried. If the problem persists, contact AWS Support. </p>
            capo_elementalinference.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the action doesn't exist.</p>
            capo_elementalinference.errors.too_many_request_exception.TooManyRequestException: <p>The request was denied due to request throttling. Too many requests have been made within a given time period. Reduce the frequency of requests and use exponential backoff when retrying. </p>
            capo_elementalinference.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service. Check the error message for details about which parameter or field is invalid and correct the request before retrying. </p>
            capo_elementalinference.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_elementalinference.types.delete_question_set_version_request.DeleteQuestionSetVersionRequest]",
        ) -> AsyncOperationResponse[
            "capo_elementalinference.types.delete_question_set_version_response.DeleteQuestionSetVersionResponse"
        ]:
            import capo_elementalinference._operations.elemental_inference.delete_question_set_version

            (
                output,
                http_response,
            ) = await capo_elementalinference._operations.elemental_inference.delete_question_set_version.async_delete_question_set_version(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteQuestionSetVersion")
        )
        input_: capo_elementalinference.types.delete_question_set_version_request.DeleteQuestionSetVersionRequest = {
            "id": id,
            "question_set_version": question_set_version,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_question_set_versions(
        self,
        id: "capo_elementalinference.types.question_set_id.QuestionSetId",
        *,
        config_overrides: Optional[AsyncElementalInferenceClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
    ) -> "capo_elementalinference.types.list_question_set_versions_response.ListQuestionSetVersionsResponse":
        """<p>Lists the versions of the specified question set. The list starts with the DRAFT version, followed by the published versions from the highest version number to the lowest. The list doesn't include deleted versions. </p> <p>The response doesn't include the questions in each version. To retrieve them, use GetQuestionSet and specify questionSetVersion. </p>

        Args:
            id: <p>The ID of the question set whose versions you want to list.</p>
            max_results: <p>The maximum number of results to return per API request. Valid range: 1 to 100.</p>
            next_token: <p>The token that identifies the next batch of results to return.</p>

        Raises:
            capo_elementalinference.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_elementalinference.errors.internal_server_error_exception.InternalServerErrorException: <p>An internal server error occurred. This is a temporary condition and the request can be retried. If the problem persists, contact AWS Support. </p>
            capo_elementalinference.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the action doesn't exist.</p>
            capo_elementalinference.errors.too_many_request_exception.TooManyRequestException: <p>The request was denied due to request throttling. Too many requests have been made within a given time period. Reduce the frequency of requests and use exponential backoff when retrying. </p>
            capo_elementalinference.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service. Check the error message for details about which parameter or field is invalid and correct the request before retrying. </p>
            capo_elementalinference.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_elementalinference.types.list_question_set_versions_request.ListQuestionSetVersionsRequest]",
        ) -> AsyncOperationResponse[
            "capo_elementalinference.types.list_question_set_versions_response.ListQuestionSetVersionsResponse"
        ]:
            import capo_elementalinference._operations.elemental_inference.list_question_set_versions

            (
                output,
                http_response,
            ) = await capo_elementalinference._operations.elemental_inference.list_question_set_versions.async_list_question_set_versions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListQuestionSetVersions")
        )
        input_: capo_elementalinference.types.list_question_set_versions_request.ListQuestionSetVersionsRequest = {
            "id": id
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
