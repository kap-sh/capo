"""Generated from Smithy shape ``com.amazonaws.s3vectors#S3Vectors``."""

import warnings
from collections.abc import Iterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import BaseHandler, Client

import capo_s3vectors._auth._signers
import capo_s3vectors._auth._sigv4
from capo_s3vectors._auth._identity import Credentials
from capo_s3vectors._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_s3vectors._auth._zapros_handler import AuthMiddleware
from capo_s3vectors._pagination import resolve_path as _resolve_path
from capo_s3vectors._resources.s3_vectors.vector_bucket_resource import (
    VectorBucketResource,
)
from capo_s3vectors._services._aws_config import aws_config
from capo_s3vectors._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import capo_s3vectors.types.create_index_input
    import capo_s3vectors.types.create_index_output
    import capo_s3vectors.types.create_vector_bucket_input
    import capo_s3vectors.types.create_vector_bucket_output
    import capo_s3vectors.types.data_type
    import capo_s3vectors.types.delete_index_input
    import capo_s3vectors.types.delete_index_output
    import capo_s3vectors.types.delete_vector_bucket_input
    import capo_s3vectors.types.delete_vector_bucket_output
    import capo_s3vectors.types.delete_vector_bucket_policy_input
    import capo_s3vectors.types.delete_vector_bucket_policy_output
    import capo_s3vectors.types.delete_vectors_input
    import capo_s3vectors.types.delete_vectors_input_list
    import capo_s3vectors.types.delete_vectors_output
    import capo_s3vectors.types.dimension
    import capo_s3vectors.types.distance_metric
    import capo_s3vectors.types.encryption_configuration
    import capo_s3vectors.types.get_index_input
    import capo_s3vectors.types.get_index_output
    import capo_s3vectors.types.get_vector_bucket_input
    import capo_s3vectors.types.get_vector_bucket_output
    import capo_s3vectors.types.get_vector_bucket_policy_input
    import capo_s3vectors.types.get_vector_bucket_policy_output
    import capo_s3vectors.types.get_vectors_input
    import capo_s3vectors.types.get_vectors_input_list
    import capo_s3vectors.types.get_vectors_output
    import capo_s3vectors.types.index_arn
    import capo_s3vectors.types.index_mode
    import capo_s3vectors.types.index_name
    import capo_s3vectors.types.index_summary
    import capo_s3vectors.types.list_indexes_input
    import capo_s3vectors.types.list_indexes_max_results
    import capo_s3vectors.types.list_indexes_next_token
    import capo_s3vectors.types.list_indexes_output
    import capo_s3vectors.types.list_indexes_prefix
    import capo_s3vectors.types.list_output_vector
    import capo_s3vectors.types.list_tags_for_resource_input
    import capo_s3vectors.types.list_tags_for_resource_output
    import capo_s3vectors.types.list_vector_buckets_input
    import capo_s3vectors.types.list_vector_buckets_max_results
    import capo_s3vectors.types.list_vector_buckets_next_token
    import capo_s3vectors.types.list_vector_buckets_output
    import capo_s3vectors.types.list_vector_buckets_prefix
    import capo_s3vectors.types.list_vectors_input
    import capo_s3vectors.types.list_vectors_max_results
    import capo_s3vectors.types.list_vectors_next_token
    import capo_s3vectors.types.list_vectors_output
    import capo_s3vectors.types.list_vectors_segment_count
    import capo_s3vectors.types.list_vectors_segment_index
    import capo_s3vectors.types.metadata_configuration
    import capo_s3vectors.types.put_vector_bucket_default_index_mode_input
    import capo_s3vectors.types.put_vector_bucket_default_index_mode_output
    import capo_s3vectors.types.put_vector_bucket_policy_input
    import capo_s3vectors.types.put_vector_bucket_policy_output
    import capo_s3vectors.types.put_vectors_input
    import capo_s3vectors.types.put_vectors_input_list
    import capo_s3vectors.types.put_vectors_output
    import capo_s3vectors.types.query_output_vector
    import capo_s3vectors.types.query_vectors_input
    import capo_s3vectors.types.query_vectors_next_token
    import capo_s3vectors.types.query_vectors_output
    import capo_s3vectors.types.resource_arn
    import capo_s3vectors.types.tag_key_list
    import capo_s3vectors.types.tag_resource_input
    import capo_s3vectors.types.tag_resource_output
    import capo_s3vectors.types.tags_map
    import capo_s3vectors.types.top_k
    import capo_s3vectors.types.untag_resource_input
    import capo_s3vectors.types.untag_resource_output
    import capo_s3vectors.types.update_index_mode_input
    import capo_s3vectors.types.update_index_mode_output
    import capo_s3vectors.types.vector_bucket_arn
    import capo_s3vectors.types.vector_bucket_name
    import capo_s3vectors.types.vector_bucket_policy
    import capo_s3vectors.types.vector_bucket_summary
    import capo_s3vectors.types.vector_data


