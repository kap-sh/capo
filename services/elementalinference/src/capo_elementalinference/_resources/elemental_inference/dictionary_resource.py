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
    import capo_elementalinference.types.create_dictionary_request
    import capo_elementalinference.types.create_dictionary_response
    import capo_elementalinference.types.delete_dictionary_request
    import capo_elementalinference.types.delete_dictionary_response
    import capo_elementalinference.types.dictionary_entries_payload
    import capo_elementalinference.types.dictionary_id
    import capo_elementalinference.types.dictionary_language
    import capo_elementalinference.types.dictionary_summary
    import capo_elementalinference.types.export_dictionary_entries_request
    import capo_elementalinference.types.export_dictionary_entries_response
    import capo_elementalinference.types.get_dictionary_request
    import capo_elementalinference.types.get_dictionary_response
    import capo_elementalinference.types.list_dictionaries_request
    import capo_elementalinference.types.list_dictionaries_response
    import capo_elementalinference.types.resource_name
    import capo_elementalinference.types.tag_map
    import capo_elementalinference.types.update_dictionary_request
    import capo_elementalinference.types.update_dictionary_response
    from capo_elementalinference._services.async_elemental_inference import (
        AsyncElementalInferenceClient,
        AsyncElementalInferenceClientConfig,
    )
    from capo_elementalinference._services.elemental_inference import (
        ElementalInferenceClient,
        ElementalInferenceClientConfig,
    )


