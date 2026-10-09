"""Generated from Smithy shape ``com.amazonaws.polly#Parrot_v1``."""

import warnings
from collections.abc import AsyncGenerator, AsyncIterator
from contextlib import asynccontextmanager
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import AsyncBaseHandler, AsyncClient

import capo_polly._auth._signers
import capo_polly._auth._sigv4
from capo_polly._auth._identity import Credentials
from capo_polly._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_polly._auth._zapros_handler import AuthMiddleware
from capo_polly._iter import ensure_async_iterator
from capo_polly._pagination import resolve_path as _resolve_path
from capo_polly._services._aws_config import aaws_config
from capo_polly._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import capo_polly.types.delete_lexicon_input
    import capo_polly.types.delete_lexicon_output
    import capo_polly.types.describe_voices_input
    import capo_polly.types.describe_voices_output
    import capo_polly.types.engine
    import capo_polly.types.get_lexicon_input
    import capo_polly.types.get_lexicon_output
    import capo_polly.types.get_speech_synthesis_task_input
    import capo_polly.types.get_speech_synthesis_task_output
    import capo_polly.types.include_additional_language_codes
    import capo_polly.types.language_code
    import capo_polly.types.lexicon_content
    import capo_polly.types.lexicon_name
    import capo_polly.types.lexicon_name_list
    import capo_polly.types.list_lexicons_input
    import capo_polly.types.list_lexicons_output
    import capo_polly.types.list_speech_synthesis_tasks_input
    import capo_polly.types.list_speech_synthesis_tasks_output
    import capo_polly.types.max_results
    import capo_polly.types.next_token
    import capo_polly.types.output_format
    import capo_polly.types.output_s3_bucket_name
    import capo_polly.types.output_s3_key_prefix
    import capo_polly.types.put_lexicon_input
    import capo_polly.types.put_lexicon_output
    import capo_polly.types.sample_rate
    import capo_polly.types.sns_topic_arn
    import capo_polly.types.speech_mark_type_list
    import capo_polly.types.start_speech_synthesis_stream_action_stream
    import capo_polly.types.start_speech_synthesis_stream_input
    import capo_polly.types.start_speech_synthesis_stream_output
    import capo_polly.types.start_speech_synthesis_task_input
    import capo_polly.types.start_speech_synthesis_task_output
    import capo_polly.types.synthesize_speech_input
    import capo_polly.types.synthesize_speech_output
    import capo_polly.types.task_id
    import capo_polly.types.task_status
    import capo_polly.types.text
    import capo_polly.types.text_type
    import capo_polly.types.voice_id


class AsyncPollyClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None
    anonymous: bool | None