class S3VectorsClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    use_fips: bool | None
    endpoint: str | None
    region: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class S3VectorsClient:
    """A client for the ``S3Vectors`` service.

    Args:
        http_handler: HTTP handler for sending requests. If not provided, creates a default handler.
        operation_interceptors: Interceptors that wrap every operation call. If not provided, defaults to an empty list.
        retry_max_attempts: Maximum number of times to retry a failed operation. Defaults to 3.
        use_fips: The value of the ``AWS::UseFIPS`` endpoint parameter.
        endpoint: The value of the ``SDK::Endpoint`` endpoint parameter.
        region: The value of the ``AWS::Region`` endpoint parameter.
        credentials: AWS credentials for request signing.
        credentials_provider: Provider that resolves AWS credentials. Takes precedence over ``credentials``.
    """

    def __init__(
        self,
        http_handler: BaseHandler | None = None,
        operation_interceptors: Iterable[Interceptor[Any, Any]] | None = None,
        retry_max_attempts: int | None = None,
        use_fips: bool | None = None,
        endpoint: str | None = None,
        region: str | None = None,
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
        self._config = S3VectorsClientConfig(
            {
                "operation_interceptors": operation_interceptors or [],
                "retry_max_attempts": retry_max_attempts,
                "use_fips": use_fips,
                "endpoint": endpoint,
                "region": region,
                "credentials_provider": resolved_credentials_provider,
            }
        )

        # resources
        self.vector_bucket_resource = VectorBucketResource(self)

    def operation_options(
        self, config_overrides: Optional[S3VectorsClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: S3VectorsClientConfig = config_overrides or {}
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
            use_fips=overrides.get("use_fips", self._config.get("use_fips")),
            endpoint=overrides.get("endpoint", self._config.get("endpoint")),
            region=overrides.get("region", self._config.get("region")),
            credentials_provider=overrides.get(
                "credentials_provider", self._config.get("credentials_provider")
            ),
        )
        return interceptors_, options_

    def list_tags_for_resource(
        self,
        resource_arn: "capo_s3vectors.types.resource_arn.ResourceARN",
        *,
        config_overrides: Optional[S3VectorsClientConfig] = None,
    ) -> "capo_s3vectors.types.list_tags_for_resource_output.ListTagsForResourceOutput":
        """<p>Lists all of the tags applied to a specified Amazon S3 Vectors resource. Each tag is a label consisting of a key and value pair. Tags can help you organize, track costs for, and control access to resources. </p> <note> <p>For a list of S3 resources that support tagging, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/tagging.html#manage-tags">Managing tags for Amazon S3 resources</a>.</p> </note> <dl> <dt>Permissions</dt> <dd> <p>For vector buckets and vector indexes, you must have the <code>s3vectors:ListTagsForResource</code> permission to use this operation.</p> </dd> </dl>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the Amazon S3 Vectors resource that you want to list tags for. The tagged resource can be a vector bucket or a vector index. </p>

        Raises:
            capo_s3vectors.errors.access_denied_exception.AccessDeniedException: <p>Access denied.</p>
            capo_s3vectors.errors.internal_server_exception.InternalServerException: <p>The request failed due to an internal server error.</p>
            capo_s3vectors.errors.request_timeout_exception.RequestTimeoutException: <p>The request timed out. Retry your request.</p>
            capo_s3vectors.errors.too_many_requests_exception.TooManyRequestsException: <p>The request was denied due to request throttling.</p>
            capo_s3vectors.errors.validation_exception.ValidationException: <p>The requested action isn't valid.</p>
            capo_s3vectors.errors.not_found_exception.NotFoundException: <p>The request was rejected because the specified resource can't be found.</p>
            capo_s3vectors.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is unavailable. Wait briefly and retry your request. If it continues to fail, increase your waiting time between retries.</p>
            capo_s3vectors.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_s3vectors.types.list_tags_for_resource_input.ListTagsForResourceInput]",
        ) -> OperationResponse[
            "capo_s3vectors.types.list_tags_for_resource_output.ListTagsForResourceOutput"
        ]:
            import capo_s3vectors._operations.s3_vectors.list_tags_for_resource

            output, http_response = (
                capo_s3vectors._operations.s3_vectors.list_tags_for_resource.list_tags_for_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_s3vectors.types.list_tags_for_resource_input.ListTagsForResourceInput = {
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
        resource_arn: "capo_s3vectors.types.resource_arn.ResourceARN",
        tags: "capo_s3vectors.types.tags_map.TagsMap",
        *,
        config_overrides: Optional[S3VectorsClientConfig] = None,
    ) -> "capo_s3vectors.types.tag_resource_output.TagResourceOutput":
        """<p>Applies one or more user-defined tags to an Amazon S3 Vectors resource or updates existing tags. Each tag is a label consisting of a key and value pair. Tags can help you organize, track costs for, and control access to your resources. You can add up to 50 tags for each resource.</p> <note> <p>For a list of S3 resources that support tagging, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/tagging.html#manage-tags">Managing tags for Amazon S3 resources</a>.</p> </note> <dl> <dt>Permissions</dt> <dd> <p>For vector buckets and vector indexes, you must have the <code>s3vectors:TagResource</code> permission to use this operation.</p> </dd> </dl>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the Amazon S3 Vectors resource that you're applying tags to. The tagged resource can be a vector bucket or a vector index. </p>
            tags: <p>The user-defined tag that you want to add to the specified S3 Vectors resource. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/tagging.html">Tagging for cost allocation or attribute-based access control (ABAC)</a>.</p>

        Raises:
            capo_s3vectors.errors.access_denied_exception.AccessDeniedException: <p>Access denied.</p>
            capo_s3vectors.errors.internal_server_exception.InternalServerException: <p>The request failed due to an internal server error.</p>
            capo_s3vectors.errors.request_timeout_exception.RequestTimeoutException: <p>The request timed out. Retry your request.</p>
            capo_s3vectors.errors.too_many_requests_exception.TooManyRequestsException: <p>The request was denied due to request throttling.</p>
            capo_s3vectors.errors.validation_exception.ValidationException: <p>The requested action isn't valid.</p>
            capo_s3vectors.errors.conflict_exception.ConflictException: <p>The request failed because a vector bucket name or a vector index name already exists. Vector bucket names must be unique within your Amazon Web Services account for each Amazon Web Services Region. Vector index names must be unique within your vector bucket. Choose a different vector bucket name or vector index name, and try again.</p>
            capo_s3vectors.errors.not_found_exception.NotFoundException: <p>The request was rejected because the specified resource can't be found.</p>
            capo_s3vectors.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is unavailable. Wait briefly and retry your request. If it continues to fail, increase your waiting time between retries.</p>
            capo_s3vectors.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_s3vectors.types.tag_resource_input.TagResourceInput]",
        ) -> OperationResponse[
            "capo_s3vectors.types.tag_resource_output.TagResourceOutput"
        ]:
            import capo_s3vectors._operations.s3_vectors.tag_resource

            output, http_response = (
                capo_s3vectors._operations.s3_vectors.tag_resource.tag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_s3vectors.types.tag_resource_input.TagResourceInput = {
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
        resource_arn: "capo_s3vectors.types.resource_arn.ResourceARN",
        tag_keys: "capo_s3vectors.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[S3VectorsClientConfig] = None,
    ) -> "capo_s3vectors.types.untag_resource_output.UntagResourceOutput":
        """<p>Removes the specified user-defined tags from an Amazon S3 Vectors resource. You can pass one or more tag keys. </p> <note> <p>For a list of S3 resources that support tagging, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/tagging.html#manage-tags">Managing tags for Amazon S3 resources</a>.</p> </note> <dl> <dt>Permissions</dt> <dd> <p>For vector buckets and vector indexes, you must have the <code>s3vectors:UntagResource</code> permission to use this operation.</p> </dd> </dl>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the Amazon S3 Vectors resource that you're removing tags from. The tagged resource can be a vector bucket or a vector index. </p>
            tag_keys: <p>The array of tag keys that you're removing from the S3 Vectors resource. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/tagging.html">Tagging for cost allocation or attribute-based access control (ABAC)</a>.</p>

        Raises:
            capo_s3vectors.errors.access_denied_exception.AccessDeniedException: <p>Access denied.</p>
            capo_s3vectors.errors.internal_server_exception.InternalServerException: <p>The request failed due to an internal server error.</p>
            capo_s3vectors.errors.request_timeout_exception.RequestTimeoutException: <p>The request timed out. Retry your request.</p>
            capo_s3vectors.errors.too_many_requests_exception.TooManyRequestsException: <p>The request was denied due to request throttling.</p>
            capo_s3vectors.errors.validation_exception.ValidationException: <p>The requested action isn't valid.</p>
            capo_s3vectors.errors.conflict_exception.ConflictException: <p>The request failed because a vector bucket name or a vector index name already exists. Vector bucket names must be unique within your Amazon Web Services account for each Amazon Web Services Region. Vector index names must be unique within your vector bucket. Choose a different vector bucket name or vector index name, and try again.</p>
            capo_s3vectors.errors.not_found_exception.NotFoundException: <p>The request was rejected because the specified resource can't be found.</p>
            capo_s3vectors.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is unavailable. Wait briefly and retry your request. If it continues to fail, increase your waiting time between retries.</p>
            capo_s3vectors.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_s3vectors.types.untag_resource_input.UntagResourceInput]",
        ) -> OperationResponse[
            "capo_s3vectors.types.untag_resource_output.UntagResourceOutput"
        ]:
            import capo_s3vectors._operations.s3_vectors.untag_resource

            output, http_response = (
                capo_s3vectors._operations.s3_vectors.untag_resource.untag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_s3vectors.types.untag_resource_input.UntagResourceInput = {
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

    def create_vector_bucket(
        self,
        vector_bucket_name: "capo_s3vectors.types.vector_bucket_name.VectorBucketName",
        *,
        config_overrides: Optional[S3VectorsClientConfig] = None,
        encryption_configuration: Optional[
            "capo_s3vectors.types.encryption_configuration.EncryptionConfiguration"
        ] = None,
        tags: Optional["capo_s3vectors.types.tags_map.TagsMap"] = None,
    ) -> "capo_s3vectors.types.create_vector_bucket_output.CreateVectorBucketOutput":
        """<p>Creates a vector bucket in the Amazon Web Services Region that you want your bucket to be in. </p> <dl> <dt>Permissions</dt> <dd> <p>You must have the <code>s3vectors:CreateVectorBucket</code> permission to use this operation. </p> <p>You must have the <code>s3vectors:TagResource</code> permission in addition to <code>s3vectors:CreateVectorBucket</code> permission to create a vector bucket with tags.</p> </dd> </dl>

        Args:
            vector_bucket_name: <p>The name of the vector bucket to create. </p>
            encryption_configuration: <p>The encryption configuration for the vector bucket. By default, if you don't specify, all new vectors in Amazon S3 vector buckets use server-side encryption with Amazon S3 managed keys (SSE-S3), specifically <code>AES256</code>. </p>
            tags: <p>An array of user-defined tags that you would like to apply to the vector bucket that you are creating. A tag is a key-value pair that you apply to your resources. Tags can help you organize and control access to resources. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/tagging.html">Tagging for cost allocation or attribute-based access control (ABAC)</a>.</p> <note> <p>You must have the <code>s3vectors:TagResource</code> permission in addition to <code>s3vectors:CreateVectorBucket</code> permission to create a vector bucket with tags.</p> </note>

        Raises:
            capo_s3vectors.errors.access_denied_exception.AccessDeniedException: <p>Access denied.</p>
            capo_s3vectors.errors.internal_server_exception.InternalServerException: <p>The request failed due to an internal server error.</p>
            capo_s3vectors.errors.request_timeout_exception.RequestTimeoutException: <p>The request timed out. Retry your request.</p>
            capo_s3vectors.errors.too_many_requests_exception.TooManyRequestsException: <p>The request was denied due to request throttling.</p>
            capo_s3vectors.errors.validation_exception.ValidationException: <p>The requested action isn't valid.</p>
            capo_s3vectors.errors.conflict_exception.ConflictException: <p>The request failed because a vector bucket name or a vector index name already exists. Vector bucket names must be unique within your Amazon Web Services account for each Amazon Web Services Region. Vector index names must be unique within your vector bucket. Choose a different vector bucket name or vector index name, and try again.</p>
            capo_s3vectors.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Your request exceeds a service quota. </p>
            capo_s3vectors.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is unavailable. Wait briefly and retry your request. If it continues to fail, increase your waiting time between retries.</p>
            capo_s3vectors.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_s3vectors.types.create_vector_bucket_input.CreateVectorBucketInput]",
        ) -> OperationResponse[
            "capo_s3vectors.types.create_vector_bucket_output.CreateVectorBucketOutput"
        ]:
            import capo_s3vectors._operations.s3_vectors.create_vector_bucket

            output, http_response = (
                capo_s3vectors._operations.s3_vectors.create_vector_bucket.create_vector_bucket(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_s3vectors.types.create_vector_bucket_input.CreateVectorBucketInput = {
            "vector_bucket_name": vector_bucket_name
        }
        if encryption_configuration is not None:
            input_["encryption_configuration"] = encryption_configuration
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_vector_bucket(
        self,
        *,
        config_overrides: Optional[S3VectorsClientConfig] = None,
        vector_bucket_name: Optional[
            "capo_s3vectors.types.vector_bucket_name.VectorBucketName"
        ] = None,
        vector_bucket_arn: Optional[
            "capo_s3vectors.types.vector_bucket_arn.VectorBucketArn"
        ] = None,
    ) -> "capo_s3vectors.types.delete_vector_bucket_output.DeleteVectorBucketOutput":
        """<p>Deletes a vector bucket. All vector indexes in the vector bucket must be deleted before the vector bucket can be deleted. To perform this operation, you must use either the vector bucket name or the vector bucket Amazon Resource Name (ARN). </p> <dl> <dt>Permissions</dt> <dd> <p>You must have the <code>s3vectors:DeleteVectorBucket</code> permission to use this operation. </p> </dd> </dl>

        Args:
            vector_bucket_name: <p>The name of the vector bucket to delete.</p>
            vector_bucket_arn: <p>The ARN of the vector bucket to delete.</p>

        Raises:
            capo_s3vectors.errors.access_denied_exception.AccessDeniedException: <p>Access denied.</p>
            capo_s3vectors.errors.internal_server_exception.InternalServerException: <p>The request failed due to an internal server error.</p>
            capo_s3vectors.errors.request_timeout_exception.RequestTimeoutException: <p>The request timed out. Retry your request.</p>
            capo_s3vectors.errors.too_many_requests_exception.TooManyRequestsException: <p>The request was denied due to request throttling.</p>
            capo_s3vectors.errors.validation_exception.ValidationException: <p>The requested action isn't valid.</p>
            capo_s3vectors.errors.conflict_exception.ConflictException: <p>The request failed because a vector bucket name or a vector index name already exists. Vector bucket names must be unique within your Amazon Web Services account for each Amazon Web Services Region. Vector index names must be unique within your vector bucket. Choose a different vector bucket name or vector index name, and try again.</p>
            capo_s3vectors.errors.not_found_exception.NotFoundException: <p>The request was rejected because the specified resource can't be found.</p>
            capo_s3vectors.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is unavailable. Wait briefly and retry your request. If it continues to fail, increase your waiting time between retries.</p>
            capo_s3vectors.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_s3vectors.types.delete_vector_bucket_input.DeleteVectorBucketInput]",
        ) -> OperationResponse[
            "capo_s3vectors.types.delete_vector_bucket_output.DeleteVectorBucketOutput"
        ]:
            import capo_s3vectors._operations.s3_vectors.delete_vector_bucket

            output, http_response = (
                capo_s3vectors._operations.s3_vectors.delete_vector_bucket.delete_vector_bucket(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_s3vectors.types.delete_vector_bucket_input.DeleteVectorBucketInput = {}
        if vector_bucket_name is not None:
            input_["vector_bucket_name"] = vector_bucket_name
        if vector_bucket_arn is not None:
            input_["vector_bucket_arn"] = vector_bucket_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_vector_bucket_policy(
        self,
        *,
        config_overrides: Optional[S3VectorsClientConfig] = None,
        vector_bucket_name: Optional[
            "capo_s3vectors.types.vector_bucket_name.VectorBucketName"
        ] = None,
        vector_bucket_arn: Optional[
            "capo_s3vectors.types.vector_bucket_arn.VectorBucketArn"
        ] = None,
    ) -> "capo_s3vectors.types.delete_vector_bucket_policy_output.DeleteVectorBucketPolicyOutput":
        """<p>Deletes a vector bucket policy. To specify the bucket, you must use either the vector bucket name or the vector bucket Amazon Resource Name (ARN).</p> <dl> <dt>Permissions</dt> <dd> <p>You must have the <code>s3vectors:DeleteVectorBucketPolicy</code> permission to use this operation. </p> </dd> </dl>

        Args:
            vector_bucket_name: <p>The name of the vector bucket to delete the policy from.</p>
            vector_bucket_arn: <p>The ARN of the vector bucket to delete the policy from.</p>

        Raises:
            capo_s3vectors.errors.access_denied_exception.AccessDeniedException: <p>Access denied.</p>
            capo_s3vectors.errors.internal_server_exception.InternalServerException: <p>The request failed due to an internal server error.</p>
            capo_s3vectors.errors.request_timeout_exception.RequestTimeoutException: <p>The request timed out. Retry your request.</p>
            capo_s3vectors.errors.too_many_requests_exception.TooManyRequestsException: <p>The request was denied due to request throttling.</p>
            capo_s3vectors.errors.validation_exception.ValidationException: <p>The requested action isn't valid.</p>
            capo_s3vectors.errors.not_found_exception.NotFoundException: <p>The request was rejected because the specified resource can't be found.</p>
            capo_s3vectors.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is unavailable. Wait briefly and retry your request. If it continues to fail, increase your waiting time between retries.</p>
            capo_s3vectors.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_s3vectors.types.delete_vector_bucket_policy_input.DeleteVectorBucketPolicyInput]",
        ) -> OperationResponse[
            "capo_s3vectors.types.delete_vector_bucket_policy_output.DeleteVectorBucketPolicyOutput"
        ]:
            import capo_s3vectors._operations.s3_vectors.delete_vector_bucket_policy

            output, http_response = (
                capo_s3vectors._operations.s3_vectors.delete_vector_bucket_policy.delete_vector_bucket_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_s3vectors.types.delete_vector_bucket_policy_input.DeleteVectorBucketPolicyInput = {}
        if vector_bucket_name is not None:
            input_["vector_bucket_name"] = vector_bucket_name
        if vector_bucket_arn is not None:
            input_["vector_bucket_arn"] = vector_bucket_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_vector_bucket(
        self,
        *,
        config_overrides: Optional[S3VectorsClientConfig] = None,
        vector_bucket_name: Optional[
            "capo_s3vectors.types.vector_bucket_name.VectorBucketName"
        ] = None,
        vector_bucket_arn: Optional[
            "capo_s3vectors.types.vector_bucket_arn.VectorBucketArn"
        ] = None,
    ) -> "capo_s3vectors.types.get_vector_bucket_output.GetVectorBucketOutput":
        """<p>Returns vector bucket attributes. To specify the bucket, you must use either the vector bucket name or the vector bucket Amazon Resource Name (ARN). </p> <dl> <dt>Permissions</dt> <dd> <p>You must have the <code>s3vectors:GetVectorBucket</code> permission to use this operation. </p> </dd> </dl>

        Args:
            vector_bucket_name: <p>The name of the vector bucket to retrieve information about.</p>
            vector_bucket_arn: <p>The ARN of the vector bucket to retrieve information about.</p>

        Raises:
            capo_s3vectors.errors.access_denied_exception.AccessDeniedException: <p>Access denied.</p>
            capo_s3vectors.errors.internal_server_exception.InternalServerException: <p>The request failed due to an internal server error.</p>
            capo_s3vectors.errors.request_timeout_exception.RequestTimeoutException: <p>The request timed out. Retry your request.</p>
            capo_s3vectors.errors.too_many_requests_exception.TooManyRequestsException: <p>The request was denied due to request throttling.</p>
            capo_s3vectors.errors.validation_exception.ValidationException: <p>The requested action isn't valid.</p>
            capo_s3vectors.errors.not_found_exception.NotFoundException: <p>The request was rejected because the specified resource can't be found.</p>
            capo_s3vectors.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is unavailable. Wait briefly and retry your request. If it continues to fail, increase your waiting time between retries.</p>
            capo_s3vectors.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_s3vectors.types.get_vector_bucket_input.GetVectorBucketInput]",
        ) -> OperationResponse[
            "capo_s3vectors.types.get_vector_bucket_output.GetVectorBucketOutput"
        ]:
            import capo_s3vectors._operations.s3_vectors.get_vector_bucket

            output, http_response = (
                capo_s3vectors._operations.s3_vectors.get_vector_bucket.get_vector_bucket(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_s3vectors.types.get_vector_bucket_input.GetVectorBucketInput = {}
        if vector_bucket_name is not None:
            input_["vector_bucket_name"] = vector_bucket_name
        if vector_bucket_arn is not None:
            input_["vector_bucket_arn"] = vector_bucket_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_vector_bucket_policy(
        self,
        *,
        config_overrides: Optional[S3VectorsClientConfig] = None,
        vector_bucket_name: Optional[
            "capo_s3vectors.types.vector_bucket_name.VectorBucketName"
        ] = None,
        vector_bucket_arn: Optional[
            "capo_s3vectors.types.vector_bucket_arn.VectorBucketArn"
        ] = None,
    ) -> "capo_s3vectors.types.get_vector_bucket_policy_output.GetVectorBucketPolicyOutput":
        """<p>Gets details about a vector bucket policy. To specify the bucket, you must use either the vector bucket name or the vector bucket Amazon Resource Name (ARN). </p> <dl> <dt>Permissions</dt> <dd> <p>You must have the <code>s3vectors:GetVectorBucketPolicy</code> permission to use this operation. </p> </dd> </dl>

        Args:
            vector_bucket_name: <p>The name of the vector bucket.</p>
            vector_bucket_arn: <p>The ARN of the vector bucket.</p>

        Raises:
            capo_s3vectors.errors.access_denied_exception.AccessDeniedException: <p>Access denied.</p>
            capo_s3vectors.errors.internal_server_exception.InternalServerException: <p>The request failed due to an internal server error.</p>
            capo_s3vectors.errors.request_timeout_exception.RequestTimeoutException: <p>The request timed out. Retry your request.</p>
            capo_s3vectors.errors.too_many_requests_exception.TooManyRequestsException: <p>The request was denied due to request throttling.</p>
            capo_s3vectors.errors.validation_exception.ValidationException: <p>The requested action isn't valid.</p>
            capo_s3vectors.errors.not_found_exception.NotFoundException: <p>The request was rejected because the specified resource can't be found.</p>
            capo_s3vectors.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is unavailable. Wait briefly and retry your request. If it continues to fail, increase your waiting time between retries.</p>
            capo_s3vectors.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_s3vectors.types.get_vector_bucket_policy_input.GetVectorBucketPolicyInput]",
        ) -> OperationResponse[
            "capo_s3vectors.types.get_vector_bucket_policy_output.GetVectorBucketPolicyOutput"
        ]:
            import capo_s3vectors._operations.s3_vectors.get_vector_bucket_policy

            output, http_response = (
                capo_s3vectors._operations.s3_vectors.get_vector_bucket_policy.get_vector_bucket_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_s3vectors.types.get_vector_bucket_policy_input.GetVectorBucketPolicyInput = {}
        if vector_bucket_name is not None:
            input_["vector_bucket_name"] = vector_bucket_name
        if vector_bucket_arn is not None:
            input_["vector_bucket_arn"] = vector_bucket_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_vector_buckets(
        self,
        *,
        config_overrides: Optional[S3VectorsClientConfig] = None,
        max_results: Optional[
            "capo_s3vectors.types.list_vector_buckets_max_results.ListVectorBucketsMaxResults"
        ] = None,
        next_token: Optional[
            "capo_s3vectors.types.list_vector_buckets_next_token.ListVectorBucketsNextToken"
        ] = None,
        prefix: Optional[
            "capo_s3vectors.types.list_vector_buckets_prefix.ListVectorBucketsPrefix"
        ] = None,
    ) -> "capo_s3vectors.types.list_vector_buckets_output.ListVectorBucketsOutput":
        """<p>Returns a list of all the vector buckets that are owned by the authenticated sender of the request.</p> <dl> <dt>Permissions</dt> <dd> <p>You must have the <code>s3vectors:ListVectorBuckets</code> permission to use this operation. </p> </dd> </dl>

        Args:
            max_results: <p>The maximum number of vector buckets to be returned in the response. </p>
            next_token: <p>The previous pagination token. </p>
            prefix: <p>Limits the response to vector buckets that begin with the specified prefix.</p>

        Raises:
            capo_s3vectors.errors.access_denied_exception.AccessDeniedException: <p>Access denied.</p>
            capo_s3vectors.errors.internal_server_exception.InternalServerException: <p>The request failed due to an internal server error.</p>
            capo_s3vectors.errors.request_timeout_exception.RequestTimeoutException: <p>The request timed out. Retry your request.</p>
            capo_s3vectors.errors.too_many_requests_exception.TooManyRequestsException: <p>The request was denied due to request throttling.</p>
            capo_s3vectors.errors.validation_exception.ValidationException: <p>The requested action isn't valid.</p>
            capo_s3vectors.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is unavailable. Wait briefly and retry your request. If it continues to fail, increase your waiting time between retries.</p>
            capo_s3vectors.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_s3vectors.types.list_vector_buckets_input.ListVectorBucketsInput]",
        ) -> OperationResponse[
            "capo_s3vectors.types.list_vector_buckets_output.ListVectorBucketsOutput"
        ]:
            import capo_s3vectors._operations.s3_vectors.list_vector_buckets

            output, http_response = (
                capo_s3vectors._operations.s3_vectors.list_vector_buckets.list_vector_buckets(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_s3vectors.types.list_vector_buckets_input.ListVectorBucketsInput = {}
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if prefix is not None:
            input_["prefix"] = prefix

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_vector_buckets(
        self,
        *,
        config_overrides: Optional[S3VectorsClientConfig] = None,
        max_results: Optional[
            "capo_s3vectors.types.list_vector_buckets_max_results.ListVectorBucketsMaxResults"
        ] = None,
        next_token: Optional[
            "capo_s3vectors.types.list_vector_buckets_next_token.ListVectorBucketsNextToken"
        ] = None,
        prefix: Optional[
            "capo_s3vectors.types.list_vector_buckets_prefix.ListVectorBucketsPrefix"
        ] = None,
    ) -> "Iterator[capo_s3vectors.types.vector_bucket_summary.VectorBucketSummary]":
        _token = next_token
        while True:
            _response = self.list_vector_buckets(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
                prefix=prefix,
            )
            _page = _resolve_path(_response, ("vector_buckets",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def put_vector_bucket_default_index_mode(
        self,
        default_index_mode: "capo_s3vectors.types.index_mode.IndexMode",
        *,
        config_overrides: Optional[S3VectorsClientConfig] = None,
        vector_bucket_name: Optional[
            "capo_s3vectors.types.vector_bucket_name.VectorBucketName"
        ] = None,
        vector_bucket_arn: Optional[
            "capo_s3vectors.types.vector_bucket_arn.VectorBucketArn"
        ] = None,
    ) -> "capo_s3vectors.types.put_vector_bucket_default_index_mode_output.PutVectorBucketDefaultIndexModeOutput":
        """<p>Updates the default index mode for a vector bucket. The updated default applies to vector indexes that you create after the request succeeds. The operation doesn't change existing vector indexes. To specify the vector bucket, you must use either the vector bucket name or the vector bucket Amazon Resource Name (ARN).</p> <dl> <dt>Permissions</dt> <dd> <p>You must have the <code>s3vectors:PutVectorBucketDefaultIndexMode</code> permission to use this operation.</p> </dd> </dl>

        Args:
            vector_bucket_name: <p>The name of the vector bucket to update.</p>
            vector_bucket_arn: <p>The Amazon Resource Name (ARN) of the vector bucket to update.</p>
            default_index_mode: <p>The default mode to assign to new vector indexes in the vector bucket. This change doesn't affect existing vector indexes.</p>

        Raises:
            capo_s3vectors.errors.access_denied_exception.AccessDeniedException: <p>Access denied.</p>
            capo_s3vectors.errors.internal_server_exception.InternalServerException: <p>The request failed due to an internal server error.</p>
            capo_s3vectors.errors.request_timeout_exception.RequestTimeoutException: <p>The request timed out. Retry your request.</p>
            capo_s3vectors.errors.too_many_requests_exception.TooManyRequestsException: <p>The request was denied due to request throttling.</p>
            capo_s3vectors.errors.validation_exception.ValidationException: <p>The requested action isn't valid.</p>
            capo_s3vectors.errors.not_found_exception.NotFoundException: <p>The request was rejected because the specified resource can't be found.</p>
            capo_s3vectors.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is unavailable. Wait briefly and retry your request. If it continues to fail, increase your waiting time between retries.</p>
            capo_s3vectors.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_s3vectors.types.put_vector_bucket_default_index_mode_input.PutVectorBucketDefaultIndexModeInput]",
        ) -> OperationResponse[
            "capo_s3vectors.types.put_vector_bucket_default_index_mode_output.PutVectorBucketDefaultIndexModeOutput"
        ]:
            import capo_s3vectors._operations.s3_vectors.put_vector_bucket_default_index_mode

            output, http_response = (
                capo_s3vectors._operations.s3_vectors.put_vector_bucket_default_index_mode.put_vector_bucket_default_index_mode(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_s3vectors.types.put_vector_bucket_default_index_mode_input.PutVectorBucketDefaultIndexModeInput = {
            "default_index_mode": default_index_mode
        }
        if vector_bucket_name is not None:
            input_["vector_bucket_name"] = vector_bucket_name
        if vector_bucket_arn is not None:
            input_["vector_bucket_arn"] = vector_bucket_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def put_vector_bucket_policy(
        self,
        policy: "capo_s3vectors.types.vector_bucket_policy.VectorBucketPolicy",
        *,
        config_overrides: Optional[S3VectorsClientConfig] = None,
        vector_bucket_name: Optional[
            "capo_s3vectors.types.vector_bucket_name.VectorBucketName"
        ] = None,
        vector_bucket_arn: Optional[
            "capo_s3vectors.types.vector_bucket_arn.VectorBucketArn"
        ] = None,
    ) -> "capo_s3vectors.types.put_vector_bucket_policy_output.PutVectorBucketPolicyOutput":
        """<p>Creates a bucket policy for a vector bucket. To specify the bucket, you must use either the vector bucket name or the vector bucket Amazon Resource Name (ARN). </p> <dl> <dt>Permissions</dt> <dd> <p>You must have the <code>s3vectors:PutVectorBucketPolicy</code> permission to use this operation. </p> </dd> </dl>

        Args:
            vector_bucket_name: <p>The name of the vector bucket.</p>
            vector_bucket_arn: <p>The Amazon Resource Name (ARN) of the vector bucket.</p>
            policy: <p>The <code>JSON</code> that defines the policy. For more information about bucket policies for S3 Vectors, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-vectors-bucket-policy.html">Managing vector bucket policies</a> in the <i>Amazon S3 User Guide</i>.</p>

        Raises:
            capo_s3vectors.errors.access_denied_exception.AccessDeniedException: <p>Access denied.</p>
            capo_s3vectors.errors.internal_server_exception.InternalServerException: <p>The request failed due to an internal server error.</p>
            capo_s3vectors.errors.request_timeout_exception.RequestTimeoutException: <p>The request timed out. Retry your request.</p>
            capo_s3vectors.errors.too_many_requests_exception.TooManyRequestsException: <p>The request was denied due to request throttling.</p>
            capo_s3vectors.errors.validation_exception.ValidationException: <p>The requested action isn't valid.</p>
            capo_s3vectors.errors.not_found_exception.NotFoundException: <p>The request was rejected because the specified resource can't be found.</p>
            capo_s3vectors.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is unavailable. Wait briefly and retry your request. If it continues to fail, increase your waiting time between retries.</p>
            capo_s3vectors.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_s3vectors.types.put_vector_bucket_policy_input.PutVectorBucketPolicyInput]",
        ) -> OperationResponse[
            "capo_s3vectors.types.put_vector_bucket_policy_output.PutVectorBucketPolicyOutput"
        ]:
            import capo_s3vectors._operations.s3_vectors.put_vector_bucket_policy

            output, http_response = (
                capo_s3vectors._operations.s3_vectors.put_vector_bucket_policy.put_vector_bucket_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_s3vectors.types.put_vector_bucket_policy_input.PutVectorBucketPolicyInput = {
            "policy": policy
        }
        if vector_bucket_name is not None:
            input_["vector_bucket_name"] = vector_bucket_name
        if vector_bucket_arn is not None:
            input_["vector_bucket_arn"] = vector_bucket_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_index(
        self,
        index_name: "capo_s3vectors.types.index_name.IndexName",
        data_type: "capo_s3vectors.types.data_type.DataType",
        dimension: "capo_s3vectors.types.dimension.Dimension",
        distance_metric: "capo_s3vectors.types.distance_metric.DistanceMetric",
        *,
        config_overrides: Optional[S3VectorsClientConfig] = None,
        vector_bucket_name: Optional[
            "capo_s3vectors.types.vector_bucket_name.VectorBucketName"
        ] = None,
        vector_bucket_arn: Optional[
            "capo_s3vectors.types.vector_bucket_arn.VectorBucketArn"
        ] = None,
        metadata_configuration: Optional[
            "capo_s3vectors.types.metadata_configuration.MetadataConfiguration"
        ] = None,
        encryption_configuration: Optional[
            "capo_s3vectors.types.encryption_configuration.EncryptionConfiguration"
        ] = None,
        tags: Optional["capo_s3vectors.types.tags_map.TagsMap"] = None,
    ) -> "capo_s3vectors.types.create_index_output.CreateIndexOutput":
        """<p>Creates a vector index within a vector bucket. To specify the vector bucket, you must use either the vector bucket name or the vector bucket Amazon Resource Name (ARN).</p> <dl> <dt>Permissions</dt> <dd> <p>You must have the <code>s3vectors:CreateIndex</code> permission to use this operation.</p> <p>You must have the <code>s3vectors:TagResource</code> permission in addition to <code>s3vectors:CreateIndex</code> permission to create a vector index with tags.</p> </dd> </dl>

        Args:
            vector_bucket_name: <p>The name of the vector bucket to create the vector index in. </p>
            vector_bucket_arn: <p>The Amazon Resource Name (ARN) of the vector bucket to create the vector index in.</p>
            index_name: <p>The name of the vector index to create. </p>
            data_type: <p>The data type of the vectors to be inserted into the vector index. </p>
            dimension: <p>The dimensions of the vectors to be inserted into the vector index. </p>
            distance_metric: <p>The distance metric to be used for similarity search. </p>
            metadata_configuration: <p>The metadata configuration for the vector index. </p>
            encryption_configuration: <p>The encryption configuration for a vector index. By default, if you don't specify, all new vectors in the vector index will use the encryption configuration of the vector bucket.</p>
            tags: <p>An array of user-defined tags that you would like to apply to the vector index that you are creating. A tag is a key-value pair that you apply to your resources. Tags can help you organize, track costs, and control access to resources. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/tagging.html">Tagging for cost allocation or attribute-based access control (ABAC)</a>.</p> <note> <p>You must have the <code>s3vectors:TagResource</code> permission in addition to <code>s3vectors:CreateIndex</code> permission to create a vector index with tags.</p> </note>

        Raises:
            capo_s3vectors.errors.access_denied_exception.AccessDeniedException: <p>Access denied.</p>
            capo_s3vectors.errors.internal_server_exception.InternalServerException: <p>The request failed due to an internal server error.</p>
            capo_s3vectors.errors.request_timeout_exception.RequestTimeoutException: <p>The request timed out. Retry your request.</p>
            capo_s3vectors.errors.too_many_requests_exception.TooManyRequestsException: <p>The request was denied due to request throttling.</p>
            capo_s3vectors.errors.validation_exception.ValidationException: <p>The requested action isn't valid.</p>
            capo_s3vectors.errors.conflict_exception.ConflictException: <p>The request failed because a vector bucket name or a vector index name already exists. Vector bucket names must be unique within your Amazon Web Services account for each Amazon Web Services Region. Vector index names must be unique within your vector bucket. Choose a different vector bucket name or vector index name, and try again.</p>
            capo_s3vectors.errors.not_found_exception.NotFoundException: <p>The request was rejected because the specified resource can't be found.</p>
            capo_s3vectors.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Your request exceeds a service quota. </p>
            capo_s3vectors.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is unavailable. Wait briefly and retry your request. If it continues to fail, increase your waiting time between retries.</p>
            capo_s3vectors.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_s3vectors.types.create_index_input.CreateIndexInput]",
        ) -> OperationResponse[
            "capo_s3vectors.types.create_index_output.CreateIndexOutput"
        ]:
            import capo_s3vectors._operations.s3_vectors.create_index

            output, http_response = (
                capo_s3vectors._operations.s3_vectors.create_index.create_index(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_s3vectors.types.create_index_input.CreateIndexInput = {
            "index_name": index_name,
            "data_type": data_type,
            "dimension": dimension,
            "distance_metric": distance_metric,
        }
        if vector_bucket_name is not None:
            input_["vector_bucket_name"] = vector_bucket_name
        if vector_bucket_arn is not None:
            input_["vector_bucket_arn"] = vector_bucket_arn
        if metadata_configuration is not None:
            input_["metadata_configuration"] = metadata_configuration
        if encryption_configuration is not None:
            input_["encryption_configuration"] = encryption_configuration
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_index(
        self,
        *,
        config_overrides: Optional[S3VectorsClientConfig] = None,
        vector_bucket_name: Optional[
            "capo_s3vectors.types.vector_bucket_name.VectorBucketName"
        ] = None,
        index_name: Optional["capo_s3vectors.types.index_name.IndexName"] = None,
        index_arn: Optional["capo_s3vectors.types.index_arn.IndexArn"] = None,
    ) -> "capo_s3vectors.types.delete_index_output.DeleteIndexOutput":
        """<p>Deletes a vector index. To specify the vector index, you can either use both the vector bucket name and vector index name, or use the vector index Amazon Resource Name (ARN). </p> <dl> <dt>Permissions</dt> <dd> <p>You must have the <code>s3vectors:DeleteIndex</code> permission to use this operation. </p> </dd> </dl>

        Args:
            vector_bucket_name: <p>The name of the vector bucket that contains the vector index. </p>
            index_name: <p>The name of the vector index to delete. </p>
            index_arn: <p>The ARN of the vector index to delete.</p>

        Raises:
            capo_s3vectors.errors.access_denied_exception.AccessDeniedException: <p>Access denied.</p>
            capo_s3vectors.errors.internal_server_exception.InternalServerException: <p>The request failed due to an internal server error.</p>
            capo_s3vectors.errors.request_timeout_exception.RequestTimeoutException: <p>The request timed out. Retry your request.</p>
            capo_s3vectors.errors.too_many_requests_exception.TooManyRequestsException: <p>The request was denied due to request throttling.</p>
            capo_s3vectors.errors.validation_exception.ValidationException: <p>The requested action isn't valid.</p>
            capo_s3vectors.errors.not_found_exception.NotFoundException: <p>The request was rejected because the specified resource can't be found.</p>
            capo_s3vectors.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is unavailable. Wait briefly and retry your request. If it continues to fail, increase your waiting time between retries.</p>
            capo_s3vectors.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_s3vectors.types.delete_index_input.DeleteIndexInput]",
        ) -> OperationResponse[
            "capo_s3vectors.types.delete_index_output.DeleteIndexOutput"
        ]:
            import capo_s3vectors._operations.s3_vectors.delete_index

            output, http_response = (
                capo_s3vectors._operations.s3_vectors.delete_index.delete_index(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_s3vectors.types.delete_index_input.DeleteIndexInput = {}
        if vector_bucket_name is not None:
            input_["vector_bucket_name"] = vector_bucket_name
        if index_name is not None:
            input_["index_name"] = index_name
        if index_arn is not None:
            input_["index_arn"] = index_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_index(
        self,
        *,
        config_overrides: Optional[S3VectorsClientConfig] = None,
        vector_bucket_name: Optional[
            "capo_s3vectors.types.vector_bucket_name.VectorBucketName"
        ] = None,
        index_name: Optional["capo_s3vectors.types.index_name.IndexName"] = None,
        index_arn: Optional["capo_s3vectors.types.index_arn.IndexArn"] = None,
    ) -> "capo_s3vectors.types.get_index_output.GetIndexOutput":
        """<p>Returns vector index attributes. To specify the vector index, you can either use both the vector bucket name and the vector index name, or use the vector index Amazon Resource Name (ARN). </p> <dl> <dt>Permissions</dt> <dd> <p>You must have the <code>s3vectors:GetIndex</code> permission to use this operation. </p> </dd> </dl>

        Args:
            vector_bucket_name: <p>The name of the vector bucket that contains the vector index. </p>
            index_name: <p>The name of the vector index.</p>
            index_arn: <p>The ARN of the vector index.</p>

        Raises:
            capo_s3vectors.errors.access_denied_exception.AccessDeniedException: <p>Access denied.</p>
            capo_s3vectors.errors.internal_server_exception.InternalServerException: <p>The request failed due to an internal server error.</p>
            capo_s3vectors.errors.request_timeout_exception.RequestTimeoutException: <p>The request timed out. Retry your request.</p>
            capo_s3vectors.errors.too_many_requests_exception.TooManyRequestsException: <p>The request was denied due to request throttling.</p>
            capo_s3vectors.errors.validation_exception.ValidationException: <p>The requested action isn't valid.</p>
            capo_s3vectors.errors.not_found_exception.NotFoundException: <p>The request was rejected because the specified resource can't be found.</p>
            capo_s3vectors.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is unavailable. Wait briefly and retry your request. If it continues to fail, increase your waiting time between retries.</p>
            capo_s3vectors.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_s3vectors.types.get_index_input.GetIndexInput]",
        ) -> OperationResponse["capo_s3vectors.types.get_index_output.GetIndexOutput"]:
            import capo_s3vectors._operations.s3_vectors.get_index

            output, http_response = (
                capo_s3vectors._operations.s3_vectors.get_index.get_index(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_s3vectors.types.get_index_input.GetIndexInput = {}
        if vector_bucket_name is not None:
            input_["vector_bucket_name"] = vector_bucket_name
        if index_name is not None:
            input_["index_name"] = index_name
        if index_arn is not None:
            input_["index_arn"] = index_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_indexes(
        self,
        *,
        config_overrides: Optional[S3VectorsClientConfig] = None,
        vector_bucket_name: Optional[
            "capo_s3vectors.types.vector_bucket_name.VectorBucketName"
        ] = None,
        vector_bucket_arn: Optional[
            "capo_s3vectors.types.vector_bucket_arn.VectorBucketArn"
        ] = None,
        max_results: Optional[
            "capo_s3vectors.types.list_indexes_max_results.ListIndexesMaxResults"
        ] = None,
        next_token: Optional[
            "capo_s3vectors.types.list_indexes_next_token.ListIndexesNextToken"
        ] = None,
        prefix: Optional[
            "capo_s3vectors.types.list_indexes_prefix.ListIndexesPrefix"
        ] = None,
    ) -> "capo_s3vectors.types.list_indexes_output.ListIndexesOutput":
        """<p>Returns a list of all the vector indexes within the specified vector bucket. To specify the bucket, you must use either the vector bucket name or the vector bucket Amazon Resource Name (ARN). </p> <dl> <dt>Permissions</dt> <dd> <p>You must have the <code>s3vectors:ListIndexes</code> permission to use this operation. </p> </dd> </dl>

        Args:
            vector_bucket_name: <p>The name of the vector bucket that contains the vector indexes. </p>
            vector_bucket_arn: <p>The ARN of the vector bucket that contains the vector indexes.</p>
            max_results: <p>The maximum number of items to be returned in the response. </p>
            next_token: <p>The previous pagination token. </p>
            prefix: <p>Limits the response to vector indexes that begin with the specified prefix.</p>

        Raises:
            capo_s3vectors.errors.access_denied_exception.AccessDeniedException: <p>Access denied.</p>
            capo_s3vectors.errors.internal_server_exception.InternalServerException: <p>The request failed due to an internal server error.</p>
            capo_s3vectors.errors.request_timeout_exception.RequestTimeoutException: <p>The request timed out. Retry your request.</p>
            capo_s3vectors.errors.too_many_requests_exception.TooManyRequestsException: <p>The request was denied due to request throttling.</p>
            capo_s3vectors.errors.validation_exception.ValidationException: <p>The requested action isn't valid.</p>
            capo_s3vectors.errors.not_found_exception.NotFoundException: <p>The request was rejected because the specified resource can't be found.</p>
            capo_s3vectors.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is unavailable. Wait briefly and retry your request. If it continues to fail, increase your waiting time between retries.</p>
            capo_s3vectors.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_s3vectors.types.list_indexes_input.ListIndexesInput]",
        ) -> OperationResponse[
            "capo_s3vectors.types.list_indexes_output.ListIndexesOutput"
        ]:
            import capo_s3vectors._operations.s3_vectors.list_indexes

            output, http_response = (
                capo_s3vectors._operations.s3_vectors.list_indexes.list_indexes(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_s3vectors.types.list_indexes_input.ListIndexesInput = {}
        if vector_bucket_name is not None:
            input_["vector_bucket_name"] = vector_bucket_name
        if vector_bucket_arn is not None:
            input_["vector_bucket_arn"] = vector_bucket_arn
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if prefix is not None:
            input_["prefix"] = prefix

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_indexes(
        self,
        *,
        config_overrides: Optional[S3VectorsClientConfig] = None,
        vector_bucket_name: Optional[
            "capo_s3vectors.types.vector_bucket_name.VectorBucketName"
        ] = None,
        vector_bucket_arn: Optional[
            "capo_s3vectors.types.vector_bucket_arn.VectorBucketArn"
        ] = None,
        max_results: Optional[
            "capo_s3vectors.types.list_indexes_max_results.ListIndexesMaxResults"
        ] = None,
        next_token: Optional[
            "capo_s3vectors.types.list_indexes_next_token.ListIndexesNextToken"
        ] = None,
        prefix: Optional[
            "capo_s3vectors.types.list_indexes_prefix.ListIndexesPrefix"
        ] = None,
    ) -> "Iterator[capo_s3vectors.types.index_summary.IndexSummary]":
        _token = next_token
        while True:
            _response = self.list_indexes(
                config_overrides=config_overrides,
                vector_bucket_name=vector_bucket_name,
                vector_bucket_arn=vector_bucket_arn,
                max_results=max_results,
                next_token=_token,
                prefix=prefix,
            )
            _page = _resolve_path(_response, ("indexes",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def update_index_mode(
        self,
        index_mode: "capo_s3vectors.types.index_mode.IndexMode",
        *,
        config_overrides: Optional[S3VectorsClientConfig] = None,
        vector_bucket_name: Optional[
            "capo_s3vectors.types.vector_bucket_name.VectorBucketName"
        ] = None,
        index_name: Optional["capo_s3vectors.types.index_name.IndexName"] = None,
        index_arn: Optional["capo_s3vectors.types.index_arn.IndexArn"] = None,
    ) -> "capo_s3vectors.types.update_index_mode_output.UpdateIndexModeOutput":
        """<p>Updates the mode for an existing vector index. You can set the mode to <code>ENHANCED</code> for any vector index. You can set the mode to <code>CLASSIC</code> only for a vector index in a vector bucket created before September 30, 2026. This operation doesn't change the default index mode of the vector bucket or the mode of other vector indexes. Specify the vector index by using its Amazon Resource Name (ARN) or both the vector bucket name and vector index name.</p> <dl> <dt>Permissions</dt> <dd> <p>You must have the <code>s3vectors:UpdateIndexMode</code> permission to use this operation.</p> </dd> </dl>

        Args:
            vector_bucket_name: <p>The name of the vector bucket that contains the vector index.</p>
            index_name: <p>The name of the vector index to update.</p>
            index_arn: <p>The Amazon Resource Name (ARN) of the vector index to update.</p>
            index_mode: <p>The new mode for the vector index.</p> <p>Valid values:</p> <ul> <li> <p> <code>CLASSIC</code> - Applies metadata filters during the vector search. You can specify <code>CLASSIC</code> only for a vector index in a vector bucket created before September 30, 2026.</p> </li> <li> <p> <code>ENHANCED</code> - Applies metadata filters before the vector search.</p> </li> </ul>

        Raises:
            capo_s3vectors.errors.access_denied_exception.AccessDeniedException: <p>Access denied.</p>
            capo_s3vectors.errors.internal_server_exception.InternalServerException: <p>The request failed due to an internal server error.</p>
            capo_s3vectors.errors.request_timeout_exception.RequestTimeoutException: <p>The request timed out. Retry your request.</p>
            capo_s3vectors.errors.too_many_requests_exception.TooManyRequestsException: <p>The request was denied due to request throttling.</p>
            capo_s3vectors.errors.validation_exception.ValidationException: <p>The requested action isn't valid.</p>
            capo_s3vectors.errors.not_found_exception.NotFoundException: <p>The request was rejected because the specified resource can't be found.</p>
            capo_s3vectors.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is unavailable. Wait briefly and retry your request. If it continues to fail, increase your waiting time between retries.</p>
            capo_s3vectors.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_s3vectors.types.update_index_mode_input.UpdateIndexModeInput]",
        ) -> OperationResponse[
            "capo_s3vectors.types.update_index_mode_output.UpdateIndexModeOutput"
        ]:
            import capo_s3vectors._operations.s3_vectors.update_index_mode

            output, http_response = (
                capo_s3vectors._operations.s3_vectors.update_index_mode.update_index_mode(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_s3vectors.types.update_index_mode_input.UpdateIndexModeInput = {
            "index_mode": index_mode
        }
        if vector_bucket_name is not None:
            input_["vector_bucket_name"] = vector_bucket_name
        if index_name is not None:
            input_["index_name"] = index_name
        if index_arn is not None:
            input_["index_arn"] = index_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_vectors(
        self,
        keys: "capo_s3vectors.types.delete_vectors_input_list.DeleteVectorsInputList",
        *,
        config_overrides: Optional[S3VectorsClientConfig] = None,
        vector_bucket_name: Optional[
            "capo_s3vectors.types.vector_bucket_name.VectorBucketName"
        ] = None,
        index_name: Optional["capo_s3vectors.types.index_name.IndexName"] = None,
        index_arn: Optional["capo_s3vectors.types.index_arn.IndexArn"] = None,
    ) -> "capo_s3vectors.types.delete_vectors_output.DeleteVectorsOutput":
        """<p>Deletes one or more vectors in a vector index. To specify the vector index, you can either use both the vector bucket name and vector index name, or use the vector index Amazon Resource Name (ARN). </p> <dl> <dt>Permissions</dt> <dd> <p>You must have the <code>s3vectors:DeleteVectors</code> permission to use this operation. </p> </dd> </dl>

        Args:
            vector_bucket_name: <p>The name of the vector bucket that contains the vector index. </p>
            index_name: <p>The name of the vector index that contains a vector you want to delete.</p>
            index_arn: <p>The ARN of the vector index that contains a vector you want to delete.</p>
            keys: <p>The keys of the vectors to delete. </p>

        Raises:
            capo_s3vectors.errors.access_denied_exception.AccessDeniedException: <p>Access denied.</p>
            capo_s3vectors.errors.internal_server_exception.InternalServerException: <p>The request failed due to an internal server error.</p>
            capo_s3vectors.errors.request_timeout_exception.RequestTimeoutException: <p>The request timed out. Retry your request.</p>
            capo_s3vectors.errors.too_many_requests_exception.TooManyRequestsException: <p>The request was denied due to request throttling.</p>
            capo_s3vectors.errors.validation_exception.ValidationException: <p>The requested action isn't valid.</p>
            capo_s3vectors.errors.kms_disabled_exception.KmsDisabledException: <p>The specified Amazon Web Services KMS key isn't enabled.</p>
            capo_s3vectors.errors.kms_invalid_key_usage_exception.KmsInvalidKeyUsageException: <p>The request was rejected for one of the following reasons: </p> <ul> <li> <p>The <code>KeyUsage</code> value of the KMS key is incompatible with the API operation.</p> </li> <li> <p>The encryption algorithm or signing algorithm specified for the operation is incompatible with the type of key material in the KMS key (<code>KeySpec</code>).</p> </li> </ul> <p>For more information, see <a href="https://docs.aws.amazon.com/kms/latest/APIReference/API_Encrypt.html#API_Encrypt_Errors">InvalidKeyUsageException</a> in the <i>Amazon Web Services Key Management Service API Reference</i>.</p>
            capo_s3vectors.errors.kms_invalid_state_exception.KmsInvalidStateException: <p>The key state of the KMS key isn't compatible with the operation.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/kms/latest/APIReference/API_Encrypt.html#API_Encrypt_Errors">KMSInvalidStateException</a> in the <i>Amazon Web Services Key Management Service API Reference</i>.</p>
            capo_s3vectors.errors.kms_not_found_exception.KmsNotFoundException: <p>The KMS key can't be found.</p>
            capo_s3vectors.errors.not_found_exception.NotFoundException: <p>The request was rejected because the specified resource can't be found.</p>
            capo_s3vectors.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is unavailable. Wait briefly and retry your request. If it continues to fail, increase your waiting time between retries.</p>
            capo_s3vectors.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_s3vectors.types.delete_vectors_input.DeleteVectorsInput]",
        ) -> OperationResponse[
            "capo_s3vectors.types.delete_vectors_output.DeleteVectorsOutput"
        ]:
            import capo_s3vectors._operations.s3_vectors.delete_vectors

            output, http_response = (
                capo_s3vectors._operations.s3_vectors.delete_vectors.delete_vectors(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_s3vectors.types.delete_vectors_input.DeleteVectorsInput = {
            "keys": keys
        }
        if vector_bucket_name is not None:
            input_["vector_bucket_name"] = vector_bucket_name
        if index_name is not None:
            input_["index_name"] = index_name
        if index_arn is not None:
            input_["index_arn"] = index_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_vectors(
        self,
        keys: "capo_s3vectors.types.get_vectors_input_list.GetVectorsInputList",
        *,
        config_overrides: Optional[S3VectorsClientConfig] = None,
        vector_bucket_name: Optional[
            "capo_s3vectors.types.vector_bucket_name.VectorBucketName"
        ] = None,
        index_name: Optional["capo_s3vectors.types.index_name.IndexName"] = None,
        index_arn: Optional["capo_s3vectors.types.index_arn.IndexArn"] = None,
        return_data: Optional[bool] = None,
        return_metadata: Optional[bool] = None,
    ) -> "capo_s3vectors.types.get_vectors_output.GetVectorsOutput":
        """<p>Returns vector attributes. To specify the vector index, you can either use both the vector bucket name and the vector index name, or use the vector index Amazon Resource Name (ARN). </p> <dl> <dt>Permissions</dt> <dd> <p>You must have the <code>s3vectors:GetVectors</code> permission to use this operation. </p> </dd> </dl>

        Args:
            vector_bucket_name: <p>The name of the vector bucket that contains the vector index. </p>
            index_name: <p>The name of the vector index.</p>
            index_arn: <p>The ARN of the vector index.</p>
            keys: <p>The names of the vectors you want to return attributes for. </p>
            return_data: <p>Indicates whether to include the vector data in the response. The default value is <code>false</code>.</p>
            return_metadata: <p>Indicates whether to include metadata in the response. The default value is <code>false</code>.</p>

        Raises:
            capo_s3vectors.errors.access_denied_exception.AccessDeniedException: <p>Access denied.</p>
            capo_s3vectors.errors.internal_server_exception.InternalServerException: <p>The request failed due to an internal server error.</p>
            capo_s3vectors.errors.request_timeout_exception.RequestTimeoutException: <p>The request timed out. Retry your request.</p>
            capo_s3vectors.errors.too_many_requests_exception.TooManyRequestsException: <p>The request was denied due to request throttling.</p>
            capo_s3vectors.errors.validation_exception.ValidationException: <p>The requested action isn't valid.</p>
            capo_s3vectors.errors.kms_disabled_exception.KmsDisabledException: <p>The specified Amazon Web Services KMS key isn't enabled.</p>
            capo_s3vectors.errors.kms_invalid_key_usage_exception.KmsInvalidKeyUsageException: <p>The request was rejected for one of the following reasons: </p> <ul> <li> <p>The <code>KeyUsage</code> value of the KMS key is incompatible with the API operation.</p> </li> <li> <p>The encryption algorithm or signing algorithm specified for the operation is incompatible with the type of key material in the KMS key (<code>KeySpec</code>).</p> </li> </ul> <p>For more information, see <a href="https://docs.aws.amazon.com/kms/latest/APIReference/API_Encrypt.html#API_Encrypt_Errors">InvalidKeyUsageException</a> in the <i>Amazon Web Services Key Management Service API Reference</i>.</p>
            capo_s3vectors.errors.kms_invalid_state_exception.KmsInvalidStateException: <p>The key state of the KMS key isn't compatible with the operation.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/kms/latest/APIReference/API_Encrypt.html#API_Encrypt_Errors">KMSInvalidStateException</a> in the <i>Amazon Web Services Key Management Service API Reference</i>.</p>
            capo_s3vectors.errors.kms_not_found_exception.KmsNotFoundException: <p>The KMS key can't be found.</p>
            capo_s3vectors.errors.not_found_exception.NotFoundException: <p>The request was rejected because the specified resource can't be found.</p>
            capo_s3vectors.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is unavailable. Wait briefly and retry your request. If it continues to fail, increase your waiting time between retries.</p>
            capo_s3vectors.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_s3vectors.types.get_vectors_input.GetVectorsInput]",
        ) -> OperationResponse[
            "capo_s3vectors.types.get_vectors_output.GetVectorsOutput"
        ]:
            import capo_s3vectors._operations.s3_vectors.get_vectors

            output, http_response = (
                capo_s3vectors._operations.s3_vectors.get_vectors.get_vectors(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_s3vectors.types.get_vectors_input.GetVectorsInput = {"keys": keys}
        if vector_bucket_name is not None:
            input_["vector_bucket_name"] = vector_bucket_name
        if index_name is not None:
            input_["index_name"] = index_name
        if index_arn is not None:
            input_["index_arn"] = index_arn
        if return_data is not None:
            input_["return_data"] = return_data
        if return_metadata is not None:
            input_["return_metadata"] = return_metadata

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_vectors(
        self,
        *,
        config_overrides: Optional[S3VectorsClientConfig] = None,
        vector_bucket_name: Optional[
            "capo_s3vectors.types.vector_bucket_name.VectorBucketName"
        ] = None,
        index_name: Optional["capo_s3vectors.types.index_name.IndexName"] = None,
        index_arn: Optional["capo_s3vectors.types.index_arn.IndexArn"] = None,
        max_results: Optional[
            "capo_s3vectors.types.list_vectors_max_results.ListVectorsMaxResults"
        ] = None,
        next_token: Optional[
            "capo_s3vectors.types.list_vectors_next_token.ListVectorsNextToken"
        ] = None,
        segment_count: Optional[
            "capo_s3vectors.types.list_vectors_segment_count.ListVectorsSegmentCount"
        ] = None,
        segment_index: Optional[
            "capo_s3vectors.types.list_vectors_segment_index.ListVectorsSegmentIndex"
        ] = None,
        return_data: Optional[bool] = None,
        return_metadata: Optional[bool] = None,
    ) -> "capo_s3vectors.types.list_vectors_output.ListVectorsOutput":
        """<p>List vectors in the specified vector index. To specify the vector index, you can either use both the vector bucket name and the vector index name, or use the vector index Amazon Resource Name (ARN). </p> <p> <code>ListVectors</code> operations proceed sequentially; however, for faster performance on a large number of vectors in a vector index, applications can request a parallel <code>ListVectors</code> operation by providing the <code>segmentCount</code> and <code>segmentIndex</code> parameters.</p> <dl> <dt>Permissions</dt> <dd> <p>You must have the <code>s3vectors:ListVectors</code> permission to use this operation. Additional permissions are required based on the request parameters you specify:</p> <ul> <li> <p>With only <code>s3vectors:ListVectors</code> permission, you can list vector keys when <code>returnData</code> and <code>returnMetadata</code> are both set to false or not specified..</p> </li> <li> <p>If you set <code>returnData</code> or <code>returnMetadata</code> to true, you must have both <code>s3vectors:ListVectors</code> and <code>s3vectors:GetVectors</code> permissions. The request fails with a <code>403 Forbidden</code> error if you request vector data or metadata without the <code>s3vectors:GetVectors</code> permission.</p> </li> </ul> </dd> </dl>

        Args:
            vector_bucket_name: <p>The name of the vector bucket. </p>
            index_name: <p>The name of the vector index.</p>
            index_arn: <p>The Amazon resource Name (ARN) of the vector index.</p>
            max_results: <p>The maximum number of vectors to return on a page.</p> <p>If you don't specify <code>maxResults</code>, the <code>ListVectors</code> operation uses a default value of 500.</p> <p>If the processed dataset size exceeds 1 MB before reaching the <code>maxResults</code> value, the operation stops and returns the vectors that are retrieved up to that point, along with a <code>nextToken</code> that you can use in a subsequent request to retrieve the next set of results.</p>
            next_token: <p>Pagination token from a previous request. The value of this field is empty for an initial request.</p>
            segment_count: <p>For a parallel <code>ListVectors</code> request, <code>segmentCount</code> represents the total number of vector segments into which the <code>ListVectors</code> operation will be divided. The value of <code>segmentCount</code> corresponds to the number of application workers that will perform the parallel <code>ListVectors</code> operation. For example, if you want to use four application threads to list vectors in a vector index, specify a <code>segmentCount</code> value of 4. </p> <p>If you specify a <code>segmentCount</code> value of 1, the <code>ListVectors</code> operation will be sequential rather than parallel.</p> <p>If you specify <code>segmentCount</code>, you must also specify <code>segmentIndex</code>.</p>
            segment_index: <p>For a parallel <code>ListVectors</code> request, <code>segmentIndex</code> is the index of the segment from which to list vectors in the current request. It identifies an individual segment to be listed by an application worker. </p> <p>Segment IDs are zero-based, so the first segment is always 0. For example, if you want to use four application threads to list vectors in a vector index, then the first thread specifies a <code>segmentIndex</code> value of 0, the second thread specifies 1, and so on. </p> <p>The value of <code>segmentIndex</code> must be less than the value provided for <code>segmentCount</code>. </p> <p>If you provide <code>segmentIndex</code>, you must also provide <code>segmentCount</code>.</p>
            return_data: <p>If true, the vector data of each vector will be included in the response. The default value is <code>false</code>.</p>
            return_metadata: <p>If true, the metadata associated with each vector will be included in the response. The default value is <code>false</code>.</p>

        Raises:
            capo_s3vectors.errors.access_denied_exception.AccessDeniedException: <p>Access denied.</p>
            capo_s3vectors.errors.internal_server_exception.InternalServerException: <p>The request failed due to an internal server error.</p>
            capo_s3vectors.errors.request_timeout_exception.RequestTimeoutException: <p>The request timed out. Retry your request.</p>
            capo_s3vectors.errors.too_many_requests_exception.TooManyRequestsException: <p>The request was denied due to request throttling.</p>
            capo_s3vectors.errors.validation_exception.ValidationException: <p>The requested action isn't valid.</p>
            capo_s3vectors.errors.not_found_exception.NotFoundException: <p>The request was rejected because the specified resource can't be found.</p>
            capo_s3vectors.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is unavailable. Wait briefly and retry your request. If it continues to fail, increase your waiting time between retries.</p>
            capo_s3vectors.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_s3vectors.types.list_vectors_input.ListVectorsInput]",
        ) -> OperationResponse[
            "capo_s3vectors.types.list_vectors_output.ListVectorsOutput"
        ]:
            import capo_s3vectors._operations.s3_vectors.list_vectors

            output, http_response = (
                capo_s3vectors._operations.s3_vectors.list_vectors.list_vectors(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_s3vectors.types.list_vectors_input.ListVectorsInput = {}
        if vector_bucket_name is not None:
            input_["vector_bucket_name"] = vector_bucket_name
        if index_name is not None:
            input_["index_name"] = index_name
        if index_arn is not None:
            input_["index_arn"] = index_arn
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if segment_count is not None:
            input_["segment_count"] = segment_count
        if segment_index is not None:
            input_["segment_index"] = segment_index
        if return_data is not None:
            input_["return_data"] = return_data
        if return_metadata is not None:
            input_["return_metadata"] = return_metadata

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_vectors(
        self,
        *,
        config_overrides: Optional[S3VectorsClientConfig] = None,
        vector_bucket_name: Optional[
            "capo_s3vectors.types.vector_bucket_name.VectorBucketName"
        ] = None,
        index_name: Optional["capo_s3vectors.types.index_name.IndexName"] = None,
        index_arn: Optional["capo_s3vectors.types.index_arn.IndexArn"] = None,
        max_results: Optional[
            "capo_s3vectors.types.list_vectors_max_results.ListVectorsMaxResults"
        ] = None,
        next_token: Optional[
            "capo_s3vectors.types.list_vectors_next_token.ListVectorsNextToken"
        ] = None,
        segment_count: Optional[
            "capo_s3vectors.types.list_vectors_segment_count.ListVectorsSegmentCount"
        ] = None,
        segment_index: Optional[
            "capo_s3vectors.types.list_vectors_segment_index.ListVectorsSegmentIndex"
        ] = None,
        return_data: Optional[bool] = None,
        return_metadata: Optional[bool] = None,
    ) -> "Iterator[capo_s3vectors.types.list_output_vector.ListOutputVector]":
        _token = next_token
        while True:
            _response = self.list_vectors(
                config_overrides=config_overrides,
                vector_bucket_name=vector_bucket_name,
                index_name=index_name,
                index_arn=index_arn,
                max_results=max_results,
                next_token=_token,
                segment_count=segment_count,
                segment_index=segment_index,
                return_data=return_data,
                return_metadata=return_metadata,
            )
            _page = _resolve_path(_response, ("vectors",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def put_vectors(
        self,
        vectors: "capo_s3vectors.types.put_vectors_input_list.PutVectorsInputList",
        *,
        config_overrides: Optional[S3VectorsClientConfig] = None,
        vector_bucket_name: Optional[
            "capo_s3vectors.types.vector_bucket_name.VectorBucketName"
        ] = None,
        index_name: Optional["capo_s3vectors.types.index_name.IndexName"] = None,
        index_arn: Optional["capo_s3vectors.types.index_arn.IndexArn"] = None,
    ) -> "capo_s3vectors.types.put_vectors_output.PutVectorsOutput":
        """<p>Adds one or more vectors to a vector index. To specify the vector index, you can either use both the vector bucket name and the vector index name, or use the vector index Amazon Resource Name (ARN). </p> <p>For more information about limits, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-vectors-limitations.html">Limitations and restrictions</a> in the <i>Amazon S3 User Guide</i>.</p> <note> <p>When inserting vector data into your vector index, you must provide the vector data as <code>float32</code> (32-bit floating point) values. If you pass higher-precision values to an Amazon Web Services SDK, S3 Vectors converts the values to 32-bit floating point before storing them, and <code>GetVectors</code>, <code>ListVectors</code>, and <code>QueryVectors</code> operations return the float32 values. Different Amazon Web Services SDKs may have different default numeric types, so ensure your vectors are properly formatted as <code>float32</code> values regardless of which SDK you're using. For example, in Python, use <code>numpy.float32</code> or explicitly cast your values.</p> </note> <dl> <dt>Permissions</dt> <dd> <p>You must have the <code>s3vectors:PutVectors</code> permission to use this operation. </p> </dd> </dl>

        Args:
            vector_bucket_name: <p>The name of the vector bucket that contains the vector index. </p>
            index_name: <p>The name of the vector index where you want to write vectors. </p>
            index_arn: <p>The ARN of the vector index where you want to write vectors.</p>
            vectors: <p>The vectors to add to a vector index. The number of vectors in a single request must not exceed the resource capacity, otherwise the request will be rejected with the error <code>ServiceUnavailableException</code> with the error message "Currently unable to handle the request".</p>

        Raises:
            capo_s3vectors.errors.access_denied_exception.AccessDeniedException: <p>Access denied.</p>
            capo_s3vectors.errors.internal_server_exception.InternalServerException: <p>The request failed due to an internal server error.</p>
            capo_s3vectors.errors.request_timeout_exception.RequestTimeoutException: <p>The request timed out. Retry your request.</p>
            capo_s3vectors.errors.too_many_requests_exception.TooManyRequestsException: <p>The request was denied due to request throttling.</p>
            capo_s3vectors.errors.validation_exception.ValidationException: <p>The requested action isn't valid.</p>
            capo_s3vectors.errors.kms_disabled_exception.KmsDisabledException: <p>The specified Amazon Web Services KMS key isn't enabled.</p>
            capo_s3vectors.errors.kms_invalid_key_usage_exception.KmsInvalidKeyUsageException: <p>The request was rejected for one of the following reasons: </p> <ul> <li> <p>The <code>KeyUsage</code> value of the KMS key is incompatible with the API operation.</p> </li> <li> <p>The encryption algorithm or signing algorithm specified for the operation is incompatible with the type of key material in the KMS key (<code>KeySpec</code>).</p> </li> </ul> <p>For more information, see <a href="https://docs.aws.amazon.com/kms/latest/APIReference/API_Encrypt.html#API_Encrypt_Errors">InvalidKeyUsageException</a> in the <i>Amazon Web Services Key Management Service API Reference</i>.</p>
            capo_s3vectors.errors.kms_invalid_state_exception.KmsInvalidStateException: <p>The key state of the KMS key isn't compatible with the operation.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/kms/latest/APIReference/API_Encrypt.html#API_Encrypt_Errors">KMSInvalidStateException</a> in the <i>Amazon Web Services Key Management Service API Reference</i>.</p>
            capo_s3vectors.errors.kms_not_found_exception.KmsNotFoundException: <p>The KMS key can't be found.</p>
            capo_s3vectors.errors.not_found_exception.NotFoundException: <p>The request was rejected because the specified resource can't be found.</p>
            capo_s3vectors.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Your request exceeds a service quota. </p>
            capo_s3vectors.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is unavailable. Wait briefly and retry your request. If it continues to fail, increase your waiting time between retries.</p>
            capo_s3vectors.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_s3vectors.types.put_vectors_input.PutVectorsInput]",
        ) -> OperationResponse[
            "capo_s3vectors.types.put_vectors_output.PutVectorsOutput"
        ]:
            import capo_s3vectors._operations.s3_vectors.put_vectors

            output, http_response = (
                capo_s3vectors._operations.s3_vectors.put_vectors.put_vectors(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_s3vectors.types.put_vectors_input.PutVectorsInput = {
            "vectors": vectors
        }
        if vector_bucket_name is not None:
            input_["vector_bucket_name"] = vector_bucket_name
        if index_name is not None:
            input_["index_name"] = index_name
        if index_arn is not None:
            input_["index_arn"] = index_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def query_vectors(
        self,
        top_k: "capo_s3vectors.types.top_k.TopK",
        query_vector: "capo_s3vectors.types.vector_data.VectorData",
        *,
        config_overrides: Optional[S3VectorsClientConfig] = None,
        vector_bucket_name: Optional[
            "capo_s3vectors.types.vector_bucket_name.VectorBucketName"
        ] = None,
        index_name: Optional["capo_s3vectors.types.index_name.IndexName"] = None,
        index_arn: Optional["capo_s3vectors.types.index_arn.IndexArn"] = None,
        filter: Optional[object] = None,
        query_mode: Optional["capo_s3vectors.types.index_mode.IndexMode"] = None,
        return_metadata: Optional[bool] = None,
        return_distance: Optional[bool] = None,
        next_token: Optional[
            "capo_s3vectors.types.query_vectors_next_token.QueryVectorsNextToken"
        ] = None,
    ) -> "capo_s3vectors.types.query_vectors_output.QueryVectorsOutput":
        """<p>Performs an approximate nearest neighbor search query in a vector index using a query vector. By default, it returns the keys of approximate nearest neighbors. You can optionally include the computed distance (between the query vector and each vector in the response) and metadata of each vector in the response.</p> <p>To specify the vector index, you can either use both the vector bucket name and the vector index name, or use the vector index Amazon Resource Name (ARN). </p> <dl> <dt>Permissions</dt> <dd> <p>You must have the <code>s3vectors:QueryVectors</code> permission to use this operation. Additional permissions are required based on the request parameters you specify:</p> <ul> <li> <p>With only <code>s3vectors:QueryVectors</code> permission, you can retrieve vector keys of approximate nearest neighbors and computed distances between these vectors. This permission is sufficient only when you don't set any metadata filters and don't request metadata (by keeping the <code>returnMetadata</code> parameter set to <code>false</code> or not specified).</p> </li> <li> <p>If you specify a metadata filter or set <code>returnMetadata</code> to true, you must have both <code>s3vectors:QueryVectors</code> and <code>s3vectors:GetVectors</code> permissions. The request fails with a <code>403 Forbidden error</code> if you request metadata filtering or metadata without the <code>s3vectors:GetVectors</code> permission.</p> </li> </ul> </dd> </dl>

        Args:
            vector_bucket_name: <p>The name of the vector bucket that contains the vector index. </p>
            index_name: <p>The name of the vector index that you want to query. </p>
            index_arn: <p>The ARN of the vector index that you want to query.</p>
            top_k: <p>The number of results to return for each query.</p>
            query_vector: <p>The query vector. Ensure that the query vector has the same dimension as the dimension of the vector index that's being queried. For example, if your vector index contains vectors with 384 dimensions, your query vector must also have 384 dimensions. </p>
            filter: <p>Metadata filter to apply during the query. For more information about metadata keys, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-vectors-metadata-filtering.html">Metadata filtering</a> in the <i>Amazon S3 User Guide</i>. </p>
            query_mode: <p>The mode to use to process the query. If you don't specify a query mode, the operation uses the mode that's currently configured for the vector index.</p> <p>Valid values:</p> <ul> <li> <p> <code>CLASSIC</code> - Applies metadata filters during the vector search. You can't specify <code>CLASSIC</code> for an <code>ENHANCED</code> index.</p> </li> <li> <p> <code>ENHANCED</code> - Applies metadata filters before the vector search.</p> </li> </ul>
            return_metadata: <p>Indicates whether to include metadata in the response. The default value is <code>false</code>.</p>
            return_distance: <p>Indicates whether to include the computed distance in the response. The default value is <code>false</code>.</p>
            next_token: <p>Pagination token from a previous request. The value of this field is empty for an initial request.</p>

        Raises:
            capo_s3vectors.errors.access_denied_exception.AccessDeniedException: <p>Access denied.</p>
            capo_s3vectors.errors.internal_server_exception.InternalServerException: <p>The request failed due to an internal server error.</p>
            capo_s3vectors.errors.request_timeout_exception.RequestTimeoutException: <p>The request timed out. Retry your request.</p>
            capo_s3vectors.errors.too_many_requests_exception.TooManyRequestsException: <p>The request was denied due to request throttling.</p>
            capo_s3vectors.errors.validation_exception.ValidationException: <p>The requested action isn't valid.</p>
            capo_s3vectors.errors.kms_disabled_exception.KmsDisabledException: <p>The specified Amazon Web Services KMS key isn't enabled.</p>
            capo_s3vectors.errors.kms_invalid_key_usage_exception.KmsInvalidKeyUsageException: <p>The request was rejected for one of the following reasons: </p> <ul> <li> <p>The <code>KeyUsage</code> value of the KMS key is incompatible with the API operation.</p> </li> <li> <p>The encryption algorithm or signing algorithm specified for the operation is incompatible with the type of key material in the KMS key (<code>KeySpec</code>).</p> </li> </ul> <p>For more information, see <a href="https://docs.aws.amazon.com/kms/latest/APIReference/API_Encrypt.html#API_Encrypt_Errors">InvalidKeyUsageException</a> in the <i>Amazon Web Services Key Management Service API Reference</i>.</p>
            capo_s3vectors.errors.kms_invalid_state_exception.KmsInvalidStateException: <p>The key state of the KMS key isn't compatible with the operation.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/kms/latest/APIReference/API_Encrypt.html#API_Encrypt_Errors">KMSInvalidStateException</a> in the <i>Amazon Web Services Key Management Service API Reference</i>.</p>
            capo_s3vectors.errors.kms_not_found_exception.KmsNotFoundException: <p>The KMS key can't be found.</p>
            capo_s3vectors.errors.not_found_exception.NotFoundException: <p>The request was rejected because the specified resource can't be found.</p>
            capo_s3vectors.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is unavailable. Wait briefly and retry your request. If it continues to fail, increase your waiting time between retries.</p>
            capo_s3vectors.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_s3vectors.types.query_vectors_input.QueryVectorsInput]",
        ) -> OperationResponse[
            "capo_s3vectors.types.query_vectors_output.QueryVectorsOutput"
        ]:
            import capo_s3vectors._operations.s3_vectors.query_vectors

            output, http_response = (
                capo_s3vectors._operations.s3_vectors.query_vectors.query_vectors(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_s3vectors.types.query_vectors_input.QueryVectorsInput = {
            "top_k": top_k,
            "query_vector": query_vector,
        }
        if vector_bucket_name is not None:
            input_["vector_bucket_name"] = vector_bucket_name
        if index_name is not None:
            input_["index_name"] = index_name
        if index_arn is not None:
            input_["index_arn"] = index_arn
        if filter is not None:
            input_["filter"] = filter
        if query_mode is not None:
            input_["query_mode"] = query_mode
        if return_metadata is not None:
            input_["return_metadata"] = return_metadata
        if return_distance is not None:
            input_["return_distance"] = return_distance
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_query_vectors(
        self,
        top_k: "capo_s3vectors.types.top_k.TopK",
        query_vector: "capo_s3vectors.types.vector_data.VectorData",
        *,
        config_overrides: Optional[S3VectorsClientConfig] = None,
        vector_bucket_name: Optional[
            "capo_s3vectors.types.vector_bucket_name.VectorBucketName"
        ] = None,
        index_name: Optional["capo_s3vectors.types.index_name.IndexName"] = None,
        index_arn: Optional["capo_s3vectors.types.index_arn.IndexArn"] = None,
        filter: Optional[object] = None,
        query_mode: Optional["capo_s3vectors.types.index_mode.IndexMode"] = None,
        return_metadata: Optional[bool] = None,
        return_distance: Optional[bool] = None,
        next_token: Optional[
            "capo_s3vectors.types.query_vectors_next_token.QueryVectorsNextToken"
        ] = None,
    ) -> "Iterator[capo_s3vectors.types.query_output_vector.QueryOutputVector]":
        _token = next_token
        while True:
            _response = self.query_vectors(
                top_k,
                query_vector,
                config_overrides=config_overrides,
                vector_bucket_name=vector_bucket_name,
                index_name=index_name,
                index_arn=index_arn,
                filter=filter,
                query_mode=query_mode,
                return_metadata=return_metadata,
                return_distance=return_distance,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("vectors",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def __enter__(self) -> Self:
        return self

    def __exit__(self, exc_type: Any, exc: Any, tb: Any):
        self._client.close()
