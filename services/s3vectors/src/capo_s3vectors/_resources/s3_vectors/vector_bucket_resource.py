from __future__ import annotations

from typing import TYPE_CHECKING, Optional

import capo_s3vectors._auth._signers
import capo_s3vectors._auth._sigv4
from capo_s3vectors._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_s3vectors.types.create_vector_bucket_input
    import capo_s3vectors.types.create_vector_bucket_output
    import capo_s3vectors.types.delete_vector_bucket_input
    import capo_s3vectors.types.delete_vector_bucket_output
    import capo_s3vectors.types.delete_vector_bucket_policy_input
    import capo_s3vectors.types.delete_vector_bucket_policy_output
    import capo_s3vectors.types.encryption_configuration
    import capo_s3vectors.types.get_vector_bucket_input
    import capo_s3vectors.types.get_vector_bucket_output
    import capo_s3vectors.types.get_vector_bucket_policy_input
    import capo_s3vectors.types.get_vector_bucket_policy_output
    import capo_s3vectors.types.index_mode
    import capo_s3vectors.types.list_vector_buckets_input
    import capo_s3vectors.types.list_vector_buckets_max_results
    import capo_s3vectors.types.list_vector_buckets_next_token
    import capo_s3vectors.types.list_vector_buckets_output
    import capo_s3vectors.types.list_vector_buckets_prefix
    import capo_s3vectors.types.put_vector_bucket_default_index_mode_input
    import capo_s3vectors.types.put_vector_bucket_default_index_mode_output
    import capo_s3vectors.types.put_vector_bucket_policy_input
    import capo_s3vectors.types.put_vector_bucket_policy_output
    import capo_s3vectors.types.tags_map
    import capo_s3vectors.types.vector_bucket_arn
    import capo_s3vectors.types.vector_bucket_name
    import capo_s3vectors.types.vector_bucket_policy
    import capo_s3vectors.types.vector_bucket_summary
    from capo_s3vectors._services.async_s3_vectors import (
        AsyncS3VectorsClient,
        AsyncS3VectorsClientConfig,
    )
    from capo_s3vectors._services.s3_vectors import (
        S3VectorsClient,
        S3VectorsClientConfig,
    )


class VectorBucketResource:
    def __init__(self, service: S3VectorsClient) -> None:
        self._service = service

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

        interceptors_, options_ = self._service.operation_options(config_overrides)
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

        interceptors_, options_ = self._service.operation_options(config_overrides)
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

        interceptors_, options_ = self._service.operation_options(config_overrides)
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

        interceptors_, options_ = self._service.operation_options(config_overrides)
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

        interceptors_, options_ = self._service.operation_options(config_overrides)
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

        interceptors_, options_ = self._service.operation_options(config_overrides)
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

        interceptors_, options_ = self._service.operation_options(config_overrides)
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

        interceptors_, options_ = self._service.operation_options(config_overrides)
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


