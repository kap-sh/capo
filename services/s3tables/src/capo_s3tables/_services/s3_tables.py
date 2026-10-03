"""Generated from Smithy shape ``com.amazonaws.s3tables#S3TableBuckets``."""

import warnings
from collections.abc import Iterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import BaseHandler, Client

import capo_s3tables._auth._signers
import capo_s3tables._auth._sigv4
from capo_s3tables._auth._identity import Credentials
from capo_s3tables._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_s3tables._auth._zapros_handler import AuthMiddleware
from capo_s3tables._pagination import resolve_path as _resolve_path
from capo_s3tables._resources.s3_table_buckets.namespace_resource import (
    NamespaceResource,
)
from capo_s3tables._resources.s3_table_buckets.table_bucket_encryption_resource import (
    TableBucketEncryptionResource,
)
from capo_s3tables._resources.s3_table_buckets.table_bucket_policy_resource import (
    TableBucketPolicyResource,
)
from capo_s3tables._resources.s3_table_buckets.table_bucket_replication_resource import (
    TableBucketReplicationResource,
)
from capo_s3tables._resources.s3_table_buckets.table_bucket_resource import (
    TableBucketResource,
)
from capo_s3tables._resources.s3_table_buckets.table_encryption_resource import (
    TableEncryptionResource,
)
from capo_s3tables._resources.s3_table_buckets.table_policy_resource import (
    TablePolicyResource,
)
from capo_s3tables._resources.s3_table_buckets.table_replication_resource import (
    TableReplicationResource,
)
from capo_s3tables._resources.s3_table_buckets.table_resource import TableResource
from capo_s3tables._services._aws_config import aws_config
from capo_s3tables._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import capo_s3tables.types.create_namespace_request
    import capo_s3tables.types.create_namespace_response
    import capo_s3tables.types.create_table_bucket_request
    import capo_s3tables.types.create_table_bucket_response
    import capo_s3tables.types.create_table_request
    import capo_s3tables.types.create_table_response
    import capo_s3tables.types.delete_namespace_request
    import capo_s3tables.types.delete_table_bucket_encryption_request
    import capo_s3tables.types.delete_table_bucket_metrics_configuration_request
    import capo_s3tables.types.delete_table_bucket_policy_request
    import capo_s3tables.types.delete_table_bucket_replication_request
    import capo_s3tables.types.delete_table_bucket_request
    import capo_s3tables.types.delete_table_policy_request
    import capo_s3tables.types.delete_table_replication_request
    import capo_s3tables.types.delete_table_request
    import capo_s3tables.types.encryption_configuration
    import capo_s3tables.types.get_namespace_request
    import capo_s3tables.types.get_namespace_response
    import capo_s3tables.types.get_table_bucket_encryption_request
    import capo_s3tables.types.get_table_bucket_encryption_response
    import capo_s3tables.types.get_table_bucket_maintenance_configuration_request
    import capo_s3tables.types.get_table_bucket_maintenance_configuration_response
    import capo_s3tables.types.get_table_bucket_metrics_configuration_request
    import capo_s3tables.types.get_table_bucket_metrics_configuration_response
    import capo_s3tables.types.get_table_bucket_policy_request
    import capo_s3tables.types.get_table_bucket_policy_response
    import capo_s3tables.types.get_table_bucket_replication_request
    import capo_s3tables.types.get_table_bucket_replication_response
    import capo_s3tables.types.get_table_bucket_request
    import capo_s3tables.types.get_table_bucket_response
    import capo_s3tables.types.get_table_bucket_storage_class_request
    import capo_s3tables.types.get_table_bucket_storage_class_response
    import capo_s3tables.types.get_table_encryption_request
    import capo_s3tables.types.get_table_encryption_response
    import capo_s3tables.types.get_table_maintenance_configuration_request
    import capo_s3tables.types.get_table_maintenance_configuration_response
    import capo_s3tables.types.get_table_maintenance_job_status_request
    import capo_s3tables.types.get_table_maintenance_job_status_response
    import capo_s3tables.types.get_table_metadata_location_request
    import capo_s3tables.types.get_table_metadata_location_response
    import capo_s3tables.types.get_table_policy_request
    import capo_s3tables.types.get_table_policy_response
    import capo_s3tables.types.get_table_record_expiration_configuration_request
    import capo_s3tables.types.get_table_record_expiration_configuration_response
    import capo_s3tables.types.get_table_record_expiration_job_status_request
    import capo_s3tables.types.get_table_record_expiration_job_status_response
    import capo_s3tables.types.get_table_replication_request
    import capo_s3tables.types.get_table_replication_response
    import capo_s3tables.types.get_table_replication_status_request
    import capo_s3tables.types.get_table_replication_status_response
    import capo_s3tables.types.get_table_request
    import capo_s3tables.types.get_table_response
    import capo_s3tables.types.get_table_storage_class_request
    import capo_s3tables.types.get_table_storage_class_response
    import capo_s3tables.types.list_namespaces_limit
    import capo_s3tables.types.list_namespaces_request
    import capo_s3tables.types.list_namespaces_response
    import capo_s3tables.types.list_table_buckets_limit
    import capo_s3tables.types.list_table_buckets_request
    import capo_s3tables.types.list_table_buckets_response
    import capo_s3tables.types.list_tables_limit
    import capo_s3tables.types.list_tables_request
    import capo_s3tables.types.list_tables_response
    import capo_s3tables.types.list_tags_for_resource_request
    import capo_s3tables.types.list_tags_for_resource_response
    import capo_s3tables.types.metadata_location
    import capo_s3tables.types.namespace_list
    import capo_s3tables.types.namespace_name
    import capo_s3tables.types.namespace_summary
    import capo_s3tables.types.next_token
    import capo_s3tables.types.open_table_format
    import capo_s3tables.types.put_table_bucket_encryption_request
    import capo_s3tables.types.put_table_bucket_maintenance_configuration_request
    import capo_s3tables.types.put_table_bucket_metrics_configuration_request
    import capo_s3tables.types.put_table_bucket_policy_request
    import capo_s3tables.types.put_table_bucket_replication_request
    import capo_s3tables.types.put_table_bucket_replication_response
    import capo_s3tables.types.put_table_bucket_storage_class_request
    import capo_s3tables.types.put_table_maintenance_configuration_request
    import capo_s3tables.types.put_table_policy_request
    import capo_s3tables.types.put_table_record_expiration_configuration_request
    import capo_s3tables.types.put_table_replication_request
    import capo_s3tables.types.put_table_replication_response
    import capo_s3tables.types.rename_table_request
    import capo_s3tables.types.resource_arn
    import capo_s3tables.types.resource_policy
    import capo_s3tables.types.storage_class_configuration
    import capo_s3tables.types.table_arn
    import capo_s3tables.types.table_bucket_arn
    import capo_s3tables.types.table_bucket_maintenance_configuration_value
    import capo_s3tables.types.table_bucket_maintenance_type
    import capo_s3tables.types.table_bucket_name
    import capo_s3tables.types.table_bucket_replication_configuration
    import capo_s3tables.types.table_bucket_summary
    import capo_s3tables.types.table_bucket_type
    import capo_s3tables.types.table_maintenance_configuration_value
    import capo_s3tables.types.table_maintenance_type
    import capo_s3tables.types.table_metadata
    import capo_s3tables.types.table_name
    import capo_s3tables.types.table_record_expiration_configuration_value
    import capo_s3tables.types.table_replication_configuration
    import capo_s3tables.types.table_summary
    import capo_s3tables.types.tag_key_list
    import capo_s3tables.types.tag_resource_request
    import capo_s3tables.types.tag_resource_response
    import capo_s3tables.types.tags
    import capo_s3tables.types.untag_resource_request
    import capo_s3tables.types.untag_resource_response
    import capo_s3tables.types.update_table_metadata_location_request
    import capo_s3tables.types.update_table_metadata_location_response
    import capo_s3tables.types.version_token


