"""Generated from Smithy shape ``com.amazonaws.workmailmessageflow#GiraffeMessageInTransitService``."""

import warnings
from collections.abc import Generator
from contextlib import contextmanager
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import BaseHandler, Client

import capo_workmailmessageflow._auth._signers
import capo_workmailmessageflow._auth._sigv4
from capo_workmailmessageflow._auth._identity import Credentials
from capo_workmailmessageflow._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_workmailmessageflow._auth._zapros_handler import AuthMiddleware
from capo_workmailmessageflow._services._aws_config import aws_config
from capo_workmailmessageflow._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import capo_workmailmessageflow.types.get_raw_message_content_request
    import capo_workmailmessageflow.types.get_raw_message_content_response
    import capo_workmailmessageflow.types.message_id_type
    import capo_workmailmessageflow.types.put_raw_message_content_request
    import capo_workmailmessageflow.types.put_raw_message_content_response
    import capo_workmailmessageflow.types.raw_message_content


class WorkMailMessageFlowClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None
    anonymous: bool | None


class WorkMailMessageFlowClient:
    """A client for the ``WorkMailMessageFlow`` service.

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
        http_handler: BaseHandler | None = None,
        operation_interceptors: Iterable[Interceptor[Any, Any]] | None = None,
        retry_max_attempts: int | None = None,
        region: str | None = None,
        use_dual_stack: bool | None = None,
        use_fips: bool | None = None,
        endpoint: str | None = None,
        credentials: Credentials | None = None,
        credentials_provider: CredentialsProvider | None = None,
        anonymous: bool | None = None,
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
        self._config = WorkMailMessageFlowClientConfig(
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
        self, config_overrides: Optional[WorkMailMessageFlowClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: WorkMailMessageFlowClientConfig = config_overrides or {}
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
            anonymous=overrides.get("anonymous", self._config.get("anonymous")),
        )
        return interceptors_, options_

    @contextmanager
    def get_raw_message_content(
        self,
        message_id: "capo_workmailmessageflow.types.message_id_type.messageIdType",
        *,
        config_overrides: Optional[WorkMailMessageFlowClientConfig] = None,
    ) -> "Generator[capo_workmailmessageflow.types.get_raw_message_content_response.GetRawMessageContentResponse]":
        """<p>Retrieves the raw content of an in-transit email message, in MIME format.</p>

        Args:
            message_id: <p>The identifier of the email message to retrieve.</p>

        Raises:
            capo_workmailmessageflow.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested email message is not found.</p>
            capo_workmailmessageflow.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_workmailmessageflow.types.get_raw_message_content_request.GetRawMessageContentRequest]",
        ) -> OperationResponse[
            "capo_workmailmessageflow.types.get_raw_message_content_response.GetRawMessageContentResponse"
        ]:
            import capo_workmailmessageflow._operations.giraffe_message_in_transit_service.get_raw_message_content

            output, http_response = (
                capo_workmailmessageflow._operations.giraffe_message_in_transit_service.get_raw_message_content.get_raw_message_content(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_workmailmessageflow.types.get_raw_message_content_request.GetRawMessageContentRequest = {
            "message_id": message_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        try:
            yield response.output
        finally:
            response.response.close()

    def put_raw_message_content(
        self,
        message_id: "capo_workmailmessageflow.types.message_id_type.messageIdType",
        content: "capo_workmailmessageflow.types.raw_message_content.RawMessageContent",
        *,
        config_overrides: Optional[WorkMailMessageFlowClientConfig] = None,
    ) -> "capo_workmailmessageflow.types.put_raw_message_content_response.PutRawMessageContentResponse":
        """<p>Updates the raw content of an in-transit email message, in MIME format.</p> <p>This example describes how to update in-transit email message. For more information and examples for using this API, see <a href="https://docs.aws.amazon.com/workmail/latest/adminguide/update-with-lambda.html"> Updating message content with AWS Lambda</a>.</p> <note> <p>Updates to an in-transit message only appear when you call <code>PutRawMessageContent</code> from an AWS Lambda function configured with a synchronous <a href="https://docs.aws.amazon.com/workmail/latest/adminguide/lambda.html#synchronous-rules"> Run Lambda</a> rule. If you call <code>PutRawMessageContent</code> on a delivered or sent message, the message remains unchanged, even though <a href="https://docs.aws.amazon.com/workmail/latest/APIReference/API_messageflow_GetRawMessageContent.html">GetRawMessageContent</a> returns an updated message. </p> </note>

        Args:
            message_id: <p>The identifier of the email message being updated.</p>
            content: <p>Describes the raw message content of the updated email message.</p>

        Raises:
            capo_workmailmessageflow.errors.invalid_content_location.InvalidContentLocation: <p>WorkMail could not access the updated email content. Possible reasons:</p> <ul> <li> <p>You made the request in a region other than your S3 bucket region.</p> </li> <li> <p>The <a href="https://docs.aws.amazon.com/AmazonS3/latest/dev/bucket-owner-condition.html">S3 bucket owner</a> is not the same as the calling AWS account.</p> </li> <li> <p>You have an incomplete or missing S3 bucket policy. For more information about policies, see <a href="https://docs.aws.amazon.com/workmail/latest/adminguide/update-with-lambda.html"> Updating message content with AWS Lambda </a> in the <i>WorkMail Administrator Guide</i>.</p> </li> </ul>
            capo_workmailmessageflow.errors.message_frozen.MessageFrozen: <p>The requested email is not eligible for update. This is usually the case for a redirected email.</p>
            capo_workmailmessageflow.errors.message_rejected.MessageRejected: <p>The requested email could not be updated due to an error in the MIME content. Check the error message for more information about what caused the error.</p>
            capo_workmailmessageflow.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested email message is not found.</p>
            capo_workmailmessageflow.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_workmailmessageflow.types.put_raw_message_content_request.PutRawMessageContentRequest]",
        ) -> OperationResponse[
            "capo_workmailmessageflow.types.put_raw_message_content_response.PutRawMessageContentResponse"
        ]:
            import capo_workmailmessageflow._operations.giraffe_message_in_transit_service.put_raw_message_content

            output, http_response = (
                capo_workmailmessageflow._operations.giraffe_message_in_transit_service.put_raw_message_content.put_raw_message_content(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_workmailmessageflow.types.put_raw_message_content_request.PutRawMessageContentRequest = {
            "message_id": message_id,
            "content": content,
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