class DictionaryResource:
    def __init__(self, service: ElementalInferenceClient) -> None:
        self._service = service

    def create(
        self,
        name: "capo_elementalinference.types.resource_name.ResourceName",
        language: "capo_elementalinference.types.dictionary_language.DictionaryLanguage",
        *,
        config_overrides: Optional[ElementalInferenceClientConfig] = None,
        entries: Optional[
            "capo_elementalinference.types.dictionary_entries_payload.DictionaryEntriesPayload"
        ] = None,
        tags: Optional["capo_elementalinference.types.tag_map.TagMap"] = None,
    ) -> "capo_elementalinference.types.create_dictionary_response.CreateDictionaryResponse":
        """<p>Creates a custom dictionary for improving transcription accuracy. A dictionary contains custom words and phrases that the ASR engine might not recognize, such as brand names, technical terms, or proper nouns. You can reference a dictionary when configuring a smart subtitles output. </p>

        Args:
            name: <p>A user-friendly name for this dictionary.</p>
            language: <p>The language of the dictionary entries. Specify the language using an ISO 639-2/T three-letter code. Supported values: eng, fra, ita, deu, spa, por. </p>
            entries: <p>The dictionary entries payload. Contains the custom words and phrases for the dictionary. Maximum size is 40,960 characters. </p>
            tags: <p>Optional tags to associate with the dictionary.</p>

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
            req: "OperationRequest[capo_elementalinference.types.create_dictionary_request.CreateDictionaryRequest]",
        ) -> OperationResponse[
            "capo_elementalinference.types.create_dictionary_response.CreateDictionaryResponse"
        ]:
            import capo_elementalinference._operations.elemental_inference.create_dictionary

            output, http_response = (
                capo_elementalinference._operations.elemental_inference.create_dictionary.create_dictionary(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("CreateDictionary")
        )
        input_: capo_elementalinference.types.create_dictionary_request.CreateDictionaryRequest = {
            "name": name,
            "language": language,
        }
        if entries is not None:
            input_["entries"] = entries
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
        id: "capo_elementalinference.types.dictionary_id.DictionaryId",
        *,
        config_overrides: Optional[ElementalInferenceClientConfig] = None,
    ) -> "capo_elementalinference.types.get_dictionary_response.GetDictionaryResponse":
        """<p>Retrieves information about the specified dictionary.</p>

        Args:
            id: <p>The ID of the dictionary to retrieve.</p>

        Raises:
            capo_elementalinference.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_elementalinference.errors.internal_server_error_exception.InternalServerErrorException: <p>An internal server error occurred. This is a temporary condition and the request can be retried. If the problem persists, contact AWS Support. </p>
            capo_elementalinference.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the action doesn't exist.</p>
            capo_elementalinference.errors.too_many_request_exception.TooManyRequestException: <p>The request was denied due to request throttling. Too many requests have been made within a given time period. Reduce the frequency of requests and use exponential backoff when retrying. </p>
            capo_elementalinference.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service. Check the error message for details about which parameter or field is invalid and correct the request before retrying. </p>
            capo_elementalinference.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_elementalinference.types.get_dictionary_request.GetDictionaryRequest]",
        ) -> OperationResponse[
            "capo_elementalinference.types.get_dictionary_response.GetDictionaryResponse"
        ]:
            import capo_elementalinference._operations.elemental_inference.get_dictionary

            output, http_response = (
                capo_elementalinference._operations.elemental_inference.get_dictionary.get_dictionary(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetDictionary")
        )
        input_: capo_elementalinference.types.get_dictionary_request.GetDictionaryRequest = {
            "id": id
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
        id: "capo_elementalinference.types.dictionary_id.DictionaryId",
        *,
        config_overrides: Optional[ElementalInferenceClientConfig] = None,
        name: Optional[
            "capo_elementalinference.types.resource_name.ResourceName"
        ] = None,
        language: Optional[
            "capo_elementalinference.types.dictionary_language.DictionaryLanguage"
        ] = None,
        entries: Optional[
            "capo_elementalinference.types.dictionary_entries_payload.DictionaryEntriesPayload"
        ] = None,
    ) -> "capo_elementalinference.types.update_dictionary_response.UpdateDictionaryResponse":
        """<p>Updates the specified dictionary.</p>

        Args:
            id: <p>The ID of the dictionary to update.</p>
            name: <p>A new name for the dictionary. If not specified, the name is not changed.</p>
            language: <p>A new language for the dictionary. If not specified, the language is not changed.</p>
            entries: <p>New dictionary entries. If not specified, the entries are not changed.</p>

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
            req: "OperationRequest[capo_elementalinference.types.update_dictionary_request.UpdateDictionaryRequest]",
        ) -> OperationResponse[
            "capo_elementalinference.types.update_dictionary_response.UpdateDictionaryResponse"
        ]:
            import capo_elementalinference._operations.elemental_inference.update_dictionary

            output, http_response = (
                capo_elementalinference._operations.elemental_inference.update_dictionary.update_dictionary(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("UpdateDictionary")
        )
        input_: capo_elementalinference.types.update_dictionary_request.UpdateDictionaryRequest = {
            "id": id
        }
        if name is not None:
            input_["name"] = name
        if language is not None:
            input_["language"] = language
        if entries is not None:
            input_["entries"] = entries

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete(
        self,
        id: "capo_elementalinference.types.dictionary_id.DictionaryId",
        *,
        config_overrides: Optional[ElementalInferenceClientConfig] = None,
    ) -> "capo_elementalinference.types.delete_dictionary_response.DeleteDictionaryResponse":
        """<p>Deletes the specified dictionary. You cannot delete a dictionary that is referenced by a feed. You must first remove the dictionary reference from the feed's subtitling configuration. </p>

        Args:
            id: <p>The ID of the dictionary to delete.</p>

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
            req: "OperationRequest[capo_elementalinference.types.delete_dictionary_request.DeleteDictionaryRequest]",
        ) -> OperationResponse[
            "capo_elementalinference.types.delete_dictionary_response.DeleteDictionaryResponse"
        ]:
            import capo_elementalinference._operations.elemental_inference.delete_dictionary

            output, http_response = (
                capo_elementalinference._operations.elemental_inference.delete_dictionary.delete_dictionary(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteDictionary")
        )
        input_: capo_elementalinference.types.delete_dictionary_request.DeleteDictionaryRequest = {
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
    ) -> "capo_elementalinference.types.list_dictionaries_response.ListDictionariesResponse":
        """<p>Lists the dictionaries in your account.</p>

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
            req: "OperationRequest[capo_elementalinference.types.list_dictionaries_request.ListDictionariesRequest]",
        ) -> OperationResponse[
            "capo_elementalinference.types.list_dictionaries_response.ListDictionariesResponse"
        ]:
            import capo_elementalinference._operations.elemental_inference.list_dictionaries

            output, http_response = (
                capo_elementalinference._operations.elemental_inference.list_dictionaries.list_dictionaries(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListDictionaries")
        )
        input_: capo_elementalinference.types.list_dictionaries_request.ListDictionariesRequest = {}
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

    def export_dictionary_entries(
        self,
        id: "capo_elementalinference.types.dictionary_id.DictionaryId",
        *,
        config_overrides: Optional[ElementalInferenceClientConfig] = None,
    ) -> "capo_elementalinference.types.export_dictionary_entries_response.ExportDictionaryEntriesResponse":
        """<p>Exports the entries from the specified dictionary.</p>

        Args:
            id: <p>The ID of the dictionary whose entries you want to export.</p>

        Raises:
            capo_elementalinference.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_elementalinference.errors.internal_server_error_exception.InternalServerErrorException: <p>An internal server error occurred. This is a temporary condition and the request can be retried. If the problem persists, contact AWS Support. </p>
            capo_elementalinference.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the action doesn't exist.</p>
            capo_elementalinference.errors.too_many_request_exception.TooManyRequestException: <p>The request was denied due to request throttling. Too many requests have been made within a given time period. Reduce the frequency of requests and use exponential backoff when retrying. </p>
            capo_elementalinference.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service. Check the error message for details about which parameter or field is invalid and correct the request before retrying. </p>
            capo_elementalinference.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_elementalinference.types.export_dictionary_entries_request.ExportDictionaryEntriesRequest]",
        ) -> OperationResponse[
            "capo_elementalinference.types.export_dictionary_entries_response.ExportDictionaryEntriesResponse"
        ]:
            import capo_elementalinference._operations.elemental_inference.export_dictionary_entries

            output, http_response = (
                capo_elementalinference._operations.elemental_inference.export_dictionary_entries.export_dictionary_entries(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ExportDictionaryEntries")
        )
        input_: capo_elementalinference.types.export_dictionary_entries_request.ExportDictionaryEntriesRequest = {
            "id": id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncDictionaryResource:
    def __init__(self, service: AsyncElementalInferenceClient) -> None:
        self._service = service

    async def create(
        self,
        name: "capo_elementalinference.types.resource_name.ResourceName",
        language: "capo_elementalinference.types.dictionary_language.DictionaryLanguage",
        *,
        config_overrides: Optional[AsyncElementalInferenceClientConfig] = None,
        entries: Optional[
            "capo_elementalinference.types.dictionary_entries_payload.DictionaryEntriesPayload"
        ] = None,
        tags: Optional["capo_elementalinference.types.tag_map.TagMap"] = None,
    ) -> "capo_elementalinference.types.create_dictionary_response.CreateDictionaryResponse":
        """<p>Creates a custom dictionary for improving transcription accuracy. A dictionary contains custom words and phrases that the ASR engine might not recognize, such as brand names, technical terms, or proper nouns. You can reference a dictionary when configuring a smart subtitles output. </p>

        Args:
            name: <p>A user-friendly name for this dictionary.</p>
            language: <p>The language of the dictionary entries. Specify the language using an ISO 639-2/T three-letter code. Supported values: eng, fra, ita, deu, spa, por. </p>
            entries: <p>The dictionary entries payload. Contains the custom words and phrases for the dictionary. Maximum size is 40,960 characters. </p>
            tags: <p>Optional tags to associate with the dictionary.</p>

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
            req: "AsyncOperationRequest[capo_elementalinference.types.create_dictionary_request.CreateDictionaryRequest]",
        ) -> AsyncOperationResponse[
            "capo_elementalinference.types.create_dictionary_response.CreateDictionaryResponse"
        ]:
            import capo_elementalinference._operations.elemental_inference.create_dictionary

            (
                output,
                http_response,
            ) = await capo_elementalinference._operations.elemental_inference.create_dictionary.async_create_dictionary(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("CreateDictionary")
        )
        input_: capo_elementalinference.types.create_dictionary_request.CreateDictionaryRequest = {
            "name": name,
            "language": language,
        }
        if entries is not None:
            input_["entries"] = entries
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
        id: "capo_elementalinference.types.dictionary_id.DictionaryId",
        *,
        config_overrides: Optional[AsyncElementalInferenceClientConfig] = None,
    ) -> "capo_elementalinference.types.get_dictionary_response.GetDictionaryResponse":
        """<p>Retrieves information about the specified dictionary.</p>

        Args:
            id: <p>The ID of the dictionary to retrieve.</p>

        Raises:
            capo_elementalinference.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_elementalinference.errors.internal_server_error_exception.InternalServerErrorException: <p>An internal server error occurred. This is a temporary condition and the request can be retried. If the problem persists, contact AWS Support. </p>
            capo_elementalinference.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the action doesn't exist.</p>
            capo_elementalinference.errors.too_many_request_exception.TooManyRequestException: <p>The request was denied due to request throttling. Too many requests have been made within a given time period. Reduce the frequency of requests and use exponential backoff when retrying. </p>
            capo_elementalinference.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service. Check the error message for details about which parameter or field is invalid and correct the request before retrying. </p>
            capo_elementalinference.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_elementalinference.types.get_dictionary_request.GetDictionaryRequest]",
        ) -> AsyncOperationResponse[
            "capo_elementalinference.types.get_dictionary_response.GetDictionaryResponse"
        ]:
            import capo_elementalinference._operations.elemental_inference.get_dictionary

            (
                output,
                http_response,
            ) = await capo_elementalinference._operations.elemental_inference.get_dictionary.async_get_dictionary(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetDictionary")
        )
        input_: capo_elementalinference.types.get_dictionary_request.GetDictionaryRequest = {
            "id": id
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
        id: "capo_elementalinference.types.dictionary_id.DictionaryId",
        *,
        config_overrides: Optional[AsyncElementalInferenceClientConfig] = None,
        name: Optional[
            "capo_elementalinference.types.resource_name.ResourceName"
        ] = None,
        language: Optional[
            "capo_elementalinference.types.dictionary_language.DictionaryLanguage"
        ] = None,
        entries: Optional[
            "capo_elementalinference.types.dictionary_entries_payload.DictionaryEntriesPayload"
        ] = None,
    ) -> "capo_elementalinference.types.update_dictionary_response.UpdateDictionaryResponse":
        """<p>Updates the specified dictionary.</p>

        Args:
            id: <p>The ID of the dictionary to update.</p>
            name: <p>A new name for the dictionary. If not specified, the name is not changed.</p>
            language: <p>A new language for the dictionary. If not specified, the language is not changed.</p>
            entries: <p>New dictionary entries. If not specified, the entries are not changed.</p>

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
            req: "AsyncOperationRequest[capo_elementalinference.types.update_dictionary_request.UpdateDictionaryRequest]",
        ) -> AsyncOperationResponse[
            "capo_elementalinference.types.update_dictionary_response.UpdateDictionaryResponse"
        ]:
            import capo_elementalinference._operations.elemental_inference.update_dictionary

            (
                output,
                http_response,
            ) = await capo_elementalinference._operations.elemental_inference.update_dictionary.async_update_dictionary(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("UpdateDictionary")
        )
        input_: capo_elementalinference.types.update_dictionary_request.UpdateDictionaryRequest = {
            "id": id
        }
        if name is not None:
            input_["name"] = name
        if language is not None:
            input_["language"] = language
        if entries is not None:
            input_["entries"] = entries

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete(
        self,
        id: "capo_elementalinference.types.dictionary_id.DictionaryId",
        *,
        config_overrides: Optional[AsyncElementalInferenceClientConfig] = None,
    ) -> "capo_elementalinference.types.delete_dictionary_response.DeleteDictionaryResponse":
        """<p>Deletes the specified dictionary. You cannot delete a dictionary that is referenced by a feed. You must first remove the dictionary reference from the feed's subtitling configuration. </p>

        Args:
            id: <p>The ID of the dictionary to delete.</p>

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
            req: "AsyncOperationRequest[capo_elementalinference.types.delete_dictionary_request.DeleteDictionaryRequest]",
        ) -> AsyncOperationResponse[
            "capo_elementalinference.types.delete_dictionary_response.DeleteDictionaryResponse"
        ]:
            import capo_elementalinference._operations.elemental_inference.delete_dictionary

            (
                output,
                http_response,
            ) = await capo_elementalinference._operations.elemental_inference.delete_dictionary.async_delete_dictionary(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteDictionary")
        )
        input_: capo_elementalinference.types.delete_dictionary_request.DeleteDictionaryRequest = {
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
    ) -> "capo_elementalinference.types.list_dictionaries_response.ListDictionariesResponse":
        """<p>Lists the dictionaries in your account.</p>

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
            req: "AsyncOperationRequest[capo_elementalinference.types.list_dictionaries_request.ListDictionariesRequest]",
        ) -> AsyncOperationResponse[
            "capo_elementalinference.types.list_dictionaries_response.ListDictionariesResponse"
        ]:
            import capo_elementalinference._operations.elemental_inference.list_dictionaries

            (
                output,
                http_response,
            ) = await capo_elementalinference._operations.elemental_inference.list_dictionaries.async_list_dictionaries(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListDictionaries")
        )
        input_: capo_elementalinference.types.list_dictionaries_request.ListDictionariesRequest = {}
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

    async def export_dictionary_entries(
        self,
        id: "capo_elementalinference.types.dictionary_id.DictionaryId",
        *,
        config_overrides: Optional[AsyncElementalInferenceClientConfig] = None,
    ) -> "capo_elementalinference.types.export_dictionary_entries_response.ExportDictionaryEntriesResponse":
        """<p>Exports the entries from the specified dictionary.</p>

        Args:
            id: <p>The ID of the dictionary whose entries you want to export.</p>

        Raises:
            capo_elementalinference.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_elementalinference.errors.internal_server_error_exception.InternalServerErrorException: <p>An internal server error occurred. This is a temporary condition and the request can be retried. If the problem persists, contact AWS Support. </p>
            capo_elementalinference.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the action doesn't exist.</p>
            capo_elementalinference.errors.too_many_request_exception.TooManyRequestException: <p>The request was denied due to request throttling. Too many requests have been made within a given time period. Reduce the frequency of requests and use exponential backoff when retrying. </p>
            capo_elementalinference.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service. Check the error message for details about which parameter or field is invalid and correct the request before retrying. </p>
            capo_elementalinference.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_elementalinference.types.export_dictionary_entries_request.ExportDictionaryEntriesRequest]",
        ) -> AsyncOperationResponse[
            "capo_elementalinference.types.export_dictionary_entries_response.ExportDictionaryEntriesResponse"
        ]:
            import capo_elementalinference._operations.elemental_inference.export_dictionary_entries

            (
                output,
                http_response,
            ) = await capo_elementalinference._operations.elemental_inference.export_dictionary_entries.async_export_dictionary_entries(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ExportDictionaryEntries")
        )
        input_: capo_elementalinference.types.export_dictionary_entries_request.ExportDictionaryEntriesRequest = {
            "id": id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