class S3TablesClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class S3TablesClient:
    """A client for the ``S3Tables`` service.

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
        self._config = S3TablesClientConfig(
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
        self.namespace_resource = NamespaceResource(self)
        self.table_bucket_encryption_resource = TableBucketEncryptionResource(self)
        self.table_bucket_policy_resource = TableBucketPolicyResource(self)
        self.table_bucket_replication_resource = TableBucketReplicationResource(self)
        self.table_bucket_resource = TableBucketResource(self)
        self.table_encryption_resource = TableEncryptionResource(self)
        self.table_policy_resource = TablePolicyResource(self)
        self.table_replication_resource = TableReplicationResource(self)
        self.table_resource = TableResource(self)

    def operation_options(
        self, config_overrides: Optional[S3TablesClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: S3TablesClientConfig = config_overrides or {}
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
        resource_arn: "capo_s3tables.types.resource_arn.ResourceArn",
        *,
        config_overrides: Optional[S3TablesClientConfig] = None,
    ) -> "capo_s3tables.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>Lists all of the tags applied to a specified Amazon S3 Tables resource. Each tag is a label consisting of a key and value pair. Tags can help you organize, track costs for, and control access to resources. </p> <note> <p>For a list of S3 resources that support tagging, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/tagging.html#manage-tags">Managing tags for Amazon S3 resources</a>.</p> </note> <dl> <dt>Permissions</dt> <dd> <p>For tables and table buckets, you must have the <code>s3tables:ListTagsForResource</code> permission to use this operation.</p> </dd> </dl>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the Amazon S3 Tables resource that you want to list tags for. The tagged resource can be a table bucket or a table. For a list of all S3 resources that support tagging, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/tagging.html#manage-tags">Managing tags for Amazon S3 resources</a>.</p>

        Raises:
            capo_s3tables.errors.bad_request_exception.BadRequestException: <p>The request is invalid or malformed.</p>
            capo_s3tables.errors.conflict_exception.ConflictException: <p>The request failed because there is a conflict with a previous write. You can retry the request.</p>
            capo_s3tables.errors.forbidden_exception.ForbiddenException: <p>The caller isn't authorized to make the request.</p>
            capo_s3tables.errors.internal_server_error_exception.InternalServerErrorException: <p>The request failed due to an internal server error.</p>
            capo_s3tables.errors.not_found_exception.NotFoundException: <p>The request was rejected because the specified resource could not be found.</p>
            capo_s3tables.errors.too_many_requests_exception.TooManyRequestsException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_s3tables.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_s3tables.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> OperationResponse[
            "capo_s3tables.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import capo_s3tables._operations.s3_table_buckets.list_tags_for_resource

            output, http_response = (
                capo_s3tables._operations.s3_table_buckets.list_tags_for_resource.list_tags_for_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_s3tables.types.list_tags_for_resource_request.ListTagsForResourceRequest = {
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
        resource_arn: "capo_s3tables.types.resource_arn.ResourceArn",
        tags: "capo_s3tables.types.tags.Tags",
        *,
        config_overrides: Optional[S3TablesClientConfig] = None,
    ) -> "capo_s3tables.types.tag_resource_response.TagResourceResponse":
        """<p>Applies one or more user-defined tags to an Amazon S3 Tables resource or updates existing tags. Each tag is a label consisting of a key and value pair. Tags can help you organize, track costs for, and control access to your resources. You can add up to 50 tags for each S3 resource. </p> <note> <p>For a list of S3 resources that support tagging, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/tagging.html#manage-tags">Managing tags for Amazon S3 resources</a>.</p> </note> <dl> <dt>Permissions</dt> <dd> <p>For tables and table buckets, you must have the <code>s3tables:TagResource</code> permission to use this operation.</p> </dd> </dl>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the Amazon S3 Tables resource that you're applying tags to. The tagged resource can be a table bucket or a table. For a list of all S3 resources that support tagging, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/tagging.html#manage-tags">Managing tags for Amazon S3 resources</a>.</p>
            tags: <p>The user-defined tag that you want to add to the specified S3 Tables resource. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/tagging.html">Tagging for cost allocation or attribute-based access control (ABAC)</a>.</p>

        Raises:
            capo_s3tables.errors.bad_request_exception.BadRequestException: <p>The request is invalid or malformed.</p>
            capo_s3tables.errors.conflict_exception.ConflictException: <p>The request failed because there is a conflict with a previous write. You can retry the request.</p>
            capo_s3tables.errors.forbidden_exception.ForbiddenException: <p>The caller isn't authorized to make the request.</p>
            capo_s3tables.errors.internal_server_error_exception.InternalServerErrorException: <p>The request failed due to an internal server error.</p>
            capo_s3tables.errors.not_found_exception.NotFoundException: <p>The request was rejected because the specified resource could not be found.</p>
            capo_s3tables.errors.too_many_requests_exception.TooManyRequestsException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_s3tables.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_s3tables.types.tag_resource_request.TagResourceRequest]",
        ) -> OperationResponse[
            "capo_s3tables.types.tag_resource_response.TagResourceResponse"
        ]:
            import capo_s3tables._operations.s3_table_buckets.tag_resource

            output, http_response = (
                capo_s3tables._operations.s3_table_buckets.tag_resource.tag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_s3tables.types.tag_resource_request.TagResourceRequest = {
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
        resource_arn: "capo_s3tables.types.resource_arn.ResourceArn",
        tag_keys: "capo_s3tables.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[S3TablesClientConfig] = None,
    ) -> "capo_s3tables.types.untag_resource_response.UntagResourceResponse":
        """<p>Removes the specified user-defined tags from an Amazon S3 Tables resource. You can pass one or more tag keys. </p> <note> <p>For a list of S3 resources that support tagging, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/tagging.html#manage-tags">Managing tags for Amazon S3 resources</a>.</p> </note> <dl> <dt>Permissions</dt> <dd> <p>For tables and table buckets, you must have the <code>s3tables:UntagResource</code> permission to use this operation.</p> </dd> </dl>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the Amazon S3 Tables resource that you're removing tags from. The tagged resource can be a table bucket or a table. For a list of all S3 resources that support tagging, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/tagging.html#manage-tags">Managing tags for Amazon S3 resources</a>.</p>
            tag_keys: <p>The array of tag keys that you're removing from the S3 Tables resource. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/tagging.html">Tagging for cost allocation or attribute-based access control (ABAC)</a>.</p>

        Raises:
            capo_s3tables.errors.bad_request_exception.BadRequestException: <p>The request is invalid or malformed.</p>
            capo_s3tables.errors.conflict_exception.ConflictException: <p>The request failed because there is a conflict with a previous write. You can retry the request.</p>
            capo_s3tables.errors.forbidden_exception.ForbiddenException: <p>The caller isn't authorized to make the request.</p>
            capo_s3tables.errors.internal_server_error_exception.InternalServerErrorException: <p>The request failed due to an internal server error.</p>
            capo_s3tables.errors.not_found_exception.NotFoundException: <p>The request was rejected because the specified resource could not be found.</p>
            capo_s3tables.errors.too_many_requests_exception.TooManyRequestsException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_s3tables.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_s3tables.types.untag_resource_request.UntagResourceRequest]",
        ) -> OperationResponse[
            "capo_s3tables.types.untag_resource_response.UntagResourceResponse"
        ]:
            import capo_s3tables._operations.s3_table_buckets.untag_resource

            output, http_response = (
                capo_s3tables._operations.s3_table_buckets.untag_resource.untag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_s3tables.types.untag_resource_request.UntagResourceRequest = {
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

    def create_namespace(
        self,
        table_bucket_arn: "capo_s3tables.types.table_bucket_arn.TableBucketARN",
        namespace: "capo_s3tables.types.namespace_list.NamespaceList",
        *,
        config_overrides: Optional[S3TablesClientConfig] = None,
    ) -> "capo_s3tables.types.create_namespace_response.CreateNamespaceResponse":
        """<p>Creates a namespace. A namespace is a logical grouping of tables within your table bucket, which you can use to organize tables. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-namespace-create.html">Create a namespace</a> in the <i>Amazon Simple Storage Service User Guide</i>.</p> <dl> <dt>Permissions</dt> <dd> <p>You must have the <code>s3tables:CreateNamespace</code> permission to use this operation. </p> </dd> </dl>

        Args:
            table_bucket_arn: <p>The Amazon Resource Name (ARN) of the table bucket to create the namespace in.</p>
            namespace: <p>A name for the namespace.</p>

        Raises:
            capo_s3tables.errors.bad_request_exception.BadRequestException: <p>The request is invalid or malformed.</p>
            capo_s3tables.errors.conflict_exception.ConflictException: <p>The request failed because there is a conflict with a previous write. You can retry the request.</p>
            capo_s3tables.errors.forbidden_exception.ForbiddenException: <p>The caller isn't authorized to make the request.</p>
            capo_s3tables.errors.internal_server_error_exception.InternalServerErrorException: <p>The request failed due to an internal server error.</p>
            capo_s3tables.errors.not_found_exception.NotFoundException: <p>The request was rejected because the specified resource could not be found.</p>
            capo_s3tables.errors.too_many_requests_exception.TooManyRequestsException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_s3tables.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_s3tables.types.create_namespace_request.CreateNamespaceRequest]",
        ) -> OperationResponse[
            "capo_s3tables.types.create_namespace_response.CreateNamespaceResponse"
        ]:
            import capo_s3tables._operations.s3_table_buckets.create_namespace

            output, http_response = (
                capo_s3tables._operations.s3_table_buckets.create_namespace.create_namespace(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_s3tables.types.create_namespace_request.CreateNamespaceRequest = {
            "table_bucket_arn": table_bucket_arn,
            "namespace": namespace,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_namespace(
        self,
        table_bucket_arn: "capo_s3tables.types.table_bucket_arn.TableBucketARN",
        namespace: "capo_s3tables.types.namespace_name.NamespaceName",
        *,
        config_overrides: Optional[S3TablesClientConfig] = None,
    ) -> None:
        """<p>Deletes a namespace. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-namespace-delete.html">Delete a namespace</a> in the <i>Amazon Simple Storage Service User Guide</i>.</p> <dl> <dt>Permissions</dt> <dd> <p>You must have the <code>s3tables:DeleteNamespace</code> permission to use this operation. </p> </dd> </dl>

        Args:
            table_bucket_arn: <p>The Amazon Resource Name (ARN) of the table bucket associated with the namespace.</p>
            namespace: <p>The name of the namespace.</p>

        Raises:
            capo_s3tables.errors.bad_request_exception.BadRequestException: <p>The request is invalid or malformed.</p>
            capo_s3tables.errors.conflict_exception.ConflictException: <p>The request failed because there is a conflict with a previous write. You can retry the request.</p>
            capo_s3tables.errors.forbidden_exception.ForbiddenException: <p>The caller isn't authorized to make the request.</p>
            capo_s3tables.errors.internal_server_error_exception.InternalServerErrorException: <p>The request failed due to an internal server error.</p>
            capo_s3tables.errors.not_found_exception.NotFoundException: <p>The request was rejected because the specified resource could not be found.</p>
            capo_s3tables.errors.too_many_requests_exception.TooManyRequestsException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_s3tables.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_s3tables.types.delete_namespace_request.DeleteNamespaceRequest]",
        ) -> OperationResponse[None]:
            import capo_s3tables._operations.s3_table_buckets.delete_namespace

            output, http_response = (
                capo_s3tables._operations.s3_table_buckets.delete_namespace.delete_namespace(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_s3tables.types.delete_namespace_request.DeleteNamespaceRequest = {
            "table_bucket_arn": table_bucket_arn,
            "namespace": namespace,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_namespace(
        self,
        table_bucket_arn: "capo_s3tables.types.table_bucket_arn.TableBucketARN",
        namespace: "capo_s3tables.types.namespace_name.NamespaceName",
        *,
        config_overrides: Optional[S3TablesClientConfig] = None,
    ) -> "capo_s3tables.types.get_namespace_response.GetNamespaceResponse":
        """<p>Gets details about a namespace. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-namespace.html">Table namespaces</a> in the <i>Amazon Simple Storage Service User Guide</i>.</p> <dl> <dt>Permissions</dt> <dd> <p>You must have the <code>s3tables:GetNamespace</code> permission to use this operation. </p> </dd> </dl>

        Args:
            table_bucket_arn: <p>The Amazon Resource Name (ARN) of the table bucket.</p>
            namespace: <p>The name of the namespace.</p>

        Raises:
            capo_s3tables.errors.access_denied_exception.AccessDeniedException: <p>The action cannot be performed because you do not have the required permission.</p>
            capo_s3tables.errors.bad_request_exception.BadRequestException: <p>The request is invalid or malformed.</p>
            capo_s3tables.errors.conflict_exception.ConflictException: <p>The request failed because there is a conflict with a previous write. You can retry the request.</p>
            capo_s3tables.errors.forbidden_exception.ForbiddenException: <p>The caller isn't authorized to make the request.</p>
            capo_s3tables.errors.internal_server_error_exception.InternalServerErrorException: <p>The request failed due to an internal server error.</p>
            capo_s3tables.errors.not_found_exception.NotFoundException: <p>The request was rejected because the specified resource could not be found.</p>
            capo_s3tables.errors.too_many_requests_exception.TooManyRequestsException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_s3tables.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_s3tables.types.get_namespace_request.GetNamespaceRequest]",
        ) -> OperationResponse[
            "capo_s3tables.types.get_namespace_response.GetNamespaceResponse"
        ]:
            import capo_s3tables._operations.s3_table_buckets.get_namespace

            output, http_response = (
                capo_s3tables._operations.s3_table_buckets.get_namespace.get_namespace(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_s3tables.types.get_namespace_request.GetNamespaceRequest = {
            "table_bucket_arn": table_bucket_arn,
            "namespace": namespace,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_namespaces(
        self,
        table_bucket_arn: "capo_s3tables.types.table_bucket_arn.TableBucketARN",
        *,
        config_overrides: Optional[S3TablesClientConfig] = None,
        prefix: Optional[str] = None,
        continuation_token: Optional["capo_s3tables.types.next_token.NextToken"] = None,
        max_namespaces: Optional[
            "capo_s3tables.types.list_namespaces_limit.ListNamespacesLimit"
        ] = None,
    ) -> "capo_s3tables.types.list_namespaces_response.ListNamespacesResponse":
        """<p>Lists the namespaces within a table bucket. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-namespace.html">Table namespaces</a> in the <i>Amazon Simple Storage Service User Guide</i>.</p> <dl> <dt>Permissions</dt> <dd> <p>You must have the <code>s3tables:ListNamespaces</code> permission to use this operation. </p> </dd> </dl>

        Args:
            table_bucket_arn: <p>The Amazon Resource Name (ARN) of the table bucket.</p>
            prefix: <p>The prefix of the namespaces.</p>
            continuation_token: <p> <code>ContinuationToken</code> indicates to Amazon S3 that the list is being continued on this bucket with a token. <code>ContinuationToken</code> is obfuscated and is not a real key. You can use this <code>ContinuationToken</code> for pagination of the list results.</p>
            max_namespaces: <p>The maximum number of namespaces to return in the list.</p>

        Raises:
            capo_s3tables.errors.access_denied_exception.AccessDeniedException: <p>The action cannot be performed because you do not have the required permission.</p>
            capo_s3tables.errors.bad_request_exception.BadRequestException: <p>The request is invalid or malformed.</p>
            capo_s3tables.errors.conflict_exception.ConflictException: <p>The request failed because there is a conflict with a previous write. You can retry the request.</p>
            capo_s3tables.errors.forbidden_exception.ForbiddenException: <p>The caller isn't authorized to make the request.</p>
            capo_s3tables.errors.internal_server_error_exception.InternalServerErrorException: <p>The request failed due to an internal server error.</p>
            capo_s3tables.errors.not_found_exception.NotFoundException: <p>The request was rejected because the specified resource could not be found.</p>
            capo_s3tables.errors.too_many_requests_exception.TooManyRequestsException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_s3tables.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_s3tables.types.list_namespaces_request.ListNamespacesRequest]",
        ) -> OperationResponse[
            "capo_s3tables.types.list_namespaces_response.ListNamespacesResponse"
        ]:
            import capo_s3tables._operations.s3_table_buckets.list_namespaces

            output, http_response = (
                capo_s3tables._operations.s3_table_buckets.list_namespaces.list_namespaces(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_s3tables.types.list_namespaces_request.ListNamespacesRequest = {
            "table_bucket_arn": table_bucket_arn
        }
        if prefix is not None:
            input_["prefix"] = prefix
        if continuation_token is not None:
            input_["continuation_token"] = continuation_token
        if max_namespaces is not None:
            input_["max_namespaces"] = max_namespaces

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_namespaces(
        self,
        table_bucket_arn: "capo_s3tables.types.table_bucket_arn.TableBucketARN",
        *,
        config_overrides: Optional[S3TablesClientConfig] = None,
        prefix: Optional[str] = None,
        continuation_token: Optional["capo_s3tables.types.next_token.NextToken"] = None,
        max_namespaces: Optional[
            "capo_s3tables.types.list_namespaces_limit.ListNamespacesLimit"
        ] = None,
    ) -> "Iterator[capo_s3tables.types.namespace_summary.NamespaceSummary]":
        _token = continuation_token
        while True:
            _response = self.list_namespaces(
                table_bucket_arn,
                config_overrides=config_overrides,
                prefix=prefix,
                continuation_token=_token,
                max_namespaces=max_namespaces,
            )
            _page = _resolve_path(_response, ("namespaces",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("continuation_token",))
            if not _token:
                break

    def delete_table_bucket_encryption(
        self,
        table_bucket_arn: "capo_s3tables.types.table_bucket_arn.TableBucketARN",
        *,
        config_overrides: Optional[S3TablesClientConfig] = None,
    ) -> None:
        """<p>Deletes the encryption configuration for a table bucket.</p> <dl> <dt>Permissions</dt> <dd> <p>You must have the <code>s3tables:DeleteTableBucketEncryption</code> permission to use this operation.</p> </dd> </dl>

        Args:
            table_bucket_arn: <p>The Amazon Resource Name (ARN) of the table bucket.</p>

        Raises:
            capo_s3tables.errors.bad_request_exception.BadRequestException: <p>The request is invalid or malformed.</p>
            capo_s3tables.errors.conflict_exception.ConflictException: <p>The request failed because there is a conflict with a previous write. You can retry the request.</p>
            capo_s3tables.errors.forbidden_exception.ForbiddenException: <p>The caller isn't authorized to make the request.</p>
            capo_s3tables.errors.internal_server_error_exception.InternalServerErrorException: <p>The request failed due to an internal server error.</p>
            capo_s3tables.errors.not_found_exception.NotFoundException: <p>The request was rejected because the specified resource could not be found.</p>
            capo_s3tables.errors.too_many_requests_exception.TooManyRequestsException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_s3tables.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_s3tables.types.delete_table_bucket_encryption_request.DeleteTableBucketEncryptionRequest]",
        ) -> OperationResponse[None]:
            import capo_s3tables._operations.s3_table_buckets.delete_table_bucket_encryption

            output, http_response = (
                capo_s3tables._operations.s3_table_buckets.delete_table_bucket_encryption.delete_table_bucket_encryption(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_s3tables.types.delete_table_bucket_encryption_request.DeleteTableBucketEncryptionRequest = {
            "table_bucket_arn": table_bucket_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_table_bucket_encryption(
        self,
        table_bucket_arn: "capo_s3tables.types.table_bucket_arn.TableBucketARN",
        *,
        config_overrides: Optional[S3TablesClientConfig] = None,
    ) -> "capo_s3tables.types.get_table_bucket_encryption_response.GetTableBucketEncryptionResponse":
        """<p>Gets the encryption configuration for a table bucket.</p> <dl> <dt>Permissions</dt> <dd> <p>You must have the <code>s3tables:GetTableBucketEncryption</code> permission to use this operation.</p> </dd> </dl>

        Args:
            table_bucket_arn: <p>The Amazon Resource Name (ARN) of the table bucket.</p>

        Raises:
            capo_s3tables.errors.access_denied_exception.AccessDeniedException: <p>The action cannot be performed because you do not have the required permission.</p>
            capo_s3tables.errors.bad_request_exception.BadRequestException: <p>The request is invalid or malformed.</p>
            capo_s3tables.errors.forbidden_exception.ForbiddenException: <p>The caller isn't authorized to make the request.</p>
            capo_s3tables.errors.internal_server_error_exception.InternalServerErrorException: <p>The request failed due to an internal server error.</p>
            capo_s3tables.errors.not_found_exception.NotFoundException: <p>The request was rejected because the specified resource could not be found.</p>
            capo_s3tables.errors.too_many_requests_exception.TooManyRequestsException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_s3tables.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_s3tables.types.get_table_bucket_encryption_request.GetTableBucketEncryptionRequest]",
        ) -> OperationResponse[
            "capo_s3tables.types.get_table_bucket_encryption_response.GetTableBucketEncryptionResponse"
        ]:
            import capo_s3tables._operations.s3_table_buckets.get_table_bucket_encryption

            output, http_response = (
                capo_s3tables._operations.s3_table_buckets.get_table_bucket_encryption.get_table_bucket_encryption(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_s3tables.types.get_table_bucket_encryption_request.GetTableBucketEncryptionRequest = {
            "table_bucket_arn": table_bucket_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def put_table_bucket_encryption(
        self,
        table_bucket_arn: "capo_s3tables.types.table_bucket_arn.TableBucketARN",
        encryption_configuration: "capo_s3tables.types.encryption_configuration.EncryptionConfiguration",
        *,
        config_overrides: Optional[S3TablesClientConfig] = None,
    ) -> None:
        """<p>Sets the encryption configuration for a table bucket.</p> <dl> <dt>Permissions</dt> <dd> <p>You must have the <code>s3tables:PutTableBucketEncryption</code> permission to use this operation.</p> <note> <p>If you choose SSE-KMS encryption you must grant the S3 Tables maintenance principal access to your KMS key. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-kms-permissions.html">Permissions requirements for S3 Tables SSE-KMS encryption</a> in the <i>Amazon Simple Storage Service User Guide</i>.</p> </note> </dd> </dl>

        Args:
            table_bucket_arn: <p>The Amazon Resource Name (ARN) of the table bucket.</p>
            encryption_configuration: <p>The encryption configuration to apply to the table bucket.</p>

        Raises:
            capo_s3tables.errors.bad_request_exception.BadRequestException: <p>The request is invalid or malformed.</p>
            capo_s3tables.errors.conflict_exception.ConflictException: <p>The request failed because there is a conflict with a previous write. You can retry the request.</p>
            capo_s3tables.errors.forbidden_exception.ForbiddenException: <p>The caller isn't authorized to make the request.</p>
            capo_s3tables.errors.internal_server_error_exception.InternalServerErrorException: <p>The request failed due to an internal server error.</p>
            capo_s3tables.errors.not_found_exception.NotFoundException: <p>The request was rejected because the specified resource could not be found.</p>
            capo_s3tables.errors.too_many_requests_exception.TooManyRequestsException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_s3tables.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_s3tables.types.put_table_bucket_encryption_request.PutTableBucketEncryptionRequest]",
        ) -> OperationResponse[None]:
            import capo_s3tables._operations.s3_table_buckets.put_table_bucket_encryption

            output, http_response = (
                capo_s3tables._operations.s3_table_buckets.put_table_bucket_encryption.put_table_bucket_encryption(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_s3tables.types.put_table_bucket_encryption_request.PutTableBucketEncryptionRequest = {
            "table_bucket_arn": table_bucket_arn,
            "encryption_configuration": encryption_configuration,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_table_bucket_policy(
        self,
        table_bucket_arn: "capo_s3tables.types.table_bucket_arn.TableBucketARN",
        *,
        config_overrides: Optional[S3TablesClientConfig] = None,
    ) -> None:
        """<p>Deletes a table bucket policy. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-bucket-policy.html#table-bucket-policy-delete">Deleting a table bucket policy</a> in the <i>Amazon Simple Storage Service User Guide</i>.</p> <dl> <dt>Permissions</dt> <dd> <p>You must have the <code>s3tables:DeleteTableBucketPolicy</code> permission to use this operation. </p> </dd> </dl>

        Args:
            table_bucket_arn: <p>The Amazon Resource Name (ARN) of the table bucket.</p>

        Raises:
            capo_s3tables.errors.bad_request_exception.BadRequestException: <p>The request is invalid or malformed.</p>
            capo_s3tables.errors.conflict_exception.ConflictException: <p>The request failed because there is a conflict with a previous write. You can retry the request.</p>
            capo_s3tables.errors.forbidden_exception.ForbiddenException: <p>The caller isn't authorized to make the request.</p>
            capo_s3tables.errors.internal_server_error_exception.InternalServerErrorException: <p>The request failed due to an internal server error.</p>
            capo_s3tables.errors.not_found_exception.NotFoundException: <p>The request was rejected because the specified resource could not be found.</p>
            capo_s3tables.errors.too_many_requests_exception.TooManyRequestsException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_s3tables.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_s3tables.types.delete_table_bucket_policy_request.DeleteTableBucketPolicyRequest]",
        ) -> OperationResponse[None]:
            import capo_s3tables._operations.s3_table_buckets.delete_table_bucket_policy

            output, http_response = (
                capo_s3tables._operations.s3_table_buckets.delete_table_bucket_policy.delete_table_bucket_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_s3tables.types.delete_table_bucket_policy_request.DeleteTableBucketPolicyRequest = {
            "table_bucket_arn": table_bucket_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_table_bucket_policy(
        self,
        table_bucket_arn: "capo_s3tables.types.table_bucket_arn.TableBucketARN",
        *,
        config_overrides: Optional[S3TablesClientConfig] = None,
    ) -> "capo_s3tables.types.get_table_bucket_policy_response.GetTableBucketPolicyResponse":
        """<p>Gets details about a table bucket policy. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-bucket-policy.html#table-bucket-policy-get">Viewing a table bucket policy</a> in the <i>Amazon Simple Storage Service User Guide</i>.</p> <dl> <dt>Permissions</dt> <dd> <p>You must have the <code>s3tables:GetTableBucketPolicy</code> permission to use this operation. </p> </dd> </dl>

        Args:
            table_bucket_arn: <p>The Amazon Resource Name (ARN) of the table bucket.</p>

        Raises:
            capo_s3tables.errors.bad_request_exception.BadRequestException: <p>The request is invalid or malformed.</p>
            capo_s3tables.errors.conflict_exception.ConflictException: <p>The request failed because there is a conflict with a previous write. You can retry the request.</p>
            capo_s3tables.errors.forbidden_exception.ForbiddenException: <p>The caller isn't authorized to make the request.</p>
            capo_s3tables.errors.internal_server_error_exception.InternalServerErrorException: <p>The request failed due to an internal server error.</p>
            capo_s3tables.errors.not_found_exception.NotFoundException: <p>The request was rejected because the specified resource could not be found.</p>
            capo_s3tables.errors.too_many_requests_exception.TooManyRequestsException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_s3tables.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_s3tables.types.get_table_bucket_policy_request.GetTableBucketPolicyRequest]",
        ) -> OperationResponse[
            "capo_s3tables.types.get_table_bucket_policy_response.GetTableBucketPolicyResponse"
        ]:
            import capo_s3tables._operations.s3_table_buckets.get_table_bucket_policy

            output, http_response = (
                capo_s3tables._operations.s3_table_buckets.get_table_bucket_policy.get_table_bucket_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_s3tables.types.get_table_bucket_policy_request.GetTableBucketPolicyRequest = {
            "table_bucket_arn": table_bucket_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def put_table_bucket_policy(
        self,
        table_bucket_arn: "capo_s3tables.types.table_bucket_arn.TableBucketARN",
        resource_policy: "capo_s3tables.types.resource_policy.ResourcePolicy",
        *,
        config_overrides: Optional[S3TablesClientConfig] = None,
    ) -> None:
        """<p>Creates a new table bucket policy or replaces an existing table bucket policy for a table bucket. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-bucket-policy.html#table-bucket-policy-add">Adding a table bucket policy</a> in the <i>Amazon Simple Storage Service User Guide</i>.</p> <dl> <dt>Permissions</dt> <dd> <p>You must have the <code>s3tables:PutTableBucketPolicy</code> permission to use this operation. </p> </dd> </dl>

        Args:
            table_bucket_arn: <p>The Amazon Resource Name (ARN) of the table bucket.</p>
            resource_policy: <p>The <code>JSON</code> that defines the policy.</p>

        Raises:
            capo_s3tables.errors.bad_request_exception.BadRequestException: <p>The request is invalid or malformed.</p>
            capo_s3tables.errors.conflict_exception.ConflictException: <p>The request failed because there is a conflict with a previous write. You can retry the request.</p>
            capo_s3tables.errors.forbidden_exception.ForbiddenException: <p>The caller isn't authorized to make the request.</p>
            capo_s3tables.errors.internal_server_error_exception.InternalServerErrorException: <p>The request failed due to an internal server error.</p>
            capo_s3tables.errors.not_found_exception.NotFoundException: <p>The request was rejected because the specified resource could not be found.</p>
            capo_s3tables.errors.too_many_requests_exception.TooManyRequestsException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_s3tables.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_s3tables.types.put_table_bucket_policy_request.PutTableBucketPolicyRequest]",
        ) -> OperationResponse[None]:
            import capo_s3tables._operations.s3_table_buckets.put_table_bucket_policy

            output, http_response = (
                capo_s3tables._operations.s3_table_buckets.put_table_bucket_policy.put_table_bucket_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_s3tables.types.put_table_bucket_policy_request.PutTableBucketPolicyRequest = {
            "table_bucket_arn": table_bucket_arn,
            "resource_policy": resource_policy,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_table_bucket_replication(
        self,
        table_bucket_arn: "capo_s3tables.types.table_bucket_arn.TableBucketARN",
        *,
        config_overrides: Optional[S3TablesClientConfig] = None,
        version_token: Optional[
            "capo_s3tables.types.version_token.VersionToken"
        ] = None,
    ) -> None:
        """<p>Deletes the replication configuration for a table bucket. After deletion, new table updates will no longer be replicated to destination buckets, though existing replicated tables will remain in destination buckets.</p> <dl> <dt>Permissions</dt> <dd> <p>You must have the <code>s3tables:DeleteTableBucketReplication</code> permission to use this operation.</p> </dd> </dl>

        Args:
            table_bucket_arn: <p>The Amazon Resource Name (ARN) of the table bucket.</p>
            version_token: <p>A version token from a previous GetTableBucketReplication call. Use this token to ensure you're deleting the expected version of the configuration.</p>

        Raises:
            capo_s3tables.errors.access_denied_exception.AccessDeniedException: <p>The action cannot be performed because you do not have the required permission.</p>
            capo_s3tables.errors.bad_request_exception.BadRequestException: <p>The request is invalid or malformed.</p>
            capo_s3tables.errors.conflict_exception.ConflictException: <p>The request failed because there is a conflict with a previous write. You can retry the request.</p>
            capo_s3tables.errors.forbidden_exception.ForbiddenException: <p>The caller isn't authorized to make the request.</p>
            capo_s3tables.errors.internal_server_error_exception.InternalServerErrorException: <p>The request failed due to an internal server error.</p>
            capo_s3tables.errors.not_found_exception.NotFoundException: <p>The request was rejected because the specified resource could not be found.</p>
            capo_s3tables.errors.too_many_requests_exception.TooManyRequestsException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_s3tables.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_s3tables.types.delete_table_bucket_replication_request.DeleteTableBucketReplicationRequest]",
        ) -> OperationResponse[None]:
            import capo_s3tables._operations.s3_table_buckets.delete_table_bucket_replication

            output, http_response = (
                capo_s3tables._operations.s3_table_buckets.delete_table_bucket_replication.delete_table_bucket_replication(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_s3tables.types.delete_table_bucket_replication_request.DeleteTableBucketReplicationRequest = {
            "table_bucket_arn": table_bucket_arn
        }
        if version_token is not None:
            input_["version_token"] = version_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_table_bucket_replication(
        self,
        table_bucket_arn: "capo_s3tables.types.table_bucket_arn.TableBucketARN",
        *,
        config_overrides: Optional[S3TablesClientConfig] = None,
    ) -> "capo_s3tables.types.get_table_bucket_replication_response.GetTableBucketReplicationResponse":
        """<p>Retrieves the replication configuration for a table bucket.This operation returns the IAM role, <code>versionToken</code>, and replication rules that define how tables in this bucket are replicated to other buckets.</p> <dl> <dt>Permissions</dt> <dd> <p>You must have the <code>s3tables:GetTableBucketReplication</code> permission to use this operation.</p> </dd> </dl>

        Args:
            table_bucket_arn: <p>The Amazon Resource Name (ARN) of the table bucket.</p>

        Raises:
            capo_s3tables.errors.access_denied_exception.AccessDeniedException: <p>The action cannot be performed because you do not have the required permission.</p>
            capo_s3tables.errors.bad_request_exception.BadRequestException: <p>The request is invalid or malformed.</p>
            capo_s3tables.errors.conflict_exception.ConflictException: <p>The request failed because there is a conflict with a previous write. You can retry the request.</p>
            capo_s3tables.errors.forbidden_exception.ForbiddenException: <p>The caller isn't authorized to make the request.</p>
            capo_s3tables.errors.internal_server_error_exception.InternalServerErrorException: <p>The request failed due to an internal server error.</p>
            capo_s3tables.errors.not_found_exception.NotFoundException: <p>The request was rejected because the specified resource could not be found.</p>
            capo_s3tables.errors.too_many_requests_exception.TooManyRequestsException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_s3tables.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_s3tables.types.get_table_bucket_replication_request.GetTableBucketReplicationRequest]",
        ) -> OperationResponse[
            "capo_s3tables.types.get_table_bucket_replication_response.GetTableBucketReplicationResponse"
        ]:
            import capo_s3tables._operations.s3_table_buckets.get_table_bucket_replication

            output, http_response = (
                capo_s3tables._operations.s3_table_buckets.get_table_bucket_replication.get_table_bucket_replication(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_s3tables.types.get_table_bucket_replication_request.GetTableBucketReplicationRequest = {
            "table_bucket_arn": table_bucket_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def put_table_bucket_replication(
        self,
        table_bucket_arn: "capo_s3tables.types.table_bucket_arn.TableBucketARN",
        configuration: "capo_s3tables.types.table_bucket_replication_configuration.TableBucketReplicationConfiguration",
        *,
        config_overrides: Optional[S3TablesClientConfig] = None,
        version_token: Optional[
            "capo_s3tables.types.version_token.VersionToken"
        ] = None,
    ) -> "capo_s3tables.types.put_table_bucket_replication_response.PutTableBucketReplicationResponse":
        """<p>Creates or updates the replication configuration for a table bucket. This operation defines how tables in the source bucket are replicated to destination buckets. Replication helps ensure data availability and disaster recovery across regions or accounts.</p> <dl> <dt>Permissions</dt> <dd> <ul> <li> <p>You must have the <code>s3tables:PutTableBucketReplication</code> permission to use this operation. The IAM role specified in the configuration must have permissions to read from the source bucket and write permissions to all destination buckets.</p> </li> <li> <p>You must also have the following permissions:</p> <ul> <li> <p> <code>s3tables:GetTable</code> permission on the source table.</p> </li> <li> <p> <code>s3tables:ListTables</code> permission on the bucket containing the table.</p> </li> <li> <p> <code>s3tables:CreateTable</code> permission for the destination.</p> </li> <li> <p> <code>s3tables:CreateNamespace</code> permission for the destination.</p> </li> <li> <p> <code>s3tables:GetTableMaintenanceConfig</code> permission for the source bucket.</p> </li> <li> <p> <code>s3tables:PutTableMaintenanceConfig</code> permission for the destination bucket.</p> </li> </ul> </li> <li> <p>You must have <code>iam:PassRole</code> permission with condition allowing roles to be passed to <code>replication.s3tables.amazonaws.com</code>.</p> </li> </ul> </dd> </dl>

        Args:
            table_bucket_arn: <p>The Amazon Resource Name (ARN) of the source table bucket.</p>
            version_token: <p>A version token from a previous GetTableBucketReplication call. Use this token to ensure you're updating the expected version of the configuration.</p>
            configuration: <p>The replication configuration to apply, including the IAM role and replication rules.</p>

        Raises:
            capo_s3tables.errors.access_denied_exception.AccessDeniedException: <p>The action cannot be performed because you do not have the required permission.</p>
            capo_s3tables.errors.bad_request_exception.BadRequestException: <p>The request is invalid or malformed.</p>
            capo_s3tables.errors.conflict_exception.ConflictException: <p>The request failed because there is a conflict with a previous write. You can retry the request.</p>
            capo_s3tables.errors.forbidden_exception.ForbiddenException: <p>The caller isn't authorized to make the request.</p>
            capo_s3tables.errors.internal_server_error_exception.InternalServerErrorException: <p>The request failed due to an internal server error.</p>
            capo_s3tables.errors.not_found_exception.NotFoundException: <p>The request was rejected because the specified resource could not be found.</p>
            capo_s3tables.errors.too_many_requests_exception.TooManyRequestsException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_s3tables.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_s3tables.types.put_table_bucket_replication_request.PutTableBucketReplicationRequest]",
        ) -> OperationResponse[
            "capo_s3tables.types.put_table_bucket_replication_response.PutTableBucketReplicationResponse"
        ]:
            import capo_s3tables._operations.s3_table_buckets.put_table_bucket_replication

            output, http_response = (
                capo_s3tables._operations.s3_table_buckets.put_table_bucket_replication.put_table_bucket_replication(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_s3tables.types.put_table_bucket_replication_request.PutTableBucketReplicationRequest = {
            "table_bucket_arn": table_bucket_arn,
            "configuration": configuration,
        }
        if version_token is not None:
            input_["version_token"] = version_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_table_bucket(
        self,
        name: "capo_s3tables.types.table_bucket_name.TableBucketName",
        *,
        config_overrides: Optional[S3TablesClientConfig] = None,
        encryption_configuration: Optional[
            "capo_s3tables.types.encryption_configuration.EncryptionConfiguration"
        ] = None,
        storage_class_configuration: Optional[
            "capo_s3tables.types.storage_class_configuration.StorageClassConfiguration"
        ] = None,
        tags: Optional["capo_s3tables.types.tags.Tags"] = None,
    ) -> "capo_s3tables.types.create_table_bucket_response.CreateTableBucketResponse":
        """<p>Creates a table bucket. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-buckets-create.html">Creating a table bucket</a> in the <i>Amazon Simple Storage Service User Guide</i>.</p> <dl> <dt>Permissions</dt> <dd> <ul> <li> <p>You must have the <code>s3tables:CreateTableBucket</code> permission to use this operation. </p> </li> <li> <p>If you use this operation with the optional <code>encryptionConfiguration</code> parameter you must have the <code>s3tables:PutTableBucketEncryption</code> permission.</p> </li> <li> <p>If you use this operation with the <code>storageClassConfiguration</code> request parameter, you must have the <code>s3tables:PutTableBucketStorageClass</code> permission.</p> </li> <li> <p>To create a table bucket with tags, you must have the <code>s3tables:TagResource</code> permission in addition to <code>s3tables:CreateTableBucket</code> permission.</p> </li> </ul> </dd> </dl>

        Args:
            name: <p>The name for the table bucket.</p>
            encryption_configuration: <p>The encryption configuration to use for the table bucket. This configuration specifies the default encryption settings that will be applied to all tables created in this bucket unless overridden at the table level. The configuration includes the encryption algorithm and, if using SSE-KMS, the KMS key to use.</p>
            storage_class_configuration: <p>The default storage class configuration for the table bucket. This configuration will be applied to all new tables created in this bucket unless overridden at the table level. If not specified, the service default storage class will be used.</p>
            tags: <p>A map of user-defined tags that you would like to apply to the table bucket that you are creating. A tag is a key-value pair that you apply to your resources. Tags can help you organize and control access to resources. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/tagging.html">Tagging for cost allocation or attribute-based access control (ABAC)</a>.</p> <note> <p>You must have the <code>s3tables:TagResource</code> permission in addition to <code>s3tables:CreateTableBucket</code> permisson to create a table bucket with tags.</p> </note>

        Raises:
            capo_s3tables.errors.bad_request_exception.BadRequestException: <p>The request is invalid or malformed.</p>
            capo_s3tables.errors.conflict_exception.ConflictException: <p>The request failed because there is a conflict with a previous write. You can retry the request.</p>
            capo_s3tables.errors.forbidden_exception.ForbiddenException: <p>The caller isn't authorized to make the request.</p>
            capo_s3tables.errors.internal_server_error_exception.InternalServerErrorException: <p>The request failed due to an internal server error.</p>
            capo_s3tables.errors.not_found_exception.NotFoundException: <p>The request was rejected because the specified resource could not be found.</p>
            capo_s3tables.errors.too_many_requests_exception.TooManyRequestsException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_s3tables.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_s3tables.types.create_table_bucket_request.CreateTableBucketRequest]",
        ) -> OperationResponse[
            "capo_s3tables.types.create_table_bucket_response.CreateTableBucketResponse"
        ]:
            import capo_s3tables._operations.s3_table_buckets.create_table_bucket

            output, http_response = (
                capo_s3tables._operations.s3_table_buckets.create_table_bucket.create_table_bucket(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_s3tables.types.create_table_bucket_request.CreateTableBucketRequest = {
            "name": name
        }
        if encryption_configuration is not None:
            input_["encryption_configuration"] = encryption_configuration
        if storage_class_configuration is not None:
            input_["storage_class_configuration"] = storage_class_configuration
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_table_bucket(
        self,
        table_bucket_arn: "capo_s3tables.types.table_bucket_arn.TableBucketARN",
        *,
        config_overrides: Optional[S3TablesClientConfig] = None,
    ) -> None:
        """<p>Deletes a table bucket. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-buckets-delete.html">Deleting a table bucket</a> in the <i>Amazon Simple Storage Service User Guide</i>.</p> <dl> <dt>Permissions</dt> <dd> <p>You must have the <code>s3tables:DeleteTableBucket</code> permission to use this operation. </p> </dd> </dl>

        Args:
            table_bucket_arn: <p>The Amazon Resource Name (ARN) of the table bucket.</p>

        Raises:
            capo_s3tables.errors.bad_request_exception.BadRequestException: <p>The request is invalid or malformed.</p>
            capo_s3tables.errors.conflict_exception.ConflictException: <p>The request failed because there is a conflict with a previous write. You can retry the request.</p>
            capo_s3tables.errors.forbidden_exception.ForbiddenException: <p>The caller isn't authorized to make the request.</p>
            capo_s3tables.errors.internal_server_error_exception.InternalServerErrorException: <p>The request failed due to an internal server error.</p>
            capo_s3tables.errors.not_found_exception.NotFoundException: <p>The request was rejected because the specified resource could not be found.</p>
            capo_s3tables.errors.too_many_requests_exception.TooManyRequestsException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_s3tables.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_s3tables.types.delete_table_bucket_request.DeleteTableBucketRequest]",
        ) -> OperationResponse[None]:
            import capo_s3tables._operations.s3_table_buckets.delete_table_bucket

            output, http_response = (
                capo_s3tables._operations.s3_table_buckets.delete_table_bucket.delete_table_bucket(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_s3tables.types.delete_table_bucket_request.DeleteTableBucketRequest = {
            "table_bucket_arn": table_bucket_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_table_bucket_metrics_configuration(
        self,
        table_bucket_arn: "capo_s3tables.types.table_bucket_arn.TableBucketARN",
        *,
        config_overrides: Optional[S3TablesClientConfig] = None,
    ) -> None:
        """<p>Deletes the metrics configuration for a table bucket.</p> <dl> <dt>Permissions</dt> <dd> <p>You must have the <code>s3tables:DeleteTableBucketMetricsConfiguration</code> permission to use this operation.</p> </dd> </dl>

        Args:
            table_bucket_arn: <p>The Amazon Resource Name (ARN) of the table bucket.</p>

        Raises:
            capo_s3tables.errors.bad_request_exception.BadRequestException: <p>The request is invalid or malformed.</p>
            capo_s3tables.errors.conflict_exception.ConflictException: <p>The request failed because there is a conflict with a previous write. You can retry the request.</p>
            capo_s3tables.errors.forbidden_exception.ForbiddenException: <p>The caller isn't authorized to make the request.</p>
            capo_s3tables.errors.internal_server_error_exception.InternalServerErrorException: <p>The request failed due to an internal server error.</p>
            capo_s3tables.errors.not_found_exception.NotFoundException: <p>The request was rejected because the specified resource could not be found.</p>
            capo_s3tables.errors.too_many_requests_exception.TooManyRequestsException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_s3tables.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_s3tables.types.delete_table_bucket_metrics_configuration_request.DeleteTableBucketMetricsConfigurationRequest]",
        ) -> OperationResponse[None]:
            import capo_s3tables._operations.s3_table_buckets.delete_table_bucket_metrics_configuration

            output, http_response = (
                capo_s3tables._operations.s3_table_buckets.delete_table_bucket_metrics_configuration.delete_table_bucket_metrics_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_s3tables.types.delete_table_bucket_metrics_configuration_request.DeleteTableBucketMetricsConfigurationRequest = {
            "table_bucket_arn": table_bucket_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_table_bucket(
        self,
        table_bucket_arn: "capo_s3tables.types.table_bucket_arn.TableBucketARN",
        *,
        config_overrides: Optional[S3TablesClientConfig] = None,
    ) -> "capo_s3tables.types.get_table_bucket_response.GetTableBucketResponse":
        """<p>Gets details on a table bucket. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-buckets-details.html">Viewing details about an Amazon S3 table bucket</a> in the <i>Amazon Simple Storage Service User Guide</i>.</p> <dl> <dt>Permissions</dt> <dd> <p>You must have the <code>s3tables:GetTableBucket</code> permission to use this operation. </p> </dd> </dl>

        Args:
            table_bucket_arn: <p>The Amazon Resource Name (ARN) of the table bucket.</p>

        Raises:
            capo_s3tables.errors.access_denied_exception.AccessDeniedException: <p>The action cannot be performed because you do not have the required permission.</p>
            capo_s3tables.errors.bad_request_exception.BadRequestException: <p>The request is invalid or malformed.</p>
            capo_s3tables.errors.conflict_exception.ConflictException: <p>The request failed because there is a conflict with a previous write. You can retry the request.</p>
            capo_s3tables.errors.forbidden_exception.ForbiddenException: <p>The caller isn't authorized to make the request.</p>
            capo_s3tables.errors.internal_server_error_exception.InternalServerErrorException: <p>The request failed due to an internal server error.</p>
            capo_s3tables.errors.not_found_exception.NotFoundException: <p>The request was rejected because the specified resource could not be found.</p>
            capo_s3tables.errors.too_many_requests_exception.TooManyRequestsException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_s3tables.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_s3tables.types.get_table_bucket_request.GetTableBucketRequest]",
        ) -> OperationResponse[
            "capo_s3tables.types.get_table_bucket_response.GetTableBucketResponse"
        ]:
            import capo_s3tables._operations.s3_table_buckets.get_table_bucket

            output, http_response = (
                capo_s3tables._operations.s3_table_buckets.get_table_bucket.get_table_bucket(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_s3tables.types.get_table_bucket_request.GetTableBucketRequest = {
            "table_bucket_arn": table_bucket_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_table_bucket_maintenance_configuration(
        self,
        table_bucket_arn: "capo_s3tables.types.table_bucket_arn.TableBucketARN",
        *,
        config_overrides: Optional[S3TablesClientConfig] = None,
    ) -> "capo_s3tables.types.get_table_bucket_maintenance_configuration_response.GetTableBucketMaintenanceConfigurationResponse":
        """<p>Gets details about a maintenance configuration for a given table bucket. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-table-buckets-maintenance.html">Amazon S3 table bucket maintenance</a> in the <i>Amazon Simple Storage Service User Guide</i>.</p> <dl> <dt>Permissions</dt> <dd> <p>You must have the <code>s3tables:GetTableBucketMaintenanceConfiguration</code> permission to use this operation. </p> </dd> </dl>

        Args:
            table_bucket_arn: <p>The Amazon Resource Name (ARN) of the table bucket associated with the maintenance configuration.</p>

        Raises:
            capo_s3tables.errors.bad_request_exception.BadRequestException: <p>The request is invalid or malformed.</p>
            capo_s3tables.errors.conflict_exception.ConflictException: <p>The request failed because there is a conflict with a previous write. You can retry the request.</p>
            capo_s3tables.errors.forbidden_exception.ForbiddenException: <p>The caller isn't authorized to make the request.</p>
            capo_s3tables.errors.internal_server_error_exception.InternalServerErrorException: <p>The request failed due to an internal server error.</p>
            capo_s3tables.errors.not_found_exception.NotFoundException: <p>The request was rejected because the specified resource could not be found.</p>
            capo_s3tables.errors.too_many_requests_exception.TooManyRequestsException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_s3tables.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_s3tables.types.get_table_bucket_maintenance_configuration_request.GetTableBucketMaintenanceConfigurationRequest]",
        ) -> OperationResponse[
            "capo_s3tables.types.get_table_bucket_maintenance_configuration_response.GetTableBucketMaintenanceConfigurationResponse"
        ]:
            import capo_s3tables._operations.s3_table_buckets.get_table_bucket_maintenance_configuration

            output, http_response = (
                capo_s3tables._operations.s3_table_buckets.get_table_bucket_maintenance_configuration.get_table_bucket_maintenance_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_s3tables.types.get_table_bucket_maintenance_configuration_request.GetTableBucketMaintenanceConfigurationRequest = {
            "table_bucket_arn": table_bucket_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_table_bucket_metrics_configuration(
        self,
        table_bucket_arn: "capo_s3tables.types.table_bucket_arn.TableBucketARN",
        *,
        config_overrides: Optional[S3TablesClientConfig] = None,
    ) -> "capo_s3tables.types.get_table_bucket_metrics_configuration_response.GetTableBucketMetricsConfigurationResponse":
        """<p>Gets the metrics configuration for a table bucket.</p> <dl> <dt>Permissions</dt> <dd> <p>You must have the <code>s3tables:GetTableBucketMetricsConfiguration</code> permission to use this operation.</p> </dd> </dl>

        Args:
            table_bucket_arn: <p>The Amazon Resource Name (ARN) of the table bucket.</p>

        Raises:
            capo_s3tables.errors.bad_request_exception.BadRequestException: <p>The request is invalid or malformed.</p>
            capo_s3tables.errors.conflict_exception.ConflictException: <p>The request failed because there is a conflict with a previous write. You can retry the request.</p>
            capo_s3tables.errors.forbidden_exception.ForbiddenException: <p>The caller isn't authorized to make the request.</p>
            capo_s3tables.errors.internal_server_error_exception.InternalServerErrorException: <p>The request failed due to an internal server error.</p>
            capo_s3tables.errors.not_found_exception.NotFoundException: <p>The request was rejected because the specified resource could not be found.</p>
            capo_s3tables.errors.too_many_requests_exception.TooManyRequestsException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_s3tables.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_s3tables.types.get_table_bucket_metrics_configuration_request.GetTableBucketMetricsConfigurationRequest]",
        ) -> OperationResponse[
            "capo_s3tables.types.get_table_bucket_metrics_configuration_response.GetTableBucketMetricsConfigurationResponse"
        ]:
            import capo_s3tables._operations.s3_table_buckets.get_table_bucket_metrics_configuration

            output, http_response = (
                capo_s3tables._operations.s3_table_buckets.get_table_bucket_metrics_configuration.get_table_bucket_metrics_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_s3tables.types.get_table_bucket_metrics_configuration_request.GetTableBucketMetricsConfigurationRequest = {
            "table_bucket_arn": table_bucket_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_table_bucket_storage_class(
        self,
        table_bucket_arn: "capo_s3tables.types.table_bucket_arn.TableBucketARN",
        *,
        config_overrides: Optional[S3TablesClientConfig] = None,
    ) -> "capo_s3tables.types.get_table_bucket_storage_class_response.GetTableBucketStorageClassResponse":
        """<p>Retrieves the storage class configuration for a specific table. This allows you to view the storage class settings that apply to an individual table, which may differ from the table bucket's default configuration.</p> <dl> <dt>Permissions</dt> <dd> <p>You must have the <code>s3tables:GetTableBucketStorageClass</code> permission to use this operation.</p> </dd> </dl>

        Args:
            table_bucket_arn: <p>The Amazon Resource Name (ARN) of the table bucket.</p>

        Raises:
            capo_s3tables.errors.access_denied_exception.AccessDeniedException: <p>The action cannot be performed because you do not have the required permission.</p>
            capo_s3tables.errors.bad_request_exception.BadRequestException: <p>The request is invalid or malformed.</p>
            capo_s3tables.errors.forbidden_exception.ForbiddenException: <p>The caller isn't authorized to make the request.</p>
            capo_s3tables.errors.internal_server_error_exception.InternalServerErrorException: <p>The request failed due to an internal server error.</p>
            capo_s3tables.errors.not_found_exception.NotFoundException: <p>The request was rejected because the specified resource could not be found.</p>
            capo_s3tables.errors.too_many_requests_exception.TooManyRequestsException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_s3tables.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_s3tables.types.get_table_bucket_storage_class_request.GetTableBucketStorageClassRequest]",
        ) -> OperationResponse[
            "capo_s3tables.types.get_table_bucket_storage_class_response.GetTableBucketStorageClassResponse"
        ]:
            import capo_s3tables._operations.s3_table_buckets.get_table_bucket_storage_class

            output, http_response = (
                capo_s3tables._operations.s3_table_buckets.get_table_bucket_storage_class.get_table_bucket_storage_class(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_s3tables.types.get_table_bucket_storage_class_request.GetTableBucketStorageClassRequest = {
            "table_bucket_arn": table_bucket_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_table_buckets(
        self,
        *,
        config_overrides: Optional[S3TablesClientConfig] = None,
        prefix: Optional[str] = None,
        continuation_token: Optional["capo_s3tables.types.next_token.NextToken"] = None,
        max_buckets: Optional[
            "capo_s3tables.types.list_table_buckets_limit.ListTableBucketsLimit"
        ] = None,
        type: Optional["capo_s3tables.types.table_bucket_type.TableBucketType"] = None,
    ) -> "capo_s3tables.types.list_table_buckets_response.ListTableBucketsResponse":
        """<p>Lists table buckets for your account. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-buckets.html">S3 Table buckets</a> in the <i>Amazon Simple Storage Service User Guide</i>.</p> <dl> <dt>Permissions</dt> <dd> <p>You must have the <code>s3tables:ListTableBuckets</code> permission to use this operation. </p> </dd> </dl>

        Args:
            prefix: <p>The prefix of the table buckets.</p>
            continuation_token: <p> <code>ContinuationToken</code> indicates to Amazon S3 that the list is being continued on this bucket with a token. <code>ContinuationToken</code> is obfuscated and is not a real key. You can use this <code>ContinuationToken</code> for pagination of the list results.</p>
            max_buckets: <p>The maximum number of table buckets to return in the list.</p>
            type: <p>The type of table buckets to filter by in the list.</p>

        Raises:
            capo_s3tables.errors.access_denied_exception.AccessDeniedException: <p>The action cannot be performed because you do not have the required permission.</p>
            capo_s3tables.errors.bad_request_exception.BadRequestException: <p>The request is invalid or malformed.</p>
            capo_s3tables.errors.conflict_exception.ConflictException: <p>The request failed because there is a conflict with a previous write. You can retry the request.</p>
            capo_s3tables.errors.forbidden_exception.ForbiddenException: <p>The caller isn't authorized to make the request.</p>
            capo_s3tables.errors.internal_server_error_exception.InternalServerErrorException: <p>The request failed due to an internal server error.</p>
            capo_s3tables.errors.not_found_exception.NotFoundException: <p>The request was rejected because the specified resource could not be found.</p>
            capo_s3tables.errors.too_many_requests_exception.TooManyRequestsException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_s3tables.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_s3tables.types.list_table_buckets_request.ListTableBucketsRequest]",
        ) -> OperationResponse[
            "capo_s3tables.types.list_table_buckets_response.ListTableBucketsResponse"
        ]:
            import capo_s3tables._operations.s3_table_buckets.list_table_buckets

            output, http_response = (
                capo_s3tables._operations.s3_table_buckets.list_table_buckets.list_table_buckets(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_s3tables.types.list_table_buckets_request.ListTableBucketsRequest = {}
        if prefix is not None:
            input_["prefix"] = prefix
        if continuation_token is not None:
            input_["continuation_token"] = continuation_token
        if max_buckets is not None:
            input_["max_buckets"] = max_buckets
        if type is not None:
            input_["type"] = type

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_table_buckets(
        self,
        *,
        config_overrides: Optional[S3TablesClientConfig] = None,
        prefix: Optional[str] = None,
        continuation_token: Optional["capo_s3tables.types.next_token.NextToken"] = None,
        max_buckets: Optional[
            "capo_s3tables.types.list_table_buckets_limit.ListTableBucketsLimit"
        ] = None,
        type: Optional["capo_s3tables.types.table_bucket_type.TableBucketType"] = None,
    ) -> "Iterator[capo_s3tables.types.table_bucket_summary.TableBucketSummary]":
        _token = continuation_token
        while True:
            _response = self.list_table_buckets(
                config_overrides=config_overrides,
                prefix=prefix,
                continuation_token=_token,
                max_buckets=max_buckets,
                type=type,
            )
            _page = _resolve_path(_response, ("table_buckets",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("continuation_token",))
            if not _token:
                break

    def put_table_bucket_maintenance_configuration(
        self,
        table_bucket_arn: "capo_s3tables.types.table_bucket_arn.TableBucketARN",
        type: "capo_s3tables.types.table_bucket_maintenance_type.TableBucketMaintenanceType",
        value: "capo_s3tables.types.table_bucket_maintenance_configuration_value.TableBucketMaintenanceConfigurationValue",
        *,
        config_overrides: Optional[S3TablesClientConfig] = None,
    ) -> None:
        """<p>Creates a new maintenance configuration or replaces an existing maintenance configuration for a table bucket. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-table-buckets-maintenance.html">Amazon S3 table bucket maintenance</a> in the <i>Amazon Simple Storage Service User Guide</i>.</p> <dl> <dt>Permissions</dt> <dd> <p>You must have the <code>s3tables:PutTableBucketMaintenanceConfiguration</code> permission to use this operation. </p> </dd> </dl>

        Args:
            table_bucket_arn: <p>The Amazon Resource Name (ARN) of the table bucket associated with the maintenance configuration.</p>
            type: <p>The type of the maintenance configuration.</p>
            value: <p>Defines the values of the maintenance configuration for the table bucket.</p>

        Raises:
            capo_s3tables.errors.bad_request_exception.BadRequestException: <p>The request is invalid or malformed.</p>
            capo_s3tables.errors.conflict_exception.ConflictException: <p>The request failed because there is a conflict with a previous write. You can retry the request.</p>
            capo_s3tables.errors.forbidden_exception.ForbiddenException: <p>The caller isn't authorized to make the request.</p>
            capo_s3tables.errors.internal_server_error_exception.InternalServerErrorException: <p>The request failed due to an internal server error.</p>
            capo_s3tables.errors.not_found_exception.NotFoundException: <p>The request was rejected because the specified resource could not be found.</p>
            capo_s3tables.errors.too_many_requests_exception.TooManyRequestsException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_s3tables.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_s3tables.types.put_table_bucket_maintenance_configuration_request.PutTableBucketMaintenanceConfigurationRequest]",
        ) -> OperationResponse[None]:
            import capo_s3tables._operations.s3_table_buckets.put_table_bucket_maintenance_configuration

            output, http_response = (
                capo_s3tables._operations.s3_table_buckets.put_table_bucket_maintenance_configuration.put_table_bucket_maintenance_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_s3tables.types.put_table_bucket_maintenance_configuration_request.PutTableBucketMaintenanceConfigurationRequest = {
            "table_bucket_arn": table_bucket_arn,
            "type": type,
            "value": value,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def put_table_bucket_metrics_configuration(
        self,
        table_bucket_arn: "capo_s3tables.types.table_bucket_arn.TableBucketARN",
        *,
        config_overrides: Optional[S3TablesClientConfig] = None,
    ) -> None:
        """<p>Sets the metrics configuration for a table bucket.</p> <dl> <dt>Permissions</dt> <dd> <p>You must have the <code>s3tables:PutTableBucketMetricsConfiguration</code> permission to use this operation.</p> </dd> </dl>

        Args:
            table_bucket_arn: <p>The Amazon Resource Name (ARN) of the table bucket.</p>

        Raises:
            capo_s3tables.errors.bad_request_exception.BadRequestException: <p>The request is invalid or malformed.</p>
            capo_s3tables.errors.conflict_exception.ConflictException: <p>The request failed because there is a conflict with a previous write. You can retry the request.</p>
            capo_s3tables.errors.forbidden_exception.ForbiddenException: <p>The caller isn't authorized to make the request.</p>
            capo_s3tables.errors.internal_server_error_exception.InternalServerErrorException: <p>The request failed due to an internal server error.</p>
            capo_s3tables.errors.not_found_exception.NotFoundException: <p>The request was rejected because the specified resource could not be found.</p>
            capo_s3tables.errors.too_many_requests_exception.TooManyRequestsException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_s3tables.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_s3tables.types.put_table_bucket_metrics_configuration_request.PutTableBucketMetricsConfigurationRequest]",
        ) -> OperationResponse[None]:
            import capo_s3tables._operations.s3_table_buckets.put_table_bucket_metrics_configuration

            output, http_response = (
                capo_s3tables._operations.s3_table_buckets.put_table_bucket_metrics_configuration.put_table_bucket_metrics_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_s3tables.types.put_table_bucket_metrics_configuration_request.PutTableBucketMetricsConfigurationRequest = {
            "table_bucket_arn": table_bucket_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def put_table_bucket_storage_class(
        self,
        table_bucket_arn: "capo_s3tables.types.table_bucket_arn.TableBucketARN",
        storage_class_configuration: "capo_s3tables.types.storage_class_configuration.StorageClassConfiguration",
        *,
        config_overrides: Optional[S3TablesClientConfig] = None,
    ) -> None:
        """<p>Sets or updates the storage class configuration for a table bucket. This configuration serves as the default storage class for all new tables created in the bucket, allowing you to optimize storage costs at the bucket level.</p> <dl> <dt>Permissions</dt> <dd> <p>You must have the <code>s3tables:PutTableBucketStorageClass</code> permission to use this operation.</p> </dd> </dl>

        Args:
            table_bucket_arn: <p>The Amazon Resource Name (ARN) of the table bucket.</p>
            storage_class_configuration: <p>The storage class configuration to apply to the table bucket. This configuration will serve as the default for new tables created in this bucket.</p>

        Raises:
            capo_s3tables.errors.bad_request_exception.BadRequestException: <p>The request is invalid or malformed.</p>
            capo_s3tables.errors.conflict_exception.ConflictException: <p>The request failed because there is a conflict with a previous write. You can retry the request.</p>
            capo_s3tables.errors.forbidden_exception.ForbiddenException: <p>The caller isn't authorized to make the request.</p>
            capo_s3tables.errors.internal_server_error_exception.InternalServerErrorException: <p>The request failed due to an internal server error.</p>
            capo_s3tables.errors.not_found_exception.NotFoundException: <p>The request was rejected because the specified resource could not be found.</p>
            capo_s3tables.errors.too_many_requests_exception.TooManyRequestsException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_s3tables.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_s3tables.types.put_table_bucket_storage_class_request.PutTableBucketStorageClassRequest]",
        ) -> OperationResponse[None]:
            import capo_s3tables._operations.s3_table_buckets.put_table_bucket_storage_class

            output, http_response = (
                capo_s3tables._operations.s3_table_buckets.put_table_bucket_storage_class.put_table_bucket_storage_class(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_s3tables.types.put_table_bucket_storage_class_request.PutTableBucketStorageClassRequest = {
            "table_bucket_arn": table_bucket_arn,
            "storage_class_configuration": storage_class_configuration,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_table_encryption(
        self,
        table_bucket_arn: "capo_s3tables.types.table_bucket_arn.TableBucketARN",
        namespace: "capo_s3tables.types.namespace_name.NamespaceName",
        name: "capo_s3tables.types.table_name.TableName",
        *,
        config_overrides: Optional[S3TablesClientConfig] = None,
    ) -> "capo_s3tables.types.get_table_encryption_response.GetTableEncryptionResponse":
        """<p>Gets the encryption configuration for a table.</p> <dl> <dt>Permissions</dt> <dd> <p>You must have the <code>s3tables:GetTableEncryption</code> permission to use this operation.</p> </dd> </dl>

        Args:
            table_bucket_arn: <p>The Amazon Resource Name (ARN) of the table bucket containing the table.</p>
            namespace: <p>The namespace associated with the table.</p>
            name: <p>The name of the table.</p>

        Raises:
            capo_s3tables.errors.access_denied_exception.AccessDeniedException: <p>The action cannot be performed because you do not have the required permission.</p>
            capo_s3tables.errors.bad_request_exception.BadRequestException: <p>The request is invalid or malformed.</p>
            capo_s3tables.errors.forbidden_exception.ForbiddenException: <p>The caller isn't authorized to make the request.</p>
            capo_s3tables.errors.internal_server_error_exception.InternalServerErrorException: <p>The request failed due to an internal server error.</p>
            capo_s3tables.errors.not_found_exception.NotFoundException: <p>The request was rejected because the specified resource could not be found.</p>
            capo_s3tables.errors.too_many_requests_exception.TooManyRequestsException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_s3tables.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_s3tables.types.get_table_encryption_request.GetTableEncryptionRequest]",
        ) -> OperationResponse[
            "capo_s3tables.types.get_table_encryption_response.GetTableEncryptionResponse"
        ]:
            import capo_s3tables._operations.s3_table_buckets.get_table_encryption

            output, http_response = (
                capo_s3tables._operations.s3_table_buckets.get_table_encryption.get_table_encryption(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_s3tables.types.get_table_encryption_request.GetTableEncryptionRequest = {
            "table_bucket_arn": table_bucket_arn,
            "namespace": namespace,
            "name": name,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_table_policy(
        self,
        table_bucket_arn: "capo_s3tables.types.table_bucket_arn.TableBucketARN",
        namespace: "capo_s3tables.types.namespace_name.NamespaceName",
        name: "capo_s3tables.types.table_name.TableName",
        *,
        config_overrides: Optional[S3TablesClientConfig] = None,
    ) -> None:
        """<p>Deletes a table policy. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-table-policy.html#table-policy-delete">Deleting a table policy</a> in the <i>Amazon Simple Storage Service User Guide</i>.</p> <dl> <dt>Permissions</dt> <dd> <p>You must have the <code>s3tables:DeleteTablePolicy</code> permission to use this operation. </p> </dd> </dl>

        Args:
            table_bucket_arn: <p>The Amazon Resource Name (ARN) of the table bucket that contains the table.</p>
            namespace: <p>The namespace associated with the table. </p>
            name: <p>The table name.</p>

        Raises:
            capo_s3tables.errors.bad_request_exception.BadRequestException: <p>The request is invalid or malformed.</p>
            capo_s3tables.errors.conflict_exception.ConflictException: <p>The request failed because there is a conflict with a previous write. You can retry the request.</p>
            capo_s3tables.errors.forbidden_exception.ForbiddenException: <p>The caller isn't authorized to make the request.</p>
            capo_s3tables.errors.internal_server_error_exception.InternalServerErrorException: <p>The request failed due to an internal server error.</p>
            capo_s3tables.errors.not_found_exception.NotFoundException: <p>The request was rejected because the specified resource could not be found.</p>
            capo_s3tables.errors.too_many_requests_exception.TooManyRequestsException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_s3tables.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_s3tables.types.delete_table_policy_request.DeleteTablePolicyRequest]",
        ) -> OperationResponse[None]:
            import capo_s3tables._operations.s3_table_buckets.delete_table_policy

            output, http_response = (
                capo_s3tables._operations.s3_table_buckets.delete_table_policy.delete_table_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_s3tables.types.delete_table_policy_request.DeleteTablePolicyRequest = {
            "table_bucket_arn": table_bucket_arn,
            "namespace": namespace,
            "name": name,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_table_policy(
        self,
        table_bucket_arn: "capo_s3tables.types.table_bucket_arn.TableBucketARN",
        namespace: "capo_s3tables.types.namespace_name.NamespaceName",
        name: "capo_s3tables.types.table_name.TableName",
        *,
        config_overrides: Optional[S3TablesClientConfig] = None,
    ) -> "capo_s3tables.types.get_table_policy_response.GetTablePolicyResponse":
        """<p>Gets details about a table policy. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-table-policy.html#table-policy-get">Viewing a table policy</a> in the <i>Amazon Simple Storage Service User Guide</i>.</p> <dl> <dt>Permissions</dt> <dd> <p>You must have the <code>s3tables:GetTablePolicy</code> permission to use this operation. </p> </dd> </dl>

        Args:
            table_bucket_arn: <p>The Amazon Resource Name (ARN) of the table bucket that contains the table.</p>
            namespace: <p>The namespace associated with the table.</p>
            name: <p>The name of the table.</p>

        Raises:
            capo_s3tables.errors.bad_request_exception.BadRequestException: <p>The request is invalid or malformed.</p>
            capo_s3tables.errors.conflict_exception.ConflictException: <p>The request failed because there is a conflict with a previous write. You can retry the request.</p>
            capo_s3tables.errors.forbidden_exception.ForbiddenException: <p>The caller isn't authorized to make the request.</p>
            capo_s3tables.errors.internal_server_error_exception.InternalServerErrorException: <p>The request failed due to an internal server error.</p>
            capo_s3tables.errors.not_found_exception.NotFoundException: <p>The request was rejected because the specified resource could not be found.</p>
            capo_s3tables.errors.too_many_requests_exception.TooManyRequestsException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_s3tables.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_s3tables.types.get_table_policy_request.GetTablePolicyRequest]",
        ) -> OperationResponse[
            "capo_s3tables.types.get_table_policy_response.GetTablePolicyResponse"
        ]:
            import capo_s3tables._operations.s3_table_buckets.get_table_policy

            output, http_response = (
                capo_s3tables._operations.s3_table_buckets.get_table_policy.get_table_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_s3tables.types.get_table_policy_request.GetTablePolicyRequest = {
            "table_bucket_arn": table_bucket_arn,
            "namespace": namespace,
            "name": name,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def put_table_policy(
        self,
        table_bucket_arn: "capo_s3tables.types.table_bucket_arn.TableBucketARN",
        namespace: "capo_s3tables.types.namespace_name.NamespaceName",
        name: "capo_s3tables.types.table_name.TableName",
        resource_policy: "capo_s3tables.types.resource_policy.ResourcePolicy",
        *,
        config_overrides: Optional[S3TablesClientConfig] = None,
    ) -> None:
        """<p>Creates a new table policy or replaces an existing table policy for a table. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-table-policy.html#table-policy-add">Adding a table policy</a> in the <i>Amazon Simple Storage Service User Guide</i>. </p> <dl> <dt>Permissions</dt> <dd> <p>You must have the <code>s3tables:PutTablePolicy</code> permission to use this operation. </p> </dd> </dl>

        Args:
            table_bucket_arn: <p>The Amazon Resource Name (ARN) of the table bucket that contains the table.</p>
            namespace: <p>The namespace associated with the table.</p>
            name: <p>The name of the table.</p>
            resource_policy: <p>The <code>JSON</code> that defines the policy.</p>

        Raises:
            capo_s3tables.errors.bad_request_exception.BadRequestException: <p>The request is invalid or malformed.</p>
            capo_s3tables.errors.conflict_exception.ConflictException: <p>The request failed because there is a conflict with a previous write. You can retry the request.</p>
            capo_s3tables.errors.forbidden_exception.ForbiddenException: <p>The caller isn't authorized to make the request.</p>
            capo_s3tables.errors.internal_server_error_exception.InternalServerErrorException: <p>The request failed due to an internal server error.</p>
            capo_s3tables.errors.not_found_exception.NotFoundException: <p>The request was rejected because the specified resource could not be found.</p>
            capo_s3tables.errors.too_many_requests_exception.TooManyRequestsException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_s3tables.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_s3tables.types.put_table_policy_request.PutTablePolicyRequest]",
        ) -> OperationResponse[None]:
            import capo_s3tables._operations.s3_table_buckets.put_table_policy

            output, http_response = (
                capo_s3tables._operations.s3_table_buckets.put_table_policy.put_table_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_s3tables.types.put_table_policy_request.PutTablePolicyRequest = {
            "table_bucket_arn": table_bucket_arn,
            "namespace": namespace,
            "name": name,
            "resource_policy": resource_policy,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_table_replication(
        self,
        table_arn: "capo_s3tables.types.table_arn.TableARN",
        version_token: str,
        *,
        config_overrides: Optional[S3TablesClientConfig] = None,
    ) -> None:
        """<p>Deletes the replication configuration for a specific table. After deletion, new updates to this table will no longer be replicated to destination tables, though existing replicated copies will remain in destination buckets.</p> <dl> <dt>Permissions</dt> <dd> <p>You must have the <code>s3tables:DeleteTableReplication</code> permission to use this operation.</p> </dd> </dl>

        Args:
            table_arn: <p>The Amazon Resource Name (ARN) of the table.</p>
            version_token: <p>A version token from a previous GetTableReplication call. Use this token to ensure you're deleting the expected version of the configuration.</p>

        Raises:
            capo_s3tables.errors.access_denied_exception.AccessDeniedException: <p>The action cannot be performed because you do not have the required permission.</p>
            capo_s3tables.errors.bad_request_exception.BadRequestException: <p>The request is invalid or malformed.</p>
            capo_s3tables.errors.conflict_exception.ConflictException: <p>The request failed because there is a conflict with a previous write. You can retry the request.</p>
            capo_s3tables.errors.forbidden_exception.ForbiddenException: <p>The caller isn't authorized to make the request.</p>
            capo_s3tables.errors.internal_server_error_exception.InternalServerErrorException: <p>The request failed due to an internal server error.</p>
            capo_s3tables.errors.not_found_exception.NotFoundException: <p>The request was rejected because the specified resource could not be found.</p>
            capo_s3tables.errors.too_many_requests_exception.TooManyRequestsException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_s3tables.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_s3tables.types.delete_table_replication_request.DeleteTableReplicationRequest]",
        ) -> OperationResponse[None]:
            import capo_s3tables._operations.s3_table_buckets.delete_table_replication

            output, http_response = (
                capo_s3tables._operations.s3_table_buckets.delete_table_replication.delete_table_replication(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_s3tables.types.delete_table_replication_request.DeleteTableReplicationRequest = {
            "table_arn": table_arn,
            "version_token": version_token,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_table_replication(
        self,
        table_arn: "capo_s3tables.types.table_arn.TableARN",
        *,
        config_overrides: Optional[S3TablesClientConfig] = None,
    ) -> (
        "capo_s3tables.types.get_table_replication_response.GetTableReplicationResponse"
    ):
        """<p>Retrieves the replication configuration for a specific table.</p> <dl> <dt>Permissions</dt> <dd> <p>You must have the <code>s3tables:GetTableReplication</code> permission to use this operation.</p> </dd> </dl>

        Args:
            table_arn: <p>The Amazon Resource Name (ARN) of the table.</p>

        Raises:
            capo_s3tables.errors.access_denied_exception.AccessDeniedException: <p>The action cannot be performed because you do not have the required permission.</p>
            capo_s3tables.errors.bad_request_exception.BadRequestException: <p>The request is invalid or malformed.</p>
            capo_s3tables.errors.conflict_exception.ConflictException: <p>The request failed because there is a conflict with a previous write. You can retry the request.</p>
            capo_s3tables.errors.forbidden_exception.ForbiddenException: <p>The caller isn't authorized to make the request.</p>
            capo_s3tables.errors.internal_server_error_exception.InternalServerErrorException: <p>The request failed due to an internal server error.</p>
            capo_s3tables.errors.not_found_exception.NotFoundException: <p>The request was rejected because the specified resource could not be found.</p>
            capo_s3tables.errors.too_many_requests_exception.TooManyRequestsException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_s3tables.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_s3tables.types.get_table_replication_request.GetTableReplicationRequest]",
        ) -> OperationResponse[
            "capo_s3tables.types.get_table_replication_response.GetTableReplicationResponse"
        ]:
            import capo_s3tables._operations.s3_table_buckets.get_table_replication

            output, http_response = (
                capo_s3tables._operations.s3_table_buckets.get_table_replication.get_table_replication(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_s3tables.types.get_table_replication_request.GetTableReplicationRequest = {
            "table_arn": table_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_table_replication_status(
        self,
        table_arn: "capo_s3tables.types.table_arn.TableARN",
        *,
        config_overrides: Optional[S3TablesClientConfig] = None,
    ) -> "capo_s3tables.types.get_table_replication_status_response.GetTableReplicationStatusResponse":
        """<p>Retrieves the replication status for a table, including the status of replication to each destination. This operation provides visibility into replication health and progress.</p> <dl> <dt>Permissions</dt> <dd> <p>You must have the <code>s3tables:GetTableReplicationStatus</code> permission to use this operation.</p> </dd> </dl>

        Args:
            table_arn: <p>The Amazon Resource Name (ARN) of the table.</p>

        Raises:
            capo_s3tables.errors.bad_request_exception.BadRequestException: <p>The request is invalid or malformed.</p>
            capo_s3tables.errors.conflict_exception.ConflictException: <p>The request failed because there is a conflict with a previous write. You can retry the request.</p>
            capo_s3tables.errors.forbidden_exception.ForbiddenException: <p>The caller isn't authorized to make the request.</p>
            capo_s3tables.errors.internal_server_error_exception.InternalServerErrorException: <p>The request failed due to an internal server error.</p>
            capo_s3tables.errors.not_found_exception.NotFoundException: <p>The request was rejected because the specified resource could not be found.</p>
            capo_s3tables.errors.too_many_requests_exception.TooManyRequestsException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_s3tables.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_s3tables.types.get_table_replication_status_request.GetTableReplicationStatusRequest]",
        ) -> OperationResponse[
            "capo_s3tables.types.get_table_replication_status_response.GetTableReplicationStatusResponse"
        ]:
            import capo_s3tables._operations.s3_table_buckets.get_table_replication_status

            output, http_response = (
                capo_s3tables._operations.s3_table_buckets.get_table_replication_status.get_table_replication_status(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_s3tables.types.get_table_replication_status_request.GetTableReplicationStatusRequest = {
            "table_arn": table_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def put_table_replication(
        self,
        table_arn: "capo_s3tables.types.table_arn.TableARN",
        configuration: "capo_s3tables.types.table_replication_configuration.TableReplicationConfiguration",
        *,
        config_overrides: Optional[S3TablesClientConfig] = None,
        version_token: Optional[str] = None,
    ) -> (
        "capo_s3tables.types.put_table_replication_response.PutTableReplicationResponse"
    ):
        """<p>Creates or updates the replication configuration for a specific table. This operation allows you to define table-level replication independently of bucket-level replication, providing granular control over which tables are replicated and where.</p> <dl> <dt>Permissions</dt> <dd> <ul> <li> <p>You must have the <code>s3tables:PutTableReplication</code> permission to use this operation. The IAM role specified in the configuration must have permissions to read from the source table and write to all destination tables.</p> </li> <li> <p>You must also have the following permissions:</p> <ul> <li> <p> <code>s3tables:GetTable</code> permission on the source table being replicated.</p> </li> <li> <p> <code>s3tables:CreateTable</code> permission for the destination.</p> </li> <li> <p> <code>s3tables:CreateNamespace</code> permission for the destination.</p> </li> <li> <p> <code>s3tables:GetTableMaintenanceConfig</code> permission for the source table.</p> </li> <li> <p> <code>s3tables:PutTableMaintenanceConfig</code> permission for the destination table.</p> </li> </ul> </li> <li> <p>You must have <code>iam:PassRole</code> permission with condition allowing roles to be passed to <code>replication.s3tables.amazonaws.com</code>.</p> </li> </ul> </dd> </dl>

        Args:
            table_arn: <p>The Amazon Resource Name (ARN) of the source table.</p>
            version_token: <p>A version token from a previous GetTableReplication call. Use this token to ensure you're updating the expected version of the configuration.</p>
            configuration: <p>The replication configuration to apply to the table, including the IAM role and replication rules.</p>

        Raises:
            capo_s3tables.errors.access_denied_exception.AccessDeniedException: <p>The action cannot be performed because you do not have the required permission.</p>
            capo_s3tables.errors.bad_request_exception.BadRequestException: <p>The request is invalid or malformed.</p>
            capo_s3tables.errors.conflict_exception.ConflictException: <p>The request failed because there is a conflict with a previous write. You can retry the request.</p>
            capo_s3tables.errors.forbidden_exception.ForbiddenException: <p>The caller isn't authorized to make the request.</p>
            capo_s3tables.errors.internal_server_error_exception.InternalServerErrorException: <p>The request failed due to an internal server error.</p>
            capo_s3tables.errors.not_found_exception.NotFoundException: <p>The request was rejected because the specified resource could not be found.</p>
            capo_s3tables.errors.too_many_requests_exception.TooManyRequestsException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_s3tables.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_s3tables.types.put_table_replication_request.PutTableReplicationRequest]",
        ) -> OperationResponse[
            "capo_s3tables.types.put_table_replication_response.PutTableReplicationResponse"
        ]:
            import capo_s3tables._operations.s3_table_buckets.put_table_replication

            output, http_response = (
                capo_s3tables._operations.s3_table_buckets.put_table_replication.put_table_replication(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_s3tables.types.put_table_replication_request.PutTableReplicationRequest = {
            "table_arn": table_arn,
            "configuration": configuration,
        }
        if version_token is not None:
            input_["version_token"] = version_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_table(
        self,
        table_bucket_arn: "capo_s3tables.types.table_bucket_arn.TableBucketARN",
        namespace: "capo_s3tables.types.namespace_name.NamespaceName",
        name: "capo_s3tables.types.table_name.TableName",
        format: "capo_s3tables.types.open_table_format.OpenTableFormat",
        *,
        config_overrides: Optional[S3TablesClientConfig] = None,
        metadata: Optional["capo_s3tables.types.table_metadata.TableMetadata"] = None,
        encryption_configuration: Optional[
            "capo_s3tables.types.encryption_configuration.EncryptionConfiguration"
        ] = None,
        storage_class_configuration: Optional[
            "capo_s3tables.types.storage_class_configuration.StorageClassConfiguration"
        ] = None,
        tags: Optional["capo_s3tables.types.tags.Tags"] = None,
    ) -> "capo_s3tables.types.create_table_response.CreateTableResponse":
        """<p>Creates a new table associated with the given namespace in a table bucket. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-create.html">Creating an Amazon S3 table</a> in the <i>Amazon Simple Storage Service User Guide</i>.</p> <dl> <dt>Permissions</dt> <dd> <ul> <li> <p>You must have the <code>s3tables:CreateTable</code> permission to use this operation. </p> </li> <li> <p>If you use this operation with the optional <code>metadata</code> request parameter you must have the <code>s3tables:PutTableData</code> permission. </p> </li> <li> <p>If you use this operation with the optional <code>encryptionConfiguration</code> request parameter you must have the <code>s3tables:PutTableEncryption</code> permission. </p> </li> <li> <p>If you use this operation with the <code>storageClassConfiguration</code> request parameter, you must have the <code>s3tables:PutTableStorageClass</code> permission.</p> </li> <li> <p>To create a table with tags, you must have the <code>s3tables:TagResource</code> permission in addition to <code>s3tables:CreateTable</code> permission.</p> </li> </ul> <note> <p>Additionally, If you choose SSE-KMS encryption you must grant the S3 Tables maintenance principal access to your KMS key. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-kms-permissions.html">Permissions requirements for S3 Tables SSE-KMS encryption</a>. </p> </note> </dd> </dl>

        Args:
            table_bucket_arn: <p>The Amazon Resource Name (ARN) of the table bucket to create the table in.</p>
            namespace: <p>The namespace to associated with the table.</p>
            name: <p>The name for the table.</p>
            format: <p>The format for the table.</p>
            metadata: <p>The metadata for the table.</p>
            encryption_configuration: <p>The encryption configuration to use for the table. This configuration specifies the encryption algorithm and, if using SSE-KMS, the KMS key to use for encrypting the table. </p> <note> <p>If you choose SSE-KMS encryption you must grant the S3 Tables maintenance principal access to your KMS key. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-kms-permissions.html">Permissions requirements for S3 Tables SSE-KMS encryption</a>.</p> </note>
            storage_class_configuration: <p>The storage class configuration for the table. If not specified, the table inherits the storage class configuration from its table bucket. Specify this parameter to override the bucket's default storage class for this table.</p>
            tags: <p>A map of user-defined tags that you would like to apply to the table that you are creating. A tag is a key-value pair that you apply to your resources. Tags can help you organize, track costs for, and control access to resources. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/tagging.html">Tagging for cost allocation or attribute-based access control (ABAC)</a>.</p> <note> <p>You must have the <code>s3tables:TagResource</code> permission in addition to <code>s3tables:CreateTable</code> permission to create a table with tags.</p> </note>

        Raises:
            capo_s3tables.errors.bad_request_exception.BadRequestException: <p>The request is invalid or malformed.</p>
            capo_s3tables.errors.conflict_exception.ConflictException: <p>The request failed because there is a conflict with a previous write. You can retry the request.</p>
            capo_s3tables.errors.forbidden_exception.ForbiddenException: <p>The caller isn't authorized to make the request.</p>
            capo_s3tables.errors.internal_server_error_exception.InternalServerErrorException: <p>The request failed due to an internal server error.</p>
            capo_s3tables.errors.not_found_exception.NotFoundException: <p>The request was rejected because the specified resource could not be found.</p>
            capo_s3tables.errors.too_many_requests_exception.TooManyRequestsException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_s3tables.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_s3tables.types.create_table_request.CreateTableRequest]",
        ) -> OperationResponse[
            "capo_s3tables.types.create_table_response.CreateTableResponse"
        ]:
            import capo_s3tables._operations.s3_table_buckets.create_table

            output, http_response = (
                capo_s3tables._operations.s3_table_buckets.create_table.create_table(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_s3tables.types.create_table_request.CreateTableRequest = {
            "table_bucket_arn": table_bucket_arn,
            "namespace": namespace,
            "name": name,
            "format": format,
        }
        if metadata is not None:
            input_["metadata"] = metadata
        if encryption_configuration is not None:
            input_["encryption_configuration"] = encryption_configuration
        if storage_class_configuration is not None:
            input_["storage_class_configuration"] = storage_class_configuration
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_table(
        self,
        table_bucket_arn: "capo_s3tables.types.table_bucket_arn.TableBucketARN",
        namespace: "capo_s3tables.types.namespace_name.NamespaceName",
        name: "capo_s3tables.types.table_name.TableName",
        *,
        config_overrides: Optional[S3TablesClientConfig] = None,
        version_token: Optional[
            "capo_s3tables.types.version_token.VersionToken"
        ] = None,
    ) -> None:
        """<p>Deletes a table. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-delete.html">Deleting an Amazon S3 table</a> in the <i>Amazon Simple Storage Service User Guide</i>.</p> <dl> <dt>Permissions</dt> <dd> <p>You must have the <code>s3tables:DeleteTable</code> permission to use this operation. </p> </dd> </dl>

        Args:
            table_bucket_arn: <p>The Amazon Resource Name (ARN) of the table bucket that contains the table.</p>
            namespace: <p>The namespace associated with the table.</p>
            name: <p>The name of the table.</p>
            version_token: <p>The version token of the table.</p>

        Raises:
            capo_s3tables.errors.bad_request_exception.BadRequestException: <p>The request is invalid or malformed.</p>
            capo_s3tables.errors.conflict_exception.ConflictException: <p>The request failed because there is a conflict with a previous write. You can retry the request.</p>
            capo_s3tables.errors.forbidden_exception.ForbiddenException: <p>The caller isn't authorized to make the request.</p>
            capo_s3tables.errors.internal_server_error_exception.InternalServerErrorException: <p>The request failed due to an internal server error.</p>
            capo_s3tables.errors.not_found_exception.NotFoundException: <p>The request was rejected because the specified resource could not be found.</p>
            capo_s3tables.errors.too_many_requests_exception.TooManyRequestsException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_s3tables.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_s3tables.types.delete_table_request.DeleteTableRequest]",
        ) -> OperationResponse[None]:
            import capo_s3tables._operations.s3_table_buckets.delete_table

            output, http_response = (
                capo_s3tables._operations.s3_table_buckets.delete_table.delete_table(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_s3tables.types.delete_table_request.DeleteTableRequest = {
            "table_bucket_arn": table_bucket_arn,
            "namespace": namespace,
            "name": name,
        }
        if version_token is not None:
            input_["version_token"] = version_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_table(
        self,
        *,
        config_overrides: Optional[S3TablesClientConfig] = None,
        table_bucket_arn: Optional[
            "capo_s3tables.types.table_bucket_arn.TableBucketARN"
        ] = None,
        namespace: Optional["capo_s3tables.types.namespace_name.NamespaceName"] = None,
        name: Optional["capo_s3tables.types.table_name.TableName"] = None,
        table_arn: Optional["capo_s3tables.types.table_arn.TableARN"] = None,
    ) -> "capo_s3tables.types.get_table_response.GetTableResponse":
        """<p>Gets details about a table. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-tables.html">S3 Tables</a> in the <i>Amazon Simple Storage Service User Guide</i>.</p> <dl> <dt>Permissions</dt> <dd> <p>You must have the <code>s3tables:GetTable</code> permission to use this operation. </p> </dd> </dl>

        Args:
            table_bucket_arn: <p>The Amazon Resource Name (ARN) of the table bucket associated with the table.</p>
            namespace: <p>The name of the namespace the table is associated with.</p>
            name: <p>The name of the table.</p>
            table_arn: <p>The Amazon Resource Name (ARN) of the table.</p>

        Raises:
            capo_s3tables.errors.access_denied_exception.AccessDeniedException: <p>The action cannot be performed because you do not have the required permission.</p>
            capo_s3tables.errors.bad_request_exception.BadRequestException: <p>The request is invalid or malformed.</p>
            capo_s3tables.errors.conflict_exception.ConflictException: <p>The request failed because there is a conflict with a previous write. You can retry the request.</p>
            capo_s3tables.errors.forbidden_exception.ForbiddenException: <p>The caller isn't authorized to make the request.</p>
            capo_s3tables.errors.internal_server_error_exception.InternalServerErrorException: <p>The request failed due to an internal server error.</p>
            capo_s3tables.errors.not_found_exception.NotFoundException: <p>The request was rejected because the specified resource could not be found.</p>
            capo_s3tables.errors.too_many_requests_exception.TooManyRequestsException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_s3tables.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_s3tables.types.get_table_request.GetTableRequest]",
        ) -> OperationResponse[
            "capo_s3tables.types.get_table_response.GetTableResponse"
        ]:
            import capo_s3tables._operations.s3_table_buckets.get_table

            output, http_response = (
                capo_s3tables._operations.s3_table_buckets.get_table.get_table(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_s3tables.types.get_table_request.GetTableRequest = {}
        if table_bucket_arn is not None:
            input_["table_bucket_arn"] = table_bucket_arn
        if namespace is not None:
            input_["namespace"] = namespace
        if name is not None:
            input_["name"] = name
        if table_arn is not None:
            input_["table_arn"] = table_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_table_maintenance_configuration(
        self,
        table_bucket_arn: "capo_s3tables.types.table_bucket_arn.TableBucketARN",
        namespace: "capo_s3tables.types.namespace_name.NamespaceName",
        name: "capo_s3tables.types.table_name.TableName",
        *,
        config_overrides: Optional[S3TablesClientConfig] = None,
    ) -> "capo_s3tables.types.get_table_maintenance_configuration_response.GetTableMaintenanceConfigurationResponse":
        """<p>Gets details about the maintenance configuration of a table. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-maintenance.html">S3 Tables maintenance</a> in the <i>Amazon Simple Storage Service User Guide</i>.</p> <dl> <dt>Permissions</dt> <dd> <ul> <li> <p>You must have the <code>s3tables:GetTableMaintenanceConfiguration</code> permission to use this operation. </p> </li> <li> <p>You must have the <code>s3tables:GetTableData</code> permission to use set the compaction strategy to <code>sort</code> or <code>zorder</code>.</p> </li> </ul> </dd> </dl>

        Args:
            table_bucket_arn: <p>The Amazon Resource Name (ARN) of the table bucket.</p>
            namespace: <p>The namespace associated with the table.</p>
            name: <p>The name of the table.</p>

        Raises:
            capo_s3tables.errors.bad_request_exception.BadRequestException: <p>The request is invalid or malformed.</p>
            capo_s3tables.errors.conflict_exception.ConflictException: <p>The request failed because there is a conflict with a previous write. You can retry the request.</p>
            capo_s3tables.errors.forbidden_exception.ForbiddenException: <p>The caller isn't authorized to make the request.</p>
            capo_s3tables.errors.internal_server_error_exception.InternalServerErrorException: <p>The request failed due to an internal server error.</p>
            capo_s3tables.errors.not_found_exception.NotFoundException: <p>The request was rejected because the specified resource could not be found.</p>
            capo_s3tables.errors.too_many_requests_exception.TooManyRequestsException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_s3tables.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_s3tables.types.get_table_maintenance_configuration_request.GetTableMaintenanceConfigurationRequest]",
        ) -> OperationResponse[
            "capo_s3tables.types.get_table_maintenance_configuration_response.GetTableMaintenanceConfigurationResponse"
        ]:
            import capo_s3tables._operations.s3_table_buckets.get_table_maintenance_configuration

            output, http_response = (
                capo_s3tables._operations.s3_table_buckets.get_table_maintenance_configuration.get_table_maintenance_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_s3tables.types.get_table_maintenance_configuration_request.GetTableMaintenanceConfigurationRequest = {
            "table_bucket_arn": table_bucket_arn,
            "namespace": namespace,
            "name": name,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_table_maintenance_job_status(
        self,
        table_bucket_arn: "capo_s3tables.types.table_bucket_arn.TableBucketARN",
        namespace: "capo_s3tables.types.namespace_name.NamespaceName",
        name: "capo_s3tables.types.table_name.TableName",
        *,
        config_overrides: Optional[S3TablesClientConfig] = None,
    ) -> "capo_s3tables.types.get_table_maintenance_job_status_response.GetTableMaintenanceJobStatusResponse":
        """<p>Gets the status of a maintenance job for a table. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-maintenance.html">S3 Tables maintenance</a> in the <i>Amazon Simple Storage Service User Guide</i>.</p> <dl> <dt>Permissions</dt> <dd> <p>You must have the <code>s3tables:GetTableMaintenanceJobStatus</code> permission to use this operation. </p> </dd> </dl>

        Args:
            table_bucket_arn: <p>The Amazon Resource Name (ARN) of the table bucket.</p>
            namespace: <p>The name of the namespace the table is associated with. </p>
            name: <p>The name of the table containing the maintenance job status you want to check.</p>

        Raises:
            capo_s3tables.errors.bad_request_exception.BadRequestException: <p>The request is invalid or malformed.</p>
            capo_s3tables.errors.conflict_exception.ConflictException: <p>The request failed because there is a conflict with a previous write. You can retry the request.</p>
            capo_s3tables.errors.forbidden_exception.ForbiddenException: <p>The caller isn't authorized to make the request.</p>
            capo_s3tables.errors.internal_server_error_exception.InternalServerErrorException: <p>The request failed due to an internal server error.</p>
            capo_s3tables.errors.not_found_exception.NotFoundException: <p>The request was rejected because the specified resource could not be found.</p>
            capo_s3tables.errors.too_many_requests_exception.TooManyRequestsException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_s3tables.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_s3tables.types.get_table_maintenance_job_status_request.GetTableMaintenanceJobStatusRequest]",
        ) -> OperationResponse[
            "capo_s3tables.types.get_table_maintenance_job_status_response.GetTableMaintenanceJobStatusResponse"
        ]:
            import capo_s3tables._operations.s3_table_buckets.get_table_maintenance_job_status

            output, http_response = (
                capo_s3tables._operations.s3_table_buckets.get_table_maintenance_job_status.get_table_maintenance_job_status(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_s3tables.types.get_table_maintenance_job_status_request.GetTableMaintenanceJobStatusRequest = {
            "table_bucket_arn": table_bucket_arn,
            "namespace": namespace,
            "name": name,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_table_metadata_location(
        self,
        table_bucket_arn: "capo_s3tables.types.table_bucket_arn.TableBucketARN",
        namespace: "capo_s3tables.types.namespace_name.NamespaceName",
        name: "capo_s3tables.types.table_name.TableName",
        *,
        config_overrides: Optional[S3TablesClientConfig] = None,
    ) -> "capo_s3tables.types.get_table_metadata_location_response.GetTableMetadataLocationResponse":
        """<p>Gets the location of the table metadata.</p> <dl> <dt>Permissions</dt> <dd> <p>You must have the <code>s3tables:GetTableMetadataLocation</code> permission to use this operation. </p> </dd> </dl>

        Args:
            table_bucket_arn: <p>The Amazon Resource Name (ARN) of the table bucket.</p>
            namespace: <p>The namespace of the table.</p>
            name: <p>The name of the table.</p>

        Raises:
            capo_s3tables.errors.bad_request_exception.BadRequestException: <p>The request is invalid or malformed.</p>
            capo_s3tables.errors.conflict_exception.ConflictException: <p>The request failed because there is a conflict with a previous write. You can retry the request.</p>
            capo_s3tables.errors.forbidden_exception.ForbiddenException: <p>The caller isn't authorized to make the request.</p>
            capo_s3tables.errors.internal_server_error_exception.InternalServerErrorException: <p>The request failed due to an internal server error.</p>
            capo_s3tables.errors.not_found_exception.NotFoundException: <p>The request was rejected because the specified resource could not be found.</p>
            capo_s3tables.errors.too_many_requests_exception.TooManyRequestsException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_s3tables.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_s3tables.types.get_table_metadata_location_request.GetTableMetadataLocationRequest]",
        ) -> OperationResponse[
            "capo_s3tables.types.get_table_metadata_location_response.GetTableMetadataLocationResponse"
        ]:
            import capo_s3tables._operations.s3_table_buckets.get_table_metadata_location

            output, http_response = (
                capo_s3tables._operations.s3_table_buckets.get_table_metadata_location.get_table_metadata_location(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_s3tables.types.get_table_metadata_location_request.GetTableMetadataLocationRequest = {
            "table_bucket_arn": table_bucket_arn,
            "namespace": namespace,
            "name": name,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_table_record_expiration_configuration(
        self,
        table_arn: "capo_s3tables.types.table_arn.TableARN",
        *,
        config_overrides: Optional[S3TablesClientConfig] = None,
    ) -> "capo_s3tables.types.get_table_record_expiration_configuration_response.GetTableRecordExpirationConfigurationResponse":
        """<p>Retrieves the expiration configuration settings for records in a table, and the status of the configuration. If the status of the configuration is <code>enabled</code>, records expire and are automatically removed from the table after the specified number of days.</p> <dl> <dt>Permissions</dt> <dd> <p>You must have the <code>s3tables:GetTableRecordExpirationConfiguration</code> permission to use this operation.</p> </dd> </dl>

        Args:
            table_arn: <p>The Amazon Resource Name (ARN) of the table.</p>

        Raises:
            capo_s3tables.errors.bad_request_exception.BadRequestException: <p>The request is invalid or malformed.</p>
            capo_s3tables.errors.forbidden_exception.ForbiddenException: <p>The caller isn't authorized to make the request.</p>
            capo_s3tables.errors.internal_server_error_exception.InternalServerErrorException: <p>The request failed due to an internal server error.</p>
            capo_s3tables.errors.method_not_allowed_exception.MethodNotAllowedException: <p>The requested operation is not allowed on this resource. This may occur when attempting to modify a resource that is managed by a service or has restrictions that prevent the operation.</p>
            capo_s3tables.errors.not_found_exception.NotFoundException: <p>The request was rejected because the specified resource could not be found.</p>
            capo_s3tables.errors.too_many_requests_exception.TooManyRequestsException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_s3tables.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_s3tables.types.get_table_record_expiration_configuration_request.GetTableRecordExpirationConfigurationRequest]",
        ) -> OperationResponse[
            "capo_s3tables.types.get_table_record_expiration_configuration_response.GetTableRecordExpirationConfigurationResponse"
        ]:
            import capo_s3tables._operations.s3_table_buckets.get_table_record_expiration_configuration

            output, http_response = (
                capo_s3tables._operations.s3_table_buckets.get_table_record_expiration_configuration.get_table_record_expiration_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_s3tables.types.get_table_record_expiration_configuration_request.GetTableRecordExpirationConfigurationRequest = {
            "table_arn": table_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_table_record_expiration_job_status(
        self,
        table_arn: "capo_s3tables.types.table_arn.TableARN",
        *,
        config_overrides: Optional[S3TablesClientConfig] = None,
    ) -> "capo_s3tables.types.get_table_record_expiration_job_status_response.GetTableRecordExpirationJobStatusResponse":
        """<p>Retrieves the status, metrics, and details of the latest record expiration job for a table. This includes when the job ran, and whether it succeeded or failed. If the job ran successfully, this also includes statistics about the records that were removed.</p> <dl> <dt>Permissions</dt> <dd> <p>You must have the <code>s3tables:GetTableRecordExpirationJobStatus</code> permission to use this operation.</p> </dd> </dl>

        Args:
            table_arn: <p>The Amazon Resource Name (ARN) of the table.</p>

        Raises:
            capo_s3tables.errors.bad_request_exception.BadRequestException: <p>The request is invalid or malformed.</p>
            capo_s3tables.errors.forbidden_exception.ForbiddenException: <p>The caller isn't authorized to make the request.</p>
            capo_s3tables.errors.internal_server_error_exception.InternalServerErrorException: <p>The request failed due to an internal server error.</p>
            capo_s3tables.errors.method_not_allowed_exception.MethodNotAllowedException: <p>The requested operation is not allowed on this resource. This may occur when attempting to modify a resource that is managed by a service or has restrictions that prevent the operation.</p>
            capo_s3tables.errors.not_found_exception.NotFoundException: <p>The request was rejected because the specified resource could not be found.</p>
            capo_s3tables.errors.too_many_requests_exception.TooManyRequestsException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_s3tables.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_s3tables.types.get_table_record_expiration_job_status_request.GetTableRecordExpirationJobStatusRequest]",
        ) -> OperationResponse[
            "capo_s3tables.types.get_table_record_expiration_job_status_response.GetTableRecordExpirationJobStatusResponse"
        ]:
            import capo_s3tables._operations.s3_table_buckets.get_table_record_expiration_job_status

            output, http_response = (
                capo_s3tables._operations.s3_table_buckets.get_table_record_expiration_job_status.get_table_record_expiration_job_status(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_s3tables.types.get_table_record_expiration_job_status_request.GetTableRecordExpirationJobStatusRequest = {
            "table_arn": table_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_table_storage_class(
        self,
        table_bucket_arn: "capo_s3tables.types.table_bucket_arn.TableBucketARN",
        namespace: "capo_s3tables.types.namespace_name.NamespaceName",
        name: "capo_s3tables.types.table_name.TableName",
        *,
        config_overrides: Optional[S3TablesClientConfig] = None,
    ) -> "capo_s3tables.types.get_table_storage_class_response.GetTableStorageClassResponse":
        """<p>Retrieves the storage class configuration for a specific table. This allows you to view the storage class settings that apply to an individual table, which may differ from the table bucket's default configuration.</p> <dl> <dt>Permissions</dt> <dd> <p>You must have the <code>s3tables:GetTableStorageClass</code> permission to use this operation.</p> </dd> </dl>

        Args:
            table_bucket_arn: <p>The Amazon Resource Name (ARN) of the table bucket that contains the table.</p>
            namespace: <p>The namespace associated with the table.</p>
            name: <p>The name of the table.</p>

        Raises:
            capo_s3tables.errors.access_denied_exception.AccessDeniedException: <p>The action cannot be performed because you do not have the required permission.</p>
            capo_s3tables.errors.bad_request_exception.BadRequestException: <p>The request is invalid or malformed.</p>
            capo_s3tables.errors.forbidden_exception.ForbiddenException: <p>The caller isn't authorized to make the request.</p>
            capo_s3tables.errors.internal_server_error_exception.InternalServerErrorException: <p>The request failed due to an internal server error.</p>
            capo_s3tables.errors.not_found_exception.NotFoundException: <p>The request was rejected because the specified resource could not be found.</p>
            capo_s3tables.errors.too_many_requests_exception.TooManyRequestsException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_s3tables.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_s3tables.types.get_table_storage_class_request.GetTableStorageClassRequest]",
        ) -> OperationResponse[
            "capo_s3tables.types.get_table_storage_class_response.GetTableStorageClassResponse"
        ]:
            import capo_s3tables._operations.s3_table_buckets.get_table_storage_class

            output, http_response = (
                capo_s3tables._operations.s3_table_buckets.get_table_storage_class.get_table_storage_class(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_s3tables.types.get_table_storage_class_request.GetTableStorageClassRequest = {
            "table_bucket_arn": table_bucket_arn,
            "namespace": namespace,
            "name": name,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_tables(
        self,
        table_bucket_arn: "capo_s3tables.types.table_bucket_arn.TableBucketARN",
        *,
        config_overrides: Optional[S3TablesClientConfig] = None,
        namespace: Optional["capo_s3tables.types.namespace_name.NamespaceName"] = None,
        prefix: Optional[str] = None,
        continuation_token: Optional["capo_s3tables.types.next_token.NextToken"] = None,
        max_tables: Optional[
            "capo_s3tables.types.list_tables_limit.ListTablesLimit"
        ] = None,
    ) -> "capo_s3tables.types.list_tables_response.ListTablesResponse":
        """<p>List tables in the given table bucket. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-tables.html">S3 Tables</a> in the <i>Amazon Simple Storage Service User Guide</i>.</p> <dl> <dt>Permissions</dt> <dd> <p>You must have the <code>s3tables:ListTables</code> permission to use this operation. </p> </dd> </dl>

        Args:
            table_bucket_arn: <p>The Amazon resource Name (ARN) of the table bucket.</p>
            namespace: <p>The namespace of the tables.</p>
            prefix: <p>The prefix of the tables.</p>
            continuation_token: <p> <code>ContinuationToken</code> indicates to Amazon S3 that the list is being continued on this bucket with a token. <code>ContinuationToken</code> is obfuscated and is not a real key. You can use this <code>ContinuationToken</code> for pagination of the list results.</p>
            max_tables: <p>The maximum number of tables to return.</p>

        Raises:
            capo_s3tables.errors.bad_request_exception.BadRequestException: <p>The request is invalid or malformed.</p>
            capo_s3tables.errors.conflict_exception.ConflictException: <p>The request failed because there is a conflict with a previous write. You can retry the request.</p>
            capo_s3tables.errors.forbidden_exception.ForbiddenException: <p>The caller isn't authorized to make the request.</p>
            capo_s3tables.errors.internal_server_error_exception.InternalServerErrorException: <p>The request failed due to an internal server error.</p>
            capo_s3tables.errors.not_found_exception.NotFoundException: <p>The request was rejected because the specified resource could not be found.</p>
            capo_s3tables.errors.too_many_requests_exception.TooManyRequestsException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_s3tables.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_s3tables.types.list_tables_request.ListTablesRequest]",
        ) -> OperationResponse[
            "capo_s3tables.types.list_tables_response.ListTablesResponse"
        ]:
            import capo_s3tables._operations.s3_table_buckets.list_tables

            output, http_response = (
                capo_s3tables._operations.s3_table_buckets.list_tables.list_tables(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_s3tables.types.list_tables_request.ListTablesRequest = {
            "table_bucket_arn": table_bucket_arn
        }
        if namespace is not None:
            input_["namespace"] = namespace
        if prefix is not None:
            input_["prefix"] = prefix
        if continuation_token is not None:
            input_["continuation_token"] = continuation_token
        if max_tables is not None:
            input_["max_tables"] = max_tables

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_tables(
        self,
        table_bucket_arn: "capo_s3tables.types.table_bucket_arn.TableBucketARN",
        *,
        config_overrides: Optional[S3TablesClientConfig] = None,
        namespace: Optional["capo_s3tables.types.namespace_name.NamespaceName"] = None,
        prefix: Optional[str] = None,
        continuation_token: Optional["capo_s3tables.types.next_token.NextToken"] = None,
        max_tables: Optional[
            "capo_s3tables.types.list_tables_limit.ListTablesLimit"
        ] = None,
    ) -> "Iterator[capo_s3tables.types.table_summary.TableSummary]":
        _token = continuation_token
        while True:
            _response = self.list_tables(
                table_bucket_arn,
                config_overrides=config_overrides,
                namespace=namespace,
                prefix=prefix,
                continuation_token=_token,
                max_tables=max_tables,
            )
            _page = _resolve_path(_response, ("tables",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("continuation_token",))
            if not _token:
                break

    def put_table_maintenance_configuration(
        self,
        table_bucket_arn: "capo_s3tables.types.table_bucket_arn.TableBucketARN",
        namespace: "capo_s3tables.types.namespace_name.NamespaceName",
        name: "capo_s3tables.types.table_name.TableName",
        type: "capo_s3tables.types.table_maintenance_type.TableMaintenanceType",
        value: "capo_s3tables.types.table_maintenance_configuration_value.TableMaintenanceConfigurationValue",
        *,
        config_overrides: Optional[S3TablesClientConfig] = None,
    ) -> None:
        """<p>Creates a new maintenance configuration or replaces an existing maintenance configuration for a table. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-maintenance.html">S3 Tables maintenance</a> in the <i>Amazon Simple Storage Service User Guide</i>.</p> <dl> <dt>Permissions</dt> <dd> <p>You must have the <code>s3tables:PutTableMaintenanceConfiguration</code> permission to use this operation. </p> </dd> </dl>

        Args:
            table_bucket_arn: <p>The Amazon Resource Name (ARN) of the table associated with the maintenance configuration.</p>
            namespace: <p>The namespace of the table.</p>
            name: <p>The name of the table.</p>
            type: <p>The type of the maintenance configuration.</p>
            value: <p>Defines the values of the maintenance configuration for the table.</p>

        Raises:
            capo_s3tables.errors.bad_request_exception.BadRequestException: <p>The request is invalid or malformed.</p>
            capo_s3tables.errors.conflict_exception.ConflictException: <p>The request failed because there is a conflict with a previous write. You can retry the request.</p>
            capo_s3tables.errors.forbidden_exception.ForbiddenException: <p>The caller isn't authorized to make the request.</p>
            capo_s3tables.errors.internal_server_error_exception.InternalServerErrorException: <p>The request failed due to an internal server error.</p>
            capo_s3tables.errors.not_found_exception.NotFoundException: <p>The request was rejected because the specified resource could not be found.</p>
            capo_s3tables.errors.too_many_requests_exception.TooManyRequestsException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_s3tables.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_s3tables.types.put_table_maintenance_configuration_request.PutTableMaintenanceConfigurationRequest]",
        ) -> OperationResponse[None]:
            import capo_s3tables._operations.s3_table_buckets.put_table_maintenance_configuration

            output, http_response = (
                capo_s3tables._operations.s3_table_buckets.put_table_maintenance_configuration.put_table_maintenance_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_s3tables.types.put_table_maintenance_configuration_request.PutTableMaintenanceConfigurationRequest = {
            "table_bucket_arn": table_bucket_arn,
            "namespace": namespace,
            "name": name,
            "type": type,
            "value": value,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def put_table_record_expiration_configuration(
        self,
        table_arn: "capo_s3tables.types.table_arn.TableARN",
        value: "capo_s3tables.types.table_record_expiration_configuration_value.TableRecordExpirationConfigurationValue",
        *,
        config_overrides: Optional[S3TablesClientConfig] = None,
    ) -> None:
        """<p>Creates or updates the expiration configuration settings for records in a table, including the status of the configuration. If you enable record expiration for a table, records expire and are automatically removed from the table after the number of days that you specify.</p> <dl> <dt>Permissions</dt> <dd> <p>You must have the <code>s3tables:PutTableRecordExpirationConfiguration</code> permission to use this operation.</p> </dd> </dl>

        Args:
            table_arn: <p>The Amazon Resource Name (ARN) of the table.</p>
            value: <p>The record expiration configuration to apply to the table, including the status (<code>enabled</code> or <code>disabled</code>) and retention period in days.</p>

        Raises:
            capo_s3tables.errors.bad_request_exception.BadRequestException: <p>The request is invalid or malformed.</p>
            capo_s3tables.errors.forbidden_exception.ForbiddenException: <p>The caller isn't authorized to make the request.</p>
            capo_s3tables.errors.internal_server_error_exception.InternalServerErrorException: <p>The request failed due to an internal server error.</p>
            capo_s3tables.errors.method_not_allowed_exception.MethodNotAllowedException: <p>The requested operation is not allowed on this resource. This may occur when attempting to modify a resource that is managed by a service or has restrictions that prevent the operation.</p>
            capo_s3tables.errors.not_found_exception.NotFoundException: <p>The request was rejected because the specified resource could not be found.</p>
            capo_s3tables.errors.too_many_requests_exception.TooManyRequestsException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_s3tables.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_s3tables.types.put_table_record_expiration_configuration_request.PutTableRecordExpirationConfigurationRequest]",
        ) -> OperationResponse[None]:
            import capo_s3tables._operations.s3_table_buckets.put_table_record_expiration_configuration

            output, http_response = (
                capo_s3tables._operations.s3_table_buckets.put_table_record_expiration_configuration.put_table_record_expiration_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_s3tables.types.put_table_record_expiration_configuration_request.PutTableRecordExpirationConfigurationRequest = {
            "table_arn": table_arn,
            "value": value,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def rename_table(
        self,
        table_bucket_arn: "capo_s3tables.types.table_bucket_arn.TableBucketARN",
        namespace: "capo_s3tables.types.namespace_name.NamespaceName",
        name: "capo_s3tables.types.table_name.TableName",
        *,
        config_overrides: Optional[S3TablesClientConfig] = None,
        new_namespace_name: Optional[
            "capo_s3tables.types.namespace_name.NamespaceName"
        ] = None,
        new_name: Optional["capo_s3tables.types.table_name.TableName"] = None,
        version_token: Optional[
            "capo_s3tables.types.version_token.VersionToken"
        ] = None,
    ) -> None:
        """<p>Renames a table or a namespace. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-tables.html">S3 Tables</a> in the <i>Amazon Simple Storage Service User Guide</i>.</p> <dl> <dt>Permissions</dt> <dd> <p>You must have the <code>s3tables:RenameTable</code> permission to use this operation. </p> </dd> </dl>

        Args:
            table_bucket_arn: <p>The Amazon Resource Name (ARN) of the table bucket. </p>
            namespace: <p>The namespace associated with the table. </p>
            name: <p>The current name of the table.</p>
            new_namespace_name: <p>The new name for the namespace.</p>
            new_name: <p>The new name for the table.</p>
            version_token: <p>The version token of the table.</p>

        Raises:
            capo_s3tables.errors.bad_request_exception.BadRequestException: <p>The request is invalid or malformed.</p>
            capo_s3tables.errors.conflict_exception.ConflictException: <p>The request failed because there is a conflict with a previous write. You can retry the request.</p>
            capo_s3tables.errors.forbidden_exception.ForbiddenException: <p>The caller isn't authorized to make the request.</p>
            capo_s3tables.errors.internal_server_error_exception.InternalServerErrorException: <p>The request failed due to an internal server error.</p>
            capo_s3tables.errors.not_found_exception.NotFoundException: <p>The request was rejected because the specified resource could not be found.</p>
            capo_s3tables.errors.too_many_requests_exception.TooManyRequestsException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_s3tables.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_s3tables.types.rename_table_request.RenameTableRequest]",
        ) -> OperationResponse[None]:
            import capo_s3tables._operations.s3_table_buckets.rename_table

            output, http_response = (
                capo_s3tables._operations.s3_table_buckets.rename_table.rename_table(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_s3tables.types.rename_table_request.RenameTableRequest = {
            "table_bucket_arn": table_bucket_arn,
            "namespace": namespace,
            "name": name,
        }
        if new_namespace_name is not None:
            input_["new_namespace_name"] = new_namespace_name
        if new_name is not None:
            input_["new_name"] = new_name
        if version_token is not None:
            input_["version_token"] = version_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_table_metadata_location(
        self,
        table_bucket_arn: "capo_s3tables.types.table_bucket_arn.TableBucketARN",
        namespace: "capo_s3tables.types.namespace_name.NamespaceName",
        name: "capo_s3tables.types.table_name.TableName",
        version_token: "capo_s3tables.types.version_token.VersionToken",
        metadata_location: "capo_s3tables.types.metadata_location.MetadataLocation",
        *,
        config_overrides: Optional[S3TablesClientConfig] = None,
    ) -> "capo_s3tables.types.update_table_metadata_location_response.UpdateTableMetadataLocationResponse":
        """<p>Updates the metadata location for a table. The metadata location of a table must be an S3 URI that begins with the table's warehouse location. The metadata location for an Apache Iceberg table must end with <code>.metadata.json</code>, or if the metadata file is Gzip-compressed, <code>.metadata.json.gz</code>.</p> <dl> <dt>Permissions</dt> <dd> <p>You must have the <code>s3tables:UpdateTableMetadataLocation</code> permission to use this operation. </p> </dd> </dl>

        Args:
            table_bucket_arn: <p>The Amazon Resource Name (ARN) of the table bucket. </p>
            namespace: <p>The namespace of the table.</p>
            name: <p>The name of the table.</p>
            version_token: <p>The version token of the table. </p>
            metadata_location: <p>The new metadata location for the table. </p>

        Raises:
            capo_s3tables.errors.bad_request_exception.BadRequestException: <p>The request is invalid or malformed.</p>
            capo_s3tables.errors.conflict_exception.ConflictException: <p>The request failed because there is a conflict with a previous write. You can retry the request.</p>
            capo_s3tables.errors.forbidden_exception.ForbiddenException: <p>The caller isn't authorized to make the request.</p>
            capo_s3tables.errors.internal_server_error_exception.InternalServerErrorException: <p>The request failed due to an internal server error.</p>
            capo_s3tables.errors.not_found_exception.NotFoundException: <p>The request was rejected because the specified resource could not be found.</p>
            capo_s3tables.errors.too_many_requests_exception.TooManyRequestsException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_s3tables.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_s3tables.types.update_table_metadata_location_request.UpdateTableMetadataLocationRequest]",
        ) -> OperationResponse[
            "capo_s3tables.types.update_table_metadata_location_response.UpdateTableMetadataLocationResponse"
        ]:
            import capo_s3tables._operations.s3_table_buckets.update_table_metadata_location

            output, http_response = (
                capo_s3tables._operations.s3_table_buckets.update_table_metadata_location.update_table_metadata_location(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_s3tables.types.update_table_metadata_location_request.UpdateTableMetadataLocationRequest = {
            "table_bucket_arn": table_bucket_arn,
            "namespace": namespace,
            "name": name,
            "version_token": version_token,
            "metadata_location": metadata_location,
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
