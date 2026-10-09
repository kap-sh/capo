"""Generated from Smithy shape ``com.amazonaws.elastictranscoder#EtsCustomerService``."""

import warnings
from collections.abc import Iterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import BaseHandler, Client

import capo_elastic_transcoder._auth._signers
import capo_elastic_transcoder._auth._sigv4
from capo_elastic_transcoder._auth._identity import Credentials
from capo_elastic_transcoder._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_elastic_transcoder._auth._zapros_handler import AuthMiddleware
from capo_elastic_transcoder._pagination import resolve_path as _resolve_path
from capo_elastic_transcoder._services._aws_config import aws_config
from capo_elastic_transcoder._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import capo_elastic_transcoder.types.ascending
    import capo_elastic_transcoder.types.audio_parameters
    import capo_elastic_transcoder.types.bucket_name
    import capo_elastic_transcoder.types.cancel_job_request
    import capo_elastic_transcoder.types.cancel_job_response
    import capo_elastic_transcoder.types.create_job_output
    import capo_elastic_transcoder.types.create_job_outputs
    import capo_elastic_transcoder.types.create_job_playlists
    import capo_elastic_transcoder.types.create_job_request
    import capo_elastic_transcoder.types.create_job_response
    import capo_elastic_transcoder.types.create_pipeline_request
    import capo_elastic_transcoder.types.create_pipeline_response
    import capo_elastic_transcoder.types.create_preset_request
    import capo_elastic_transcoder.types.create_preset_response
    import capo_elastic_transcoder.types.delete_pipeline_request
    import capo_elastic_transcoder.types.delete_pipeline_response
    import capo_elastic_transcoder.types.delete_preset_request
    import capo_elastic_transcoder.types.delete_preset_response
    import capo_elastic_transcoder.types.description
    import capo_elastic_transcoder.types.id
    import capo_elastic_transcoder.types.job
    import capo_elastic_transcoder.types.job_input
    import capo_elastic_transcoder.types.job_inputs
    import capo_elastic_transcoder.types.job_status
    import capo_elastic_transcoder.types.key
    import capo_elastic_transcoder.types.key_arn
    import capo_elastic_transcoder.types.list_jobs_by_pipeline_request
    import capo_elastic_transcoder.types.list_jobs_by_pipeline_response
    import capo_elastic_transcoder.types.list_jobs_by_status_request
    import capo_elastic_transcoder.types.list_jobs_by_status_response
    import capo_elastic_transcoder.types.list_pipelines_request
    import capo_elastic_transcoder.types.list_pipelines_response
    import capo_elastic_transcoder.types.list_presets_request
    import capo_elastic_transcoder.types.list_presets_response
    import capo_elastic_transcoder.types.name
    import capo_elastic_transcoder.types.notifications
    import capo_elastic_transcoder.types.pipeline
    import capo_elastic_transcoder.types.pipeline_output_config
    import capo_elastic_transcoder.types.pipeline_status
    import capo_elastic_transcoder.types.preset
    import capo_elastic_transcoder.types.preset_container
    import capo_elastic_transcoder.types.read_job_request
    import capo_elastic_transcoder.types.read_job_response
    import capo_elastic_transcoder.types.read_pipeline_request
    import capo_elastic_transcoder.types.read_pipeline_response
    import capo_elastic_transcoder.types.read_preset_request
    import capo_elastic_transcoder.types.read_preset_response
    import capo_elastic_transcoder.types.role
    import capo_elastic_transcoder.types.sns_topics
    import capo_elastic_transcoder.types.test_role_request
    import capo_elastic_transcoder.types.test_role_response
    import capo_elastic_transcoder.types.thumbnails
    import capo_elastic_transcoder.types.update_pipeline_notifications_request
    import capo_elastic_transcoder.types.update_pipeline_notifications_response
    import capo_elastic_transcoder.types.update_pipeline_request
    import capo_elastic_transcoder.types.update_pipeline_response
    import capo_elastic_transcoder.types.update_pipeline_status_request
    import capo_elastic_transcoder.types.update_pipeline_status_response
    import capo_elastic_transcoder.types.user_metadata
    import capo_elastic_transcoder.types.video_parameters


class ElasticTranscoderClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None
    anonymous: bool | None


