"""Generated from Smithy shape ``com.amazonaws.personalizeevents#AmazonPersonalizeEvents``."""

import warnings
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import BaseHandler, Client

import capo_personalize_events._auth._signers
import capo_personalize_events._auth._sigv4
from capo_personalize_events._auth._identity import Credentials
from capo_personalize_events._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_personalize_events._auth._zapros_handler import AuthMiddleware
from capo_personalize_events._services._aws_config import aws_config
from capo_personalize_events._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import capo_personalize_events.types.action_interactions_list
    import capo_personalize_events.types.action_list
    import capo_personalize_events.types.arn
    import capo_personalize_events.types.event_list
    import capo_personalize_events.types.item_list
    import capo_personalize_events.types.put_action_interactions_request
    import capo_personalize_events.types.put_actions_request
    import capo_personalize_events.types.put_events_request
    import capo_personalize_events.types.put_items_request
    import capo_personalize_events.types.put_users_request
    import capo_personalize_events.types.string_type
    import capo_personalize_events.types.user_id
    import capo_personalize_events.types.user_list


class PersonalizeEventsClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class PersonalizeEventsClient:
    """A client for the ``PersonalizeEvents`` service.

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
        self._config = PersonalizeEventsClientConfig(
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

    def operation_options(
        self, config_overrides: Optional[PersonalizeEventsClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: PersonalizeEventsClientConfig = config_overrides or {}
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

    def put_action_interactions(
        self,
        tracking_id: "capo_personalize_events.types.string_type.StringType",
        action_interactions: "capo_personalize_events.types.action_interactions_list.ActionInteractionsList",
        *,
        config_overrides: Optional[PersonalizeEventsClientConfig] = None,
    ) -> None:
        """<p>Records action interaction event data. An <i>action interaction</i> event is an interaction between a user and an <i>action</i>. For example, a user taking an action, such a enrolling in a membership program or downloading your app.</p> <p> For more information about recording action interactions, see <a href="https://docs.aws.amazon.com/personalize/latest/dg/recording-action-interaction-events.html">Recording action interaction events</a>. For more information about actions in an Actions dataset, see <a href="https://docs.aws.amazon.com/personalize/latest/dg/actions-datasets.html">Actions dataset</a>.</p>

        Args:
            tracking_id: <p>The ID of your action interaction event tracker. When you create an Action interactions dataset, Amazon Personalize creates an action interaction event tracker for you. For more information, see <a href="https://docs.aws.amazon.com/personalize/latest/dg/action-interaction-tracker-id.html">Action interaction event tracker ID</a>.</p>
            action_interactions: <p>A list of action interaction events from the session.</p>

        Raises:
            capo_personalize_events.errors.invalid_input_exception.InvalidInputException: <p>Provide a valid value for the field or parameter.</p>
            capo_personalize_events.errors.resource_in_use_exception.ResourceInUseException: <p>The specified resource is in use.</p>
            capo_personalize_events.errors.resource_not_found_exception.ResourceNotFoundException: <p>Could not find the specified resource.</p>
            capo_personalize_events.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_personalize_events.types.put_action_interactions_request.PutActionInteractionsRequest]",
        ) -> OperationResponse[None]:
            import capo_personalize_events._operations.amazon_personalize_events.put_action_interactions

            output, http_response = (
                capo_personalize_events._operations.amazon_personalize_events.put_action_interactions.put_action_interactions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_personalize_events.types.put_action_interactions_request.PutActionInteractionsRequest = {
            "tracking_id": tracking_id,
            "action_interactions": action_interactions,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def put_actions(
        self,
        dataset_arn: "capo_personalize_events.types.arn.Arn",
        actions: "capo_personalize_events.types.action_list.ActionList",
        *,
        config_overrides: Optional[PersonalizeEventsClientConfig] = None,
    ) -> None:
        """<p>Adds one or more actions to an Actions dataset. For more information see <a href="https://docs.aws.amazon.com/personalize/latest/dg/importing-actions.html">Importing actions individually</a>. </p>

        Args:
            dataset_arn: <p>The Amazon Resource Name (ARN) of the Actions dataset you are adding the action or actions to.</p>
            actions: <p>A list of action data.</p>

        Raises:
            capo_personalize_events.errors.invalid_input_exception.InvalidInputException: <p>Provide a valid value for the field or parameter.</p>
            capo_personalize_events.errors.resource_in_use_exception.ResourceInUseException: <p>The specified resource is in use.</p>
            capo_personalize_events.errors.resource_not_found_exception.ResourceNotFoundException: <p>Could not find the specified resource.</p>
            capo_personalize_events.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_personalize_events.types.put_actions_request.PutActionsRequest]",
        ) -> OperationResponse[None]:
            import capo_personalize_events._operations.amazon_personalize_events.put_actions

            output, http_response = (
                capo_personalize_events._operations.amazon_personalize_events.put_actions.put_actions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_personalize_events.types.put_actions_request.PutActionsRequest = {
            "dataset_arn": dataset_arn,
            "actions": actions,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def put_events(
        self,
        tracking_id: "capo_personalize_events.types.string_type.StringType",
        session_id: "capo_personalize_events.types.string_type.StringType",
        event_list: "capo_personalize_events.types.event_list.EventList",
        *,
        config_overrides: Optional[PersonalizeEventsClientConfig] = None,
        user_id: Optional["capo_personalize_events.types.user_id.UserId"] = None,
    ) -> None:
        """<p>Records item interaction event data. For more information see <a href="https://docs.aws.amazon.com/personalize/latest/dg/recording-item-interaction-events.html">Recording item interaction events</a>.</p>

        Args:
            tracking_id: <p>The tracking ID for the event. The ID is generated by a call to the <a href="https://docs.aws.amazon.com/personalize/latest/dg/API_CreateEventTracker.html">CreateEventTracker</a> API.</p>
            user_id: <p>The user associated with the event.</p>
            session_id: <p>The session ID associated with the user's visit. Your application generates the sessionId when a user first visits your website or uses your application. Amazon Personalize uses the sessionId to associate events with the user before they log in. For more information, see <a href="https://docs.aws.amazon.com/personalize/latest/dg/recording-item-interaction-events.html">Recording item interaction events</a>.</p>
            event_list: <p>A list of event data from the session.</p>

        Raises:
            capo_personalize_events.errors.invalid_input_exception.InvalidInputException: <p>Provide a valid value for the field or parameter.</p>
            capo_personalize_events.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_personalize_events.types.put_events_request.PutEventsRequest]",
        ) -> OperationResponse[None]:
            import capo_personalize_events._operations.amazon_personalize_events.put_events

            output, http_response = (
                capo_personalize_events._operations.amazon_personalize_events.put_events.put_events(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_personalize_events.types.put_events_request.PutEventsRequest = {
            "tracking_id": tracking_id,
            "session_id": session_id,
            "event_list": event_list,
        }
        if user_id is not None:
            input_["user_id"] = user_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def put_items(
        self,
        dataset_arn: "capo_personalize_events.types.arn.Arn",
        items: "capo_personalize_events.types.item_list.ItemList",
        *,
        config_overrides: Optional[PersonalizeEventsClientConfig] = None,
    ) -> None:
        """<p>Adds one or more items to an Items dataset. For more information see <a href="https://docs.aws.amazon.com/personalize/latest/dg/importing-items.html">Importing items individually</a>. </p>

        Args:
            dataset_arn: <p>The Amazon Resource Name (ARN) of the Items dataset you are adding the item or items to.</p>
            items: <p>A list of item data.</p>

        Raises:
            capo_personalize_events.errors.invalid_input_exception.InvalidInputException: <p>Provide a valid value for the field or parameter.</p>
            capo_personalize_events.errors.resource_in_use_exception.ResourceInUseException: <p>The specified resource is in use.</p>
            capo_personalize_events.errors.resource_not_found_exception.ResourceNotFoundException: <p>Could not find the specified resource.</p>
            capo_personalize_events.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_personalize_events.types.put_items_request.PutItemsRequest]",
        ) -> OperationResponse[None]:
            import capo_personalize_events._operations.amazon_personalize_events.put_items

            output, http_response = (
                capo_personalize_events._operations.amazon_personalize_events.put_items.put_items(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_personalize_events.types.put_items_request.PutItemsRequest = {
            "dataset_arn": dataset_arn,
            "items": items,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def put_users(
        self,
        dataset_arn: "capo_personalize_events.types.arn.Arn",
        users: "capo_personalize_events.types.user_list.UserList",
        *,
        config_overrides: Optional[PersonalizeEventsClientConfig] = None,
    ) -> None:
        """<p>Adds one or more users to a Users dataset. For more information see <a href="https://docs.aws.amazon.com/personalize/latest/dg/importing-users.html">Importing users individually</a>.</p>

        Args:
            dataset_arn: <p>The Amazon Resource Name (ARN) of the Users dataset you are adding the user or users to.</p>
            users: <p>A list of user data.</p>

        Raises:
            capo_personalize_events.errors.invalid_input_exception.InvalidInputException: <p>Provide a valid value for the field or parameter.</p>
            capo_personalize_events.errors.resource_in_use_exception.ResourceInUseException: <p>The specified resource is in use.</p>
            capo_personalize_events.errors.resource_not_found_exception.ResourceNotFoundException: <p>Could not find the specified resource.</p>
            capo_personalize_events.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_personalize_events.types.put_users_request.PutUsersRequest]",
        ) -> OperationResponse[None]:
            import capo_personalize_events._operations.amazon_personalize_events.put_users

            output, http_response = (
                capo_personalize_events._operations.amazon_personalize_events.put_users.put_users(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_personalize_events.types.put_users_request.PutUsersRequest = {
            "dataset_arn": dataset_arn,
            "users": users,
        }

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