class AsyncVectorBucketResource:
    def __init__(self, service: AsyncS3VectorsClient) -> None:
        self._service = service

    async def create_vector_bucket(
        self,
        vector_bucket_name: "capo_s3vectors.types.vector_bucket_name.VectorBucketName",
        *,
        config_overrides: Optional[AsyncS3VectorsClientConfig] = None,
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

        async def _handler(
            req: "AsyncOperationRequest[capo_s3vectors.types.create_vector_bucket_input.CreateVectorBucketInput]",
        ) -> AsyncOperationResponse[
            "capo_s3vectors.types.create_vector_bucket_output.CreateVectorBucketOutput"
        ]:
            import capo_s3vectors._operations.s3_vectors.create_vector_bucket

            (
                output,
                http_response,
            ) = await capo_s3vectors._operations.s3_vectors.create_vector_bucket.async_create_vector_bucket(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_s3vectors.types.create_vector_bucket_input.CreateVectorBucketInput = {
            "vector_bucket_name": vector_bucket_name
        }
        if encryption_configuration is not None:
            input_["encryption_configuration"] = encryption_configuration
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_vector_bucket(
        self,
        *,
        config_overrides: Optional[AsyncS3VectorsClientConfig] = None,
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

        async def _handler(
            req: "AsyncOperationRequest[capo_s3vectors.types.delete_vector_bucket_input.DeleteVectorBucketInput]",
        ) -> AsyncOperationResponse[
            "capo_s3vectors.types.delete_vector_bucket_output.DeleteVectorBucketOutput"
        ]:
            import capo_s3vectors._operations.s3_vectors.delete_vector_bucket

            (
                output,
                http_response,
            ) = await capo_s3vectors._operations.s3_vectors.delete_vector_bucket.async_delete_vector_bucket(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_s3vectors.types.delete_vector_bucket_input.DeleteVectorBucketInput = {}
        if vector_bucket_name is not None:
            input_["vector_bucket_name"] = vector_bucket_name
        if vector_bucket_arn is not None:
            input_["vector_bucket_arn"] = vector_bucket_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_vector_bucket_policy(
        self,
        *,
        config_overrides: Optional[AsyncS3VectorsClientConfig] = None,
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

        async def _handler(
            req: "AsyncOperationRequest[capo_s3vectors.types.delete_vector_bucket_policy_input.DeleteVectorBucketPolicyInput]",
        ) -> AsyncOperationResponse[
            "capo_s3vectors.types.delete_vector_bucket_policy_output.DeleteVectorBucketPolicyOutput"
        ]:
            import capo_s3vectors._operations.s3_vectors.delete_vector_bucket_policy

            (
                output,
                http_response,
            ) = await capo_s3vectors._operations.s3_vectors.delete_vector_bucket_policy.async_delete_vector_bucket_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_s3vectors.types.delete_vector_bucket_policy_input.DeleteVectorBucketPolicyInput = {}
        if vector_bucket_name is not None:
            input_["vector_bucket_name"] = vector_bucket_name
        if vector_bucket_arn is not None:
            input_["vector_bucket_arn"] = vector_bucket_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_vector_bucket(
        self,
        *,
        config_overrides: Optional[AsyncS3VectorsClientConfig] = None,
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

        async def _handler(
            req: "AsyncOperationRequest[capo_s3vectors.types.get_vector_bucket_input.GetVectorBucketInput]",
        ) -> AsyncOperationResponse[
            "capo_s3vectors.types.get_vector_bucket_output.GetVectorBucketOutput"
        ]:
            import capo_s3vectors._operations.s3_vectors.get_vector_bucket

            (
                output,
                http_response,
            ) = await capo_s3vectors._operations.s3_vectors.get_vector_bucket.async_get_vector_bucket(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_s3vectors.types.get_vector_bucket_input.GetVectorBucketInput = {}
        if vector_bucket_name is not None:
            input_["vector_bucket_name"] = vector_bucket_name
        if vector_bucket_arn is not None:
            input_["vector_bucket_arn"] = vector_bucket_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_vector_bucket_policy(
        self,
        *,
        config_overrides: Optional[AsyncS3VectorsClientConfig] = None,
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

        async def _handler(
            req: "AsyncOperationRequest[capo_s3vectors.types.get_vector_bucket_policy_input.GetVectorBucketPolicyInput]",
        ) -> AsyncOperationResponse[
            "capo_s3vectors.types.get_vector_bucket_policy_output.GetVectorBucketPolicyOutput"
        ]:
            import capo_s3vectors._operations.s3_vectors.get_vector_bucket_policy

            (
                output,
                http_response,
            ) = await capo_s3vectors._operations.s3_vectors.get_vector_bucket_policy.async_get_vector_bucket_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_s3vectors.types.get_vector_bucket_policy_input.GetVectorBucketPolicyInput = {}
        if vector_bucket_name is not None:
            input_["vector_bucket_name"] = vector_bucket_name
        if vector_bucket_arn is not None:
            input_["vector_bucket_arn"] = vector_bucket_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_vector_buckets(
        self,
        *,
        config_overrides: Optional[AsyncS3VectorsClientConfig] = None,
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

        async def _handler(
            req: "AsyncOperationRequest[capo_s3vectors.types.list_vector_buckets_input.ListVectorBucketsInput]",
        ) -> AsyncOperationResponse[
            "capo_s3vectors.types.list_vector_buckets_output.ListVectorBucketsOutput"
        ]:
            import capo_s3vectors._operations.s3_vectors.list_vector_buckets

            (
                output,
                http_response,
            ) = await capo_s3vectors._operations.s3_vectors.list_vector_buckets.async_list_vector_buckets(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_s3vectors.types.list_vector_buckets_input.ListVectorBucketsInput = {}
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if prefix is not None:
            input_["prefix"] = prefix

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def put_vector_bucket_default_index_mode(
        self,
        default_index_mode: "capo_s3vectors.types.index_mode.IndexMode",
        *,
        config_overrides: Optional[AsyncS3VectorsClientConfig] = None,
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

        async def _handler(
            req: "AsyncOperationRequest[capo_s3vectors.types.put_vector_bucket_default_index_mode_input.PutVectorBucketDefaultIndexModeInput]",
        ) -> AsyncOperationResponse[
            "capo_s3vectors.types.put_vector_bucket_default_index_mode_output.PutVectorBucketDefaultIndexModeOutput"
        ]:
            import capo_s3vectors._operations.s3_vectors.put_vector_bucket_default_index_mode

            (
                output,
                http_response,
            ) = await capo_s3vectors._operations.s3_vectors.put_vector_bucket_default_index_mode.async_put_vector_bucket_default_index_mode(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_s3vectors.types.put_vector_bucket_default_index_mode_input.PutVectorBucketDefaultIndexModeInput = {
            "default_index_mode": default_index_mode
        }
        if vector_bucket_name is not None:
            input_["vector_bucket_name"] = vector_bucket_name
        if vector_bucket_arn is not None:
            input_["vector_bucket_arn"] = vector_bucket_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def put_vector_bucket_policy(
        self,
        policy: "capo_s3vectors.types.vector_bucket_policy.VectorBucketPolicy",
        *,
        config_overrides: Optional[AsyncS3VectorsClientConfig] = None,
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

        async def _handler(
            req: "AsyncOperationRequest[capo_s3vectors.types.put_vector_bucket_policy_input.PutVectorBucketPolicyInput]",
        ) -> AsyncOperationResponse[
            "capo_s3vectors.types.put_vector_bucket_policy_output.PutVectorBucketPolicyOutput"
        ]:
            import capo_s3vectors._operations.s3_vectors.put_vector_bucket_policy

            (
                output,
                http_response,
            ) = await capo_s3vectors._operations.s3_vectors.put_vector_bucket_policy.async_put_vector_bucket_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_s3vectors.types.put_vector_bucket_policy_input.PutVectorBucketPolicyInput = {
            "policy": policy
        }
        if vector_bucket_name is not None:
            input_["vector_bucket_name"] = vector_bucket_name
        if vector_bucket_arn is not None:
            input_["vector_bucket_arn"] = vector_bucket_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