class AsyncPollyClient:
    """A client for the ``Polly`` service.

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
        anonymous: Send requests unsigned, without resolving credentials, even for operations that require authentication.
    """

    def __init__(
        self,
        http_handler: AsyncBaseHandler | None = None,
        operation_interceptors: Iterable[AsyncInterceptor[Any, Any]] | None = None,
        retry_max_attempts: int | None = None,
        region: str | None = None,
        use_dual_stack: bool | None = None,
        use_fips: bool | None = None,
        endpoint: str | None = None,
        credentials: Credentials | None = None,
        credentials_provider: CredentialsProvider | None = None,
        anonymous: bool | None = None,
    ):
        self._client = AsyncClient(http_handler).wrap_with_middleware(
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
                AsyncClient(http_handler)
            )
        self._config = AsyncPollyClientConfig(
            {
                "operation_interceptors": operation_interceptors or [],
                "retry_max_attempts": retry_max_attempts,
                "region": region,
                "use_dual_stack": use_dual_stack,
                "use_fips": use_fips,
                "endpoint": endpoint,
                "credentials_provider": resolved_credentials_provider,
                "anonymous": anonymous,
            }
        )

    def operation_options(
        self, config_overrides: Optional[AsyncPollyClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncPollyClientConfig = config_overrides or {}
        interceptors_: list[AsyncInterceptor[Any, Any]] = [
            *overrides.get(
                "operation_interceptors", self._config.get("operation_interceptors", [])
            ),
            aaws_config(),
            aretry(),
        ]
        options_: AsyncOperationOptions = AsyncOperationOptions(
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
            anonymous=overrides.get("anonymous", self._config.get("anonymous")),
        )
        return interceptors_, options_

    async def delete_lexicon(
        self,
        name: "capo_polly.types.lexicon_name.LexiconName",
        *,
        config_overrides: Optional[AsyncPollyClientConfig] = None,
    ) -> "capo_polly.types.delete_lexicon_output.DeleteLexiconOutput":
        """<p>Deletes the specified pronunciation lexicon stored in an Amazon Web Services Region. A lexicon which has been deleted is not available for speech synthesis, nor is it possible to retrieve it using either the <code>GetLexicon</code> or <code>ListLexicon</code> APIs.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/polly/latest/dg/managing-lexicons.html">Managing Lexicons</a>.</p>

        Args:
            name: <p>The name of the lexicon to delete. Must be an existing lexicon in the region.</p>

        Raises:
            capo_polly.errors.lexicon_not_found_exception.LexiconNotFoundException: <p>Amazon Polly can't find the specified lexicon. This could be caused by a lexicon that is missing, its name is misspelled or specifying a lexicon that is in a different region.</p> <p>Verify that the lexicon exists, is in the region (see <a>ListLexicons</a>) and that you spelled its name is spelled correctly. Then try again.</p>
            capo_polly.errors.service_failure_exception.ServiceFailureException: <p>An unknown condition has caused a service failure.</p>
            capo_polly.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To delete a lexicon
            Deletes a specified pronunciation lexicon stored in an AWS Region.

            >>> await client.delete_lexicon(name='example')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_polly.types.delete_lexicon_input.DeleteLexiconInput]",
        ) -> AsyncOperationResponse[
            "capo_polly.types.delete_lexicon_output.DeleteLexiconOutput"
        ]:
            import capo_polly._operations.parrot_v1.delete_lexicon

            (
                output,
                http_response,
            ) = await capo_polly._operations.parrot_v1.delete_lexicon.async_delete_lexicon(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_polly.types.delete_lexicon_input.DeleteLexiconInput = {
            "name": name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_voices(
        self,
        *,
        config_overrides: Optional[AsyncPollyClientConfig] = None,
        engine: Optional["capo_polly.types.engine.Engine"] = None,
        language_code: Optional["capo_polly.types.language_code.LanguageCode"] = None,
        include_additional_language_codes: Optional[
            "capo_polly.types.include_additional_language_codes.IncludeAdditionalLanguageCodes"
        ] = None,
        next_token: Optional["capo_polly.types.next_token.NextToken"] = None,
    ) -> "capo_polly.types.describe_voices_output.DescribeVoicesOutput":
        """<p>Returns the list of voices that are available for use when requesting speech synthesis. Each voice speaks a specified language, is either male or female, and is identified by an ID, which is the ASCII version of the voice name. </p> <p>When synthesizing speech ( <code>SynthesizeSpeech</code> ), you provide the voice ID for the voice you want from the list of voices returned by <code>DescribeVoices</code>.</p> <p>For example, you want your news reader application to read news in a specific language, but giving a user the option to choose the voice. Using the <code>DescribeVoices</code> operation you can provide the user with a list of available voices to select from.</p> <p> You can optionally specify a language code to filter the available voices. For example, if you specify <code>en-US</code>, the operation returns a list of all available US English voices. </p> <p>This operation requires permissions to perform the <code>polly:DescribeVoices</code> action.</p>

        Args:
            engine: <p>Specifies the engine (<code>standard</code>, <code>neural</code>, <code>long-form</code> or <code>generative</code>) used by Amazon Polly when processing input text for speech synthesis. </p>
            language_code: <p> The language identification tag (ISO 639 code for the language name-ISO 3166 country code) for filtering the list of voices returned. If you don't specify this optional parameter, all available voices are returned. </p>
            include_additional_language_codes: <p>Boolean value indicating whether to return any bilingual voices that use the specified language as an additional language. For instance, if you request all languages that use US English (es-US), and there is an Italian voice that speaks both Italian (it-IT) and US English, that voice will be included if you specify <code>yes</code> but not if you specify <code>no</code>.</p>
            next_token: <p>An opaque pagination token returned from the previous <code>DescribeVoices</code> operation. If present, this indicates where to continue the listing.</p>

        Raises:
            capo_polly.errors.invalid_next_token_exception.InvalidNextTokenException: <p>The NextToken is invalid. Verify that it's spelled correctly, and then try again.</p>
            capo_polly.errors.service_failure_exception.ServiceFailureException: <p>An unknown condition has caused a service failure.</p>
            capo_polly.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To describe available voices
            Returns the list of voices that are available for use when requesting speech synthesis. Displayed languages are those within the specified language code. If no language code is specified, voices for all available languages are displayed.

            >>> await client.describe_voices(language_code='en-GB')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_polly.types.describe_voices_input.DescribeVoicesInput]",
        ) -> AsyncOperationResponse[
            "capo_polly.types.describe_voices_output.DescribeVoicesOutput"
        ]:
            import capo_polly._operations.parrot_v1.describe_voices

            (
                output,
                http_response,
            ) = await capo_polly._operations.parrot_v1.describe_voices.async_describe_voices(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_polly.types.describe_voices_input.DescribeVoicesInput = {}
        if engine is not None:
            input_["engine"] = engine
        if language_code is not None:
            input_["language_code"] = language_code
        if include_additional_language_codes is not None:
            input_["include_additional_language_codes"] = (
                include_additional_language_codes
            )
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_lexicon(
        self,
        name: "capo_polly.types.lexicon_name.LexiconName",
        *,
        config_overrides: Optional[AsyncPollyClientConfig] = None,
    ) -> "capo_polly.types.get_lexicon_output.GetLexiconOutput":
        """<p>Returns the content of the specified pronunciation lexicon stored in an Amazon Web Services Region. For more information, see <a href="https://docs.aws.amazon.com/polly/latest/dg/managing-lexicons.html">Managing Lexicons</a>.</p>

        Args:
            name: <p>Name of the lexicon.</p>

        Raises:
            capo_polly.errors.lexicon_not_found_exception.LexiconNotFoundException: <p>Amazon Polly can't find the specified lexicon. This could be caused by a lexicon that is missing, its name is misspelled or specifying a lexicon that is in a different region.</p> <p>Verify that the lexicon exists, is in the region (see <a>ListLexicons</a>) and that you spelled its name is spelled correctly. Then try again.</p>
            capo_polly.errors.service_failure_exception.ServiceFailureException: <p>An unknown condition has caused a service failure.</p>
            capo_polly.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_polly.types.get_lexicon_input.GetLexiconInput]",
        ) -> AsyncOperationResponse[
            "capo_polly.types.get_lexicon_output.GetLexiconOutput"
        ]:
            import capo_polly._operations.parrot_v1.get_lexicon

            (
                output,
                http_response,
            ) = await capo_polly._operations.parrot_v1.get_lexicon.async_get_lexicon(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_polly.types.get_lexicon_input.GetLexiconInput = {"name": name}

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_speech_synthesis_task(
        self,
        task_id: "capo_polly.types.task_id.TaskId",
        *,
        config_overrides: Optional[AsyncPollyClientConfig] = None,
    ) -> (
        "capo_polly.types.get_speech_synthesis_task_output.GetSpeechSynthesisTaskOutput"
    ):
        """<p>Retrieves a specific SpeechSynthesisTask object based on its TaskID. This object contains information about the given speech synthesis task, including the status of the task, and a link to the S3 bucket containing the output of the task.</p>

        Args:
            task_id: <p>The Amazon Polly generated identifier for a speech synthesis task.</p>

        Raises:
            capo_polly.errors.invalid_task_id_exception.InvalidTaskIdException: <p>The provided Task ID is not valid. Please provide a valid Task ID and try again.</p>
            capo_polly.errors.service_failure_exception.ServiceFailureException: <p>An unknown condition has caused a service failure.</p>
            capo_polly.errors.synthesis_task_not_found_exception.SynthesisTaskNotFoundException: <p>The Speech Synthesis task with requested Task ID cannot be found.</p>
            capo_polly.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_polly.types.get_speech_synthesis_task_input.GetSpeechSynthesisTaskInput]",
        ) -> AsyncOperationResponse[
            "capo_polly.types.get_speech_synthesis_task_output.GetSpeechSynthesisTaskOutput"
        ]:
            import capo_polly._operations.parrot_v1.get_speech_synthesis_task

            (
                output,
                http_response,
            ) = await capo_polly._operations.parrot_v1.get_speech_synthesis_task.async_get_speech_synthesis_task(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_polly.types.get_speech_synthesis_task_input.GetSpeechSynthesisTaskInput = {
            "task_id": task_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_lexicons(
        self,
        *,
        config_overrides: Optional[AsyncPollyClientConfig] = None,
        next_token: Optional["capo_polly.types.next_token.NextToken"] = None,
    ) -> "capo_polly.types.list_lexicons_output.ListLexiconsOutput":
        """<p>Returns a list of pronunciation lexicons stored in an Amazon Web Services Region. For more information, see <a href="https://docs.aws.amazon.com/polly/latest/dg/managing-lexicons.html">Managing Lexicons</a>.</p>

        Args:
            next_token: <p>An opaque pagination token returned from previous <code>ListLexicons</code> operation. If present, indicates where to continue the list of lexicons.</p>

        Raises:
            capo_polly.errors.invalid_next_token_exception.InvalidNextTokenException: <p>The NextToken is invalid. Verify that it's spelled correctly, and then try again.</p>
            capo_polly.errors.service_failure_exception.ServiceFailureException: <p>An unknown condition has caused a service failure.</p>
            capo_polly.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To list all lexicons in a region
            Returns a list of pronunciation lexicons stored in an AWS Region.

            >>> await client.list_lexicons()
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_polly.types.list_lexicons_input.ListLexiconsInput]",
        ) -> AsyncOperationResponse[
            "capo_polly.types.list_lexicons_output.ListLexiconsOutput"
        ]:
            import capo_polly._operations.parrot_v1.list_lexicons

            (
                output,
                http_response,
            ) = await capo_polly._operations.parrot_v1.list_lexicons.async_list_lexicons(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_polly.types.list_lexicons_input.ListLexiconsInput = {}
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_speech_synthesis_tasks(
        self,
        *,
        config_overrides: Optional[AsyncPollyClientConfig] = None,
        max_results: Optional["capo_polly.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_polly.types.next_token.NextToken"] = None,
        status: Optional["capo_polly.types.task_status.TaskStatus"] = None,
    ) -> "capo_polly.types.list_speech_synthesis_tasks_output.ListSpeechSynthesisTasksOutput":
        """<p>Returns a list of SpeechSynthesisTask objects ordered by their creation date. This operation can filter the tasks by their status, for example, allowing users to list only tasks that are completed.</p>

        Args:
            max_results: <p>Maximum number of speech synthesis tasks returned in a List operation.</p>
            next_token: <p>The pagination token to use in the next request to continue the listing of speech synthesis tasks. </p>
            status: <p>Status of the speech synthesis tasks returned in a List operation</p>

        Raises:
            capo_polly.errors.invalid_next_token_exception.InvalidNextTokenException: <p>The NextToken is invalid. Verify that it's spelled correctly, and then try again.</p>
            capo_polly.errors.service_failure_exception.ServiceFailureException: <p>An unknown condition has caused a service failure.</p>
            capo_polly.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_polly.types.list_speech_synthesis_tasks_input.ListSpeechSynthesisTasksInput]",
        ) -> AsyncOperationResponse[
            "capo_polly.types.list_speech_synthesis_tasks_output.ListSpeechSynthesisTasksOutput"
        ]:
            import capo_polly._operations.parrot_v1.list_speech_synthesis_tasks

            (
                output,
                http_response,
            ) = await capo_polly._operations.parrot_v1.list_speech_synthesis_tasks.async_list_speech_synthesis_tasks(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_polly.types.list_speech_synthesis_tasks_input.ListSpeechSynthesisTasksInput = {}
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if status is not None:
            input_["status"] = status

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_speech_synthesis_tasks(
        self,
        *,
        config_overrides: Optional[AsyncPollyClientConfig] = None,
        max_results: Optional["capo_polly.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_polly.types.next_token.NextToken"] = None,
        status: Optional["capo_polly.types.task_status.TaskStatus"] = None,
    ) -> "AsyncIterator[capo_polly.types.list_speech_synthesis_tasks_output.ListSpeechSynthesisTasksOutput]":
        _token = next_token
        while True:
            _response = await self.list_speech_synthesis_tasks(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
                status=status,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def put_lexicon(
        self,
        name: "capo_polly.types.lexicon_name.LexiconName",
        content: "capo_polly.types.lexicon_content.LexiconContent",
        *,
        config_overrides: Optional[AsyncPollyClientConfig] = None,
    ) -> "capo_polly.types.put_lexicon_output.PutLexiconOutput":
        """<p>Stores a pronunciation lexicon in an Amazon Web Services Region. If a lexicon with the same name already exists in the region, it is overwritten by the new lexicon. Lexicon operations have eventual consistency, therefore, it might take some time before the lexicon is available to the SynthesizeSpeech operation.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/polly/latest/dg/managing-lexicons.html">Managing Lexicons</a>.</p>

        Args:
            name: <p>Name of the lexicon. The name must follow the regular express format [0-9A-Za-z]{1,20}. That is, the name is a case-sensitive alphanumeric string up to 20 characters long. </p>
            content: <p>Content of the PLS lexicon as string data.</p>

        Raises:
            capo_polly.errors.invalid_lexicon_exception.InvalidLexiconException: <p>Amazon Polly can't find the specified lexicon. Verify that the lexicon's name is spelled correctly, and then try again.</p>
            capo_polly.errors.lexicon_size_exceeded_exception.LexiconSizeExceededException: <p>The maximum size of the specified lexicon would be exceeded by this operation.</p>
            capo_polly.errors.max_lexeme_length_exceeded_exception.MaxLexemeLengthExceededException: <p>The maximum size of the lexeme would be exceeded by this operation.</p>
            capo_polly.errors.max_lexicons_number_exceeded_exception.MaxLexiconsNumberExceededException: <p>The maximum number of lexicons would be exceeded by this operation.</p>
            capo_polly.errors.service_failure_exception.ServiceFailureException: <p>An unknown condition has caused a service failure.</p>
            capo_polly.errors.unsupported_pls_alphabet_exception.UnsupportedPlsAlphabetException: <p>The alphabet specified by the lexicon is not a supported alphabet. Valid values are <code>x-sampa</code> and <code>ipa</code>.</p>
            capo_polly.errors.unsupported_pls_language_exception.UnsupportedPlsLanguageException: <p>The language specified in the lexicon is unsupported. For a list of supported languages, see <a href="https://docs.aws.amazon.com/polly/latest/dg/API_LexiconAttributes.html">Lexicon Attributes</a>.</p>
            capo_polly.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To save a lexicon
            Stores a pronunciation lexicon in an AWS Region.

            >>> await client.put_lexicon(name='W3C', content='<Lexicon Content>')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_polly.types.put_lexicon_input.PutLexiconInput]",
        ) -> AsyncOperationResponse[
            "capo_polly.types.put_lexicon_output.PutLexiconOutput"
        ]:
            import capo_polly._operations.parrot_v1.put_lexicon

            (
                output,
                http_response,
            ) = await capo_polly._operations.parrot_v1.put_lexicon.async_put_lexicon(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_polly.types.put_lexicon_input.PutLexiconInput = {
            "name": name,
            "content": content,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    @asynccontextmanager
    async def start_speech_synthesis_stream(
        self,
        engine: "capo_polly.types.engine.Engine",
        output_format: "capo_polly.types.output_format.OutputFormat",
        voice_id: "capo_polly.types.voice_id.VoiceId",
        *,
        config_overrides: Optional[AsyncPollyClientConfig] = None,
        language_code: Optional["capo_polly.types.language_code.LanguageCode"] = None,
        lexicon_names: Optional[
            "capo_polly.types.lexicon_name_list.LexiconNameList"
        ] = None,
        sample_rate: Optional["capo_polly.types.sample_rate.SampleRate"] = None,
        action_stream: Optional[
            "AsyncIterator[capo_polly.types.start_speech_synthesis_stream_action_stream._StartSpeechSynthesisStreamActionStream] | capo_polly.types.start_speech_synthesis_stream_action_stream._StartSpeechSynthesisStreamActionStream"
        ] = None,
    ) -> "AsyncGenerator[capo_polly.types.start_speech_synthesis_stream_output.StartSpeechSynthesisStreamOutput]":
        """<p>Synthesizes UTF-8 input, plain text, or SSML over a bidirectional streaming connection. Specify synthesis parameters in HTTP/2 headers, send text incrementally as events on the input stream, and receive synthesized audio as it becomes available.</p> <p>This operation serves as a bidirectional counterpart to <code>SynthesizeSpeech</code>:</p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/polly/latest/API/API_SynthesizeSpeech.html">SynthesizeSpeech</a> </p> </li> </ul>

        Args:
            engine: <p>Specifies the engine for Amazon Polly to use when processing input text for speech synthesis. Currently, only the <code>generative</code> engine is supported. If you specify a voice that the selected engine doesn't support, Amazon Polly returns an error.</p>
            language_code: <p>An optional parameter that sets the language code for the speech synthesis request. Specify this parameter only when using a bilingual voice. If a bilingual voice is used and no language code is specified, Amazon Polly uses the default language of the bilingual voice.</p>
            lexicon_names: <p>The names of one or more pronunciation lexicons for the service to apply during synthesis. Amazon Polly applies lexicons only when the lexicon language matches the voice language.</p>
            output_format: <p>The audio format for the synthesized speech. Currently, Amazon Polly does not support JSON speech marks.</p>
            sample_rate: <p>The audio frequency, specified in Hz.</p>
            voice_id: <p>The voice to use in synthesis. To get a list of available voice IDs, use the <a href="https://docs.aws.amazon.com/polly/latest/API/API_DescribeVoices.html">DescribeVoices</a> operation.</p>
            action_stream: <p>The input event stream that contains text events and stream control events.</p>

        Raises:
            capo_polly.errors.service_failure_exception.ServiceFailureException: <p>An unknown condition has caused a service failure.</p>
            capo_polly.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would cause a service quota to be exceeded.</p>
            capo_polly.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling.</p>
            capo_polly.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_polly.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_polly.types.start_speech_synthesis_stream_input.StartSpeechSynthesisStreamInput]",
        ) -> AsyncOperationResponse[
            "capo_polly.types.start_speech_synthesis_stream_output.StartSpeechSynthesisStreamOutput"
        ]:
            import capo_polly._operations.parrot_v1.start_speech_synthesis_stream

            (
                output,
                http_response,
            ) = await capo_polly._operations.parrot_v1.start_speech_synthesis_stream.async_start_speech_synthesis_stream(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_polly.types.start_speech_synthesis_stream_input.StartSpeechSynthesisStreamInput = {
            "engine": engine,
            "output_format": output_format,
            "voice_id": voice_id,
        }
        if language_code is not None:
            input_["language_code"] = language_code
        if lexicon_names is not None:
            input_["lexicon_names"] = lexicon_names
        if sample_rate is not None:
            input_["sample_rate"] = sample_rate
        if action_stream is not None:
            input_["action_stream"] = ensure_async_iterator(action_stream)

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        try:
            yield response.output
        finally:
            await response.response.aclose()

    async def start_speech_synthesis_task(
        self,
        output_format: "capo_polly.types.output_format.OutputFormat",
        output_s3_bucket_name: "capo_polly.types.output_s3_bucket_name.OutputS3BucketName",
        text: "capo_polly.types.text.Text",
        voice_id: "capo_polly.types.voice_id.VoiceId",
        *,
        config_overrides: Optional[AsyncPollyClientConfig] = None,
        engine: Optional["capo_polly.types.engine.Engine"] = None,
        language_code: Optional["capo_polly.types.language_code.LanguageCode"] = None,
        lexicon_names: Optional[
            "capo_polly.types.lexicon_name_list.LexiconNameList"
        ] = None,
        output_s3_key_prefix: Optional[
            "capo_polly.types.output_s3_key_prefix.OutputS3KeyPrefix"
        ] = None,
        sample_rate: Optional["capo_polly.types.sample_rate.SampleRate"] = None,
        sns_topic_arn: Optional["capo_polly.types.sns_topic_arn.SnsTopicArn"] = None,
        speech_mark_types: Optional[
            "capo_polly.types.speech_mark_type_list.SpeechMarkTypeList"
        ] = None,
        text_type: Optional["capo_polly.types.text_type.TextType"] = None,
    ) -> "capo_polly.types.start_speech_synthesis_task_output.StartSpeechSynthesisTaskOutput":
        """<p>Allows the creation of an asynchronous synthesis task, by starting a new <code>SpeechSynthesisTask</code>. This operation requires all the standard information needed for speech synthesis, plus the name of an Amazon S3 bucket for the service to store the output of the synthesis task and two optional parameters (<code>OutputS3KeyPrefix</code> and <code>SnsTopicArn</code>). Once the synthesis task is created, this operation will return a <code>SpeechSynthesisTask</code> object, which will include an identifier of this task as well as the current status. The <code>SpeechSynthesisTask</code> object is available for 72 hours after starting the asynchronous synthesis task.</p>

        Args:
            engine: <p>Specifies the engine (<code>standard</code>, <code>neural</code>, <code>long-form</code> or <code>generative</code>) for Amazon Polly to use when processing input text for speech synthesis. Using a voice that is not supported for the engine selected will result in an error.</p>
            language_code: <p>Optional language code for the Speech Synthesis request. This is only necessary if using a bilingual voice, such as Aditi, which can be used for either Indian English (en-IN) or Hindi (hi-IN). </p> <p>If a bilingual voice is used and no language code is specified, Amazon Polly uses the default language of the bilingual voice. The default language for any voice is the one returned by the <a href="https://docs.aws.amazon.com/polly/latest/dg/API_DescribeVoices.html">DescribeVoices</a> operation for the <code>LanguageCode</code> parameter. For example, if no language code is specified, Aditi will use Indian English rather than Hindi.</p>
            lexicon_names: <p>List of one or more pronunciation lexicon names you want the service to apply during synthesis. Lexicons are applied only if the language of the lexicon is the same as the language of the voice. </p>
            output_format: <p>The format in which the returned output will be encoded. For audio stream, this will be mp3, ogg_vorbis, ogg_opus, mu-law, a-law, or pcm. For speech marks, this will be json. </p>
            output_s3_bucket_name: <p>Amazon S3 bucket name to which the output file will be saved.</p>
            output_s3_key_prefix: <p>The Amazon S3 key prefix for the output speech file.</p>
            sample_rate: <p>The audio frequency specified in Hz.</p> <p>The valid values for mp3 and ogg_vorbis are "8000", "16000", "22050", and "24000". The default value for standard voices is "22050". The default value for neural voices is "24000". The default value for long-form voices is "24000". The default value for generative voices is "24000".</p> <p>Valid values for pcm are "8000" and "16000" The default value is "16000". </p> <p>Valid value for ogg_opus is "48000". </p> <p>Valid value for mu-law and a-law is "8000". </p>
            sns_topic_arn: <p>ARN for the SNS topic optionally used for providing status notification for a speech synthesis task.</p>
            speech_mark_types: <p>The type of speech marks returned for the input text.</p>
            text: <p>The input text to synthesize. If you specify ssml as the TextType, follow the SSML format for the input text. </p>
            text_type: <p>Specifies whether the input text is plain text or SSML. The default value is plain text. </p>
            voice_id: <p>Voice ID to use for the synthesis. </p>

        Raises:
            capo_polly.errors.engine_not_supported_exception.EngineNotSupportedException: <p>This engine is not compatible with the voice that you have designated. Choose a new voice that is compatible with the engine or change the engine and restart the operation.</p>
            capo_polly.errors.invalid_s3_bucket_exception.InvalidS3BucketException: <p>The provided Amazon S3 bucket name is invalid. Please check your input with S3 bucket naming requirements and try again.</p>
            capo_polly.errors.invalid_s3_key_exception.InvalidS3KeyException: <p>The provided Amazon S3 key prefix is invalid. Please provide a valid S3 object key name.</p>
            capo_polly.errors.invalid_sample_rate_exception.InvalidSampleRateException: <p>The specified sample rate is not valid.</p>
            capo_polly.errors.invalid_sns_topic_arn_exception.InvalidSnsTopicArnException: <p>The provided SNS topic ARN is invalid. Please provide a valid SNS topic ARN and try again.</p>
            capo_polly.errors.invalid_ssml_exception.InvalidSsmlException: <p>The SSML you provided is invalid. Verify the SSML syntax, spelling of tags and values, and then try again.</p>
            capo_polly.errors.language_not_supported_exception.LanguageNotSupportedException: <p>The language specified is not currently supported by Amazon Polly in this capacity.</p>
            capo_polly.errors.lexicon_not_found_exception.LexiconNotFoundException: <p>Amazon Polly can't find the specified lexicon. This could be caused by a lexicon that is missing, its name is misspelled or specifying a lexicon that is in a different region.</p> <p>Verify that the lexicon exists, is in the region (see <a>ListLexicons</a>) and that you spelled its name is spelled correctly. Then try again.</p>
            capo_polly.errors.marks_not_supported_for_format_exception.MarksNotSupportedForFormatException: <p>Speech marks are not supported for the <code>OutputFormat</code> selected. Speech marks are only available for content in <code>json</code> format.</p>
            capo_polly.errors.service_failure_exception.ServiceFailureException: <p>An unknown condition has caused a service failure.</p>
            capo_polly.errors.ssml_marks_not_supported_for_text_type_exception.SsmlMarksNotSupportedForTextTypeException: <p>SSML speech marks are not supported for plain text-type input.</p>
            capo_polly.errors.text_length_exceeded_exception.TextLengthExceededException: <p>The value of the "Text" parameter is longer than the accepted limits. For the <code>SynthesizeSpeech</code> API, the limit for input text is a maximum of 6000 characters total, of which no more than 3000 can be billed characters. For the <code>StartSpeechSynthesisTask</code> API, the maximum is 200,000 characters, of which no more than 100,000 can be billed characters. SSML tags are not counted as billed characters.</p>
            capo_polly.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_polly.types.start_speech_synthesis_task_input.StartSpeechSynthesisTaskInput]",
        ) -> AsyncOperationResponse[
            "capo_polly.types.start_speech_synthesis_task_output.StartSpeechSynthesisTaskOutput"
        ]:
            import capo_polly._operations.parrot_v1.start_speech_synthesis_task

            (
                output,
                http_response,
            ) = await capo_polly._operations.parrot_v1.start_speech_synthesis_task.async_start_speech_synthesis_task(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_polly.types.start_speech_synthesis_task_input.StartSpeechSynthesisTaskInput = {
            "output_format": output_format,
            "output_s3_bucket_name": output_s3_bucket_name,
            "text": text,
            "voice_id": voice_id,
        }
        if engine is not None:
            input_["engine"] = engine
        if language_code is not None:
            input_["language_code"] = language_code
        if lexicon_names is not None:
            input_["lexicon_names"] = lexicon_names
        if output_s3_key_prefix is not None:
            input_["output_s3_key_prefix"] = output_s3_key_prefix
        if sample_rate is not None:
            input_["sample_rate"] = sample_rate
        if sns_topic_arn is not None:
            input_["sns_topic_arn"] = sns_topic_arn
        if speech_mark_types is not None:
            input_["speech_mark_types"] = speech_mark_types
        if text_type is not None:
            input_["text_type"] = text_type

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    @asynccontextmanager
    async def synthesize_speech(
        self,
        output_format: "capo_polly.types.output_format.OutputFormat",
        text: "capo_polly.types.text.Text",
        voice_id: "capo_polly.types.voice_id.VoiceId",
        *,
        config_overrides: Optional[AsyncPollyClientConfig] = None,
        engine: Optional["capo_polly.types.engine.Engine"] = None,
        language_code: Optional["capo_polly.types.language_code.LanguageCode"] = None,
        lexicon_names: Optional[
            "capo_polly.types.lexicon_name_list.LexiconNameList"
        ] = None,
        sample_rate: Optional["capo_polly.types.sample_rate.SampleRate"] = None,
        speech_mark_types: Optional[
            "capo_polly.types.speech_mark_type_list.SpeechMarkTypeList"
        ] = None,
        text_type: Optional["capo_polly.types.text_type.TextType"] = None,
    ) -> "AsyncGenerator[capo_polly.types.synthesize_speech_output.SynthesizeSpeechOutput]":
        """<p>Synthesizes UTF-8 input, plain text or SSML, to a stream of bytes. SSML input must be valid, well-formed SSML. Some alphabets might not be available with all the voices (for example, Cyrillic might not be read at all by English voices) unless phoneme mapping is used. For more information, see <a href="https://docs.aws.amazon.com/polly/latest/dg/how-text-to-speech-works.html">How it Works</a>.</p>

        Args:
            engine: <p>Specifies the engine (<code>standard</code>, <code>neural</code>, <code>long-form</code>, or <code>generative</code>) for Amazon Polly to use when processing input text for speech synthesis. Provide an engine that is supported by the voice you select. If you don't provide an engine, the standard engine is selected by default. If a chosen voice isn't supported by the standard engine, this will result in an error. For information on Amazon Polly voices and which voices are available for each engine, see <a href="https://docs.aws.amazon.com/polly/latest/dg/voicelist.html">Available Voices</a>.</p>
            language_code: <p>Optional language code for the Synthesize Speech request. This is only necessary if using a bilingual voice, such as Aditi, which can be used for either Indian English (en-IN) or Hindi (hi-IN). </p> <p>If a bilingual voice is used and no language code is specified, Amazon Polly uses the default language of the bilingual voice. The default language for any voice is the one returned by the <a href="https://docs.aws.amazon.com/polly/latest/dg/API_DescribeVoices.html">DescribeVoices</a> operation for the <code>LanguageCode</code> parameter. For example, if no language code is specified, Aditi will use Indian English rather than Hindi.</p>
            lexicon_names: <p>List of one or more pronunciation lexicon names you want the service to apply during synthesis. Lexicons are applied only if the language of the lexicon is the same as the language of the voice. For information about storing lexicons, see <a href="https://docs.aws.amazon.com/polly/latest/dg/API_PutLexicon.html">PutLexicon</a>.</p>
            output_format: <p> The format in which the returned output will be encoded. For audio stream, this will be mp3, ogg_vorbis, ogg_opus, mu-law, a-law or pcm. For speech marks, this will be json. </p> <p>When pcm is used, the content returned is audio/pcm in a signed 16-bit, 1 channel (mono), little-endian format. </p>
            sample_rate: <p>The audio frequency specified in Hz.</p> <p>The valid values for mp3 and ogg_vorbis are "8000", "16000", "22050", "24000", "44100" and "48000". The default value for standard voices is "22050". The default value for neural voices is "24000". The default value for long-form voices is "24000". The default value for generative voices is "24000".</p> <p>Valid values for pcm are "8000" and "16000" The default value is "16000". </p> <p>Valid value for ogg_opus is "48000". </p> <p>Valid value for mu-law and a-law is "8000". </p>
            speech_mark_types: <p>The type of speech marks returned for the input text.</p>
            text: <p> Input text to synthesize. If you specify <code>ssml</code> as the <code>TextType</code>, follow the SSML format for the input text. </p>
            text_type: <p> Specifies whether the input text is plain text or SSML. The default value is plain text. For more information, see <a href="https://docs.aws.amazon.com/polly/latest/dg/ssml.html">Using SSML</a>.</p>
            voice_id: <p> Voice ID to use for the synthesis. You can get a list of available voice IDs by calling the <a href="https://docs.aws.amazon.com/polly/latest/dg/API_DescribeVoices.html">DescribeVoices</a> operation. </p>

        Raises:
            capo_polly.errors.engine_not_supported_exception.EngineNotSupportedException: <p>This engine is not compatible with the voice that you have designated. Choose a new voice that is compatible with the engine or change the engine and restart the operation.</p>
            capo_polly.errors.invalid_sample_rate_exception.InvalidSampleRateException: <p>The specified sample rate is not valid.</p>
            capo_polly.errors.invalid_ssml_exception.InvalidSsmlException: <p>The SSML you provided is invalid. Verify the SSML syntax, spelling of tags and values, and then try again.</p>
            capo_polly.errors.language_not_supported_exception.LanguageNotSupportedException: <p>The language specified is not currently supported by Amazon Polly in this capacity.</p>
            capo_polly.errors.lexicon_not_found_exception.LexiconNotFoundException: <p>Amazon Polly can't find the specified lexicon. This could be caused by a lexicon that is missing, its name is misspelled or specifying a lexicon that is in a different region.</p> <p>Verify that the lexicon exists, is in the region (see <a>ListLexicons</a>) and that you spelled its name is spelled correctly. Then try again.</p>
            capo_polly.errors.marks_not_supported_for_format_exception.MarksNotSupportedForFormatException: <p>Speech marks are not supported for the <code>OutputFormat</code> selected. Speech marks are only available for content in <code>json</code> format.</p>
            capo_polly.errors.service_failure_exception.ServiceFailureException: <p>An unknown condition has caused a service failure.</p>
            capo_polly.errors.ssml_marks_not_supported_for_text_type_exception.SsmlMarksNotSupportedForTextTypeException: <p>SSML speech marks are not supported for plain text-type input.</p>
            capo_polly.errors.text_length_exceeded_exception.TextLengthExceededException: <p>The value of the "Text" parameter is longer than the accepted limits. For the <code>SynthesizeSpeech</code> API, the limit for input text is a maximum of 6000 characters total, of which no more than 3000 can be billed characters. For the <code>StartSpeechSynthesisTask</code> API, the maximum is 200,000 characters, of which no more than 100,000 can be billed characters. SSML tags are not counted as billed characters.</p>
            capo_polly.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To synthesize speech
            Synthesizes plain text or SSML into a file of human-like speech.

            >>> await client.synthesize_speech(lexicon_names=['example'], output_format='mp3', sample_rate='8000', text='All Gaul is divided into three parts', text_type='text', voice_id='Joanna')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_polly.types.synthesize_speech_input.SynthesizeSpeechInput]",
        ) -> AsyncOperationResponse[
            "capo_polly.types.synthesize_speech_output.SynthesizeSpeechOutput"
        ]:
            import capo_polly._operations.parrot_v1.synthesize_speech

            (
                output,
                http_response,
            ) = await capo_polly._operations.parrot_v1.synthesize_speech.async_synthesize_speech(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_polly.types.synthesize_speech_input.SynthesizeSpeechInput = {
            "output_format": output_format,
            "text": text,
            "voice_id": voice_id,
        }
        if engine is not None:
            input_["engine"] = engine
        if language_code is not None:
            input_["language_code"] = language_code
        if lexicon_names is not None:
            input_["lexicon_names"] = lexicon_names
        if sample_rate is not None:
            input_["sample_rate"] = sample_rate
        if speech_mark_types is not None:
            input_["speech_mark_types"] = speech_mark_types
        if text_type is not None:
            input_["text_type"] = text_type

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        try:
            yield response.output
        finally:
            await response.response.aclose()

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(self, exc_type: Any, exc: Any, tb: Any):
        await self._client.aclose()
