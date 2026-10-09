"""Generated from Smithy shape ``com.amazonaws.codegurureviewer#AWSGuruFrontendService``."""

import uuid
import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import AsyncBaseHandler, AsyncClient

import capo_codeguru_reviewer._auth._signers
import capo_codeguru_reviewer._auth._sigv4
from capo_codeguru_reviewer._auth._identity import Credentials
from capo_codeguru_reviewer._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_codeguru_reviewer._auth._zapros_handler import AuthMiddleware
from capo_codeguru_reviewer._pagination import resolve_path as _resolve_path
from capo_codeguru_reviewer._services._aws_config import aaws_config
from capo_codeguru_reviewer._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import capo_codeguru_reviewer.types.arn
    import capo_codeguru_reviewer.types.associate_repository_request
    import capo_codeguru_reviewer.types.associate_repository_response
    import capo_codeguru_reviewer.types.association_arn
    import capo_codeguru_reviewer.types.client_request_token
    import capo_codeguru_reviewer.types.code_review_name
    import capo_codeguru_reviewer.types.code_review_type
    import capo_codeguru_reviewer.types.create_code_review_request
    import capo_codeguru_reviewer.types.create_code_review_response
    import capo_codeguru_reviewer.types.describe_code_review_request
    import capo_codeguru_reviewer.types.describe_code_review_response
    import capo_codeguru_reviewer.types.describe_recommendation_feedback_request
    import capo_codeguru_reviewer.types.describe_recommendation_feedback_response
    import capo_codeguru_reviewer.types.describe_repository_association_request
    import capo_codeguru_reviewer.types.describe_repository_association_response
    import capo_codeguru_reviewer.types.disassociate_repository_request
    import capo_codeguru_reviewer.types.disassociate_repository_response
    import capo_codeguru_reviewer.types.job_states
    import capo_codeguru_reviewer.types.kms_key_details
    import capo_codeguru_reviewer.types.list_code_reviews_max_results
    import capo_codeguru_reviewer.types.list_code_reviews_request
    import capo_codeguru_reviewer.types.list_code_reviews_response
    import capo_codeguru_reviewer.types.list_recommendation_feedback_request
    import capo_codeguru_reviewer.types.list_recommendation_feedback_response
    import capo_codeguru_reviewer.types.list_recommendations_max_results
    import capo_codeguru_reviewer.types.list_recommendations_request
    import capo_codeguru_reviewer.types.list_recommendations_response
    import capo_codeguru_reviewer.types.list_repository_associations_request
    import capo_codeguru_reviewer.types.list_repository_associations_response
    import capo_codeguru_reviewer.types.list_tags_for_resource_request
    import capo_codeguru_reviewer.types.list_tags_for_resource_response
    import capo_codeguru_reviewer.types.max_results
    import capo_codeguru_reviewer.types.names
    import capo_codeguru_reviewer.types.next_token
    import capo_codeguru_reviewer.types.owners
    import capo_codeguru_reviewer.types.provider_types
    import capo_codeguru_reviewer.types.put_recommendation_feedback_request
    import capo_codeguru_reviewer.types.put_recommendation_feedback_response
    import capo_codeguru_reviewer.types.reactions
    import capo_codeguru_reviewer.types.recommendation_id
    import capo_codeguru_reviewer.types.recommendation_ids
    import capo_codeguru_reviewer.types.repository
    import capo_codeguru_reviewer.types.repository_association_states
    import capo_codeguru_reviewer.types.repository_association_summary
    import capo_codeguru_reviewer.types.repository_names
    import capo_codeguru_reviewer.types.tag_key_list
    import capo_codeguru_reviewer.types.tag_map
    import capo_codeguru_reviewer.types.tag_resource_request
    import capo_codeguru_reviewer.types.tag_resource_response
    import capo_codeguru_reviewer.types.type
    import capo_codeguru_reviewer.types.untag_resource_request
    import capo_codeguru_reviewer.types.untag_resource_response
    import capo_codeguru_reviewer.types.user_id
    import capo_codeguru_reviewer.types.user_ids


class AsyncCodeGuruReviewerClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None
    anonymous: bool | None


