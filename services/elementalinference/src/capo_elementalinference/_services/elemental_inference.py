"""Generated from Smithy shape ``com.amazonaws.elementalinference#ElementalInference``."""

import warnings
from collections.abc import Iterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import BaseHandler, Client

import capo_elementalinference._auth._signers
import capo_elementalinference._auth._sigv4
from capo_elementalinference._auth._identity import Credentials
from capo_elementalinference._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_elementalinference._auth._zapros_handler import AuthMiddleware
from capo_elementalinference._pagination import resolve_path as _resolve_path
from capo_elementalinference._resources.elemental_inference.dictionary_resource import (
    DictionaryResource,
)
from capo_elementalinference._resources.elemental_inference.feed_resource import (
    FeedResource,
)
from capo_elementalinference._services._aws_config import aws_config
from capo_elementalinference._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import capo_elementalinference.types.associate_feed_request
    import capo_elementalinference.types.associate_feed_response
    import capo_elementalinference.types.associated_resource_name
    import capo_elementalinference.types.create_dictionary_request
    import capo_elementalinference.types.create_dictionary_response
    import capo_elementalinference.types.create_feed_request
    import capo_elementalinference.types.create_feed_response
    import capo_elementalinference.types.create_output_list
    import capo_elementalinference.types.delete_dictionary_request
    import capo_elementalinference.types.delete_dictionary_response
    import capo_elementalinference.types.delete_feed_request
    import capo_elementalinference.types.delete_feed_response
    import capo_elementalinference.types.dictionary_entries_payload
    import capo_elementalinference.types.dictionary_id
    import capo_elementalinference.types.dictionary_language
    import capo_elementalinference.types.dictionary_summary
    import capo_elementalinference.types.disassociate_feed_request
    import capo_elementalinference.types.disassociate_feed_response
    import capo_elementalinference.types.export_dictionary_entries_request
    import capo_elementalinference.types.export_dictionary_entries_response
    import capo_elementalinference.types.feed_id
    import capo_elementalinference.types.feed_summary
    import capo_elementalinference.types.get_dictionary_request
    import capo_elementalinference.types.get_dictionary_response
    import capo_elementalinference.types.get_feed_request
    import capo_elementalinference.types.get_feed_response
    import capo_elementalinference.types.list_dictionaries_request
    import capo_elementalinference.types.list_dictionaries_response
    import capo_elementalinference.types.list_feeds_request
    import capo_elementalinference.types.list_feeds_response
    import capo_elementalinference.types.list_tags_for_resource_request
    import capo_elementalinference.types.list_tags_for_resource_response
    import capo_elementalinference.types.resource_arn
    import capo_elementalinference.types.resource_name
    import capo_elementalinference.types.tag_key_list
    import capo_elementalinference.types.tag_map
    import capo_elementalinference.types.tag_resource_request
    import capo_elementalinference.types.untag_resource_request
    import capo_elementalinference.types.update_dictionary_request
    import capo_elementalinference.types.update_dictionary_response
    import capo_elementalinference.types.update_feed_request
    import capo_elementalinference.types.update_feed_response
    import capo_elementalinference.types.update_output_list


class ElementalInferenceClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class ElementalInferenceClient:
    """A client for the ``ElementalInference`` service.

    Args:
        http_handler: HTTP handler for sending requests. If not provided, creates a default handler.
        operation_interceptors: Interceptors that wrap every operation call. If not provided, defaults to an empty list.
        retry_max_attempts: Maximum number of times to retry a failed operation. Defaults to 3.
        region: The value of the ``AWS::Region`` endpoint parameter.
        use_dual_stack: The value of the ``AWS::UseDualStack`` endpoint parameter.
        use_fips: The value of the ``AWS::UseFIPS`` endpoint parameter.
        endpoint: The value of the ``SDK::Endpoint`` endpoint parameter.
        credentials: AWS credentials for request signing.
        credentials_provider: Provider that resolves AWS credentials. Takes precedence over ``credentials``.
    """

    def __init__(
        self,
        http_handler: BaseHandler | None = None,
        operation_interceptors: Iterable[Interceptor[Any, Any]] | None = None,
        retry_max_attempts: int | None = None,
        region: str | None = None,
        use_dual_stack: bool | None = None,
        use_fips: bool | None = None,
        endpoint: str | None = None,
        credentials: Credentials | None = None,
        credentials_provider: CredentialsProvider | None = None,
    ):
        self._client = Client(http_handler).wrap_with_middleware(
            lambda next: AuthMiddleware(next)
        )
        if credentials is not None and credentials_provider is not None:
            warnings.warn(
                "Both credentials and credentials_provider given; provider takes precedence"
            )
        resolved_credentials_provider: IdentityProvider[Credentials] | None = (
            credentials_provider
        )
        if resolved_credentials_provider is None and credentials is not None:
            resolved_credentials_provider = StaticAwsCredentialsProvider(credentials)
        if resolved_credentials_provider is None and credentials is None:
            resolved_credentials_provider = default_aws_credentials_chain(
                Client(http_handler)
            )
        self._config = ElementalInferenceClientConfig(
            {
                "operation_interceptors": operation_interceptors or [],
                "retry_max_attempts": retry_max_attempts,
                "region": region,
                "use_dual_stack": use_dual_stack,
                "use_fips": use_fips,
                "endpoint": endpoint,
                "credentials_provider": resolved_credentials_provider,
            }
        )

        # resources
        self.dictionary_resource = DictionaryResource(self)
        self.feed_resource = FeedResource(self)

    def operation_options(
        self, config_overrides: Optional[ElementalInferenceClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: ElementalInferenceClientConfig = config_overrides or {}
        interceptors_: list[Interceptor[Any, Any]] = [
            *overrides.get(
                "operation_interceptors", self._config.get("operation_interceptors", [])
            ),
            aws_config(),
            retry(),
        ]
        options_: OperationOptions = OperationOptions(
            client=self._client,
            retry_max_attempts=overrides.get(
                "retry_max_attempts", self._config.get("retry_max_attempts")
            ),
            region=overrides.get("region", self._config.get("region")),
            use_dual_stack=overrides.get(
                "use_dual_stack", self._config.get("use_dual_stack")
            ),
            use_fips=overrides.get("use_fips", self._config.get("use_fips")),
            endpoint=overrides.get("endpoint", self._config.get("endpoint")),
            credentials_provider=overrides.get(
                "credentials_provider", self._config.get("credentials_provider")
            ),
        )
        return interceptors_, options_

    def list_tags_for_resource(
        self,
        resource_arn: "capo_elementalinference.types.resource_arn.ResourceArn",
        *,
        config_overrides: Optional[ElementalInferenceClientConfig] = None,
    ) -> "capo_elementalinference.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>List all tags that are on an Elemental Inference resource in the current region.</p>

        Args:
            resource_arn: <p>The ARN of the resource whose tags you want to query.</p>

        Raises:
            capo_elementalinference.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_elementalinference.errors.internal_server_error_exception.InternalServerErrorException: <p>An internal server error occurred. This is a temporary condition and the request can be retried. If the problem persists, contact AWS Support. </p>
            capo_elementalinference.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the action doesn't exist.</p>
            capo_elementalinference.errors.too_many_request_exception.TooManyRequestException: <p>The request was denied due to request throttling. Too many requests have been made within a given time period. Reduce the frequency of requests and use exponential backoff when retrying. </p>
            capo_elementalinference.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service. Check the error message for details about which parameter or field is invalid and correct the request before retrying. </p>
            capo_elementalinference.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_elementalinference.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> OperationResponse[
            "capo_elementalinference.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import capo_elementalinference._operations.elemental_inference.list_tags_for_resource

            output, http_response = (
                capo_elementalinference._operations.elemental_inference.list_tags_for_resource.list_tags_for_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elementalinference.types.list_tags_for_resource_request.ListTagsForResourceRequest = {
            "resource_arn": resource_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def tag_resource(
        self,
        resource_arn: "capo_elementalinference.types.resource_arn.ResourceArn",
        tags: "capo_elementalinference.types.tag_map.TagMap",
        *,
        config_overrides: Optional[ElementalInferenceClientConfig] = None,
    ) -> None:
        """<p>Associates the specified tags to the resource identified by the specified resourceArn in the current region. If existing tags on a resource are not specified in the request parameters, they are not changed. When a resource is deleted, the tags associated with that resource are also deleted. </p>

        Args:
            resource_arn: <p>The ARN of the resource where you want to add tags.</p>
            tags: <p>A list of tags to add to the resource.</p>

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
            req: "OperationRequest[capo_elementalinference.types.tag_resource_request.TagResourceRequest]",
        ) -> OperationResponse[None]:
            import capo_elementalinference._operations.elemental_inference.tag_resource

            output, http_response = (
                capo_elementalinference._operations.elemental_inference.tag_resource.tag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elementalinference.types.tag_resource_request.TagResourceRequest = {
            "resource_arn": resource_arn,
            "tags": tags,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def untag_resource(
        self,
        resource_arn: "capo_elementalinference.types.resource_arn.ResourceArn",
        tag_keys: "capo_elementalinference.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[ElementalInferenceClientConfig] = None,
    ) -> None:
        """<p>Deletes specified tags from the specified resource in the current region.</p>

        Args:
            resource_arn: <p>The ARN of the resource where you want to delete one or more tags.</p>
            tag_keys: <p>The keys of the tags to delete.</p>

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
            req: "OperationRequest[capo_elementalinference.types.untag_resource_request.UntagResourceRequest]",
        ) -> OperationResponse[None]:
            import capo_elementalinference._operations.elemental_inference.untag_resource

            output, http_response = (
                capo_elementalinference._operations.elemental_inference.untag_resource.untag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elementalinference.types.untag_resource_request.UntagResourceRequest = {
            "resource_arn": resource_arn,
            "tag_keys": tag_keys,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_dictionary(
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

        interceptors_, options_ = self.operation_options(config_overrides)
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

    def get_dictionary(
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

        interceptors_, options_ = self.operation_options(config_overrides)
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

    def update_dictionary(
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

        interceptors_, options_ = self.operation_options(config_overrides)
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

    def delete_dictionary(
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

        interceptors_, options_ = self.operation_options(config_overrides)
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

    def list_dictionaries(
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

        interceptors_, options_ = self.operation_options(config_overrides)
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

    def iter_list_dictionaries(
        self,
        *,
        config_overrides: Optional[ElementalInferenceClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
    ) -> "Iterator[capo_elementalinference.types.dictionary_summary.DictionarySummary]":
        _token = next_token
        while True:
            _response = self.list_dictionaries(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("dictionaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

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

        interceptors_, options_ = self.operation_options(config_overrides)
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

    def create_feed(
        self,
        name: "capo_elementalinference.types.resource_name.ResourceName",
        outputs: "capo_elementalinference.types.create_output_list.CreateOutputList",
        *,
        config_overrides: Optional[ElementalInferenceClientConfig] = None,
        tags: Optional["capo_elementalinference.types.tag_map.TagMap"] = None,
    ) -> "capo_elementalinference.types.create_feed_response.CreateFeedResponse":
        """<p>Creates a feed. The feed is the target for the live media stream that is being sent by the calling application. An example of a calling application is AWS Elemental MediaLive. </p> <p>The key contents of the feed is an array of outputs. Each output represents an Elemental Inference feature. After you create the feed, you must associate a resource with the feed. At that point, you will have a useable feed: resource - feed - output or outputs. </p>

        Args:
            name: <p>A user-friendly name for this feed.</p>
            outputs: <p>An array of outputs for this feed. Each output represents a specific Elemental Inference feature. For example, there is one output type for the smart crop feature. You must specify at least one output, but you can later add outputs using AssociateFeed, or add, modify, and delete outputs using UpdateFeed. </p>
            tags: <p>Optional tags. You can also add tags later, using TagResource.</p>

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
            req: "OperationRequest[capo_elementalinference.types.create_feed_request.CreateFeedRequest]",
        ) -> OperationResponse[
            "capo_elementalinference.types.create_feed_response.CreateFeedResponse"
        ]:
            import capo_elementalinference._operations.elemental_inference.create_feed

            output, http_response = (
                capo_elementalinference._operations.elemental_inference.create_feed.create_feed(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elementalinference.types.create_feed_request.CreateFeedRequest = {
            "name": name,
            "outputs": outputs,
        }
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_feed(
        self,
        id: "capo_elementalinference.types.feed_id.FeedId",
        *,
        config_overrides: Optional[ElementalInferenceClientConfig] = None,
    ) -> "capo_elementalinference.types.get_feed_response.GetFeedResponse":
        """<p>Retrieves information about the specified feed.</p>

        Args:
            id: <p>The ID of the feed to query.</p>

        Raises:
            capo_elementalinference.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_elementalinference.errors.internal_server_error_exception.InternalServerErrorException: <p>An internal server error occurred. This is a temporary condition and the request can be retried. If the problem persists, contact AWS Support. </p>
            capo_elementalinference.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the action doesn't exist.</p>
            capo_elementalinference.errors.too_many_request_exception.TooManyRequestException: <p>The request was denied due to request throttling. Too many requests have been made within a given time period. Reduce the frequency of requests and use exponential backoff when retrying. </p>
            capo_elementalinference.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_elementalinference.types.get_feed_request.GetFeedRequest]",
        ) -> OperationResponse[
            "capo_elementalinference.types.get_feed_response.GetFeedResponse"
        ]:
            import capo_elementalinference._operations.elemental_inference.get_feed

            output, http_response = (
                capo_elementalinference._operations.elemental_inference.get_feed.get_feed(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elementalinference.types.get_feed_request.GetFeedRequest = {
            "id": id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_feed(
        self,
        name: "capo_elementalinference.types.resource_name.ResourceName",
        id: "capo_elementalinference.types.feed_id.FeedId",
        outputs: "capo_elementalinference.types.update_output_list.UpdateOutputList",
        *,
        config_overrides: Optional[ElementalInferenceClientConfig] = None,
    ) -> "capo_elementalinference.types.update_feed_response.UpdateFeedResponse":
        """<p>Updates the name and/or outputs in a feed. </p> <p>UpdateFeed is a PUT operation, which means that the payload that you specify completely overwrites the existing payload. </p> <p>This means that if you want to touch the array of outputs, you must pass in the full new list. So you must omit outputs you want to delete, and include outputs you want to add or modify. </p> <p>If you want to patch the array of outputs to make selective additions, use AssociateFeed. </p>

        Args:
            name: <p>Required. You can specify the existing name (to leave it unchanged) or a new name. </p>
            id: <p>The ID of the feed to update.</p>
            outputs: <p>Required. You can specify the existing array of outputs (to leave outputs unchanged) or you can specify a new array. </p>

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
            req: "OperationRequest[capo_elementalinference.types.update_feed_request.UpdateFeedRequest]",
        ) -> OperationResponse[
            "capo_elementalinference.types.update_feed_response.UpdateFeedResponse"
        ]:
            import capo_elementalinference._operations.elemental_inference.update_feed

            output, http_response = (
                capo_elementalinference._operations.elemental_inference.update_feed.update_feed(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elementalinference.types.update_feed_request.UpdateFeedRequest = {
            "name": name,
            "id": id,
            "outputs": outputs,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_feed(
        self,
        id: "capo_elementalinference.types.feed_id.FeedId",
        *,
        config_overrides: Optional[ElementalInferenceClientConfig] = None,
    ) -> "capo_elementalinference.types.delete_feed_response.DeleteFeedResponse":
        """<p>Deletes the specified feed. You can delete the feed at any time. Elemental Inference doesn't block you from deleting a feed when the calling application is calling PutMedia or GetMetadata on that feed, although both these calls will start to fail. For more information about managing inactive feeds, see the Elemental Inference User Guide. </p>

        Args:
            id: <p>The ID of the feed.</p>

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
            req: "OperationRequest[capo_elementalinference.types.delete_feed_request.DeleteFeedRequest]",
        ) -> OperationResponse[
            "capo_elementalinference.types.delete_feed_response.DeleteFeedResponse"
        ]:
            import capo_elementalinference._operations.elemental_inference.delete_feed

            output, http_response = (
                capo_elementalinference._operations.elemental_inference.delete_feed.delete_feed(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elementalinference.types.delete_feed_request.DeleteFeedRequest = {
            "id": id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_feeds(
        self,
        *,
        config_overrides: Optional[ElementalInferenceClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
    ) -> "capo_elementalinference.types.list_feeds_response.ListFeedsResponse":
        """<p>Displays a list of feeds that belong to this AWS account.</p>

        Args:
            max_results: <p>The maximum number of results to return per API request.</p> <p>For example, you submit a list request with MaxResults set at 5. Although 20 items match your request, the service returns no more than the first 5 items. (The service also returns a NextToken value that you can use to fetch the next batch of results.) </p> <p>The service might return fewer results than the MaxResults value. If MaxResults is not included in the request, the service defaults to pagination with a maximum of 10 results per page. </p> <p>Valid Range: Minimum value of 1. Maximum value of 1000.</p>
            next_token: <p>The token that identifies the batch of results that you want to see.</p> <p>For example, you submit a ListFeeds request with MaxResults set at 5. The service returns the first batch of results (up to 5) and a NextToken value. To see the next batch of results, you can submit the ListFeeds request a second time and specify the NextToken value. </p>

        Raises:
            capo_elementalinference.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_elementalinference.errors.internal_server_error_exception.InternalServerErrorException: <p>An internal server error occurred. This is a temporary condition and the request can be retried. If the problem persists, contact AWS Support. </p>
            capo_elementalinference.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the action doesn't exist.</p>
            capo_elementalinference.errors.too_many_request_exception.TooManyRequestException: <p>The request was denied due to request throttling. Too many requests have been made within a given time period. Reduce the frequency of requests and use exponential backoff when retrying. </p>
            capo_elementalinference.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service. Check the error message for details about which parameter or field is invalid and correct the request before retrying. </p>
            capo_elementalinference.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_elementalinference.types.list_feeds_request.ListFeedsRequest]",
        ) -> OperationResponse[
            "capo_elementalinference.types.list_feeds_response.ListFeedsResponse"
        ]:
            import capo_elementalinference._operations.elemental_inference.list_feeds

            output, http_response = (
                capo_elementalinference._operations.elemental_inference.list_feeds.list_feeds(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elementalinference.types.list_feeds_request.ListFeedsRequest = {}
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

    def iter_list_feeds(
        self,
        *,
        config_overrides: Optional[ElementalInferenceClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
    ) -> "Iterator[capo_elementalinference.types.feed_summary.FeedSummary]":
        _token = next_token
        while True:
            _response = self.list_feeds(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("feeds",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def associate_feed(
        self,
        id: "capo_elementalinference.types.feed_id.FeedId",
        associated_resource_name: "capo_elementalinference.types.associated_resource_name.AssociatedResourceName",
        outputs: "capo_elementalinference.types.create_output_list.CreateOutputList",
        *,
        config_overrides: Optional[ElementalInferenceClientConfig] = None,
        dry_run: Optional[bool] = None,
    ) -> "capo_elementalinference.types.associate_feed_response.AssociateFeedResponse":
        """<p>Associates a resource with the feed. The resource provides the input that Elemental Inference needs in order to perform an Elemental Inference feature, such as cropping video. You always provide the resource by associating it with a feed. You can associate only one resource with each feed. With an association, a specific source media is claiming ownership of the feed. </p> <p>AssociateFeed is a PATCH operation, which means that you can include only parameters that you want to change. Parameters that you don't include will not be affected by the operation. </p> <p>Specifically:</p> <ul> <li> <p>You can add more outputs to the existing outputs. New outputs will be appended.</p> </li> <li> <p>You can't modify an existing output (for example to change its name). Instead, use UpdateFeed. </p> </li> <li> <p>You can't delete an existing output. Instead, use UpdateFeed.</p> </li> </ul> <p>Also note that you can't change the feed name with AssociateFeed. Instead, use UpdateFeed. </p>

        Args:
            id: <p>The ID of the feed.</p>
            associated_resource_name: <p>An identifier for the resource. This name must not resemble an ARN.</p> <p>The resource is the source media that the feed will process. The name you assign should help you to later identify the source media that belongs to the feed. In this way, you will know which source media to push to the feed (using PutMedia). </p>
            outputs: <p>An array of one or more outputs that you want to add to this feed now, to supplement any outputs that you specified when you created or updated the feed. </p>
            dry_run: <p>Set to true if you want to do a dry run of the associate action.</p> <p>Elemental Inference will validate that the real request would succeed without actually making any changes. A dry run catches errors such as missing IAM permissions, quota limits exceeded, conflicting outputs, and so on. If the dry run fails, the action returns a 4xx error code. After you've fixed the errors, resubmit the request. </p>

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
            req: "OperationRequest[capo_elementalinference.types.associate_feed_request.AssociateFeedRequest]",
        ) -> OperationResponse[
            "capo_elementalinference.types.associate_feed_response.AssociateFeedResponse"
        ]:
            import capo_elementalinference._operations.elemental_inference.associate_feed

            output, http_response = (
                capo_elementalinference._operations.elemental_inference.associate_feed.associate_feed(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elementalinference.types.associate_feed_request.AssociateFeedRequest = {
            "id": id,
            "associated_resource_name": associated_resource_name,
            "outputs": outputs,
        }
        if dry_run is not None:
            input_["dry_run"] = dry_run

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def disassociate_feed(
        self,
        id: "capo_elementalinference.types.feed_id.FeedId",
        associated_resource_name: "capo_elementalinference.types.associated_resource_name.AssociatedResourceName",
        *,
        config_overrides: Optional[ElementalInferenceClientConfig] = None,
        dry_run: Optional[bool] = None,
    ) -> "capo_elementalinference.types.disassociate_feed_response.DisassociateFeedResponse":
        """<p>Releases the resource (the source media) that is associated with this feed. The outputs in the feed become DISABLED. </p>

        Args:
            id: <p>The ID of the feed where you want to release the resource.</p>
            associated_resource_name: <p>The name of the resource currently associated with the feed.</p>
            dry_run: <p>Set to true if you want to do a dry run of the disassociate action.</p> <p>Elemental Inference will validate that the real request would succeed without actually making any changes. A dry run catches errors such as missing IAM permissions. If the dry run fails, the action returns a 4xx error code. </p>

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
            req: "OperationRequest[capo_elementalinference.types.disassociate_feed_request.DisassociateFeedRequest]",
        ) -> OperationResponse[
            "capo_elementalinference.types.disassociate_feed_response.DisassociateFeedResponse"
        ]:
            import capo_elementalinference._operations.elemental_inference.disassociate_feed

            output, http_response = (
                capo_elementalinference._operations.elemental_inference.disassociate_feed.disassociate_feed(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elementalinference.types.disassociate_feed_request.DisassociateFeedRequest = {
            "id": id,
            "associated_resource_name": associated_resource_name,
        }
        if dry_run is not None:
            input_["dry_run"] = dry_run

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def __enter__(self) -> Self:
        return self

    def __exit__(self, exc_type: Any, exc: Any, tb: Any):
        self._client.close()
