"""Generated from Smithy shape ``com.amazonaws.lexmodelbuildingservice#AWSDeepSenseModelBuildingService``."""

import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import AsyncBaseHandler, AsyncClient

import capo_lex_model_building_service._auth._signers
import capo_lex_model_building_service._auth._sigv4
from capo_lex_model_building_service._auth._identity import Credentials
from capo_lex_model_building_service._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_lex_model_building_service._auth._zapros_handler import AuthMiddleware
from capo_lex_model_building_service._pagination import resolve_path as _resolve_path
from capo_lex_model_building_service._services._aws_config import aaws_config
from capo_lex_model_building_service._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import capo_lex_model_building_service.types.alias_name
    import capo_lex_model_building_service.types.alias_name_or_list_all
    import capo_lex_model_building_service.types.amazon_resource_name
    import capo_lex_model_building_service.types.blob
    import capo_lex_model_building_service.types.boolean
    import capo_lex_model_building_service.types.bot_channel_name
    import capo_lex_model_building_service.types.bot_name
    import capo_lex_model_building_service.types.bot_versions
    import capo_lex_model_building_service.types.builtin_intent_signature
    import capo_lex_model_building_service.types.code_hook
    import capo_lex_model_building_service.types.confidence_threshold
    import capo_lex_model_building_service.types.conversation_logs_request
    import capo_lex_model_building_service.types.create_bot_version_request
    import capo_lex_model_building_service.types.create_bot_version_response
    import capo_lex_model_building_service.types.create_intent_version_request
    import capo_lex_model_building_service.types.create_intent_version_response
    import capo_lex_model_building_service.types.create_slot_type_version_request
    import capo_lex_model_building_service.types.create_slot_type_version_response
    import capo_lex_model_building_service.types.custom_or_builtin_slot_type_name
    import capo_lex_model_building_service.types.delete_bot_alias_request
    import capo_lex_model_building_service.types.delete_bot_channel_association_request
    import capo_lex_model_building_service.types.delete_bot_request
    import capo_lex_model_building_service.types.delete_bot_version_request
    import capo_lex_model_building_service.types.delete_intent_request
    import capo_lex_model_building_service.types.delete_intent_version_request
    import capo_lex_model_building_service.types.delete_slot_type_request
    import capo_lex_model_building_service.types.delete_slot_type_version_request
    import capo_lex_model_building_service.types.delete_utterances_request
    import capo_lex_model_building_service.types.description
    import capo_lex_model_building_service.types.enumeration_values
    import capo_lex_model_building_service.types.export_type
    import capo_lex_model_building_service.types.follow_up_prompt
    import capo_lex_model_building_service.types.fulfillment_activity
    import capo_lex_model_building_service.types.get_bot_alias_request
    import capo_lex_model_building_service.types.get_bot_alias_response
    import capo_lex_model_building_service.types.get_bot_aliases_request
    import capo_lex_model_building_service.types.get_bot_aliases_response
    import capo_lex_model_building_service.types.get_bot_channel_association_request
    import capo_lex_model_building_service.types.get_bot_channel_association_response
    import capo_lex_model_building_service.types.get_bot_channel_associations_request
    import capo_lex_model_building_service.types.get_bot_channel_associations_response
    import capo_lex_model_building_service.types.get_bot_request
    import capo_lex_model_building_service.types.get_bot_response
    import capo_lex_model_building_service.types.get_bot_versions_request
    import capo_lex_model_building_service.types.get_bot_versions_response
    import capo_lex_model_building_service.types.get_bots_request
    import capo_lex_model_building_service.types.get_bots_response
    import capo_lex_model_building_service.types.get_builtin_intent_request
    import capo_lex_model_building_service.types.get_builtin_intent_response
    import capo_lex_model_building_service.types.get_builtin_intents_request
    import capo_lex_model_building_service.types.get_builtin_intents_response
    import capo_lex_model_building_service.types.get_builtin_slot_types_request
    import capo_lex_model_building_service.types.get_builtin_slot_types_response
    import capo_lex_model_building_service.types.get_export_request
    import capo_lex_model_building_service.types.get_export_response
    import capo_lex_model_building_service.types.get_import_request
    import capo_lex_model_building_service.types.get_import_response
    import capo_lex_model_building_service.types.get_intent_request
    import capo_lex_model_building_service.types.get_intent_response
    import capo_lex_model_building_service.types.get_intent_versions_request
    import capo_lex_model_building_service.types.get_intent_versions_response
    import capo_lex_model_building_service.types.get_intents_request
    import capo_lex_model_building_service.types.get_intents_response
    import capo_lex_model_building_service.types.get_migration_request
    import capo_lex_model_building_service.types.get_migration_response
    import capo_lex_model_building_service.types.get_migrations_request
    import capo_lex_model_building_service.types.get_migrations_response
    import capo_lex_model_building_service.types.get_slot_type_request
    import capo_lex_model_building_service.types.get_slot_type_response
    import capo_lex_model_building_service.types.get_slot_type_versions_request
    import capo_lex_model_building_service.types.get_slot_type_versions_response
    import capo_lex_model_building_service.types.get_slot_types_request
    import capo_lex_model_building_service.types.get_slot_types_response
    import capo_lex_model_building_service.types.get_utterances_view_request
    import capo_lex_model_building_service.types.get_utterances_view_response
    import capo_lex_model_building_service.types.iam_role_arn
    import capo_lex_model_building_service.types.input_context_list
    import capo_lex_model_building_service.types.intent_list
    import capo_lex_model_building_service.types.intent_name
    import capo_lex_model_building_service.types.intent_utterance_list
    import capo_lex_model_building_service.types.kendra_configuration
    import capo_lex_model_building_service.types.list_tags_for_resource_request
    import capo_lex_model_building_service.types.list_tags_for_resource_response
    import capo_lex_model_building_service.types.locale
    import capo_lex_model_building_service.types.max_results
    import capo_lex_model_building_service.types.merge_strategy
    import capo_lex_model_building_service.types.migration_id
    import capo_lex_model_building_service.types.migration_sort_attribute
    import capo_lex_model_building_service.types.migration_status
    import capo_lex_model_building_service.types.migration_strategy
    import capo_lex_model_building_service.types.name
    import capo_lex_model_building_service.types.next_token
    import capo_lex_model_building_service.types.numerical_version
    import capo_lex_model_building_service.types.output_context_list
    import capo_lex_model_building_service.types.process_behavior
    import capo_lex_model_building_service.types.prompt
    import capo_lex_model_building_service.types.put_bot_alias_request
    import capo_lex_model_building_service.types.put_bot_alias_response
    import capo_lex_model_building_service.types.put_bot_request
    import capo_lex_model_building_service.types.put_bot_response
    import capo_lex_model_building_service.types.put_intent_request
    import capo_lex_model_building_service.types.put_intent_response
    import capo_lex_model_building_service.types.put_slot_type_request
    import capo_lex_model_building_service.types.put_slot_type_response
    import capo_lex_model_building_service.types.resource_type
    import capo_lex_model_building_service.types.session_ttl
    import capo_lex_model_building_service.types.slot_list
    import capo_lex_model_building_service.types.slot_type_configurations
    import capo_lex_model_building_service.types.slot_type_name
    import capo_lex_model_building_service.types.slot_value_selection_strategy
    import capo_lex_model_building_service.types.sort_order
    import capo_lex_model_building_service.types.start_import_request
    import capo_lex_model_building_service.types.start_import_response
    import capo_lex_model_building_service.types.start_migration_request
    import capo_lex_model_building_service.types.start_migration_response
    import capo_lex_model_building_service.types.statement
    import capo_lex_model_building_service.types.status_type
    import capo_lex_model_building_service.types.string
    import capo_lex_model_building_service.types.tag_key_list
    import capo_lex_model_building_service.types.tag_list
    import capo_lex_model_building_service.types.tag_resource_request
    import capo_lex_model_building_service.types.tag_resource_response
    import capo_lex_model_building_service.types.untag_resource_request
    import capo_lex_model_building_service.types.untag_resource_response
    import capo_lex_model_building_service.types.user_id
    import capo_lex_model_building_service.types.v2_bot_name
    import capo_lex_model_building_service.types.version


class AsyncLexModelBuildingServiceClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None
    anonymous: bool | None