class ElasticTranscoderClient:
    """A client for the ``ElasticTranscoder`` service.

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
        self._config = ElasticTranscoderClientConfig(
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
        self, config_overrides: Optional[ElasticTranscoderClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: ElasticTranscoderClientConfig = config_overrides or {}
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

    def cancel_job(
        self,
        id: "capo_elastic_transcoder.types.id.Id",
        *,
        config_overrides: Optional[ElasticTranscoderClientConfig] = None,
    ) -> "capo_elastic_transcoder.types.cancel_job_response.CancelJobResponse":
        """<p>The CancelJob operation cancels an unfinished job.</p> <note> <p>You can only cancel a job that has a status of <code>Submitted</code>. To prevent a pipeline from starting to process a job while you're getting the job identifier, use <a>UpdatePipelineStatus</a> to temporarily pause the pipeline.</p> </note>

        Args:
            id: <p>The identifier of the job that you want to cancel.</p> <p>To get a list of the jobs (including their <code>jobId</code>) that have a status of <code>Submitted</code>, use the <a>ListJobsByStatus</a> API action.</p>

        Raises:
            capo_elastic_transcoder.errors.access_denied_exception.AccessDeniedException: <p>General authentication failure. The request was not signed correctly.</p>
            capo_elastic_transcoder.errors.incompatible_version_exception.IncompatibleVersionException
            capo_elastic_transcoder.errors.internal_service_exception.InternalServiceException: <p>Elastic Transcoder encountered an unexpected exception while trying to fulfill the request.</p>
            capo_elastic_transcoder.errors.resource_in_use_exception.ResourceInUseException: <p>The resource you are attempting to change is in use. For example, you are attempting to delete a pipeline that is currently in use.</p>
            capo_elastic_transcoder.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource does not exist or is not available. For example, the pipeline to which you're trying to add a job doesn't exist or is still being created.</p>
            capo_elastic_transcoder.errors.validation_exception.ValidationException: <p>One or more required parameter values were not provided in the request.</p>
            capo_elastic_transcoder.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_elastic_transcoder.types.cancel_job_request.CancelJobRequest]",
        ) -> OperationResponse[
            "capo_elastic_transcoder.types.cancel_job_response.CancelJobResponse"
        ]:
            import capo_elastic_transcoder._operations.ets_customer_service.cancel_job

            output, http_response = (
                capo_elastic_transcoder._operations.ets_customer_service.cancel_job.cancel_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elastic_transcoder.types.cancel_job_request.CancelJobRequest = {
            "id": id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_job(
        self,
        pipeline_id: "capo_elastic_transcoder.types.id.Id",
        *,
        config_overrides: Optional[ElasticTranscoderClientConfig] = None,
        input: Optional["capo_elastic_transcoder.types.job_input.JobInput"] = None,
        inputs: Optional["capo_elastic_transcoder.types.job_inputs.JobInputs"] = None,
        output: Optional[
            "capo_elastic_transcoder.types.create_job_output.CreateJobOutput"
        ] = None,
        outputs: Optional[
            "capo_elastic_transcoder.types.create_job_outputs.CreateJobOutputs"
        ] = None,
        output_key_prefix: Optional["capo_elastic_transcoder.types.key.Key"] = None,
        playlists: Optional[
            "capo_elastic_transcoder.types.create_job_playlists.CreateJobPlaylists"
        ] = None,
        user_metadata: Optional[
            "capo_elastic_transcoder.types.user_metadata.UserMetadata"
        ] = None,
    ) -> "capo_elastic_transcoder.types.create_job_response.CreateJobResponse":
        """<p>When you create a job, Elastic Transcoder returns JSON data that includes the values that you specified plus information about the job that is created.</p> <p>If you have specified more than one output for your jobs (for example, one output for the Kindle Fire and another output for the Apple iPhone 4s), you currently must use the Elastic Transcoder API to list the jobs (as opposed to the AWS Console).</p>

        Args:
            pipeline_id: <p>The <code>Id</code> of the pipeline that you want Elastic Transcoder to use for transcoding. The pipeline determines several settings, including the Amazon S3 bucket from which Elastic Transcoder gets the files to transcode and the bucket into which Elastic Transcoder puts the transcoded files.</p>
            input: <p>A section of the request body that provides information about the file that is being transcoded.</p>
            inputs: <p>A section of the request body that provides information about the files that are being transcoded.</p>
            output: <p> A section of the request body that provides information about the transcoded (target) file. We strongly recommend that you use the <code>Outputs</code> syntax instead of the <code>Output</code> syntax. </p>
            outputs: <p> A section of the request body that provides information about the transcoded (target) files. We recommend that you use the <code>Outputs</code> syntax instead of the <code>Output</code> syntax. </p>
            output_key_prefix: <p>The value, if any, that you want Elastic Transcoder to prepend to the names of all files that this job creates, including output files, thumbnails, and playlists.</p>
            playlists: <p>If you specify a preset in <code>PresetId</code> for which the value of <code>Container</code> is fmp4 (Fragmented MP4) or ts (MPEG-TS), Playlists contains information about the master playlists that you want Elastic Transcoder to create.</p> <p>The maximum number of master playlists in a job is 30.</p>
            user_metadata: <p>User-defined metadata that you want to associate with an Elastic Transcoder job. You specify metadata in <code>key/value</code> pairs, and you can add up to 10 <code>key/value</code> pairs per job. Elastic Transcoder does not guarantee that <code>key/value</code> pairs are returned in the same order in which you specify them.</p>

        Raises:
            capo_elastic_transcoder.errors.access_denied_exception.AccessDeniedException: <p>General authentication failure. The request was not signed correctly.</p>
            capo_elastic_transcoder.errors.incompatible_version_exception.IncompatibleVersionException
            capo_elastic_transcoder.errors.internal_service_exception.InternalServiceException: <p>Elastic Transcoder encountered an unexpected exception while trying to fulfill the request.</p>
            capo_elastic_transcoder.errors.limit_exceeded_exception.LimitExceededException: <p>Too many operations for a given AWS account. For example, the number of pipelines exceeds the maximum allowed.</p>
            capo_elastic_transcoder.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource does not exist or is not available. For example, the pipeline to which you're trying to add a job doesn't exist or is still being created.</p>
            capo_elastic_transcoder.errors.validation_exception.ValidationException: <p>One or more required parameter values were not provided in the request.</p>
            capo_elastic_transcoder.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_elastic_transcoder.types.create_job_request.CreateJobRequest]",
        ) -> OperationResponse[
            "capo_elastic_transcoder.types.create_job_response.CreateJobResponse"
        ]:
            import capo_elastic_transcoder._operations.ets_customer_service.create_job

            output, http_response = (
                capo_elastic_transcoder._operations.ets_customer_service.create_job.create_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elastic_transcoder.types.create_job_request.CreateJobRequest = {
            "pipeline_id": pipeline_id
        }
        if input is not None:
            input_["input"] = input
        if inputs is not None:
            input_["inputs"] = inputs
        if output is not None:
            input_["output"] = output
        if outputs is not None:
            input_["outputs"] = outputs
        if output_key_prefix is not None:
            input_["output_key_prefix"] = output_key_prefix
        if playlists is not None:
            input_["playlists"] = playlists
        if user_metadata is not None:
            input_["user_metadata"] = user_metadata

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_pipeline(
        self,
        name: "capo_elastic_transcoder.types.name.Name",
        input_bucket: "capo_elastic_transcoder.types.bucket_name.BucketName",
        role: "capo_elastic_transcoder.types.role.Role",
        *,
        config_overrides: Optional[ElasticTranscoderClientConfig] = None,
        output_bucket: Optional[
            "capo_elastic_transcoder.types.bucket_name.BucketName"
        ] = None,
        aws_kms_key_arn: Optional[
            "capo_elastic_transcoder.types.key_arn.KeyArn"
        ] = None,
        notifications: Optional[
            "capo_elastic_transcoder.types.notifications.Notifications"
        ] = None,
        content_config: Optional[
            "capo_elastic_transcoder.types.pipeline_output_config.PipelineOutputConfig"
        ] = None,
        thumbnail_config: Optional[
            "capo_elastic_transcoder.types.pipeline_output_config.PipelineOutputConfig"
        ] = None,
    ) -> (
        "capo_elastic_transcoder.types.create_pipeline_response.CreatePipelineResponse"
    ):
        """<p>The CreatePipeline operation creates a pipeline with settings that you specify.</p>

        Args:
            name: <p>The name of the pipeline. We recommend that the name be unique within the AWS account, but uniqueness is not enforced.</p> <p>Constraints: Maximum 40 characters.</p>
            input_bucket: <p>The Amazon S3 bucket in which you saved the media files that you want to transcode.</p>
            output_bucket: <p>The Amazon S3 bucket in which you want Elastic Transcoder to save the transcoded files. (Use this, or use ContentConfig:Bucket plus ThumbnailConfig:Bucket.)</p> <p>Specify this value when all of the following are true:</p> <ul> <li> <p>You want to save transcoded files, thumbnails (if any), and playlists (if any) together in one bucket.</p> </li> <li> <p>You do not want to specify the users or groups who have access to the transcoded files, thumbnails, and playlists.</p> </li> <li> <p>You do not want to specify the permissions that Elastic Transcoder grants to the files. </p> <important> <p>When Elastic Transcoder saves files in <code>OutputBucket</code>, it grants full control over the files only to the AWS account that owns the role that is specified by <code>Role</code>.</p> </important> </li> <li> <p>You want to associate the transcoded files and thumbnails with the Amazon S3 Standard storage class.</p> </li> </ul> <p>If you want to save transcoded files and playlists in one bucket and thumbnails in another bucket, specify which users can access the transcoded files or the permissions the users have, or change the Amazon S3 storage class, omit <code>OutputBucket</code> and specify values for <code>ContentConfig</code> and <code>ThumbnailConfig</code> instead.</p>
            role: <p>The IAM Amazon Resource Name (ARN) for the role that you want Elastic Transcoder to use to create the pipeline.</p>
            aws_kms_key_arn: <p>The AWS Key Management Service (AWS KMS) key that you want to use with this pipeline.</p> <p>If you use either <code>s3</code> or <code>s3-aws-kms</code> as your <code>Encryption:Mode</code>, you don't need to provide a key with your job because a default key, known as an AWS-KMS key, is created for you automatically. You need to provide an AWS-KMS key only if you want to use a non-default AWS-KMS key, or if you are using an <code>Encryption:Mode</code> of <code>aes-cbc-pkcs7</code>, <code>aes-ctr</code>, or <code>aes-gcm</code>.</p>
            notifications: <p>The Amazon Simple Notification Service (Amazon SNS) topic that you want to notify to report job status.</p> <important> <p>To receive notifications, you must also subscribe to the new topic in the Amazon SNS console.</p> </important> <ul> <li> <p> <b>Progressing</b>: The topic ARN for the Amazon Simple Notification Service (Amazon SNS) topic that you want to notify when Elastic Transcoder has started to process a job in this pipeline. This is the ARN that Amazon SNS returned when you created the topic. For more information, see Create a Topic in the Amazon Simple Notification Service Developer Guide.</p> </li> <li> <p> <b>Complete</b>: The topic ARN for the Amazon SNS topic that you want to notify when Elastic Transcoder has finished processing a job in this pipeline. This is the ARN that Amazon SNS returned when you created the topic.</p> </li> <li> <p> <b>Warning</b>: The topic ARN for the Amazon SNS topic that you want to notify when Elastic Transcoder encounters a warning condition while processing a job in this pipeline. This is the ARN that Amazon SNS returned when you created the topic.</p> </li> <li> <p> <b>Error</b>: The topic ARN for the Amazon SNS topic that you want to notify when Elastic Transcoder encounters an error condition while processing a job in this pipeline. This is the ARN that Amazon SNS returned when you created the topic.</p> </li> </ul>
            content_config: <p>The optional <code>ContentConfig</code> object specifies information about the Amazon S3 bucket in which you want Elastic Transcoder to save transcoded files and playlists: which bucket to use, which users you want to have access to the files, the type of access you want users to have, and the storage class that you want to assign to the files.</p> <p>If you specify values for <code>ContentConfig</code>, you must also specify values for <code>ThumbnailConfig</code>.</p> <p>If you specify values for <code>ContentConfig</code> and <code>ThumbnailConfig</code>, omit the <code>OutputBucket</code> object.</p> <ul> <li> <p> <b>Bucket</b>: The Amazon S3 bucket in which you want Elastic Transcoder to save transcoded files and playlists.</p> </li> <li> <p> <b>Permissions</b> (Optional): The Permissions object specifies which users you want to have access to transcoded files and the type of access you want them to have. You can grant permissions to a maximum of 30 users and/or predefined Amazon S3 groups.</p> </li> <li> <p> <b>Grantee Type</b>: Specify the type of value that appears in the <code>Grantee</code> object: </p> <ul> <li> <p> <b>Canonical</b>: The value in the <code>Grantee</code> object is either the canonical user ID for an AWS account or an origin access identity for an Amazon CloudFront distribution. For more information about canonical user IDs, see Access Control List (ACL) Overview in the Amazon Simple Storage Service Developer Guide. For more information about using CloudFront origin access identities to require that users use CloudFront URLs instead of Amazon S3 URLs, see Using an Origin Access Identity to Restrict Access to Your Amazon S3 Content.</p> <important> <p>A canonical user ID is not the same as an AWS account number.</p> </important> </li> <li> <p> <b>Email</b>: The value in the <code>Grantee</code> object is the registered email address of an AWS account.</p> </li> <li> <p> <b>Group</b>: The value in the <code>Grantee</code> object is one of the following predefined Amazon S3 groups: <code>AllUsers</code>, <code>AuthenticatedUsers</code>, or <code>LogDelivery</code>.</p> </li> </ul> </li> <li> <p> <b>Grantee</b>: The AWS user or group that you want to have access to transcoded files and playlists. To identify the user or group, you can specify the canonical user ID for an AWS account, an origin access identity for a CloudFront distribution, the registered email address of an AWS account, or a predefined Amazon S3 group </p> </li> <li> <p> <b>Access</b>: The permission that you want to give to the AWS user that you specified in <code>Grantee</code>. Permissions are granted on the files that Elastic Transcoder adds to the bucket, including playlists and video files. Valid values include: </p> <ul> <li> <p> <code>READ</code>: The grantee can read the objects and metadata for objects that Elastic Transcoder adds to the Amazon S3 bucket.</p> </li> <li> <p> <code>READ_ACP</code>: The grantee can read the object ACL for objects that Elastic Transcoder adds to the Amazon S3 bucket.</p> </li> <li> <p> <code>WRITE_ACP</code>: The grantee can write the ACL for the objects that Elastic Transcoder adds to the Amazon S3 bucket.</p> </li> <li> <p> <code>FULL_CONTROL</code>: The grantee has <code>READ</code>, <code>READ_ACP</code>, and <code>WRITE_ACP</code> permissions for the objects that Elastic Transcoder adds to the Amazon S3 bucket.</p> </li> </ul> </li> <li> <p> <b>StorageClass</b>: The Amazon S3 storage class, <code>Standard</code> or <code>ReducedRedundancy</code>, that you want Elastic Transcoder to assign to the video files and playlists that it stores in your Amazon S3 bucket.</p> </li> </ul>
            thumbnail_config: <p>The <code>ThumbnailConfig</code> object specifies several values, including the Amazon S3 bucket in which you want Elastic Transcoder to save thumbnail files, which users you want to have access to the files, the type of access you want users to have, and the storage class that you want to assign to the files.</p> <p>If you specify values for <code>ContentConfig</code>, you must also specify values for <code>ThumbnailConfig</code> even if you don't want to create thumbnails.</p> <p>If you specify values for <code>ContentConfig</code> and <code>ThumbnailConfig</code>, omit the <code>OutputBucket</code> object.</p> <ul> <li> <p> <b>Bucket</b>: The Amazon S3 bucket in which you want Elastic Transcoder to save thumbnail files.</p> </li> <li> <p> <b>Permissions</b> (Optional): The <code>Permissions</code> object specifies which users and/or predefined Amazon S3 groups you want to have access to thumbnail files, and the type of access you want them to have. You can grant permissions to a maximum of 30 users and/or predefined Amazon S3 groups.</p> </li> <li> <p> <b>GranteeType</b>: Specify the type of value that appears in the Grantee object: </p> <ul> <li> <p> <b>Canonical</b>: The value in the <code>Grantee</code> object is either the canonical user ID for an AWS account or an origin access identity for an Amazon CloudFront distribution.</p> <important> <p>A canonical user ID is not the same as an AWS account number.</p> </important> </li> <li> <p> <b>Email</b>: The value in the <code>Grantee</code> object is the registered email address of an AWS account. </p> </li> <li> <p> <b>Group</b>: The value in the <code>Grantee</code> object is one of the following predefined Amazon S3 groups: <code>AllUsers</code>, <code>AuthenticatedUsers</code>, or <code>LogDelivery</code>.</p> </li> </ul> </li> <li> <p> <b>Grantee</b>: The AWS user or group that you want to have access to thumbnail files. To identify the user or group, you can specify the canonical user ID for an AWS account, an origin access identity for a CloudFront distribution, the registered email address of an AWS account, or a predefined Amazon S3 group. </p> </li> <li> <p> <b>Access</b>: The permission that you want to give to the AWS user that you specified in <code>Grantee</code>. Permissions are granted on the thumbnail files that Elastic Transcoder adds to the bucket. Valid values include: </p> <ul> <li> <p> <code>READ</code>: The grantee can read the thumbnails and metadata for objects that Elastic Transcoder adds to the Amazon S3 bucket.</p> </li> <li> <p> <code>READ_ACP</code>: The grantee can read the object ACL for thumbnails that Elastic Transcoder adds to the Amazon S3 bucket.</p> </li> <li> <p> <code>WRITE_ACP</code>: The grantee can write the ACL for the thumbnails that Elastic Transcoder adds to the Amazon S3 bucket.</p> </li> <li> <p> <code>FULL_CONTROL</code>: The grantee has <code>READ</code>, <code>READ_ACP</code>, and <code>WRITE_ACP</code> permissions for the thumbnails that Elastic Transcoder adds to the Amazon S3 bucket.</p> </li> </ul> </li> <li> <p> <b>StorageClass</b>: The Amazon S3 storage class, <code>Standard</code> or <code>ReducedRedundancy</code>, that you want Elastic Transcoder to assign to the thumbnails that it stores in your Amazon S3 bucket.</p> </li> </ul>

        Raises:
            capo_elastic_transcoder.errors.access_denied_exception.AccessDeniedException: <p>General authentication failure. The request was not signed correctly.</p>
            capo_elastic_transcoder.errors.incompatible_version_exception.IncompatibleVersionException
            capo_elastic_transcoder.errors.internal_service_exception.InternalServiceException: <p>Elastic Transcoder encountered an unexpected exception while trying to fulfill the request.</p>
            capo_elastic_transcoder.errors.limit_exceeded_exception.LimitExceededException: <p>Too many operations for a given AWS account. For example, the number of pipelines exceeds the maximum allowed.</p>
            capo_elastic_transcoder.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource does not exist or is not available. For example, the pipeline to which you're trying to add a job doesn't exist or is still being created.</p>
            capo_elastic_transcoder.errors.validation_exception.ValidationException: <p>One or more required parameter values were not provided in the request.</p>
            capo_elastic_transcoder.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_elastic_transcoder.types.create_pipeline_request.CreatePipelineRequest]",
        ) -> OperationResponse[
            "capo_elastic_transcoder.types.create_pipeline_response.CreatePipelineResponse"
        ]:
            import capo_elastic_transcoder._operations.ets_customer_service.create_pipeline

            output, http_response = (
                capo_elastic_transcoder._operations.ets_customer_service.create_pipeline.create_pipeline(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elastic_transcoder.types.create_pipeline_request.CreatePipelineRequest = {
            "name": name,
            "input_bucket": input_bucket,
            "role": role,
        }
        if output_bucket is not None:
            input_["output_bucket"] = output_bucket
        if aws_kms_key_arn is not None:
            input_["aws_kms_key_arn"] = aws_kms_key_arn
        if notifications is not None:
            input_["notifications"] = notifications
        if content_config is not None:
            input_["content_config"] = content_config
        if thumbnail_config is not None:
            input_["thumbnail_config"] = thumbnail_config

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_preset(
        self,
        name: "capo_elastic_transcoder.types.name.Name",
        container: "capo_elastic_transcoder.types.preset_container.PresetContainer",
        *,
        config_overrides: Optional[ElasticTranscoderClientConfig] = None,
        description: Optional[
            "capo_elastic_transcoder.types.description.Description"
        ] = None,
        video: Optional[
            "capo_elastic_transcoder.types.video_parameters.VideoParameters"
        ] = None,
        audio: Optional[
            "capo_elastic_transcoder.types.audio_parameters.AudioParameters"
        ] = None,
        thumbnails: Optional[
            "capo_elastic_transcoder.types.thumbnails.Thumbnails"
        ] = None,
    ) -> "capo_elastic_transcoder.types.create_preset_response.CreatePresetResponse":
        """<p>The CreatePreset operation creates a preset with settings that you specify.</p> <important> <p>Elastic Transcoder checks the CreatePreset settings to ensure that they meet Elastic Transcoder requirements and to determine whether they comply with H.264 standards. If your settings are not valid for Elastic Transcoder, Elastic Transcoder returns an HTTP 400 response (<code>ValidationException</code>) and does not create the preset. If the settings are valid for Elastic Transcoder but aren't strictly compliant with the H.264 standard, Elastic Transcoder creates the preset and returns a warning message in the response. This helps you determine whether your settings comply with the H.264 standard while giving you greater flexibility with respect to the video that Elastic Transcoder produces.</p> </important> <p>Elastic Transcoder uses the H.264 video-compression format. For more information, see the International Telecommunication Union publication <i>Recommendation ITU-T H.264: Advanced video coding for generic audiovisual services</i>.</p>

        Args:
            name: <p>The name of the preset. We recommend that the name be unique within the AWS account, but uniqueness is not enforced.</p>
            description: <p>A description of the preset.</p>
            container: <p>The container type for the output file. Valid values include <code>flac</code>, <code>flv</code>, <code>fmp4</code>, <code>gif</code>, <code>mp3</code>, <code>mp4</code>, <code>mpg</code>, <code>mxf</code>, <code>oga</code>, <code>ogg</code>, <code>ts</code>, and <code>webm</code>.</p>
            video: <p>A section of the request body that specifies the video parameters.</p>
            audio: <p>A section of the request body that specifies the audio parameters.</p>
            thumbnails: <p>A section of the request body that specifies the thumbnail parameters, if any.</p>

        Raises:
            capo_elastic_transcoder.errors.access_denied_exception.AccessDeniedException: <p>General authentication failure. The request was not signed correctly.</p>
            capo_elastic_transcoder.errors.incompatible_version_exception.IncompatibleVersionException
            capo_elastic_transcoder.errors.internal_service_exception.InternalServiceException: <p>Elastic Transcoder encountered an unexpected exception while trying to fulfill the request.</p>
            capo_elastic_transcoder.errors.limit_exceeded_exception.LimitExceededException: <p>Too many operations for a given AWS account. For example, the number of pipelines exceeds the maximum allowed.</p>
            capo_elastic_transcoder.errors.validation_exception.ValidationException: <p>One or more required parameter values were not provided in the request.</p>
            capo_elastic_transcoder.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_elastic_transcoder.types.create_preset_request.CreatePresetRequest]",
        ) -> OperationResponse[
            "capo_elastic_transcoder.types.create_preset_response.CreatePresetResponse"
        ]:
            import capo_elastic_transcoder._operations.ets_customer_service.create_preset

            output, http_response = (
                capo_elastic_transcoder._operations.ets_customer_service.create_preset.create_preset(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elastic_transcoder.types.create_preset_request.CreatePresetRequest = {
            "name": name,
            "container": container,
        }
        if description is not None:
            input_["description"] = description
        if video is not None:
            input_["video"] = video
        if audio is not None:
            input_["audio"] = audio
        if thumbnails is not None:
            input_["thumbnails"] = thumbnails

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_pipeline(
        self,
        id: "capo_elastic_transcoder.types.id.Id",
        *,
        config_overrides: Optional[ElasticTranscoderClientConfig] = None,
    ) -> (
        "capo_elastic_transcoder.types.delete_pipeline_response.DeletePipelineResponse"
    ):
        """<p>The DeletePipeline operation removes a pipeline.</p> <p> You can only delete a pipeline that has never been used or that is not currently in use (doesn't contain any active jobs). If the pipeline is currently in use, <code>DeletePipeline</code> returns an error. </p>

        Args:
            id: <p>The identifier of the pipeline that you want to delete.</p>

        Raises:
            capo_elastic_transcoder.errors.access_denied_exception.AccessDeniedException: <p>General authentication failure. The request was not signed correctly.</p>
            capo_elastic_transcoder.errors.incompatible_version_exception.IncompatibleVersionException
            capo_elastic_transcoder.errors.internal_service_exception.InternalServiceException: <p>Elastic Transcoder encountered an unexpected exception while trying to fulfill the request.</p>
            capo_elastic_transcoder.errors.resource_in_use_exception.ResourceInUseException: <p>The resource you are attempting to change is in use. For example, you are attempting to delete a pipeline that is currently in use.</p>
            capo_elastic_transcoder.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource does not exist or is not available. For example, the pipeline to which you're trying to add a job doesn't exist or is still being created.</p>
            capo_elastic_transcoder.errors.validation_exception.ValidationException: <p>One or more required parameter values were not provided in the request.</p>
            capo_elastic_transcoder.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_elastic_transcoder.types.delete_pipeline_request.DeletePipelineRequest]",
        ) -> OperationResponse[
            "capo_elastic_transcoder.types.delete_pipeline_response.DeletePipelineResponse"
        ]:
            import capo_elastic_transcoder._operations.ets_customer_service.delete_pipeline

            output, http_response = (
                capo_elastic_transcoder._operations.ets_customer_service.delete_pipeline.delete_pipeline(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elastic_transcoder.types.delete_pipeline_request.DeletePipelineRequest = {
            "id": id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_preset(
        self,
        id: "capo_elastic_transcoder.types.id.Id",
        *,
        config_overrides: Optional[ElasticTranscoderClientConfig] = None,
    ) -> "capo_elastic_transcoder.types.delete_preset_response.DeletePresetResponse":
        """<p>The DeletePreset operation removes a preset that you've added in an AWS region.</p> <note> <p>You can't delete the default presets that are included with Elastic Transcoder.</p> </note>

        Args:
            id: <p>The identifier of the preset for which you want to get detailed information.</p>

        Raises:
            capo_elastic_transcoder.errors.access_denied_exception.AccessDeniedException: <p>General authentication failure. The request was not signed correctly.</p>
            capo_elastic_transcoder.errors.incompatible_version_exception.IncompatibleVersionException
            capo_elastic_transcoder.errors.internal_service_exception.InternalServiceException: <p>Elastic Transcoder encountered an unexpected exception while trying to fulfill the request.</p>
            capo_elastic_transcoder.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource does not exist or is not available. For example, the pipeline to which you're trying to add a job doesn't exist or is still being created.</p>
            capo_elastic_transcoder.errors.validation_exception.ValidationException: <p>One or more required parameter values were not provided in the request.</p>
            capo_elastic_transcoder.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_elastic_transcoder.types.delete_preset_request.DeletePresetRequest]",
        ) -> OperationResponse[
            "capo_elastic_transcoder.types.delete_preset_response.DeletePresetResponse"
        ]:
            import capo_elastic_transcoder._operations.ets_customer_service.delete_preset

            output, http_response = (
                capo_elastic_transcoder._operations.ets_customer_service.delete_preset.delete_preset(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elastic_transcoder.types.delete_preset_request.DeletePresetRequest = {
            "id": id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_jobs_by_pipeline(
        self,
        pipeline_id: "capo_elastic_transcoder.types.id.Id",
        *,
        config_overrides: Optional[ElasticTranscoderClientConfig] = None,
        ascending: Optional["capo_elastic_transcoder.types.ascending.Ascending"] = None,
        page_token: Optional["capo_elastic_transcoder.types.id.Id"] = None,
    ) -> "capo_elastic_transcoder.types.list_jobs_by_pipeline_response.ListJobsByPipelineResponse":
        """<p>The ListJobsByPipeline operation gets a list of the jobs currently in a pipeline.</p> <p>Elastic Transcoder returns all of the jobs currently in the specified pipeline. The response body contains one element for each job that satisfies the search criteria.</p>

        Args:
            pipeline_id: <p>The ID of the pipeline for which you want to get job information.</p>
            ascending: <p> To list jobs in chronological order by the date and time that they were submitted, enter <code>true</code>. To list jobs in reverse chronological order, enter <code>false</code>. </p>
            page_token: <p> When Elastic Transcoder returns more than one page of results, use <code>pageToken</code> in subsequent <code>GET</code> requests to get each successive page of results. </p>

        Raises:
            capo_elastic_transcoder.errors.access_denied_exception.AccessDeniedException: <p>General authentication failure. The request was not signed correctly.</p>
            capo_elastic_transcoder.errors.incompatible_version_exception.IncompatibleVersionException
            capo_elastic_transcoder.errors.internal_service_exception.InternalServiceException: <p>Elastic Transcoder encountered an unexpected exception while trying to fulfill the request.</p>
            capo_elastic_transcoder.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource does not exist or is not available. For example, the pipeline to which you're trying to add a job doesn't exist or is still being created.</p>
            capo_elastic_transcoder.errors.validation_exception.ValidationException: <p>One or more required parameter values were not provided in the request.</p>
            capo_elastic_transcoder.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_elastic_transcoder.types.list_jobs_by_pipeline_request.ListJobsByPipelineRequest]",
        ) -> OperationResponse[
            "capo_elastic_transcoder.types.list_jobs_by_pipeline_response.ListJobsByPipelineResponse"
        ]:
            import capo_elastic_transcoder._operations.ets_customer_service.list_jobs_by_pipeline

            output, http_response = (
                capo_elastic_transcoder._operations.ets_customer_service.list_jobs_by_pipeline.list_jobs_by_pipeline(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elastic_transcoder.types.list_jobs_by_pipeline_request.ListJobsByPipelineRequest = {
            "pipeline_id": pipeline_id
        }
        if ascending is not None:
            input_["ascending"] = ascending
        if page_token is not None:
            input_["page_token"] = page_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_jobs_by_pipeline(
        self,
        pipeline_id: "capo_elastic_transcoder.types.id.Id",
        *,
        config_overrides: Optional[ElasticTranscoderClientConfig] = None,
        ascending: Optional["capo_elastic_transcoder.types.ascending.Ascending"] = None,
        page_token: Optional["capo_elastic_transcoder.types.id.Id"] = None,
    ) -> "Iterator[capo_elastic_transcoder.types.job.Job]":
        _token = page_token
        while True:
            _response = self.list_jobs_by_pipeline(
                pipeline_id,
                config_overrides=config_overrides,
                ascending=ascending,
                page_token=_token,
            )
            _page = _resolve_path(_response, ("jobs",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_page_token",))
            if not _token:
                break

    def list_jobs_by_status(
        self,
        status: "capo_elastic_transcoder.types.job_status.JobStatus",
        *,
        config_overrides: Optional[ElasticTranscoderClientConfig] = None,
        ascending: Optional["capo_elastic_transcoder.types.ascending.Ascending"] = None,
        page_token: Optional["capo_elastic_transcoder.types.id.Id"] = None,
    ) -> "capo_elastic_transcoder.types.list_jobs_by_status_response.ListJobsByStatusResponse":
        """<p>The ListJobsByStatus operation gets a list of jobs that have a specified status. The response body contains one element for each job that satisfies the search criteria.</p>

        Args:
            status: <p>To get information about all of the jobs associated with the current AWS account that have a given status, specify the following status: <code>Submitted</code>, <code>Progressing</code>, <code>Complete</code>, <code>Canceled</code>, or <code>Error</code>.</p>
            ascending: <p> To list jobs in chronological order by the date and time that they were submitted, enter <code>true</code>. To list jobs in reverse chronological order, enter <code>false</code>. </p>
            page_token: <p> When Elastic Transcoder returns more than one page of results, use <code>pageToken</code> in subsequent <code>GET</code> requests to get each successive page of results. </p>

        Raises:
            capo_elastic_transcoder.errors.access_denied_exception.AccessDeniedException: <p>General authentication failure. The request was not signed correctly.</p>
            capo_elastic_transcoder.errors.incompatible_version_exception.IncompatibleVersionException
            capo_elastic_transcoder.errors.internal_service_exception.InternalServiceException: <p>Elastic Transcoder encountered an unexpected exception while trying to fulfill the request.</p>
            capo_elastic_transcoder.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource does not exist or is not available. For example, the pipeline to which you're trying to add a job doesn't exist or is still being created.</p>
            capo_elastic_transcoder.errors.validation_exception.ValidationException: <p>One or more required parameter values were not provided in the request.</p>
            capo_elastic_transcoder.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_elastic_transcoder.types.list_jobs_by_status_request.ListJobsByStatusRequest]",
        ) -> OperationResponse[
            "capo_elastic_transcoder.types.list_jobs_by_status_response.ListJobsByStatusResponse"
        ]:
            import capo_elastic_transcoder._operations.ets_customer_service.list_jobs_by_status

            output, http_response = (
                capo_elastic_transcoder._operations.ets_customer_service.list_jobs_by_status.list_jobs_by_status(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elastic_transcoder.types.list_jobs_by_status_request.ListJobsByStatusRequest = {
            "status": status
        }
        if ascending is not None:
            input_["ascending"] = ascending
        if page_token is not None:
            input_["page_token"] = page_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_jobs_by_status(
        self,
        status: "capo_elastic_transcoder.types.job_status.JobStatus",
        *,
        config_overrides: Optional[ElasticTranscoderClientConfig] = None,
        ascending: Optional["capo_elastic_transcoder.types.ascending.Ascending"] = None,
        page_token: Optional["capo_elastic_transcoder.types.id.Id"] = None,
    ) -> "Iterator[capo_elastic_transcoder.types.job.Job]":
        _token = page_token
        while True:
            _response = self.list_jobs_by_status(
                status,
                config_overrides=config_overrides,
                ascending=ascending,
                page_token=_token,
            )
            _page = _resolve_path(_response, ("jobs",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_page_token",))
            if not _token:
                break

    def list_pipelines(
        self,
        *,
        config_overrides: Optional[ElasticTranscoderClientConfig] = None,
        ascending: Optional["capo_elastic_transcoder.types.ascending.Ascending"] = None,
        page_token: Optional["capo_elastic_transcoder.types.id.Id"] = None,
    ) -> "capo_elastic_transcoder.types.list_pipelines_response.ListPipelinesResponse":
        """<p>The ListPipelines operation gets a list of the pipelines associated with the current AWS account.</p>

        Args:
            ascending: <p>To list pipelines in chronological order by the date and time that they were created, enter <code>true</code>. To list pipelines in reverse chronological order, enter <code>false</code>.</p>
            page_token: <p>When Elastic Transcoder returns more than one page of results, use <code>pageToken</code> in subsequent <code>GET</code> requests to get each successive page of results. </p>

        Raises:
            capo_elastic_transcoder.errors.access_denied_exception.AccessDeniedException: <p>General authentication failure. The request was not signed correctly.</p>
            capo_elastic_transcoder.errors.incompatible_version_exception.IncompatibleVersionException
            capo_elastic_transcoder.errors.internal_service_exception.InternalServiceException: <p>Elastic Transcoder encountered an unexpected exception while trying to fulfill the request.</p>
            capo_elastic_transcoder.errors.validation_exception.ValidationException: <p>One or more required parameter values were not provided in the request.</p>
            capo_elastic_transcoder.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_elastic_transcoder.types.list_pipelines_request.ListPipelinesRequest]",
        ) -> OperationResponse[
            "capo_elastic_transcoder.types.list_pipelines_response.ListPipelinesResponse"
        ]:
            import capo_elastic_transcoder._operations.ets_customer_service.list_pipelines

            output, http_response = (
                capo_elastic_transcoder._operations.ets_customer_service.list_pipelines.list_pipelines(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elastic_transcoder.types.list_pipelines_request.ListPipelinesRequest = {}
        if ascending is not None:
            input_["ascending"] = ascending
        if page_token is not None:
            input_["page_token"] = page_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_pipelines(
        self,
        *,
        config_overrides: Optional[ElasticTranscoderClientConfig] = None,
        ascending: Optional["capo_elastic_transcoder.types.ascending.Ascending"] = None,
        page_token: Optional["capo_elastic_transcoder.types.id.Id"] = None,
    ) -> "Iterator[capo_elastic_transcoder.types.pipeline.Pipeline]":
        _token = page_token
        while True:
            _response = self.list_pipelines(
                config_overrides=config_overrides,
                ascending=ascending,
                page_token=_token,
            )
            _page = _resolve_path(_response, ("pipelines",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_page_token",))
            if not _token:
                break

    def list_presets(
        self,
        *,
        config_overrides: Optional[ElasticTranscoderClientConfig] = None,
        ascending: Optional["capo_elastic_transcoder.types.ascending.Ascending"] = None,
        page_token: Optional["capo_elastic_transcoder.types.id.Id"] = None,
    ) -> "capo_elastic_transcoder.types.list_presets_response.ListPresetsResponse":
        """<p>The ListPresets operation gets a list of the default presets included with Elastic Transcoder and the presets that you've added in an AWS region.</p>

        Args:
            ascending: <p>To list presets in chronological order by the date and time that they were created, enter <code>true</code>. To list presets in reverse chronological order, enter <code>false</code>.</p>
            page_token: <p>When Elastic Transcoder returns more than one page of results, use <code>pageToken</code> in subsequent <code>GET</code> requests to get each successive page of results. </p>

        Raises:
            capo_elastic_transcoder.errors.access_denied_exception.AccessDeniedException: <p>General authentication failure. The request was not signed correctly.</p>
            capo_elastic_transcoder.errors.incompatible_version_exception.IncompatibleVersionException
            capo_elastic_transcoder.errors.internal_service_exception.InternalServiceException: <p>Elastic Transcoder encountered an unexpected exception while trying to fulfill the request.</p>
            capo_elastic_transcoder.errors.validation_exception.ValidationException: <p>One or more required parameter values were not provided in the request.</p>
            capo_elastic_transcoder.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_elastic_transcoder.types.list_presets_request.ListPresetsRequest]",
        ) -> OperationResponse[
            "capo_elastic_transcoder.types.list_presets_response.ListPresetsResponse"
        ]:
            import capo_elastic_transcoder._operations.ets_customer_service.list_presets

            output, http_response = (
                capo_elastic_transcoder._operations.ets_customer_service.list_presets.list_presets(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elastic_transcoder.types.list_presets_request.ListPresetsRequest = {}
        if ascending is not None:
            input_["ascending"] = ascending
        if page_token is not None:
            input_["page_token"] = page_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_presets(
        self,
        *,
        config_overrides: Optional[ElasticTranscoderClientConfig] = None,
        ascending: Optional["capo_elastic_transcoder.types.ascending.Ascending"] = None,
        page_token: Optional["capo_elastic_transcoder.types.id.Id"] = None,
    ) -> "Iterator[capo_elastic_transcoder.types.preset.Preset]":
        _token = page_token
        while True:
            _response = self.list_presets(
                config_overrides=config_overrides,
                ascending=ascending,
                page_token=_token,
            )
            _page = _resolve_path(_response, ("presets",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_page_token",))
            if not _token:
                break

    def read_job(
        self,
        id: "capo_elastic_transcoder.types.id.Id",
        *,
        config_overrides: Optional[ElasticTranscoderClientConfig] = None,
    ) -> "capo_elastic_transcoder.types.read_job_response.ReadJobResponse":
        """<p>The ReadJob operation returns detailed information about a job.</p>

        Args:
            id: <p>The identifier of the job for which you want to get detailed information.</p>

        Raises:
            capo_elastic_transcoder.errors.access_denied_exception.AccessDeniedException: <p>General authentication failure. The request was not signed correctly.</p>
            capo_elastic_transcoder.errors.incompatible_version_exception.IncompatibleVersionException
            capo_elastic_transcoder.errors.internal_service_exception.InternalServiceException: <p>Elastic Transcoder encountered an unexpected exception while trying to fulfill the request.</p>
            capo_elastic_transcoder.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource does not exist or is not available. For example, the pipeline to which you're trying to add a job doesn't exist or is still being created.</p>
            capo_elastic_transcoder.errors.validation_exception.ValidationException: <p>One or more required parameter values were not provided in the request.</p>
            capo_elastic_transcoder.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_elastic_transcoder.types.read_job_request.ReadJobRequest]",
        ) -> OperationResponse[
            "capo_elastic_transcoder.types.read_job_response.ReadJobResponse"
        ]:
            import capo_elastic_transcoder._operations.ets_customer_service.read_job

            output, http_response = (
                capo_elastic_transcoder._operations.ets_customer_service.read_job.read_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elastic_transcoder.types.read_job_request.ReadJobRequest = {
            "id": id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def read_pipeline(
        self,
        id: "capo_elastic_transcoder.types.id.Id",
        *,
        config_overrides: Optional[ElasticTranscoderClientConfig] = None,
    ) -> "capo_elastic_transcoder.types.read_pipeline_response.ReadPipelineResponse":
        """<p>The ReadPipeline operation gets detailed information about a pipeline.</p>

        Args:
            id: <p>The identifier of the pipeline to read.</p>

        Raises:
            capo_elastic_transcoder.errors.access_denied_exception.AccessDeniedException: <p>General authentication failure. The request was not signed correctly.</p>
            capo_elastic_transcoder.errors.incompatible_version_exception.IncompatibleVersionException
            capo_elastic_transcoder.errors.internal_service_exception.InternalServiceException: <p>Elastic Transcoder encountered an unexpected exception while trying to fulfill the request.</p>
            capo_elastic_transcoder.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource does not exist or is not available. For example, the pipeline to which you're trying to add a job doesn't exist or is still being created.</p>
            capo_elastic_transcoder.errors.validation_exception.ValidationException: <p>One or more required parameter values were not provided in the request.</p>
            capo_elastic_transcoder.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_elastic_transcoder.types.read_pipeline_request.ReadPipelineRequest]",
        ) -> OperationResponse[
            "capo_elastic_transcoder.types.read_pipeline_response.ReadPipelineResponse"
        ]:
            import capo_elastic_transcoder._operations.ets_customer_service.read_pipeline

            output, http_response = (
                capo_elastic_transcoder._operations.ets_customer_service.read_pipeline.read_pipeline(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elastic_transcoder.types.read_pipeline_request.ReadPipelineRequest = {
            "id": id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def read_preset(
        self,
        id: "capo_elastic_transcoder.types.id.Id",
        *,
        config_overrides: Optional[ElasticTranscoderClientConfig] = None,
    ) -> "capo_elastic_transcoder.types.read_preset_response.ReadPresetResponse":
        """<p>The ReadPreset operation gets detailed information about a preset.</p>

        Args:
            id: <p>The identifier of the preset for which you want to get detailed information.</p>

        Raises:
            capo_elastic_transcoder.errors.access_denied_exception.AccessDeniedException: <p>General authentication failure. The request was not signed correctly.</p>
            capo_elastic_transcoder.errors.incompatible_version_exception.IncompatibleVersionException
            capo_elastic_transcoder.errors.internal_service_exception.InternalServiceException: <p>Elastic Transcoder encountered an unexpected exception while trying to fulfill the request.</p>
            capo_elastic_transcoder.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource does not exist or is not available. For example, the pipeline to which you're trying to add a job doesn't exist or is still being created.</p>
            capo_elastic_transcoder.errors.validation_exception.ValidationException: <p>One or more required parameter values were not provided in the request.</p>
            capo_elastic_transcoder.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_elastic_transcoder.types.read_preset_request.ReadPresetRequest]",
        ) -> OperationResponse[
            "capo_elastic_transcoder.types.read_preset_response.ReadPresetResponse"
        ]:
            import capo_elastic_transcoder._operations.ets_customer_service.read_preset

            output, http_response = (
                capo_elastic_transcoder._operations.ets_customer_service.read_preset.read_preset(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elastic_transcoder.types.read_preset_request.ReadPresetRequest = {
            "id": id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def test_role(
        self,
        role: "capo_elastic_transcoder.types.role.Role",
        input_bucket: "capo_elastic_transcoder.types.bucket_name.BucketName",
        output_bucket: "capo_elastic_transcoder.types.bucket_name.BucketName",
        topics: "capo_elastic_transcoder.types.sns_topics.SnsTopics",
        *,
        config_overrides: Optional[ElasticTranscoderClientConfig] = None,
    ) -> "capo_elastic_transcoder.types.test_role_response.TestRoleResponse":
        """<p>The TestRole operation tests the IAM role used to create the pipeline.</p> <p>The <code>TestRole</code> action lets you determine whether the IAM role you are using has sufficient permissions to let Elastic Transcoder perform tasks associated with the transcoding process. The action attempts to assume the specified IAM role, checks read access to the input and output buckets, and tries to send a test notification to Amazon SNS topics that you specify.</p>

        Args:
            role: <p>The IAM Amazon Resource Name (ARN) for the role that you want Elastic Transcoder to test.</p>
            input_bucket: <p>The Amazon S3 bucket that contains media files to be transcoded. The action attempts to read from this bucket.</p>
            output_bucket: <p>The Amazon S3 bucket that Elastic Transcoder writes transcoded media files to. The action attempts to read from this bucket.</p>
            topics: <p>The ARNs of one or more Amazon Simple Notification Service (Amazon SNS) topics that you want the action to send a test notification to.</p>

        Raises:
            capo_elastic_transcoder.errors.access_denied_exception.AccessDeniedException: <p>General authentication failure. The request was not signed correctly.</p>
            capo_elastic_transcoder.errors.incompatible_version_exception.IncompatibleVersionException
            capo_elastic_transcoder.errors.internal_service_exception.InternalServiceException: <p>Elastic Transcoder encountered an unexpected exception while trying to fulfill the request.</p>
            capo_elastic_transcoder.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource does not exist or is not available. For example, the pipeline to which you're trying to add a job doesn't exist or is still being created.</p>
            capo_elastic_transcoder.errors.validation_exception.ValidationException: <p>One or more required parameter values were not provided in the request.</p>
            capo_elastic_transcoder.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_elastic_transcoder.types.test_role_request.TestRoleRequest]",
        ) -> OperationResponse[
            "capo_elastic_transcoder.types.test_role_response.TestRoleResponse"
        ]:
            import capo_elastic_transcoder._operations.ets_customer_service.test_role

            output, http_response = (
                capo_elastic_transcoder._operations.ets_customer_service.test_role.test_role(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elastic_transcoder.types.test_role_request.TestRoleRequest = {
            "role": role,
            "input_bucket": input_bucket,
            "output_bucket": output_bucket,
            "topics": topics,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_pipeline(
        self,
        id: "capo_elastic_transcoder.types.id.Id",
        *,
        config_overrides: Optional[ElasticTranscoderClientConfig] = None,
        name: Optional["capo_elastic_transcoder.types.name.Name"] = None,
        input_bucket: Optional[
            "capo_elastic_transcoder.types.bucket_name.BucketName"
        ] = None,
        role: Optional["capo_elastic_transcoder.types.role.Role"] = None,
        aws_kms_key_arn: Optional[
            "capo_elastic_transcoder.types.key_arn.KeyArn"
        ] = None,
        notifications: Optional[
            "capo_elastic_transcoder.types.notifications.Notifications"
        ] = None,
        content_config: Optional[
            "capo_elastic_transcoder.types.pipeline_output_config.PipelineOutputConfig"
        ] = None,
        thumbnail_config: Optional[
            "capo_elastic_transcoder.types.pipeline_output_config.PipelineOutputConfig"
        ] = None,
    ) -> (
        "capo_elastic_transcoder.types.update_pipeline_response.UpdatePipelineResponse"
    ):
        """<p> Use the <code>UpdatePipeline</code> operation to update settings for a pipeline.</p> <important> <p>When you change pipeline settings, your changes take effect immediately. Jobs that you have already submitted and that Elastic Transcoder has not started to process are affected in addition to jobs that you submit after you change settings. </p> </important>

        Args:
            id: <p>The ID of the pipeline that you want to update.</p>
            name: <p>The name of the pipeline. We recommend that the name be unique within the AWS account, but uniqueness is not enforced.</p> <p>Constraints: Maximum 40 characters</p>
            input_bucket: <p>The Amazon S3 bucket in which you saved the media files that you want to transcode and the graphics that you want to use as watermarks.</p>
            role: <p>The IAM Amazon Resource Name (ARN) for the role that you want Elastic Transcoder to use to transcode jobs for this pipeline.</p>
            aws_kms_key_arn: <p>The AWS Key Management Service (AWS KMS) key that you want to use with this pipeline.</p> <p>If you use either <code>s3</code> or <code>s3-aws-kms</code> as your <code>Encryption:Mode</code>, you don't need to provide a key with your job because a default key, known as an AWS-KMS key, is created for you automatically. You need to provide an AWS-KMS key only if you want to use a non-default AWS-KMS key, or if you are using an <code>Encryption:Mode</code> of <code>aes-cbc-pkcs7</code>, <code>aes-ctr</code>, or <code>aes-gcm</code>.</p>
            notifications: <p>The topic ARN for the Amazon Simple Notification Service (Amazon SNS) topic that you want to notify to report job status.</p> <important> <p>To receive notifications, you must also subscribe to the new topic in the Amazon SNS console.</p> </important> <ul> <li> <p> <b>Progressing</b>: The topic ARN for the Amazon Simple Notification Service (Amazon SNS) topic that you want to notify when Elastic Transcoder has started to process jobs that are added to this pipeline. This is the ARN that Amazon SNS returned when you created the topic.</p> </li> <li> <p> <b>Complete</b>: The topic ARN for the Amazon SNS topic that you want to notify when Elastic Transcoder has finished processing a job. This is the ARN that Amazon SNS returned when you created the topic.</p> </li> <li> <p> <b>Warning</b>: The topic ARN for the Amazon SNS topic that you want to notify when Elastic Transcoder encounters a warning condition. This is the ARN that Amazon SNS returned when you created the topic.</p> </li> <li> <p> <b>Error</b>: The topic ARN for the Amazon SNS topic that you want to notify when Elastic Transcoder encounters an error condition. This is the ARN that Amazon SNS returned when you created the topic.</p> </li> </ul>
            content_config: <p>The optional <code>ContentConfig</code> object specifies information about the Amazon S3 bucket in which you want Elastic Transcoder to save transcoded files and playlists: which bucket to use, which users you want to have access to the files, the type of access you want users to have, and the storage class that you want to assign to the files.</p> <p>If you specify values for <code>ContentConfig</code>, you must also specify values for <code>ThumbnailConfig</code>.</p> <p>If you specify values for <code>ContentConfig</code> and <code>ThumbnailConfig</code>, omit the <code>OutputBucket</code> object.</p> <ul> <li> <p> <b>Bucket</b>: The Amazon S3 bucket in which you want Elastic Transcoder to save transcoded files and playlists.</p> </li> <li> <p> <b>Permissions</b> (Optional): The Permissions object specifies which users you want to have access to transcoded files and the type of access you want them to have. You can grant permissions to a maximum of 30 users and/or predefined Amazon S3 groups.</p> </li> <li> <p> <b>Grantee Type</b>: Specify the type of value that appears in the <code>Grantee</code> object:</p> <ul> <li> <p> <b>Canonical</b>: The value in the <code>Grantee</code> object is either the canonical user ID for an AWS account or an origin access identity for an Amazon CloudFront distribution. For more information about canonical user IDs, see Access Control List (ACL) Overview in the Amazon Simple Storage Service Developer Guide. For more information about using CloudFront origin access identities to require that users use CloudFront URLs instead of Amazon S3 URLs, see Using an Origin Access Identity to Restrict Access to Your Amazon S3 Content.</p> <important> <p>A canonical user ID is not the same as an AWS account number.</p> </important> </li> <li> <p> <b>Email</b>: The value in the <code>Grantee</code> object is the registered email address of an AWS account.</p> </li> <li> <p> <b>Group</b>: The value in the <code>Grantee</code> object is one of the following predefined Amazon S3 groups: <code>AllUsers</code>, <code>AuthenticatedUsers</code>, or <code>LogDelivery</code>.</p> </li> </ul> </li> <li> <p> <b>Grantee</b>: The AWS user or group that you want to have access to transcoded files and playlists. To identify the user or group, you can specify the canonical user ID for an AWS account, an origin access identity for a CloudFront distribution, the registered email address of an AWS account, or a predefined Amazon S3 group </p> </li> <li> <p> <b>Access</b>: The permission that you want to give to the AWS user that you specified in <code>Grantee</code>. Permissions are granted on the files that Elastic Transcoder adds to the bucket, including playlists and video files. Valid values include: </p> <ul> <li> <p> <code>READ</code>: The grantee can read the objects and metadata for objects that Elastic Transcoder adds to the Amazon S3 bucket.</p> </li> <li> <p> <code>READ_ACP</code>: The grantee can read the object ACL for objects that Elastic Transcoder adds to the Amazon S3 bucket. </p> </li> <li> <p> <code>WRITE_ACP</code>: The grantee can write the ACL for the objects that Elastic Transcoder adds to the Amazon S3 bucket.</p> </li> <li> <p> <code>FULL_CONTROL</code>: The grantee has <code>READ</code>, <code>READ_ACP</code>, and <code>WRITE_ACP</code> permissions for the objects that Elastic Transcoder adds to the Amazon S3 bucket.</p> </li> </ul> </li> <li> <p> <b>StorageClass</b>: The Amazon S3 storage class, <code>Standard</code> or <code>ReducedRedundancy</code>, that you want Elastic Transcoder to assign to the video files and playlists that it stores in your Amazon S3 bucket.</p> </li> </ul>
            thumbnail_config: <p>The <code>ThumbnailConfig</code> object specifies several values, including the Amazon S3 bucket in which you want Elastic Transcoder to save thumbnail files, which users you want to have access to the files, the type of access you want users to have, and the storage class that you want to assign to the files.</p> <p>If you specify values for <code>ContentConfig</code>, you must also specify values for <code>ThumbnailConfig</code> even if you don't want to create thumbnails.</p> <p>If you specify values for <code>ContentConfig</code> and <code>ThumbnailConfig</code>, omit the <code>OutputBucket</code> object.</p> <ul> <li> <p> <b>Bucket</b>: The Amazon S3 bucket in which you want Elastic Transcoder to save thumbnail files.</p> </li> <li> <p> <b>Permissions</b> (Optional): The <code>Permissions</code> object specifies which users and/or predefined Amazon S3 groups you want to have access to thumbnail files, and the type of access you want them to have. You can grant permissions to a maximum of 30 users and/or predefined Amazon S3 groups.</p> </li> <li> <p> <b>GranteeType</b>: Specify the type of value that appears in the Grantee object:</p> <ul> <li> <p> <b>Canonical</b>: The value in the <code>Grantee</code> object is either the canonical user ID for an AWS account or an origin access identity for an Amazon CloudFront distribution.</p> <important> <p>A canonical user ID is not the same as an AWS account number.</p> </important> </li> <li> <p> <b>Email</b>: The value in the <code>Grantee</code> object is the registered email address of an AWS account.</p> </li> <li> <p> <b>Group</b>: The value in the <code>Grantee</code> object is one of the following predefined Amazon S3 groups: <code>AllUsers</code>, <code>AuthenticatedUsers</code>, or <code>LogDelivery</code>.</p> </li> </ul> </li> <li> <p> <b>Grantee</b>: The AWS user or group that you want to have access to thumbnail files. To identify the user or group, you can specify the canonical user ID for an AWS account, an origin access identity for a CloudFront distribution, the registered email address of an AWS account, or a predefined Amazon S3 group. </p> </li> <li> <p> <b>Access</b>: The permission that you want to give to the AWS user that you specified in <code>Grantee</code>. Permissions are granted on the thumbnail files that Elastic Transcoder adds to the bucket. Valid values include: </p> <ul> <li> <p> <code>READ</code>: The grantee can read the thumbnails and metadata for objects that Elastic Transcoder adds to the Amazon S3 bucket.</p> </li> <li> <p> <code>READ_ACP</code>: The grantee can read the object ACL for thumbnails that Elastic Transcoder adds to the Amazon S3 bucket.</p> </li> <li> <p> <code>WRITE_ACP</code>: The grantee can write the ACL for the thumbnails that Elastic Transcoder adds to the Amazon S3 bucket.</p> </li> <li> <p> <code>FULL_CONTROL</code>: The grantee has <code>READ</code>, <code>READ_ACP</code>, and <code>WRITE_ACP</code> permissions for the thumbnails that Elastic Transcoder adds to the Amazon S3 bucket. </p> </li> </ul> </li> <li> <p> <b>StorageClass</b>: The Amazon S3 storage class, <code>Standard</code> or <code>ReducedRedundancy</code>, that you want Elastic Transcoder to assign to the thumbnails that it stores in your Amazon S3 bucket.</p> </li> </ul>

        Raises:
            capo_elastic_transcoder.errors.access_denied_exception.AccessDeniedException: <p>General authentication failure. The request was not signed correctly.</p>
            capo_elastic_transcoder.errors.incompatible_version_exception.IncompatibleVersionException
            capo_elastic_transcoder.errors.internal_service_exception.InternalServiceException: <p>Elastic Transcoder encountered an unexpected exception while trying to fulfill the request.</p>
            capo_elastic_transcoder.errors.resource_in_use_exception.ResourceInUseException: <p>The resource you are attempting to change is in use. For example, you are attempting to delete a pipeline that is currently in use.</p>
            capo_elastic_transcoder.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource does not exist or is not available. For example, the pipeline to which you're trying to add a job doesn't exist or is still being created.</p>
            capo_elastic_transcoder.errors.validation_exception.ValidationException: <p>One or more required parameter values were not provided in the request.</p>
            capo_elastic_transcoder.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_elastic_transcoder.types.update_pipeline_request.UpdatePipelineRequest]",
        ) -> OperationResponse[
            "capo_elastic_transcoder.types.update_pipeline_response.UpdatePipelineResponse"
        ]:
            import capo_elastic_transcoder._operations.ets_customer_service.update_pipeline

            output, http_response = (
                capo_elastic_transcoder._operations.ets_customer_service.update_pipeline.update_pipeline(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elastic_transcoder.types.update_pipeline_request.UpdatePipelineRequest = {
            "id": id
        }
        if name is not None:
            input_["name"] = name
        if input_bucket is not None:
            input_["input_bucket"] = input_bucket
        if role is not None:
            input_["role"] = role
        if aws_kms_key_arn is not None:
            input_["aws_kms_key_arn"] = aws_kms_key_arn
        if notifications is not None:
            input_["notifications"] = notifications
        if content_config is not None:
            input_["content_config"] = content_config
        if thumbnail_config is not None:
            input_["thumbnail_config"] = thumbnail_config

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_pipeline_notifications(
        self,
        id: "capo_elastic_transcoder.types.id.Id",
        notifications: "capo_elastic_transcoder.types.notifications.Notifications",
        *,
        config_overrides: Optional[ElasticTranscoderClientConfig] = None,
    ) -> "capo_elastic_transcoder.types.update_pipeline_notifications_response.UpdatePipelineNotificationsResponse":
        """<p>With the UpdatePipelineNotifications operation, you can update Amazon Simple Notification Service (Amazon SNS) notifications for a pipeline.</p> <p>When you update notifications for a pipeline, Elastic Transcoder returns the values that you specified in the request.</p>

        Args:
            id: <p>The identifier of the pipeline for which you want to change notification settings.</p>
            notifications: <p>The topic ARN for the Amazon Simple Notification Service (Amazon SNS) topic that you want to notify to report job status.</p> <important> <p>To receive notifications, you must also subscribe to the new topic in the Amazon SNS console.</p> </important> <ul> <li> <p> <b>Progressing</b>: The topic ARN for the Amazon Simple Notification Service (Amazon SNS) topic that you want to notify when Elastic Transcoder has started to process jobs that are added to this pipeline. This is the ARN that Amazon SNS returned when you created the topic.</p> </li> <li> <p> <b>Complete</b>: The topic ARN for the Amazon SNS topic that you want to notify when Elastic Transcoder has finished processing a job. This is the ARN that Amazon SNS returned when you created the topic.</p> </li> <li> <p> <b>Warning</b>: The topic ARN for the Amazon SNS topic that you want to notify when Elastic Transcoder encounters a warning condition. This is the ARN that Amazon SNS returned when you created the topic.</p> </li> <li> <p> <b>Error</b>: The topic ARN for the Amazon SNS topic that you want to notify when Elastic Transcoder encounters an error condition. This is the ARN that Amazon SNS returned when you created the topic.</p> </li> </ul>

        Raises:
            capo_elastic_transcoder.errors.access_denied_exception.AccessDeniedException: <p>General authentication failure. The request was not signed correctly.</p>
            capo_elastic_transcoder.errors.incompatible_version_exception.IncompatibleVersionException
            capo_elastic_transcoder.errors.internal_service_exception.InternalServiceException: <p>Elastic Transcoder encountered an unexpected exception while trying to fulfill the request.</p>
            capo_elastic_transcoder.errors.resource_in_use_exception.ResourceInUseException: <p>The resource you are attempting to change is in use. For example, you are attempting to delete a pipeline that is currently in use.</p>
            capo_elastic_transcoder.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource does not exist or is not available. For example, the pipeline to which you're trying to add a job doesn't exist or is still being created.</p>
            capo_elastic_transcoder.errors.validation_exception.ValidationException: <p>One or more required parameter values were not provided in the request.</p>
            capo_elastic_transcoder.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_elastic_transcoder.types.update_pipeline_notifications_request.UpdatePipelineNotificationsRequest]",
        ) -> OperationResponse[
            "capo_elastic_transcoder.types.update_pipeline_notifications_response.UpdatePipelineNotificationsResponse"
        ]:
            import capo_elastic_transcoder._operations.ets_customer_service.update_pipeline_notifications

            output, http_response = (
                capo_elastic_transcoder._operations.ets_customer_service.update_pipeline_notifications.update_pipeline_notifications(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elastic_transcoder.types.update_pipeline_notifications_request.UpdatePipelineNotificationsRequest = {
            "id": id,
            "notifications": notifications,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_pipeline_status(
        self,
        id: "capo_elastic_transcoder.types.id.Id",
        status: "capo_elastic_transcoder.types.pipeline_status.PipelineStatus",
        *,
        config_overrides: Optional[ElasticTranscoderClientConfig] = None,
    ) -> "capo_elastic_transcoder.types.update_pipeline_status_response.UpdatePipelineStatusResponse":
        """<p>The UpdatePipelineStatus operation pauses or reactivates a pipeline, so that the pipeline stops or restarts the processing of jobs.</p> <p>Changing the pipeline status is useful if you want to cancel one or more jobs. You can't cancel jobs after Elastic Transcoder has started processing them; if you pause the pipeline to which you submitted the jobs, you have more time to get the job IDs for the jobs that you want to cancel, and to send a <a>CancelJob</a> request. </p>

        Args:
            id: <p>The identifier of the pipeline to update.</p>
            status: <p>The desired status of the pipeline:</p> <ul> <li> <p> <code>Active</code>: The pipeline is processing jobs.</p> </li> <li> <p> <code>Paused</code>: The pipeline is not currently processing jobs.</p> </li> </ul>

        Raises:
            capo_elastic_transcoder.errors.access_denied_exception.AccessDeniedException: <p>General authentication failure. The request was not signed correctly.</p>
            capo_elastic_transcoder.errors.incompatible_version_exception.IncompatibleVersionException
            capo_elastic_transcoder.errors.internal_service_exception.InternalServiceException: <p>Elastic Transcoder encountered an unexpected exception while trying to fulfill the request.</p>
            capo_elastic_transcoder.errors.resource_in_use_exception.ResourceInUseException: <p>The resource you are attempting to change is in use. For example, you are attempting to delete a pipeline that is currently in use.</p>
            capo_elastic_transcoder.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource does not exist or is not available. For example, the pipeline to which you're trying to add a job doesn't exist or is still being created.</p>
            capo_elastic_transcoder.errors.validation_exception.ValidationException: <p>One or more required parameter values were not provided in the request.</p>
            capo_elastic_transcoder.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_elastic_transcoder.types.update_pipeline_status_request.UpdatePipelineStatusRequest]",
        ) -> OperationResponse[
            "capo_elastic_transcoder.types.update_pipeline_status_response.UpdatePipelineStatusResponse"
        ]:
            import capo_elastic_transcoder._operations.ets_customer_service.update_pipeline_status

            output, http_response = (
                capo_elastic_transcoder._operations.ets_customer_service.update_pipeline_status.update_pipeline_status(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elastic_transcoder.types.update_pipeline_status_request.UpdatePipelineStatusRequest = {
            "id": id,
            "status": status,
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