class AsyncCodeGuruReviewerClient:
    """A client for the ``CodeGuruReviewer`` service.

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
        self._config = AsyncCodeGuruReviewerClientConfig(
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
        self, config_overrides: Optional[AsyncCodeGuruReviewerClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncCodeGuruReviewerClientConfig = config_overrides or {}
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

    async def associate_repository(
        self,
        repository: "capo_codeguru_reviewer.types.repository.Repository",
        *,
        config_overrides: Optional[AsyncCodeGuruReviewerClientConfig] = None,
        client_request_token: Optional[
            "capo_codeguru_reviewer.types.client_request_token.ClientRequestToken"
        ] = None,
        tags: Optional["capo_codeguru_reviewer.types.tag_map.TagMap"] = None,
        kms_key_details: Optional[
            "capo_codeguru_reviewer.types.kms_key_details.KMSKeyDetails"
        ] = None,
    ) -> "capo_codeguru_reviewer.types.associate_repository_response.AssociateRepositoryResponse":
        """<p>Use to associate an Amazon Web Services CodeCommit repository or a repository managed by Amazon Web Services CodeStar Connections with Amazon CodeGuru Reviewer. When you associate a repository, CodeGuru Reviewer reviews source code changes in the repository's pull requests and provides automatic recommendations. You can view recommendations using the CodeGuru Reviewer console. For more information, see <a href="https://docs.aws.amazon.com/codeguru/latest/reviewer-ug/recommendations.html">Recommendations in Amazon CodeGuru Reviewer</a> in the <i>Amazon CodeGuru Reviewer User Guide.</i> </p> <p>If you associate a CodeCommit or S3 repository, it must be in the same Amazon Web Services Region and Amazon Web Services account where its CodeGuru Reviewer code reviews are configured.</p> <p>Bitbucket and GitHub Enterprise Server repositories are managed by Amazon Web Services CodeStar Connections to connect to CodeGuru Reviewer. For more information, see <a href="https://docs.aws.amazon.com/codeguru/latest/reviewer-ug/getting-started-associate-repository.html">Associate a repository</a> in the <i>Amazon CodeGuru Reviewer User Guide.</i> </p> <note> <p>You cannot use the CodeGuru Reviewer SDK or the Amazon Web Services CLI to associate a GitHub repository with Amazon CodeGuru Reviewer. To associate a GitHub repository, use the console. For more information, see <a href="https://docs.aws.amazon.com/codeguru/latest/reviewer-ug/getting-started-with-guru.html">Getting started with CodeGuru Reviewer</a> in the <i>CodeGuru Reviewer User Guide.</i> </p> </note>

        Args:
            repository: <p>The repository to associate.</p>
            client_request_token: <p>Amazon CodeGuru Reviewer uses this value to prevent the accidental creation of duplicate repository associations if there are failures and retries.</p>
            tags: <p>An array of key-value pairs used to tag an associated repository. A tag is a custom attribute label with two parts:</p> <ul> <li> <p>A <i>tag key</i> (for example, <code>CostCenter</code>, <code>Environment</code>, <code>Project</code>, or <code>Secret</code>). Tag keys are case sensitive.</p> </li> <li> <p>An optional field known as a <i>tag value</i> (for example, <code>111122223333</code>, <code>Production</code>, or a team name). Omitting the tag value is the same as using an empty string. Like tag keys, tag values are case sensitive.</p> </li> </ul>
            kms_key_details: <p>A <code>KMSKeyDetails</code> object that contains:</p> <ul> <li> <p>The encryption option for this repository association. It is either owned by Amazon Web Services Key Management Service (KMS) (<code>AWS_OWNED_CMK</code>) or customer managed (<code>CUSTOMER_MANAGED_CMK</code>).</p> </li> <li> <p>The ID of the Amazon Web Services KMS key that is associated with this repository association.</p> </li> </ul>

        Raises:
            capo_codeguru_reviewer.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_codeguru_reviewer.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. </p>
            capo_codeguru_reviewer.errors.internal_server_exception.InternalServerException: <p>The server encountered an internal error and is unable to complete the request.</p>
            capo_codeguru_reviewer.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_codeguru_reviewer.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_codeguru_reviewer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_codeguru_reviewer.types.associate_repository_request.AssociateRepositoryRequest]",
        ) -> AsyncOperationResponse[
            "capo_codeguru_reviewer.types.associate_repository_response.AssociateRepositoryResponse"
        ]:
            import capo_codeguru_reviewer._operations.aws_guru_frontend_service.associate_repository

            (
                output,
                http_response,
            ) = await capo_codeguru_reviewer._operations.aws_guru_frontend_service.associate_repository.async_associate_repository(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codeguru_reviewer.types.associate_repository_request.AssociateRepositoryRequest = {
            "repository": repository
        }
        if client_request_token is None:
            client_request_token = str(uuid.uuid4())
        input_["client_request_token"] = client_request_token
        if tags is not None:
            input_["tags"] = tags
        if kms_key_details is not None:
            input_["kms_key_details"] = kms_key_details

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_code_review(
        self,
        name: "capo_codeguru_reviewer.types.code_review_name.CodeReviewName",
        repository_association_arn: "capo_codeguru_reviewer.types.association_arn.AssociationArn",
        type: "capo_codeguru_reviewer.types.code_review_type.CodeReviewType",
        *,
        config_overrides: Optional[AsyncCodeGuruReviewerClientConfig] = None,
        client_request_token: Optional[
            "capo_codeguru_reviewer.types.client_request_token.ClientRequestToken"
        ] = None,
    ) -> "capo_codeguru_reviewer.types.create_code_review_response.CreateCodeReviewResponse":
        """<p>Use to create a code review with a <a href="https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_CodeReviewType.html">CodeReviewType</a> of <code>RepositoryAnalysis</code>. This type of code review analyzes all code under a specified branch in an associated repository. <code>PullRequest</code> code reviews are automatically triggered by a pull request.</p>

        Args:
            name: <p>The name of the code review. The name of each code review in your Amazon Web Services account must be unique.</p>
            repository_association_arn: <p>The Amazon Resource Name (ARN) of the <a href="https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_RepositoryAssociation.html">RepositoryAssociation</a> object. You can retrieve this ARN by calling <a href="https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_ListRepositoryAssociations.html">ListRepositoryAssociations</a>.</p> <p>A code review can only be created on an associated repository. This is the ARN of the associated repository.</p>
            type: <p>The type of code review to create. This is specified using a <a href="https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_CodeReviewType.html">CodeReviewType</a> object. You can create a code review only of type <code>RepositoryAnalysis</code>.</p>
            client_request_token: <p>Amazon CodeGuru Reviewer uses this value to prevent the accidental creation of duplicate code reviews if there are failures and retries.</p>

        Raises:
            capo_codeguru_reviewer.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_codeguru_reviewer.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. </p>
            capo_codeguru_reviewer.errors.internal_server_exception.InternalServerException: <p>The server encountered an internal error and is unable to complete the request.</p>
            capo_codeguru_reviewer.errors.resource_not_found_exception.ResourceNotFoundException: <p> The resource specified in the request was not found. </p>
            capo_codeguru_reviewer.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_codeguru_reviewer.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_codeguru_reviewer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_codeguru_reviewer.types.create_code_review_request.CreateCodeReviewRequest]",
        ) -> AsyncOperationResponse[
            "capo_codeguru_reviewer.types.create_code_review_response.CreateCodeReviewResponse"
        ]:
            import capo_codeguru_reviewer._operations.aws_guru_frontend_service.create_code_review

            (
                output,
                http_response,
            ) = await capo_codeguru_reviewer._operations.aws_guru_frontend_service.create_code_review.async_create_code_review(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codeguru_reviewer.types.create_code_review_request.CreateCodeReviewRequest = {
            "name": name,
            "repository_association_arn": repository_association_arn,
            "type": type,
        }
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

    async def describe_code_review(
        self,
        code_review_arn: "capo_codeguru_reviewer.types.arn.Arn",
        *,
        config_overrides: Optional[AsyncCodeGuruReviewerClientConfig] = None,
    ) -> "capo_codeguru_reviewer.types.describe_code_review_response.DescribeCodeReviewResponse":
        """<p>Returns the metadata associated with the code review along with its status.</p>

        Args:
            code_review_arn: <p>The Amazon Resource Name (ARN) of the <a href="https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_CodeReview.html">CodeReview</a> object. </p>

        Raises:
            capo_codeguru_reviewer.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_codeguru_reviewer.errors.internal_server_exception.InternalServerException: <p>The server encountered an internal error and is unable to complete the request.</p>
            capo_codeguru_reviewer.errors.resource_not_found_exception.ResourceNotFoundException: <p> The resource specified in the request was not found. </p>
            capo_codeguru_reviewer.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_codeguru_reviewer.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_codeguru_reviewer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_codeguru_reviewer.types.describe_code_review_request.DescribeCodeReviewRequest]",
        ) -> AsyncOperationResponse[
            "capo_codeguru_reviewer.types.describe_code_review_response.DescribeCodeReviewResponse"
        ]:
            import capo_codeguru_reviewer._operations.aws_guru_frontend_service.describe_code_review

            (
                output,
                http_response,
            ) = await capo_codeguru_reviewer._operations.aws_guru_frontend_service.describe_code_review.async_describe_code_review(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codeguru_reviewer.types.describe_code_review_request.DescribeCodeReviewRequest = {
            "code_review_arn": code_review_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_recommendation_feedback(
        self,
        code_review_arn: "capo_codeguru_reviewer.types.arn.Arn",
        recommendation_id: "capo_codeguru_reviewer.types.recommendation_id.RecommendationId",
        *,
        config_overrides: Optional[AsyncCodeGuruReviewerClientConfig] = None,
        user_id: Optional["capo_codeguru_reviewer.types.user_id.UserId"] = None,
    ) -> "capo_codeguru_reviewer.types.describe_recommendation_feedback_response.DescribeRecommendationFeedbackResponse":
        """<p>Describes the customer feedback for a CodeGuru Reviewer recommendation.</p>

        Args:
            code_review_arn: <p>The Amazon Resource Name (ARN) of the <a href="https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_CodeReview.html">CodeReview</a> object. </p>
            recommendation_id: <p>The recommendation ID that can be used to track the provided recommendations and then to collect the feedback.</p>
            user_id: <p>Optional parameter to describe the feedback for a given user. If this is not supplied, it defaults to the user making the request.</p> <p> The <code>UserId</code> is an IAM principal that can be specified as an Amazon Web Services account ID or an Amazon Resource Name (ARN). For more information, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_principal.html#Principal_specifying"> Specifying a Principal</a> in the <i>Amazon Web Services Identity and Access Management User Guide</i>.</p>

        Raises:
            capo_codeguru_reviewer.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_codeguru_reviewer.errors.internal_server_exception.InternalServerException: <p>The server encountered an internal error and is unable to complete the request.</p>
            capo_codeguru_reviewer.errors.resource_not_found_exception.ResourceNotFoundException: <p> The resource specified in the request was not found. </p>
            capo_codeguru_reviewer.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_codeguru_reviewer.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_codeguru_reviewer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_codeguru_reviewer.types.describe_recommendation_feedback_request.DescribeRecommendationFeedbackRequest]",
        ) -> AsyncOperationResponse[
            "capo_codeguru_reviewer.types.describe_recommendation_feedback_response.DescribeRecommendationFeedbackResponse"
        ]:
            import capo_codeguru_reviewer._operations.aws_guru_frontend_service.describe_recommendation_feedback

            (
                output,
                http_response,
            ) = await capo_codeguru_reviewer._operations.aws_guru_frontend_service.describe_recommendation_feedback.async_describe_recommendation_feedback(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codeguru_reviewer.types.describe_recommendation_feedback_request.DescribeRecommendationFeedbackRequest = {
            "code_review_arn": code_review_arn,
            "recommendation_id": recommendation_id,
        }
        if user_id is not None:
            input_["user_id"] = user_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_repository_association(
        self,
        association_arn: "capo_codeguru_reviewer.types.association_arn.AssociationArn",
        *,
        config_overrides: Optional[AsyncCodeGuruReviewerClientConfig] = None,
    ) -> "capo_codeguru_reviewer.types.describe_repository_association_response.DescribeRepositoryAssociationResponse":
        """<p>Returns a <a href="https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_RepositoryAssociation.html">RepositoryAssociation</a> object that contains information about the requested repository association.</p>

        Args:
            association_arn: <p>The Amazon Resource Name (ARN) of the <a href="https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_RepositoryAssociation.html">RepositoryAssociation</a> object. You can retrieve this ARN by calling <a href="https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_ListRepositoryAssociations.html">ListRepositoryAssociations</a>.</p>

        Raises:
            capo_codeguru_reviewer.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_codeguru_reviewer.errors.internal_server_exception.InternalServerException: <p>The server encountered an internal error and is unable to complete the request.</p>
            capo_codeguru_reviewer.errors.not_found_exception.NotFoundException: <p>The resource specified in the request was not found.</p>
            capo_codeguru_reviewer.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_codeguru_reviewer.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_codeguru_reviewer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_codeguru_reviewer.types.describe_repository_association_request.DescribeRepositoryAssociationRequest]",
        ) -> AsyncOperationResponse[
            "capo_codeguru_reviewer.types.describe_repository_association_response.DescribeRepositoryAssociationResponse"
        ]:
            import capo_codeguru_reviewer._operations.aws_guru_frontend_service.describe_repository_association

            (
                output,
                http_response,
            ) = await capo_codeguru_reviewer._operations.aws_guru_frontend_service.describe_repository_association.async_describe_repository_association(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codeguru_reviewer.types.describe_repository_association_request.DescribeRepositoryAssociationRequest = {
            "association_arn": association_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def disassociate_repository(
        self,
        association_arn: "capo_codeguru_reviewer.types.association_arn.AssociationArn",
        *,
        config_overrides: Optional[AsyncCodeGuruReviewerClientConfig] = None,
    ) -> "capo_codeguru_reviewer.types.disassociate_repository_response.DisassociateRepositoryResponse":
        """<p>Removes the association between Amazon CodeGuru Reviewer and a repository.</p>

        Args:
            association_arn: <p>The Amazon Resource Name (ARN) of the <a href="https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_RepositoryAssociation.html">RepositoryAssociation</a> object. You can retrieve this ARN by calling <a href="https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_ListRepositoryAssociations.html">ListRepositoryAssociations</a>.</p>

        Raises:
            capo_codeguru_reviewer.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_codeguru_reviewer.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. </p>
            capo_codeguru_reviewer.errors.internal_server_exception.InternalServerException: <p>The server encountered an internal error and is unable to complete the request.</p>
            capo_codeguru_reviewer.errors.not_found_exception.NotFoundException: <p>The resource specified in the request was not found.</p>
            capo_codeguru_reviewer.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_codeguru_reviewer.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_codeguru_reviewer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_codeguru_reviewer.types.disassociate_repository_request.DisassociateRepositoryRequest]",
        ) -> AsyncOperationResponse[
            "capo_codeguru_reviewer.types.disassociate_repository_response.DisassociateRepositoryResponse"
        ]:
            import capo_codeguru_reviewer._operations.aws_guru_frontend_service.disassociate_repository

            (
                output,
                http_response,
            ) = await capo_codeguru_reviewer._operations.aws_guru_frontend_service.disassociate_repository.async_disassociate_repository(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codeguru_reviewer.types.disassociate_repository_request.DisassociateRepositoryRequest = {
            "association_arn": association_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_code_reviews(
        self,
        type: "capo_codeguru_reviewer.types.type.Type",
        *,
        config_overrides: Optional[AsyncCodeGuruReviewerClientConfig] = None,
        provider_types: Optional[
            "capo_codeguru_reviewer.types.provider_types.ProviderTypes"
        ] = None,
        states: Optional["capo_codeguru_reviewer.types.job_states.JobStates"] = None,
        repository_names: Optional[
            "capo_codeguru_reviewer.types.repository_names.RepositoryNames"
        ] = None,
        max_results: Optional[
            "capo_codeguru_reviewer.types.list_code_reviews_max_results.ListCodeReviewsMaxResults"
        ] = None,
        next_token: Optional[
            "capo_codeguru_reviewer.types.next_token.NextToken"
        ] = None,
    ) -> "capo_codeguru_reviewer.types.list_code_reviews_response.ListCodeReviewsResponse":
        """<p>Lists all the code reviews that the customer has created in the past 90 days.</p>

        Args:
            provider_types: <p>List of provider types for filtering that needs to be applied before displaying the result. For example, <code>providerTypes=[GitHub]</code> lists code reviews from GitHub.</p>
            states: <p>List of states for filtering that needs to be applied before displaying the result. For example, <code>states=[Pending]</code> lists code reviews in the Pending state.</p> <p>The valid code review states are:</p> <ul> <li> <p> <code>Completed</code>: The code review is complete.</p> </li> <li> <p> <code>Pending</code>: The code review started and has not completed or failed.</p> </li> <li> <p> <code>Failed</code>: The code review failed.</p> </li> <li> <p> <code>Deleting</code>: The code review is being deleted.</p> </li> </ul>
            repository_names: <p>List of repository names for filtering that needs to be applied before displaying the result.</p>
            type: <p>The type of code reviews to list in the response.</p>
            max_results: <p>The maximum number of results that are returned per call. The default is 100.</p>
            next_token: <p>If <code>nextToken</code> is returned, there are more results available. The value of <code>nextToken</code> is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged.</p>

        Raises:
            capo_codeguru_reviewer.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_codeguru_reviewer.errors.internal_server_exception.InternalServerException: <p>The server encountered an internal error and is unable to complete the request.</p>
            capo_codeguru_reviewer.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_codeguru_reviewer.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_codeguru_reviewer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_codeguru_reviewer.types.list_code_reviews_request.ListCodeReviewsRequest]",
        ) -> AsyncOperationResponse[
            "capo_codeguru_reviewer.types.list_code_reviews_response.ListCodeReviewsResponse"
        ]:
            import capo_codeguru_reviewer._operations.aws_guru_frontend_service.list_code_reviews

            (
                output,
                http_response,
            ) = await capo_codeguru_reviewer._operations.aws_guru_frontend_service.list_code_reviews.async_list_code_reviews(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codeguru_reviewer.types.list_code_reviews_request.ListCodeReviewsRequest = {
            "type": type
        }
        if provider_types is not None:
            input_["provider_types"] = provider_types
        if states is not None:
            input_["states"] = states
        if repository_names is not None:
            input_["repository_names"] = repository_names
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

    async def iter_list_code_reviews(
        self,
        type: "capo_codeguru_reviewer.types.type.Type",
        *,
        config_overrides: Optional[AsyncCodeGuruReviewerClientConfig] = None,
        provider_types: Optional[
            "capo_codeguru_reviewer.types.provider_types.ProviderTypes"
        ] = None,
        states: Optional["capo_codeguru_reviewer.types.job_states.JobStates"] = None,
        repository_names: Optional[
            "capo_codeguru_reviewer.types.repository_names.RepositoryNames"
        ] = None,
        max_results: Optional[
            "capo_codeguru_reviewer.types.list_code_reviews_max_results.ListCodeReviewsMaxResults"
        ] = None,
        next_token: Optional[
            "capo_codeguru_reviewer.types.next_token.NextToken"
        ] = None,
    ) -> "AsyncIterator[capo_codeguru_reviewer.types.list_code_reviews_response.ListCodeReviewsResponse]":
        _token = next_token
        while True:
            _response = await self.list_code_reviews(
                type,
                config_overrides=config_overrides,
                provider_types=provider_types,
                states=states,
                repository_names=repository_names,
                max_results=max_results,
                next_token=_token,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_recommendation_feedback(
        self,
        code_review_arn: "capo_codeguru_reviewer.types.arn.Arn",
        *,
        config_overrides: Optional[AsyncCodeGuruReviewerClientConfig] = None,
        next_token: Optional[
            "capo_codeguru_reviewer.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "capo_codeguru_reviewer.types.max_results.MaxResults"
        ] = None,
        user_ids: Optional["capo_codeguru_reviewer.types.user_ids.UserIds"] = None,
        recommendation_ids: Optional[
            "capo_codeguru_reviewer.types.recommendation_ids.RecommendationIds"
        ] = None,
    ) -> "capo_codeguru_reviewer.types.list_recommendation_feedback_response.ListRecommendationFeedbackResponse":
        """<p>Returns a list of <a href="https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_RecommendationFeedbackSummary.html">RecommendationFeedbackSummary</a> objects that contain customer recommendation feedback for all CodeGuru Reviewer users.</p>

        Args:
            next_token: <p>If <code>nextToken</code> is returned, there are more results available. The value of <code>nextToken</code> is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged.</p>
            max_results: <p>The maximum number of results that are returned per call. The default is 100.</p>
            code_review_arn: <p>The Amazon Resource Name (ARN) of the <a href="https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_CodeReview.html">CodeReview</a> object. </p>
            user_ids: <p>An Amazon Web Services user's account ID or Amazon Resource Name (ARN). Use this ID to query the recommendation feedback for a code review from that user.</p> <p> The <code>UserId</code> is an IAM principal that can be specified as an Amazon Web Services account ID or an Amazon Resource Name (ARN). For more information, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_principal.html#Principal_specifying"> Specifying a Principal</a> in the <i>Amazon Web Services Identity and Access Management User Guide</i>.</p>
            recommendation_ids: <p>Used to query the recommendation feedback for a given recommendation.</p>

        Raises:
            capo_codeguru_reviewer.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_codeguru_reviewer.errors.internal_server_exception.InternalServerException: <p>The server encountered an internal error and is unable to complete the request.</p>
            capo_codeguru_reviewer.errors.resource_not_found_exception.ResourceNotFoundException: <p> The resource specified in the request was not found. </p>
            capo_codeguru_reviewer.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_codeguru_reviewer.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_codeguru_reviewer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_codeguru_reviewer.types.list_recommendation_feedback_request.ListRecommendationFeedbackRequest]",
        ) -> AsyncOperationResponse[
            "capo_codeguru_reviewer.types.list_recommendation_feedback_response.ListRecommendationFeedbackResponse"
        ]:
            import capo_codeguru_reviewer._operations.aws_guru_frontend_service.list_recommendation_feedback

            (
                output,
                http_response,
            ) = await capo_codeguru_reviewer._operations.aws_guru_frontend_service.list_recommendation_feedback.async_list_recommendation_feedback(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codeguru_reviewer.types.list_recommendation_feedback_request.ListRecommendationFeedbackRequest = {
            "code_review_arn": code_review_arn
        }
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if user_ids is not None:
            input_["user_ids"] = user_ids
        if recommendation_ids is not None:
            input_["recommendation_ids"] = recommendation_ids

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_recommendation_feedback(
        self,
        code_review_arn: "capo_codeguru_reviewer.types.arn.Arn",
        *,
        config_overrides: Optional[AsyncCodeGuruReviewerClientConfig] = None,
        next_token: Optional[
            "capo_codeguru_reviewer.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "capo_codeguru_reviewer.types.max_results.MaxResults"
        ] = None,
        user_ids: Optional["capo_codeguru_reviewer.types.user_ids.UserIds"] = None,
        recommendation_ids: Optional[
            "capo_codeguru_reviewer.types.recommendation_ids.RecommendationIds"
        ] = None,
    ) -> "AsyncIterator[capo_codeguru_reviewer.types.list_recommendation_feedback_response.ListRecommendationFeedbackResponse]":
        _token = next_token
        while True:
            _response = await self.list_recommendation_feedback(
                code_review_arn,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
                user_ids=user_ids,
                recommendation_ids=recommendation_ids,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_recommendations(
        self,
        code_review_arn: "capo_codeguru_reviewer.types.arn.Arn",
        *,
        config_overrides: Optional[AsyncCodeGuruReviewerClientConfig] = None,
        next_token: Optional[
            "capo_codeguru_reviewer.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "capo_codeguru_reviewer.types.list_recommendations_max_results.ListRecommendationsMaxResults"
        ] = None,
    ) -> "capo_codeguru_reviewer.types.list_recommendations_response.ListRecommendationsResponse":
        """<p>Returns the list of all recommendations for a completed code review.</p>

        Args:
            next_token: <p>Pagination token.</p>
            max_results: <p>The maximum number of results that are returned per call. The default is 100.</p>
            code_review_arn: <p>The Amazon Resource Name (ARN) of the <a href="https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_CodeReview.html">CodeReview</a> object. </p>

        Raises:
            capo_codeguru_reviewer.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_codeguru_reviewer.errors.internal_server_exception.InternalServerException: <p>The server encountered an internal error and is unable to complete the request.</p>
            capo_codeguru_reviewer.errors.resource_not_found_exception.ResourceNotFoundException: <p> The resource specified in the request was not found. </p>
            capo_codeguru_reviewer.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_codeguru_reviewer.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_codeguru_reviewer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_codeguru_reviewer.types.list_recommendations_request.ListRecommendationsRequest]",
        ) -> AsyncOperationResponse[
            "capo_codeguru_reviewer.types.list_recommendations_response.ListRecommendationsResponse"
        ]:
            import capo_codeguru_reviewer._operations.aws_guru_frontend_service.list_recommendations

            (
                output,
                http_response,
            ) = await capo_codeguru_reviewer._operations.aws_guru_frontend_service.list_recommendations.async_list_recommendations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codeguru_reviewer.types.list_recommendations_request.ListRecommendationsRequest = {
            "code_review_arn": code_review_arn
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

    async def iter_list_recommendations(
        self,
        code_review_arn: "capo_codeguru_reviewer.types.arn.Arn",
        *,
        config_overrides: Optional[AsyncCodeGuruReviewerClientConfig] = None,
        next_token: Optional[
            "capo_codeguru_reviewer.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "capo_codeguru_reviewer.types.list_recommendations_max_results.ListRecommendationsMaxResults"
        ] = None,
    ) -> "AsyncIterator[capo_codeguru_reviewer.types.list_recommendations_response.ListRecommendationsResponse]":
        _token = next_token
        while True:
            _response = await self.list_recommendations(
                code_review_arn,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_repository_associations(
        self,
        *,
        config_overrides: Optional[AsyncCodeGuruReviewerClientConfig] = None,
        provider_types: Optional[
            "capo_codeguru_reviewer.types.provider_types.ProviderTypes"
        ] = None,
        states: Optional[
            "capo_codeguru_reviewer.types.repository_association_states.RepositoryAssociationStates"
        ] = None,
        names: Optional["capo_codeguru_reviewer.types.names.Names"] = None,
        owners: Optional["capo_codeguru_reviewer.types.owners.Owners"] = None,
        max_results: Optional[
            "capo_codeguru_reviewer.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_codeguru_reviewer.types.next_token.NextToken"
        ] = None,
    ) -> "capo_codeguru_reviewer.types.list_repository_associations_response.ListRepositoryAssociationsResponse":
        """<p>Returns a list of <a href="https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_RepositoryAssociationSummary.html">RepositoryAssociationSummary</a> objects that contain summary information about a repository association. You can filter the returned list by <a href="https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_RepositoryAssociationSummary.html#reviewer-Type-RepositoryAssociationSummary-ProviderType">ProviderType</a>, <a href="https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_RepositoryAssociationSummary.html#reviewer-Type-RepositoryAssociationSummary-Name">Name</a>, <a href="https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_RepositoryAssociationSummary.html#reviewer-Type-RepositoryAssociationSummary-State">State</a>, and <a href="https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_RepositoryAssociationSummary.html#reviewer-Type-RepositoryAssociationSummary-Owner">Owner</a>.</p>

        Args:
            provider_types: <p>List of provider types to use as a filter.</p>
            states: <p>List of repository association states to use as a filter.</p> <p>The valid repository association states are:</p> <ul> <li> <p> <b>Associated</b>: The repository association is complete.</p> </li> <li> <p> <b>Associating</b>: CodeGuru Reviewer is:</p> <ul> <li> <p>Setting up pull request notifications. This is required for pull requests to trigger a CodeGuru Reviewer review.</p> <note> <p>If your repository <code>ProviderType</code> is <code>GitHub</code>, <code>GitHub Enterprise Server</code>, or <code>Bitbucket</code>, CodeGuru Reviewer creates webhooks in your repository to trigger CodeGuru Reviewer reviews. If you delete these webhooks, reviews of code in your repository cannot be triggered.</p> </note> </li> <li> <p>Setting up source code access. This is required for CodeGuru Reviewer to securely clone code in your repository.</p> </li> </ul> </li> <li> <p> <b>Failed</b>: The repository failed to associate or disassociate.</p> </li> <li> <p> <b>Disassociating</b>: CodeGuru Reviewer is removing the repository's pull request notifications and source code access.</p> </li> <li> <p> <b>Disassociated</b>: CodeGuru Reviewer successfully disassociated the repository. You can create a new association with this repository if you want to review source code in it later. You can control access to code reviews created in anassociated repository with tags after it has been disassociated. For more information, see <a href="https://docs.aws.amazon.com/codeguru/latest/reviewer-ug/auth-and-access-control-using-tags.html">Using tags to control access to associated repositories</a> in the <i>Amazon CodeGuru Reviewer User Guide</i>.</p> </li> </ul>
            names: <p>List of repository names to use as a filter.</p>
            owners: <p>List of owners to use as a filter. For Amazon Web Services CodeCommit, it is the name of the CodeCommit account that was used to associate the repository. For other repository source providers, such as Bitbucket and GitHub Enterprise Server, this is name of the account that was used to associate the repository. </p>
            max_results: <p>The maximum number of repository association results returned by <code>ListRepositoryAssociations</code> in paginated output. When this parameter is used, <code>ListRepositoryAssociations</code> only returns <code>maxResults</code> results in a single page with a <code>nextToken</code> response element. The remaining results of the initial request can be seen by sending another <code>ListRepositoryAssociations</code> request with the returned <code>nextToken</code> value. This value can be between 1 and 100. If this parameter is not used, <code>ListRepositoryAssociations</code> returns up to 100 results and a <code>nextToken</code> value if applicable. </p>
            next_token: <p>The <code>nextToken</code> value returned from a previous paginated <code>ListRepositoryAssociations</code> request where <code>maxResults</code> was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the <code>nextToken</code> value. </p> <note> <p>Treat this token as an opaque identifier that is only used to retrieve the next items in a list and not for other programmatic purposes.</p> </note>

        Raises:
            capo_codeguru_reviewer.errors.internal_server_exception.InternalServerException: <p>The server encountered an internal error and is unable to complete the request.</p>
            capo_codeguru_reviewer.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_codeguru_reviewer.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_codeguru_reviewer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_codeguru_reviewer.types.list_repository_associations_request.ListRepositoryAssociationsRequest]",
        ) -> AsyncOperationResponse[
            "capo_codeguru_reviewer.types.list_repository_associations_response.ListRepositoryAssociationsResponse"
        ]:
            import capo_codeguru_reviewer._operations.aws_guru_frontend_service.list_repository_associations

            (
                output,
                http_response,
            ) = await capo_codeguru_reviewer._operations.aws_guru_frontend_service.list_repository_associations.async_list_repository_associations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codeguru_reviewer.types.list_repository_associations_request.ListRepositoryAssociationsRequest = {}
        if provider_types is not None:
            input_["provider_types"] = provider_types
        if states is not None:
            input_["states"] = states
        if names is not None:
            input_["names"] = names
        if owners is not None:
            input_["owners"] = owners
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

    async def iter_list_repository_associations(
        self,
        *,
        config_overrides: Optional[AsyncCodeGuruReviewerClientConfig] = None,
        provider_types: Optional[
            "capo_codeguru_reviewer.types.provider_types.ProviderTypes"
        ] = None,
        states: Optional[
            "capo_codeguru_reviewer.types.repository_association_states.RepositoryAssociationStates"
        ] = None,
        names: Optional["capo_codeguru_reviewer.types.names.Names"] = None,
        owners: Optional["capo_codeguru_reviewer.types.owners.Owners"] = None,
        max_results: Optional[
            "capo_codeguru_reviewer.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_codeguru_reviewer.types.next_token.NextToken"
        ] = None,
    ) -> "AsyncIterator[capo_codeguru_reviewer.types.repository_association_summary.RepositoryAssociationSummary]":
        _token = next_token
        while True:
            _response = await self.list_repository_associations(
                config_overrides=config_overrides,
                provider_types=provider_types,
                states=states,
                names=names,
                owners=owners,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("repository_association_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_tags_for_resource(
        self,
        resource_arn: "capo_codeguru_reviewer.types.association_arn.AssociationArn",
        *,
        config_overrides: Optional[AsyncCodeGuruReviewerClientConfig] = None,
    ) -> "capo_codeguru_reviewer.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>Returns the list of tags associated with an associated repository resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the <a href="https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_RepositoryAssociation.html">RepositoryAssociation</a> object. You can retrieve this ARN by calling <a href="https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_ListRepositoryAssociations.html">ListRepositoryAssociations</a>.</p>

        Raises:
            capo_codeguru_reviewer.errors.internal_server_exception.InternalServerException: <p>The server encountered an internal error and is unable to complete the request.</p>
            capo_codeguru_reviewer.errors.resource_not_found_exception.ResourceNotFoundException: <p> The resource specified in the request was not found. </p>
            capo_codeguru_reviewer.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_codeguru_reviewer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_codeguru_reviewer.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_codeguru_reviewer.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import capo_codeguru_reviewer._operations.aws_guru_frontend_service.list_tags_for_resource

            (
                output,
                http_response,
            ) = await capo_codeguru_reviewer._operations.aws_guru_frontend_service.list_tags_for_resource.async_list_tags_for_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codeguru_reviewer.types.list_tags_for_resource_request.ListTagsForResourceRequest = {
            "resource_arn": resource_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def put_recommendation_feedback(
        self,
        code_review_arn: "capo_codeguru_reviewer.types.arn.Arn",
        recommendation_id: "capo_codeguru_reviewer.types.recommendation_id.RecommendationId",
        reactions: "capo_codeguru_reviewer.types.reactions.Reactions",
        *,
        config_overrides: Optional[AsyncCodeGuruReviewerClientConfig] = None,
    ) -> "capo_codeguru_reviewer.types.put_recommendation_feedback_response.PutRecommendationFeedbackResponse":
        """<p>Stores customer feedback for a CodeGuru Reviewer recommendation. When this API is called again with different reactions the previous feedback is overwritten.</p>

        Args:
            code_review_arn: <p>The Amazon Resource Name (ARN) of the <a href="https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_CodeReview.html">CodeReview</a> object. </p>
            recommendation_id: <p>The recommendation ID that can be used to track the provided recommendations and then to collect the feedback.</p>
            reactions: <p>List for storing reactions. Reactions are utf-8 text code for emojis. If you send an empty list it clears all your feedback.</p>

        Raises:
            capo_codeguru_reviewer.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_codeguru_reviewer.errors.internal_server_exception.InternalServerException: <p>The server encountered an internal error and is unable to complete the request.</p>
            capo_codeguru_reviewer.errors.resource_not_found_exception.ResourceNotFoundException: <p> The resource specified in the request was not found. </p>
            capo_codeguru_reviewer.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_codeguru_reviewer.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_codeguru_reviewer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_codeguru_reviewer.types.put_recommendation_feedback_request.PutRecommendationFeedbackRequest]",
        ) -> AsyncOperationResponse[
            "capo_codeguru_reviewer.types.put_recommendation_feedback_response.PutRecommendationFeedbackResponse"
        ]:
            import capo_codeguru_reviewer._operations.aws_guru_frontend_service.put_recommendation_feedback

            (
                output,
                http_response,
            ) = await capo_codeguru_reviewer._operations.aws_guru_frontend_service.put_recommendation_feedback.async_put_recommendation_feedback(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codeguru_reviewer.types.put_recommendation_feedback_request.PutRecommendationFeedbackRequest = {
            "code_review_arn": code_review_arn,
            "recommendation_id": recommendation_id,
            "reactions": reactions,
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
        resource_arn: "capo_codeguru_reviewer.types.association_arn.AssociationArn",
        tags: "capo_codeguru_reviewer.types.tag_map.TagMap",
        *,
        config_overrides: Optional[AsyncCodeGuruReviewerClientConfig] = None,
    ) -> "capo_codeguru_reviewer.types.tag_resource_response.TagResourceResponse":
        """<p>Adds one or more tags to an associated repository.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the <a href="https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_RepositoryAssociation.html">RepositoryAssociation</a> object. You can retrieve this ARN by calling <a href="https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_ListRepositoryAssociations.html">ListRepositoryAssociations</a>.</p>
            tags: <p>An array of key-value pairs used to tag an associated repository. A tag is a custom attribute label with two parts:</p> <ul> <li> <p>A <i>tag key</i> (for example, <code>CostCenter</code>, <code>Environment</code>, <code>Project</code>, or <code>Secret</code>). Tag keys are case sensitive.</p> </li> <li> <p>An optional field known as a <i>tag value</i> (for example, <code>111122223333</code>, <code>Production</code>, or a team name). Omitting the tag value is the same as using an empty string. Like tag keys, tag values are case sensitive.</p> </li> </ul>

        Raises:
            capo_codeguru_reviewer.errors.internal_server_exception.InternalServerException: <p>The server encountered an internal error and is unable to complete the request.</p>
            capo_codeguru_reviewer.errors.resource_not_found_exception.ResourceNotFoundException: <p> The resource specified in the request was not found. </p>
            capo_codeguru_reviewer.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_codeguru_reviewer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_codeguru_reviewer.types.tag_resource_request.TagResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_codeguru_reviewer.types.tag_resource_response.TagResourceResponse"
        ]:
            import capo_codeguru_reviewer._operations.aws_guru_frontend_service.tag_resource

            (
                output,
                http_response,
            ) = await capo_codeguru_reviewer._operations.aws_guru_frontend_service.tag_resource.async_tag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codeguru_reviewer.types.tag_resource_request.TagResourceRequest = {
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
        resource_arn: "capo_codeguru_reviewer.types.association_arn.AssociationArn",
        tag_keys: "capo_codeguru_reviewer.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[AsyncCodeGuruReviewerClientConfig] = None,
    ) -> "capo_codeguru_reviewer.types.untag_resource_response.UntagResourceResponse":
        """<p>Removes a tag from an associated repository.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the <a href="https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_RepositoryAssociation.html">RepositoryAssociation</a> object. You can retrieve this ARN by calling <a href="https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_ListRepositoryAssociations.html">ListRepositoryAssociations</a>.</p>
            tag_keys: <p>A list of the keys for each tag you want to remove from an associated repository.</p>

        Raises:
            capo_codeguru_reviewer.errors.internal_server_exception.InternalServerException: <p>The server encountered an internal error and is unable to complete the request.</p>
            capo_codeguru_reviewer.errors.resource_not_found_exception.ResourceNotFoundException: <p> The resource specified in the request was not found. </p>
            capo_codeguru_reviewer.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_codeguru_reviewer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_codeguru_reviewer.types.untag_resource_request.UntagResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_codeguru_reviewer.types.untag_resource_response.UntagResourceResponse"
        ]:
            import capo_codeguru_reviewer._operations.aws_guru_frontend_service.untag_resource

            (
                output,
                http_response,
            ) = await capo_codeguru_reviewer._operations.aws_guru_frontend_service.untag_resource.async_untag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codeguru_reviewer.types.untag_resource_request.UntagResourceRequest = {
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