class AsyncLexModelBuildingServiceClient:
    """A client for the ``LexModelBuildingService`` service.

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
        self._config = AsyncLexModelBuildingServiceClientConfig(
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
        self,
        config_overrides: Optional[AsyncLexModelBuildingServiceClientConfig] = None,
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncLexModelBuildingServiceClientConfig = config_overrides or {}
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

    async def create_bot_version(
        self,
        name: "capo_lex_model_building_service.types.bot_name.BotName",
        *,
        config_overrides: Optional[AsyncLexModelBuildingServiceClientConfig] = None,
        checksum: Optional[
            "capo_lex_model_building_service.types.string.String"
        ] = None,
    ) -> "capo_lex_model_building_service.types.create_bot_version_response.CreateBotVersionResponse":
        """<p>Creates a new version of the bot based on the <code>$LATEST</code> version. If the <code>$LATEST</code> version of this resource hasn't changed since you created the last version, Amazon Lex doesn't create a new version. It returns the last created version.</p> <note> <p>You can update only the <code>$LATEST</code> version of the bot. You can't update the numbered versions that you create with the <code>CreateBotVersion</code> operation.</p> </note> <p> When you create the first version of a bot, Amazon Lex sets the version to 1. Subsequent versions increment by 1. For more information, see <a>versioning-intro</a>. </p> <p> This operation requires permission for the <code>lex:CreateBotVersion</code> action. </p>

        Args:
            name: <p>The name of the bot that you want to create a new version of. The name is case sensitive. </p>
            checksum: <p>Identifies a specific revision of the <code>$LATEST</code> version of the bot. If you specify a checksum and the <code>$LATEST</code> version of the bot has a different checksum, a <code>PreconditionFailedException</code> exception is returned and Amazon Lex doesn't publish a new version. If you don't specify a checksum, Amazon Lex publishes the <code>$LATEST</code> version.</p>

        Raises:
            capo_lex_model_building_service.errors.bad_request_exception.BadRequestException: <p>The request is not well formed. For example, a value is invalid or a required field is missing. Check the field values, and try again.</p>
            capo_lex_model_building_service.errors.conflict_exception.ConflictException: <p> There was a conflict processing the request. Try your request again. </p>
            capo_lex_model_building_service.errors.internal_failure_exception.InternalFailureException: <p>An internal Amazon Lex error occurred. Try your request again.</p>
            capo_lex_model_building_service.errors.limit_exceeded_exception.LimitExceededException: <p>The request exceeded a limit. Try your request again.</p>
            capo_lex_model_building_service.errors.not_found_exception.NotFoundException: <p>The resource specified in the request was not found. Check the resource and try again.</p>
            capo_lex_model_building_service.errors.precondition_failed_exception.PreconditionFailedException: <p> The checksum of the resource that you are trying to change does not match the checksum in the request. Check the resource's checksum and try again.</p>
            capo_lex_model_building_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lex_model_building_service.types.create_bot_version_request.CreateBotVersionRequest]",
        ) -> AsyncOperationResponse[
            "capo_lex_model_building_service.types.create_bot_version_response.CreateBotVersionResponse"
        ]:
            import capo_lex_model_building_service._operations.aws_deep_sense_model_building_service.create_bot_version

            (
                output,
                http_response,
            ) = await capo_lex_model_building_service._operations.aws_deep_sense_model_building_service.create_bot_version.async_create_bot_version(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lex_model_building_service.types.create_bot_version_request.CreateBotVersionRequest = {
            "name": name
        }
        if checksum is not None:
            input_["checksum"] = checksum

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_intent_version(
        self,
        name: "capo_lex_model_building_service.types.intent_name.IntentName",
        *,
        config_overrides: Optional[AsyncLexModelBuildingServiceClientConfig] = None,
        checksum: Optional[
            "capo_lex_model_building_service.types.string.String"
        ] = None,
    ) -> "capo_lex_model_building_service.types.create_intent_version_response.CreateIntentVersionResponse":
        """<p>Creates a new version of an intent based on the <code>$LATEST</code> version of the intent. If the <code>$LATEST</code> version of this intent hasn't changed since you last updated it, Amazon Lex doesn't create a new version. It returns the last version you created.</p> <note> <p>You can update only the <code>$LATEST</code> version of the intent. You can't update the numbered versions that you create with the <code>CreateIntentVersion</code> operation.</p> </note> <p> When you create a version of an intent, Amazon Lex sets the version to 1. Subsequent versions increment by 1. For more information, see <a>versioning-intro</a>. </p> <p>This operation requires permissions to perform the <code>lex:CreateIntentVersion</code> action. </p>

        Args:
            name: <p>The name of the intent that you want to create a new version of. The name is case sensitive. </p>
            checksum: <p>Checksum of the <code>$LATEST</code> version of the intent that should be used to create the new version. If you specify a checksum and the <code>$LATEST</code> version of the intent has a different checksum, Amazon Lex returns a <code>PreconditionFailedException</code> exception and doesn't publish a new version. If you don't specify a checksum, Amazon Lex publishes the <code>$LATEST</code> version.</p>

        Raises:
            capo_lex_model_building_service.errors.bad_request_exception.BadRequestException: <p>The request is not well formed. For example, a value is invalid or a required field is missing. Check the field values, and try again.</p>
            capo_lex_model_building_service.errors.conflict_exception.ConflictException: <p> There was a conflict processing the request. Try your request again. </p>
            capo_lex_model_building_service.errors.internal_failure_exception.InternalFailureException: <p>An internal Amazon Lex error occurred. Try your request again.</p>
            capo_lex_model_building_service.errors.limit_exceeded_exception.LimitExceededException: <p>The request exceeded a limit. Try your request again.</p>
            capo_lex_model_building_service.errors.not_found_exception.NotFoundException: <p>The resource specified in the request was not found. Check the resource and try again.</p>
            capo_lex_model_building_service.errors.precondition_failed_exception.PreconditionFailedException: <p> The checksum of the resource that you are trying to change does not match the checksum in the request. Check the resource's checksum and try again.</p>
            capo_lex_model_building_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lex_model_building_service.types.create_intent_version_request.CreateIntentVersionRequest]",
        ) -> AsyncOperationResponse[
            "capo_lex_model_building_service.types.create_intent_version_response.CreateIntentVersionResponse"
        ]:
            import capo_lex_model_building_service._operations.aws_deep_sense_model_building_service.create_intent_version

            (
                output,
                http_response,
            ) = await capo_lex_model_building_service._operations.aws_deep_sense_model_building_service.create_intent_version.async_create_intent_version(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lex_model_building_service.types.create_intent_version_request.CreateIntentVersionRequest = {
            "name": name
        }
        if checksum is not None:
            input_["checksum"] = checksum

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_slot_type_version(
        self,
        name: "capo_lex_model_building_service.types.slot_type_name.SlotTypeName",
        *,
        config_overrides: Optional[AsyncLexModelBuildingServiceClientConfig] = None,
        checksum: Optional[
            "capo_lex_model_building_service.types.string.String"
        ] = None,
    ) -> "capo_lex_model_building_service.types.create_slot_type_version_response.CreateSlotTypeVersionResponse":
        """<p>Creates a new version of a slot type based on the <code>$LATEST</code> version of the specified slot type. If the <code>$LATEST</code> version of this resource has not changed since the last version that you created, Amazon Lex doesn't create a new version. It returns the last version that you created. </p> <note> <p>You can update only the <code>$LATEST</code> version of a slot type. You can't update the numbered versions that you create with the <code>CreateSlotTypeVersion</code> operation.</p> </note> <p>When you create a version of a slot type, Amazon Lex sets the version to 1. Subsequent versions increment by 1. For more information, see <a>versioning-intro</a>. </p> <p>This operation requires permissions for the <code>lex:CreateSlotTypeVersion</code> action.</p>

        Args:
            name: <p>The name of the slot type that you want to create a new version for. The name is case sensitive. </p>
            checksum: <p>Checksum for the <code>$LATEST</code> version of the slot type that you want to publish. If you specify a checksum and the <code>$LATEST</code> version of the slot type has a different checksum, Amazon Lex returns a <code>PreconditionFailedException</code> exception and doesn't publish the new version. If you don't specify a checksum, Amazon Lex publishes the <code>$LATEST</code> version.</p>

        Raises:
            capo_lex_model_building_service.errors.bad_request_exception.BadRequestException: <p>The request is not well formed. For example, a value is invalid or a required field is missing. Check the field values, and try again.</p>
            capo_lex_model_building_service.errors.conflict_exception.ConflictException: <p> There was a conflict processing the request. Try your request again. </p>
            capo_lex_model_building_service.errors.internal_failure_exception.InternalFailureException: <p>An internal Amazon Lex error occurred. Try your request again.</p>
            capo_lex_model_building_service.errors.limit_exceeded_exception.LimitExceededException: <p>The request exceeded a limit. Try your request again.</p>
            capo_lex_model_building_service.errors.not_found_exception.NotFoundException: <p>The resource specified in the request was not found. Check the resource and try again.</p>
            capo_lex_model_building_service.errors.precondition_failed_exception.PreconditionFailedException: <p> The checksum of the resource that you are trying to change does not match the checksum in the request. Check the resource's checksum and try again.</p>
            capo_lex_model_building_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lex_model_building_service.types.create_slot_type_version_request.CreateSlotTypeVersionRequest]",
        ) -> AsyncOperationResponse[
            "capo_lex_model_building_service.types.create_slot_type_version_response.CreateSlotTypeVersionResponse"
        ]:
            import capo_lex_model_building_service._operations.aws_deep_sense_model_building_service.create_slot_type_version

            (
                output,
                http_response,
            ) = await capo_lex_model_building_service._operations.aws_deep_sense_model_building_service.create_slot_type_version.async_create_slot_type_version(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lex_model_building_service.types.create_slot_type_version_request.CreateSlotTypeVersionRequest = {
            "name": name
        }
        if checksum is not None:
            input_["checksum"] = checksum

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_bot(
        self,
        name: "capo_lex_model_building_service.types.bot_name.BotName",
        *,
        config_overrides: Optional[AsyncLexModelBuildingServiceClientConfig] = None,
    ) -> None:
        """<p>Deletes all versions of the bot, including the <code>$LATEST</code> version. To delete a specific version of the bot, use the <a>DeleteBotVersion</a> operation. The <code>DeleteBot</code> operation doesn't immediately remove the bot schema. Instead, it is marked for deletion and removed later.</p> <p>Amazon Lex stores utterances indefinitely for improving the ability of your bot to respond to user inputs. These utterances are not removed when the bot is deleted. To remove the utterances, use the <a>DeleteUtterances</a> operation.</p> <p>If a bot has an alias, you can't delete it. Instead, the <code>DeleteBot</code> operation returns a <code>ResourceInUseException</code> exception that includes a reference to the alias that refers to the bot. To remove the reference to the bot, delete the alias. If you get the same exception again, delete the referring alias until the <code>DeleteBot</code> operation is successful.</p> <p>This operation requires permissions for the <code>lex:DeleteBot</code> action.</p>

        Args:
            name: <p>The name of the bot. The name is case sensitive. </p>

        Raises:
            capo_lex_model_building_service.errors.bad_request_exception.BadRequestException: <p>The request is not well formed. For example, a value is invalid or a required field is missing. Check the field values, and try again.</p>
            capo_lex_model_building_service.errors.conflict_exception.ConflictException: <p> There was a conflict processing the request. Try your request again. </p>
            capo_lex_model_building_service.errors.internal_failure_exception.InternalFailureException: <p>An internal Amazon Lex error occurred. Try your request again.</p>
            capo_lex_model_building_service.errors.limit_exceeded_exception.LimitExceededException: <p>The request exceeded a limit. Try your request again.</p>
            capo_lex_model_building_service.errors.not_found_exception.NotFoundException: <p>The resource specified in the request was not found. Check the resource and try again.</p>
            capo_lex_model_building_service.errors.resource_in_use_exception.ResourceInUseException: <p>The resource that you are attempting to delete is referred to by another resource. Use this information to remove references to the resource that you are trying to delete.</p> <p>The body of the exception contains a JSON object that describes the resource.</p> <p> <code>{ "resourceType": BOT | BOTALIAS | BOTCHANNEL | INTENT,</code> </p> <p> <code>"resourceReference": {</code> </p> <p> <code>"name": <i>string</i>, "version": <i>string</i> } }</code> </p>
            capo_lex_model_building_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lex_model_building_service.types.delete_bot_request.DeleteBotRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_lex_model_building_service._operations.aws_deep_sense_model_building_service.delete_bot

            (
                output,
                http_response,
            ) = await capo_lex_model_building_service._operations.aws_deep_sense_model_building_service.delete_bot.async_delete_bot(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lex_model_building_service.types.delete_bot_request.DeleteBotRequest = {
            "name": name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_bot_alias(
        self,
        name: "capo_lex_model_building_service.types.alias_name.AliasName",
        bot_name: "capo_lex_model_building_service.types.bot_name.BotName",
        *,
        config_overrides: Optional[AsyncLexModelBuildingServiceClientConfig] = None,
    ) -> None:
        """<p>Deletes an alias for the specified bot. </p> <p>You can't delete an alias that is used in the association between a bot and a messaging channel. If an alias is used in a channel association, the <code>DeleteBot</code> operation returns a <code>ResourceInUseException</code> exception that includes a reference to the channel association that refers to the bot. You can remove the reference to the alias by deleting the channel association. If you get the same exception again, delete the referring association until the <code>DeleteBotAlias</code> operation is successful.</p>

        Args:
            name: <p>The name of the alias to delete. The name is case sensitive. </p>
            bot_name: <p>The name of the bot that the alias points to.</p>

        Raises:
            capo_lex_model_building_service.errors.bad_request_exception.BadRequestException: <p>The request is not well formed. For example, a value is invalid or a required field is missing. Check the field values, and try again.</p>
            capo_lex_model_building_service.errors.conflict_exception.ConflictException: <p> There was a conflict processing the request. Try your request again. </p>
            capo_lex_model_building_service.errors.internal_failure_exception.InternalFailureException: <p>An internal Amazon Lex error occurred. Try your request again.</p>
            capo_lex_model_building_service.errors.limit_exceeded_exception.LimitExceededException: <p>The request exceeded a limit. Try your request again.</p>
            capo_lex_model_building_service.errors.not_found_exception.NotFoundException: <p>The resource specified in the request was not found. Check the resource and try again.</p>
            capo_lex_model_building_service.errors.resource_in_use_exception.ResourceInUseException: <p>The resource that you are attempting to delete is referred to by another resource. Use this information to remove references to the resource that you are trying to delete.</p> <p>The body of the exception contains a JSON object that describes the resource.</p> <p> <code>{ "resourceType": BOT | BOTALIAS | BOTCHANNEL | INTENT,</code> </p> <p> <code>"resourceReference": {</code> </p> <p> <code>"name": <i>string</i>, "version": <i>string</i> } }</code> </p>
            capo_lex_model_building_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lex_model_building_service.types.delete_bot_alias_request.DeleteBotAliasRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_lex_model_building_service._operations.aws_deep_sense_model_building_service.delete_bot_alias

            (
                output,
                http_response,
            ) = await capo_lex_model_building_service._operations.aws_deep_sense_model_building_service.delete_bot_alias.async_delete_bot_alias(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lex_model_building_service.types.delete_bot_alias_request.DeleteBotAliasRequest = {
            "name": name,
            "bot_name": bot_name,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_bot_channel_association(
        self,
        name: "capo_lex_model_building_service.types.bot_channel_name.BotChannelName",
        bot_name: "capo_lex_model_building_service.types.bot_name.BotName",
        bot_alias: "capo_lex_model_building_service.types.alias_name.AliasName",
        *,
        config_overrides: Optional[AsyncLexModelBuildingServiceClientConfig] = None,
    ) -> None:
        """<p>Deletes the association between an Amazon Lex bot and a messaging platform.</p> <p>This operation requires permission for the <code>lex:DeleteBotChannelAssociation</code> action.</p>

        Args:
            name: <p>The name of the association. The name is case sensitive. </p>
            bot_name: <p>The name of the Amazon Lex bot.</p>
            bot_alias: <p>An alias that points to the specific version of the Amazon Lex bot to which this association is being made.</p>

        Raises:
            capo_lex_model_building_service.errors.bad_request_exception.BadRequestException: <p>The request is not well formed. For example, a value is invalid or a required field is missing. Check the field values, and try again.</p>
            capo_lex_model_building_service.errors.conflict_exception.ConflictException: <p> There was a conflict processing the request. Try your request again. </p>
            capo_lex_model_building_service.errors.internal_failure_exception.InternalFailureException: <p>An internal Amazon Lex error occurred. Try your request again.</p>
            capo_lex_model_building_service.errors.limit_exceeded_exception.LimitExceededException: <p>The request exceeded a limit. Try your request again.</p>
            capo_lex_model_building_service.errors.not_found_exception.NotFoundException: <p>The resource specified in the request was not found. Check the resource and try again.</p>
            capo_lex_model_building_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lex_model_building_service.types.delete_bot_channel_association_request.DeleteBotChannelAssociationRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_lex_model_building_service._operations.aws_deep_sense_model_building_service.delete_bot_channel_association

            (
                output,
                http_response,
            ) = await capo_lex_model_building_service._operations.aws_deep_sense_model_building_service.delete_bot_channel_association.async_delete_bot_channel_association(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lex_model_building_service.types.delete_bot_channel_association_request.DeleteBotChannelAssociationRequest = {
            "name": name,
            "bot_name": bot_name,
            "bot_alias": bot_alias,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_bot_version(
        self,
        name: "capo_lex_model_building_service.types.bot_name.BotName",
        version: "capo_lex_model_building_service.types.numerical_version.NumericalVersion",
        *,
        config_overrides: Optional[AsyncLexModelBuildingServiceClientConfig] = None,
    ) -> None:
        """<p>Deletes a specific version of a bot. To delete all versions of a bot, use the <a>DeleteBot</a> operation. </p> <p>This operation requires permissions for the <code>lex:DeleteBotVersion</code> action.</p>

        Args:
            name: <p>The name of the bot.</p>
            version: <p>The version of the bot to delete. You cannot delete the <code>$LATEST</code> version of the bot. To delete the <code>$LATEST</code> version, use the <a>DeleteBot</a> operation.</p>

        Raises:
            capo_lex_model_building_service.errors.bad_request_exception.BadRequestException: <p>The request is not well formed. For example, a value is invalid or a required field is missing. Check the field values, and try again.</p>
            capo_lex_model_building_service.errors.conflict_exception.ConflictException: <p> There was a conflict processing the request. Try your request again. </p>
            capo_lex_model_building_service.errors.internal_failure_exception.InternalFailureException: <p>An internal Amazon Lex error occurred. Try your request again.</p>
            capo_lex_model_building_service.errors.limit_exceeded_exception.LimitExceededException: <p>The request exceeded a limit. Try your request again.</p>
            capo_lex_model_building_service.errors.not_found_exception.NotFoundException: <p>The resource specified in the request was not found. Check the resource and try again.</p>
            capo_lex_model_building_service.errors.resource_in_use_exception.ResourceInUseException: <p>The resource that you are attempting to delete is referred to by another resource. Use this information to remove references to the resource that you are trying to delete.</p> <p>The body of the exception contains a JSON object that describes the resource.</p> <p> <code>{ "resourceType": BOT | BOTALIAS | BOTCHANNEL | INTENT,</code> </p> <p> <code>"resourceReference": {</code> </p> <p> <code>"name": <i>string</i>, "version": <i>string</i> } }</code> </p>
            capo_lex_model_building_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lex_model_building_service.types.delete_bot_version_request.DeleteBotVersionRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_lex_model_building_service._operations.aws_deep_sense_model_building_service.delete_bot_version

            (
                output,
                http_response,
            ) = await capo_lex_model_building_service._operations.aws_deep_sense_model_building_service.delete_bot_version.async_delete_bot_version(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lex_model_building_service.types.delete_bot_version_request.DeleteBotVersionRequest = {
            "name": name,
            "version": version,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_intent(
        self,
        name: "capo_lex_model_building_service.types.intent_name.IntentName",
        *,
        config_overrides: Optional[AsyncLexModelBuildingServiceClientConfig] = None,
    ) -> None:
        """<p>Deletes all versions of the intent, including the <code>$LATEST</code> version. To delete a specific version of the intent, use the <a>DeleteIntentVersion</a> operation.</p> <p> You can delete a version of an intent only if it is not referenced. To delete an intent that is referred to in one or more bots (see <a>how-it-works</a>), you must remove those references first. </p> <note> <p> If you get the <code>ResourceInUseException</code> exception, it provides an example reference that shows where the intent is referenced. To remove the reference to the intent, either update the bot or delete it. If you get the same exception when you attempt to delete the intent again, repeat until the intent has no references and the call to <code>DeleteIntent</code> is successful. </p> </note> <p> This operation requires permission for the <code>lex:DeleteIntent</code> action. </p>

        Args:
            name: <p>The name of the intent. The name is case sensitive. </p>

        Raises:
            capo_lex_model_building_service.errors.bad_request_exception.BadRequestException: <p>The request is not well formed. For example, a value is invalid or a required field is missing. Check the field values, and try again.</p>
            capo_lex_model_building_service.errors.conflict_exception.ConflictException: <p> There was a conflict processing the request. Try your request again. </p>
            capo_lex_model_building_service.errors.internal_failure_exception.InternalFailureException: <p>An internal Amazon Lex error occurred. Try your request again.</p>
            capo_lex_model_building_service.errors.limit_exceeded_exception.LimitExceededException: <p>The request exceeded a limit. Try your request again.</p>
            capo_lex_model_building_service.errors.not_found_exception.NotFoundException: <p>The resource specified in the request was not found. Check the resource and try again.</p>
            capo_lex_model_building_service.errors.resource_in_use_exception.ResourceInUseException: <p>The resource that you are attempting to delete is referred to by another resource. Use this information to remove references to the resource that you are trying to delete.</p> <p>The body of the exception contains a JSON object that describes the resource.</p> <p> <code>{ "resourceType": BOT | BOTALIAS | BOTCHANNEL | INTENT,</code> </p> <p> <code>"resourceReference": {</code> </p> <p> <code>"name": <i>string</i>, "version": <i>string</i> } }</code> </p>
            capo_lex_model_building_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lex_model_building_service.types.delete_intent_request.DeleteIntentRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_lex_model_building_service._operations.aws_deep_sense_model_building_service.delete_intent

            (
                output,
                http_response,
            ) = await capo_lex_model_building_service._operations.aws_deep_sense_model_building_service.delete_intent.async_delete_intent(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lex_model_building_service.types.delete_intent_request.DeleteIntentRequest = {
            "name": name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_intent_version(
        self,
        name: "capo_lex_model_building_service.types.intent_name.IntentName",
        version: "capo_lex_model_building_service.types.numerical_version.NumericalVersion",
        *,
        config_overrides: Optional[AsyncLexModelBuildingServiceClientConfig] = None,
    ) -> None:
        """<p>Deletes a specific version of an intent. To delete all versions of a intent, use the <a>DeleteIntent</a> operation. </p> <p>This operation requires permissions for the <code>lex:DeleteIntentVersion</code> action.</p>

        Args:
            name: <p>The name of the intent.</p>
            version: <p>The version of the intent to delete. You cannot delete the <code>$LATEST</code> version of the intent. To delete the <code>$LATEST</code> version, use the <a>DeleteIntent</a> operation.</p>

        Raises:
            capo_lex_model_building_service.errors.bad_request_exception.BadRequestException: <p>The request is not well formed. For example, a value is invalid or a required field is missing. Check the field values, and try again.</p>
            capo_lex_model_building_service.errors.conflict_exception.ConflictException: <p> There was a conflict processing the request. Try your request again. </p>
            capo_lex_model_building_service.errors.internal_failure_exception.InternalFailureException: <p>An internal Amazon Lex error occurred. Try your request again.</p>
            capo_lex_model_building_service.errors.limit_exceeded_exception.LimitExceededException: <p>The request exceeded a limit. Try your request again.</p>
            capo_lex_model_building_service.errors.not_found_exception.NotFoundException: <p>The resource specified in the request was not found. Check the resource and try again.</p>
            capo_lex_model_building_service.errors.resource_in_use_exception.ResourceInUseException: <p>The resource that you are attempting to delete is referred to by another resource. Use this information to remove references to the resource that you are trying to delete.</p> <p>The body of the exception contains a JSON object that describes the resource.</p> <p> <code>{ "resourceType": BOT | BOTALIAS | BOTCHANNEL | INTENT,</code> </p> <p> <code>"resourceReference": {</code> </p> <p> <code>"name": <i>string</i>, "version": <i>string</i> } }</code> </p>
            capo_lex_model_building_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lex_model_building_service.types.delete_intent_version_request.DeleteIntentVersionRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_lex_model_building_service._operations.aws_deep_sense_model_building_service.delete_intent_version

            (
                output,
                http_response,
            ) = await capo_lex_model_building_service._operations.aws_deep_sense_model_building_service.delete_intent_version.async_delete_intent_version(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lex_model_building_service.types.delete_intent_version_request.DeleteIntentVersionRequest = {
            "name": name,
            "version": version,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_slot_type(
        self,
        name: "capo_lex_model_building_service.types.slot_type_name.SlotTypeName",
        *,
        config_overrides: Optional[AsyncLexModelBuildingServiceClientConfig] = None,
    ) -> None:
        """<p>Deletes all versions of the slot type, including the <code>$LATEST</code> version. To delete a specific version of the slot type, use the <a>DeleteSlotTypeVersion</a> operation.</p> <p> You can delete a version of a slot type only if it is not referenced. To delete a slot type that is referred to in one or more intents, you must remove those references first. </p> <note> <p> If you get the <code>ResourceInUseException</code> exception, the exception provides an example reference that shows the intent where the slot type is referenced. To remove the reference to the slot type, either update the intent or delete it. If you get the same exception when you attempt to delete the slot type again, repeat until the slot type has no references and the <code>DeleteSlotType</code> call is successful. </p> </note> <p>This operation requires permission for the <code>lex:DeleteSlotType</code> action.</p>

        Args:
            name: <p>The name of the slot type. The name is case sensitive. </p>

        Raises:
            capo_lex_model_building_service.errors.bad_request_exception.BadRequestException: <p>The request is not well formed. For example, a value is invalid or a required field is missing. Check the field values, and try again.</p>
            capo_lex_model_building_service.errors.conflict_exception.ConflictException: <p> There was a conflict processing the request. Try your request again. </p>
            capo_lex_model_building_service.errors.internal_failure_exception.InternalFailureException: <p>An internal Amazon Lex error occurred. Try your request again.</p>
            capo_lex_model_building_service.errors.limit_exceeded_exception.LimitExceededException: <p>The request exceeded a limit. Try your request again.</p>
            capo_lex_model_building_service.errors.not_found_exception.NotFoundException: <p>The resource specified in the request was not found. Check the resource and try again.</p>
            capo_lex_model_building_service.errors.resource_in_use_exception.ResourceInUseException: <p>The resource that you are attempting to delete is referred to by another resource. Use this information to remove references to the resource that you are trying to delete.</p> <p>The body of the exception contains a JSON object that describes the resource.</p> <p> <code>{ "resourceType": BOT | BOTALIAS | BOTCHANNEL | INTENT,</code> </p> <p> <code>"resourceReference": {</code> </p> <p> <code>"name": <i>string</i>, "version": <i>string</i> } }</code> </p>
            capo_lex_model_building_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lex_model_building_service.types.delete_slot_type_request.DeleteSlotTypeRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_lex_model_building_service._operations.aws_deep_sense_model_building_service.delete_slot_type

            (
                output,
                http_response,
            ) = await capo_lex_model_building_service._operations.aws_deep_sense_model_building_service.delete_slot_type.async_delete_slot_type(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lex_model_building_service.types.delete_slot_type_request.DeleteSlotTypeRequest = {
            "name": name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_slot_type_version(
        self,
        name: "capo_lex_model_building_service.types.slot_type_name.SlotTypeName",
        version: "capo_lex_model_building_service.types.numerical_version.NumericalVersion",
        *,
        config_overrides: Optional[AsyncLexModelBuildingServiceClientConfig] = None,
    ) -> None:
        """<p>Deletes a specific version of a slot type. To delete all versions of a slot type, use the <a>DeleteSlotType</a> operation. </p> <p>This operation requires permissions for the <code>lex:DeleteSlotTypeVersion</code> action.</p>

        Args:
            name: <p>The name of the slot type.</p>
            version: <p>The version of the slot type to delete. You cannot delete the <code>$LATEST</code> version of the slot type. To delete the <code>$LATEST</code> version, use the <a>DeleteSlotType</a> operation.</p>

        Raises:
            capo_lex_model_building_service.errors.bad_request_exception.BadRequestException: <p>The request is not well formed. For example, a value is invalid or a required field is missing. Check the field values, and try again.</p>
            capo_lex_model_building_service.errors.conflict_exception.ConflictException: <p> There was a conflict processing the request. Try your request again. </p>
            capo_lex_model_building_service.errors.internal_failure_exception.InternalFailureException: <p>An internal Amazon Lex error occurred. Try your request again.</p>
            capo_lex_model_building_service.errors.limit_exceeded_exception.LimitExceededException: <p>The request exceeded a limit. Try your request again.</p>
            capo_lex_model_building_service.errors.not_found_exception.NotFoundException: <p>The resource specified in the request was not found. Check the resource and try again.</p>
            capo_lex_model_building_service.errors.resource_in_use_exception.ResourceInUseException: <p>The resource that you are attempting to delete is referred to by another resource. Use this information to remove references to the resource that you are trying to delete.</p> <p>The body of the exception contains a JSON object that describes the resource.</p> <p> <code>{ "resourceType": BOT | BOTALIAS | BOTCHANNEL | INTENT,</code> </p> <p> <code>"resourceReference": {</code> </p> <p> <code>"name": <i>string</i>, "version": <i>string</i> } }</code> </p>
            capo_lex_model_building_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lex_model_building_service.types.delete_slot_type_version_request.DeleteSlotTypeVersionRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_lex_model_building_service._operations.aws_deep_sense_model_building_service.delete_slot_type_version

            (
                output,
                http_response,
            ) = await capo_lex_model_building_service._operations.aws_deep_sense_model_building_service.delete_slot_type_version.async_delete_slot_type_version(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lex_model_building_service.types.delete_slot_type_version_request.DeleteSlotTypeVersionRequest = {
            "name": name,
            "version": version,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_utterances(
        self,
        bot_name: "capo_lex_model_building_service.types.bot_name.BotName",
        user_id: "capo_lex_model_building_service.types.user_id.UserId",
        *,
        config_overrides: Optional[AsyncLexModelBuildingServiceClientConfig] = None,
    ) -> None:
        """<p>Deletes stored utterances.</p> <p>Amazon Lex stores the utterances that users send to your bot. Utterances are stored for 15 days for use with the <a>GetUtterancesView</a> operation, and then stored indefinitely for use in improving the ability of your bot to respond to user input.</p> <p>Use the <code>DeleteUtterances</code> operation to manually delete stored utterances for a specific user. When you use the <code>DeleteUtterances</code> operation, utterances stored for improving your bot's ability to respond to user input are deleted immediately. Utterances stored for use with the <code>GetUtterancesView</code> operation are deleted after 15 days.</p> <p>This operation requires permissions for the <code>lex:DeleteUtterances</code> action.</p>

        Args:
            bot_name: <p>The name of the bot that stored the utterances.</p>
            user_id: <p> The unique identifier for the user that made the utterances. This is the user ID that was sent in the <a href="http://docs.aws.amazon.com/lex/latest/dg/API_runtime_PostContent.html">PostContent</a> or <a href="http://docs.aws.amazon.com/lex/latest/dg/API_runtime_PostText.html">PostText</a> operation request that contained the utterance.</p>

        Raises:
            capo_lex_model_building_service.errors.bad_request_exception.BadRequestException: <p>The request is not well formed. For example, a value is invalid or a required field is missing. Check the field values, and try again.</p>
            capo_lex_model_building_service.errors.internal_failure_exception.InternalFailureException: <p>An internal Amazon Lex error occurred. Try your request again.</p>
            capo_lex_model_building_service.errors.limit_exceeded_exception.LimitExceededException: <p>The request exceeded a limit. Try your request again.</p>
            capo_lex_model_building_service.errors.not_found_exception.NotFoundException: <p>The resource specified in the request was not found. Check the resource and try again.</p>
            capo_lex_model_building_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lex_model_building_service.types.delete_utterances_request.DeleteUtterancesRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_lex_model_building_service._operations.aws_deep_sense_model_building_service.delete_utterances

            (
                output,
                http_response,
            ) = await capo_lex_model_building_service._operations.aws_deep_sense_model_building_service.delete_utterances.async_delete_utterances(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lex_model_building_service.types.delete_utterances_request.DeleteUtterancesRequest = {
            "bot_name": bot_name,
            "user_id": user_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_bot(
        self,
        name: "capo_lex_model_building_service.types.bot_name.BotName",
        version_or_alias: "capo_lex_model_building_service.types.string.String",
        *,
        config_overrides: Optional[AsyncLexModelBuildingServiceClientConfig] = None,
    ) -> "capo_lex_model_building_service.types.get_bot_response.GetBotResponse":
        """<p>Returns metadata information for a specific bot. You must provide the bot name and the bot version or alias. </p> <p> This operation requires permissions for the <code>lex:GetBot</code> action. </p>

        Args:
            name: <p>The name of the bot. The name is case sensitive. </p>
            version_or_alias: <p>The version or alias of the bot.</p>

        Raises:
            capo_lex_model_building_service.errors.bad_request_exception.BadRequestException: <p>The request is not well formed. For example, a value is invalid or a required field is missing. Check the field values, and try again.</p>
            capo_lex_model_building_service.errors.internal_failure_exception.InternalFailureException: <p>An internal Amazon Lex error occurred. Try your request again.</p>
            capo_lex_model_building_service.errors.limit_exceeded_exception.LimitExceededException: <p>The request exceeded a limit. Try your request again.</p>
            capo_lex_model_building_service.errors.not_found_exception.NotFoundException: <p>The resource specified in the request was not found. Check the resource and try again.</p>
            capo_lex_model_building_service.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To get information about a bot
            This example shows how to get configuration information for a bot.

            >>> await client.get_bot(name='DocOrderPizza', version_or_alias='$LATEST')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lex_model_building_service.types.get_bot_request.GetBotRequest]",
        ) -> AsyncOperationResponse[
            "capo_lex_model_building_service.types.get_bot_response.GetBotResponse"
        ]:
            import capo_lex_model_building_service._operations.aws_deep_sense_model_building_service.get_bot

            (
                output,
                http_response,
            ) = await capo_lex_model_building_service._operations.aws_deep_sense_model_building_service.get_bot.async_get_bot(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lex_model_building_service.types.get_bot_request.GetBotRequest = {
            "name": name,
            "version_or_alias": version_or_alias,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_bot_alias(
        self,
        name: "capo_lex_model_building_service.types.alias_name.AliasName",
        bot_name: "capo_lex_model_building_service.types.bot_name.BotName",
        *,
        config_overrides: Optional[AsyncLexModelBuildingServiceClientConfig] = None,
    ) -> "capo_lex_model_building_service.types.get_bot_alias_response.GetBotAliasResponse":
        """<p>Returns information about an Amazon Lex bot alias. For more information about aliases, see <a>versioning-aliases</a>.</p> <p>This operation requires permissions for the <code>lex:GetBotAlias</code> action.</p>

        Args:
            name: <p>The name of the bot alias. The name is case sensitive.</p>
            bot_name: <p>The name of the bot.</p>

        Raises:
            capo_lex_model_building_service.errors.bad_request_exception.BadRequestException: <p>The request is not well formed. For example, a value is invalid or a required field is missing. Check the field values, and try again.</p>
            capo_lex_model_building_service.errors.internal_failure_exception.InternalFailureException: <p>An internal Amazon Lex error occurred. Try your request again.</p>
            capo_lex_model_building_service.errors.limit_exceeded_exception.LimitExceededException: <p>The request exceeded a limit. Try your request again.</p>
            capo_lex_model_building_service.errors.not_found_exception.NotFoundException: <p>The resource specified in the request was not found. Check the resource and try again.</p>
            capo_lex_model_building_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lex_model_building_service.types.get_bot_alias_request.GetBotAliasRequest]",
        ) -> AsyncOperationResponse[
            "capo_lex_model_building_service.types.get_bot_alias_response.GetBotAliasResponse"
        ]:
            import capo_lex_model_building_service._operations.aws_deep_sense_model_building_service.get_bot_alias

            (
                output,
                http_response,
            ) = await capo_lex_model_building_service._operations.aws_deep_sense_model_building_service.get_bot_alias.async_get_bot_alias(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lex_model_building_service.types.get_bot_alias_request.GetBotAliasRequest = {
            "name": name,
            "bot_name": bot_name,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_bot_aliases(
        self,
        bot_name: "capo_lex_model_building_service.types.bot_name.BotName",
        *,
        config_overrides: Optional[AsyncLexModelBuildingServiceClientConfig] = None,
        next_token: Optional[
            "capo_lex_model_building_service.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "capo_lex_model_building_service.types.max_results.MaxResults"
        ] = None,
        name_contains: Optional[
            "capo_lex_model_building_service.types.alias_name.AliasName"
        ] = None,
    ) -> "capo_lex_model_building_service.types.get_bot_aliases_response.GetBotAliasesResponse":
        """<p>Returns a list of aliases for a specified Amazon Lex bot.</p> <p>This operation requires permissions for the <code>lex:GetBotAliases</code> action.</p>

        Args:
            bot_name: <p>The name of the bot.</p>
            next_token: <p>A pagination token for fetching the next page of aliases. If the response to this call is truncated, Amazon Lex returns a pagination token in the response. To fetch the next page of aliases, specify the pagination token in the next request. </p>
            max_results: <p>The maximum number of aliases to return in the response. The default is 50. . </p>
            name_contains: <p>Substring to match in bot alias names. An alias will be returned if any part of its name matches the substring. For example, "xyz" matches both "xyzabc" and "abcxyz."</p>

        Raises:
            capo_lex_model_building_service.errors.bad_request_exception.BadRequestException: <p>The request is not well formed. For example, a value is invalid or a required field is missing. Check the field values, and try again.</p>
            capo_lex_model_building_service.errors.internal_failure_exception.InternalFailureException: <p>An internal Amazon Lex error occurred. Try your request again.</p>
            capo_lex_model_building_service.errors.limit_exceeded_exception.LimitExceededException: <p>The request exceeded a limit. Try your request again.</p>
            capo_lex_model_building_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lex_model_building_service.types.get_bot_aliases_request.GetBotAliasesRequest]",
        ) -> AsyncOperationResponse[
            "capo_lex_model_building_service.types.get_bot_aliases_response.GetBotAliasesResponse"
        ]:
            import capo_lex_model_building_service._operations.aws_deep_sense_model_building_service.get_bot_aliases

            (
                output,
                http_response,
            ) = await capo_lex_model_building_service._operations.aws_deep_sense_model_building_service.get_bot_aliases.async_get_bot_aliases(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lex_model_building_service.types.get_bot_aliases_request.GetBotAliasesRequest = {
            "bot_name": bot_name
        }
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if name_contains is not None:
            input_["name_contains"] = name_contains

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_get_bot_aliases(
        self,
        bot_name: "capo_lex_model_building_service.types.bot_name.BotName",
        *,
        config_overrides: Optional[AsyncLexModelBuildingServiceClientConfig] = None,
        next_token: Optional[
            "capo_lex_model_building_service.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "capo_lex_model_building_service.types.max_results.MaxResults"
        ] = None,
        name_contains: Optional[
            "capo_lex_model_building_service.types.alias_name.AliasName"
        ] = None,
    ) -> "AsyncIterator[capo_lex_model_building_service.types.get_bot_aliases_response.GetBotAliasesResponse]":
        _token = next_token
        while True:
            _response = await self.get_bot_aliases(
                bot_name,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
                name_contains=name_contains,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def get_bot_channel_association(
        self,
        name: "capo_lex_model_building_service.types.bot_channel_name.BotChannelName",
        bot_name: "capo_lex_model_building_service.types.bot_name.BotName",
        bot_alias: "capo_lex_model_building_service.types.alias_name.AliasName",
        *,
        config_overrides: Optional[AsyncLexModelBuildingServiceClientConfig] = None,
    ) -> "capo_lex_model_building_service.types.get_bot_channel_association_response.GetBotChannelAssociationResponse":
        """<p>Returns information about the association between an Amazon Lex bot and a messaging platform.</p> <p>This operation requires permissions for the <code>lex:GetBotChannelAssociation</code> action.</p>

        Args:
            name: <p>The name of the association between the bot and the channel. The name is case sensitive. </p>
            bot_name: <p>The name of the Amazon Lex bot.</p>
            bot_alias: <p>An alias pointing to the specific version of the Amazon Lex bot to which this association is being made.</p>

        Raises:
            capo_lex_model_building_service.errors.bad_request_exception.BadRequestException: <p>The request is not well formed. For example, a value is invalid or a required field is missing. Check the field values, and try again.</p>
            capo_lex_model_building_service.errors.internal_failure_exception.InternalFailureException: <p>An internal Amazon Lex error occurred. Try your request again.</p>
            capo_lex_model_building_service.errors.limit_exceeded_exception.LimitExceededException: <p>The request exceeded a limit. Try your request again.</p>
            capo_lex_model_building_service.errors.not_found_exception.NotFoundException: <p>The resource specified in the request was not found. Check the resource and try again.</p>
            capo_lex_model_building_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lex_model_building_service.types.get_bot_channel_association_request.GetBotChannelAssociationRequest]",
        ) -> AsyncOperationResponse[
            "capo_lex_model_building_service.types.get_bot_channel_association_response.GetBotChannelAssociationResponse"
        ]:
            import capo_lex_model_building_service._operations.aws_deep_sense_model_building_service.get_bot_channel_association

            (
                output,
                http_response,
            ) = await capo_lex_model_building_service._operations.aws_deep_sense_model_building_service.get_bot_channel_association.async_get_bot_channel_association(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lex_model_building_service.types.get_bot_channel_association_request.GetBotChannelAssociationRequest = {
            "name": name,
            "bot_name": bot_name,
            "bot_alias": bot_alias,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_bot_channel_associations(
        self,
        bot_name: "capo_lex_model_building_service.types.bot_name.BotName",
        bot_alias: "capo_lex_model_building_service.types.alias_name_or_list_all.AliasNameOrListAll",
        *,
        config_overrides: Optional[AsyncLexModelBuildingServiceClientConfig] = None,
        next_token: Optional[
            "capo_lex_model_building_service.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "capo_lex_model_building_service.types.max_results.MaxResults"
        ] = None,
        name_contains: Optional[
            "capo_lex_model_building_service.types.bot_channel_name.BotChannelName"
        ] = None,
    ) -> "capo_lex_model_building_service.types.get_bot_channel_associations_response.GetBotChannelAssociationsResponse":
        """<p> Returns a list of all of the channels associated with the specified bot. </p> <p>The <code>GetBotChannelAssociations</code> operation requires permissions for the <code>lex:GetBotChannelAssociations</code> action.</p>

        Args:
            bot_name: <p>The name of the Amazon Lex bot in the association.</p>
            bot_alias: <p>An alias pointing to the specific version of the Amazon Lex bot to which this association is being made.</p>
            next_token: <p>A pagination token for fetching the next page of associations. If the response to this call is truncated, Amazon Lex returns a pagination token in the response. To fetch the next page of associations, specify the pagination token in the next request. </p>
            max_results: <p>The maximum number of associations to return in the response. The default is 50. </p>
            name_contains: <p>Substring to match in channel association names. An association will be returned if any part of its name matches the substring. For example, "xyz" matches both "xyzabc" and "abcxyz." To return all bot channel associations, use a hyphen ("-") as the <code>nameContains</code> parameter.</p>

        Raises:
            capo_lex_model_building_service.errors.bad_request_exception.BadRequestException: <p>The request is not well formed. For example, a value is invalid or a required field is missing. Check the field values, and try again.</p>
            capo_lex_model_building_service.errors.internal_failure_exception.InternalFailureException: <p>An internal Amazon Lex error occurred. Try your request again.</p>
            capo_lex_model_building_service.errors.limit_exceeded_exception.LimitExceededException: <p>The request exceeded a limit. Try your request again.</p>
            capo_lex_model_building_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lex_model_building_service.types.get_bot_channel_associations_request.GetBotChannelAssociationsRequest]",
        ) -> AsyncOperationResponse[
            "capo_lex_model_building_service.types.get_bot_channel_associations_response.GetBotChannelAssociationsResponse"
        ]:
            import capo_lex_model_building_service._operations.aws_deep_sense_model_building_service.get_bot_channel_associations

            (
                output,
                http_response,
            ) = await capo_lex_model_building_service._operations.aws_deep_sense_model_building_service.get_bot_channel_associations.async_get_bot_channel_associations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lex_model_building_service.types.get_bot_channel_associations_request.GetBotChannelAssociationsRequest = {
            "bot_name": bot_name,
            "bot_alias": bot_alias,
        }
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if name_contains is not None:
            input_["name_contains"] = name_contains

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_get_bot_channel_associations(
        self,
        bot_name: "capo_lex_model_building_service.types.bot_name.BotName",
        bot_alias: "capo_lex_model_building_service.types.alias_name_or_list_all.AliasNameOrListAll",
        *,
        config_overrides: Optional[AsyncLexModelBuildingServiceClientConfig] = None,
        next_token: Optional[
            "capo_lex_model_building_service.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "capo_lex_model_building_service.types.max_results.MaxResults"
        ] = None,
        name_contains: Optional[
            "capo_lex_model_building_service.types.bot_channel_name.BotChannelName"
        ] = None,
    ) -> "AsyncIterator[capo_lex_model_building_service.types.get_bot_channel_associations_response.GetBotChannelAssociationsResponse]":
        _token = next_token
        while True:
            _response = await self.get_bot_channel_associations(
                bot_name,
                bot_alias,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
                name_contains=name_contains,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def get_bots(
        self,
        *,
        config_overrides: Optional[AsyncLexModelBuildingServiceClientConfig] = None,
        next_token: Optional[
            "capo_lex_model_building_service.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "capo_lex_model_building_service.types.max_results.MaxResults"
        ] = None,
        name_contains: Optional[
            "capo_lex_model_building_service.types.bot_name.BotName"
        ] = None,
    ) -> "capo_lex_model_building_service.types.get_bots_response.GetBotsResponse":
        """<p>Returns bot information as follows: </p> <ul> <li> <p>If you provide the <code>nameContains</code> field, the response includes information for the <code>$LATEST</code> version of all bots whose name contains the specified string.</p> </li> <li> <p>If you don't specify the <code>nameContains</code> field, the operation returns information about the <code>$LATEST</code> version of all of your bots.</p> </li> </ul> <p>This operation requires permission for the <code>lex:GetBots</code> action.</p>

        Args:
            next_token: <p>A pagination token that fetches the next page of bots. If the response to this call is truncated, Amazon Lex returns a pagination token in the response. To fetch the next page of bots, specify the pagination token in the next request. </p>
            max_results: <p>The maximum number of bots to return in the response that the request will return. The default is 10.</p>
            name_contains: <p>Substring to match in bot names. A bot will be returned if any part of its name matches the substring. For example, "xyz" matches both "xyzabc" and "abcxyz."</p>

        Raises:
            capo_lex_model_building_service.errors.bad_request_exception.BadRequestException: <p>The request is not well formed. For example, a value is invalid or a required field is missing. Check the field values, and try again.</p>
            capo_lex_model_building_service.errors.internal_failure_exception.InternalFailureException: <p>An internal Amazon Lex error occurred. Try your request again.</p>
            capo_lex_model_building_service.errors.limit_exceeded_exception.LimitExceededException: <p>The request exceeded a limit. Try your request again.</p>
            capo_lex_model_building_service.errors.not_found_exception.NotFoundException: <p>The resource specified in the request was not found. Check the resource and try again.</p>
            capo_lex_model_building_service.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To get a list of bots
            This example shows how to get a list of all of the bots in your account.

            >>> await client.get_bots(next_token='', max_results=5)
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lex_model_building_service.types.get_bots_request.GetBotsRequest]",
        ) -> AsyncOperationResponse[
            "capo_lex_model_building_service.types.get_bots_response.GetBotsResponse"
        ]:
            import capo_lex_model_building_service._operations.aws_deep_sense_model_building_service.get_bots

            (
                output,
                http_response,
            ) = await capo_lex_model_building_service._operations.aws_deep_sense_model_building_service.get_bots.async_get_bots(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lex_model_building_service.types.get_bots_request.GetBotsRequest = {}
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if name_contains is not None:
            input_["name_contains"] = name_contains

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_get_bots(
        self,
        *,
        config_overrides: Optional[AsyncLexModelBuildingServiceClientConfig] = None,
        next_token: Optional[
            "capo_lex_model_building_service.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "capo_lex_model_building_service.types.max_results.MaxResults"
        ] = None,
        name_contains: Optional[
            "capo_lex_model_building_service.types.bot_name.BotName"
        ] = None,
    ) -> "AsyncIterator[capo_lex_model_building_service.types.get_bots_response.GetBotsResponse]":
        _token = next_token
        while True:
            _response = await self.get_bots(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
                name_contains=name_contains,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def get_bot_versions(
        self,
        name: "capo_lex_model_building_service.types.bot_name.BotName",
        *,
        config_overrides: Optional[AsyncLexModelBuildingServiceClientConfig] = None,
        next_token: Optional[
            "capo_lex_model_building_service.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "capo_lex_model_building_service.types.max_results.MaxResults"
        ] = None,
    ) -> "capo_lex_model_building_service.types.get_bot_versions_response.GetBotVersionsResponse":
        """<p>Gets information about all of the versions of a bot.</p> <p>The <code>GetBotVersions</code> operation returns a <code>BotMetadata</code> object for each version of a bot. For example, if a bot has three numbered versions, the <code>GetBotVersions</code> operation returns four <code>BotMetadata</code> objects in the response, one for each numbered version and one for the <code>$LATEST</code> version. </p> <p>The <code>GetBotVersions</code> operation always returns at least one version, the <code>$LATEST</code> version.</p> <p>This operation requires permissions for the <code>lex:GetBotVersions</code> action.</p>

        Args:
            name: <p>The name of the bot for which versions should be returned.</p>
            next_token: <p>A pagination token for fetching the next page of bot versions. If the response to this call is truncated, Amazon Lex returns a pagination token in the response. To fetch the next page of versions, specify the pagination token in the next request. </p>
            max_results: <p>The maximum number of bot versions to return in the response. The default is 10.</p>

        Raises:
            capo_lex_model_building_service.errors.bad_request_exception.BadRequestException: <p>The request is not well formed. For example, a value is invalid or a required field is missing. Check the field values, and try again.</p>
            capo_lex_model_building_service.errors.internal_failure_exception.InternalFailureException: <p>An internal Amazon Lex error occurred. Try your request again.</p>
            capo_lex_model_building_service.errors.limit_exceeded_exception.LimitExceededException: <p>The request exceeded a limit. Try your request again.</p>
            capo_lex_model_building_service.errors.not_found_exception.NotFoundException: <p>The resource specified in the request was not found. Check the resource and try again.</p>
            capo_lex_model_building_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lex_model_building_service.types.get_bot_versions_request.GetBotVersionsRequest]",
        ) -> AsyncOperationResponse[
            "capo_lex_model_building_service.types.get_bot_versions_response.GetBotVersionsResponse"
        ]:
            import capo_lex_model_building_service._operations.aws_deep_sense_model_building_service.get_bot_versions

            (
                output,
                http_response,
            ) = await capo_lex_model_building_service._operations.aws_deep_sense_model_building_service.get_bot_versions.async_get_bot_versions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lex_model_building_service.types.get_bot_versions_request.GetBotVersionsRequest = {
            "name": name
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

    async def iter_get_bot_versions(
        self,
        name: "capo_lex_model_building_service.types.bot_name.BotName",
        *,
        config_overrides: Optional[AsyncLexModelBuildingServiceClientConfig] = None,
        next_token: Optional[
            "capo_lex_model_building_service.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "capo_lex_model_building_service.types.max_results.MaxResults"
        ] = None,
    ) -> "AsyncIterator[capo_lex_model_building_service.types.get_bot_versions_response.GetBotVersionsResponse]":
        _token = next_token
        while True:
            _response = await self.get_bot_versions(
                name,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def get_builtin_intent(
        self,
        signature: "capo_lex_model_building_service.types.builtin_intent_signature.BuiltinIntentSignature",
        *,
        config_overrides: Optional[AsyncLexModelBuildingServiceClientConfig] = None,
    ) -> "capo_lex_model_building_service.types.get_builtin_intent_response.GetBuiltinIntentResponse":
        """<p>Returns information about a built-in intent.</p> <p>This operation requires permission for the <code>lex:GetBuiltinIntent</code> action.</p>

        Args:
            signature: <p>The unique identifier for a built-in intent. To find the signature for an intent, see <a href="https://developer.amazon.com/public/solutions/alexa/alexa-skills-kit/docs/built-in-intent-ref/standard-intents">Standard Built-in Intents</a> in the <i>Alexa Skills Kit</i>.</p>

        Raises:
            capo_lex_model_building_service.errors.bad_request_exception.BadRequestException: <p>The request is not well formed. For example, a value is invalid or a required field is missing. Check the field values, and try again.</p>
            capo_lex_model_building_service.errors.internal_failure_exception.InternalFailureException: <p>An internal Amazon Lex error occurred. Try your request again.</p>
            capo_lex_model_building_service.errors.limit_exceeded_exception.LimitExceededException: <p>The request exceeded a limit. Try your request again.</p>
            capo_lex_model_building_service.errors.not_found_exception.NotFoundException: <p>The resource specified in the request was not found. Check the resource and try again.</p>
            capo_lex_model_building_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lex_model_building_service.types.get_builtin_intent_request.GetBuiltinIntentRequest]",
        ) -> AsyncOperationResponse[
            "capo_lex_model_building_service.types.get_builtin_intent_response.GetBuiltinIntentResponse"
        ]:
            import capo_lex_model_building_service._operations.aws_deep_sense_model_building_service.get_builtin_intent

            (
                output,
                http_response,
            ) = await capo_lex_model_building_service._operations.aws_deep_sense_model_building_service.get_builtin_intent.async_get_builtin_intent(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lex_model_building_service.types.get_builtin_intent_request.GetBuiltinIntentRequest = {
            "signature": signature
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_builtin_intents(
        self,
        *,
        config_overrides: Optional[AsyncLexModelBuildingServiceClientConfig] = None,
        locale: Optional["capo_lex_model_building_service.types.locale.Locale"] = None,
        signature_contains: Optional[
            "capo_lex_model_building_service.types.string.String"
        ] = None,
        next_token: Optional[
            "capo_lex_model_building_service.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "capo_lex_model_building_service.types.max_results.MaxResults"
        ] = None,
    ) -> "capo_lex_model_building_service.types.get_builtin_intents_response.GetBuiltinIntentsResponse":
        """<p>Gets a list of built-in intents that meet the specified criteria.</p> <p>This operation requires permission for the <code>lex:GetBuiltinIntents</code> action.</p>

        Args:
            locale: <p>A list of locales that the intent supports.</p>
            signature_contains: <p>Substring to match in built-in intent signatures. An intent will be returned if any part of its signature matches the substring. For example, "xyz" matches both "xyzabc" and "abcxyz." To find the signature for an intent, see <a href="https://developer.amazon.com/public/solutions/alexa/alexa-skills-kit/docs/built-in-intent-ref/standard-intents">Standard Built-in Intents</a> in the <i>Alexa Skills Kit</i>.</p>
            next_token: <p>A pagination token that fetches the next page of intents. If this API call is truncated, Amazon Lex returns a pagination token in the response. To fetch the next page of intents, use the pagination token in the next request.</p>
            max_results: <p>The maximum number of intents to return in the response. The default is 10.</p>

        Raises:
            capo_lex_model_building_service.errors.bad_request_exception.BadRequestException: <p>The request is not well formed. For example, a value is invalid or a required field is missing. Check the field values, and try again.</p>
            capo_lex_model_building_service.errors.internal_failure_exception.InternalFailureException: <p>An internal Amazon Lex error occurred. Try your request again.</p>
            capo_lex_model_building_service.errors.limit_exceeded_exception.LimitExceededException: <p>The request exceeded a limit. Try your request again.</p>
            capo_lex_model_building_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lex_model_building_service.types.get_builtin_intents_request.GetBuiltinIntentsRequest]",
        ) -> AsyncOperationResponse[
            "capo_lex_model_building_service.types.get_builtin_intents_response.GetBuiltinIntentsResponse"
        ]:
            import capo_lex_model_building_service._operations.aws_deep_sense_model_building_service.get_builtin_intents

            (
                output,
                http_response,
            ) = await capo_lex_model_building_service._operations.aws_deep_sense_model_building_service.get_builtin_intents.async_get_builtin_intents(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lex_model_building_service.types.get_builtin_intents_request.GetBuiltinIntentsRequest = {}
        if locale is not None:
            input_["locale"] = locale
        if signature_contains is not None:
            input_["signature_contains"] = signature_contains
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

    async def iter_get_builtin_intents(
        self,
        *,
        config_overrides: Optional[AsyncLexModelBuildingServiceClientConfig] = None,
        locale: Optional["capo_lex_model_building_service.types.locale.Locale"] = None,
        signature_contains: Optional[
            "capo_lex_model_building_service.types.string.String"
        ] = None,
        next_token: Optional[
            "capo_lex_model_building_service.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "capo_lex_model_building_service.types.max_results.MaxResults"
        ] = None,
    ) -> "AsyncIterator[capo_lex_model_building_service.types.get_builtin_intents_response.GetBuiltinIntentsResponse]":
        _token = next_token
        while True:
            _response = await self.get_builtin_intents(
                config_overrides=config_overrides,
                locale=locale,
                signature_contains=signature_contains,
                next_token=_token,
                max_results=max_results,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def get_builtin_slot_types(
        self,
        *,
        config_overrides: Optional[AsyncLexModelBuildingServiceClientConfig] = None,
        locale: Optional["capo_lex_model_building_service.types.locale.Locale"] = None,
        signature_contains: Optional[
            "capo_lex_model_building_service.types.string.String"
        ] = None,
        next_token: Optional[
            "capo_lex_model_building_service.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "capo_lex_model_building_service.types.max_results.MaxResults"
        ] = None,
    ) -> "capo_lex_model_building_service.types.get_builtin_slot_types_response.GetBuiltinSlotTypesResponse":
        """<p>Gets a list of built-in slot types that meet the specified criteria.</p> <p>For a list of built-in slot types, see <a href="https://developer.amazon.com/public/solutions/alexa/alexa-skills-kit/docs/built-in-intent-ref/slot-type-reference">Slot Type Reference</a> in the <i>Alexa Skills Kit</i>.</p> <p>This operation requires permission for the <code>lex:GetBuiltInSlotTypes</code> action.</p>

        Args:
            locale: <p>A list of locales that the slot type supports.</p>
            signature_contains: <p>Substring to match in built-in slot type signatures. A slot type will be returned if any part of its signature matches the substring. For example, "xyz" matches both "xyzabc" and "abcxyz."</p>
            next_token: <p>A pagination token that fetches the next page of slot types. If the response to this API call is truncated, Amazon Lex returns a pagination token in the response. To fetch the next page of slot types, specify the pagination token in the next request.</p>
            max_results: <p>The maximum number of slot types to return in the response. The default is 10.</p>

        Raises:
            capo_lex_model_building_service.errors.bad_request_exception.BadRequestException: <p>The request is not well formed. For example, a value is invalid or a required field is missing. Check the field values, and try again.</p>
            capo_lex_model_building_service.errors.internal_failure_exception.InternalFailureException: <p>An internal Amazon Lex error occurred. Try your request again.</p>
            capo_lex_model_building_service.errors.limit_exceeded_exception.LimitExceededException: <p>The request exceeded a limit. Try your request again.</p>
            capo_lex_model_building_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lex_model_building_service.types.get_builtin_slot_types_request.GetBuiltinSlotTypesRequest]",
        ) -> AsyncOperationResponse[
            "capo_lex_model_building_service.types.get_builtin_slot_types_response.GetBuiltinSlotTypesResponse"
        ]:
            import capo_lex_model_building_service._operations.aws_deep_sense_model_building_service.get_builtin_slot_types

            (
                output,
                http_response,
            ) = await capo_lex_model_building_service._operations.aws_deep_sense_model_building_service.get_builtin_slot_types.async_get_builtin_slot_types(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lex_model_building_service.types.get_builtin_slot_types_request.GetBuiltinSlotTypesRequest = {}
        if locale is not None:
            input_["locale"] = locale
        if signature_contains is not None:
            input_["signature_contains"] = signature_contains
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

    async def iter_get_builtin_slot_types(
        self,
        *,
        config_overrides: Optional[AsyncLexModelBuildingServiceClientConfig] = None,
        locale: Optional["capo_lex_model_building_service.types.locale.Locale"] = None,
        signature_contains: Optional[
            "capo_lex_model_building_service.types.string.String"
        ] = None,
        next_token: Optional[
            "capo_lex_model_building_service.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "capo_lex_model_building_service.types.max_results.MaxResults"
        ] = None,
    ) -> "AsyncIterator[capo_lex_model_building_service.types.get_builtin_slot_types_response.GetBuiltinSlotTypesResponse]":
        _token = next_token
        while True:
            _response = await self.get_builtin_slot_types(
                config_overrides=config_overrides,
                locale=locale,
                signature_contains=signature_contains,
                next_token=_token,
                max_results=max_results,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def get_export(
        self,
        name: "capo_lex_model_building_service.types.name.Name",
        version: "capo_lex_model_building_service.types.numerical_version.NumericalVersion",
        resource_type: "capo_lex_model_building_service.types.resource_type.ResourceType",
        export_type: "capo_lex_model_building_service.types.export_type.ExportType",
        *,
        config_overrides: Optional[AsyncLexModelBuildingServiceClientConfig] = None,
    ) -> "capo_lex_model_building_service.types.get_export_response.GetExportResponse":
        """<p>Exports the contents of a Amazon Lex resource in a specified format. </p>

        Args:
            name: <p>The name of the bot to export.</p>
            version: <p>The version of the bot to export.</p>
            resource_type: <p>The type of resource to export. </p>
            export_type: <p>The format of the exported data.</p>

        Raises:
            capo_lex_model_building_service.errors.bad_request_exception.BadRequestException: <p>The request is not well formed. For example, a value is invalid or a required field is missing. Check the field values, and try again.</p>
            capo_lex_model_building_service.errors.internal_failure_exception.InternalFailureException: <p>An internal Amazon Lex error occurred. Try your request again.</p>
            capo_lex_model_building_service.errors.limit_exceeded_exception.LimitExceededException: <p>The request exceeded a limit. Try your request again.</p>
            capo_lex_model_building_service.errors.not_found_exception.NotFoundException: <p>The resource specified in the request was not found. Check the resource and try again.</p>
            capo_lex_model_building_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lex_model_building_service.types.get_export_request.GetExportRequest]",
        ) -> AsyncOperationResponse[
            "capo_lex_model_building_service.types.get_export_response.GetExportResponse"
        ]:
            import capo_lex_model_building_service._operations.aws_deep_sense_model_building_service.get_export

            (
                output,
                http_response,
            ) = await capo_lex_model_building_service._operations.aws_deep_sense_model_building_service.get_export.async_get_export(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lex_model_building_service.types.get_export_request.GetExportRequest = {
            "name": name,
            "version": version,
            "resource_type": resource_type,
            "export_type": export_type,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_import(
        self,
        import_id: "capo_lex_model_building_service.types.string.String",
        *,
        config_overrides: Optional[AsyncLexModelBuildingServiceClientConfig] = None,
    ) -> "capo_lex_model_building_service.types.get_import_response.GetImportResponse":
        """<p>Gets information about an import job started with the <code>StartImport</code> operation.</p>

        Args:
            import_id: <p>The identifier of the import job information to return.</p>

        Raises:
            capo_lex_model_building_service.errors.bad_request_exception.BadRequestException: <p>The request is not well formed. For example, a value is invalid or a required field is missing. Check the field values, and try again.</p>
            capo_lex_model_building_service.errors.internal_failure_exception.InternalFailureException: <p>An internal Amazon Lex error occurred. Try your request again.</p>
            capo_lex_model_building_service.errors.limit_exceeded_exception.LimitExceededException: <p>The request exceeded a limit. Try your request again.</p>
            capo_lex_model_building_service.errors.not_found_exception.NotFoundException: <p>The resource specified in the request was not found. Check the resource and try again.</p>
            capo_lex_model_building_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lex_model_building_service.types.get_import_request.GetImportRequest]",
        ) -> AsyncOperationResponse[
            "capo_lex_model_building_service.types.get_import_response.GetImportResponse"
        ]:
            import capo_lex_model_building_service._operations.aws_deep_sense_model_building_service.get_import

            (
                output,
                http_response,
            ) = await capo_lex_model_building_service._operations.aws_deep_sense_model_building_service.get_import.async_get_import(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lex_model_building_service.types.get_import_request.GetImportRequest = {
            "import_id": import_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_intent(
        self,
        name: "capo_lex_model_building_service.types.intent_name.IntentName",
        version: "capo_lex_model_building_service.types.version.Version",
        *,
        config_overrides: Optional[AsyncLexModelBuildingServiceClientConfig] = None,
    ) -> "capo_lex_model_building_service.types.get_intent_response.GetIntentResponse":
        """<p> Returns information about an intent. In addition to the intent name, you must specify the intent version. </p> <p> This operation requires permissions to perform the <code>lex:GetIntent</code> action. </p>

        Args:
            name: <p>The name of the intent. The name is case sensitive. </p>
            version: <p>The version of the intent.</p>

        Raises:
            capo_lex_model_building_service.errors.bad_request_exception.BadRequestException: <p>The request is not well formed. For example, a value is invalid or a required field is missing. Check the field values, and try again.</p>
            capo_lex_model_building_service.errors.internal_failure_exception.InternalFailureException: <p>An internal Amazon Lex error occurred. Try your request again.</p>
            capo_lex_model_building_service.errors.limit_exceeded_exception.LimitExceededException: <p>The request exceeded a limit. Try your request again.</p>
            capo_lex_model_building_service.errors.not_found_exception.NotFoundException: <p>The resource specified in the request was not found. Check the resource and try again.</p>
            capo_lex_model_building_service.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To get a information about an intent
            This example shows how to get information about an intent.

            >>> await client.get_intent(name='DocOrderPizza', version='$LATEST')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lex_model_building_service.types.get_intent_request.GetIntentRequest]",
        ) -> AsyncOperationResponse[
            "capo_lex_model_building_service.types.get_intent_response.GetIntentResponse"
        ]:
            import capo_lex_model_building_service._operations.aws_deep_sense_model_building_service.get_intent

            (
                output,
                http_response,
            ) = await capo_lex_model_building_service._operations.aws_deep_sense_model_building_service.get_intent.async_get_intent(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lex_model_building_service.types.get_intent_request.GetIntentRequest = {
            "name": name,
            "version": version,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_intents(
        self,
        *,
        config_overrides: Optional[AsyncLexModelBuildingServiceClientConfig] = None,
        next_token: Optional[
            "capo_lex_model_building_service.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "capo_lex_model_building_service.types.max_results.MaxResults"
        ] = None,
        name_contains: Optional[
            "capo_lex_model_building_service.types.intent_name.IntentName"
        ] = None,
    ) -> (
        "capo_lex_model_building_service.types.get_intents_response.GetIntentsResponse"
    ):
        """<p>Returns intent information as follows: </p> <ul> <li> <p>If you specify the <code>nameContains</code> field, returns the <code>$LATEST</code> version of all intents that contain the specified string.</p> </li> <li> <p> If you don't specify the <code>nameContains</code> field, returns information about the <code>$LATEST</code> version of all intents. </p> </li> </ul> <p> The operation requires permission for the <code>lex:GetIntents</code> action. </p>

        Args:
            next_token: <p>A pagination token that fetches the next page of intents. If the response to this API call is truncated, Amazon Lex returns a pagination token in the response. To fetch the next page of intents, specify the pagination token in the next request. </p>
            max_results: <p>The maximum number of intents to return in the response. The default is 10.</p>
            name_contains: <p>Substring to match in intent names. An intent will be returned if any part of its name matches the substring. For example, "xyz" matches both "xyzabc" and "abcxyz."</p>

        Raises:
            capo_lex_model_building_service.errors.bad_request_exception.BadRequestException: <p>The request is not well formed. For example, a value is invalid or a required field is missing. Check the field values, and try again.</p>
            capo_lex_model_building_service.errors.internal_failure_exception.InternalFailureException: <p>An internal Amazon Lex error occurred. Try your request again.</p>
            capo_lex_model_building_service.errors.limit_exceeded_exception.LimitExceededException: <p>The request exceeded a limit. Try your request again.</p>
            capo_lex_model_building_service.errors.not_found_exception.NotFoundException: <p>The resource specified in the request was not found. Check the resource and try again.</p>
            capo_lex_model_building_service.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To get a list of intents
            This example shows how to get a list of all of the intents in your account.

            >>> await client.get_intents(next_token='', max_results=10)
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lex_model_building_service.types.get_intents_request.GetIntentsRequest]",
        ) -> AsyncOperationResponse[
            "capo_lex_model_building_service.types.get_intents_response.GetIntentsResponse"
        ]:
            import capo_lex_model_building_service._operations.aws_deep_sense_model_building_service.get_intents

            (
                output,
                http_response,
            ) = await capo_lex_model_building_service._operations.aws_deep_sense_model_building_service.get_intents.async_get_intents(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lex_model_building_service.types.get_intents_request.GetIntentsRequest = {}
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if name_contains is not None:
            input_["name_contains"] = name_contains

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_get_intents(
        self,
        *,
        config_overrides: Optional[AsyncLexModelBuildingServiceClientConfig] = None,
        next_token: Optional[
            "capo_lex_model_building_service.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "capo_lex_model_building_service.types.max_results.MaxResults"
        ] = None,
        name_contains: Optional[
            "capo_lex_model_building_service.types.intent_name.IntentName"
        ] = None,
    ) -> "AsyncIterator[capo_lex_model_building_service.types.get_intents_response.GetIntentsResponse]":
        _token = next_token
        while True:
            _response = await self.get_intents(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
                name_contains=name_contains,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def get_intent_versions(
        self,
        name: "capo_lex_model_building_service.types.intent_name.IntentName",
        *,
        config_overrides: Optional[AsyncLexModelBuildingServiceClientConfig] = None,
        next_token: Optional[
            "capo_lex_model_building_service.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "capo_lex_model_building_service.types.max_results.MaxResults"
        ] = None,
    ) -> "capo_lex_model_building_service.types.get_intent_versions_response.GetIntentVersionsResponse":
        """<p>Gets information about all of the versions of an intent.</p> <p>The <code>GetIntentVersions</code> operation returns an <code>IntentMetadata</code> object for each version of an intent. For example, if an intent has three numbered versions, the <code>GetIntentVersions</code> operation returns four <code>IntentMetadata</code> objects in the response, one for each numbered version and one for the <code>$LATEST</code> version. </p> <p>The <code>GetIntentVersions</code> operation always returns at least one version, the <code>$LATEST</code> version.</p> <p>This operation requires permissions for the <code>lex:GetIntentVersions</code> action.</p>

        Args:
            name: <p>The name of the intent for which versions should be returned.</p>
            next_token: <p>A pagination token for fetching the next page of intent versions. If the response to this call is truncated, Amazon Lex returns a pagination token in the response. To fetch the next page of versions, specify the pagination token in the next request. </p>
            max_results: <p>The maximum number of intent versions to return in the response. The default is 10.</p>

        Raises:
            capo_lex_model_building_service.errors.bad_request_exception.BadRequestException: <p>The request is not well formed. For example, a value is invalid or a required field is missing. Check the field values, and try again.</p>
            capo_lex_model_building_service.errors.internal_failure_exception.InternalFailureException: <p>An internal Amazon Lex error occurred. Try your request again.</p>
            capo_lex_model_building_service.errors.limit_exceeded_exception.LimitExceededException: <p>The request exceeded a limit. Try your request again.</p>
            capo_lex_model_building_service.errors.not_found_exception.NotFoundException: <p>The resource specified in the request was not found. Check the resource and try again.</p>
            capo_lex_model_building_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lex_model_building_service.types.get_intent_versions_request.GetIntentVersionsRequest]",
        ) -> AsyncOperationResponse[
            "capo_lex_model_building_service.types.get_intent_versions_response.GetIntentVersionsResponse"
        ]:
            import capo_lex_model_building_service._operations.aws_deep_sense_model_building_service.get_intent_versions

            (
                output,
                http_response,
            ) = await capo_lex_model_building_service._operations.aws_deep_sense_model_building_service.get_intent_versions.async_get_intent_versions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lex_model_building_service.types.get_intent_versions_request.GetIntentVersionsRequest = {
            "name": name
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

    async def iter_get_intent_versions(
        self,
        name: "capo_lex_model_building_service.types.intent_name.IntentName",
        *,
        config_overrides: Optional[AsyncLexModelBuildingServiceClientConfig] = None,
        next_token: Optional[
            "capo_lex_model_building_service.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "capo_lex_model_building_service.types.max_results.MaxResults"
        ] = None,
    ) -> "AsyncIterator[capo_lex_model_building_service.types.get_intent_versions_response.GetIntentVersionsResponse]":
        _token = next_token
        while True:
            _response = await self.get_intent_versions(
                name,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def get_migration(
        self,
        migration_id: "capo_lex_model_building_service.types.migration_id.MigrationId",
        *,
        config_overrides: Optional[AsyncLexModelBuildingServiceClientConfig] = None,
    ) -> "capo_lex_model_building_service.types.get_migration_response.GetMigrationResponse":
        """<p>Provides details about an ongoing or complete migration from an Amazon Lex V1 bot to an Amazon Lex V2 bot. Use this operation to view the migration alerts and warnings related to the migration.</p>

        Args:
            migration_id: <p>The unique identifier of the migration to view. The <code>migrationID</code> is returned by the operation.</p>

        Raises:
            capo_lex_model_building_service.errors.bad_request_exception.BadRequestException: <p>The request is not well formed. For example, a value is invalid or a required field is missing. Check the field values, and try again.</p>
            capo_lex_model_building_service.errors.internal_failure_exception.InternalFailureException: <p>An internal Amazon Lex error occurred. Try your request again.</p>
            capo_lex_model_building_service.errors.limit_exceeded_exception.LimitExceededException: <p>The request exceeded a limit. Try your request again.</p>
            capo_lex_model_building_service.errors.not_found_exception.NotFoundException: <p>The resource specified in the request was not found. Check the resource and try again.</p>
            capo_lex_model_building_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lex_model_building_service.types.get_migration_request.GetMigrationRequest]",
        ) -> AsyncOperationResponse[
            "capo_lex_model_building_service.types.get_migration_response.GetMigrationResponse"
        ]:
            import capo_lex_model_building_service._operations.aws_deep_sense_model_building_service.get_migration

            (
                output,
                http_response,
            ) = await capo_lex_model_building_service._operations.aws_deep_sense_model_building_service.get_migration.async_get_migration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lex_model_building_service.types.get_migration_request.GetMigrationRequest = {
            "migration_id": migration_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_migrations(
        self,
        *,
        config_overrides: Optional[AsyncLexModelBuildingServiceClientConfig] = None,
        sort_by_attribute: Optional[
            "capo_lex_model_building_service.types.migration_sort_attribute.MigrationSortAttribute"
        ] = None,
        sort_by_order: Optional[
            "capo_lex_model_building_service.types.sort_order.SortOrder"
        ] = None,
        v1_bot_name_contains: Optional[
            "capo_lex_model_building_service.types.bot_name.BotName"
        ] = None,
        migration_status_equals: Optional[
            "capo_lex_model_building_service.types.migration_status.MigrationStatus"
        ] = None,
        max_results: Optional[
            "capo_lex_model_building_service.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_lex_model_building_service.types.next_token.NextToken"
        ] = None,
    ) -> "capo_lex_model_building_service.types.get_migrations_response.GetMigrationsResponse":
        """<p>Gets a list of migrations between Amazon Lex V1 and Amazon Lex V2.</p>

        Args:
            sort_by_attribute: <p>The field to sort the list of migrations by. You can sort by the Amazon Lex V1 bot name or the date and time that the migration was started.</p>
            sort_by_order: <p>The order so sort the list.</p>
            v1_bot_name_contains: <p>Filters the list to contain only bots whose name contains the specified string. The string is matched anywhere in bot name.</p>
            migration_status_equals: <p>Filters the list to contain only migrations in the specified state.</p>
            max_results: <p>The maximum number of migrations to return in the response. The default is 10.</p>
            next_token: <p>A pagination token that fetches the next page of migrations. If the response to this operation is truncated, Amazon Lex returns a pagination token in the response. To fetch the next page of migrations, specify the pagination token in the request.</p>

        Raises:
            capo_lex_model_building_service.errors.bad_request_exception.BadRequestException: <p>The request is not well formed. For example, a value is invalid or a required field is missing. Check the field values, and try again.</p>
            capo_lex_model_building_service.errors.internal_failure_exception.InternalFailureException: <p>An internal Amazon Lex error occurred. Try your request again.</p>
            capo_lex_model_building_service.errors.limit_exceeded_exception.LimitExceededException: <p>The request exceeded a limit. Try your request again.</p>
            capo_lex_model_building_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lex_model_building_service.types.get_migrations_request.GetMigrationsRequest]",
        ) -> AsyncOperationResponse[
            "capo_lex_model_building_service.types.get_migrations_response.GetMigrationsResponse"
        ]:
            import capo_lex_model_building_service._operations.aws_deep_sense_model_building_service.get_migrations

            (
                output,
                http_response,
            ) = await capo_lex_model_building_service._operations.aws_deep_sense_model_building_service.get_migrations.async_get_migrations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lex_model_building_service.types.get_migrations_request.GetMigrationsRequest = {}
        if sort_by_attribute is not None:
            input_["sort_by_attribute"] = sort_by_attribute
        if sort_by_order is not None:
            input_["sort_by_order"] = sort_by_order
        if v1_bot_name_contains is not None:
            input_["v1_bot_name_contains"] = v1_bot_name_contains
        if migration_status_equals is not None:
            input_["migration_status_equals"] = migration_status_equals
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

    async def iter_get_migrations(
        self,
        *,
        config_overrides: Optional[AsyncLexModelBuildingServiceClientConfig] = None,
        sort_by_attribute: Optional[
            "capo_lex_model_building_service.types.migration_sort_attribute.MigrationSortAttribute"
        ] = None,
        sort_by_order: Optional[
            "capo_lex_model_building_service.types.sort_order.SortOrder"
        ] = None,
        v1_bot_name_contains: Optional[
            "capo_lex_model_building_service.types.bot_name.BotName"
        ] = None,
        migration_status_equals: Optional[
            "capo_lex_model_building_service.types.migration_status.MigrationStatus"
        ] = None,
        max_results: Optional[
            "capo_lex_model_building_service.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_lex_model_building_service.types.next_token.NextToken"
        ] = None,
    ) -> "AsyncIterator[capo_lex_model_building_service.types.get_migrations_response.GetMigrationsResponse]":
        _token = next_token
        while True:
            _response = await self.get_migrations(
                config_overrides=config_overrides,
                sort_by_attribute=sort_by_attribute,
                sort_by_order=sort_by_order,
                v1_bot_name_contains=v1_bot_name_contains,
                migration_status_equals=migration_status_equals,
                max_results=max_results,
                next_token=_token,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def get_slot_type(
        self,
        name: "capo_lex_model_building_service.types.slot_type_name.SlotTypeName",
        version: "capo_lex_model_building_service.types.version.Version",
        *,
        config_overrides: Optional[AsyncLexModelBuildingServiceClientConfig] = None,
    ) -> "capo_lex_model_building_service.types.get_slot_type_response.GetSlotTypeResponse":
        """<p>Returns information about a specific version of a slot type. In addition to specifying the slot type name, you must specify the slot type version.</p> <p>This operation requires permissions for the <code>lex:GetSlotType</code> action.</p>

        Args:
            name: <p>The name of the slot type. The name is case sensitive. </p>
            version: <p>The version of the slot type. </p>

        Raises:
            capo_lex_model_building_service.errors.bad_request_exception.BadRequestException: <p>The request is not well formed. For example, a value is invalid or a required field is missing. Check the field values, and try again.</p>
            capo_lex_model_building_service.errors.internal_failure_exception.InternalFailureException: <p>An internal Amazon Lex error occurred. Try your request again.</p>
            capo_lex_model_building_service.errors.limit_exceeded_exception.LimitExceededException: <p>The request exceeded a limit. Try your request again.</p>
            capo_lex_model_building_service.errors.not_found_exception.NotFoundException: <p>The resource specified in the request was not found. Check the resource and try again.</p>
            capo_lex_model_building_service.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To get information about a slot type
            This example shows how to get information about a slot type.

            >>> await client.get_slot_type(name='DocPizzaCrustType', version='$LATEST')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lex_model_building_service.types.get_slot_type_request.GetSlotTypeRequest]",
        ) -> AsyncOperationResponse[
            "capo_lex_model_building_service.types.get_slot_type_response.GetSlotTypeResponse"
        ]:
            import capo_lex_model_building_service._operations.aws_deep_sense_model_building_service.get_slot_type

            (
                output,
                http_response,
            ) = await capo_lex_model_building_service._operations.aws_deep_sense_model_building_service.get_slot_type.async_get_slot_type(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lex_model_building_service.types.get_slot_type_request.GetSlotTypeRequest = {
            "name": name,
            "version": version,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_slot_types(
        self,
        *,
        config_overrides: Optional[AsyncLexModelBuildingServiceClientConfig] = None,
        next_token: Optional[
            "capo_lex_model_building_service.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "capo_lex_model_building_service.types.max_results.MaxResults"
        ] = None,
        name_contains: Optional[
            "capo_lex_model_building_service.types.slot_type_name.SlotTypeName"
        ] = None,
    ) -> "capo_lex_model_building_service.types.get_slot_types_response.GetSlotTypesResponse":
        """<p>Returns slot type information as follows: </p> <ul> <li> <p>If you specify the <code>nameContains</code> field, returns the <code>$LATEST</code> version of all slot types that contain the specified string.</p> </li> <li> <p> If you don't specify the <code>nameContains</code> field, returns information about the <code>$LATEST</code> version of all slot types. </p> </li> </ul> <p> The operation requires permission for the <code>lex:GetSlotTypes</code> action. </p>

        Args:
            next_token: <p>A pagination token that fetches the next page of slot types. If the response to this API call is truncated, Amazon Lex returns a pagination token in the response. To fetch next page of slot types, specify the pagination token in the next request.</p>
            max_results: <p>The maximum number of slot types to return in the response. The default is 10.</p>
            name_contains: <p>Substring to match in slot type names. A slot type will be returned if any part of its name matches the substring. For example, "xyz" matches both "xyzabc" and "abcxyz."</p>

        Raises:
            capo_lex_model_building_service.errors.bad_request_exception.BadRequestException: <p>The request is not well formed. For example, a value is invalid or a required field is missing. Check the field values, and try again.</p>
            capo_lex_model_building_service.errors.internal_failure_exception.InternalFailureException: <p>An internal Amazon Lex error occurred. Try your request again.</p>
            capo_lex_model_building_service.errors.limit_exceeded_exception.LimitExceededException: <p>The request exceeded a limit. Try your request again.</p>
            capo_lex_model_building_service.errors.not_found_exception.NotFoundException: <p>The resource specified in the request was not found. Check the resource and try again.</p>
            capo_lex_model_building_service.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To get a list of slot types
            This example shows how to get a list of all of the slot types in your account.

            >>> await client.get_slot_types(next_token='', max_results=10)
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lex_model_building_service.types.get_slot_types_request.GetSlotTypesRequest]",
        ) -> AsyncOperationResponse[
            "capo_lex_model_building_service.types.get_slot_types_response.GetSlotTypesResponse"
        ]:
            import capo_lex_model_building_service._operations.aws_deep_sense_model_building_service.get_slot_types

            (
                output,
                http_response,
            ) = await capo_lex_model_building_service._operations.aws_deep_sense_model_building_service.get_slot_types.async_get_slot_types(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lex_model_building_service.types.get_slot_types_request.GetSlotTypesRequest = {}
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if name_contains is not None:
            input_["name_contains"] = name_contains

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_get_slot_types(
        self,
        *,
        config_overrides: Optional[AsyncLexModelBuildingServiceClientConfig] = None,
        next_token: Optional[
            "capo_lex_model_building_service.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "capo_lex_model_building_service.types.max_results.MaxResults"
        ] = None,
        name_contains: Optional[
            "capo_lex_model_building_service.types.slot_type_name.SlotTypeName"
        ] = None,
    ) -> "AsyncIterator[capo_lex_model_building_service.types.get_slot_types_response.GetSlotTypesResponse]":
        _token = next_token
        while True:
            _response = await self.get_slot_types(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
                name_contains=name_contains,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def get_slot_type_versions(
        self,
        name: "capo_lex_model_building_service.types.slot_type_name.SlotTypeName",
        *,
        config_overrides: Optional[AsyncLexModelBuildingServiceClientConfig] = None,
        next_token: Optional[
            "capo_lex_model_building_service.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "capo_lex_model_building_service.types.max_results.MaxResults"
        ] = None,
    ) -> "capo_lex_model_building_service.types.get_slot_type_versions_response.GetSlotTypeVersionsResponse":
        """<p>Gets information about all versions of a slot type.</p> <p>The <code>GetSlotTypeVersions</code> operation returns a <code>SlotTypeMetadata</code> object for each version of a slot type. For example, if a slot type has three numbered versions, the <code>GetSlotTypeVersions</code> operation returns four <code>SlotTypeMetadata</code> objects in the response, one for each numbered version and one for the <code>$LATEST</code> version. </p> <p>The <code>GetSlotTypeVersions</code> operation always returns at least one version, the <code>$LATEST</code> version.</p> <p>This operation requires permissions for the <code>lex:GetSlotTypeVersions</code> action.</p>

        Args:
            name: <p>The name of the slot type for which versions should be returned.</p>
            next_token: <p>A pagination token for fetching the next page of slot type versions. If the response to this call is truncated, Amazon Lex returns a pagination token in the response. To fetch the next page of versions, specify the pagination token in the next request. </p>
            max_results: <p>The maximum number of slot type versions to return in the response. The default is 10.</p>

        Raises:
            capo_lex_model_building_service.errors.bad_request_exception.BadRequestException: <p>The request is not well formed. For example, a value is invalid or a required field is missing. Check the field values, and try again.</p>
            capo_lex_model_building_service.errors.internal_failure_exception.InternalFailureException: <p>An internal Amazon Lex error occurred. Try your request again.</p>
            capo_lex_model_building_service.errors.limit_exceeded_exception.LimitExceededException: <p>The request exceeded a limit. Try your request again.</p>
            capo_lex_model_building_service.errors.not_found_exception.NotFoundException: <p>The resource specified in the request was not found. Check the resource and try again.</p>
            capo_lex_model_building_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lex_model_building_service.types.get_slot_type_versions_request.GetSlotTypeVersionsRequest]",
        ) -> AsyncOperationResponse[
            "capo_lex_model_building_service.types.get_slot_type_versions_response.GetSlotTypeVersionsResponse"
        ]:
            import capo_lex_model_building_service._operations.aws_deep_sense_model_building_service.get_slot_type_versions

            (
                output,
                http_response,
            ) = await capo_lex_model_building_service._operations.aws_deep_sense_model_building_service.get_slot_type_versions.async_get_slot_type_versions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lex_model_building_service.types.get_slot_type_versions_request.GetSlotTypeVersionsRequest = {
            "name": name
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

    async def iter_get_slot_type_versions(
        self,
        name: "capo_lex_model_building_service.types.slot_type_name.SlotTypeName",
        *,
        config_overrides: Optional[AsyncLexModelBuildingServiceClientConfig] = None,
        next_token: Optional[
            "capo_lex_model_building_service.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "capo_lex_model_building_service.types.max_results.MaxResults"
        ] = None,
    ) -> "AsyncIterator[capo_lex_model_building_service.types.get_slot_type_versions_response.GetSlotTypeVersionsResponse]":
        _token = next_token
        while True:
            _response = await self.get_slot_type_versions(
                name,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def get_utterances_view(
        self,
        bot_name: "capo_lex_model_building_service.types.bot_name.BotName",
        bot_versions: "capo_lex_model_building_service.types.bot_versions.BotVersions",
        status_type: "capo_lex_model_building_service.types.status_type.StatusType",
        *,
        config_overrides: Optional[AsyncLexModelBuildingServiceClientConfig] = None,
    ) -> "capo_lex_model_building_service.types.get_utterances_view_response.GetUtterancesViewResponse":
        """<p>Use the <code>GetUtterancesView</code> operation to get information about the utterances that your users have made to your bot. You can use this list to tune the utterances that your bot responds to.</p> <p>For example, say that you have created a bot to order flowers. After your users have used your bot for a while, use the <code>GetUtterancesView</code> operation to see the requests that they have made and whether they have been successful. You might find that the utterance "I want flowers" is not being recognized. You could add this utterance to the <code>OrderFlowers</code> intent so that your bot recognizes that utterance.</p> <p>After you publish a new version of a bot, you can get information about the old version and the new so that you can compare the performance across the two versions. </p> <p>Utterance statistics are generated once a day. Data is available for the last 15 days. You can request information for up to 5 versions of your bot in each request. Amazon Lex returns the most frequent utterances received by the bot in the last 15 days. The response contains information about a maximum of 100 utterances for each version.</p> <p>If you set <code>childDirected</code> field to true when you created your bot, if you are using slot obfuscation with one or more slots, or if you opted out of participating in improving Amazon Lex, utterances are not available.</p> <p>This operation requires permissions for the <code>lex:GetUtterancesView</code> action.</p>

        Args:
            bot_name: <p>The name of the bot for which utterance information should be returned.</p>
            bot_versions: <p>An array of bot versions for which utterance information should be returned. The limit is 5 versions per request.</p>
            status_type: <p>To return utterances that were recognized and handled, use <code>Detected</code>. To return utterances that were not recognized, use <code>Missed</code>.</p>

        Raises:
            capo_lex_model_building_service.errors.bad_request_exception.BadRequestException: <p>The request is not well formed. For example, a value is invalid or a required field is missing. Check the field values, and try again.</p>
            capo_lex_model_building_service.errors.internal_failure_exception.InternalFailureException: <p>An internal Amazon Lex error occurred. Try your request again.</p>
            capo_lex_model_building_service.errors.limit_exceeded_exception.LimitExceededException: <p>The request exceeded a limit. Try your request again.</p>
            capo_lex_model_building_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lex_model_building_service.types.get_utterances_view_request.GetUtterancesViewRequest]",
        ) -> AsyncOperationResponse[
            "capo_lex_model_building_service.types.get_utterances_view_response.GetUtterancesViewResponse"
        ]:
            import capo_lex_model_building_service._operations.aws_deep_sense_model_building_service.get_utterances_view

            (
                output,
                http_response,
            ) = await capo_lex_model_building_service._operations.aws_deep_sense_model_building_service.get_utterances_view.async_get_utterances_view(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lex_model_building_service.types.get_utterances_view_request.GetUtterancesViewRequest = {
            "bot_name": bot_name,
            "bot_versions": bot_versions,
            "status_type": status_type,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_tags_for_resource(
        self,
        resource_arn: "capo_lex_model_building_service.types.amazon_resource_name.AmazonResourceName",
        *,
        config_overrides: Optional[AsyncLexModelBuildingServiceClientConfig] = None,
    ) -> "capo_lex_model_building_service.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>Gets a list of tags associated with the specified resource. Only bots, bot aliases, and bot channels can have tags associated with them.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource to get a list of tags for.</p>

        Raises:
            capo_lex_model_building_service.errors.bad_request_exception.BadRequestException: <p>The request is not well formed. For example, a value is invalid or a required field is missing. Check the field values, and try again.</p>
            capo_lex_model_building_service.errors.internal_failure_exception.InternalFailureException: <p>An internal Amazon Lex error occurred. Try your request again.</p>
            capo_lex_model_building_service.errors.limit_exceeded_exception.LimitExceededException: <p>The request exceeded a limit. Try your request again.</p>
            capo_lex_model_building_service.errors.not_found_exception.NotFoundException: <p>The resource specified in the request was not found. Check the resource and try again.</p>
            capo_lex_model_building_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lex_model_building_service.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_lex_model_building_service.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import capo_lex_model_building_service._operations.aws_deep_sense_model_building_service.list_tags_for_resource

            (
                output,
                http_response,
            ) = await capo_lex_model_building_service._operations.aws_deep_sense_model_building_service.list_tags_for_resource.async_list_tags_for_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lex_model_building_service.types.list_tags_for_resource_request.ListTagsForResourceRequest = {
            "resource_arn": resource_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def put_bot(
        self,
        name: "capo_lex_model_building_service.types.bot_name.BotName",
        locale: "capo_lex_model_building_service.types.locale.Locale",
        child_directed: "capo_lex_model_building_service.types.boolean.Boolean",
        *,
        config_overrides: Optional[AsyncLexModelBuildingServiceClientConfig] = None,
        description: Optional[
            "capo_lex_model_building_service.types.description.Description"
        ] = None,
        intents: Optional[
            "capo_lex_model_building_service.types.intent_list.IntentList"
        ] = None,
        enable_model_improvements: Optional[
            "capo_lex_model_building_service.types.boolean.Boolean"
        ] = None,
        nlu_intent_confidence_threshold: Optional[
            "capo_lex_model_building_service.types.confidence_threshold.ConfidenceThreshold"
        ] = None,
        clarification_prompt: Optional[
            "capo_lex_model_building_service.types.prompt.Prompt"
        ] = None,
        abort_statement: Optional[
            "capo_lex_model_building_service.types.statement.Statement"
        ] = None,
        idle_session_ttl_in_seconds: Optional[
            "capo_lex_model_building_service.types.session_ttl.SessionTTL"
        ] = None,
        voice_id: Optional[
            "capo_lex_model_building_service.types.string.String"
        ] = None,
        checksum: Optional[
            "capo_lex_model_building_service.types.string.String"
        ] = None,
        process_behavior: Optional[
            "capo_lex_model_building_service.types.process_behavior.ProcessBehavior"
        ] = None,
        detect_sentiment: Optional[
            "capo_lex_model_building_service.types.boolean.Boolean"
        ] = None,
        create_version: Optional[
            "capo_lex_model_building_service.types.boolean.Boolean"
        ] = None,
        tags: Optional["capo_lex_model_building_service.types.tag_list.TagList"] = None,
    ) -> "capo_lex_model_building_service.types.put_bot_response.PutBotResponse":
        """<p>Creates an Amazon Lex conversational bot or replaces an existing bot. When you create or update a bot you are only required to specify a name, a locale, and whether the bot is directed toward children under age 13. You can use this to add intents later, or to remove intents from an existing bot. When you create a bot with the minimum information, the bot is created or updated but Amazon Lex returns the <code></code> response <code>FAILED</code>. You can build the bot after you add one or more intents. For more information about Amazon Lex bots, see <a>how-it-works</a>. </p> <p>If you specify the name of an existing bot, the fields in the request replace the existing values in the <code>$LATEST</code> version of the bot. Amazon Lex removes any fields that you don't provide values for in the request, except for the <code>idleTTLInSeconds</code> and <code>privacySettings</code> fields, which are set to their default values. If you don't specify values for required fields, Amazon Lex throws an exception.</p> <p>This operation requires permissions for the <code>lex:PutBot</code> action. For more information, see <a>security-iam</a>.</p>

        Args:
            name: <p>The name of the bot. The name is <i>not</i> case sensitive. </p>
            description: <p>A description of the bot.</p>
            intents: <p>An array of <code>Intent</code> objects. Each intent represents a command that a user can express. For example, a pizza ordering bot might support an OrderPizza intent. For more information, see <a>how-it-works</a>.</p>
            enable_model_improvements: <p>Set to <code>true</code> to enable access to natural language understanding improvements. </p> <p>When you set the <code>enableModelImprovements</code> parameter to <code>true</code> you can use the <code>nluIntentConfidenceThreshold</code> parameter to configure confidence scores. For more information, see <a href="https://docs.aws.amazon.com/lex/latest/dg/confidence-scores.html">Confidence Scores</a>.</p> <p>You can only set the <code>enableModelImprovements</code> parameter in certain Regions. If you set the parameter to <code>true</code>, your bot has access to accuracy improvements.</p> <p>The Regions where you can set the <code>enableModelImprovements</code> parameter to <code>true</code> are:</p> <ul> <li> <p>US East (N. Virginia) (us-east-1)</p> </li> <li> <p>US West (Oregon) (us-west-2)</p> </li> <li> <p>Asia Pacific (Sydney) (ap-southeast-2)</p> </li> <li> <p>EU (Ireland) (eu-west-1)</p> </li> </ul> <p>In other Regions, the <code>enableModelImprovements</code> parameter is set to <code>true</code> by default. In these Regions setting the parameter to <code>false</code> throws a <code>ValidationException</code> exception.</p>
            nlu_intent_confidence_threshold: <p>Determines the threshold where Amazon Lex will insert the <code>AMAZON.FallbackIntent</code>, <code>AMAZON.KendraSearchIntent</code>, or both when returning alternative intents in a <a href="https://docs.aws.amazon.com/lex/latest/dg/API_runtime_PostContent.html">PostContent</a> or <a href="https://docs.aws.amazon.com/lex/latest/dg/API_runtime_PostText.html">PostText</a> response. <code>AMAZON.FallbackIntent</code> and <code>AMAZON.KendraSearchIntent</code> are only inserted if they are configured for the bot.</p> <p>You must set the <code>enableModelImprovements</code> parameter to <code>true</code> to use confidence scores in the following regions.</p> <ul> <li> <p>US East (N. Virginia) (us-east-1)</p> </li> <li> <p>US West (Oregon) (us-west-2)</p> </li> <li> <p>Asia Pacific (Sydney) (ap-southeast-2)</p> </li> <li> <p>EU (Ireland) (eu-west-1)</p> </li> </ul> <p>In other Regions, the <code>enableModelImprovements</code> parameter is set to <code>true</code> by default.</p> <p>For example, suppose a bot is configured with the confidence threshold of 0.80 and the <code>AMAZON.FallbackIntent</code>. Amazon Lex returns three alternative intents with the following confidence scores: IntentA (0.70), IntentB (0.60), IntentC (0.50). The response from the <code>PostText</code> operation would be:</p> <ul> <li> <p>AMAZON.FallbackIntent</p> </li> <li> <p>IntentA</p> </li> <li> <p>IntentB</p> </li> <li> <p>IntentC</p> </li> </ul>
            clarification_prompt: <p>When Amazon Lex doesn't understand the user's intent, it uses this message to get clarification. To specify how many times Amazon Lex should repeat the clarification prompt, use the <code>maxAttempts</code> field. If Amazon Lex still doesn't understand, it sends the message in the <code>abortStatement</code> field. </p> <p>When you create a clarification prompt, make sure that it suggests the correct response from the user. for example, for a bot that orders pizza and drinks, you might create this clarification prompt: "What would you like to do? You can say 'Order a pizza' or 'Order a drink.'"</p> <p>If you have defined a fallback intent, it will be invoked if the clarification prompt is repeated the number of times defined in the <code>maxAttempts</code> field. For more information, see <a href="https://docs.aws.amazon.com/lex/latest/dg/built-in-intent-fallback.html"> AMAZON.FallbackIntent</a>.</p> <p>If you don't define a clarification prompt, at runtime Amazon Lex will return a 400 Bad Request exception in three cases: </p> <ul> <li> <p>Follow-up prompt - When the user responds to a follow-up prompt but does not provide an intent. For example, in response to a follow-up prompt that says "Would you like anything else today?" the user says "Yes." Amazon Lex will return a 400 Bad Request exception because it does not have a clarification prompt to send to the user to get an intent.</p> </li> <li> <p>Lambda function - When using a Lambda function, you return an <code>ElicitIntent</code> dialog type. Since Amazon Lex does not have a clarification prompt to get an intent from the user, it returns a 400 Bad Request exception.</p> </li> <li> <p>PutSession operation - When using the <code>PutSession</code> operation, you send an <code>ElicitIntent</code> dialog type. Since Amazon Lex does not have a clarification prompt to get an intent from the user, it returns a 400 Bad Request exception.</p> </li> </ul>
            abort_statement: <p>When Amazon Lex can't understand the user's input in context, it tries to elicit the information a few times. After that, Amazon Lex sends the message defined in <code>abortStatement</code> to the user, and then cancels the conversation. To set the number of retries, use the <code>valueElicitationPrompt</code> field for the slot type. </p> <p>For example, in a pizza ordering bot, Amazon Lex might ask a user "What type of crust would you like?" If the user's response is not one of the expected responses (for example, "thin crust, "deep dish," etc.), Amazon Lex tries to elicit a correct response a few more times. </p> <p>For example, in a pizza ordering application, <code>OrderPizza</code> might be one of the intents. This intent might require the <code>CrustType</code> slot. You specify the <code>valueElicitationPrompt</code> field when you create the <code>CrustType</code> slot.</p> <p>If you have defined a fallback intent the cancel statement will not be sent to the user, the fallback intent is used instead. For more information, see <a href="https://docs.aws.amazon.com/lex/latest/dg/built-in-intent-fallback.html"> AMAZON.FallbackIntent</a>.</p>
            idle_session_ttl_in_seconds: <p>The maximum time in seconds that Amazon Lex retains the data gathered in a conversation.</p> <p>A user interaction session remains active for the amount of time specified. If no conversation occurs during this time, the session expires and Amazon Lex deletes any data provided before the timeout.</p> <p>For example, suppose that a user chooses the OrderPizza intent, but gets sidetracked halfway through placing an order. If the user doesn't complete the order within the specified time, Amazon Lex discards the slot information that it gathered, and the user must start over.</p> <p>If you don't include the <code>idleSessionTTLInSeconds</code> element in a <code>PutBot</code> operation request, Amazon Lex uses the default value. This is also true if the request replaces an existing bot.</p> <p>The default is 300 seconds (5 minutes).</p>
            voice_id: <p>The Amazon Polly voice ID that you want Amazon Lex to use for voice interactions with the user. The locale configured for the voice must match the locale of the bot. For more information, see <a href="https://docs.aws.amazon.com/polly/latest/dg/voicelist.html">Voices in Amazon Polly</a> in the <i>Amazon Polly Developer Guide</i>.</p>
            checksum: <p>Identifies a specific revision of the <code>$LATEST</code> version.</p> <p>When you create a new bot, leave the <code>checksum</code> field blank. If you specify a checksum you get a <code>BadRequestException</code> exception.</p> <p>When you want to update a bot, set the <code>checksum</code> field to the checksum of the most recent revision of the <code>$LATEST</code> version. If you don't specify the <code> checksum</code> field, or if the checksum does not match the <code>$LATEST</code> version, you get a <code>PreconditionFailedException</code> exception.</p>
            process_behavior: <p>If you set the <code>processBehavior</code> element to <code>BUILD</code>, Amazon Lex builds the bot so that it can be run. If you set the element to <code>SAVE</code> Amazon Lex saves the bot, but doesn't build it. </p> <p>If you don't specify this value, the default value is <code>BUILD</code>.</p>
            locale: <p> Specifies the target locale for the bot. Any intent used in the bot must be compatible with the locale of the bot. </p> <p>The default is <code>en-US</code>.</p>
            child_directed: <p>For each Amazon Lex bot created with the Amazon Lex Model Building Service, you must specify whether your use of Amazon Lex is related to a website, program, or other application that is directed or targeted, in whole or in part, to children under age 13 and subject to the Children's Online Privacy Protection Act (COPPA) by specifying <code>true</code> or <code>false</code> in the <code>childDirected</code> field. By specifying <code>true</code> in the <code>childDirected</code> field, you confirm that your use of Amazon Lex <b>is</b> related to a website, program, or other application that is directed or targeted, in whole or in part, to children under age 13 and subject to COPPA. By specifying <code>false</code> in the <code>childDirected</code> field, you confirm that your use of Amazon Lex <b>is not</b> related to a website, program, or other application that is directed or targeted, in whole or in part, to children under age 13 and subject to COPPA. You may not specify a default value for the <code>childDirected</code> field that does not accurately reflect whether your use of Amazon Lex is related to a website, program, or other application that is directed or targeted, in whole or in part, to children under age 13 and subject to COPPA.</p> <p>If your use of Amazon Lex relates to a website, program, or other application that is directed in whole or in part, to children under age 13, you must obtain any required verifiable parental consent under COPPA. For information regarding the use of Amazon Lex in connection with websites, programs, or other applications that are directed or targeted, in whole or in part, to children under age 13, see the <a href="https://aws.amazon.com/lex/faqs#data-security">Amazon Lex FAQ.</a> </p>
            detect_sentiment: <p>When set to <code>true</code> user utterances are sent to Amazon Comprehend for sentiment analysis. If you don't specify <code>detectSentiment</code>, the default is <code>false</code>.</p>
            create_version: <p>When set to <code>true</code> a new numbered version of the bot is created. This is the same as calling the <code>CreateBotVersion</code> operation. If you don't specify <code>createVersion</code>, the default is <code>false</code>.</p>
            tags: <p>A list of tags to add to the bot. You can only add tags when you create a bot, you can't use the <code>PutBot</code> operation to update the tags on a bot. To update tags, use the <code>TagResource</code> operation.</p>

        Raises:
            capo_lex_model_building_service.errors.bad_request_exception.BadRequestException: <p>The request is not well formed. For example, a value is invalid or a required field is missing. Check the field values, and try again.</p>
            capo_lex_model_building_service.errors.conflict_exception.ConflictException: <p> There was a conflict processing the request. Try your request again. </p>
            capo_lex_model_building_service.errors.internal_failure_exception.InternalFailureException: <p>An internal Amazon Lex error occurred. Try your request again.</p>
            capo_lex_model_building_service.errors.limit_exceeded_exception.LimitExceededException: <p>The request exceeded a limit. Try your request again.</p>
            capo_lex_model_building_service.errors.precondition_failed_exception.PreconditionFailedException: <p> The checksum of the resource that you are trying to change does not match the checksum in the request. Check the resource's checksum and try again.</p>
            capo_lex_model_building_service.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To create a bot
            This example shows how to create a bot for ordering pizzas.

            >>> await client.put_bot(name='DocOrderPizzaBot', description='Orders a pizza from a local pizzeria.', intents=[{'intentName': 'DocOrderPizza', 'intentVersion': '$LATEST'}], clarification_prompt={'messages': [{'contentType': 'PlainText', 'content': "I'm sorry, I didn't hear that. Can you repeat what you just said?"}, {'contentType': 'PlainText', 'content': 'Can you say that again?'}], 'maxAttempts': 1}, abort_statement={'messages': [{'contentType': 'PlainText', 'content': "I don't understand. Can you try again?"}, {'contentType': 'PlainText', 'content': "I'm sorry, I don't understand."}]}, idle_session_ttl_in_seconds=300, process_behavior='SAVE', locale='en-US', child_directed=True)
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lex_model_building_service.types.put_bot_request.PutBotRequest]",
        ) -> AsyncOperationResponse[
            "capo_lex_model_building_service.types.put_bot_response.PutBotResponse"
        ]:
            import capo_lex_model_building_service._operations.aws_deep_sense_model_building_service.put_bot

            (
                output,
                http_response,
            ) = await capo_lex_model_building_service._operations.aws_deep_sense_model_building_service.put_bot.async_put_bot(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lex_model_building_service.types.put_bot_request.PutBotRequest = {
            "name": name,
            "locale": locale,
            "child_directed": child_directed,
        }
        if description is not None:
            input_["description"] = description
        if intents is not None:
            input_["intents"] = intents
        if enable_model_improvements is not None:
            input_["enable_model_improvements"] = enable_model_improvements
        if nlu_intent_confidence_threshold is not None:
            input_["nlu_intent_confidence_threshold"] = nlu_intent_confidence_threshold
        if clarification_prompt is not None:
            input_["clarification_prompt"] = clarification_prompt
        if abort_statement is not None:
            input_["abort_statement"] = abort_statement
        if idle_session_ttl_in_seconds is not None:
            input_["idle_session_ttl_in_seconds"] = idle_session_ttl_in_seconds
        if voice_id is not None:
            input_["voice_id"] = voice_id
        if checksum is not None:
            input_["checksum"] = checksum
        if process_behavior is not None:
            input_["process_behavior"] = process_behavior
        if detect_sentiment is not None:
            input_["detect_sentiment"] = detect_sentiment
        if create_version is not None:
            input_["create_version"] = create_version
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def put_bot_alias(
        self,
        name: "capo_lex_model_building_service.types.alias_name.AliasName",
        bot_version: "capo_lex_model_building_service.types.version.Version",
        bot_name: "capo_lex_model_building_service.types.bot_name.BotName",
        *,
        config_overrides: Optional[AsyncLexModelBuildingServiceClientConfig] = None,
        description: Optional[
            "capo_lex_model_building_service.types.description.Description"
        ] = None,
        checksum: Optional[
            "capo_lex_model_building_service.types.string.String"
        ] = None,
        conversation_logs: Optional[
            "capo_lex_model_building_service.types.conversation_logs_request.ConversationLogsRequest"
        ] = None,
        tags: Optional["capo_lex_model_building_service.types.tag_list.TagList"] = None,
    ) -> "capo_lex_model_building_service.types.put_bot_alias_response.PutBotAliasResponse":
        """<p>Creates an alias for the specified version of the bot or replaces an alias for the specified bot. To change the version of the bot that the alias points to, replace the alias. For more information about aliases, see <a>versioning-aliases</a>.</p> <p>This operation requires permissions for the <code>lex:PutBotAlias</code> action. </p>

        Args:
            name: <p>The name of the alias. The name is <i>not</i> case sensitive.</p>
            description: <p>A description of the alias.</p>
            bot_version: <p>The version of the bot.</p>
            bot_name: <p>The name of the bot.</p>
            checksum: <p>Identifies a specific revision of the <code>$LATEST</code> version.</p> <p>When you create a new bot alias, leave the <code>checksum</code> field blank. If you specify a checksum you get a <code>BadRequestException</code> exception.</p> <p>When you want to update a bot alias, set the <code>checksum</code> field to the checksum of the most recent revision of the <code>$LATEST</code> version. If you don't specify the <code> checksum</code> field, or if the checksum does not match the <code>$LATEST</code> version, you get a <code>PreconditionFailedException</code> exception.</p>
            conversation_logs: <p>Settings for conversation logs for the alias.</p>
            tags: <p>A list of tags to add to the bot alias. You can only add tags when you create an alias, you can't use the <code>PutBotAlias</code> operation to update the tags on a bot alias. To update tags, use the <code>TagResource</code> operation.</p>

        Raises:
            capo_lex_model_building_service.errors.bad_request_exception.BadRequestException: <p>The request is not well formed. For example, a value is invalid or a required field is missing. Check the field values, and try again.</p>
            capo_lex_model_building_service.errors.conflict_exception.ConflictException: <p> There was a conflict processing the request. Try your request again. </p>
            capo_lex_model_building_service.errors.internal_failure_exception.InternalFailureException: <p>An internal Amazon Lex error occurred. Try your request again.</p>
            capo_lex_model_building_service.errors.limit_exceeded_exception.LimitExceededException: <p>The request exceeded a limit. Try your request again.</p>
            capo_lex_model_building_service.errors.precondition_failed_exception.PreconditionFailedException: <p> The checksum of the resource that you are trying to change does not match the checksum in the request. Check the resource's checksum and try again.</p>
            capo_lex_model_building_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lex_model_building_service.types.put_bot_alias_request.PutBotAliasRequest]",
        ) -> AsyncOperationResponse[
            "capo_lex_model_building_service.types.put_bot_alias_response.PutBotAliasResponse"
        ]:
            import capo_lex_model_building_service._operations.aws_deep_sense_model_building_service.put_bot_alias

            (
                output,
                http_response,
            ) = await capo_lex_model_building_service._operations.aws_deep_sense_model_building_service.put_bot_alias.async_put_bot_alias(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lex_model_building_service.types.put_bot_alias_request.PutBotAliasRequest = {
            "name": name,
            "bot_version": bot_version,
            "bot_name": bot_name,
        }
        if description is not None:
            input_["description"] = description
        if checksum is not None:
            input_["checksum"] = checksum
        if conversation_logs is not None:
            input_["conversation_logs"] = conversation_logs
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def put_intent(
        self,
        name: "capo_lex_model_building_service.types.intent_name.IntentName",
        *,
        config_overrides: Optional[AsyncLexModelBuildingServiceClientConfig] = None,
        description: Optional[
            "capo_lex_model_building_service.types.description.Description"
        ] = None,
        slots: Optional[
            "capo_lex_model_building_service.types.slot_list.SlotList"
        ] = None,
        sample_utterances: Optional[
            "capo_lex_model_building_service.types.intent_utterance_list.IntentUtteranceList"
        ] = None,
        confirmation_prompt: Optional[
            "capo_lex_model_building_service.types.prompt.Prompt"
        ] = None,
        rejection_statement: Optional[
            "capo_lex_model_building_service.types.statement.Statement"
        ] = None,
        follow_up_prompt: Optional[
            "capo_lex_model_building_service.types.follow_up_prompt.FollowUpPrompt"
        ] = None,
        conclusion_statement: Optional[
            "capo_lex_model_building_service.types.statement.Statement"
        ] = None,
        dialog_code_hook: Optional[
            "capo_lex_model_building_service.types.code_hook.CodeHook"
        ] = None,
        fulfillment_activity: Optional[
            "capo_lex_model_building_service.types.fulfillment_activity.FulfillmentActivity"
        ] = None,
        parent_intent_signature: Optional[
            "capo_lex_model_building_service.types.builtin_intent_signature.BuiltinIntentSignature"
        ] = None,
        checksum: Optional[
            "capo_lex_model_building_service.types.string.String"
        ] = None,
        create_version: Optional[
            "capo_lex_model_building_service.types.boolean.Boolean"
        ] = None,
        kendra_configuration: Optional[
            "capo_lex_model_building_service.types.kendra_configuration.KendraConfiguration"
        ] = None,
        input_contexts: Optional[
            "capo_lex_model_building_service.types.input_context_list.InputContextList"
        ] = None,
        output_contexts: Optional[
            "capo_lex_model_building_service.types.output_context_list.OutputContextList"
        ] = None,
    ) -> "capo_lex_model_building_service.types.put_intent_response.PutIntentResponse":
        """<p>Creates an intent or replaces an existing intent.</p> <p>To define the interaction between the user and your bot, you use one or more intents. For a pizza ordering bot, for example, you would create an <code>OrderPizza</code> intent. </p> <p>To create an intent or replace an existing intent, you must provide the following:</p> <ul> <li> <p>Intent name. For example, <code>OrderPizza</code>.</p> </li> <li> <p>Sample utterances. For example, "Can I order a pizza, please." and "I want to order a pizza."</p> </li> <li> <p>Information to be gathered. You specify slot types for the information that your bot will request from the user. You can specify standard slot types, such as a date or a time, or custom slot types such as the size and crust of a pizza.</p> </li> <li> <p>How the intent will be fulfilled. You can provide a Lambda function or configure the intent to return the intent information to the client application. If you use a Lambda function, when all of the intent information is available, Amazon Lex invokes your Lambda function. If you configure your intent to return the intent information to the client application. </p> </li> </ul> <p>You can specify other optional information in the request, such as:</p> <ul> <li> <p>A confirmation prompt to ask the user to confirm an intent. For example, "Shall I order your pizza?"</p> </li> <li> <p>A conclusion statement to send to the user after the intent has been fulfilled. For example, "I placed your pizza order."</p> </li> <li> <p>A follow-up prompt that asks the user for additional activity. For example, asking "Do you want to order a drink with your pizza?"</p> </li> </ul> <p>If you specify an existing intent name to update the intent, Amazon Lex replaces the values in the <code>$LATEST</code> version of the intent with the values in the request. Amazon Lex removes fields that you don't provide in the request. If you don't specify the required fields, Amazon Lex throws an exception. When you update the <code>$LATEST</code> version of an intent, the <code>status</code> field of any bot that uses the <code>$LATEST</code> version of the intent is set to <code>NOT_BUILT</code>.</p> <p>For more information, see <a>how-it-works</a>.</p> <p>This operation requires permissions for the <code>lex:PutIntent</code> action.</p>

        Args:
            name: <p>The name of the intent. The name is <i>not</i> case sensitive. </p> <p>The name can't match a built-in intent name, or a built-in intent name with "AMAZON." removed. For example, because there is a built-in intent called <code>AMAZON.HelpIntent</code>, you can't create a custom intent called <code>HelpIntent</code>.</p> <p>For a list of built-in intents, see <a href="https://developer.amazon.com/public/solutions/alexa/alexa-skills-kit/docs/built-in-intent-ref/standard-intents">Standard Built-in Intents</a> in the <i>Alexa Skills Kit</i>.</p>
            description: <p>A description of the intent.</p>
            slots: <p>An array of intent slots. At runtime, Amazon Lex elicits required slot values from the user using prompts defined in the slots. For more information, see <a>how-it-works</a>. </p>
            sample_utterances: <p>An array of utterances (strings) that a user might say to signal the intent. For example, "I want {PizzaSize} pizza", "Order {Quantity} {PizzaSize} pizzas". </p> <p>In each utterance, a slot name is enclosed in curly braces. </p>
            confirmation_prompt: <p>Prompts the user to confirm the intent. This question should have a yes or no answer.</p> <p>Amazon Lex uses this prompt to ensure that the user acknowledges that the intent is ready for fulfillment. For example, with the <code>OrderPizza</code> intent, you might want to confirm that the order is correct before placing it. For other intents, such as intents that simply respond to user questions, you might not need to ask the user for confirmation before providing the information. </p> <note> <p>You you must provide both the <code>rejectionStatement</code> and the <code>confirmationPrompt</code>, or neither.</p> </note>
            rejection_statement: <p>When the user answers "no" to the question defined in <code>confirmationPrompt</code>, Amazon Lex responds with this statement to acknowledge that the intent was canceled. </p> <note> <p>You must provide both the <code>rejectionStatement</code> and the <code>confirmationPrompt</code>, or neither.</p> </note>
            follow_up_prompt: <p>Amazon Lex uses this prompt to solicit additional activity after fulfilling an intent. For example, after the <code>OrderPizza</code> intent is fulfilled, you might prompt the user to order a drink.</p> <p>The action that Amazon Lex takes depends on the user's response, as follows:</p> <ul> <li> <p>If the user says "Yes" it responds with the clarification prompt that is configured for the bot.</p> </li> <li> <p>if the user says "Yes" and continues with an utterance that triggers an intent it starts a conversation for the intent.</p> </li> <li> <p>If the user says "No" it responds with the rejection statement configured for the the follow-up prompt.</p> </li> <li> <p>If it doesn't recognize the utterance it repeats the follow-up prompt again.</p> </li> </ul> <p>The <code>followUpPrompt</code> field and the <code>conclusionStatement</code> field are mutually exclusive. You can specify only one. </p>
            conclusion_statement: <p> The statement that you want Amazon Lex to convey to the user after the intent is successfully fulfilled by the Lambda function. </p> <p>This element is relevant only if you provide a Lambda function in the <code>fulfillmentActivity</code>. If you return the intent to the client application, you can't specify this element.</p> <note> <p>The <code>followUpPrompt</code> and <code>conclusionStatement</code> are mutually exclusive. You can specify only one.</p> </note>
            dialog_code_hook: <p> Specifies a Lambda function to invoke for each user input. You can invoke this Lambda function to personalize user interaction. </p> <p>For example, suppose your bot determines that the user is John. Your Lambda function might retrieve John's information from a backend database and prepopulate some of the values. For example, if you find that John is gluten intolerant, you might set the corresponding intent slot, <code>GlutenIntolerant</code>, to true. You might find John's phone number and set the corresponding session attribute. </p>
            fulfillment_activity: <p>Required. Describes how the intent is fulfilled. For example, after a user provides all of the information for a pizza order, <code>fulfillmentActivity</code> defines how the bot places an order with a local pizza store. </p> <p> You might configure Amazon Lex to return all of the intent information to the client application, or direct it to invoke a Lambda function that can process the intent (for example, place an order with a pizzeria). </p>
            parent_intent_signature: <p>A unique identifier for the built-in intent to base this intent on. To find the signature for an intent, see <a href="https://developer.amazon.com/public/solutions/alexa/alexa-skills-kit/docs/built-in-intent-ref/standard-intents">Standard Built-in Intents</a> in the <i>Alexa Skills Kit</i>.</p>
            checksum: <p>Identifies a specific revision of the <code>$LATEST</code> version.</p> <p>When you create a new intent, leave the <code>checksum</code> field blank. If you specify a checksum you get a <code>BadRequestException</code> exception.</p> <p>When you want to update a intent, set the <code>checksum</code> field to the checksum of the most recent revision of the <code>$LATEST</code> version. If you don't specify the <code> checksum</code> field, or if the checksum does not match the <code>$LATEST</code> version, you get a <code>PreconditionFailedException</code> exception.</p>
            create_version: <p>When set to <code>true</code> a new numbered version of the intent is created. This is the same as calling the <code>CreateIntentVersion</code> operation. If you do not specify <code>createVersion</code>, the default is <code>false</code>.</p>
            kendra_configuration: <p>Configuration information required to use the <code>AMAZON.KendraSearchIntent</code> intent to connect to an Amazon Kendra index. For more information, see <a href="http://docs.aws.amazon.com/lex/latest/dg/built-in-intent-kendra-search.html"> AMAZON.KendraSearchIntent</a>.</p>
            input_contexts: <p>An array of <code>InputContext</code> objects that lists the contexts that must be active for Amazon Lex to choose the intent in a conversation with the user.</p>
            output_contexts: <p>An array of <code>OutputContext</code> objects that lists the contexts that the intent activates when the intent is fulfilled.</p>

        Raises:
            capo_lex_model_building_service.errors.bad_request_exception.BadRequestException: <p>The request is not well formed. For example, a value is invalid or a required field is missing. Check the field values, and try again.</p>
            capo_lex_model_building_service.errors.conflict_exception.ConflictException: <p> There was a conflict processing the request. Try your request again. </p>
            capo_lex_model_building_service.errors.internal_failure_exception.InternalFailureException: <p>An internal Amazon Lex error occurred. Try your request again.</p>
            capo_lex_model_building_service.errors.limit_exceeded_exception.LimitExceededException: <p>The request exceeded a limit. Try your request again.</p>
            capo_lex_model_building_service.errors.precondition_failed_exception.PreconditionFailedException: <p> The checksum of the resource that you are trying to change does not match the checksum in the request. Check the resource's checksum and try again.</p>
            capo_lex_model_building_service.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To create an intent
            This example shows how to create an intent for ordering pizzas.

            >>> await client.put_intent(name='DocOrderPizza', description='Order a pizza from a local pizzeria.', slots=[{'name': 'Type', 'description': 'The type of pizza to order.', 'slotConstraint': 'Required', 'slotType': 'DocPizzaType', 'slotTypeVersion': '$LATEST', 'valueElicitationPrompt': {'messages': [{'contentType': 'PlainText', 'content': 'What type of pizza would you like?'}, {'contentType': 'PlainText', 'content': 'Vegie or cheese pizza?'}, {'contentType': 'PlainText', 'content': 'I can get you a vegie or a cheese pizza.'}], 'maxAttempts': 1}, 'priority': 1, 'sampleUtterances': ['Get me a {Type} pizza.', 'A {Type} pizza please.', "I'd like a {Type} pizza."]}, {'name': 'Crust', 'description': 'The type of pizza crust to order.', 'slotConstraint': 'Required', 'slotType': 'DocPizzaCrustType', 'slotTypeVersion': '$LATEST', 'valueElicitationPrompt': {'messages': [{'contentType': 'PlainText', 'content': 'What type of crust would you like?'}, {'contentType': 'PlainText', 'content': 'Thick or thin crust?'}], 'maxAttempts': 1}, 'priority': 2, 'sampleUtterances': ['Make it a {Crust} crust.', "I'd like a {Crust} crust."]}, {'name': 'Sauce', 'description': 'The type of sauce to use on the pizza.', 'slotConstraint': 'Required', 'slotType': 'DocPizzaSauceType', 'slotTypeVersion': '$LATEST', 'valueElicitationPrompt': {'messages': [{'contentType': 'PlainText', 'content': 'White or red sauce?'}, {'contentType': 'PlainText', 'content': 'Garlic or tomato sauce?'}], 'maxAttempts': 1}, 'priority': 3, 'sampleUtterances': ['Make it {Sauce} sauce.', "I'd like {Sauce} sauce."]}], sample_utterances=['Order me a pizza.', 'Order me a {Type} pizza.', 'I want a {Crust} crust {Type} pizza', 'I want a {Crust} crust {Type} pizza with {Sauce} sauce.'], confirmation_prompt={'messages': [{'contentType': 'PlainText', 'content': 'Should I order  your {Crust} crust {Type} pizza with {Sauce} sauce?'}], 'maxAttempts': 1}, rejection_statement={'messages': [{'contentType': 'PlainText', 'content': "Ok, I'll cancel your order."}, {'contentType': 'PlainText', 'content': 'I cancelled your order.'}]}, conclusion_statement={'messages': [{'contentType': 'PlainText', 'content': 'All right, I ordered  you a {Crust} crust {Type} pizza with {Sauce} sauce.'}, {'contentType': 'PlainText', 'content': 'OK, your {Crust} crust {Type} pizza with {Sauce} sauce is on the way.'}], 'responseCard': 'foo'}, fulfillment_activity={'type': 'ReturnIntent'})
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lex_model_building_service.types.put_intent_request.PutIntentRequest]",
        ) -> AsyncOperationResponse[
            "capo_lex_model_building_service.types.put_intent_response.PutIntentResponse"
        ]:
            import capo_lex_model_building_service._operations.aws_deep_sense_model_building_service.put_intent

            (
                output,
                http_response,
            ) = await capo_lex_model_building_service._operations.aws_deep_sense_model_building_service.put_intent.async_put_intent(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lex_model_building_service.types.put_intent_request.PutIntentRequest = {
            "name": name
        }
        if description is not None:
            input_["description"] = description
        if slots is not None:
            input_["slots"] = slots
        if sample_utterances is not None:
            input_["sample_utterances"] = sample_utterances
        if confirmation_prompt is not None:
            input_["confirmation_prompt"] = confirmation_prompt
        if rejection_statement is not None:
            input_["rejection_statement"] = rejection_statement
        if follow_up_prompt is not None:
            input_["follow_up_prompt"] = follow_up_prompt
        if conclusion_statement is not None:
            input_["conclusion_statement"] = conclusion_statement
        if dialog_code_hook is not None:
            input_["dialog_code_hook"] = dialog_code_hook
        if fulfillment_activity is not None:
            input_["fulfillment_activity"] = fulfillment_activity
        if parent_intent_signature is not None:
            input_["parent_intent_signature"] = parent_intent_signature
        if checksum is not None:
            input_["checksum"] = checksum
        if create_version is not None:
            input_["create_version"] = create_version
        if kendra_configuration is not None:
            input_["kendra_configuration"] = kendra_configuration
        if input_contexts is not None:
            input_["input_contexts"] = input_contexts
        if output_contexts is not None:
            input_["output_contexts"] = output_contexts

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def put_slot_type(
        self,
        name: "capo_lex_model_building_service.types.slot_type_name.SlotTypeName",
        *,
        config_overrides: Optional[AsyncLexModelBuildingServiceClientConfig] = None,
        description: Optional[
            "capo_lex_model_building_service.types.description.Description"
        ] = None,
        enumeration_values: Optional[
            "capo_lex_model_building_service.types.enumeration_values.EnumerationValues"
        ] = None,
        checksum: Optional[
            "capo_lex_model_building_service.types.string.String"
        ] = None,
        value_selection_strategy: Optional[
            "capo_lex_model_building_service.types.slot_value_selection_strategy.SlotValueSelectionStrategy"
        ] = None,
        create_version: Optional[
            "capo_lex_model_building_service.types.boolean.Boolean"
        ] = None,
        parent_slot_type_signature: Optional[
            "capo_lex_model_building_service.types.custom_or_builtin_slot_type_name.CustomOrBuiltinSlotTypeName"
        ] = None,
        slot_type_configurations: Optional[
            "capo_lex_model_building_service.types.slot_type_configurations.SlotTypeConfigurations"
        ] = None,
    ) -> "capo_lex_model_building_service.types.put_slot_type_response.PutSlotTypeResponse":
        """<p>Creates a custom slot type or replaces an existing custom slot type.</p> <p>To create a custom slot type, specify a name for the slot type and a set of enumeration values, which are the values that a slot of this type can assume. For more information, see <a>how-it-works</a>.</p> <p>If you specify the name of an existing slot type, the fields in the request replace the existing values in the <code>$LATEST</code> version of the slot type. Amazon Lex removes the fields that you don't provide in the request. If you don't specify required fields, Amazon Lex throws an exception. When you update the <code>$LATEST</code> version of a slot type, if a bot uses the <code>$LATEST</code> version of an intent that contains the slot type, the bot's <code>status</code> field is set to <code>NOT_BUILT</code>.</p> <p>This operation requires permissions for the <code>lex:PutSlotType</code> action.</p>

        Args:
            name: <p>The name of the slot type. The name is <i>not</i> case sensitive. </p> <p>The name can't match a built-in slot type name, or a built-in slot type name with "AMAZON." removed. For example, because there is a built-in slot type called <code>AMAZON.DATE</code>, you can't create a custom slot type called <code>DATE</code>.</p> <p>For a list of built-in slot types, see <a href="https://developer.amazon.com/public/solutions/alexa/alexa-skills-kit/docs/built-in-intent-ref/slot-type-reference">Slot Type Reference</a> in the <i>Alexa Skills Kit</i>.</p>
            description: <p>A description of the slot type.</p>
            enumeration_values: <p>A list of <code>EnumerationValue</code> objects that defines the values that the slot type can take. Each value can have a list of <code>synonyms</code>, which are additional values that help train the machine learning model about the values that it resolves for a slot. </p> <p>A regular expression slot type doesn't require enumeration values. All other slot types require a list of enumeration values.</p> <p>When Amazon Lex resolves a slot value, it generates a resolution list that contains up to five possible values for the slot. If you are using a Lambda function, this resolution list is passed to the function. If you are not using a Lambda function you can choose to return the value that the user entered or the first value in the resolution list as the slot value. The <code>valueSelectionStrategy</code> field indicates the option to use. </p>
            checksum: <p>Identifies a specific revision of the <code>$LATEST</code> version.</p> <p>When you create a new slot type, leave the <code>checksum</code> field blank. If you specify a checksum you get a <code>BadRequestException</code> exception.</p> <p>When you want to update a slot type, set the <code>checksum</code> field to the checksum of the most recent revision of the <code>$LATEST</code> version. If you don't specify the <code> checksum</code> field, or if the checksum does not match the <code>$LATEST</code> version, you get a <code>PreconditionFailedException</code> exception.</p>
            value_selection_strategy: <p>Determines the slot resolution strategy that Amazon Lex uses to return slot type values. The field can be set to one of the following values:</p> <ul> <li> <p> <code>ORIGINAL_VALUE</code> - Returns the value entered by the user, if the user value is similar to the slot value.</p> </li> <li> <p> <code>TOP_RESOLUTION</code> - If there is a resolution list for the slot, return the first value in the resolution list as the slot type value. If there is no resolution list, null is returned.</p> </li> </ul> <p>If you don't specify the <code>valueSelectionStrategy</code>, the default is <code>ORIGINAL_VALUE</code>.</p>
            create_version: <p>When set to <code>true</code> a new numbered version of the slot type is created. This is the same as calling the <code>CreateSlotTypeVersion</code> operation. If you do not specify <code>createVersion</code>, the default is <code>false</code>.</p>
            parent_slot_type_signature: <p>The built-in slot type used as the parent of the slot type. When you define a parent slot type, the new slot type has all of the same configuration as the parent.</p> <p>Only <code>AMAZON.AlphaNumeric</code> is supported.</p>
            slot_type_configurations: <p>Configuration information that extends the parent built-in slot type. The configuration is added to the settings for the parent slot type.</p>

        Raises:
            capo_lex_model_building_service.errors.bad_request_exception.BadRequestException: <p>The request is not well formed. For example, a value is invalid or a required field is missing. Check the field values, and try again.</p>
            capo_lex_model_building_service.errors.conflict_exception.ConflictException: <p> There was a conflict processing the request. Try your request again. </p>
            capo_lex_model_building_service.errors.internal_failure_exception.InternalFailureException: <p>An internal Amazon Lex error occurred. Try your request again.</p>
            capo_lex_model_building_service.errors.limit_exceeded_exception.LimitExceededException: <p>The request exceeded a limit. Try your request again.</p>
            capo_lex_model_building_service.errors.precondition_failed_exception.PreconditionFailedException: <p> The checksum of the resource that you are trying to change does not match the checksum in the request. Check the resource's checksum and try again.</p>
            capo_lex_model_building_service.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To Create a Slot Type
            This example shows how to create a slot type that describes pizza sauces.

            >>> await client.put_slot_type(name='PizzaSauceType', description='Available pizza sauces', enumeration_values=[{'value': 'red'}, {'value': 'white'}])
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lex_model_building_service.types.put_slot_type_request.PutSlotTypeRequest]",
        ) -> AsyncOperationResponse[
            "capo_lex_model_building_service.types.put_slot_type_response.PutSlotTypeResponse"
        ]:
            import capo_lex_model_building_service._operations.aws_deep_sense_model_building_service.put_slot_type

            (
                output,
                http_response,
            ) = await capo_lex_model_building_service._operations.aws_deep_sense_model_building_service.put_slot_type.async_put_slot_type(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lex_model_building_service.types.put_slot_type_request.PutSlotTypeRequest = {
            "name": name
        }
        if description is not None:
            input_["description"] = description
        if enumeration_values is not None:
            input_["enumeration_values"] = enumeration_values
        if checksum is not None:
            input_["checksum"] = checksum
        if value_selection_strategy is not None:
            input_["value_selection_strategy"] = value_selection_strategy
        if create_version is not None:
            input_["create_version"] = create_version
        if parent_slot_type_signature is not None:
            input_["parent_slot_type_signature"] = parent_slot_type_signature
        if slot_type_configurations is not None:
            input_["slot_type_configurations"] = slot_type_configurations

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def start_import(
        self,
        payload: "capo_lex_model_building_service.types.blob.Blob",
        resource_type: "capo_lex_model_building_service.types.resource_type.ResourceType",
        merge_strategy: "capo_lex_model_building_service.types.merge_strategy.MergeStrategy",
        *,
        config_overrides: Optional[AsyncLexModelBuildingServiceClientConfig] = None,
        tags: Optional["capo_lex_model_building_service.types.tag_list.TagList"] = None,
    ) -> "capo_lex_model_building_service.types.start_import_response.StartImportResponse":
        """<p>Starts a job to import a resource to Amazon Lex.</p>

        Args:
            payload: <p>A zip archive in binary format. The archive should contain one file, a JSON file containing the resource to import. The resource should match the type specified in the <code>resourceType</code> field.</p>
            resource_type: <p>Specifies the type of resource to export. Each resource also exports any resources that it depends on. </p> <ul> <li> <p>A bot exports dependent intents.</p> </li> <li> <p>An intent exports dependent slot types.</p> </li> </ul>
            merge_strategy: <p>Specifies the action that the <code>StartImport</code> operation should take when there is an existing resource with the same name.</p> <ul> <li> <p>FAIL_ON_CONFLICT - The import operation is stopped on the first conflict between a resource in the import file and an existing resource. The name of the resource causing the conflict is in the <code>failureReason</code> field of the response to the <code>GetImport</code> operation.</p> <p>OVERWRITE_LATEST - The import operation proceeds even if there is a conflict with an existing resource. The $LASTEST version of the existing resource is overwritten with the data from the import file.</p> </li> </ul>
            tags: <p>A list of tags to add to the imported bot. You can only add tags when you import a bot, you can't add tags to an intent or slot type.</p>

        Raises:
            capo_lex_model_building_service.errors.bad_request_exception.BadRequestException: <p>The request is not well formed. For example, a value is invalid or a required field is missing. Check the field values, and try again.</p>
            capo_lex_model_building_service.errors.internal_failure_exception.InternalFailureException: <p>An internal Amazon Lex error occurred. Try your request again.</p>
            capo_lex_model_building_service.errors.limit_exceeded_exception.LimitExceededException: <p>The request exceeded a limit. Try your request again.</p>
            capo_lex_model_building_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lex_model_building_service.types.start_import_request.StartImportRequest]",
        ) -> AsyncOperationResponse[
            "capo_lex_model_building_service.types.start_import_response.StartImportResponse"
        ]:
            import capo_lex_model_building_service._operations.aws_deep_sense_model_building_service.start_import

            (
                output,
                http_response,
            ) = await capo_lex_model_building_service._operations.aws_deep_sense_model_building_service.start_import.async_start_import(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lex_model_building_service.types.start_import_request.StartImportRequest = {
            "payload": payload,
            "resource_type": resource_type,
            "merge_strategy": merge_strategy,
        }
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def start_migration(
        self,
        v1_bot_name: "capo_lex_model_building_service.types.bot_name.BotName",
        v1_bot_version: "capo_lex_model_building_service.types.version.Version",
        v2_bot_name: "capo_lex_model_building_service.types.v2_bot_name.V2BotName",
        v2_bot_role: "capo_lex_model_building_service.types.iam_role_arn.IamRoleArn",
        migration_strategy: "capo_lex_model_building_service.types.migration_strategy.MigrationStrategy",
        *,
        config_overrides: Optional[AsyncLexModelBuildingServiceClientConfig] = None,
    ) -> "capo_lex_model_building_service.types.start_migration_response.StartMigrationResponse":
        """<p>Starts migrating a bot from Amazon Lex V1 to Amazon Lex V2. Migrate your bot when you want to take advantage of the new features of Amazon Lex V2.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/lex/latest/dg/migrate.html">Migrating a bot</a> in the <i>Amazon Lex developer guide</i>.</p>

        Args:
            v1_bot_name: <p>The name of the Amazon Lex V1 bot that you are migrating to Amazon Lex V2.</p>
            v1_bot_version: <p>The version of the bot to migrate to Amazon Lex V2. You can migrate the <code>$LATEST</code> version as well as any numbered version.</p>
            v2_bot_name: <p>The name of the Amazon Lex V2 bot that you are migrating the Amazon Lex V1 bot to. </p> <ul> <li> <p>If the Amazon Lex V2 bot doesn't exist, you must use the <code>CREATE_NEW</code> migration strategy.</p> </li> <li> <p>If the Amazon Lex V2 bot exists, you must use the <code>UPDATE_EXISTING</code> migration strategy to change the contents of the Amazon Lex V2 bot.</p> </li> </ul>
            v2_bot_role: <p>The IAM role that Amazon Lex uses to run the Amazon Lex V2 bot.</p>
            migration_strategy: <p>The strategy used to conduct the migration.</p> <ul> <li> <p> <code>CREATE_NEW</code> - Creates a new Amazon Lex V2 bot and migrates the Amazon Lex V1 bot to the new bot.</p> </li> <li> <p> <code>UPDATE_EXISTING</code> - Overwrites the existing Amazon Lex V2 bot metadata and the locale being migrated. It doesn't change any other locales in the Amazon Lex V2 bot. If the locale doesn't exist, a new locale is created in the Amazon Lex V2 bot.</p> </li> </ul>

        Raises:
            capo_lex_model_building_service.errors.access_denied_exception.AccessDeniedException: <p>Your IAM user or role does not have permission to call the Amazon Lex V2 APIs required to migrate your bot.</p>
            capo_lex_model_building_service.errors.bad_request_exception.BadRequestException: <p>The request is not well formed. For example, a value is invalid or a required field is missing. Check the field values, and try again.</p>
            capo_lex_model_building_service.errors.internal_failure_exception.InternalFailureException: <p>An internal Amazon Lex error occurred. Try your request again.</p>
            capo_lex_model_building_service.errors.limit_exceeded_exception.LimitExceededException: <p>The request exceeded a limit. Try your request again.</p>
            capo_lex_model_building_service.errors.not_found_exception.NotFoundException: <p>The resource specified in the request was not found. Check the resource and try again.</p>
            capo_lex_model_building_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lex_model_building_service.types.start_migration_request.StartMigrationRequest]",
        ) -> AsyncOperationResponse[
            "capo_lex_model_building_service.types.start_migration_response.StartMigrationResponse"
        ]:
            import capo_lex_model_building_service._operations.aws_deep_sense_model_building_service.start_migration

            (
                output,
                http_response,
            ) = await capo_lex_model_building_service._operations.aws_deep_sense_model_building_service.start_migration.async_start_migration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lex_model_building_service.types.start_migration_request.StartMigrationRequest = {
            "v1_bot_name": v1_bot_name,
            "v1_bot_version": v1_bot_version,
            "v2_bot_name": v2_bot_name,
            "v2_bot_role": v2_bot_role,
            "migration_strategy": migration_strategy,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def tag_resource(
        self,
        resource_arn: "capo_lex_model_building_service.types.amazon_resource_name.AmazonResourceName",
        tags: "capo_lex_model_building_service.types.tag_list.TagList",
        *,
        config_overrides: Optional[AsyncLexModelBuildingServiceClientConfig] = None,
    ) -> "capo_lex_model_building_service.types.tag_resource_response.TagResourceResponse":
        """<p>Adds the specified tags to the specified resource. If a tag key already exists, the existing value is replaced with the new value.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the bot, bot alias, or bot channel to tag.</p>
            tags: <p>A list of tag keys to add to the resource. If a tag key already exists, the existing value is replaced with the new value.</p>

        Raises:
            capo_lex_model_building_service.errors.bad_request_exception.BadRequestException: <p>The request is not well formed. For example, a value is invalid or a required field is missing. Check the field values, and try again.</p>
            capo_lex_model_building_service.errors.conflict_exception.ConflictException: <p> There was a conflict processing the request. Try your request again. </p>
            capo_lex_model_building_service.errors.internal_failure_exception.InternalFailureException: <p>An internal Amazon Lex error occurred. Try your request again.</p>
            capo_lex_model_building_service.errors.limit_exceeded_exception.LimitExceededException: <p>The request exceeded a limit. Try your request again.</p>
            capo_lex_model_building_service.errors.not_found_exception.NotFoundException: <p>The resource specified in the request was not found. Check the resource and try again.</p>
            capo_lex_model_building_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lex_model_building_service.types.tag_resource_request.TagResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_lex_model_building_service.types.tag_resource_response.TagResourceResponse"
        ]:
            import capo_lex_model_building_service._operations.aws_deep_sense_model_building_service.tag_resource

            (
                output,
                http_response,
            ) = await capo_lex_model_building_service._operations.aws_deep_sense_model_building_service.tag_resource.async_tag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lex_model_building_service.types.tag_resource_request.TagResourceRequest = {
            "resource_arn": resource_arn,
            "tags": tags,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def untag_resource(
        self,
        resource_arn: "capo_lex_model_building_service.types.amazon_resource_name.AmazonResourceName",
        tag_keys: "capo_lex_model_building_service.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[AsyncLexModelBuildingServiceClientConfig] = None,
    ) -> "capo_lex_model_building_service.types.untag_resource_response.UntagResourceResponse":
        """<p>Removes tags from a bot, bot alias or bot channel.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource to remove the tags from.</p>
            tag_keys: <p>A list of tag keys to remove from the resource. If a tag key does not exist on the resource, it is ignored.</p>

        Raises:
            capo_lex_model_building_service.errors.bad_request_exception.BadRequestException: <p>The request is not well formed. For example, a value is invalid or a required field is missing. Check the field values, and try again.</p>
            capo_lex_model_building_service.errors.conflict_exception.ConflictException: <p> There was a conflict processing the request. Try your request again. </p>
            capo_lex_model_building_service.errors.internal_failure_exception.InternalFailureException: <p>An internal Amazon Lex error occurred. Try your request again.</p>
            capo_lex_model_building_service.errors.limit_exceeded_exception.LimitExceededException: <p>The request exceeded a limit. Try your request again.</p>
            capo_lex_model_building_service.errors.not_found_exception.NotFoundException: <p>The resource specified in the request was not found. Check the resource and try again.</p>
            capo_lex_model_building_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lex_model_building_service.types.untag_resource_request.UntagResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_lex_model_building_service.types.untag_resource_response.UntagResourceResponse"
        ]:
            import capo_lex_model_building_service._operations.aws_deep_sense_model_building_service.untag_resource

            (
                output,
                http_response,
            ) = await capo_lex_model_building_service._operations.aws_deep_sense_model_building_service.untag_resource.async_untag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lex_model_building_service.types.untag_resource_request.UntagResourceRequest = {
            "resource_arn": resource_arn,
            "tag_keys": tag_keys,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(self, exc_type: Any, exc: Any, tb: Any):
        await self._client.aclose()
