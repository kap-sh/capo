"""Generated from Smithy shape ``com.amazonaws.omics#Omics``."""

import uuid
import warnings
from collections.abc import AsyncGenerator, AsyncIterator
from contextlib import asynccontextmanager
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import AsyncBaseHandler, AsyncClient

import capo_omics._auth._signers
import capo_omics._auth._sigv4
from capo_omics._auth._identity import Credentials
from capo_omics._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_omics._auth._zapros_handler import AuthMiddleware
from capo_omics._body import Body, aclosing_bodies
from capo_omics._iter import ensure_async_iterator
from capo_omics._pagination import resolve_path as _resolve_path
from capo_omics._resources.omics.annotation_import_job import AsyncAnnotationImportJob
from capo_omics._resources.omics.annotation_store import AsyncAnnotationStore
from capo_omics._resources.omics.annotation_store_version import (
    AsyncAnnotationStoreVersion,
)
from capo_omics._resources.omics.configuration_resource import (
    AsyncConfigurationResource,
)
from capo_omics._resources.omics.reference_store_resource import (
    AsyncReferenceStoreResource,
)
from capo_omics._resources.omics.run_batch_resource import AsyncRunBatchResource
from capo_omics._resources.omics.run_cache_resource import AsyncRunCacheResource
from capo_omics._resources.omics.run_group_resource import AsyncRunGroupResource
from capo_omics._resources.omics.run_resource import AsyncRunResource
from capo_omics._resources.omics.sequence_store_resource import (
    AsyncSequenceStoreResource,
)
from capo_omics._resources.omics.share import AsyncShare
from capo_omics._resources.omics.tagging_resource import AsyncTaggingResource
from capo_omics._resources.omics.variant_import_job import AsyncVariantImportJob
from capo_omics._resources.omics.variant_store import AsyncVariantStore
from capo_omics._resources.omics.workflow_resource import AsyncWorkflowResource
from capo_omics._services._aws_config import aaws_config
from capo_omics._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import capo_omics.types.abort_multipart_read_set_upload_request
    import capo_omics.types.abort_multipart_read_set_upload_response
    import capo_omics.types.accelerators
    import capo_omics.types.accept_share_request
    import capo_omics.types.accept_share_response
    import capo_omics.types.activate_read_set_filter
    import capo_omics.types.activate_read_set_job_item
    import capo_omics.types.activation_job_id
    import capo_omics.types.annotation_field_map
    import capo_omics.types.annotation_import_item_sources
    import capo_omics.types.annotation_import_job_item
    import capo_omics.types.annotation_store_item
    import capo_omics.types.annotation_store_version_item
    import capo_omics.types.arn
    import capo_omics.types.aws_account_id
    import capo_omics.types.batch_delete_read_set_request
    import capo_omics.types.batch_delete_read_set_response
    import capo_omics.types.batch_id
    import capo_omics.types.batch_list_item
    import capo_omics.types.batch_name
    import capo_omics.types.batch_request_id
    import capo_omics.types.batch_run_settings
    import capo_omics.types.batch_status
    import capo_omics.types.cache_behavior
    import capo_omics.types.cancel_annotation_import_request
    import capo_omics.types.cancel_annotation_import_response
    import capo_omics.types.cancel_run_batch_request
    import capo_omics.types.cancel_run_batch_response
    import capo_omics.types.cancel_run_request
    import capo_omics.types.cancel_variant_import_request
    import capo_omics.types.cancel_variant_import_response
    import capo_omics.types.client_token
    import capo_omics.types.complete_multipart_read_set_upload_request
    import capo_omics.types.complete_multipart_read_set_upload_response
    import capo_omics.types.complete_read_set_upload_part_list
    import capo_omics.types.configuration_description
    import capo_omics.types.configuration_list_item
    import capo_omics.types.configuration_list_token
    import capo_omics.types.configuration_name
    import capo_omics.types.configuration_request_id
    import capo_omics.types.container_registry_map
    import capo_omics.types.create_annotation_store_request
    import capo_omics.types.create_annotation_store_response
    import capo_omics.types.create_annotation_store_version_request
    import capo_omics.types.create_annotation_store_version_response
    import capo_omics.types.create_configuration_request
    import capo_omics.types.create_configuration_response
    import capo_omics.types.create_multipart_read_set_upload_request
    import capo_omics.types.create_multipart_read_set_upload_response
    import capo_omics.types.create_reference_store_request
    import capo_omics.types.create_reference_store_response
    import capo_omics.types.create_run_cache_request
    import capo_omics.types.create_run_cache_response
    import capo_omics.types.create_run_group_request
    import capo_omics.types.create_run_group_response
    import capo_omics.types.create_sequence_store_request
    import capo_omics.types.create_sequence_store_response
    import capo_omics.types.create_share_request
    import capo_omics.types.create_share_response
    import capo_omics.types.create_variant_store_request
    import capo_omics.types.create_variant_store_response
    import capo_omics.types.create_workflow_request
    import capo_omics.types.create_workflow_response
    import capo_omics.types.create_workflow_version_request
    import capo_omics.types.create_workflow_version_response
    import capo_omics.types.default_run_setting
    import capo_omics.types.definition_repository
    import capo_omics.types.delete_annotation_store_request
    import capo_omics.types.delete_annotation_store_response
    import capo_omics.types.delete_annotation_store_versions_request
    import capo_omics.types.delete_annotation_store_versions_response
    import capo_omics.types.delete_batch_request
    import capo_omics.types.delete_configuration_request
    import capo_omics.types.delete_reference_request
    import capo_omics.types.delete_reference_response
    import capo_omics.types.delete_reference_store_request
    import capo_omics.types.delete_reference_store_response
    import capo_omics.types.delete_run_batch_request
    import capo_omics.types.delete_run_batch_response
    import capo_omics.types.delete_run_cache_request
    import capo_omics.types.delete_run_group_request
    import capo_omics.types.delete_run_request
    import capo_omics.types.delete_s3_access_policy_request
    import capo_omics.types.delete_s3_access_policy_response
    import capo_omics.types.delete_sequence_store_request
    import capo_omics.types.delete_sequence_store_response
    import capo_omics.types.delete_share_request
    import capo_omics.types.delete_share_response
    import capo_omics.types.delete_variant_store_request
    import capo_omics.types.delete_variant_store_response
    import capo_omics.types.delete_workflow_request
    import capo_omics.types.delete_workflow_version_request
    import capo_omics.types.description
    import capo_omics.types.e_tag_algorithm_family
    import capo_omics.types.engine_settings
    import capo_omics.types.export_job_id
    import capo_omics.types.export_read_set_filter
    import capo_omics.types.export_read_set_job_detail
    import capo_omics.types.export_read_set_list
    import capo_omics.types.fallback_location
    import capo_omics.types.file_type
    import capo_omics.types.filter
    import capo_omics.types.format_options
    import capo_omics.types.generated_from
    import capo_omics.types.get_annotation_import_request
    import capo_omics.types.get_annotation_import_response
    import capo_omics.types.get_annotation_store_request
    import capo_omics.types.get_annotation_store_response
    import capo_omics.types.get_annotation_store_version_request
    import capo_omics.types.get_annotation_store_version_response
    import capo_omics.types.get_batch_request
    import capo_omics.types.get_batch_response
    import capo_omics.types.get_configuration_request
    import capo_omics.types.get_configuration_response
    import capo_omics.types.get_read_set_activation_job_request
    import capo_omics.types.get_read_set_activation_job_response
    import capo_omics.types.get_read_set_export_job_request
    import capo_omics.types.get_read_set_export_job_response
    import capo_omics.types.get_read_set_import_job_request
    import capo_omics.types.get_read_set_import_job_response
    import capo_omics.types.get_read_set_metadata_request
    import capo_omics.types.get_read_set_metadata_response
    import capo_omics.types.get_read_set_request
    import capo_omics.types.get_read_set_response
    import capo_omics.types.get_reference_import_job_request
    import capo_omics.types.get_reference_import_job_response
    import capo_omics.types.get_reference_metadata_request
    import capo_omics.types.get_reference_metadata_response
    import capo_omics.types.get_reference_request
    import capo_omics.types.get_reference_response
    import capo_omics.types.get_reference_store_request
    import capo_omics.types.get_reference_store_response
    import capo_omics.types.get_run_cache_request
    import capo_omics.types.get_run_cache_response
    import capo_omics.types.get_run_group_request
    import capo_omics.types.get_run_group_response
    import capo_omics.types.get_run_request
    import capo_omics.types.get_run_response
    import capo_omics.types.get_run_task_request
    import capo_omics.types.get_run_task_response
    import capo_omics.types.get_s3_access_policy_request
    import capo_omics.types.get_s3_access_policy_response
    import capo_omics.types.get_sequence_store_request
    import capo_omics.types.get_sequence_store_response
    import capo_omics.types.get_share_request
    import capo_omics.types.get_share_response
    import capo_omics.types.get_variant_import_request
    import capo_omics.types.get_variant_import_response
    import capo_omics.types.get_variant_store_request
    import capo_omics.types.get_variant_store_response
    import capo_omics.types.get_workflow_request
    import capo_omics.types.get_workflow_response
    import capo_omics.types.get_workflow_version_request
    import capo_omics.types.get_workflow_version_response
    import capo_omics.types.id_list
    import capo_omics.types.import_job_id
    import capo_omics.types.import_read_set_filter
    import capo_omics.types.import_read_set_job_item
    import capo_omics.types.import_reference_filter
    import capo_omics.types.import_reference_job_item
    import capo_omics.types.list_annotation_import_jobs_filter
    import capo_omics.types.list_annotation_import_jobs_request
    import capo_omics.types.list_annotation_import_jobs_response
    import capo_omics.types.list_annotation_store_versions_filter
    import capo_omics.types.list_annotation_store_versions_request
    import capo_omics.types.list_annotation_store_versions_response
    import capo_omics.types.list_annotation_stores_filter
    import capo_omics.types.list_annotation_stores_request
    import capo_omics.types.list_annotation_stores_response
    import capo_omics.types.list_batch_request
    import capo_omics.types.list_batch_response
    import capo_omics.types.list_configurations_request
    import capo_omics.types.list_configurations_response
    import capo_omics.types.list_multipart_read_set_uploads_request
    import capo_omics.types.list_multipart_read_set_uploads_response
    import capo_omics.types.list_read_set_activation_jobs_request
    import capo_omics.types.list_read_set_activation_jobs_response
    import capo_omics.types.list_read_set_export_jobs_request
    import capo_omics.types.list_read_set_export_jobs_response
    import capo_omics.types.list_read_set_import_jobs_request
    import capo_omics.types.list_read_set_import_jobs_response
    import capo_omics.types.list_read_set_upload_parts_request
    import capo_omics.types.list_read_set_upload_parts_response
    import capo_omics.types.list_read_sets_request
    import capo_omics.types.list_read_sets_response
    import capo_omics.types.list_reference_import_jobs_request
    import capo_omics.types.list_reference_import_jobs_response
    import capo_omics.types.list_reference_stores_request
    import capo_omics.types.list_reference_stores_response
    import capo_omics.types.list_references_request
    import capo_omics.types.list_references_response
    import capo_omics.types.list_run_caches_request
    import capo_omics.types.list_run_caches_response
    import capo_omics.types.list_run_groups_request
    import capo_omics.types.list_run_groups_response
    import capo_omics.types.list_run_tasks_request
    import capo_omics.types.list_run_tasks_response
    import capo_omics.types.list_runs_in_batch_request
    import capo_omics.types.list_runs_in_batch_response
    import capo_omics.types.list_runs_request
    import capo_omics.types.list_runs_response
    import capo_omics.types.list_sequence_stores_request
    import capo_omics.types.list_sequence_stores_response
    import capo_omics.types.list_shares_request
    import capo_omics.types.list_shares_response
    import capo_omics.types.list_tags_for_resource_request
    import capo_omics.types.list_tags_for_resource_response
    import capo_omics.types.list_token
    import capo_omics.types.list_variant_import_jobs_filter
    import capo_omics.types.list_variant_import_jobs_request
    import capo_omics.types.list_variant_import_jobs_response
    import capo_omics.types.list_variant_stores_filter
    import capo_omics.types.list_variant_stores_request
    import capo_omics.types.list_variant_stores_response
    import capo_omics.types.list_workflow_versions_request
    import capo_omics.types.list_workflow_versions_response
    import capo_omics.types.list_workflows_request
    import capo_omics.types.list_workflows_response
    import capo_omics.types.multipart_read_set_upload_list_item
    import capo_omics.types.networking_mode
    import capo_omics.types.next_token
    import capo_omics.types.numeric_id_in_arn
    import capo_omics.types.parameter_template_path
    import capo_omics.types.propagated_set_level_tags
    import capo_omics.types.put_s3_access_policy_request
    import capo_omics.types.put_s3_access_policy_response
    import capo_omics.types.range
    import capo_omics.types.read_set_description
    import capo_omics.types.read_set_file
    import capo_omics.types.read_set_filter
    import capo_omics.types.read_set_id
    import capo_omics.types.read_set_id_list
    import capo_omics.types.read_set_list_item
    import capo_omics.types.read_set_name
    import capo_omics.types.read_set_part_source
    import capo_omics.types.read_set_part_streaming_blob
    import capo_omics.types.read_set_upload_part_list_filter
    import capo_omics.types.read_set_upload_part_list_item
    import capo_omics.types.readme_markdown
    import capo_omics.types.readme_path
    import capo_omics.types.reference_arn
    import capo_omics.types.reference_file
    import capo_omics.types.reference_filter
    import capo_omics.types.reference_id
    import capo_omics.types.reference_item
    import capo_omics.types.reference_list_item
    import capo_omics.types.reference_store_description
    import capo_omics.types.reference_store_detail
    import capo_omics.types.reference_store_filter
    import capo_omics.types.reference_store_id
    import capo_omics.types.reference_store_name
    import capo_omics.types.resource_id
    import capo_omics.types.resource_owner
    import capo_omics.types.role_arn
    import capo_omics.types.run_batch_list_item
    import capo_omics.types.run_cache_id
    import capo_omics.types.run_cache_list_item
    import capo_omics.types.run_cache_request_id
    import capo_omics.types.run_configurations
    import capo_omics.types.run_export_list
    import capo_omics.types.run_group_id
    import capo_omics.types.run_group_list_item
    import capo_omics.types.run_group_list_token
    import capo_omics.types.run_group_name
    import capo_omics.types.run_group_request_id
    import capo_omics.types.run_id
    import capo_omics.types.run_left_normalization
    import capo_omics.types.run_list_item
    import capo_omics.types.run_list_token
    import capo_omics.types.run_log_level
    import capo_omics.types.run_name
    import capo_omics.types.run_output_uri
    import capo_omics.types.run_parameters
    import capo_omics.types.run_request_id
    import capo_omics.types.run_retention_mode
    import capo_omics.types.run_role_arn
    import capo_omics.types.run_status
    import capo_omics.types.s3_access_config
    import capo_omics.types.s3_access_point_arn
    import capo_omics.types.s3_access_policy
    import capo_omics.types.s3_destination
    import capo_omics.types.s3_uri_for_bucket_or_object
    import capo_omics.types.s3_uri_for_object
    import capo_omics.types.sample_id
    import capo_omics.types.scratch_storage_mode
    import capo_omics.types.sequence_store_description
    import capo_omics.types.sequence_store_detail
    import capo_omics.types.sequence_store_filter
    import capo_omics.types.sequence_store_id
    import capo_omics.types.sequence_store_name
    import capo_omics.types.session_policy
    import capo_omics.types.share_details
    import capo_omics.types.share_name
    import capo_omics.types.sse_config
    import capo_omics.types.start_annotation_import_request
    import capo_omics.types.start_annotation_import_response
    import capo_omics.types.start_read_set_activation_job_request
    import capo_omics.types.start_read_set_activation_job_response
    import capo_omics.types.start_read_set_activation_job_source_list
    import capo_omics.types.start_read_set_export_job_request
    import capo_omics.types.start_read_set_export_job_response
    import capo_omics.types.start_read_set_import_job_request
    import capo_omics.types.start_read_set_import_job_response
    import capo_omics.types.start_read_set_import_job_source_list
    import capo_omics.types.start_reference_import_job_request
    import capo_omics.types.start_reference_import_job_response
    import capo_omics.types.start_reference_import_job_source_list
    import capo_omics.types.start_run_batch_request
    import capo_omics.types.start_run_batch_response
    import capo_omics.types.start_run_request
    import capo_omics.types.start_run_response
    import capo_omics.types.start_variant_import_request
    import capo_omics.types.start_variant_import_response
    import capo_omics.types.storage_type
    import capo_omics.types.store_format
    import capo_omics.types.store_name
    import capo_omics.types.store_options
    import capo_omics.types.subject_id
    import capo_omics.types.submission_status
    import capo_omics.types.tag_arn
    import capo_omics.types.tag_key_list
    import capo_omics.types.tag_map
    import capo_omics.types.tag_resource_request
    import capo_omics.types.tag_resource_response
    import capo_omics.types.task_id
    import capo_omics.types.task_list_item
    import capo_omics.types.task_list_token
    import capo_omics.types.task_status
    import capo_omics.types.untag_resource_request
    import capo_omics.types.untag_resource_response
    import capo_omics.types.update_annotation_store_request
    import capo_omics.types.update_annotation_store_response
    import capo_omics.types.update_annotation_store_version_request
    import capo_omics.types.update_annotation_store_version_response
    import capo_omics.types.update_run_cache_request
    import capo_omics.types.update_run_group_request
    import capo_omics.types.update_sequence_store_request
    import capo_omics.types.update_sequence_store_response
    import capo_omics.types.update_variant_store_request
    import capo_omics.types.update_variant_store_response
    import capo_omics.types.update_workflow_request
    import capo_omics.types.update_workflow_version_request
    import capo_omics.types.upload_id
    import capo_omics.types.upload_read_set_part_request
    import capo_omics.types.upload_read_set_part_response
    import capo_omics.types.uri
    import capo_omics.types.user_custom_description
    import capo_omics.types.user_custom_name
    import capo_omics.types.variant_import_item_sources
    import capo_omics.types.variant_import_job_item
    import capo_omics.types.variant_store_item
    import capo_omics.types.version_list
    import capo_omics.types.version_name
    import capo_omics.types.version_options
    import capo_omics.types.workflow_bucket_owner_id
    import capo_omics.types.workflow_definition
    import capo_omics.types.workflow_description
    import capo_omics.types.workflow_engine
    import capo_omics.types.workflow_export_list
    import capo_omics.types.workflow_id
    import capo_omics.types.workflow_list_item
    import capo_omics.types.workflow_list_token
    import capo_omics.types.workflow_main
    import capo_omics.types.workflow_name
    import capo_omics.types.workflow_owner_id
    import capo_omics.types.workflow_parameter_template
    import capo_omics.types.workflow_request_id
    import capo_omics.types.workflow_type
    import capo_omics.types.workflow_version_description
    import capo_omics.types.workflow_version_list_item
    import capo_omics.types.workflow_version_list_token
    import capo_omics.types.workflow_version_name


class AsyncOmicsClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None
    anonymous: bool | None


class AsyncOmicsClient:
    """A client for the ``Omics`` service.

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
        self._config = AsyncOmicsClientConfig(
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

        # resources
        self.annotation_import_job = AsyncAnnotationImportJob(self)
        self.annotation_store = AsyncAnnotationStore(self)
        self.annotation_store_version = AsyncAnnotationStoreVersion(self)
        self.configuration_resource = AsyncConfigurationResource(self)
        self.reference_store_resource = AsyncReferenceStoreResource(self)
        self.run_batch_resource = AsyncRunBatchResource(self)
        self.run_cache_resource = AsyncRunCacheResource(self)
        self.run_group_resource = AsyncRunGroupResource(self)
        self.run_resource = AsyncRunResource(self)
        self.sequence_store_resource = AsyncSequenceStoreResource(self)
        self.share = AsyncShare(self)
        self.tagging_resource = AsyncTaggingResource(self)
        self.variant_import_job = AsyncVariantImportJob(self)
        self.variant_store = AsyncVariantStore(self)
        self.workflow_resource = AsyncWorkflowResource(self)

    def operation_options(
        self, config_overrides: Optional[AsyncOmicsClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncOmicsClientConfig = config_overrides or {}
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

    async def delete_s3_access_policy(
        self,
        s3_access_point_arn: "capo_omics.types.s3_access_point_arn.S3AccessPointArn",
        *,
        config_overrides: Optional[AsyncOmicsClientConfig] = None,
    ) -> (
        "capo_omics.types.delete_s3_access_policy_response.DeleteS3AccessPolicyResponse"
    ):
        """<p>Deletes an access policy for the specified store.</p>

        Args:
            s3_access_point_arn: <p>The S3 access point ARN that has the access policy.</p>

        Raises:
            capo_omics.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_omics.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred. Try the request again.</p>
            capo_omics.errors.not_supported_operation_exception.NotSupportedOperationException: <p> The operation is not supported by Amazon Omics, or the API does not exist. </p>
            capo_omics.errors.request_timeout_exception.RequestTimeoutException: <p>The request timed out.</p>
            capo_omics.errors.resource_not_found_exception.ResourceNotFoundException: <p>The target resource was not found in the current Region.</p>
            capo_omics.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_omics.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_omics.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_omics.types.delete_s3_access_policy_request.DeleteS3AccessPolicyRequest]",
        ) -> AsyncOperationResponse[
            "capo_omics.types.delete_s3_access_policy_response.DeleteS3AccessPolicyResponse"
        ]:
            import capo_omics._operations.omics.delete_s3_access_policy

            (
                output,
                http_response,
            ) = await capo_omics._operations.omics.delete_s3_access_policy.async_delete_s3_access_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_omics.types.delete_s3_access_policy_request.DeleteS3AccessPolicyRequest = {
            "s3_access_point_arn": s3_access_point_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_s3_access_policy(
        self,
        s3_access_point_arn: "capo_omics.types.s3_access_point_arn.S3AccessPointArn",
        *,
        config_overrides: Optional[AsyncOmicsClientConfig] = None,
    ) -> "capo_omics.types.get_s3_access_policy_response.GetS3AccessPolicyResponse":
        """<p>Retrieves details about an access policy on a given store.</p>

        Args:
            s3_access_point_arn: <p>The S3 access point ARN that has the access policy.</p>

        Raises:
            capo_omics.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_omics.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred. Try the request again.</p>
            capo_omics.errors.not_supported_operation_exception.NotSupportedOperationException: <p> The operation is not supported by Amazon Omics, or the API does not exist. </p>
            capo_omics.errors.request_timeout_exception.RequestTimeoutException: <p>The request timed out.</p>
            capo_omics.errors.resource_not_found_exception.ResourceNotFoundException: <p>The target resource was not found in the current Region.</p>
            capo_omics.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request exceeds a service quota.</p>
            capo_omics.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_omics.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_omics.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_omics.types.get_s3_access_policy_request.GetS3AccessPolicyRequest]",
        ) -> AsyncOperationResponse[
            "capo_omics.types.get_s3_access_policy_response.GetS3AccessPolicyResponse"
        ]:
            import capo_omics._operations.omics.get_s3_access_policy

            (
                output,
                http_response,
            ) = await capo_omics._operations.omics.get_s3_access_policy.async_get_s3_access_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_omics.types.get_s3_access_policy_request.GetS3AccessPolicyRequest = {
            "s3_access_point_arn": s3_access_point_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def put_s3_access_policy(
        self,
        s3_access_point_arn: "capo_omics.types.s3_access_point_arn.S3AccessPointArn",
        s3_access_policy: "capo_omics.types.s3_access_policy.S3AccessPolicy",
        *,
        config_overrides: Optional[AsyncOmicsClientConfig] = None,
    ) -> "capo_omics.types.put_s3_access_policy_response.PutS3AccessPolicyResponse":
        """<p>Adds an access policy to the specified store.</p>

        Args:
            s3_access_point_arn: <p>The S3 access point ARN where you want to put the access policy.</p>
            s3_access_policy: <p>The resource policy that controls S3 access to the store.</p>

        Raises:
            capo_omics.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_omics.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred. Try the request again.</p>
            capo_omics.errors.not_supported_operation_exception.NotSupportedOperationException: <p> The operation is not supported by Amazon Omics, or the API does not exist. </p>
            capo_omics.errors.request_timeout_exception.RequestTimeoutException: <p>The request timed out.</p>
            capo_omics.errors.resource_not_found_exception.ResourceNotFoundException: <p>The target resource was not found in the current Region.</p>
            capo_omics.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_omics.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_omics.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_omics.types.put_s3_access_policy_request.PutS3AccessPolicyRequest]",
        ) -> AsyncOperationResponse[
            "capo_omics.types.put_s3_access_policy_response.PutS3AccessPolicyResponse"
        ]:
            import capo_omics._operations.omics.put_s3_access_policy

            (
                output,
                http_response,
            ) = await capo_omics._operations.omics.put_s3_access_policy.async_put_s3_access_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_omics.types.put_s3_access_policy_request.PutS3AccessPolicyRequest = {
            "s3_access_point_arn": s3_access_point_arn,
            "s3_access_policy": s3_access_policy,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def start_annotation_import_job(
        self,
        destination_name: "capo_omics.types.store_name.StoreName",
        role_arn: "capo_omics.types.arn.Arn",
        items: "capo_omics.types.annotation_import_item_sources.AnnotationImportItemSources",
        *,
        config_overrides: Optional[AsyncOmicsClientConfig] = None,
        version_name: Optional["capo_omics.types.version_name.VersionName"] = None,
        format_options: Optional[
            "capo_omics.types.format_options.FormatOptions"
        ] = None,
        run_left_normalization: Optional[
            "capo_omics.types.run_left_normalization.RunLeftNormalization"
        ] = None,
        annotation_fields: Optional[
            "capo_omics.types.annotation_field_map.AnnotationFieldMap"
        ] = None,
    ) -> "capo_omics.types.start_annotation_import_response.StartAnnotationImportResponse":
        """<important> <p>Amazon Web Services HealthOmics variant stores and annotation stores are no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see <a href="https://docs.aws.amazon.com/omics/latest/dev/variant-store-availability-change.html"> Amazon Web Services HealthOmics variant store and annotation store availability change</a>.</p> </important> <p>Starts an annotation import job.</p>

        Args:
            destination_name: <p>A destination annotation store for the job.</p>
            role_arn: <p>A service role for the job.</p>
            items: <p>Items to import.</p>
            version_name: <p> The name of the annotation store version. </p>
            format_options: <p>Formatting options for the annotation file.</p>
            run_left_normalization: <p>The job's left normalization setting.</p>
            annotation_fields: <p>The annotation schema generated by the parsed annotation data.</p>

        Raises:
            capo_omics.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_omics.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred. Try the request again.</p>
            capo_omics.errors.resource_not_found_exception.ResourceNotFoundException: <p>The target resource was not found in the current Region.</p>
            capo_omics.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request exceeds a service quota.</p>
            capo_omics.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_omics.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_omics.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_omics.types.start_annotation_import_request.StartAnnotationImportRequest]",
        ) -> AsyncOperationResponse[
            "capo_omics.types.start_annotation_import_response.StartAnnotationImportResponse"
        ]:
            import capo_omics._operations.omics.start_annotation_import_job

            (
                output,
                http_response,
            ) = await capo_omics._operations.omics.start_annotation_import_job.async_start_annotation_import_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_omics.types.start_annotation_import_request.StartAnnotationImportRequest = {
            "destination_name": destination_name,
            "role_arn": role_arn,
            "items": items,
        }
        if version_name is not None:
            input_["version_name"] = version_name
        if format_options is not None:
            input_["format_options"] = format_options
        if run_left_normalization is not None:
            input_["run_left_normalization"] = run_left_normalization
        if annotation_fields is not None:
            input_["annotation_fields"] = annotation_fields

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_annotation_import_job(
        self,
        job_id: "capo_omics.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncOmicsClientConfig] = None,
    ) -> "capo_omics.types.get_annotation_import_response.GetAnnotationImportResponse":
        """<important> <p>Amazon Web Services HealthOmics variant stores and annotation stores are no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see <a href="https://docs.aws.amazon.com/omics/latest/dev/variant-store-availability-change.html"> Amazon Web Services HealthOmics variant store and annotation store availability change</a>.</p> </important> <p>Gets information about an annotation import job.</p>

        Args:
            job_id: <p>The job's ID.</p>

        Raises:
            capo_omics.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_omics.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred. Try the request again.</p>
            capo_omics.errors.resource_not_found_exception.ResourceNotFoundException: <p>The target resource was not found in the current Region.</p>
            capo_omics.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_omics.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_omics.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_omics.types.get_annotation_import_request.GetAnnotationImportRequest]",
        ) -> AsyncOperationResponse[
            "capo_omics.types.get_annotation_import_response.GetAnnotationImportResponse"
        ]:
            import capo_omics._operations.omics.get_annotation_import_job

            (
                output,
                http_response,
            ) = await capo_omics._operations.omics.get_annotation_import_job.async_get_annotation_import_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_omics.types.get_annotation_import_request.GetAnnotationImportRequest = {
            "job_id": job_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def cancel_annotation_import_job(
        self,
        job_id: "capo_omics.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncOmicsClientConfig] = None,
    ) -> "capo_omics.types.cancel_annotation_import_response.CancelAnnotationImportResponse":
        """<important> <p>Amazon Web Services HealthOmics variant stores and annotation stores are no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see <a href="https://docs.aws.amazon.com/omics/latest/dev/variant-store-availability-change.html"> Amazon Web Services HealthOmics variant store and annotation store availability change</a>.</p> </important> <p>Cancels an annotation import job.</p>

        Args:
            job_id: <p>The job's ID.</p>

        Raises:
            capo_omics.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_omics.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred. Try the request again.</p>
            capo_omics.errors.resource_not_found_exception.ResourceNotFoundException: <p>The target resource was not found in the current Region.</p>
            capo_omics.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_omics.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_omics.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_omics.types.cancel_annotation_import_request.CancelAnnotationImportRequest]",
        ) -> AsyncOperationResponse[
            "capo_omics.types.cancel_annotation_import_response.CancelAnnotationImportResponse"
        ]:
            import capo_omics._operations.omics.cancel_annotation_import_job

            (
                output,
                http_response,
            ) = await capo_omics._operations.omics.cancel_annotation_import_job.async_cancel_annotation_import_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_omics.types.cancel_annotation_import_request.CancelAnnotationImportRequest = {
            "job_id": job_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_annotation_import_jobs(
        self,
        *,
        config_overrides: Optional[AsyncOmicsClientConfig] = None,
        max_results: Optional[int] = None,
        ids: Optional["capo_omics.types.id_list.IdList"] = None,
        next_token: Optional[str] = None,
        filter: Optional[
            "capo_omics.types.list_annotation_import_jobs_filter.ListAnnotationImportJobsFilter"
        ] = None,
    ) -> "capo_omics.types.list_annotation_import_jobs_response.ListAnnotationImportJobsResponse":
        """<important> <p>Amazon Web Services HealthOmics variant stores and annotation stores are no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see <a href="https://docs.aws.amazon.com/omics/latest/dev/variant-store-availability-change.html"> Amazon Web Services HealthOmics variant store and annotation store availability change</a>.</p> </important> <p>Retrieves a list of annotation import jobs.</p>

        Args:
            max_results: <p>The maximum number of jobs to return in one page of results.</p>
            ids: <p>IDs of annotation import jobs to retrieve.</p>
            next_token: <p>Specifies the pagination token from a previous request to retrieve the next page of results.</p>
            filter: <p>A filter to apply to the list.</p>

        Raises:
            capo_omics.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_omics.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred. Try the request again.</p>
            capo_omics.errors.resource_not_found_exception.ResourceNotFoundException: <p>The target resource was not found in the current Region.</p>
            capo_omics.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_omics.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_omics.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_omics.types.list_annotation_import_jobs_request.ListAnnotationImportJobsRequest]",
        ) -> AsyncOperationResponse[
            "capo_omics.types.list_annotation_import_jobs_response.ListAnnotationImportJobsResponse"
        ]:
            import capo_omics._operations.omics.list_annotation_import_jobs

            (
                output,
                http_response,
            ) = await capo_omics._operations.omics.list_annotation_import_jobs.async_list_annotation_import_jobs(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_omics.types.list_annotation_import_jobs_request.ListAnnotationImportJobsRequest = {}
        if max_results is not None:
            input_["max_results"] = max_results
        if ids is not None:
            input_["ids"] = ids
        if next_token is not None:
            input_["next_token"] = next_token
        if filter is not None:
            input_["filter"] = filter

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_annotation_import_jobs(
        self,
        *,
        config_overrides: Optional[AsyncOmicsClientConfig] = None,
        max_results: Optional[int] = None,
        ids: Optional["capo_omics.types.id_list.IdList"] = None,
        next_token: Optional[str] = None,
        filter: Optional[
            "capo_omics.types.list_annotation_import_jobs_filter.ListAnnotationImportJobsFilter"
        ] = None,
    ) -> "AsyncIterator[capo_omics.types.annotation_import_job_item.AnnotationImportJobItem]":
        _token = next_token
        while True:
            _response = await self.list_annotation_import_jobs(
                config_overrides=config_overrides,
                max_results=max_results,
                ids=ids,
                next_token=_token,
                filter=filter,
            )
            _page = _resolve_path(_response, ("annotation_import_jobs",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def create_annotation_store(
        self,
        store_format: "capo_omics.types.store_format.StoreFormat",
        *,
        config_overrides: Optional[AsyncOmicsClientConfig] = None,
        reference: Optional["capo_omics.types.reference_item.ReferenceItem"] = None,
        name: Optional["capo_omics.types.store_name.StoreName"] = None,
        description: Optional["capo_omics.types.description.Description"] = None,
        tags: Optional["capo_omics.types.tag_map.TagMap"] = None,
        version_name: Optional["capo_omics.types.version_name.VersionName"] = None,
        sse_config: Optional["capo_omics.types.sse_config.SseConfig"] = None,
        store_options: Optional["capo_omics.types.store_options.StoreOptions"] = None,
    ) -> "capo_omics.types.create_annotation_store_response.CreateAnnotationStoreResponse":
        """<important> <p>Amazon Web Services HealthOmics variant stores and annotation stores are no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see <a href="https://docs.aws.amazon.com/omics/latest/dev/variant-store-availability-change.html"> Amazon Web Services HealthOmics variant store and annotation store availability change</a>.</p> </important> <p>Creates an annotation store.</p>

        Args:
            reference: <p>The genome reference for the store's annotations.</p>
            name: <p>A name for the store.</p>
            description: <p>A description for the store.</p>
            tags: <p>Tags for the store.</p>
            version_name: <p> The name given to an annotation store version to distinguish it from other versions. </p>
            sse_config: <p>Server-side encryption (SSE) settings for the store.</p>
            store_format: <p>The annotation file format of the store.</p>
            store_options: <p>File parsing options for the annotation store.</p>

        Raises:
            capo_omics.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_omics.errors.conflict_exception.ConflictException: <p>The request cannot be applied to the target resource in its current state.</p>
            capo_omics.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred. Try the request again.</p>
            capo_omics.errors.resource_not_found_exception.ResourceNotFoundException: <p>The target resource was not found in the current Region.</p>
            capo_omics.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request exceeds a service quota.</p>
            capo_omics.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_omics.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_omics.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_omics.types.create_annotation_store_request.CreateAnnotationStoreRequest]",
        ) -> AsyncOperationResponse[
            "capo_omics.types.create_annotation_store_response.CreateAnnotationStoreResponse"
        ]:
            import capo_omics._operations.omics.create_annotation_store

            (
                output,
                http_response,
            ) = await capo_omics._operations.omics.create_annotation_store.async_create_annotation_store(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_omics.types.create_annotation_store_request.CreateAnnotationStoreRequest = {
            "store_format": store_format
        }
        if reference is not None:
            input_["reference"] = reference
        if name is not None:
            input_["name"] = name
        if description is not None:
            input_["description"] = description
        if tags is not None:
            input_["tags"] = tags
        if version_name is not None:
            input_["version_name"] = version_name
        if sse_config is not None:
            input_["sse_config"] = sse_config
        if store_options is not None:
            input_["store_options"] = store_options

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_annotation_store(
        self, name: str, *, config_overrides: Optional[AsyncOmicsClientConfig] = None
    ) -> "capo_omics.types.get_annotation_store_response.GetAnnotationStoreResponse":
        """<important> <p>Amazon Web Services HealthOmics variant stores and annotation stores are no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see <a href="https://docs.aws.amazon.com/omics/latest/dev/variant-store-availability-change.html"> Amazon Web Services HealthOmics variant store and annotation store availability change</a>.</p> </important> <p>Gets information about an annotation store.</p>

        Args:
            name: <p>The store's name.</p>

        Raises:
            capo_omics.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_omics.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred. Try the request again.</p>
            capo_omics.errors.resource_not_found_exception.ResourceNotFoundException: <p>The target resource was not found in the current Region.</p>
            capo_omics.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_omics.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_omics.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_omics.types.get_annotation_store_request.GetAnnotationStoreRequest]",
        ) -> AsyncOperationResponse[
            "capo_omics.types.get_annotation_store_response.GetAnnotationStoreResponse"
        ]:
            import capo_omics._operations.omics.get_annotation_store

            (
                output,
                http_response,
            ) = await capo_omics._operations.omics.get_annotation_store.async_get_annotation_store(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_omics.types.get_annotation_store_request.GetAnnotationStoreRequest = {
            "name": name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_annotation_store(
        self,
        name: str,
        *,
        config_overrides: Optional[AsyncOmicsClientConfig] = None,
        description: Optional["capo_omics.types.description.Description"] = None,
    ) -> "capo_omics.types.update_annotation_store_response.UpdateAnnotationStoreResponse":
        """<important> <p>Amazon Web Services HealthOmics variant stores and annotation stores are no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see <a href="https://docs.aws.amazon.com/omics/latest/dev/variant-store-availability-change.html"> Amazon Web Services HealthOmics variant store and annotation store availability change</a>.</p> </important> <p>Updates an annotation store.</p>

        Args:
            name: <p>A name for the store.</p>
            description: <p>A description for the store.</p>

        Raises:
            capo_omics.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_omics.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred. Try the request again.</p>
            capo_omics.errors.resource_not_found_exception.ResourceNotFoundException: <p>The target resource was not found in the current Region.</p>
            capo_omics.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_omics.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_omics.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_omics.types.update_annotation_store_request.UpdateAnnotationStoreRequest]",
        ) -> AsyncOperationResponse[
            "capo_omics.types.update_annotation_store_response.UpdateAnnotationStoreResponse"
        ]:
            import capo_omics._operations.omics.update_annotation_store

            (
                output,
                http_response,
            ) = await capo_omics._operations.omics.update_annotation_store.async_update_annotation_store(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_omics.types.update_annotation_store_request.UpdateAnnotationStoreRequest = {
            "name": name
        }
        if description is not None:
            input_["description"] = description

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_annotation_store(
        self,
        name: str,
        *,
        config_overrides: Optional[AsyncOmicsClientConfig] = None,
        force: Optional[bool] = None,
    ) -> "capo_omics.types.delete_annotation_store_response.DeleteAnnotationStoreResponse":
        """<important> <p>Amazon Web Services HealthOmics variant stores and annotation stores are no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see <a href="https://docs.aws.amazon.com/omics/latest/dev/variant-store-availability-change.html"> Amazon Web Services HealthOmics variant store and annotation store availability change</a>.</p> </important> <p>Deletes an annotation store.</p>

        Args:
            name: <p>The store's name.</p>
            force: <p>Whether to force deletion.</p>

        Raises:
            capo_omics.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_omics.errors.conflict_exception.ConflictException: <p>The request cannot be applied to the target resource in its current state.</p>
            capo_omics.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred. Try the request again.</p>
            capo_omics.errors.resource_not_found_exception.ResourceNotFoundException: <p>The target resource was not found in the current Region.</p>
            capo_omics.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_omics.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_omics.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_omics.types.delete_annotation_store_request.DeleteAnnotationStoreRequest]",
        ) -> AsyncOperationResponse[
            "capo_omics.types.delete_annotation_store_response.DeleteAnnotationStoreResponse"
        ]:
            import capo_omics._operations.omics.delete_annotation_store

            (
                output,
                http_response,
            ) = await capo_omics._operations.omics.delete_annotation_store.async_delete_annotation_store(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_omics.types.delete_annotation_store_request.DeleteAnnotationStoreRequest = {
            "name": name
        }
        if force is not None:
            input_["force"] = force

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_annotation_stores(
        self,
        *,
        config_overrides: Optional[AsyncOmicsClientConfig] = None,
        ids: Optional["capo_omics.types.id_list.IdList"] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
        filter: Optional[
            "capo_omics.types.list_annotation_stores_filter.ListAnnotationStoresFilter"
        ] = None,
    ) -> (
        "capo_omics.types.list_annotation_stores_response.ListAnnotationStoresResponse"
    ):
        """<important> <p>Amazon Web Services HealthOmics variant stores and annotation stores are no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see <a href="https://docs.aws.amazon.com/omics/latest/dev/variant-store-availability-change.html"> Amazon Web Services HealthOmics variant store and annotation store availability change</a>.</p> </important> <p>Retrieves a list of annotation stores.</p>

        Args:
            ids: <p>IDs of stores to list.</p>
            max_results: <p>The maximum number of stores to return in one page of results.</p>
            next_token: <p>Specify the pagination token from a previous request to retrieve the next page of results.</p>
            filter: <p>A filter to apply to the list.</p>

        Raises:
            capo_omics.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_omics.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred. Try the request again.</p>
            capo_omics.errors.resource_not_found_exception.ResourceNotFoundException: <p>The target resource was not found in the current Region.</p>
            capo_omics.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_omics.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_omics.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_omics.types.list_annotation_stores_request.ListAnnotationStoresRequest]",
        ) -> AsyncOperationResponse[
            "capo_omics.types.list_annotation_stores_response.ListAnnotationStoresResponse"
        ]:
            import capo_omics._operations.omics.list_annotation_stores

            (
                output,
                http_response,
            ) = await capo_omics._operations.omics.list_annotation_stores.async_list_annotation_stores(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_omics.types.list_annotation_stores_request.ListAnnotationStoresRequest = {}
        if ids is not None:
            input_["ids"] = ids
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if filter is not None:
            input_["filter"] = filter

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_annotation_stores(
        self,
        *,
        config_overrides: Optional[AsyncOmicsClientConfig] = None,
        ids: Optional["capo_omics.types.id_list.IdList"] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
        filter: Optional[
            "capo_omics.types.list_annotation_stores_filter.ListAnnotationStoresFilter"
        ] = None,
    ) -> "AsyncIterator[capo_omics.types.annotation_store_item.AnnotationStoreItem]":
        _token = next_token
        while True:
            _response = await self.list_annotation_stores(
                config_overrides=config_overrides,
                ids=ids,
                max_results=max_results,
                next_token=_token,
                filter=filter,
            )
            _page = _resolve_path(_response, ("annotation_stores",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def create_annotation_store_version(
        self,
        name: "capo_omics.types.store_name.StoreName",
        version_name: "capo_omics.types.version_name.VersionName",
        *,
        config_overrides: Optional[AsyncOmicsClientConfig] = None,
        description: Optional["capo_omics.types.description.Description"] = None,
        version_options: Optional[
            "capo_omics.types.version_options.VersionOptions"
        ] = None,
        tags: Optional["capo_omics.types.tag_map.TagMap"] = None,
    ) -> "capo_omics.types.create_annotation_store_version_response.CreateAnnotationStoreVersionResponse":
        """<p> Creates a new version of an annotation store. </p>

        Args:
            name: <p> The name of an annotation store version from which versions are being created. </p>
            version_name: <p> The name given to an annotation store version to distinguish it from other versions. </p>
            description: <p> The description of an annotation store version. </p>
            version_options: <p> The options for an annotation store version. </p>
            tags: <p> Any tags added to annotation store version. </p>

        Raises:
            capo_omics.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_omics.errors.conflict_exception.ConflictException: <p>The request cannot be applied to the target resource in its current state.</p>
            capo_omics.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred. Try the request again.</p>
            capo_omics.errors.resource_not_found_exception.ResourceNotFoundException: <p>The target resource was not found in the current Region.</p>
            capo_omics.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request exceeds a service quota.</p>
            capo_omics.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_omics.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_omics.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_omics.types.create_annotation_store_version_request.CreateAnnotationStoreVersionRequest]",
        ) -> AsyncOperationResponse[
            "capo_omics.types.create_annotation_store_version_response.CreateAnnotationStoreVersionResponse"
        ]:
            import capo_omics._operations.omics.create_annotation_store_version

            (
                output,
                http_response,
            ) = await capo_omics._operations.omics.create_annotation_store_version.async_create_annotation_store_version(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_omics.types.create_annotation_store_version_request.CreateAnnotationStoreVersionRequest = {
            "name": name,
            "version_name": version_name,
        }
        if description is not None:
            input_["description"] = description
        if version_options is not None:
            input_["version_options"] = version_options
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_annotation_store_version(
        self,
        name: str,
        version_name: str,
        *,
        config_overrides: Optional[AsyncOmicsClientConfig] = None,
    ) -> "capo_omics.types.get_annotation_store_version_response.GetAnnotationStoreVersionResponse":
        """<p> Retrieves the metadata for an annotation store version. </p>

        Args:
            name: <p> The name given to an annotation store version to distinguish it from others. </p>
            version_name: <p> The name given to an annotation store version to distinguish it from others. </p>

        Raises:
            capo_omics.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_omics.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred. Try the request again.</p>
            capo_omics.errors.resource_not_found_exception.ResourceNotFoundException: <p>The target resource was not found in the current Region.</p>
            capo_omics.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_omics.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_omics.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_omics.types.get_annotation_store_version_request.GetAnnotationStoreVersionRequest]",
        ) -> AsyncOperationResponse[
            "capo_omics.types.get_annotation_store_version_response.GetAnnotationStoreVersionResponse"
        ]:
            import capo_omics._operations.omics.get_annotation_store_version

            (
                output,
                http_response,
            ) = await capo_omics._operations.omics.get_annotation_store_version.async_get_annotation_store_version(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_omics.types.get_annotation_store_version_request.GetAnnotationStoreVersionRequest = {
            "name": name,
            "version_name": version_name,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_annotation_store_version(
        self,
        name: str,
        version_name: str,
        *,
        config_overrides: Optional[AsyncOmicsClientConfig] = None,
        description: Optional["capo_omics.types.description.Description"] = None,
    ) -> "capo_omics.types.update_annotation_store_version_response.UpdateAnnotationStoreVersionResponse":
        """<p> Updates the description of an annotation store version. </p>

        Args:
            name: <p> The name of an annotation store. </p>
            version_name: <p> The name of an annotation store version. </p>
            description: <p> The description of an annotation store. </p>

        Raises:
            capo_omics.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_omics.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred. Try the request again.</p>
            capo_omics.errors.resource_not_found_exception.ResourceNotFoundException: <p>The target resource was not found in the current Region.</p>
            capo_omics.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_omics.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_omics.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_omics.types.update_annotation_store_version_request.UpdateAnnotationStoreVersionRequest]",
        ) -> AsyncOperationResponse[
            "capo_omics.types.update_annotation_store_version_response.UpdateAnnotationStoreVersionResponse"
        ]:
            import capo_omics._operations.omics.update_annotation_store_version

            (
                output,
                http_response,
            ) = await capo_omics._operations.omics.update_annotation_store_version.async_update_annotation_store_version(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_omics.types.update_annotation_store_version_request.UpdateAnnotationStoreVersionRequest = {
            "name": name,
            "version_name": version_name,
        }
        if description is not None:
            input_["description"] = description

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_annotation_store_versions(
        self,
        name: str,
        *,
        config_overrides: Optional[AsyncOmicsClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
        filter: Optional[
            "capo_omics.types.list_annotation_store_versions_filter.ListAnnotationStoreVersionsFilter"
        ] = None,
    ) -> "capo_omics.types.list_annotation_store_versions_response.ListAnnotationStoreVersionsResponse":
        """<p> Lists the versions of an annotation store. </p>

        Args:
            name: <p> The name of an annotation store. </p>
            max_results: <p> The maximum number of annotation store versions to return in one page of results. </p>
            next_token: <p> Specifies the pagination token from a previous request to retrieve the next page of results. </p>
            filter: <p> A filter to apply to the list of annotation store versions. </p>

        Raises:
            capo_omics.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_omics.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred. Try the request again.</p>
            capo_omics.errors.resource_not_found_exception.ResourceNotFoundException: <p>The target resource was not found in the current Region.</p>
            capo_omics.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_omics.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_omics.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_omics.types.list_annotation_store_versions_request.ListAnnotationStoreVersionsRequest]",
        ) -> AsyncOperationResponse[
            "capo_omics.types.list_annotation_store_versions_response.ListAnnotationStoreVersionsResponse"
        ]:
            import capo_omics._operations.omics.list_annotation_store_versions

            (
                output,
                http_response,
            ) = await capo_omics._operations.omics.list_annotation_store_versions.async_list_annotation_store_versions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_omics.types.list_annotation_store_versions_request.ListAnnotationStoreVersionsRequest = {
            "name": name
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if filter is not None:
            input_["filter"] = filter

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_annotation_store_versions(
        self,
        name: str,
        *,
        config_overrides: Optional[AsyncOmicsClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
        filter: Optional[
            "capo_omics.types.list_annotation_store_versions_filter.ListAnnotationStoreVersionsFilter"
        ] = None,
    ) -> "AsyncIterator[capo_omics.types.annotation_store_version_item.AnnotationStoreVersionItem]":
        _token = next_token
        while True:
            _response = await self.list_annotation_store_versions(
                name,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
                filter=filter,
            )
            _page = _resolve_path(_response, ("annotation_store_versions",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def delete_annotation_store_versions(
        self,
        name: str,
        versions: "capo_omics.types.version_list.VersionList",
        *,
        config_overrides: Optional[AsyncOmicsClientConfig] = None,
        force: Optional[bool] = None,
    ) -> "capo_omics.types.delete_annotation_store_versions_response.DeleteAnnotationStoreVersionsResponse":
        """<p> Deletes one or multiple versions of an annotation store. </p>

        Args:
            name: <p> The name of the annotation store from which versions are being deleted. </p>
            versions: <p> The versions of an annotation store to be deleted. </p>
            force: <p> Forces the deletion of an annotation store version when imports are in-progress.. </p>

        Raises:
            capo_omics.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_omics.errors.conflict_exception.ConflictException: <p>The request cannot be applied to the target resource in its current state.</p>
            capo_omics.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred. Try the request again.</p>
            capo_omics.errors.resource_not_found_exception.ResourceNotFoundException: <p>The target resource was not found in the current Region.</p>
            capo_omics.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_omics.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_omics.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_omics.types.delete_annotation_store_versions_request.DeleteAnnotationStoreVersionsRequest]",
        ) -> AsyncOperationResponse[
            "capo_omics.types.delete_annotation_store_versions_response.DeleteAnnotationStoreVersionsResponse"
        ]:
            import capo_omics._operations.omics.delete_annotation_store_versions

            (
                output,
                http_response,
            ) = await capo_omics._operations.omics.delete_annotation_store_versions.async_delete_annotation_store_versions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_omics.types.delete_annotation_store_versions_request.DeleteAnnotationStoreVersionsRequest = {
            "name": name,
            "versions": versions,
        }
        if force is not None:
            input_["force"] = force

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_configuration(
        self,
        name: "capo_omics.types.configuration_name.ConfigurationName",
        run_configurations: "capo_omics.types.run_configurations.RunConfigurations",
        request_id: "capo_omics.types.configuration_request_id.ConfigurationRequestId",
        *,
        config_overrides: Optional[AsyncOmicsClientConfig] = None,
        description: Optional[
            "capo_omics.types.configuration_description.ConfigurationDescription"
        ] = None,
        tags: Optional["capo_omics.types.tag_map.TagMap"] = None,
    ) -> "capo_omics.types.create_configuration_response.CreateConfigurationResponse":
        """<p>Create a new configuration.</p>

        Args:
            name: <p>User-friendly name for the configuration.</p>
            description: <p>Optional description for the configuration.</p>
            run_configurations: <p>Required run-specific configurations.</p>
            tags: <p>Optional tags for the configuration.</p>
            request_id: <p>Optional request idempotency token. If not specified, a universally unique identifier (UUID) will be automatically generated for the request.</p>

        Raises:
            capo_omics.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_omics.errors.conflict_exception.ConflictException: <p>The request cannot be applied to the target resource in its current state.</p>
            capo_omics.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred. Try the request again.</p>
            capo_omics.errors.request_timeout_exception.RequestTimeoutException: <p>The request timed out.</p>
            capo_omics.errors.resource_not_found_exception.ResourceNotFoundException: <p>The target resource was not found in the current Region.</p>
            capo_omics.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request exceeds a service quota.</p>
            capo_omics.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_omics.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_omics.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_omics.types.create_configuration_request.CreateConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "capo_omics.types.create_configuration_response.CreateConfigurationResponse"
        ]:
            import capo_omics._operations.omics.create_configuration

            (
                output,
                http_response,
            ) = await capo_omics._operations.omics.create_configuration.async_create_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_omics.types.create_configuration_request.CreateConfigurationRequest = {
            "name": name,
            "run_configurations": run_configurations,
            "request_id": request_id,
        }
        if description is not None:
            input_["description"] = description
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_configuration(
        self,
        name: "capo_omics.types.configuration_name.ConfigurationName",
        *,
        config_overrides: Optional[AsyncOmicsClientConfig] = None,
    ) -> "capo_omics.types.get_configuration_response.GetConfigurationResponse":
        """<p>Retrieve configuration details for specified name.</p>

        Args:
            name: <p>Configuration name to retrieve.</p>

        Raises:
            capo_omics.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_omics.errors.conflict_exception.ConflictException: <p>The request cannot be applied to the target resource in its current state.</p>
            capo_omics.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred. Try the request again.</p>
            capo_omics.errors.request_timeout_exception.RequestTimeoutException: <p>The request timed out.</p>
            capo_omics.errors.resource_not_found_exception.ResourceNotFoundException: <p>The target resource was not found in the current Region.</p>
            capo_omics.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request exceeds a service quota.</p>
            capo_omics.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_omics.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_omics.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_omics.types.get_configuration_request.GetConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "capo_omics.types.get_configuration_response.GetConfigurationResponse"
        ]:
            import capo_omics._operations.omics.get_configuration

            (
                output,
                http_response,
            ) = await capo_omics._operations.omics.get_configuration.async_get_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_omics.types.get_configuration_request.GetConfigurationRequest = {
            "name": name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_configuration(
        self,
        name: "capo_omics.types.configuration_name.ConfigurationName",
        *,
        config_overrides: Optional[AsyncOmicsClientConfig] = None,
    ) -> None:
        """<p>Delete an existing configuration.</p>

        Args:
            name: <p>Configuration name to delete.</p>

        Raises:
            capo_omics.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_omics.errors.conflict_exception.ConflictException: <p>The request cannot be applied to the target resource in its current state.</p>
            capo_omics.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred. Try the request again.</p>
            capo_omics.errors.request_timeout_exception.RequestTimeoutException: <p>The request timed out.</p>
            capo_omics.errors.resource_not_found_exception.ResourceNotFoundException: <p>The target resource was not found in the current Region.</p>
            capo_omics.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request exceeds a service quota.</p>
            capo_omics.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_omics.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_omics.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_omics.types.delete_configuration_request.DeleteConfigurationRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_omics._operations.omics.delete_configuration

            (
                output,
                http_response,
            ) = await capo_omics._operations.omics.delete_configuration.async_delete_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_omics.types.delete_configuration_request.DeleteConfigurationRequest = {
            "name": name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_configurations(
        self,
        *,
        config_overrides: Optional[AsyncOmicsClientConfig] = None,
        max_results: Optional[int] = None,
        starting_token: Optional[
            "capo_omics.types.configuration_list_token.ConfigurationListToken"
        ] = None,
    ) -> "capo_omics.types.list_configurations_response.ListConfigurationsResponse":
        """<p>List all configurations for the account.</p>

        Args:
            max_results: <p>Maximum number of results to return.</p>
            starting_token: <p>Pagination token for retrieving next page of results.</p>

        Raises:
            capo_omics.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_omics.errors.conflict_exception.ConflictException: <p>The request cannot be applied to the target resource in its current state.</p>
            capo_omics.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred. Try the request again.</p>
            capo_omics.errors.request_timeout_exception.RequestTimeoutException: <p>The request timed out.</p>
            capo_omics.errors.resource_not_found_exception.ResourceNotFoundException: <p>The target resource was not found in the current Region.</p>
            capo_omics.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request exceeds a service quota.</p>
            capo_omics.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_omics.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_omics.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_omics.types.list_configurations_request.ListConfigurationsRequest]",
        ) -> AsyncOperationResponse[
            "capo_omics.types.list_configurations_response.ListConfigurationsResponse"
        ]:
            import capo_omics._operations.omics.list_configurations

            (
                output,
                http_response,
            ) = await capo_omics._operations.omics.list_configurations.async_list_configurations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_omics.types.list_configurations_request.ListConfigurationsRequest = {}
        if max_results is not None:
            input_["max_results"] = max_results
        if starting_token is not None:
            input_["starting_token"] = starting_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_configurations(
        self,
        *,
        config_overrides: Optional[AsyncOmicsClientConfig] = None,
        max_results: Optional[int] = None,
        starting_token: Optional[
            "capo_omics.types.configuration_list_token.ConfigurationListToken"
        ] = None,
    ) -> (
        "AsyncIterator[capo_omics.types.configuration_list_item.ConfigurationListItem]"
    ):
        _token = starting_token
        while True:
            _response = await self.list_configurations(
                config_overrides=config_overrides,
                max_results=max_results,
                starting_token=_token,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def create_reference_store(
        self,
        name: "capo_omics.types.reference_store_name.ReferenceStoreName",
        *,
        config_overrides: Optional[AsyncOmicsClientConfig] = None,
        description: Optional[
            "capo_omics.types.reference_store_description.ReferenceStoreDescription"
        ] = None,
        sse_config: Optional["capo_omics.types.sse_config.SseConfig"] = None,
        tags: Optional["capo_omics.types.tag_map.TagMap"] = None,
        client_token: Optional["capo_omics.types.client_token.ClientToken"] = None,
    ) -> (
        "capo_omics.types.create_reference_store_response.CreateReferenceStoreResponse"
    ):
        """<p>Creates a reference store and returns metadata in JSON format. Reference stores are used to store reference genomes in FASTA format. A reference store is created when the first reference genome is imported. To import additional reference genomes from an Amazon S3 bucket, use the <code>StartReferenceImportJob</code> API operation. </p> <p>For more information, see <a href="https://docs.aws.amazon.com/omics/latest/dev/create-reference-store.html">Creating a HealthOmics reference store</a> in the <i>Amazon Web Services HealthOmics User Guide</i>.</p>

        Args:
            name: <p>A name for the store.</p>
            description: <p>A description for the store.</p>
            sse_config: <p>Server-side encryption (SSE) settings for the store.</p>
            tags: <p>Tags for the store.</p>
            client_token: <p>To ensure that requests don't run multiple times, specify a unique token for each request.</p>

        Raises:
            capo_omics.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_omics.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred. Try the request again.</p>
            capo_omics.errors.request_timeout_exception.RequestTimeoutException: <p>The request timed out.</p>
            capo_omics.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request exceeds a service quota.</p>
            capo_omics.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_omics.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_omics.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_omics.types.create_reference_store_request.CreateReferenceStoreRequest]",
        ) -> AsyncOperationResponse[
            "capo_omics.types.create_reference_store_response.CreateReferenceStoreResponse"
        ]:
            import capo_omics._operations.omics.create_reference_store

            (
                output,
                http_response,
            ) = await capo_omics._operations.omics.create_reference_store.async_create_reference_store(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_omics.types.create_reference_store_request.CreateReferenceStoreRequest = {
            "name": name
        }
        if description is not None:
            input_["description"] = description
        if sse_config is not None:
            input_["sse_config"] = sse_config
        if tags is not None:
            input_["tags"] = tags
        if client_token is not None:
            input_["client_token"] = client_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_reference_store(
        self,
        id: "capo_omics.types.reference_store_id.ReferenceStoreId",
        *,
        config_overrides: Optional[AsyncOmicsClientConfig] = None,
    ) -> "capo_omics.types.get_reference_store_response.GetReferenceStoreResponse":
        """<p>Gets information about a reference store.</p>

        Args:
            id: <p>The store's ID.</p>

        Raises:
            capo_omics.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_omics.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred. Try the request again.</p>
            capo_omics.errors.request_timeout_exception.RequestTimeoutException: <p>The request timed out.</p>
            capo_omics.errors.resource_not_found_exception.ResourceNotFoundException: <p>The target resource was not found in the current Region.</p>
            capo_omics.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_omics.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_omics.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_omics.types.get_reference_store_request.GetReferenceStoreRequest]",
        ) -> AsyncOperationResponse[
            "capo_omics.types.get_reference_store_response.GetReferenceStoreResponse"
        ]:
            import capo_omics._operations.omics.get_reference_store

            (
                output,
                http_response,
            ) = await capo_omics._operations.omics.get_reference_store.async_get_reference_store(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_omics.types.get_reference_store_request.GetReferenceStoreRequest = {
            "id": id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_reference_store(
        self,
        id: "capo_omics.types.reference_store_id.ReferenceStoreId",
        *,
        config_overrides: Optional[AsyncOmicsClientConfig] = None,
    ) -> (
        "capo_omics.types.delete_reference_store_response.DeleteReferenceStoreResponse"
    ):
        """<p>Deletes a reference store and returns a response with no body if the operation is successful. You can only delete a reference store when it does not contain any reference genomes. To empty a reference store, use <code>DeleteReference</code>.</p> <p>For more information about your workflow status, see <a href="https://docs.aws.amazon.com/omics/latest/dev/deleting-reference-and-sequence-stores.html">Deleting HealthOmics reference and sequence stores</a> in the <i>Amazon Web Services HealthOmics User Guide</i>.</p>

        Args:
            id: <p>The store's ID.</p>

        Raises:
            capo_omics.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_omics.errors.conflict_exception.ConflictException: <p>The request cannot be applied to the target resource in its current state.</p>
            capo_omics.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred. Try the request again.</p>
            capo_omics.errors.request_timeout_exception.RequestTimeoutException: <p>The request timed out.</p>
            capo_omics.errors.resource_not_found_exception.ResourceNotFoundException: <p>The target resource was not found in the current Region.</p>
            capo_omics.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_omics.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_omics.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_omics.types.delete_reference_store_request.DeleteReferenceStoreRequest]",
        ) -> AsyncOperationResponse[
            "capo_omics.types.delete_reference_store_response.DeleteReferenceStoreResponse"
        ]:
            import capo_omics._operations.omics.delete_reference_store

            (
                output,
                http_response,
            ) = await capo_omics._operations.omics.delete_reference_store.async_delete_reference_store(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_omics.types.delete_reference_store_request.DeleteReferenceStoreRequest = {
            "id": id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_reference_stores(
        self,
        *,
        config_overrides: Optional[AsyncOmicsClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional["capo_omics.types.next_token.NextToken"] = None,
        filter: Optional[
            "capo_omics.types.reference_store_filter.ReferenceStoreFilter"
        ] = None,
    ) -> "capo_omics.types.list_reference_stores_response.ListReferenceStoresResponse":
        """<p>Retrieves a list of reference stores linked to your account and returns their metadata in JSON format.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/omics/latest/dev/create-reference-store.html">Creating a reference store</a> in the <i>Amazon Web Services HealthOmics User Guide</i>.</p>

        Args:
            max_results: <p>The maximum number of stores to return in one page of results.</p>
            next_token: <p>Specify the pagination token from a previous request to retrieve the next page of results.</p>
            filter: <p>A filter to apply to the list.</p>

        Raises:
            capo_omics.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_omics.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred. Try the request again.</p>
            capo_omics.errors.request_timeout_exception.RequestTimeoutException: <p>The request timed out.</p>
            capo_omics.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_omics.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_omics.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_omics.types.list_reference_stores_request.ListReferenceStoresRequest]",
        ) -> AsyncOperationResponse[
            "capo_omics.types.list_reference_stores_response.ListReferenceStoresResponse"
        ]:
            import capo_omics._operations.omics.list_reference_stores

            (
                output,
                http_response,
            ) = await capo_omics._operations.omics.list_reference_stores.async_list_reference_stores(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_omics.types.list_reference_stores_request.ListReferenceStoresRequest = {}
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if filter is not None:
            input_["filter"] = filter

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_reference_stores(
        self,
        *,
        config_overrides: Optional[AsyncOmicsClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional["capo_omics.types.next_token.NextToken"] = None,
        filter: Optional[
            "capo_omics.types.reference_store_filter.ReferenceStoreFilter"
        ] = None,
    ) -> "AsyncIterator[capo_omics.types.reference_store_detail.ReferenceStoreDetail]":
        _token = next_token
        while True:
            _response = await self.list_reference_stores(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
                filter=filter,
            )
            _page = _resolve_path(_response, ("reference_stores",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def get_reference_import_job(
        self,
        id: "capo_omics.types.import_job_id.ImportJobId",
        reference_store_id: "capo_omics.types.reference_store_id.ReferenceStoreId",
        *,
        config_overrides: Optional[AsyncOmicsClientConfig] = None,
    ) -> "capo_omics.types.get_reference_import_job_response.GetReferenceImportJobResponse":
        """<p>Monitors the status of a reference import job. This operation can be called after calling the <code>StartReferenceImportJob</code> operation.</p>

        Args:
            id: <p>The job's ID.</p>
            reference_store_id: <p>The job's reference store ID.</p>

        Raises:
            capo_omics.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_omics.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred. Try the request again.</p>
            capo_omics.errors.request_timeout_exception.RequestTimeoutException: <p>The request timed out.</p>
            capo_omics.errors.resource_not_found_exception.ResourceNotFoundException: <p>The target resource was not found in the current Region.</p>
            capo_omics.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_omics.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_omics.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_omics.types.get_reference_import_job_request.GetReferenceImportJobRequest]",
        ) -> AsyncOperationResponse[
            "capo_omics.types.get_reference_import_job_response.GetReferenceImportJobResponse"
        ]:
            import capo_omics._operations.omics.get_reference_import_job

            (
                output,
                http_response,
            ) = await capo_omics._operations.omics.get_reference_import_job.async_get_reference_import_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_omics.types.get_reference_import_job_request.GetReferenceImportJobRequest = {
            "id": id,
            "reference_store_id": reference_store_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_reference_import_jobs(
        self,
        reference_store_id: "capo_omics.types.reference_store_id.ReferenceStoreId",
        *,
        config_overrides: Optional[AsyncOmicsClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional["capo_omics.types.next_token.NextToken"] = None,
        filter: Optional[
            "capo_omics.types.import_reference_filter.ImportReferenceFilter"
        ] = None,
    ) -> "capo_omics.types.list_reference_import_jobs_response.ListReferenceImportJobsResponse":
        """<p>Retrieves the metadata of one or more reference import jobs for a reference store.</p>

        Args:
            max_results: <p>The maximum number of jobs to return in one page of results.</p>
            next_token: <p>Specify the pagination token from a previous request to retrieve the next page of results.</p>
            reference_store_id: <p>The job's reference store ID.</p>
            filter: <p>A filter to apply to the list.</p>

        Raises:
            capo_omics.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_omics.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred. Try the request again.</p>
            capo_omics.errors.request_timeout_exception.RequestTimeoutException: <p>The request timed out.</p>
            capo_omics.errors.resource_not_found_exception.ResourceNotFoundException: <p>The target resource was not found in the current Region.</p>
            capo_omics.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_omics.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_omics.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_omics.types.list_reference_import_jobs_request.ListReferenceImportJobsRequest]",
        ) -> AsyncOperationResponse[
            "capo_omics.types.list_reference_import_jobs_response.ListReferenceImportJobsResponse"
        ]:
            import capo_omics._operations.omics.list_reference_import_jobs

            (
                output,
                http_response,
            ) = await capo_omics._operations.omics.list_reference_import_jobs.async_list_reference_import_jobs(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_omics.types.list_reference_import_jobs_request.ListReferenceImportJobsRequest = {
            "reference_store_id": reference_store_id
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if filter is not None:
            input_["filter"] = filter

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_reference_import_jobs(
        self,
        reference_store_id: "capo_omics.types.reference_store_id.ReferenceStoreId",
        *,
        config_overrides: Optional[AsyncOmicsClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional["capo_omics.types.next_token.NextToken"] = None,
        filter: Optional[
            "capo_omics.types.import_reference_filter.ImportReferenceFilter"
        ] = None,
    ) -> "AsyncIterator[capo_omics.types.import_reference_job_item.ImportReferenceJobItem]":
        _token = next_token
        while True:
            _response = await self.list_reference_import_jobs(
                reference_store_id,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
                filter=filter,
            )
            _page = _resolve_path(_response, ("import_jobs",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def start_reference_import_job(
        self,
        reference_store_id: "capo_omics.types.reference_store_id.ReferenceStoreId",
        role_arn: "capo_omics.types.role_arn.RoleArn",
        sources: "capo_omics.types.start_reference_import_job_source_list.StartReferenceImportJobSourceList",
        *,
        config_overrides: Optional[AsyncOmicsClientConfig] = None,
        client_token: Optional["capo_omics.types.client_token.ClientToken"] = None,
    ) -> "capo_omics.types.start_reference_import_job_response.StartReferenceImportJobResponse":
        """<p>Imports a reference genome from Amazon S3 into a specified reference store. You can have multiple reference genomes in a reference store. You can only import reference genomes one at a time into each reference store. Monitor the status of your reference import job by using the <code>GetReferenceImportJob</code> API operation.</p>

        Args:
            reference_store_id: <p>The job's reference store ID.</p>
            role_arn: <p>A service role for the job.</p>
            client_token: <p>To ensure that jobs don't run multiple times, specify a unique token for each job.</p>
            sources: <p>The job's source files.</p>

        Raises:
            capo_omics.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_omics.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred. Try the request again.</p>
            capo_omics.errors.request_timeout_exception.RequestTimeoutException: <p>The request timed out.</p>
            capo_omics.errors.resource_not_found_exception.ResourceNotFoundException: <p>The target resource was not found in the current Region.</p>
            capo_omics.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request exceeds a service quota.</p>
            capo_omics.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_omics.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_omics.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_omics.types.start_reference_import_job_request.StartReferenceImportJobRequest]",
        ) -> AsyncOperationResponse[
            "capo_omics.types.start_reference_import_job_response.StartReferenceImportJobResponse"
        ]:
            import capo_omics._operations.omics.start_reference_import_job

            (
                output,
                http_response,
            ) = await capo_omics._operations.omics.start_reference_import_job.async_start_reference_import_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_omics.types.start_reference_import_job_request.StartReferenceImportJobRequest = {
            "reference_store_id": reference_store_id,
            "role_arn": role_arn,
            "sources": sources,
        }
        if client_token is not None:
            input_["client_token"] = client_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_reference_metadata(
        self,
        id: "capo_omics.types.reference_id.ReferenceId",
        reference_store_id: "capo_omics.types.reference_store_id.ReferenceStoreId",
        *,
        config_overrides: Optional[AsyncOmicsClientConfig] = None,
    ) -> (
        "capo_omics.types.get_reference_metadata_response.GetReferenceMetadataResponse"
    ):
        """<p>Retrieves metadata for a reference genome. This operation returns the number of parts, part size, and MD5 of an entire file. This operation does not return tags. To retrieve the list of tags for a read set, use the <code>ListTagsForResource</code> API operation.</p>

        Args:
            id: <p>The reference's ID.</p>
            reference_store_id: <p>The reference's reference store ID.</p>

        Raises:
            capo_omics.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_omics.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred. Try the request again.</p>
            capo_omics.errors.request_timeout_exception.RequestTimeoutException: <p>The request timed out.</p>
            capo_omics.errors.resource_not_found_exception.ResourceNotFoundException: <p>The target resource was not found in the current Region.</p>
            capo_omics.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_omics.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_omics.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_omics.types.get_reference_metadata_request.GetReferenceMetadataRequest]",
        ) -> AsyncOperationResponse[
            "capo_omics.types.get_reference_metadata_response.GetReferenceMetadataResponse"
        ]:
            import capo_omics._operations.omics.get_reference_metadata

            (
                output,
                http_response,
            ) = await capo_omics._operations.omics.get_reference_metadata.async_get_reference_metadata(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_omics.types.get_reference_metadata_request.GetReferenceMetadataRequest = {
            "id": id,
            "reference_store_id": reference_store_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_reference(
        self,
        id: "capo_omics.types.reference_id.ReferenceId",
        reference_store_id: "capo_omics.types.reference_store_id.ReferenceStoreId",
        *,
        config_overrides: Optional[AsyncOmicsClientConfig] = None,
    ) -> "capo_omics.types.delete_reference_response.DeleteReferenceResponse":
        """<p>Deletes a reference genome and returns a response with no body if the operation is successful. The read set associated with the reference genome must first be deleted before deleting the reference genome. After the reference genome is deleted, you can delete the reference store using the <code>DeleteReferenceStore</code> API operation.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/omics/latest/dev/deleting-reference-and-sequence-stores.html">Deleting HealthOmics reference and sequence stores</a> in the <i>Amazon Web Services HealthOmics User Guide</i>.</p>

        Args:
            id: <p>The reference's ID.</p>
            reference_store_id: <p>The reference's store ID.</p>

        Raises:
            capo_omics.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_omics.errors.conflict_exception.ConflictException: <p>The request cannot be applied to the target resource in its current state.</p>
            capo_omics.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred. Try the request again.</p>
            capo_omics.errors.request_timeout_exception.RequestTimeoutException: <p>The request timed out.</p>
            capo_omics.errors.resource_not_found_exception.ResourceNotFoundException: <p>The target resource was not found in the current Region.</p>
            capo_omics.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_omics.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_omics.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_omics.types.delete_reference_request.DeleteReferenceRequest]",
        ) -> AsyncOperationResponse[
            "capo_omics.types.delete_reference_response.DeleteReferenceResponse"
        ]:
            import capo_omics._operations.omics.delete_reference

            (
                output,
                http_response,
            ) = await capo_omics._operations.omics.delete_reference.async_delete_reference(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_omics.types.delete_reference_request.DeleteReferenceRequest = {
            "id": id,
            "reference_store_id": reference_store_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_references(
        self,
        reference_store_id: "capo_omics.types.reference_store_id.ReferenceStoreId",
        *,
        config_overrides: Optional[AsyncOmicsClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional["capo_omics.types.next_token.NextToken"] = None,
        filter: Optional["capo_omics.types.reference_filter.ReferenceFilter"] = None,
    ) -> "capo_omics.types.list_references_response.ListReferencesResponse":
        """<p>Retrieves the metadata of one or more reference genomes in a reference store.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/omics/latest/dev/create-reference-store.html">Creating a reference store</a> in the <i>Amazon Web Services HealthOmics User Guide</i>.</p>

        Args:
            reference_store_id: <p>The references' reference store ID.</p>
            max_results: <p>The maximum number of references to return in one page of results.</p>
            next_token: <p>Specify the pagination token from a previous request to retrieve the next page of results.</p>
            filter: <p>A filter to apply to the list.</p>

        Raises:
            capo_omics.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_omics.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred. Try the request again.</p>
            capo_omics.errors.request_timeout_exception.RequestTimeoutException: <p>The request timed out.</p>
            capo_omics.errors.resource_not_found_exception.ResourceNotFoundException: <p>The target resource was not found in the current Region.</p>
            capo_omics.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_omics.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_omics.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_omics.types.list_references_request.ListReferencesRequest]",
        ) -> AsyncOperationResponse[
            "capo_omics.types.list_references_response.ListReferencesResponse"
        ]:
            import capo_omics._operations.omics.list_references

            (
                output,
                http_response,
            ) = await capo_omics._operations.omics.list_references.async_list_references(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_omics.types.list_references_request.ListReferencesRequest = {
            "reference_store_id": reference_store_id
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if filter is not None:
            input_["filter"] = filter

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_references(
        self,
        reference_store_id: "capo_omics.types.reference_store_id.ReferenceStoreId",
        *,
        config_overrides: Optional[AsyncOmicsClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional["capo_omics.types.next_token.NextToken"] = None,
        filter: Optional["capo_omics.types.reference_filter.ReferenceFilter"] = None,
    ) -> "AsyncIterator[capo_omics.types.reference_list_item.ReferenceListItem]":
        _token = next_token
        while True:
            _response = await self.list_references(
                reference_store_id,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
                filter=filter,
            )
            _page = _resolve_path(_response, ("references",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    @asynccontextmanager
    async def get_reference(
        self,
        id: "capo_omics.types.reference_id.ReferenceId",
        reference_store_id: "capo_omics.types.reference_store_id.ReferenceStoreId",
        part_number: int,
        *,
        config_overrides: Optional[AsyncOmicsClientConfig] = None,
        range: Optional["capo_omics.types.range.Range"] = None,
        file: Optional["capo_omics.types.reference_file.ReferenceFile"] = None,
    ) -> "AsyncGenerator[capo_omics.types.get_reference_response.GetReferenceResponse]":
        """<p>Downloads parts of data from a reference genome and returns the reference file in the same format that it was uploaded.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/omics/latest/dev/create-reference-store.html">Creating a HealthOmics reference store</a> in the <i>Amazon Web Services HealthOmics User Guide</i>.</p>

        Args:
            id: <p>The reference's ID.</p>
            reference_store_id: <p>The reference's store ID.</p>
            range: <p>The range to retrieve.</p>
            part_number: <p>The part number to retrieve.</p>
            file: <p>The file to retrieve.</p>

        Raises:
            capo_omics.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_omics.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred. Try the request again.</p>
            capo_omics.errors.range_not_satisfiable_exception.RangeNotSatisfiableException: <p>The ranges specified in the request are not valid.</p>
            capo_omics.errors.request_timeout_exception.RequestTimeoutException: <p>The request timed out.</p>
            capo_omics.errors.resource_not_found_exception.ResourceNotFoundException: <p>The target resource was not found in the current Region.</p>
            capo_omics.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_omics.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_omics.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_omics.types.get_reference_request.GetReferenceRequest]",
        ) -> AsyncOperationResponse[
            "capo_omics.types.get_reference_response.GetReferenceResponse"
        ]:
            import capo_omics._operations.omics.get_reference

            (
                output,
                http_response,
            ) = await capo_omics._operations.omics.get_reference.async_get_reference(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_omics.types.get_reference_request.GetReferenceRequest = {
            "id": id,
            "reference_store_id": reference_store_id,
            "part_number": part_number,
        }
        if range is not None:
            input_["range"] = range
        if file is not None:
            input_["file"] = file

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        try:
            yield response.output
        finally:
            await response.response.aclose()

    async def start_run_batch(
        self,
        request_id: "capo_omics.types.batch_request_id.BatchRequestId",
        default_run_setting: "capo_omics.types.default_run_setting.DefaultRunSetting",
        batch_run_settings: "capo_omics.types.batch_run_settings.BatchRunSettings",
        *,
        config_overrides: Optional[AsyncOmicsClientConfig] = None,
        batch_name: Optional["capo_omics.types.batch_name.BatchName"] = None,
        tags: Optional["capo_omics.types.tag_map.TagMap"] = None,
    ) -> "capo_omics.types.start_run_batch_response.StartRunBatchResponse":
        """<p>Starts a batch of workflow runs. You can group up to 100,000 runs into a single batch that share a common configuration defined in <code>defaultRunSetting</code>. Per-run overrides can be provided either inline via <code>inlineSettings</code> (up to 100 runs) or via a JSON file stored in Amazon S3 via <code>s3UriSettings</code> (up to 100,000 runs).</p> <p> <code>StartRunBatch</code> validates common fields synchronously and returns immediately with a batch ID and status <code>CREATING</code>. The batch transitions to <code>PENDING</code> once initial setup completes. Runs are then submitted gradually and asynchronously at a rate governed by your <code>StartRun</code> throughput quota.</p>

        Args:
            batch_name: <p>An optional user-friendly name for the run batch.</p>
            request_id: <p>A client token used to deduplicate retry requests and prevent duplicate batches from being created.</p>
            tags: <p>Amazon Web Services tags to associate with the batch resource. These tags are not inherited by individual runs. To tag individual runs, use <code>defaultRunSetting.runTags</code>.</p>
            default_run_setting: <p>Shared configuration applied to all runs in the batch. See <code>DefaultRunSetting</code>.</p>
            batch_run_settings: <p>The individual run configurations. Specify exactly one of <code>inlineSettings</code> or <code>s3UriSettings</code>. See <code>BatchRunSettings</code>.</p>

        Raises:
            capo_omics.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_omics.errors.conflict_exception.ConflictException: <p>The request cannot be applied to the target resource in its current state.</p>
            capo_omics.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred. Try the request again.</p>
            capo_omics.errors.request_timeout_exception.RequestTimeoutException: <p>The request timed out.</p>
            capo_omics.errors.resource_not_found_exception.ResourceNotFoundException: <p>The target resource was not found in the current Region.</p>
            capo_omics.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request exceeds a service quota.</p>
            capo_omics.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_omics.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_omics.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_omics.types.start_run_batch_request.StartRunBatchRequest]",
        ) -> AsyncOperationResponse[
            "capo_omics.types.start_run_batch_response.StartRunBatchResponse"
        ]:
            import capo_omics._operations.omics.start_run_batch

            (
                output,
                http_response,
            ) = await capo_omics._operations.omics.start_run_batch.async_start_run_batch(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_omics.types.start_run_batch_request.StartRunBatchRequest = {
            "request_id": request_id,
            "default_run_setting": default_run_setting,
            "batch_run_settings": batch_run_settings,
        }
        if batch_name is not None:
            input_["batch_name"] = batch_name
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_batch(
        self,
        batch_id: "capo_omics.types.batch_id.BatchId",
        *,
        config_overrides: Optional[AsyncOmicsClientConfig] = None,
    ) -> "capo_omics.types.get_batch_response.GetBatchResponse":
        """<p>Retrieves details and current status for a specific run batch, including submission progress and run execution counts.</p>

        Args:
            batch_id: <p>The identifier portion of the run batch ARN.</p>

        Raises:
            capo_omics.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_omics.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred. Try the request again.</p>
            capo_omics.errors.request_timeout_exception.RequestTimeoutException: <p>The request timed out.</p>
            capo_omics.errors.resource_not_found_exception.ResourceNotFoundException: <p>The target resource was not found in the current Region.</p>
            capo_omics.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_omics.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_omics.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_omics.types.get_batch_request.GetBatchRequest]",
        ) -> AsyncOperationResponse[
            "capo_omics.types.get_batch_response.GetBatchResponse"
        ]:
            import capo_omics._operations.omics.get_batch

            (
                output,
                http_response,
            ) = await capo_omics._operations.omics.get_batch.async_get_batch(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_omics.types.get_batch_request.GetBatchRequest = {
            "batch_id": batch_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_batch(
        self,
        batch_id: "capo_omics.types.batch_id.BatchId",
        *,
        config_overrides: Optional[AsyncOmicsClientConfig] = None,
    ) -> None:
        """<p>Deletes a run batch resource and its associated metadata. This operation does not delete the individual workflow runs. To delete the runs, call <code>DeleteRunBatch</code> before calling <code>DeleteBatch</code>.</p> <p> <code>DeleteBatch</code> requires the batch to be in a terminal state: <code>PROCESSED</code>, <code>FAILED</code>, <code>CANCELLED</code>, <code>RUNS_DELETE_FAILED</code>, or <code>RUNS_DELETED</code>. After <code>DeleteBatch</code> completes, the batch metadata is no longer accessible. You cannot call <code>GetBatch</code>, <code>ListRunsInBatch</code>, <code>DeleteRunBatch</code>, or <code>CancelRunBatch</code> on a deleted batch.</p>

        Args:
            batch_id: <p>The identifier portion of the run batch ARN.</p>

        Raises:
            capo_omics.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_omics.errors.conflict_exception.ConflictException: <p>The request cannot be applied to the target resource in its current state.</p>
            capo_omics.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred. Try the request again.</p>
            capo_omics.errors.request_timeout_exception.RequestTimeoutException: <p>The request timed out.</p>
            capo_omics.errors.resource_not_found_exception.ResourceNotFoundException: <p>The target resource was not found in the current Region.</p>
            capo_omics.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request exceeds a service quota.</p>
            capo_omics.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_omics.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_omics.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_omics.types.delete_batch_request.DeleteBatchRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_omics._operations.omics.delete_batch

            (
                output,
                http_response,
            ) = await capo_omics._operations.omics.delete_batch.async_delete_batch(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_omics.types.delete_batch_request.DeleteBatchRequest = {
            "batch_id": batch_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_batch(
        self,
        *,
        config_overrides: Optional[AsyncOmicsClientConfig] = None,
        max_items: Optional[int] = None,
        starting_token: Optional["capo_omics.types.list_token.ListToken"] = None,
        status: Optional["capo_omics.types.batch_status.BatchStatus"] = None,
        name: Optional["capo_omics.types.batch_name.BatchName"] = None,
        run_group_id: Optional["capo_omics.types.run_group_id.RunGroupId"] = None,
    ) -> "capo_omics.types.list_batch_response.ListBatchResponse":
        """<p>Returns a list of run batches in your account, with optional filtering by status, name, or run group. Results are paginated. Only one filter per call is supported.</p>

        Args:
            max_items: <p>The maximum number of batches to return. If not specified, defaults to 100.</p>
            starting_token: <p>A pagination token returned from a prior <code>ListBatch</code> call.</p>
            status: <p>Filter batches by status.</p>
            name: <p>Filter batches by name.</p>
            run_group_id: <p>Filter batches by run group ID.</p>

        Raises:
            capo_omics.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_omics.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred. Try the request again.</p>
            capo_omics.errors.request_timeout_exception.RequestTimeoutException: <p>The request timed out.</p>
            capo_omics.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_omics.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_omics.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_omics.types.list_batch_request.ListBatchRequest]",
        ) -> AsyncOperationResponse[
            "capo_omics.types.list_batch_response.ListBatchResponse"
        ]:
            import capo_omics._operations.omics.list_batch

            (
                output,
                http_response,
            ) = await capo_omics._operations.omics.list_batch.async_list_batch(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_omics.types.list_batch_request.ListBatchRequest = {}
        if max_items is not None:
            input_["max_items"] = max_items
        if starting_token is not None:
            input_["starting_token"] = starting_token
        if status is not None:
            input_["status"] = status
        if name is not None:
            input_["name"] = name
        if run_group_id is not None:
            input_["run_group_id"] = run_group_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_batch(
        self,
        *,
        config_overrides: Optional[AsyncOmicsClientConfig] = None,
        max_items: Optional[int] = None,
        starting_token: Optional["capo_omics.types.list_token.ListToken"] = None,
        status: Optional["capo_omics.types.batch_status.BatchStatus"] = None,
        name: Optional["capo_omics.types.batch_name.BatchName"] = None,
        run_group_id: Optional["capo_omics.types.run_group_id.RunGroupId"] = None,
    ) -> "AsyncIterator[capo_omics.types.batch_list_item.BatchListItem]":
        _token = starting_token
        while True:
            _response = await self.list_batch(
                config_overrides=config_overrides,
                max_items=max_items,
                starting_token=_token,
                status=status,
                name=name,
                run_group_id=run_group_id,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def cancel_run_batch(
        self,
        batch_id: "capo_omics.types.batch_id.BatchId",
        *,
        config_overrides: Optional[AsyncOmicsClientConfig] = None,
    ) -> "capo_omics.types.cancel_run_batch_response.CancelRunBatchResponse":
        """<p>Cancels all runs within a specified batch. This operation prevents not-yet-submitted runs from starting and submits <code>CancelRun</code> requests for runs that have already started.</p> <p>Cancel is only allowed on batches in <code>PENDING</code>, <code>SUBMITTING</code>, or <code>INPROGRESS</code> state. Cancel operations are non-atomic and may be partially successful. Use <code>GetBatch</code> to review <code>successfulCancelSubmissionCount</code> and <code>failedCancelSubmissionCount</code> in the <code>submissionSummary</code>. Only one cancel or delete operation per batch is allowed at a time.</p>

        Args:
            batch_id: <p>The identifier portion of the run batch ARN.</p>

        Raises:
            capo_omics.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_omics.errors.conflict_exception.ConflictException: <p>The request cannot be applied to the target resource in its current state.</p>
            capo_omics.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred. Try the request again.</p>
            capo_omics.errors.request_timeout_exception.RequestTimeoutException: <p>The request timed out.</p>
            capo_omics.errors.resource_not_found_exception.ResourceNotFoundException: <p>The target resource was not found in the current Region.</p>
            capo_omics.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request exceeds a service quota.</p>
            capo_omics.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_omics.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_omics.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_omics.types.cancel_run_batch_request.CancelRunBatchRequest]",
        ) -> AsyncOperationResponse[
            "capo_omics.types.cancel_run_batch_response.CancelRunBatchResponse"
        ]:
            import capo_omics._operations.omics.cancel_run_batch

            (
                output,
                http_response,
            ) = await capo_omics._operations.omics.cancel_run_batch.async_cancel_run_batch(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_omics.types.cancel_run_batch_request.CancelRunBatchRequest = {
            "batch_id": batch_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_run_batch(
        self,
        batch_id: "capo_omics.types.batch_id.BatchId",
        *,
        config_overrides: Optional[AsyncOmicsClientConfig] = None,
    ) -> "capo_omics.types.delete_run_batch_response.DeleteRunBatchResponse":
        """<p>Deletes the individual workflow runs within a batch. This operation is separate from <code>DeleteBatch</code>, which removes the batch metadata.</p> <p>Delete is only allowed on batches in <code>PROCESSED</code> or <code>CANCELLED</code> state. Delete operations are non-atomic and may be partially successful. Use <code>GetBatch</code> to review <code>successfulDeleteSubmissionCount</code> and <code>failedDeleteSubmissionCount</code> in the <code>submissionSummary</code>. Only one cancel or delete operation per batch is allowed at a time.</p>

        Args:
            batch_id: <p>The identifier portion of the run batch ARN.</p>

        Raises:
            capo_omics.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_omics.errors.conflict_exception.ConflictException: <p>The request cannot be applied to the target resource in its current state.</p>
            capo_omics.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred. Try the request again.</p>
            capo_omics.errors.request_timeout_exception.RequestTimeoutException: <p>The request timed out.</p>
            capo_omics.errors.resource_not_found_exception.ResourceNotFoundException: <p>The target resource was not found in the current Region.</p>
            capo_omics.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request exceeds a service quota.</p>
            capo_omics.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_omics.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_omics.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_omics.types.delete_run_batch_request.DeleteRunBatchRequest]",
        ) -> AsyncOperationResponse[
            "capo_omics.types.delete_run_batch_response.DeleteRunBatchResponse"
        ]:
            import capo_omics._operations.omics.delete_run_batch

            (
                output,
                http_response,
            ) = await capo_omics._operations.omics.delete_run_batch.async_delete_run_batch(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_omics.types.delete_run_batch_request.DeleteRunBatchRequest = {
            "batch_id": batch_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_runs_in_batch(
        self,
        batch_id: "capo_omics.types.batch_id.BatchId",
        *,
        config_overrides: Optional[AsyncOmicsClientConfig] = None,
        max_items: Optional[int] = None,
        starting_token: Optional["capo_omics.types.list_token.ListToken"] = None,
        submission_status: Optional[
            "capo_omics.types.submission_status.SubmissionStatus"
        ] = None,
        run_setting_id: Optional[str] = None,
        run_id: Optional[str] = None,
    ) -> "capo_omics.types.list_runs_in_batch_response.ListRunsInBatchResponse":
        """<p>Returns a paginated list of individual workflow runs within a specific batch. Use this operation to map each <code>runSettingId</code> to its HealthOmics-generated <code>runId</code>, and to check the submission status of each run. Only one filter per call is supported.</p>

        Args:
            batch_id: <p>The identifier portion of the run batch ARN.</p>
            max_items: <p>The maximum number of runs to return.</p>
            starting_token: <p>A pagination token returned from a prior <code>ListRunsInBatch</code> call.</p>
            submission_status: <p>Filter runs by submission status.</p>
            run_setting_id: <p>Filter runs by the customer-provided run setting ID.</p>
            run_id: <p>Filter runs by the HealthOmics-generated run ID.</p>

        Raises:
            capo_omics.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_omics.errors.conflict_exception.ConflictException: <p>The request cannot be applied to the target resource in its current state.</p>
            capo_omics.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred. Try the request again.</p>
            capo_omics.errors.request_timeout_exception.RequestTimeoutException: <p>The request timed out.</p>
            capo_omics.errors.resource_not_found_exception.ResourceNotFoundException: <p>The target resource was not found in the current Region.</p>
            capo_omics.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request exceeds a service quota.</p>
            capo_omics.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_omics.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_omics.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_omics.types.list_runs_in_batch_request.ListRunsInBatchRequest]",
        ) -> AsyncOperationResponse[
            "capo_omics.types.list_runs_in_batch_response.ListRunsInBatchResponse"
        ]:
            import capo_omics._operations.omics.list_runs_in_batch

            (
                output,
                http_response,
            ) = await capo_omics._operations.omics.list_runs_in_batch.async_list_runs_in_batch(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_omics.types.list_runs_in_batch_request.ListRunsInBatchRequest = {
            "batch_id": batch_id
        }
        if max_items is not None:
            input_["max_items"] = max_items
        if starting_token is not None:
            input_["starting_token"] = starting_token
        if submission_status is not None:
            input_["submission_status"] = submission_status
        if run_setting_id is not None:
            input_["run_setting_id"] = run_setting_id
        if run_id is not None:
            input_["run_id"] = run_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_runs_in_batch(
        self,
        batch_id: "capo_omics.types.batch_id.BatchId",
        *,
        config_overrides: Optional[AsyncOmicsClientConfig] = None,
        max_items: Optional[int] = None,
        starting_token: Optional["capo_omics.types.list_token.ListToken"] = None,
        submission_status: Optional[
            "capo_omics.types.submission_status.SubmissionStatus"
        ] = None,
        run_setting_id: Optional[str] = None,
        run_id: Optional[str] = None,
    ) -> "AsyncIterator[capo_omics.types.run_batch_list_item.RunBatchListItem]":
        _token = starting_token
        while True:
            _response = await self.list_runs_in_batch(
                batch_id,
                config_overrides=config_overrides,
                max_items=max_items,
                starting_token=_token,
                submission_status=submission_status,
                run_setting_id=run_setting_id,
                run_id=run_id,
            )
            _page = _resolve_path(_response, ("runs",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def create_run_cache(
        self,
        cache_s3_location: "capo_omics.types.s3_uri_for_bucket_or_object.S3UriForBucketOrObject",
        request_id: "capo_omics.types.run_cache_request_id.RunCacheRequestId",
        *,
        config_overrides: Optional[AsyncOmicsClientConfig] = None,
        cache_behavior: Optional[
            "capo_omics.types.cache_behavior.CacheBehavior"
        ] = None,
        description: Optional[
            "capo_omics.types.user_custom_description.UserCustomDescription"
        ] = None,
        name: Optional["capo_omics.types.user_custom_name.UserCustomName"] = None,
        tags: Optional["capo_omics.types.tag_map.TagMap"] = None,
        cache_bucket_owner_id: Optional[
            "capo_omics.types.aws_account_id.AwsAccountId"
        ] = None,
    ) -> "capo_omics.types.create_run_cache_response.CreateRunCacheResponse":
        """<p>Creates a run cache to store and reference task outputs from completed private runs. Specify an Amazon S3 location where Amazon Web Services HealthOmics saves the cached data. This data must be immediately accessible and not in an archived state. You can save intermediate task files to a run cache if they are declared as task outputs in the workflow definition file.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/omics/latest/dev/workflows-call-caching.html">Call caching</a> and <a href="https://docs.aws.amazon.com/omics/latest/dev/workflow-cache-create.html">Creating a run cache</a> in the <i>Amazon Web Services HealthOmics User Guide</i>.</p>

        Args:
            cache_behavior: <p>Default cache behavior for runs that use this cache. Supported values are:</p> <p> <code>CACHE_ON_FAILURE</code>: Caches task outputs from completed tasks for runs that fail. This setting is useful if you're debugging a workflow that fails after several tasks completed successfully. The subsequent run uses the cache outputs for previously-completed tasks if the task definition, inputs, and container in ECR are identical to the prior run.</p> <p> <code>CACHE_ALWAYS</code>: Caches task outputs from completed tasks for all runs. This setting is useful in development mode, but do not use it in a production setting.</p> <p>If you don't specify a value, the default behavior is CACHE_ON_FAILURE. When you start a run that uses this cache, you can override the default cache behavior.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/omics/latest/dev/how-run-cache.html#run-cache-behavior">Run cache behavior</a> in the <i>Amazon Web Services HealthOmics User Guide</i>.</p>
            cache_s3_location: <p>Specify the S3 location for storing the cached task outputs. This data must be immediately accessible (not in an archived state).</p>
            description: <p>Enter a description of the run cache.</p>
            name: <p>Enter a user-friendly name for the run cache.</p>
            request_id: <p>A unique request token, to ensure idempotency. If you don't specify a token, Amazon Web Services HealthOmics automatically generates a universally unique identifier (UUID) for the request.</p>
            tags: <p>Specify one or more tags to associate with this run cache.</p>
            cache_bucket_owner_id: <p>The Amazon Web Services account ID of the expected owner of the S3 bucket for the run cache. If not provided, your account ID is set as the owner of the bucket.</p>

        Raises:
            capo_omics.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_omics.errors.conflict_exception.ConflictException: <p>The request cannot be applied to the target resource in its current state.</p>
            capo_omics.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred. Try the request again.</p>
            capo_omics.errors.request_timeout_exception.RequestTimeoutException: <p>The request timed out.</p>
            capo_omics.errors.resource_not_found_exception.ResourceNotFoundException: <p>The target resource was not found in the current Region.</p>
            capo_omics.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request exceeds a service quota.</p>
            capo_omics.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_omics.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_omics.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_omics.types.create_run_cache_request.CreateRunCacheRequest]",
        ) -> AsyncOperationResponse[
            "capo_omics.types.create_run_cache_response.CreateRunCacheResponse"
        ]:
            import capo_omics._operations.omics.create_run_cache

            (
                output,
                http_response,
            ) = await capo_omics._operations.omics.create_run_cache.async_create_run_cache(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_omics.types.create_run_cache_request.CreateRunCacheRequest = {
            "cache_s3_location": cache_s3_location,
            "request_id": request_id,
        }
        if cache_behavior is not None:
            input_["cache_behavior"] = cache_behavior
        if description is not None:
            input_["description"] = description
        if name is not None:
            input_["name"] = name
        if tags is not None:
            input_["tags"] = tags
        if cache_bucket_owner_id is not None:
            input_["cache_bucket_owner_id"] = cache_bucket_owner_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_run_cache(
        self,
        id: "capo_omics.types.run_cache_id.RunCacheId",
        *,
        config_overrides: Optional[AsyncOmicsClientConfig] = None,
    ) -> "capo_omics.types.get_run_cache_response.GetRunCacheResponse":
        """<p>Retrieves detailed information about the specified run cache using its ID.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/omics/latest/dev/workflows-call-caching.html">Call caching for Amazon Web Services HealthOmics runs</a> in the <i>Amazon Web Services HealthOmics User Guide</i>.</p>

        Args:
            id: <p>The identifier of the run cache to retrieve.</p>

        Raises:
            capo_omics.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_omics.errors.conflict_exception.ConflictException: <p>The request cannot be applied to the target resource in its current state.</p>
            capo_omics.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred. Try the request again.</p>
            capo_omics.errors.request_timeout_exception.RequestTimeoutException: <p>The request timed out.</p>
            capo_omics.errors.resource_not_found_exception.ResourceNotFoundException: <p>The target resource was not found in the current Region.</p>
            capo_omics.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request exceeds a service quota.</p>
            capo_omics.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_omics.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_omics.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_omics.types.get_run_cache_request.GetRunCacheRequest]",
        ) -> AsyncOperationResponse[
            "capo_omics.types.get_run_cache_response.GetRunCacheResponse"
        ]:
            import capo_omics._operations.omics.get_run_cache

            (
                output,
                http_response,
            ) = await capo_omics._operations.omics.get_run_cache.async_get_run_cache(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_omics.types.get_run_cache_request.GetRunCacheRequest = {"id": id}

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_run_cache(
        self,
        id: "capo_omics.types.run_cache_id.RunCacheId",
        *,
        config_overrides: Optional[AsyncOmicsClientConfig] = None,
        cache_behavior: Optional[
            "capo_omics.types.cache_behavior.CacheBehavior"
        ] = None,
        description: Optional[
            "capo_omics.types.user_custom_description.UserCustomDescription"
        ] = None,
        name: Optional["capo_omics.types.user_custom_name.UserCustomName"] = None,
    ) -> None:
        """<p>Updates a run cache using its ID and returns a response with no body if the operation is successful. You can update the run cache description, name, or the default run cache behavior with <code>CACHE_ON_FAILURE</code> or <code>CACHE_ALWAYS</code>. To confirm that your run cache settings have been properly updated, use the <code>GetRunCache</code> API operation.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/omics/latest/dev/how-run-cache.html">How call caching works</a> in the <i>Amazon Web Services HealthOmics User Guide</i>.</p>

        Args:
            cache_behavior: <p>Update the default run cache behavior.</p>
            description: <p>Update the run cache description.</p>
            id: <p>The identifier of the run cache you want to update.</p>
            name: <p>Update the name of the run cache.</p>

        Raises:
            capo_omics.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_omics.errors.conflict_exception.ConflictException: <p>The request cannot be applied to the target resource in its current state.</p>
            capo_omics.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred. Try the request again.</p>
            capo_omics.errors.request_timeout_exception.RequestTimeoutException: <p>The request timed out.</p>
            capo_omics.errors.resource_not_found_exception.ResourceNotFoundException: <p>The target resource was not found in the current Region.</p>
            capo_omics.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request exceeds a service quota.</p>
            capo_omics.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_omics.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_omics.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_omics.types.update_run_cache_request.UpdateRunCacheRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_omics._operations.omics.update_run_cache

            (
                output,
                http_response,
            ) = await capo_omics._operations.omics.update_run_cache.async_update_run_cache(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_omics.types.update_run_cache_request.UpdateRunCacheRequest = {
            "id": id
        }
        if cache_behavior is not None:
            input_["cache_behavior"] = cache_behavior
        if description is not None:
            input_["description"] = description
        if name is not None:
            input_["name"] = name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_run_cache(
        self,
        id: "capo_omics.types.run_cache_id.RunCacheId",
        *,
        config_overrides: Optional[AsyncOmicsClientConfig] = None,
    ) -> None:
        """<p>Deletes a run cache and returns a response with no body if the operation is successful. This action removes the cache metadata stored in the service account, but does not delete the data in Amazon S3. You can access the cache data in Amazon S3, for inspection or to troubleshoot issues. You can remove old cache data using standard S3 <code>Delete</code> operations. </p> <p>For more information, see <a href="https://docs.aws.amazon.com/omics/latest/dev/workflow-cache-delete.html">Deleting a run cache</a> in the <i>Amazon Web Services HealthOmics User Guide</i>.</p>

        Args:
            id: <p>Run cache identifier for the cache you want to delete.</p>

        Raises:
            capo_omics.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_omics.errors.conflict_exception.ConflictException: <p>The request cannot be applied to the target resource in its current state.</p>
            capo_omics.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred. Try the request again.</p>
            capo_omics.errors.request_timeout_exception.RequestTimeoutException: <p>The request timed out.</p>
            capo_omics.errors.resource_not_found_exception.ResourceNotFoundException: <p>The target resource was not found in the current Region.</p>
            capo_omics.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request exceeds a service quota.</p>
            capo_omics.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_omics.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_omics.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_omics.types.delete_run_cache_request.DeleteRunCacheRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_omics._operations.omics.delete_run_cache

            (
                output,
                http_response,
            ) = await capo_omics._operations.omics.delete_run_cache.async_delete_run_cache(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_omics.types.delete_run_cache_request.DeleteRunCacheRequest = {
            "id": id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_run_caches(
        self,
        *,
        config_overrides: Optional[AsyncOmicsClientConfig] = None,
        max_results: Optional[int] = None,
        starting_token: Optional["capo_omics.types.list_token.ListToken"] = None,
    ) -> "capo_omics.types.list_run_caches_response.ListRunCachesResponse":
        """<p>Retrieves a list of your run caches and the metadata for each cache.</p>

        Args:
            max_results: <p>The maximum number of results to return.</p>
            starting_token: <p>Optional pagination token returned from a prior call to the <code>ListRunCaches</code> API operation.</p>

        Raises:
            capo_omics.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_omics.errors.conflict_exception.ConflictException: <p>The request cannot be applied to the target resource in its current state.</p>
            capo_omics.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred. Try the request again.</p>
            capo_omics.errors.request_timeout_exception.RequestTimeoutException: <p>The request timed out.</p>
            capo_omics.errors.resource_not_found_exception.ResourceNotFoundException: <p>The target resource was not found in the current Region.</p>
            capo_omics.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request exceeds a service quota.</p>
            capo_omics.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_omics.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_omics.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_omics.types.list_run_caches_request.ListRunCachesRequest]",
        ) -> AsyncOperationResponse[
            "capo_omics.types.list_run_caches_response.ListRunCachesResponse"
        ]:
            import capo_omics._operations.omics.list_run_caches

            (
                output,
                http_response,
            ) = await capo_omics._operations.omics.list_run_caches.async_list_run_caches(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_omics.types.list_run_caches_request.ListRunCachesRequest = {}
        if max_results is not None:
            input_["max_results"] = max_results
        if starting_token is not None:
            input_["starting_token"] = starting_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_run_caches(
        self,
        *,
        config_overrides: Optional[AsyncOmicsClientConfig] = None,
        max_results: Optional[int] = None,
        starting_token: Optional["capo_omics.types.list_token.ListToken"] = None,
    ) -> "AsyncIterator[capo_omics.types.run_cache_list_item.RunCacheListItem]":
        _token = starting_token
        while True:
            _response = await self.list_run_caches(
                config_overrides=config_overrides,
                max_results=max_results,
                starting_token=_token,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def create_run_group(
        self,
        request_id: "capo_omics.types.run_group_request_id.RunGroupRequestId",
        *,
        config_overrides: Optional[AsyncOmicsClientConfig] = None,
        name: Optional["capo_omics.types.run_group_name.RunGroupName"] = None,
        max_cpus: Optional[int] = None,
        max_runs: Optional[int] = None,
        max_duration: Optional[int] = None,
        tags: Optional["capo_omics.types.tag_map.TagMap"] = None,
        max_gpus: Optional[int] = None,
    ) -> "capo_omics.types.create_run_group_response.CreateRunGroupResponse":
        """<p>Creates a run group to limit the compute resources for the runs that are added to the group. Returns an ARN, ID, and tags for the run group.</p>

        Args:
            name: <p>A name for the group.</p>
            max_cpus: <p>The maximum number of CPUs that can run concurrently across all active runs in the run group.</p>
            max_runs: <p>The maximum number of runs that can be running at the same time.</p>
            max_duration: <p>The maximum time for each run (in minutes). If a run exceeds the maximum run time, the run fails automatically.</p>
            tags: <p>Tags for the group.</p>
            request_id: <p>To ensure that requests don't run multiple times, specify a unique ID for each request.</p>
            max_gpus: <p>The maximum number of GPUs that can run concurrently across all active runs in the run group.</p>

        Raises:
            capo_omics.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_omics.errors.conflict_exception.ConflictException: <p>The request cannot be applied to the target resource in its current state.</p>
            capo_omics.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred. Try the request again.</p>
            capo_omics.errors.request_timeout_exception.RequestTimeoutException: <p>The request timed out.</p>
            capo_omics.errors.resource_not_found_exception.ResourceNotFoundException: <p>The target resource was not found in the current Region.</p>
            capo_omics.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request exceeds a service quota.</p>
            capo_omics.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_omics.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_omics.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_omics.types.create_run_group_request.CreateRunGroupRequest]",
        ) -> AsyncOperationResponse[
            "capo_omics.types.create_run_group_response.CreateRunGroupResponse"
        ]:
            import capo_omics._operations.omics.create_run_group

            (
                output,
                http_response,
            ) = await capo_omics._operations.omics.create_run_group.async_create_run_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_omics.types.create_run_group_request.CreateRunGroupRequest = {
            "request_id": request_id
        }
        if name is not None:
            input_["name"] = name
        if max_cpus is not None:
            input_["max_cpus"] = max_cpus
        if max_runs is not None:
            input_["max_runs"] = max_runs
        if max_duration is not None:
            input_["max_duration"] = max_duration
        if tags is not None:
            input_["tags"] = tags
        if max_gpus is not None:
            input_["max_gpus"] = max_gpus

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_run_group(
        self,
        id: "capo_omics.types.run_group_id.RunGroupId",
        *,
        config_overrides: Optional[AsyncOmicsClientConfig] = None,
    ) -> "capo_omics.types.get_run_group_response.GetRunGroupResponse":
        """<p>Gets information about a run group and returns its metadata.</p>

        Args:
            id: <p>The group's ID.</p>

        Raises:
            capo_omics.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_omics.errors.conflict_exception.ConflictException: <p>The request cannot be applied to the target resource in its current state.</p>
            capo_omics.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred. Try the request again.</p>
            capo_omics.errors.request_timeout_exception.RequestTimeoutException: <p>The request timed out.</p>
            capo_omics.errors.resource_not_found_exception.ResourceNotFoundException: <p>The target resource was not found in the current Region.</p>
            capo_omics.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request exceeds a service quota.</p>
            capo_omics.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_omics.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_omics.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_omics.types.get_run_group_request.GetRunGroupRequest]",
        ) -> AsyncOperationResponse[
            "capo_omics.types.get_run_group_response.GetRunGroupResponse"
        ]:
            import capo_omics._operations.omics.get_run_group

            (
                output,
                http_response,
            ) = await capo_omics._operations.omics.get_run_group.async_get_run_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_omics.types.get_run_group_request.GetRunGroupRequest = {"id": id}

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_run_group(
        self,
        id: "capo_omics.types.run_group_id.RunGroupId",
        *,
        config_overrides: Optional[AsyncOmicsClientConfig] = None,
        name: Optional["capo_omics.types.run_group_name.RunGroupName"] = None,
        max_cpus: Optional[int] = None,
        max_runs: Optional[int] = None,
        max_duration: Optional[int] = None,
        max_gpus: Optional[int] = None,
    ) -> None:
        """<p>Updates the settings of a run group and returns a response with no body if the operation is successful.</p> <p>You can update the following settings with <code>UpdateRunGroup</code>:</p> <ul> <li> <p>Maximum number of CPUs</p> </li> <li> <p>Run time (measured in minutes)</p> </li> <li> <p>Number of GPUs</p> </li> <li> <p>Number of concurrent runs</p> </li> <li> <p>Group name</p> </li> </ul> <p>To confirm that the settings have been successfully updated, use the <code>ListRunGroups</code> or <code>GetRunGroup</code> API operations to verify that the desired changes have been made.</p>

        Args:
            id: <p>The group's ID.</p>
            name: <p>A name for the group.</p>
            max_cpus: <p>The maximum number of CPUs to use.</p>
            max_runs: <p>The maximum number of concurrent runs for the group.</p>
            max_duration: <p>A maximum run time for the group in minutes.</p>
            max_gpus: <p>The maximum GPUs that can be used by a run group.</p>

        Raises:
            capo_omics.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_omics.errors.conflict_exception.ConflictException: <p>The request cannot be applied to the target resource in its current state.</p>
            capo_omics.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred. Try the request again.</p>
            capo_omics.errors.request_timeout_exception.RequestTimeoutException: <p>The request timed out.</p>
            capo_omics.errors.resource_not_found_exception.ResourceNotFoundException: <p>The target resource was not found in the current Region.</p>
            capo_omics.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request exceeds a service quota.</p>
            capo_omics.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_omics.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_omics.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_omics.types.update_run_group_request.UpdateRunGroupRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_omics._operations.omics.update_run_group

            (
                output,
                http_response,
            ) = await capo_omics._operations.omics.update_run_group.async_update_run_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_omics.types.update_run_group_request.UpdateRunGroupRequest = {
            "id": id
        }
        if name is not None:
            input_["name"] = name
        if max_cpus is not None:
            input_["max_cpus"] = max_cpus
        if max_runs is not None:
            input_["max_runs"] = max_runs
        if max_duration is not None:
            input_["max_duration"] = max_duration
        if max_gpus is not None:
            input_["max_gpus"] = max_gpus

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_run_group(
        self,
        id: "capo_omics.types.run_group_id.RunGroupId",
        *,
        config_overrides: Optional[AsyncOmicsClientConfig] = None,
    ) -> None:
        """<p>Deletes a run group and returns a response with no body if the operation is successful.</p> <p>To verify that the run group is deleted:</p> <ul> <li> <p>Use <code>ListRunGroups</code> to confirm the workflow no longer appears in the list.</p> </li> <li> <p>Use <code>GetRunGroup</code> to verify the workflow cannot be found.</p> </li> </ul>

        Args:
            id: <p>The run group's ID.</p>

        Raises:
            capo_omics.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_omics.errors.conflict_exception.ConflictException: <p>The request cannot be applied to the target resource in its current state.</p>
            capo_omics.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred. Try the request again.</p>
            capo_omics.errors.request_timeout_exception.RequestTimeoutException: <p>The request timed out.</p>
            capo_omics.errors.resource_not_found_exception.ResourceNotFoundException: <p>The target resource was not found in the current Region.</p>
            capo_omics.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request exceeds a service quota.</p>
            capo_omics.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_omics.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_omics.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_omics.types.delete_run_group_request.DeleteRunGroupRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_omics._operations.omics.delete_run_group

            (
                output,
                http_response,
            ) = await capo_omics._operations.omics.delete_run_group.async_delete_run_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_omics.types.delete_run_group_request.DeleteRunGroupRequest = {
            "id": id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_run_groups(
        self,
        *,
        config_overrides: Optional[AsyncOmicsClientConfig] = None,
        name: Optional["capo_omics.types.run_group_name.RunGroupName"] = None,
        starting_token: Optional[
            "capo_omics.types.run_group_list_token.RunGroupListToken"
        ] = None,
        max_results: Optional[int] = None,
    ) -> "capo_omics.types.list_run_groups_response.ListRunGroupsResponse":
        """<p>Retrieves a list of all run groups and returns the metadata for each run group.</p>

        Args:
            name: <p>The run groups' name.</p>
            starting_token: <p>Specify the pagination token from a previous request to retrieve the next page of results.</p>
            max_results: <p>The maximum number of run groups to return in one page of results.</p>

        Raises:
            capo_omics.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_omics.errors.conflict_exception.ConflictException: <p>The request cannot be applied to the target resource in its current state.</p>
            capo_omics.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred. Try the request again.</p>
            capo_omics.errors.request_timeout_exception.RequestTimeoutException: <p>The request timed out.</p>
            capo_omics.errors.resource_not_found_exception.ResourceNotFoundException: <p>The target resource was not found in the current Region.</p>
            capo_omics.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request exceeds a service quota.</p>
            capo_omics.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_omics.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_omics.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_omics.types.list_run_groups_request.ListRunGroupsRequest]",
        ) -> AsyncOperationResponse[
            "capo_omics.types.list_run_groups_response.ListRunGroupsResponse"
        ]:
            import capo_omics._operations.omics.list_run_groups

            (
                output,
                http_response,
            ) = await capo_omics._operations.omics.list_run_groups.async_list_run_groups(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_omics.types.list_run_groups_request.ListRunGroupsRequest = {}
        if name is not None:
            input_["name"] = name
        if starting_token is not None:
            input_["starting_token"] = starting_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_run_groups(
        self,
        *,
        config_overrides: Optional[AsyncOmicsClientConfig] = None,
        name: Optional["capo_omics.types.run_group_name.RunGroupName"] = None,
        starting_token: Optional[
            "capo_omics.types.run_group_list_token.RunGroupListToken"
        ] = None,
        max_results: Optional[int] = None,
    ) -> "AsyncIterator[capo_omics.types.run_group_list_item.RunGroupListItem]":
        _token = starting_token
        while True:
            _response = await self.list_run_groups(
                config_overrides=config_overrides,
                name=name,
                starting_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def start_run(
        self,
        role_arn: "capo_omics.types.run_role_arn.RunRoleArn",
        output_uri: "capo_omics.types.run_output_uri.RunOutputUri",
        request_id: "capo_omics.types.run_request_id.RunRequestId",
        *,
        config_overrides: Optional[AsyncOmicsClientConfig] = None,
        workflow_id: Optional["capo_omics.types.workflow_id.WorkflowId"] = None,
        workflow_type: Optional["capo_omics.types.workflow_type.WorkflowType"] = None,
        run_id: Optional["capo_omics.types.run_id.RunId"] = None,
        name: Optional["capo_omics.types.run_name.RunName"] = None,
        cache_id: Optional["capo_omics.types.numeric_id_in_arn.NumericIdInArn"] = None,
        cache_behavior: Optional[
            "capo_omics.types.cache_behavior.CacheBehavior"
        ] = None,
        run_group_id: Optional["capo_omics.types.run_group_id.RunGroupId"] = None,
        priority: Optional[int] = None,
        parameters: Optional["capo_omics.types.run_parameters.RunParameters"] = None,
        storage_capacity: Optional[int] = None,
        log_level: Optional["capo_omics.types.run_log_level.RunLogLevel"] = None,
        tags: Optional["capo_omics.types.tag_map.TagMap"] = None,
        retention_mode: Optional[
            "capo_omics.types.run_retention_mode.RunRetentionMode"
        ] = None,
        storage_type: Optional["capo_omics.types.storage_type.StorageType"] = None,
        workflow_owner_id: Optional[
            "capo_omics.types.workflow_owner_id.WorkflowOwnerId"
        ] = None,
        workflow_version_name: Optional[
            "capo_omics.types.workflow_version_name.WorkflowVersionName"
        ] = None,
        networking_mode: Optional[
            "capo_omics.types.networking_mode.NetworkingMode"
        ] = None,
        scratch_storage_mode: Optional[
            "capo_omics.types.scratch_storage_mode.ScratchStorageMode"
        ] = None,
        configuration_name: Optional[
            "capo_omics.types.configuration_name.ConfigurationName"
        ] = None,
        session_policy: Optional[
            "capo_omics.types.session_policy.SessionPolicy"
        ] = None,
        engine_settings: Optional[
            "capo_omics.types.engine_settings.EngineSettings"
        ] = None,
    ) -> "capo_omics.types.start_run_response.StartRunResponse":
        """<p>Starts a new run and returns details about the run, or duplicates an existing run. A run is a single invocation of a workflow. If you provide request IDs, Amazon Web Services HealthOmics identifies duplicate requests and starts the run only once. Monitor the progress of the run by calling the <code>GetRun</code> API operation.</p> <p>To start a new run, the following inputs are required:</p> <ul> <li> <p>A service role ARN (<code>roleArn</code>).</p> </li> <li> <p>The run's workflow ID (<code>workflowId</code>, not the <code>uuid</code> or <code>runId</code>).</p> </li> <li> <p>An Amazon S3 location (<code>outputUri</code>) where the run outputs will be saved.</p> </li> <li> <p>All required workflow parameters (<code>parameter</code>), which can include optional parameters from the parameter template. The run cannot include any parameters that are not defined in the parameter template. To see all possible parameters, use the <code>GetRun</code> API operation. </p> </li> <li> <p>For runs with a <code>STATIC</code> (default) storage type, specify the required storage capacity (in gibibytes). A storage capacity value is not required for runs that use <code>DYNAMIC</code> storage.</p> </li> </ul> <p> <code>StartRun</code> can also duplicate an existing run using the run's default values. You can modify these default values and/or add other optional inputs. To duplicate a run, the following inputs are required:</p> <ul> <li> <p>A service role ARN (<code>roleArn</code>).</p> </li> <li> <p>The ID of the run to duplicate (<code>runId</code>).</p> </li> <li> <p>An Amazon S3 location where the run outputs will be saved (<code>outputUri</code>).</p> </li> </ul> <p>To learn more about the optional parameters for <code>StartRun</code>, see <a href="https://docs.aws.amazon.com/omics/latest/dev/starting-a-run.html">Starting a run</a> in the <i>Amazon Web Services HealthOmics User Guide</i>.</p> <p>Use the <code>retentionMode</code> input to control how long the metadata for each run is stored in CloudWatch. There are two retention modes:</p> <ul> <li> <p>Specify <code>REMOVE</code> to automatically remove the oldest runs when you reach the maximum service retention limit for runs. It is recommended that you use the <code>REMOVE</code> mode to initiate major run requests so that your runs do not fail when you reach the limit.</p> </li> <li> <p>The <code>retentionMode</code> is set to the <code>RETAIN</code> mode by default, which allows you to manually remove runs after reaching the maximum service retention limit. Under this setting, you cannot create additional runs until you remove the excess runs.</p> </li> </ul> <p>To learn more about the retention modes, see <a href="https://docs.aws.amazon.com/omics/latest/dev/run-retention.html">Run retention mode</a> in the <i>Amazon Web Services HealthOmics User Guide</i>.</p> <p>You can use Amazon Q CLI to analyze run logs and make performance optimization recommendations. To get started, see the <a href="https://github.com/awslabs/mcp/tree/main/src/aws-healthomics-mcp-server">Amazon Web Services HealthOmics MCP server</a> on GitHub.</p>

        Args:
            workflow_id: <p>The run's workflow ID. The <code>workflowId</code> is not the UUID.</p>
            workflow_type: <p>The run's workflow type. The <code>workflowType</code> must be specified if you are running a <code>READY2RUN</code> workflow. If you are running a <code>PRIVATE</code> workflow (default), you do not need to include the workflow type. </p>
            run_id: <p>The ID of a run to duplicate.</p>
            role_arn: <p>A service role for the run. The <code>roleArn</code> requires access to Amazon Web Services HealthOmics, S3, Cloudwatch logs, and EC2. An example <code>roleArn</code> is <code>arn:aws:iam::123456789012:role/omics-service-role-serviceRole-W8O1XMPL7QZ</code>. In this example, the Amazon Web Services account ID is <code>123456789012</code> and the role name is <code>omics-service-role-serviceRole-W8O1XMPL7QZ</code>.</p>
            name: <p>A name for the run. This is recommended to view and organize runs in the Amazon Web Services HealthOmics console and CloudWatch logs.</p>
            cache_id: <p>Identifier of the cache associated with this run. If you don't specify a cache ID, no task outputs are cached for this run.</p>
            cache_behavior: <p>The cache behavior for the run. You specify this value if you want to override the default behavior for the cache. You had set the default value when you created the cache. For more information, see <a href="https://docs.aws.amazon.com/omics/latest/dev/how-run-cache.html#run-cache-behavior">Run cache behavior</a> in the <i>Amazon Web Services HealthOmics User Guide</i>.</p>
            run_group_id: <p>The run's group ID. Use a run group to cap the compute resources (and number of concurrent runs) for the runs that you add to the run group.</p>
            priority: <p>Use the run priority (highest: 1) to establish the order of runs in a run group when you start a run. If multiple runs share the same priority, the run that was initiated first will have the higher priority. Runs that do not belong to a run group can be assigned a priority. The priorities of these runs are ranked among other runs that are not in a run group. For more information, see <a href="https://docs.aws.amazon.com/omics/latest/dev/creating-run-groups.html#run-priority">Run priority</a> in the <i>Amazon Web Services HealthOmics User Guide</i>.</p>
            parameters: <p>Parameters for the run. The run needs all required parameters and can include optional parameters. The run cannot include any parameters that are not defined in the parameter template. To retrieve parameters from the run, use the GetRun API operation.</p>
            storage_capacity: <p>The <code>STATIC</code> storage capacity (in gibibytes, GiB) for this run. The default run storage capacity is 1200 GiB. If your requested storage capacity is unavailable, the system rounds up the value to the nearest 1200 GiB multiple. If the requested storage capacity is still unavailable, the system rounds up the value to the nearest 2400 GiB multiple. This field is not required if the storage type is <code>DYNAMIC</code> (the system ignores any value that you enter).</p>
            output_uri: <p>An output S3 URI for the run. The S3 bucket must be in the same region as the workflow. The role ARN must have permission to write to this S3 bucket.</p>
            log_level: <p>A log level for the run.</p>
            tags: <p>Tags for the run. You can add up to 50 tags per run. For more information, see <a href="https://docs.aws.amazon.com/omics/latest/dev/add-a-tag.html">Adding a tag</a> in the <i>Amazon Web Services HealthOmics User Guide</i>.</p>
            request_id: <p>An idempotency token used to dedupe retry requests so that duplicate runs are not created.</p>
            retention_mode: <p>The retention mode for the run. The default value is <code>RETAIN</code>. </p> <p>Amazon Web Services HealthOmics stores a fixed number of runs that are available to the console and API. In the default mode (<code>RETAIN</code>), you need to remove runs manually when the number of run exceeds the maximum. If you set the retention mode to <code>REMOVE</code>, Amazon Web Services HealthOmics automatically removes runs (that have mode set to <code>REMOVE</code>) when the number of run exceeds the maximum. All run logs are available in CloudWatch logs, if you need information about a run that is no longer available to the API.</p> <p>For more information about retention mode, see <a href="https://docs.aws.amazon.com/omics/latest/dev/starting-a-run.html">Specifying run retention mode</a> in the <i>Amazon Web Services HealthOmics User Guide</i>.</p>
            storage_type: <p>The storage type for the run. If you set the storage type to <code>DYNAMIC</code>, Amazon Web Services HealthOmics dynamically scales the storage up or down, based on file system utilization. By default, the run uses <code>STATIC</code> storage type, which allocates a fixed amount of storage. For more information about <code>DYNAMIC</code> and <code>STATIC</code> storage, see <a href="https://docs.aws.amazon.com/omics/latest/dev/workflows-run-types.html">Run storage types</a> in the <i>Amazon Web Services HealthOmics User Guide</i>.</p>
            workflow_owner_id: <p>The 12-digit account ID of the workflow owner that is used for running a shared workflow. The workflow owner ID can be retrieved using the <code>GetShare</code> API operation. If you are the workflow owner, you do not need to include this ID.</p>
            workflow_version_name: <p>The name of the workflow version. Use workflow versions to track and organize changes to the workflow. If your workflow has multiple versions, the run uses the default version unless you specify a version name. To learn more, see <a href="https://docs.aws.amazon.com/omics/latest/dev/workflow-versions.html">Workflow versioning</a> in the <i>Amazon Web Services HealthOmics User Guide</i>.</p>
            networking_mode: <p>Optional configuration for run networking behavior. If not specified, this will default to RESTRICTED.</p>
            scratch_storage_mode: <p>Optional configuration for enabling scratch ephemeral storage mounted at /tmp. If not specified, this will default to SHARED. This configuration is applicable only for CPU tasks. For tasks using GPUs, scratch storage is always LOCAL.</p>
            configuration_name: <p>Optional configuration name to use for the workflow run.</p>
            session_policy: Optional inline policy json for scoping down permissions via a session policy on the IAM role provided in the roleArn parameter.
            engine_settings: <p>Engine-specific settings for the workflow run. Use this field to specify configuration options that are specific to the workflow engine (for example, Nextflow profiles).</p>

        Raises:
            capo_omics.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_omics.errors.conflict_exception.ConflictException: <p>The request cannot be applied to the target resource in its current state.</p>
            capo_omics.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred. Try the request again.</p>
            capo_omics.errors.request_timeout_exception.RequestTimeoutException: <p>The request timed out.</p>
            capo_omics.errors.resource_not_found_exception.ResourceNotFoundException: <p>The target resource was not found in the current Region.</p>
            capo_omics.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request exceeds a service quota.</p>
            capo_omics.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_omics.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_omics.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_omics.types.start_run_request.StartRunRequest]",
        ) -> AsyncOperationResponse[
            "capo_omics.types.start_run_response.StartRunResponse"
        ]:
            import capo_omics._operations.omics.start_run

            (
                output,
                http_response,
            ) = await capo_omics._operations.omics.start_run.async_start_run(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_omics.types.start_run_request.StartRunRequest = {
            "role_arn": role_arn,
            "output_uri": output_uri,
            "request_id": request_id,
        }
        if workflow_id is not None:
            input_["workflow_id"] = workflow_id
        if workflow_type is not None:
            input_["workflow_type"] = workflow_type
        if run_id is not None:
            input_["run_id"] = run_id
        if name is not None:
            input_["name"] = name
        if cache_id is not None:
            input_["cache_id"] = cache_id
        if cache_behavior is not None:
            input_["cache_behavior"] = cache_behavior
        if run_group_id is not None:
            input_["run_group_id"] = run_group_id
        if priority is not None:
            input_["priority"] = priority
        if parameters is not None:
            input_["parameters"] = parameters
        if storage_capacity is not None:
            input_["storage_capacity"] = storage_capacity
        if log_level is not None:
            input_["log_level"] = log_level
        if tags is not None:
            input_["tags"] = tags
        if retention_mode is not None:
            input_["retention_mode"] = retention_mode
        if storage_type is not None:
            input_["storage_type"] = storage_type
        if workflow_owner_id is not None:
            input_["workflow_owner_id"] = workflow_owner_id
        if workflow_version_name is not None:
            input_["workflow_version_name"] = workflow_version_name
        if networking_mode is not None:
            input_["networking_mode"] = networking_mode
        if scratch_storage_mode is not None:
            input_["scratch_storage_mode"] = scratch_storage_mode
        if configuration_name is not None:
            input_["configuration_name"] = configuration_name
        if session_policy is not None:
            input_["session_policy"] = session_policy
        if engine_settings is not None:
            input_["engine_settings"] = engine_settings

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_run(
        self,
        id: "capo_omics.types.run_id.RunId",
        *,
        config_overrides: Optional[AsyncOmicsClientConfig] = None,
        export: Optional["capo_omics.types.run_export_list.RunExportList"] = None,
    ) -> "capo_omics.types.get_run_response.GetRunResponse":
        """<p>Gets detailed information about a specific run using its ID.</p> <p>Amazon Web Services HealthOmics stores a configurable number of runs, as determined by service limits, that are available to the console and API. If <code>GetRun</code> does not return the requested run, you can find all run logs in the CloudWatch logs. For more information about viewing the run logs, see <a href="https://docs.aws.amazon.com/omics/latest/dev/monitoring-cloudwatch-logs.html">CloudWatch logs</a> in the <i>Amazon Web Services HealthOmics User Guide</i>.</p>

        Args:
            id: <p>The run's ID.</p>
            export: <p>The run's export format.</p>

        Raises:
            capo_omics.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_omics.errors.conflict_exception.ConflictException: <p>The request cannot be applied to the target resource in its current state.</p>
            capo_omics.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred. Try the request again.</p>
            capo_omics.errors.request_timeout_exception.RequestTimeoutException: <p>The request timed out.</p>
            capo_omics.errors.resource_not_found_exception.ResourceNotFoundException: <p>The target resource was not found in the current Region.</p>
            capo_omics.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request exceeds a service quota.</p>
            capo_omics.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_omics.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_omics.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_omics.types.get_run_request.GetRunRequest]",
        ) -> AsyncOperationResponse["capo_omics.types.get_run_response.GetRunResponse"]:
            import capo_omics._operations.omics.get_run

            (
                output,
                http_response,
            ) = await capo_omics._operations.omics.get_run.async_get_run(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_omics.types.get_run_request.GetRunRequest = {"id": id}
        if export is not None:
            input_["export"] = export

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_run(
        self,
        id: "capo_omics.types.run_id.RunId",
        *,
        config_overrides: Optional[AsyncOmicsClientConfig] = None,
    ) -> None:
        """<p>Deletes a run and returns a response with no body if the operation is successful. You can only delete a run that has reached a <code>COMPLETED</code>, <code>FAILED</code>, or <code>CANCELLED</code> stage. A completed run has delivered an output, or was cancelled and resulted in no output. When you delete a run, only the metadata associated with the run is deleted. The run outputs remain in Amazon S3 and logs remain in CloudWatch.</p> <p>To verify that the workflow is deleted:</p> <ul> <li> <p>Use <code>ListRuns</code> to confirm the workflow no longer appears in the list.</p> </li> <li> <p>Use <code>GetRun</code> to verify the workflow cannot be found.</p> </li> </ul>

        Args:
            id: <p>The run's ID.</p>

        Raises:
            capo_omics.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_omics.errors.conflict_exception.ConflictException: <p>The request cannot be applied to the target resource in its current state.</p>
            capo_omics.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred. Try the request again.</p>
            capo_omics.errors.request_timeout_exception.RequestTimeoutException: <p>The request timed out.</p>
            capo_omics.errors.resource_not_found_exception.ResourceNotFoundException: <p>The target resource was not found in the current Region.</p>
            capo_omics.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request exceeds a service quota.</p>
            capo_omics.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_omics.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_omics.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_omics.types.delete_run_request.DeleteRunRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_omics._operations.omics.delete_run

            (
                output,
                http_response,
            ) = await capo_omics._operations.omics.delete_run.async_delete_run(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_omics.types.delete_run_request.DeleteRunRequest = {"id": id}

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_runs(
        self,
        *,
        config_overrides: Optional[AsyncOmicsClientConfig] = None,
        name: Optional["capo_omics.types.run_name.RunName"] = None,
        run_group_id: Optional["capo_omics.types.run_group_id.RunGroupId"] = None,
        batch_id: Optional["capo_omics.types.batch_id.BatchId"] = None,
        starting_token: Optional["capo_omics.types.run_list_token.RunListToken"] = None,
        max_results: Optional[int] = None,
        status: Optional["capo_omics.types.run_status.RunStatus"] = None,
    ) -> "capo_omics.types.list_runs_response.ListRunsResponse":
        """<p>Retrieves a list of runs and returns each run's metadata and status.</p> <p>Amazon Web Services HealthOmics stores a configurable number of runs, as determined by service limits, that are available to the console and API. If the <code>ListRuns</code> response doesn't include specific runs that you expected, you can find all run logs in the CloudWatch logs. For more information about viewing the run logs, see <a href="https://docs.aws.amazon.com/omics/latest/dev/monitoring-cloudwatch-logs.html">CloudWatch logs</a> in the <i>Amazon Web Services HealthOmics User Guide</i>.</p>

        Args:
            name: <p>Filter the list by run name.</p>
            run_group_id: <p>Filter the list by run group ID.</p>
            batch_id: <p>Filter by batch ID.</p>
            starting_token: <p>Specify the pagination token from a previous request to retrieve the next page of results.</p>
            max_results: <p>The maximum number of runs to return in one page of results.</p>
            status: <p>The status of a run.</p>

        Raises:
            capo_omics.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_omics.errors.conflict_exception.ConflictException: <p>The request cannot be applied to the target resource in its current state.</p>
            capo_omics.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred. Try the request again.</p>
            capo_omics.errors.request_timeout_exception.RequestTimeoutException: <p>The request timed out.</p>
            capo_omics.errors.resource_not_found_exception.ResourceNotFoundException: <p>The target resource was not found in the current Region.</p>
            capo_omics.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request exceeds a service quota.</p>
            capo_omics.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_omics.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_omics.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_omics.types.list_runs_request.ListRunsRequest]",
        ) -> AsyncOperationResponse[
            "capo_omics.types.list_runs_response.ListRunsResponse"
        ]:
            import capo_omics._operations.omics.list_runs

            (
                output,
                http_response,
            ) = await capo_omics._operations.omics.list_runs.async_list_runs(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_omics.types.list_runs_request.ListRunsRequest = {}
        if name is not None:
            input_["name"] = name
        if run_group_id is not None:
            input_["run_group_id"] = run_group_id
        if batch_id is not None:
            input_["batch_id"] = batch_id
        if starting_token is not None:
            input_["starting_token"] = starting_token
        if max_results is not None:
            input_["max_results"] = max_results
        if status is not None:
            input_["status"] = status

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_runs(
        self,
        *,
        config_overrides: Optional[AsyncOmicsClientConfig] = None,
        name: Optional["capo_omics.types.run_name.RunName"] = None,
        run_group_id: Optional["capo_omics.types.run_group_id.RunGroupId"] = None,
        batch_id: Optional["capo_omics.types.batch_id.BatchId"] = None,
        starting_token: Optional["capo_omics.types.run_list_token.RunListToken"] = None,
        max_results: Optional[int] = None,
        status: Optional["capo_omics.types.run_status.RunStatus"] = None,
    ) -> "AsyncIterator[capo_omics.types.run_list_item.RunListItem]":
        _token = starting_token
        while True:
            _response = await self.list_runs(
                config_overrides=config_overrides,
                name=name,
                run_group_id=run_group_id,
                batch_id=batch_id,
                starting_token=_token,
                max_results=max_results,
                status=status,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def cancel_run(
        self,
        id: "capo_omics.types.run_id.RunId",
        *,
        config_overrides: Optional[AsyncOmicsClientConfig] = None,
    ) -> None:
        """<p>Cancels a run using its ID and returns a response with no body if the operation is successful. To confirm that the run has been cancelled, use the <code>ListRuns</code> API operation to check that it is no longer listed.</p>

        Args:
            id: <p>The run's ID.</p>

        Raises:
            capo_omics.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_omics.errors.conflict_exception.ConflictException: <p>The request cannot be applied to the target resource in its current state.</p>
            capo_omics.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred. Try the request again.</p>
            capo_omics.errors.request_timeout_exception.RequestTimeoutException: <p>The request timed out.</p>
            capo_omics.errors.resource_not_found_exception.ResourceNotFoundException: <p>The target resource was not found in the current Region.</p>
            capo_omics.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request exceeds a service quota.</p>
            capo_omics.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_omics.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_omics.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_omics.types.cancel_run_request.CancelRunRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_omics._operations.omics.cancel_run

            (
                output,
                http_response,
            ) = await capo_omics._operations.omics.cancel_run.async_cancel_run(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_omics.types.cancel_run_request.CancelRunRequest = {"id": id}

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_run_task(
        self,
        id: "capo_omics.types.run_id.RunId",
        task_id: "capo_omics.types.task_id.TaskId",
        *,
        config_overrides: Optional[AsyncOmicsClientConfig] = None,
    ) -> "capo_omics.types.get_run_task_response.GetRunTaskResponse":
        """<p>Gets detailed information about a run task using its ID.</p>

        Args:
            id: <p>The workflow run ID.</p>
            task_id: <p>The task's ID.</p>

        Raises:
            capo_omics.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_omics.errors.conflict_exception.ConflictException: <p>The request cannot be applied to the target resource in its current state.</p>
            capo_omics.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred. Try the request again.</p>
            capo_omics.errors.request_timeout_exception.RequestTimeoutException: <p>The request timed out.</p>
            capo_omics.errors.resource_not_found_exception.ResourceNotFoundException: <p>The target resource was not found in the current Region.</p>
            capo_omics.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request exceeds a service quota.</p>
            capo_omics.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_omics.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_omics.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_omics.types.get_run_task_request.GetRunTaskRequest]",
        ) -> AsyncOperationResponse[
            "capo_omics.types.get_run_task_response.GetRunTaskResponse"
        ]:
            import capo_omics._operations.omics.get_run_task

            (
                output,
                http_response,
            ) = await capo_omics._operations.omics.get_run_task.async_get_run_task(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_omics.types.get_run_task_request.GetRunTaskRequest = {
            "id": id,
            "task_id": task_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_run_tasks(
        self,
        id: "capo_omics.types.run_id.RunId",
        *,
        config_overrides: Optional[AsyncOmicsClientConfig] = None,
        status: Optional["capo_omics.types.task_status.TaskStatus"] = None,
        starting_token: Optional[
            "capo_omics.types.task_list_token.TaskListToken"
        ] = None,
        max_results: Optional[int] = None,
    ) -> "capo_omics.types.list_run_tasks_response.ListRunTasksResponse":
        """<p>Returns a list of tasks and status information within their specified run. Use this operation to monitor runs and to identify which specific tasks have failed.</p>

        Args:
            id: <p>The run's ID.</p>
            status: <p>Filter the list by status.</p>
            starting_token: <p>Specify the pagination token from a previous request to retrieve the next page of results.</p>
            max_results: <p>The maximum number of run tasks to return in one page of results.</p>

        Raises:
            capo_omics.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_omics.errors.conflict_exception.ConflictException: <p>The request cannot be applied to the target resource in its current state.</p>
            capo_omics.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred. Try the request again.</p>
            capo_omics.errors.request_timeout_exception.RequestTimeoutException: <p>The request timed out.</p>
            capo_omics.errors.resource_not_found_exception.ResourceNotFoundException: <p>The target resource was not found in the current Region.</p>
            capo_omics.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request exceeds a service quota.</p>
            capo_omics.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_omics.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_omics.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_omics.types.list_run_tasks_request.ListRunTasksRequest]",
        ) -> AsyncOperationResponse[
            "capo_omics.types.list_run_tasks_response.ListRunTasksResponse"
        ]:
            import capo_omics._operations.omics.list_run_tasks

            (
                output,
                http_response,
            ) = await capo_omics._operations.omics.list_run_tasks.async_list_run_tasks(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_omics.types.list_run_tasks_request.ListRunTasksRequest = {"id": id}
        if status is not None:
            input_["status"] = status
        if starting_token is not None:
            input_["starting_token"] = starting_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_run_tasks(
        self,
        id: "capo_omics.types.run_id.RunId",
        *,
        config_overrides: Optional[AsyncOmicsClientConfig] = None,
        status: Optional["capo_omics.types.task_status.TaskStatus"] = None,
        starting_token: Optional[
            "capo_omics.types.task_list_token.TaskListToken"
        ] = None,
        max_results: Optional[int] = None,
    ) -> "AsyncIterator[capo_omics.types.task_list_item.TaskListItem]":
        _token = starting_token
        while True:
            _response = await self.list_run_tasks(
                id,
                config_overrides=config_overrides,
                status=status,
                starting_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def create_sequence_store(
        self,
        name: "capo_omics.types.sequence_store_name.SequenceStoreName",
        *,
        config_overrides: Optional[AsyncOmicsClientConfig] = None,
        description: Optional[
            "capo_omics.types.sequence_store_description.SequenceStoreDescription"
        ] = None,
        sse_config: Optional["capo_omics.types.sse_config.SseConfig"] = None,
        tags: Optional["capo_omics.types.tag_map.TagMap"] = None,
        client_token: Optional["capo_omics.types.client_token.ClientToken"] = None,
        fallback_location: Optional[
            "capo_omics.types.fallback_location.FallbackLocation"
        ] = None,
        e_tag_algorithm_family: Optional[
            "capo_omics.types.e_tag_algorithm_family.ETagAlgorithmFamily"
        ] = None,
        propagated_set_level_tags: Optional[
            "capo_omics.types.propagated_set_level_tags.PropagatedSetLevelTags"
        ] = None,
        s3_access_config: Optional[
            "capo_omics.types.s3_access_config.S3AccessConfig"
        ] = None,
    ) -> "capo_omics.types.create_sequence_store_response.CreateSequenceStoreResponse":
        """<p>Creates a sequence store and returns its metadata. Sequence stores are used to store sequence data files called read sets that are saved in FASTQ, BAM, uBAM, or CRAM formats. For aligned formats (BAM and CRAM), a sequence store can only use one reference genome. For unaligned formats (FASTQ and uBAM), a reference genome is not required. You can create multiple sequence stores per region per account. </p> <p>The following are optional parameters you can specify for your sequence store:</p> <ul> <li> <p>Use <code>s3AccessConfig</code> to configure your sequence store with S3 access logs (recommended).</p> </li> <li> <p>Use <code>sseConfig</code> to define your own KMS key for encryption.</p> </li> <li> <p>Use <code>eTagAlgorithmFamily</code> to define which algorithm to use for the HealthOmics eTag on objects.</p> </li> <li> <p>Use <code>fallbackLocation</code> to define a backup location for storing files that have failed a direct upload.</p> </li> <li> <p>Use <code>propagatedSetLevelTags</code> to configure tags that propagate to all objects in your store.</p> </li> </ul> <p>For more information, see <a href="https://docs.aws.amazon.com/omics/latest/dev/create-sequence-store.html">Creating a HealthOmics sequence store</a> in the <i>Amazon Web Services HealthOmics User Guide</i>.</p>

        Args:
            name: <p>A name for the store.</p>
            description: <p>A description for the store.</p>
            sse_config: <p>Server-side encryption (SSE) settings for the store.</p>
            tags: <p>Tags for the store. You can configure up to 50 tags.</p>
            client_token: <p>An idempotency token used to dedupe retry requests so that duplicate runs are not created.</p>
            fallback_location: <p>An S3 location that is used to store files that have failed a direct upload. You can add or change the <code>fallbackLocation</code> after creating a sequence store. This is not required if you are uploading files from a different S3 bucket.</p>
            e_tag_algorithm_family: <p>The ETag algorithm family to use for ingested read sets. The default value is MD5up. For more information on ETags, see <a href="https://docs.aws.amazon.com/omics/latest/dev/etags-and-provenance.html">ETags and data provenance</a> in the <i>Amazon Web Services HealthOmics User Guide</i>.</p>
            propagated_set_level_tags: <p>The tags keys to propagate to the S3 objects associated with read sets in the sequence store. These tags can be used as input to add metadata to your read sets.</p>
            s3_access_config: <p>S3 access configuration parameters. This specifies the parameters needed to access logs stored in S3 buckets. The S3 bucket must be in the same region and account as the sequence store. </p>

        Raises:
            capo_omics.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_omics.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred. Try the request again.</p>
            capo_omics.errors.request_timeout_exception.RequestTimeoutException: <p>The request timed out.</p>
            capo_omics.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request exceeds a service quota.</p>
            capo_omics.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_omics.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_omics.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_omics.types.create_sequence_store_request.CreateSequenceStoreRequest]",
        ) -> AsyncOperationResponse[
            "capo_omics.types.create_sequence_store_response.CreateSequenceStoreResponse"
        ]:
            import capo_omics._operations.omics.create_sequence_store

            (
                output,
                http_response,
            ) = await capo_omics._operations.omics.create_sequence_store.async_create_sequence_store(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_omics.types.create_sequence_store_request.CreateSequenceStoreRequest = {
            "name": name
        }
        if description is not None:
            input_["description"] = description
        if sse_config is not None:
            input_["sse_config"] = sse_config
        if tags is not None:
            input_["tags"] = tags
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if fallback_location is not None:
            input_["fallback_location"] = fallback_location
        if e_tag_algorithm_family is not None:
            input_["e_tag_algorithm_family"] = e_tag_algorithm_family
        if propagated_set_level_tags is not None:
            input_["propagated_set_level_tags"] = propagated_set_level_tags
        if s3_access_config is not None:
            input_["s3_access_config"] = s3_access_config

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_sequence_store(
        self,
        id: "capo_omics.types.sequence_store_id.SequenceStoreId",
        *,
        config_overrides: Optional[AsyncOmicsClientConfig] = None,
    ) -> "capo_omics.types.get_sequence_store_response.GetSequenceStoreResponse":
        """<p>Retrieves metadata for a sequence store using its ID and returns it in JSON format.</p>

        Args:
            id: <p>The store's ID.</p>

        Raises:
            capo_omics.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_omics.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred. Try the request again.</p>
            capo_omics.errors.request_timeout_exception.RequestTimeoutException: <p>The request timed out.</p>
            capo_omics.errors.resource_not_found_exception.ResourceNotFoundException: <p>The target resource was not found in the current Region.</p>
            capo_omics.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_omics.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_omics.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_omics.types.get_sequence_store_request.GetSequenceStoreRequest]",
        ) -> AsyncOperationResponse[
            "capo_omics.types.get_sequence_store_response.GetSequenceStoreResponse"
        ]:
            import capo_omics._operations.omics.get_sequence_store

            (
                output,
                http_response,
            ) = await capo_omics._operations.omics.get_sequence_store.async_get_sequence_store(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_omics.types.get_sequence_store_request.GetSequenceStoreRequest = {
            "id": id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_sequence_store(
        self,
        id: "capo_omics.types.sequence_store_id.SequenceStoreId",
        *,
        config_overrides: Optional[AsyncOmicsClientConfig] = None,
        name: Optional["capo_omics.types.sequence_store_name.SequenceStoreName"] = None,
        description: Optional[
            "capo_omics.types.sequence_store_description.SequenceStoreDescription"
        ] = None,
        client_token: Optional["capo_omics.types.client_token.ClientToken"] = None,
        fallback_location: Optional[
            "capo_omics.types.fallback_location.FallbackLocation"
        ] = None,
        propagated_set_level_tags: Optional[
            "capo_omics.types.propagated_set_level_tags.PropagatedSetLevelTags"
        ] = None,
        s3_access_config: Optional[
            "capo_omics.types.s3_access_config.S3AccessConfig"
        ] = None,
    ) -> "capo_omics.types.update_sequence_store_response.UpdateSequenceStoreResponse":
        """<p>Update one or more parameters for the sequence store.</p>

        Args:
            id: <p>The ID of the sequence store.</p>
            name: <p>A name for the sequence store.</p>
            description: <p>A description for the sequence store.</p>
            client_token: <p>To ensure that requests don't run multiple times, specify a unique token for each request.</p>
            fallback_location: <p>The S3 URI of a bucket and folder to store Read Sets that fail to upload.</p>
            propagated_set_level_tags: <p>The tags keys to propagate to the S3 objects associated with read sets in the sequence store.</p>
            s3_access_config: <p>S3 access configuration parameters.</p>

        Raises:
            capo_omics.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_omics.errors.conflict_exception.ConflictException: <p>The request cannot be applied to the target resource in its current state.</p>
            capo_omics.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred. Try the request again.</p>
            capo_omics.errors.request_timeout_exception.RequestTimeoutException: <p>The request timed out.</p>
            capo_omics.errors.resource_not_found_exception.ResourceNotFoundException: <p>The target resource was not found in the current Region.</p>
            capo_omics.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_omics.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_omics.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_omics.types.update_sequence_store_request.UpdateSequenceStoreRequest]",
        ) -> AsyncOperationResponse[
            "capo_omics.types.update_sequence_store_response.UpdateSequenceStoreResponse"
        ]:
            import capo_omics._operations.omics.update_sequence_store

            (
                output,
                http_response,
            ) = await capo_omics._operations.omics.update_sequence_store.async_update_sequence_store(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_omics.types.update_sequence_store_request.UpdateSequenceStoreRequest = {
            "id": id
        }
        if name is not None:
            input_["name"] = name
        if description is not None:
            input_["description"] = description
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if fallback_location is not None:
            input_["fallback_location"] = fallback_location
        if propagated_set_level_tags is not None:
            input_["propagated_set_level_tags"] = propagated_set_level_tags
        if s3_access_config is not None:
            input_["s3_access_config"] = s3_access_config

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_sequence_store(
        self,
        id: "capo_omics.types.sequence_store_id.SequenceStoreId",
        *,
        config_overrides: Optional[AsyncOmicsClientConfig] = None,
    ) -> "capo_omics.types.delete_sequence_store_response.DeleteSequenceStoreResponse":
        """<p>Deletes a sequence store and returns a response with no body if the operation is successful. You can only delete a sequence store when it does not contain any read sets.</p> <p>Use the <code>BatchDeleteReadSet</code> API operation to ensure that all read sets in the sequence store are deleted. When a sequence store is deleted, all tags associated with the store are also deleted.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/omics/latest/dev/deleting-reference-and-sequence-stores.html">Deleting HealthOmics reference and sequence stores</a> in the <i>Amazon Web Services HealthOmics User Guide</i>.</p>

        Args:
            id: <p>The sequence store's ID.</p>

        Raises:
            capo_omics.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_omics.errors.conflict_exception.ConflictException: <p>The request cannot be applied to the target resource in its current state.</p>
            capo_omics.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred. Try the request again.</p>
            capo_omics.errors.request_timeout_exception.RequestTimeoutException: <p>The request timed out.</p>
            capo_omics.errors.resource_not_found_exception.ResourceNotFoundException: <p>The target resource was not found in the current Region.</p>
            capo_omics.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_omics.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_omics.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_omics.types.delete_sequence_store_request.DeleteSequenceStoreRequest]",
        ) -> AsyncOperationResponse[
            "capo_omics.types.delete_sequence_store_response.DeleteSequenceStoreResponse"
        ]:
            import capo_omics._operations.omics.delete_sequence_store

            (
                output,
                http_response,
            ) = await capo_omics._operations.omics.delete_sequence_store.async_delete_sequence_store(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_omics.types.delete_sequence_store_request.DeleteSequenceStoreRequest = {
            "id": id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_sequence_stores(
        self,
        *,
        config_overrides: Optional[AsyncOmicsClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional["capo_omics.types.next_token.NextToken"] = None,
        filter: Optional[
            "capo_omics.types.sequence_store_filter.SequenceStoreFilter"
        ] = None,
    ) -> "capo_omics.types.list_sequence_stores_response.ListSequenceStoresResponse":
        """<p>Retrieves a list of sequence stores and returns each sequence store's metadata.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/omics/latest/dev/create-sequence-store.html">Creating a HealthOmics sequence store</a> in the <i>Amazon Web Services HealthOmics User Guide</i>.</p>

        Args:
            max_results: <p>The maximum number of stores to return in one page of results.</p>
            next_token: <p>Specify the pagination token from a previous request to retrieve the next page of results.</p>
            filter: <p>A filter to apply to the list.</p>

        Raises:
            capo_omics.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_omics.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred. Try the request again.</p>
            capo_omics.errors.request_timeout_exception.RequestTimeoutException: <p>The request timed out.</p>
            capo_omics.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_omics.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_omics.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_omics.types.list_sequence_stores_request.ListSequenceStoresRequest]",
        ) -> AsyncOperationResponse[
            "capo_omics.types.list_sequence_stores_response.ListSequenceStoresResponse"
        ]:
            import capo_omics._operations.omics.list_sequence_stores

            (
                output,
                http_response,
            ) = await capo_omics._operations.omics.list_sequence_stores.async_list_sequence_stores(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_omics.types.list_sequence_stores_request.ListSequenceStoresRequest = {}
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if filter is not None:
            input_["filter"] = filter

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_sequence_stores(
        self,
        *,
        config_overrides: Optional[AsyncOmicsClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional["capo_omics.types.next_token.NextToken"] = None,
        filter: Optional[
            "capo_omics.types.sequence_store_filter.SequenceStoreFilter"
        ] = None,
    ) -> "AsyncIterator[capo_omics.types.sequence_store_detail.SequenceStoreDetail]":
        _token = next_token
        while True:
            _response = await self.list_sequence_stores(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
                filter=filter,
            )
            _page = _resolve_path(_response, ("sequence_stores",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def abort_multipart_read_set_upload(
        self,
        sequence_store_id: "capo_omics.types.sequence_store_id.SequenceStoreId",
        upload_id: "capo_omics.types.upload_id.UploadId",
        *,
        config_overrides: Optional[AsyncOmicsClientConfig] = None,
    ) -> "capo_omics.types.abort_multipart_read_set_upload_response.AbortMultipartReadSetUploadResponse":
        """<p>Stops a multipart read set upload into a sequence store and returns a response with no body if the operation is successful. To confirm that a multipart read set upload has been stopped, use the <code>ListMultipartReadSetUploads</code> API operation to view all active multipart read set uploads.</p>

        Args:
            sequence_store_id: <p>The sequence store ID for the store involved in the multipart upload.</p>
            upload_id: <p>The ID for the multipart upload.</p>

        Raises:
            capo_omics.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_omics.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred. Try the request again.</p>
            capo_omics.errors.not_supported_operation_exception.NotSupportedOperationException: <p> The operation is not supported by Amazon Omics, or the API does not exist. </p>
            capo_omics.errors.request_timeout_exception.RequestTimeoutException: <p>The request timed out.</p>
            capo_omics.errors.resource_not_found_exception.ResourceNotFoundException: <p>The target resource was not found in the current Region.</p>
            capo_omics.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request exceeds a service quota.</p>
            capo_omics.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_omics.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_omics.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_omics.types.abort_multipart_read_set_upload_request.AbortMultipartReadSetUploadRequest]",
        ) -> AsyncOperationResponse[
            "capo_omics.types.abort_multipart_read_set_upload_response.AbortMultipartReadSetUploadResponse"
        ]:
            import capo_omics._operations.omics.abort_multipart_read_set_upload

            (
                output,
                http_response,
            ) = await capo_omics._operations.omics.abort_multipart_read_set_upload.async_abort_multipart_read_set_upload(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_omics.types.abort_multipart_read_set_upload_request.AbortMultipartReadSetUploadRequest = {
            "sequence_store_id": sequence_store_id,
            "upload_id": upload_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def complete_multipart_read_set_upload(
        self,
        sequence_store_id: "capo_omics.types.sequence_store_id.SequenceStoreId",
        upload_id: "capo_omics.types.upload_id.UploadId",
        parts: "capo_omics.types.complete_read_set_upload_part_list.CompleteReadSetUploadPartList",
        *,
        config_overrides: Optional[AsyncOmicsClientConfig] = None,
    ) -> "capo_omics.types.complete_multipart_read_set_upload_response.CompleteMultipartReadSetUploadResponse":
        """<p>Completes a multipart read set upload into a sequence store after you have initiated the upload process with <code>CreateMultipartReadSetUpload</code> and uploaded all read set parts using <code>UploadReadSetPart</code>. You must specify the parts you uploaded using the parts parameter. If the operation is successful, it returns the read set ID(s) of the uploaded read set(s).</p> <p>For more information, see <a href="https://docs.aws.amazon.com/omics/latest/dev/synchronous-uploads.html">Direct upload to a sequence store</a> in the <i>Amazon Web Services HealthOmics User Guide</i>.</p>

        Args:
            sequence_store_id: <p>The sequence store ID for the store involved in the multipart upload.</p>
            upload_id: <p>The ID for the multipart upload.</p>
            parts: <p>The individual uploads or parts of a multipart upload.</p>

        Raises:
            capo_omics.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_omics.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred. Try the request again.</p>
            capo_omics.errors.not_supported_operation_exception.NotSupportedOperationException: <p> The operation is not supported by Amazon Omics, or the API does not exist. </p>
            capo_omics.errors.request_timeout_exception.RequestTimeoutException: <p>The request timed out.</p>
            capo_omics.errors.resource_not_found_exception.ResourceNotFoundException: <p>The target resource was not found in the current Region.</p>
            capo_omics.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request exceeds a service quota.</p>
            capo_omics.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_omics.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_omics.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_omics.types.complete_multipart_read_set_upload_request.CompleteMultipartReadSetUploadRequest]",
        ) -> AsyncOperationResponse[
            "capo_omics.types.complete_multipart_read_set_upload_response.CompleteMultipartReadSetUploadResponse"
        ]:
            import capo_omics._operations.omics.complete_multipart_read_set_upload

            (
                output,
                http_response,
            ) = await capo_omics._operations.omics.complete_multipart_read_set_upload.async_complete_multipart_read_set_upload(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_omics.types.complete_multipart_read_set_upload_request.CompleteMultipartReadSetUploadRequest = {
            "sequence_store_id": sequence_store_id,
            "upload_id": upload_id,
            "parts": parts,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_multipart_read_set_upload(
        self,
        sequence_store_id: "capo_omics.types.sequence_store_id.SequenceStoreId",
        source_file_type: "capo_omics.types.file_type.FileType",
        subject_id: "capo_omics.types.subject_id.SubjectId",
        sample_id: "capo_omics.types.sample_id.SampleId",
        name: "capo_omics.types.read_set_name.ReadSetName",
        *,
        config_overrides: Optional[AsyncOmicsClientConfig] = None,
        client_token: Optional["capo_omics.types.client_token.ClientToken"] = None,
        generated_from: Optional[
            "capo_omics.types.generated_from.GeneratedFrom"
        ] = None,
        reference_arn: Optional["capo_omics.types.reference_arn.ReferenceArn"] = None,
        description: Optional[
            "capo_omics.types.read_set_description.ReadSetDescription"
        ] = None,
        tags: Optional["capo_omics.types.tag_map.TagMap"] = None,
    ) -> "capo_omics.types.create_multipart_read_set_upload_response.CreateMultipartReadSetUploadResponse":
        """<p>Initiates a multipart read set upload for uploading partitioned source files into a sequence store. You can directly import source files from an EC2 instance and other local compute, or from an S3 bucket. To separate these source files into parts, use the <code>split</code> operation. Each part cannot be larger than 100 MB. If the operation is successful, it provides an <code>uploadId</code> which is required by the <code>UploadReadSetPart</code> API operation to upload parts into a sequence store.</p> <p>To continue uploading a multipart read set into your sequence store, you must use the <code>UploadReadSetPart</code> API operation to upload each part individually following the steps below:</p> <ul> <li> <p>Specify the <code>uploadId</code> obtained from the previous call to <code>CreateMultipartReadSetUpload</code>.</p> </li> <li> <p>Upload parts for that <code>uploadId</code>.</p> </li> </ul> <p>When you have finished uploading parts, use the <code>CompleteMultipartReadSetUpload</code> API to complete the multipart read set upload and to retrieve the final read set IDs in the response.</p> <p>To learn more about creating parts and the <code>split</code> operation, see <a href="https://docs.aws.amazon.com/omics/latest/dev/synchronous-uploads.html">Direct upload to a sequence store</a> in the <i>Amazon Web Services HealthOmics User Guide</i>.</p>

        Args:
            sequence_store_id: <p>The sequence store ID for the store that is the destination of the multipart uploads.</p>
            client_token: <p>An idempotency token that can be used to avoid triggering multiple multipart uploads.</p>
            source_file_type: <p>The type of file being uploaded.</p>
            subject_id: <p>The source's subject ID.</p>
            sample_id: <p>The source's sample ID.</p>
            generated_from: <p>Where the source originated.</p>
            reference_arn: <p>The ARN of the reference.</p>
            name: <p>The name of the read set.</p>
            description: <p>The description of the read set.</p>
            tags: <p>Any tags to add to the read set.</p>

        Raises:
            capo_omics.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_omics.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred. Try the request again.</p>
            capo_omics.errors.not_supported_operation_exception.NotSupportedOperationException: <p> The operation is not supported by Amazon Omics, or the API does not exist. </p>
            capo_omics.errors.request_timeout_exception.RequestTimeoutException: <p>The request timed out.</p>
            capo_omics.errors.resource_not_found_exception.ResourceNotFoundException: <p>The target resource was not found in the current Region.</p>
            capo_omics.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request exceeds a service quota.</p>
            capo_omics.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_omics.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_omics.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_omics.types.create_multipart_read_set_upload_request.CreateMultipartReadSetUploadRequest]",
        ) -> AsyncOperationResponse[
            "capo_omics.types.create_multipart_read_set_upload_response.CreateMultipartReadSetUploadResponse"
        ]:
            import capo_omics._operations.omics.create_multipart_read_set_upload

            (
                output,
                http_response,
            ) = await capo_omics._operations.omics.create_multipart_read_set_upload.async_create_multipart_read_set_upload(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_omics.types.create_multipart_read_set_upload_request.CreateMultipartReadSetUploadRequest = {
            "sequence_store_id": sequence_store_id,
            "source_file_type": source_file_type,
            "subject_id": subject_id,
            "sample_id": sample_id,
            "name": name,
        }
        if client_token is not None:
            input_["client_token"] = client_token
        if generated_from is not None:
            input_["generated_from"] = generated_from
        if reference_arn is not None:
            input_["reference_arn"] = reference_arn
        if description is not None:
            input_["description"] = description
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_read_set_activation_job(
        self,
        id: "capo_omics.types.activation_job_id.ActivationJobId",
        sequence_store_id: "capo_omics.types.sequence_store_id.SequenceStoreId",
        *,
        config_overrides: Optional[AsyncOmicsClientConfig] = None,
    ) -> "capo_omics.types.get_read_set_activation_job_response.GetReadSetActivationJobResponse":
        """<p>Returns detailed information about the status of a read set activation job in JSON format.</p>

        Args:
            id: <p>The job's ID.</p>
            sequence_store_id: <p>The job's sequence store ID.</p>

        Raises:
            capo_omics.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_omics.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred. Try the request again.</p>
            capo_omics.errors.request_timeout_exception.RequestTimeoutException: <p>The request timed out.</p>
            capo_omics.errors.resource_not_found_exception.ResourceNotFoundException: <p>The target resource was not found in the current Region.</p>
            capo_omics.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_omics.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_omics.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_omics.types.get_read_set_activation_job_request.GetReadSetActivationJobRequest]",
        ) -> AsyncOperationResponse[
            "capo_omics.types.get_read_set_activation_job_response.GetReadSetActivationJobResponse"
        ]:
            import capo_omics._operations.omics.get_read_set_activation_job

            (
                output,
                http_response,
            ) = await capo_omics._operations.omics.get_read_set_activation_job.async_get_read_set_activation_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_omics.types.get_read_set_activation_job_request.GetReadSetActivationJobRequest = {
            "id": id,
            "sequence_store_id": sequence_store_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_read_set_export_job(
        self,
        sequence_store_id: "capo_omics.types.sequence_store_id.SequenceStoreId",
        id: "capo_omics.types.export_job_id.ExportJobId",
        *,
        config_overrides: Optional[AsyncOmicsClientConfig] = None,
    ) -> (
        "capo_omics.types.get_read_set_export_job_response.GetReadSetExportJobResponse"
    ):
        """<p>Retrieves status information about a read set export job and returns the data in JSON format. Use this operation to actively monitor the progress of an export job.</p>

        Args:
            sequence_store_id: <p>The job's sequence store ID.</p>
            id: <p>The job's ID.</p>

        Raises:
            capo_omics.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_omics.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred. Try the request again.</p>
            capo_omics.errors.request_timeout_exception.RequestTimeoutException: <p>The request timed out.</p>
            capo_omics.errors.resource_not_found_exception.ResourceNotFoundException: <p>The target resource was not found in the current Region.</p>
            capo_omics.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_omics.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_omics.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_omics.types.get_read_set_export_job_request.GetReadSetExportJobRequest]",
        ) -> AsyncOperationResponse[
            "capo_omics.types.get_read_set_export_job_response.GetReadSetExportJobResponse"
        ]:
            import capo_omics._operations.omics.get_read_set_export_job

            (
                output,
                http_response,
            ) = await capo_omics._operations.omics.get_read_set_export_job.async_get_read_set_export_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_omics.types.get_read_set_export_job_request.GetReadSetExportJobRequest = {
            "sequence_store_id": sequence_store_id,
            "id": id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_read_set_import_job(
        self,
        id: "capo_omics.types.import_job_id.ImportJobId",
        sequence_store_id: "capo_omics.types.sequence_store_id.SequenceStoreId",
        *,
        config_overrides: Optional[AsyncOmicsClientConfig] = None,
    ) -> (
        "capo_omics.types.get_read_set_import_job_response.GetReadSetImportJobResponse"
    ):
        """<p>Gets detailed and status information about a read set import job and returns the data in JSON format.</p>

        Args:
            id: <p>The job's ID.</p>
            sequence_store_id: <p>The job's sequence store ID.</p>

        Raises:
            capo_omics.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_omics.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred. Try the request again.</p>
            capo_omics.errors.request_timeout_exception.RequestTimeoutException: <p>The request timed out.</p>
            capo_omics.errors.resource_not_found_exception.ResourceNotFoundException: <p>The target resource was not found in the current Region.</p>
            capo_omics.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_omics.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_omics.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_omics.types.get_read_set_import_job_request.GetReadSetImportJobRequest]",
        ) -> AsyncOperationResponse[
            "capo_omics.types.get_read_set_import_job_response.GetReadSetImportJobResponse"
        ]:
            import capo_omics._operations.omics.get_read_set_import_job

            (
                output,
                http_response,
            ) = await capo_omics._operations.omics.get_read_set_import_job.async_get_read_set_import_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_omics.types.get_read_set_import_job_request.GetReadSetImportJobRequest = {
            "id": id,
            "sequence_store_id": sequence_store_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_multipart_read_set_uploads(
        self,
        sequence_store_id: "capo_omics.types.sequence_store_id.SequenceStoreId",
        *,
        config_overrides: Optional[AsyncOmicsClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional["capo_omics.types.next_token.NextToken"] = None,
    ) -> "capo_omics.types.list_multipart_read_set_uploads_response.ListMultipartReadSetUploadsResponse":
        """<p>Lists in-progress multipart read set uploads for a sequence store and returns it in a JSON formatted output. Multipart read set uploads are initiated by the <code>CreateMultipartReadSetUploads</code> API operation. This operation returns a response with no body when the upload is complete. </p>

        Args:
            sequence_store_id: <p>The Sequence Store ID used for the multipart uploads.</p>
            max_results: <p>The maximum number of multipart uploads returned in a page.</p>
            next_token: <p>Next token returned in the response of a previous ListMultipartReadSetUploads call. Used to get the next page of results.</p>

        Raises:
            capo_omics.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_omics.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred. Try the request again.</p>
            capo_omics.errors.not_supported_operation_exception.NotSupportedOperationException: <p> The operation is not supported by Amazon Omics, or the API does not exist. </p>
            capo_omics.errors.request_timeout_exception.RequestTimeoutException: <p>The request timed out.</p>
            capo_omics.errors.resource_not_found_exception.ResourceNotFoundException: <p>The target resource was not found in the current Region.</p>
            capo_omics.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request exceeds a service quota.</p>
            capo_omics.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_omics.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_omics.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_omics.types.list_multipart_read_set_uploads_request.ListMultipartReadSetUploadsRequest]",
        ) -> AsyncOperationResponse[
            "capo_omics.types.list_multipart_read_set_uploads_response.ListMultipartReadSetUploadsResponse"
        ]:
            import capo_omics._operations.omics.list_multipart_read_set_uploads

            (
                output,
                http_response,
            ) = await capo_omics._operations.omics.list_multipart_read_set_uploads.async_list_multipart_read_set_uploads(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_omics.types.list_multipart_read_set_uploads_request.ListMultipartReadSetUploadsRequest = {
            "sequence_store_id": sequence_store_id
        }
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

    async def iter_list_multipart_read_set_uploads(
        self,
        sequence_store_id: "capo_omics.types.sequence_store_id.SequenceStoreId",
        *,
        config_overrides: Optional[AsyncOmicsClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional["capo_omics.types.next_token.NextToken"] = None,
    ) -> "AsyncIterator[capo_omics.types.multipart_read_set_upload_list_item.MultipartReadSetUploadListItem]":
        _token = next_token
        while True:
            _response = await self.list_multipart_read_set_uploads(
                sequence_store_id,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("uploads",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_read_set_activation_jobs(
        self,
        sequence_store_id: "capo_omics.types.sequence_store_id.SequenceStoreId",
        *,
        config_overrides: Optional[AsyncOmicsClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional["capo_omics.types.next_token.NextToken"] = None,
        filter: Optional[
            "capo_omics.types.activate_read_set_filter.ActivateReadSetFilter"
        ] = None,
    ) -> "capo_omics.types.list_read_set_activation_jobs_response.ListReadSetActivationJobsResponse":
        """<p>Retrieves a list of read set activation jobs and returns the metadata in a JSON formatted output. To extract metadata from a read set activation job, use the <code>GetReadSetActivationJob</code> API operation.</p>

        Args:
            sequence_store_id: <p>The read set's sequence store ID.</p>
            max_results: <p>The maximum number of read set activation jobs to return in one page of results.</p>
            next_token: <p>Specify the pagination token from a previous request to retrieve the next page of results.</p>
            filter: <p>A filter to apply to the list.</p>

        Raises:
            capo_omics.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_omics.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred. Try the request again.</p>
            capo_omics.errors.request_timeout_exception.RequestTimeoutException: <p>The request timed out.</p>
            capo_omics.errors.resource_not_found_exception.ResourceNotFoundException: <p>The target resource was not found in the current Region.</p>
            capo_omics.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_omics.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_omics.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_omics.types.list_read_set_activation_jobs_request.ListReadSetActivationJobsRequest]",
        ) -> AsyncOperationResponse[
            "capo_omics.types.list_read_set_activation_jobs_response.ListReadSetActivationJobsResponse"
        ]:
            import capo_omics._operations.omics.list_read_set_activation_jobs

            (
                output,
                http_response,
            ) = await capo_omics._operations.omics.list_read_set_activation_jobs.async_list_read_set_activation_jobs(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_omics.types.list_read_set_activation_jobs_request.ListReadSetActivationJobsRequest = {
            "sequence_store_id": sequence_store_id
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if filter is not None:
            input_["filter"] = filter

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_read_set_activation_jobs(
        self,
        sequence_store_id: "capo_omics.types.sequence_store_id.SequenceStoreId",
        *,
        config_overrides: Optional[AsyncOmicsClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional["capo_omics.types.next_token.NextToken"] = None,
        filter: Optional[
            "capo_omics.types.activate_read_set_filter.ActivateReadSetFilter"
        ] = None,
    ) -> "AsyncIterator[capo_omics.types.activate_read_set_job_item.ActivateReadSetJobItem]":
        _token = next_token
        while True:
            _response = await self.list_read_set_activation_jobs(
                sequence_store_id,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
                filter=filter,
            )
            _page = _resolve_path(_response, ("activation_jobs",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_read_set_export_jobs(
        self,
        sequence_store_id: "capo_omics.types.sequence_store_id.SequenceStoreId",
        *,
        config_overrides: Optional[AsyncOmicsClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional["capo_omics.types.next_token.NextToken"] = None,
        filter: Optional[
            "capo_omics.types.export_read_set_filter.ExportReadSetFilter"
        ] = None,
    ) -> "capo_omics.types.list_read_set_export_jobs_response.ListReadSetExportJobsResponse":
        """<p>Retrieves a list of read set export jobs in a JSON formatted response. This API operation is used to check the status of a read set export job initiated by the <code>StartReadSetExportJob</code> API operation.</p>

        Args:
            sequence_store_id: <p>The jobs' sequence store ID.</p>
            max_results: <p>The maximum number of jobs to return in one page of results.</p>
            next_token: <p>Specify the pagination token from a previous request to retrieve the next page of results.</p>
            filter: <p>A filter to apply to the list.</p>

        Raises:
            capo_omics.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_omics.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred. Try the request again.</p>
            capo_omics.errors.request_timeout_exception.RequestTimeoutException: <p>The request timed out.</p>
            capo_omics.errors.resource_not_found_exception.ResourceNotFoundException: <p>The target resource was not found in the current Region.</p>
            capo_omics.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_omics.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_omics.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_omics.types.list_read_set_export_jobs_request.ListReadSetExportJobsRequest]",
        ) -> AsyncOperationResponse[
            "capo_omics.types.list_read_set_export_jobs_response.ListReadSetExportJobsResponse"
        ]:
            import capo_omics._operations.omics.list_read_set_export_jobs

            (
                output,
                http_response,
            ) = await capo_omics._operations.omics.list_read_set_export_jobs.async_list_read_set_export_jobs(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_omics.types.list_read_set_export_jobs_request.ListReadSetExportJobsRequest = {
            "sequence_store_id": sequence_store_id
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if filter is not None:
            input_["filter"] = filter

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_read_set_export_jobs(
        self,
        sequence_store_id: "capo_omics.types.sequence_store_id.SequenceStoreId",
        *,
        config_overrides: Optional[AsyncOmicsClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional["capo_omics.types.next_token.NextToken"] = None,
        filter: Optional[
            "capo_omics.types.export_read_set_filter.ExportReadSetFilter"
        ] = None,
    ) -> "AsyncIterator[capo_omics.types.export_read_set_job_detail.ExportReadSetJobDetail]":
        _token = next_token
        while True:
            _response = await self.list_read_set_export_jobs(
                sequence_store_id,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
                filter=filter,
            )
            _page = _resolve_path(_response, ("export_jobs",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_read_set_import_jobs(
        self,
        sequence_store_id: "capo_omics.types.sequence_store_id.SequenceStoreId",
        *,
        config_overrides: Optional[AsyncOmicsClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional["capo_omics.types.next_token.NextToken"] = None,
        filter: Optional[
            "capo_omics.types.import_read_set_filter.ImportReadSetFilter"
        ] = None,
    ) -> "capo_omics.types.list_read_set_import_jobs_response.ListReadSetImportJobsResponse":
        """<p>Retrieves a list of read set import jobs and returns the data in JSON format.</p>

        Args:
            max_results: <p>The maximum number of jobs to return in one page of results.</p>
            next_token: <p>Specify the pagination token from a previous request to retrieve the next page of results.</p>
            sequence_store_id: <p>The jobs' sequence store ID.</p>
            filter: <p>A filter to apply to the list.</p>

        Raises:
            capo_omics.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_omics.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred. Try the request again.</p>
            capo_omics.errors.request_timeout_exception.RequestTimeoutException: <p>The request timed out.</p>
            capo_omics.errors.resource_not_found_exception.ResourceNotFoundException: <p>The target resource was not found in the current Region.</p>
            capo_omics.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_omics.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_omics.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_omics.types.list_read_set_import_jobs_request.ListReadSetImportJobsRequest]",
        ) -> AsyncOperationResponse[
            "capo_omics.types.list_read_set_import_jobs_response.ListReadSetImportJobsResponse"
        ]:
            import capo_omics._operations.omics.list_read_set_import_jobs

            (
                output,
                http_response,
            ) = await capo_omics._operations.omics.list_read_set_import_jobs.async_list_read_set_import_jobs(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_omics.types.list_read_set_import_jobs_request.ListReadSetImportJobsRequest = {
            "sequence_store_id": sequence_store_id
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if filter is not None:
            input_["filter"] = filter

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_read_set_import_jobs(
        self,
        sequence_store_id: "capo_omics.types.sequence_store_id.SequenceStoreId",
        *,
        config_overrides: Optional[AsyncOmicsClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional["capo_omics.types.next_token.NextToken"] = None,
        filter: Optional[
            "capo_omics.types.import_read_set_filter.ImportReadSetFilter"
        ] = None,
    ) -> (
        "AsyncIterator[capo_omics.types.import_read_set_job_item.ImportReadSetJobItem]"
    ):
        _token = next_token
        while True:
            _response = await self.list_read_set_import_jobs(
                sequence_store_id,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
                filter=filter,
            )
            _page = _resolve_path(_response, ("import_jobs",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_read_set_upload_parts(
        self,
        sequence_store_id: "capo_omics.types.sequence_store_id.SequenceStoreId",
        upload_id: "capo_omics.types.upload_id.UploadId",
        part_source: "capo_omics.types.read_set_part_source.ReadSetPartSource",
        *,
        config_overrides: Optional[AsyncOmicsClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional["capo_omics.types.next_token.NextToken"] = None,
        filter: Optional[
            "capo_omics.types.read_set_upload_part_list_filter.ReadSetUploadPartListFilter"
        ] = None,
    ) -> "capo_omics.types.list_read_set_upload_parts_response.ListReadSetUploadPartsResponse":
        """<p>Lists all parts in a multipart read set upload for a sequence store and returns the metadata in a JSON formatted output.</p>

        Args:
            sequence_store_id: <p>The Sequence Store ID used for the multipart uploads.</p>
            upload_id: <p>The ID for the initiated multipart upload.</p>
            part_source: <p>The source file for the upload part.</p>
            max_results: <p>The maximum number of read set upload parts returned in a page.</p>
            next_token: <p>Next token returned in the response of a previous ListReadSetUploadPartsRequest call. Used to get the next page of results.</p>
            filter: <p>Attributes used to filter for a specific subset of read set part uploads.</p>

        Raises:
            capo_omics.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_omics.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred. Try the request again.</p>
            capo_omics.errors.not_supported_operation_exception.NotSupportedOperationException: <p> The operation is not supported by Amazon Omics, or the API does not exist. </p>
            capo_omics.errors.request_timeout_exception.RequestTimeoutException: <p>The request timed out.</p>
            capo_omics.errors.resource_not_found_exception.ResourceNotFoundException: <p>The target resource was not found in the current Region.</p>
            capo_omics.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request exceeds a service quota.</p>
            capo_omics.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_omics.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_omics.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_omics.types.list_read_set_upload_parts_request.ListReadSetUploadPartsRequest]",
        ) -> AsyncOperationResponse[
            "capo_omics.types.list_read_set_upload_parts_response.ListReadSetUploadPartsResponse"
        ]:
            import capo_omics._operations.omics.list_read_set_upload_parts

            (
                output,
                http_response,
            ) = await capo_omics._operations.omics.list_read_set_upload_parts.async_list_read_set_upload_parts(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_omics.types.list_read_set_upload_parts_request.ListReadSetUploadPartsRequest = {
            "sequence_store_id": sequence_store_id,
            "upload_id": upload_id,
            "part_source": part_source,
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if filter is not None:
            input_["filter"] = filter

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_read_set_upload_parts(
        self,
        sequence_store_id: "capo_omics.types.sequence_store_id.SequenceStoreId",
        upload_id: "capo_omics.types.upload_id.UploadId",
        part_source: "capo_omics.types.read_set_part_source.ReadSetPartSource",
        *,
        config_overrides: Optional[AsyncOmicsClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional["capo_omics.types.next_token.NextToken"] = None,
        filter: Optional[
            "capo_omics.types.read_set_upload_part_list_filter.ReadSetUploadPartListFilter"
        ] = None,
    ) -> "AsyncIterator[capo_omics.types.read_set_upload_part_list_item.ReadSetUploadPartListItem]":
        _token = next_token
        while True:
            _response = await self.list_read_set_upload_parts(
                sequence_store_id,
                upload_id,
                part_source,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
                filter=filter,
            )
            _page = _resolve_path(_response, ("parts",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def start_read_set_activation_job(
        self,
        sequence_store_id: "capo_omics.types.sequence_store_id.SequenceStoreId",
        sources: "capo_omics.types.start_read_set_activation_job_source_list.StartReadSetActivationJobSourceList",
        *,
        config_overrides: Optional[AsyncOmicsClientConfig] = None,
        client_token: Optional["capo_omics.types.client_token.ClientToken"] = None,
    ) -> "capo_omics.types.start_read_set_activation_job_response.StartReadSetActivationJobResponse":
        """<p>Activates an archived read set and returns its metadata in a JSON formatted output. Amazon Web Services HealthOmics automatically archives unused read sets after 30 days. To monitor the status of your read set activation job, use the <code>GetReadSetActivationJob</code> operation.</p> <p>To learn more, see <a href="https://docs.aws.amazon.com/omics/latest/dev/activating-read-sets.html">Activating read sets</a> in the <i>Amazon Web Services HealthOmics User Guide</i>.</p>

        Args:
            sequence_store_id: <p>The read set's sequence store ID.</p>
            client_token: <p>To ensure that jobs don't run multiple times, specify a unique token for each job.</p>
            sources: <p>The job's source files.</p>

        Raises:
            capo_omics.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_omics.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred. Try the request again.</p>
            capo_omics.errors.request_timeout_exception.RequestTimeoutException: <p>The request timed out.</p>
            capo_omics.errors.resource_not_found_exception.ResourceNotFoundException: <p>The target resource was not found in the current Region.</p>
            capo_omics.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request exceeds a service quota.</p>
            capo_omics.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_omics.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_omics.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_omics.types.start_read_set_activation_job_request.StartReadSetActivationJobRequest]",
        ) -> AsyncOperationResponse[
            "capo_omics.types.start_read_set_activation_job_response.StartReadSetActivationJobResponse"
        ]:
            import capo_omics._operations.omics.start_read_set_activation_job

            (
                output,
                http_response,
            ) = await capo_omics._operations.omics.start_read_set_activation_job.async_start_read_set_activation_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_omics.types.start_read_set_activation_job_request.StartReadSetActivationJobRequest = {
            "sequence_store_id": sequence_store_id,
            "sources": sources,
        }
        if client_token is not None:
            input_["client_token"] = client_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def start_read_set_export_job(
        self,
        sequence_store_id: "capo_omics.types.sequence_store_id.SequenceStoreId",
        destination: "capo_omics.types.s3_destination.S3Destination",
        role_arn: "capo_omics.types.role_arn.RoleArn",
        sources: "capo_omics.types.export_read_set_list.ExportReadSetList",
        *,
        config_overrides: Optional[AsyncOmicsClientConfig] = None,
        client_token: Optional["capo_omics.types.client_token.ClientToken"] = None,
    ) -> "capo_omics.types.start_read_set_export_job_response.StartReadSetExportJobResponse":
        """<p>Starts a read set export job. When the export job is finished, the read set is exported to an Amazon S3 bucket which can be retrieved using the <code>GetReadSetExportJob</code> API operation.</p> <p>To monitor the status of the export job, use the <code>ListReadSetExportJobs</code> API operation. </p>

        Args:
            sequence_store_id: <p>The read set's sequence store ID.</p>
            destination: <p>A location for exported files in Amazon S3.</p>
            role_arn: <p>A service role for the job.</p>
            client_token: <p>To ensure that jobs don't run multiple times, specify a unique token for each job.</p>
            sources: <p>The job's source files.</p>

        Raises:
            capo_omics.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_omics.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred. Try the request again.</p>
            capo_omics.errors.request_timeout_exception.RequestTimeoutException: <p>The request timed out.</p>
            capo_omics.errors.resource_not_found_exception.ResourceNotFoundException: <p>The target resource was not found in the current Region.</p>
            capo_omics.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request exceeds a service quota.</p>
            capo_omics.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_omics.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_omics.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_omics.types.start_read_set_export_job_request.StartReadSetExportJobRequest]",
        ) -> AsyncOperationResponse[
            "capo_omics.types.start_read_set_export_job_response.StartReadSetExportJobResponse"
        ]:
            import capo_omics._operations.omics.start_read_set_export_job

            (
                output,
                http_response,
            ) = await capo_omics._operations.omics.start_read_set_export_job.async_start_read_set_export_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_omics.types.start_read_set_export_job_request.StartReadSetExportJobRequest = {
            "sequence_store_id": sequence_store_id,
            "destination": destination,
            "role_arn": role_arn,
            "sources": sources,
        }
        if client_token is not None:
            input_["client_token"] = client_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def start_read_set_import_job(
        self,
        sequence_store_id: "capo_omics.types.sequence_store_id.SequenceStoreId",
        role_arn: "capo_omics.types.role_arn.RoleArn",
        sources: "capo_omics.types.start_read_set_import_job_source_list.StartReadSetImportJobSourceList",
        *,
        config_overrides: Optional[AsyncOmicsClientConfig] = None,
        client_token: Optional["capo_omics.types.client_token.ClientToken"] = None,
    ) -> "capo_omics.types.start_read_set_import_job_response.StartReadSetImportJobResponse":
        """<p>Imports a read set from the sequence store. Read set import jobs support a maximum of 100 read sets of different types. Monitor the progress of your read set import job by calling the <code>GetReadSetImportJob</code> API operation.</p>

        Args:
            sequence_store_id: <p>The read set's sequence store ID.</p>
            role_arn: <p>A service role for the job.</p>
            client_token: <p>To ensure that jobs don't run multiple times, specify a unique token for each job.</p>
            sources: <p>The job's source files.</p>

        Raises:
            capo_omics.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_omics.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred. Try the request again.</p>
            capo_omics.errors.request_timeout_exception.RequestTimeoutException: <p>The request timed out.</p>
            capo_omics.errors.resource_not_found_exception.ResourceNotFoundException: <p>The target resource was not found in the current Region.</p>
            capo_omics.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request exceeds a service quota.</p>
            capo_omics.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_omics.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_omics.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_omics.types.start_read_set_import_job_request.StartReadSetImportJobRequest]",
        ) -> AsyncOperationResponse[
            "capo_omics.types.start_read_set_import_job_response.StartReadSetImportJobResponse"
        ]:
            import capo_omics._operations.omics.start_read_set_import_job

            (
                output,
                http_response,
            ) = await capo_omics._operations.omics.start_read_set_import_job.async_start_read_set_import_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_omics.types.start_read_set_import_job_request.StartReadSetImportJobRequest = {
            "sequence_store_id": sequence_store_id,
            "role_arn": role_arn,
            "sources": sources,
        }
        if client_token is not None:
            input_["client_token"] = client_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def upload_read_set_part(
        self,
        sequence_store_id: "capo_omics.types.sequence_store_id.SequenceStoreId",
        upload_id: "capo_omics.types.upload_id.UploadId",
        part_source: "capo_omics.types.read_set_part_source.ReadSetPartSource",
        part_number: int,
        payload: Body[AsyncIterator[bytes]] | AsyncIterator[bytes] | bytes,
        *,
        config_overrides: Optional[AsyncOmicsClientConfig] = None,
    ) -> "capo_omics.types.upload_read_set_part_response.UploadReadSetPartResponse":
        """<p>Uploads a specific part of a read set into a sequence store. When you a upload a read set part with a part number that already exists, the new part replaces the existing one. This operation returns a JSON formatted response containing a string identifier that is used to confirm that parts are being added to the intended upload.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/omics/latest/dev/synchronous-uploads.html">Direct upload to a sequence store</a> in the <i>Amazon Web Services HealthOmics User Guide</i>.</p>

        Args:
            sequence_store_id: <p>The Sequence Store ID used for the multipart upload.</p>
            upload_id: <p>The ID for the initiated multipart upload.</p>
            part_source: <p>The source file for an upload part.</p>
            part_number: <p>The number of the part being uploaded.</p>
            payload: <p>The read set data to upload for a part.</p>

        Raises:
            capo_omics.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_omics.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred. Try the request again.</p>
            capo_omics.errors.not_supported_operation_exception.NotSupportedOperationException: <p> The operation is not supported by Amazon Omics, or the API does not exist. </p>
            capo_omics.errors.request_timeout_exception.RequestTimeoutException: <p>The request timed out.</p>
            capo_omics.errors.resource_not_found_exception.ResourceNotFoundException: <p>The target resource was not found in the current Region.</p>
            capo_omics.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request exceeds a service quota.</p>
            capo_omics.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_omics.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_omics.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_omics.types.upload_read_set_part_request.UploadReadSetPartRequest]",
        ) -> AsyncOperationResponse[
            "capo_omics.types.upload_read_set_part_response.UploadReadSetPartResponse"
        ]:
            import capo_omics._operations.omics.upload_read_set_part

            (
                output,
                http_response,
            ) = await capo_omics._operations.omics.upload_read_set_part.async_upload_read_set_part(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_omics.types.upload_read_set_part_request.UploadReadSetPartRequest = {
            "sequence_store_id": sequence_store_id,
            "upload_id": upload_id,
            "part_source": part_source,
            "part_number": part_number,
            "payload": ensure_async_iterator(payload),
        }

        async with aclosing_bodies(input_):
            response = await aexecute_pipeline(
                AsyncOperationRequest(input=input_, options=options_),
                handler=_handler,
                interceptors=list(interceptors_),
            )
            await response.response.aclose()
            return response.output

    async def get_read_set_metadata(
        self,
        id: "capo_omics.types.read_set_id.ReadSetId",
        sequence_store_id: "capo_omics.types.sequence_store_id.SequenceStoreId",
        *,
        config_overrides: Optional[AsyncOmicsClientConfig] = None,
    ) -> "capo_omics.types.get_read_set_metadata_response.GetReadSetMetadataResponse":
        """<p>Retrieves the metadata for a read set from a sequence store in JSON format. This operation does not return tags. To retrieve the list of tags for a read set, use the <code>ListTagsForResource</code> API operation.</p>

        Args:
            id: <p>The read set's ID.</p>
            sequence_store_id: <p>The read set's sequence store ID.</p>

        Raises:
            capo_omics.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_omics.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred. Try the request again.</p>
            capo_omics.errors.request_timeout_exception.RequestTimeoutException: <p>The request timed out.</p>
            capo_omics.errors.resource_not_found_exception.ResourceNotFoundException: <p>The target resource was not found in the current Region.</p>
            capo_omics.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_omics.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_omics.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_omics.types.get_read_set_metadata_request.GetReadSetMetadataRequest]",
        ) -> AsyncOperationResponse[
            "capo_omics.types.get_read_set_metadata_response.GetReadSetMetadataResponse"
        ]:
            import capo_omics._operations.omics.get_read_set_metadata

            (
                output,
                http_response,
            ) = await capo_omics._operations.omics.get_read_set_metadata.async_get_read_set_metadata(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_omics.types.get_read_set_metadata_request.GetReadSetMetadataRequest = {
            "id": id,
            "sequence_store_id": sequence_store_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_read_sets(
        self,
        sequence_store_id: "capo_omics.types.sequence_store_id.SequenceStoreId",
        *,
        config_overrides: Optional[AsyncOmicsClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional["capo_omics.types.next_token.NextToken"] = None,
        filter: Optional["capo_omics.types.read_set_filter.ReadSetFilter"] = None,
    ) -> "capo_omics.types.list_read_sets_response.ListReadSetsResponse":
        """<p>Retrieves a list of read sets from a sequence store ID and returns the metadata in JSON format.</p>

        Args:
            sequence_store_id: <p>The jobs' sequence store ID.</p>
            max_results: <p>The maximum number of read sets to return in one page of results.</p>
            next_token: <p>Specify the pagination token from a previous request to retrieve the next page of results.</p>
            filter: <p>A filter to apply to the list.</p>

        Raises:
            capo_omics.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_omics.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred. Try the request again.</p>
            capo_omics.errors.request_timeout_exception.RequestTimeoutException: <p>The request timed out.</p>
            capo_omics.errors.resource_not_found_exception.ResourceNotFoundException: <p>The target resource was not found in the current Region.</p>
            capo_omics.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_omics.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_omics.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_omics.types.list_read_sets_request.ListReadSetsRequest]",
        ) -> AsyncOperationResponse[
            "capo_omics.types.list_read_sets_response.ListReadSetsResponse"
        ]:
            import capo_omics._operations.omics.list_read_sets

            (
                output,
                http_response,
            ) = await capo_omics._operations.omics.list_read_sets.async_list_read_sets(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_omics.types.list_read_sets_request.ListReadSetsRequest = {
            "sequence_store_id": sequence_store_id
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if filter is not None:
            input_["filter"] = filter

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_read_sets(
        self,
        sequence_store_id: "capo_omics.types.sequence_store_id.SequenceStoreId",
        *,
        config_overrides: Optional[AsyncOmicsClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional["capo_omics.types.next_token.NextToken"] = None,
        filter: Optional["capo_omics.types.read_set_filter.ReadSetFilter"] = None,
    ) -> "AsyncIterator[capo_omics.types.read_set_list_item.ReadSetListItem]":
        _token = next_token
        while True:
            _response = await self.list_read_sets(
                sequence_store_id,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
                filter=filter,
            )
            _page = _resolve_path(_response, ("read_sets",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    @asynccontextmanager
    async def get_read_set(
        self,
        id: "capo_omics.types.read_set_id.ReadSetId",
        sequence_store_id: "capo_omics.types.sequence_store_id.SequenceStoreId",
        part_number: int,
        *,
        config_overrides: Optional[AsyncOmicsClientConfig] = None,
        file: Optional["capo_omics.types.read_set_file.ReadSetFile"] = None,
    ) -> "AsyncGenerator[capo_omics.types.get_read_set_response.GetReadSetResponse]":
        """<p>Retrieves detailed information from parts of a read set and returns the read set in the same format that it was uploaded. You must have read sets uploaded to your sequence store in order to run this operation.</p>

        Args:
            id: <p>The read set's ID.</p>
            sequence_store_id: <p>The read set's sequence store ID.</p>
            file: <p>The file to retrieve.</p>
            part_number: <p>The part number to retrieve.</p>

        Raises:
            capo_omics.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_omics.errors.conflict_exception.ConflictException: <p>The request cannot be applied to the target resource in its current state.</p>
            capo_omics.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred. Try the request again.</p>
            capo_omics.errors.range_not_satisfiable_exception.RangeNotSatisfiableException: <p>The ranges specified in the request are not valid.</p>
            capo_omics.errors.request_timeout_exception.RequestTimeoutException: <p>The request timed out.</p>
            capo_omics.errors.resource_not_found_exception.ResourceNotFoundException: <p>The target resource was not found in the current Region.</p>
            capo_omics.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_omics.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_omics.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_omics.types.get_read_set_request.GetReadSetRequest]",
        ) -> AsyncOperationResponse[
            "capo_omics.types.get_read_set_response.GetReadSetResponse"
        ]:
            import capo_omics._operations.omics.get_read_set

            (
                output,
                http_response,
            ) = await capo_omics._operations.omics.get_read_set.async_get_read_set(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_omics.types.get_read_set_request.GetReadSetRequest = {
            "id": id,
            "sequence_store_id": sequence_store_id,
            "part_number": part_number,
        }
        if file is not None:
            input_["file"] = file

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        try:
            yield response.output
        finally:
            await response.response.aclose()

    async def batch_delete_read_set(
        self,
        ids: "capo_omics.types.read_set_id_list.ReadSetIdList",
        sequence_store_id: "capo_omics.types.sequence_store_id.SequenceStoreId",
        *,
        config_overrides: Optional[AsyncOmicsClientConfig] = None,
    ) -> "capo_omics.types.batch_delete_read_set_response.BatchDeleteReadSetResponse":
        """<p>Deletes one or more read sets. If the operation is successful, it returns a response with no body. If there is an error with deleting one of the read sets, the operation returns an error list. If the operation successfully deletes only a subset of files, it will return an error list for the remaining files that fail to be deleted. There is a limit of 100 read sets that can be deleted in each <code>BatchDeleteReadSet</code> API call.</p>

        Args:
            ids: <p>The read sets' IDs.</p>
            sequence_store_id: <p>The read sets' sequence store ID.</p>

        Raises:
            capo_omics.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_omics.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred. Try the request again.</p>
            capo_omics.errors.request_timeout_exception.RequestTimeoutException: <p>The request timed out.</p>
            capo_omics.errors.resource_not_found_exception.ResourceNotFoundException: <p>The target resource was not found in the current Region.</p>
            capo_omics.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_omics.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_omics.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_omics.types.batch_delete_read_set_request.BatchDeleteReadSetRequest]",
        ) -> AsyncOperationResponse[
            "capo_omics.types.batch_delete_read_set_response.BatchDeleteReadSetResponse"
        ]:
            import capo_omics._operations.omics.batch_delete_read_set

            (
                output,
                http_response,
            ) = await capo_omics._operations.omics.batch_delete_read_set.async_batch_delete_read_set(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_omics.types.batch_delete_read_set_request.BatchDeleteReadSetRequest = {
            "ids": ids,
            "sequence_store_id": sequence_store_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_share(
        self,
        resource_arn: str,
        principal_subscriber: str,
        *,
        config_overrides: Optional[AsyncOmicsClientConfig] = None,
        share_name: Optional["capo_omics.types.share_name.ShareName"] = None,
    ) -> "capo_omics.types.create_share_response.CreateShareResponse":
        """<p>Creates a cross-account shared resource. The resource owner makes an offer to share the resource with the principal subscriber (an Amazon Web Services user with a different account than the resource owner).</p> <p>The following resources support cross-account sharing:</p> <ul> <li> <p>HealthOmics variant stores</p> </li> <li> <p>HealthOmics annotation stores</p> </li> <li> <p>Private workflows</p> </li> </ul>

        Args:
            resource_arn: <p>The ARN of the resource to be shared.</p>
            principal_subscriber: <p>The principal subscriber is the account being offered shared access to the resource. </p>
            share_name: <p>A name that the owner defines for the share.</p>

        Raises:
            capo_omics.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_omics.errors.conflict_exception.ConflictException: <p>The request cannot be applied to the target resource in its current state.</p>
            capo_omics.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred. Try the request again.</p>
            capo_omics.errors.resource_not_found_exception.ResourceNotFoundException: <p>The target resource was not found in the current Region.</p>
            capo_omics.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request exceeds a service quota.</p>
            capo_omics.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_omics.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_omics.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_omics.types.create_share_request.CreateShareRequest]",
        ) -> AsyncOperationResponse[
            "capo_omics.types.create_share_response.CreateShareResponse"
        ]:
            import capo_omics._operations.omics.create_share

            (
                output,
                http_response,
            ) = await capo_omics._operations.omics.create_share.async_create_share(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_omics.types.create_share_request.CreateShareRequest = {
            "resource_arn": resource_arn,
            "principal_subscriber": principal_subscriber,
        }
        if share_name is not None:
            input_["share_name"] = share_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_share(
        self,
        share_id: str,
        *,
        config_overrides: Optional[AsyncOmicsClientConfig] = None,
    ) -> "capo_omics.types.get_share_response.GetShareResponse":
        """<p>Retrieves the metadata for the specified resource share.</p>

        Args:
            share_id: <p>The ID of the share.</p>

        Raises:
            capo_omics.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_omics.errors.conflict_exception.ConflictException: <p>The request cannot be applied to the target resource in its current state.</p>
            capo_omics.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred. Try the request again.</p>
            capo_omics.errors.resource_not_found_exception.ResourceNotFoundException: <p>The target resource was not found in the current Region.</p>
            capo_omics.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request exceeds a service quota.</p>
            capo_omics.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_omics.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_omics.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_omics.types.get_share_request.GetShareRequest]",
        ) -> AsyncOperationResponse[
            "capo_omics.types.get_share_response.GetShareResponse"
        ]:
            import capo_omics._operations.omics.get_share

            (
                output,
                http_response,
            ) = await capo_omics._operations.omics.get_share.async_get_share(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_omics.types.get_share_request.GetShareRequest = {
            "share_id": share_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def accept_share(
        self,
        share_id: str,
        *,
        config_overrides: Optional[AsyncOmicsClientConfig] = None,
    ) -> "capo_omics.types.accept_share_response.AcceptShareResponse":
        """<p>Accept a resource share request.</p>

        Args:
            share_id: <p>The ID of the resource share.</p>

        Raises:
            capo_omics.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_omics.errors.conflict_exception.ConflictException: <p>The request cannot be applied to the target resource in its current state.</p>
            capo_omics.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred. Try the request again.</p>
            capo_omics.errors.resource_not_found_exception.ResourceNotFoundException: <p>The target resource was not found in the current Region.</p>
            capo_omics.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request exceeds a service quota.</p>
            capo_omics.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_omics.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_omics.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_omics.types.accept_share_request.AcceptShareRequest]",
        ) -> AsyncOperationResponse[
            "capo_omics.types.accept_share_response.AcceptShareResponse"
        ]:
            import capo_omics._operations.omics.accept_share

            (
                output,
                http_response,
            ) = await capo_omics._operations.omics.accept_share.async_accept_share(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_omics.types.accept_share_request.AcceptShareRequest = {
            "share_id": share_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_share(
        self,
        share_id: str,
        *,
        config_overrides: Optional[AsyncOmicsClientConfig] = None,
    ) -> "capo_omics.types.delete_share_response.DeleteShareResponse":
        """<p>Deletes a resource share. If you are the resource owner, the subscriber will no longer have access to the shared resource. If you are the subscriber, this operation deletes your access to the share.</p>

        Args:
            share_id: <p>The ID for the resource share to be deleted.</p>

        Raises:
            capo_omics.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_omics.errors.conflict_exception.ConflictException: <p>The request cannot be applied to the target resource in its current state.</p>
            capo_omics.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred. Try the request again.</p>
            capo_omics.errors.resource_not_found_exception.ResourceNotFoundException: <p>The target resource was not found in the current Region.</p>
            capo_omics.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request exceeds a service quota.</p>
            capo_omics.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_omics.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_omics.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_omics.types.delete_share_request.DeleteShareRequest]",
        ) -> AsyncOperationResponse[
            "capo_omics.types.delete_share_response.DeleteShareResponse"
        ]:
            import capo_omics._operations.omics.delete_share

            (
                output,
                http_response,
            ) = await capo_omics._operations.omics.delete_share.async_delete_share(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_omics.types.delete_share_request.DeleteShareRequest = {
            "share_id": share_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_shares(
        self,
        resource_owner: "capo_omics.types.resource_owner.ResourceOwner",
        *,
        config_overrides: Optional[AsyncOmicsClientConfig] = None,
        filter: Optional["capo_omics.types.filter.Filter"] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
    ) -> "capo_omics.types.list_shares_response.ListSharesResponse":
        """<p>Retrieves the resource shares associated with an account. Use the filter parameter to retrieve a specific subset of the shares.</p>

        Args:
            resource_owner: <p>The account that owns the resource shares.</p>
            filter: <p>Attributes that you use to filter for a specific subset of resource shares.</p>
            next_token: <p>Next token returned in the response of a previous ListReadSetUploadPartsRequest call. Used to get the next page of results.</p>
            max_results: <p>The maximum number of shares to return in one page of results.</p>

        Raises:
            capo_omics.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_omics.errors.conflict_exception.ConflictException: <p>The request cannot be applied to the target resource in its current state.</p>
            capo_omics.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred. Try the request again.</p>
            capo_omics.errors.resource_not_found_exception.ResourceNotFoundException: <p>The target resource was not found in the current Region.</p>
            capo_omics.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request exceeds a service quota.</p>
            capo_omics.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_omics.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_omics.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_omics.types.list_shares_request.ListSharesRequest]",
        ) -> AsyncOperationResponse[
            "capo_omics.types.list_shares_response.ListSharesResponse"
        ]:
            import capo_omics._operations.omics.list_shares

            (
                output,
                http_response,
            ) = await capo_omics._operations.omics.list_shares.async_list_shares(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_omics.types.list_shares_request.ListSharesRequest = {
            "resource_owner": resource_owner
        }
        if filter is not None:
            input_["filter"] = filter
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

    async def iter_list_shares(
        self,
        resource_owner: "capo_omics.types.resource_owner.ResourceOwner",
        *,
        config_overrides: Optional[AsyncOmicsClientConfig] = None,
        filter: Optional["capo_omics.types.filter.Filter"] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
    ) -> "AsyncIterator[capo_omics.types.share_details.ShareDetails]":
        _token = next_token
        while True:
            _response = await self.list_shares(
                resource_owner,
                config_overrides=config_overrides,
                filter=filter,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("shares",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_tags_for_resource(
        self,
        resource_arn: "capo_omics.types.tag_arn.TagArn",
        *,
        config_overrides: Optional[AsyncOmicsClientConfig] = None,
    ) -> "capo_omics.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>Retrieves a list of tags for a resource.</p>

        Args:
            resource_arn: <p>The resource's ARN.</p>

        Raises:
            capo_omics.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_omics.errors.conflict_exception.ConflictException: <p>The request cannot be applied to the target resource in its current state.</p>
            capo_omics.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred. Try the request again.</p>
            capo_omics.errors.request_timeout_exception.RequestTimeoutException: <p>The request timed out.</p>
            capo_omics.errors.resource_not_found_exception.ResourceNotFoundException: <p>The target resource was not found in the current Region.</p>
            capo_omics.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request exceeds a service quota.</p>
            capo_omics.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_omics.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_omics.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_omics.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_omics.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import capo_omics._operations.omics.list_tags_for_resource

            (
                output,
                http_response,
            ) = await capo_omics._operations.omics.list_tags_for_resource.async_list_tags_for_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_omics.types.list_tags_for_resource_request.ListTagsForResourceRequest = {
            "resource_arn": resource_arn
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
        resource_arn: "capo_omics.types.tag_arn.TagArn",
        tags: "capo_omics.types.tag_map.TagMap",
        *,
        config_overrides: Optional[AsyncOmicsClientConfig] = None,
    ) -> "capo_omics.types.tag_resource_response.TagResourceResponse":
        """<p>Tags a resource.</p>

        Args:
            resource_arn: <p>The resource's ARN.</p>
            tags: <p>Tags for the resource.</p>

        Raises:
            capo_omics.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_omics.errors.conflict_exception.ConflictException: <p>The request cannot be applied to the target resource in its current state.</p>
            capo_omics.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred. Try the request again.</p>
            capo_omics.errors.request_timeout_exception.RequestTimeoutException: <p>The request timed out.</p>
            capo_omics.errors.resource_not_found_exception.ResourceNotFoundException: <p>The target resource was not found in the current Region.</p>
            capo_omics.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request exceeds a service quota.</p>
            capo_omics.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_omics.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_omics.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_omics.types.tag_resource_request.TagResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_omics.types.tag_resource_response.TagResourceResponse"
        ]:
            import capo_omics._operations.omics.tag_resource

            (
                output,
                http_response,
            ) = await capo_omics._operations.omics.tag_resource.async_tag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_omics.types.tag_resource_request.TagResourceRequest = {
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
        resource_arn: "capo_omics.types.tag_arn.TagArn",
        tag_keys: "capo_omics.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[AsyncOmicsClientConfig] = None,
    ) -> "capo_omics.types.untag_resource_response.UntagResourceResponse":
        """<p>Removes tags from a resource.</p>

        Args:
            resource_arn: <p>The resource's ARN.</p>
            tag_keys: <p>Keys of tags to remove.</p>

        Raises:
            capo_omics.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_omics.errors.conflict_exception.ConflictException: <p>The request cannot be applied to the target resource in its current state.</p>
            capo_omics.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred. Try the request again.</p>
            capo_omics.errors.request_timeout_exception.RequestTimeoutException: <p>The request timed out.</p>
            capo_omics.errors.resource_not_found_exception.ResourceNotFoundException: <p>The target resource was not found in the current Region.</p>
            capo_omics.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request exceeds a service quota.</p>
            capo_omics.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_omics.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_omics.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_omics.types.untag_resource_request.UntagResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_omics.types.untag_resource_response.UntagResourceResponse"
        ]:
            import capo_omics._operations.omics.untag_resource

            (
                output,
                http_response,
            ) = await capo_omics._operations.omics.untag_resource.async_untag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_omics.types.untag_resource_request.UntagResourceRequest = {
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

    async def start_variant_import_job(
        self,
        destination_name: "capo_omics.types.store_name.StoreName",
        role_arn: "capo_omics.types.arn.Arn",
        items: "capo_omics.types.variant_import_item_sources.VariantImportItemSources",
        *,
        config_overrides: Optional[AsyncOmicsClientConfig] = None,
        run_left_normalization: Optional[
            "capo_omics.types.run_left_normalization.RunLeftNormalization"
        ] = None,
        annotation_fields: Optional[
            "capo_omics.types.annotation_field_map.AnnotationFieldMap"
        ] = None,
    ) -> "capo_omics.types.start_variant_import_response.StartVariantImportResponse":
        """<important> <p>Amazon Web Services HealthOmics variant stores and annotation stores are no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see <a href="https://docs.aws.amazon.com/omics/latest/dev/variant-store-availability-change.html"> Amazon Web Services HealthOmics variant store and annotation store availability change</a>.</p> </important> <p>Starts a variant import job.</p>

        Args:
            destination_name: <p>The destination variant store for the job.</p>
            role_arn: <p>A service role for the job.</p>
            items: <p>Items to import.</p>
            run_left_normalization: <p>The job's left normalization setting.</p>
            annotation_fields: <p>The annotation schema generated by the parsed annotation data.</p>

        Raises:
            capo_omics.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_omics.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred. Try the request again.</p>
            capo_omics.errors.resource_not_found_exception.ResourceNotFoundException: <p>The target resource was not found in the current Region.</p>
            capo_omics.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request exceeds a service quota.</p>
            capo_omics.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_omics.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_omics.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_omics.types.start_variant_import_request.StartVariantImportRequest]",
        ) -> AsyncOperationResponse[
            "capo_omics.types.start_variant_import_response.StartVariantImportResponse"
        ]:
            import capo_omics._operations.omics.start_variant_import_job

            (
                output,
                http_response,
            ) = await capo_omics._operations.omics.start_variant_import_job.async_start_variant_import_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_omics.types.start_variant_import_request.StartVariantImportRequest = {
            "destination_name": destination_name,
            "role_arn": role_arn,
            "items": items,
        }
        if run_left_normalization is not None:
            input_["run_left_normalization"] = run_left_normalization
        if annotation_fields is not None:
            input_["annotation_fields"] = annotation_fields

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_variant_import_job(
        self,
        job_id: "capo_omics.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncOmicsClientConfig] = None,
    ) -> "capo_omics.types.get_variant_import_response.GetVariantImportResponse":
        """<important> <p>Amazon Web Services HealthOmics variant stores and annotation stores are no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see <a href="https://docs.aws.amazon.com/omics/latest/dev/variant-store-availability-change.html"> Amazon Web Services HealthOmics variant store and annotation store availability change</a>.</p> </important> <p>Gets information about a variant import job.</p>

        Args:
            job_id: <p>The job's ID.</p>

        Raises:
            capo_omics.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_omics.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred. Try the request again.</p>
            capo_omics.errors.resource_not_found_exception.ResourceNotFoundException: <p>The target resource was not found in the current Region.</p>
            capo_omics.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_omics.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_omics.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_omics.types.get_variant_import_request.GetVariantImportRequest]",
        ) -> AsyncOperationResponse[
            "capo_omics.types.get_variant_import_response.GetVariantImportResponse"
        ]:
            import capo_omics._operations.omics.get_variant_import_job

            (
                output,
                http_response,
            ) = await capo_omics._operations.omics.get_variant_import_job.async_get_variant_import_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_omics.types.get_variant_import_request.GetVariantImportRequest = {
            "job_id": job_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def cancel_variant_import_job(
        self,
        job_id: "capo_omics.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncOmicsClientConfig] = None,
    ) -> "capo_omics.types.cancel_variant_import_response.CancelVariantImportResponse":
        """<important> <p>Amazon Web Services HealthOmics variant stores and annotation stores are no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see <a href="https://docs.aws.amazon.com/omics/latest/dev/variant-store-availability-change.html"> Amazon Web Services HealthOmics variant store and annotation store availability change</a>.</p> </important> <p>Cancels a variant import job.</p>

        Args:
            job_id: <p>The job's ID.</p>

        Raises:
            capo_omics.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_omics.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred. Try the request again.</p>
            capo_omics.errors.resource_not_found_exception.ResourceNotFoundException: <p>The target resource was not found in the current Region.</p>
            capo_omics.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_omics.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_omics.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_omics.types.cancel_variant_import_request.CancelVariantImportRequest]",
        ) -> AsyncOperationResponse[
            "capo_omics.types.cancel_variant_import_response.CancelVariantImportResponse"
        ]:
            import capo_omics._operations.omics.cancel_variant_import_job

            (
                output,
                http_response,
            ) = await capo_omics._operations.omics.cancel_variant_import_job.async_cancel_variant_import_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_omics.types.cancel_variant_import_request.CancelVariantImportRequest = {
            "job_id": job_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_variant_import_jobs(
        self,
        *,
        config_overrides: Optional[AsyncOmicsClientConfig] = None,
        max_results: Optional[int] = None,
        ids: Optional["capo_omics.types.id_list.IdList"] = None,
        next_token: Optional[str] = None,
        filter: Optional[
            "capo_omics.types.list_variant_import_jobs_filter.ListVariantImportJobsFilter"
        ] = None,
    ) -> "capo_omics.types.list_variant_import_jobs_response.ListVariantImportJobsResponse":
        """<important> <p>Amazon Web Services HealthOmics variant stores and annotation stores are no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see <a href="https://docs.aws.amazon.com/omics/latest/dev/variant-store-availability-change.html"> Amazon Web Services HealthOmics variant store and annotation store availability change</a>.</p> </important> <p>Retrieves a list of variant import jobs.</p>

        Args:
            max_results: <p>The maximum number of import jobs to return in one page of results.</p>
            ids: <p>A list of job IDs.</p>
            next_token: <p>Specify the pagination token from a previous request to retrieve the next page of results.</p>
            filter: <p>A filter to apply to the list.</p>

        Raises:
            capo_omics.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_omics.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred. Try the request again.</p>
            capo_omics.errors.resource_not_found_exception.ResourceNotFoundException: <p>The target resource was not found in the current Region.</p>
            capo_omics.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_omics.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_omics.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_omics.types.list_variant_import_jobs_request.ListVariantImportJobsRequest]",
        ) -> AsyncOperationResponse[
            "capo_omics.types.list_variant_import_jobs_response.ListVariantImportJobsResponse"
        ]:
            import capo_omics._operations.omics.list_variant_import_jobs

            (
                output,
                http_response,
            ) = await capo_omics._operations.omics.list_variant_import_jobs.async_list_variant_import_jobs(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_omics.types.list_variant_import_jobs_request.ListVariantImportJobsRequest = {}
        if max_results is not None:
            input_["max_results"] = max_results
        if ids is not None:
            input_["ids"] = ids
        if next_token is not None:
            input_["next_token"] = next_token
        if filter is not None:
            input_["filter"] = filter

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_variant_import_jobs(
        self,
        *,
        config_overrides: Optional[AsyncOmicsClientConfig] = None,
        max_results: Optional[int] = None,
        ids: Optional["capo_omics.types.id_list.IdList"] = None,
        next_token: Optional[str] = None,
        filter: Optional[
            "capo_omics.types.list_variant_import_jobs_filter.ListVariantImportJobsFilter"
        ] = None,
    ) -> "AsyncIterator[capo_omics.types.variant_import_job_item.VariantImportJobItem]":
        _token = next_token
        while True:
            _response = await self.list_variant_import_jobs(
                config_overrides=config_overrides,
                max_results=max_results,
                ids=ids,
                next_token=_token,
                filter=filter,
            )
            _page = _resolve_path(_response, ("variant_import_jobs",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def create_variant_store(
        self,
        reference: "capo_omics.types.reference_item.ReferenceItem",
        *,
        config_overrides: Optional[AsyncOmicsClientConfig] = None,
        name: Optional["capo_omics.types.store_name.StoreName"] = None,
        description: Optional["capo_omics.types.description.Description"] = None,
        tags: Optional["capo_omics.types.tag_map.TagMap"] = None,
        sse_config: Optional["capo_omics.types.sse_config.SseConfig"] = None,
    ) -> "capo_omics.types.create_variant_store_response.CreateVariantStoreResponse":
        """<important> <p>Amazon Web Services HealthOmics variant stores and annotation stores are no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see <a href="https://docs.aws.amazon.com/omics/latest/dev/variant-store-availability-change.html"> Amazon Web Services HealthOmics variant store and annotation store availability change</a>.</p> </important> <p>Creates a variant store.</p>

        Args:
            reference: <p>The genome reference for the store's variants.</p>
            name: <p>A name for the store.</p>
            description: <p>A description for the store.</p>
            tags: <p>Tags for the store.</p>
            sse_config: <p>Server-side encryption (SSE) settings for the store.</p>

        Raises:
            capo_omics.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_omics.errors.conflict_exception.ConflictException: <p>The request cannot be applied to the target resource in its current state.</p>
            capo_omics.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred. Try the request again.</p>
            capo_omics.errors.resource_not_found_exception.ResourceNotFoundException: <p>The target resource was not found in the current Region.</p>
            capo_omics.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request exceeds a service quota.</p>
            capo_omics.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_omics.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_omics.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_omics.types.create_variant_store_request.CreateVariantStoreRequest]",
        ) -> AsyncOperationResponse[
            "capo_omics.types.create_variant_store_response.CreateVariantStoreResponse"
        ]:
            import capo_omics._operations.omics.create_variant_store

            (
                output,
                http_response,
            ) = await capo_omics._operations.omics.create_variant_store.async_create_variant_store(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_omics.types.create_variant_store_request.CreateVariantStoreRequest = {
            "reference": reference
        }
        if name is not None:
            input_["name"] = name
        if description is not None:
            input_["description"] = description
        if tags is not None:
            input_["tags"] = tags
        if sse_config is not None:
            input_["sse_config"] = sse_config

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_variant_store(
        self, name: str, *, config_overrides: Optional[AsyncOmicsClientConfig] = None
    ) -> "capo_omics.types.get_variant_store_response.GetVariantStoreResponse":
        """<important> <p>Amazon Web Services HealthOmics variant stores and annotation stores are no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see <a href="https://docs.aws.amazon.com/omics/latest/dev/variant-store-availability-change.html"> Amazon Web Services HealthOmics variant store and annotation store availability change</a>.</p> </important> <p>Gets information about a variant store.</p>

        Args:
            name: <p>The store's name.</p>

        Raises:
            capo_omics.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_omics.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred. Try the request again.</p>
            capo_omics.errors.resource_not_found_exception.ResourceNotFoundException: <p>The target resource was not found in the current Region.</p>
            capo_omics.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_omics.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_omics.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_omics.types.get_variant_store_request.GetVariantStoreRequest]",
        ) -> AsyncOperationResponse[
            "capo_omics.types.get_variant_store_response.GetVariantStoreResponse"
        ]:
            import capo_omics._operations.omics.get_variant_store

            (
                output,
                http_response,
            ) = await capo_omics._operations.omics.get_variant_store.async_get_variant_store(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_omics.types.get_variant_store_request.GetVariantStoreRequest = {
            "name": name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_variant_store(
        self,
        name: str,
        *,
        config_overrides: Optional[AsyncOmicsClientConfig] = None,
        description: Optional["capo_omics.types.description.Description"] = None,
    ) -> "capo_omics.types.update_variant_store_response.UpdateVariantStoreResponse":
        """<important> <p>Amazon Web Services HealthOmics variant stores and annotation stores are no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see <a href="https://docs.aws.amazon.com/omics/latest/dev/variant-store-availability-change.html"> Amazon Web Services HealthOmics variant store and annotation store availability change</a>.</p> </important> <p>Updates a variant store.</p>

        Args:
            name: <p>A name for the store.</p>
            description: <p>A description for the store.</p>

        Raises:
            capo_omics.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_omics.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred. Try the request again.</p>
            capo_omics.errors.resource_not_found_exception.ResourceNotFoundException: <p>The target resource was not found in the current Region.</p>
            capo_omics.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_omics.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_omics.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_omics.types.update_variant_store_request.UpdateVariantStoreRequest]",
        ) -> AsyncOperationResponse[
            "capo_omics.types.update_variant_store_response.UpdateVariantStoreResponse"
        ]:
            import capo_omics._operations.omics.update_variant_store

            (
                output,
                http_response,
            ) = await capo_omics._operations.omics.update_variant_store.async_update_variant_store(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_omics.types.update_variant_store_request.UpdateVariantStoreRequest = {
            "name": name
        }
        if description is not None:
            input_["description"] = description

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_variant_store(
        self,
        name: str,
        *,
        config_overrides: Optional[AsyncOmicsClientConfig] = None,
        force: Optional[bool] = None,
    ) -> "capo_omics.types.delete_variant_store_response.DeleteVariantStoreResponse":
        """<important> <p>Amazon Web Services HealthOmics variant stores and annotation stores are no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see <a href="https://docs.aws.amazon.com/omics/latest/dev/variant-store-availability-change.html"> Amazon Web Services HealthOmics variant store and annotation store availability change</a>.</p> </important> <p>Deletes a variant store.</p>

        Args:
            name: <p>The store's name.</p>
            force: <p>Whether to force deletion.</p>

        Raises:
            capo_omics.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_omics.errors.conflict_exception.ConflictException: <p>The request cannot be applied to the target resource in its current state.</p>
            capo_omics.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred. Try the request again.</p>
            capo_omics.errors.resource_not_found_exception.ResourceNotFoundException: <p>The target resource was not found in the current Region.</p>
            capo_omics.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_omics.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_omics.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_omics.types.delete_variant_store_request.DeleteVariantStoreRequest]",
        ) -> AsyncOperationResponse[
            "capo_omics.types.delete_variant_store_response.DeleteVariantStoreResponse"
        ]:
            import capo_omics._operations.omics.delete_variant_store

            (
                output,
                http_response,
            ) = await capo_omics._operations.omics.delete_variant_store.async_delete_variant_store(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_omics.types.delete_variant_store_request.DeleteVariantStoreRequest = {
            "name": name
        }
        if force is not None:
            input_["force"] = force

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_variant_stores(
        self,
        *,
        config_overrides: Optional[AsyncOmicsClientConfig] = None,
        max_results: Optional[int] = None,
        ids: Optional["capo_omics.types.id_list.IdList"] = None,
        next_token: Optional[str] = None,
        filter: Optional[
            "capo_omics.types.list_variant_stores_filter.ListVariantStoresFilter"
        ] = None,
    ) -> "capo_omics.types.list_variant_stores_response.ListVariantStoresResponse":
        """<important> <p>Amazon Web Services HealthOmics variant stores and annotation stores are no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see <a href="https://docs.aws.amazon.com/omics/latest/dev/variant-store-availability-change.html"> Amazon Web Services HealthOmics variant store and annotation store availability change</a>.</p> </important> <p>Retrieves a list of variant stores.</p>

        Args:
            max_results: <p>The maximum number of stores to return in one page of results.</p>
            ids: <p>A list of store IDs.</p>
            next_token: <p>Specify the pagination token from a previous request to retrieve the next page of results.</p>
            filter: <p>A filter to apply to the list.</p>

        Raises:
            capo_omics.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_omics.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred. Try the request again.</p>
            capo_omics.errors.resource_not_found_exception.ResourceNotFoundException: <p>The target resource was not found in the current Region.</p>
            capo_omics.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_omics.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_omics.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_omics.types.list_variant_stores_request.ListVariantStoresRequest]",
        ) -> AsyncOperationResponse[
            "capo_omics.types.list_variant_stores_response.ListVariantStoresResponse"
        ]:
            import capo_omics._operations.omics.list_variant_stores

            (
                output,
                http_response,
            ) = await capo_omics._operations.omics.list_variant_stores.async_list_variant_stores(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_omics.types.list_variant_stores_request.ListVariantStoresRequest = {}
        if max_results is not None:
            input_["max_results"] = max_results
        if ids is not None:
            input_["ids"] = ids
        if next_token is not None:
            input_["next_token"] = next_token
        if filter is not None:
            input_["filter"] = filter

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_variant_stores(
        self,
        *,
        config_overrides: Optional[AsyncOmicsClientConfig] = None,
        max_results: Optional[int] = None,
        ids: Optional["capo_omics.types.id_list.IdList"] = None,
        next_token: Optional[str] = None,
        filter: Optional[
            "capo_omics.types.list_variant_stores_filter.ListVariantStoresFilter"
        ] = None,
    ) -> "AsyncIterator[capo_omics.types.variant_store_item.VariantStoreItem]":
        _token = next_token
        while True:
            _response = await self.list_variant_stores(
                config_overrides=config_overrides,
                max_results=max_results,
                ids=ids,
                next_token=_token,
                filter=filter,
            )
            _page = _resolve_path(_response, ("variant_stores",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def create_workflow(
        self,
        request_id: "capo_omics.types.workflow_request_id.WorkflowRequestId",
        *,
        config_overrides: Optional[AsyncOmicsClientConfig] = None,
        name: Optional["capo_omics.types.workflow_name.WorkflowName"] = None,
        description: Optional[
            "capo_omics.types.workflow_description.WorkflowDescription"
        ] = None,
        engine: Optional["capo_omics.types.workflow_engine.WorkflowEngine"] = None,
        definition_zip: Optional[bytes] = None,
        definition_uri: Optional[
            "capo_omics.types.workflow_definition.WorkflowDefinition"
        ] = None,
        main: Optional["capo_omics.types.workflow_main.WorkflowMain"] = None,
        parameter_template: Optional[
            "capo_omics.types.workflow_parameter_template.WorkflowParameterTemplate"
        ] = None,
        storage_capacity: Optional[int] = None,
        tags: Optional["capo_omics.types.tag_map.TagMap"] = None,
        accelerators: Optional["capo_omics.types.accelerators.Accelerators"] = None,
        storage_type: Optional["capo_omics.types.storage_type.StorageType"] = None,
        container_registry_map: Optional[
            "capo_omics.types.container_registry_map.ContainerRegistryMap"
        ] = None,
        container_registry_map_uri: Optional["capo_omics.types.uri.Uri"] = None,
        readme_markdown: Optional[
            "capo_omics.types.readme_markdown.ReadmeMarkdown"
        ] = None,
        parameter_template_path: Optional[
            "capo_omics.types.parameter_template_path.ParameterTemplatePath"
        ] = None,
        readme_path: Optional["capo_omics.types.readme_path.ReadmePath"] = None,
        definition_repository: Optional[
            "capo_omics.types.definition_repository.DefinitionRepository"
        ] = None,
        workflow_bucket_owner_id: Optional[
            "capo_omics.types.workflow_bucket_owner_id.WorkflowBucketOwnerId"
        ] = None,
        readme_uri: Optional[
            "capo_omics.types.s3_uri_for_object.S3UriForObject"
        ] = None,
    ) -> "capo_omics.types.create_workflow_response.CreateWorkflowResponse":
        """<p>Creates a private workflow. Before you create a private workflow, you must create and configure these required resources:</p> <ul> <li> <p> <i>Workflow definition file:</i> A workflow definition file written in WDL, Nextflow, or CWL. The workflow definition specifies the inputs and outputs for runs that use the workflow. It also includes specifications for the runs and run tasks for your workflow, including compute and memory requirements. The workflow definition file must be in <code>.zip</code> format. For more information, see <a href="https://docs.aws.amazon.com/omics/latest/dev/workflow-definition-files.html">Workflow definition files</a> in Amazon Web Services HealthOmics.</p> <ul> <li> <p>You can use Amazon Q CLI to build and validate your workflow definition files in WDL, Nextflow, and CWL. For more information, see <a href="https://docs.aws.amazon.com/omics/latest/dev/getting-started.html#omics-q-prompts">Example prompts for Amazon Q CLI</a> and the <a href="https://github.com/aws-samples/aws-healthomics-tutorials/tree/main/generative-ai">Amazon Web Services HealthOmics Agentic generative AI tutorial</a> on GitHub.</p> </li> </ul> </li> <li> <p> <i>(Optional) Parameter template file:</i> A parameter template file written in JSON. Create the file to define the run parameters, or Amazon Web Services HealthOmics generates the parameter template for you. For more information, see <a href="https://docs.aws.amazon.com/omics/latest/dev/parameter-templates.html">Parameter template files for HealthOmics workflows</a>. </p> </li> <li> <p> <i>ECR container images:</i> Create container images for the workflow in a private ECR repository, or synchronize images from a supported upstream registry with your Amazon ECR private repository.</p> </li> <li> <p> <i>(Optional) Sentieon licenses:</i> Request a Sentieon license to use the Sentieon software in private workflows.</p> </li> </ul> <p>For more information, see <a href="https://docs.aws.amazon.com/omics/latest/dev/creating-private-workflows.html">Creating or updating a private workflow in Amazon Web Services HealthOmics</a> in the <i>Amazon Web Services HealthOmics User Guide</i>.</p>

        Args:
            name: <p>Name (optional but highly recommended) for the workflow to locate relevant information in the CloudWatch logs and Amazon Web Services HealthOmics console. </p>
            description: <p>A description for the workflow.</p>
            engine: <p>The workflow engine for the workflow. By default, Amazon Web Services HealthOmics detects the engine automatically from your workflow definition. Provide a value if you have workflow definition files from more than one engine in your zip file, or to use WDL lenient.</p> <p>WDL lenient is designed to handle workflows migrated from Cromwell. It supports customer Cromwell directives and some non-conformant logic. For details, see <a href="https://docs.aws.amazon.com/omics/latest/dev/workflow-wdl-type-conversion.html">Implicit type conversion in WDL lenient</a> in the <i>Amazon Web Services HealthOmics User Guide</i>.</p>
            definition_zip: <p>A ZIP archive containing the main workflow definition file and dependencies that it imports for the workflow. You can use a file with a ://fileb prefix instead of the Base64 string. For more information, see <a href="https://docs.aws.amazon.com/omics/latest/dev/workflow-defn-requirements.html">Workflow definition requirements</a> in the <i>Amazon Web Services HealthOmics User Guide</i>.</p>
            definition_uri: <p>The S3 URI of a definition for the workflow. The S3 bucket must be in the same region as the workflow.</p>
            main: <p>The path of the main definition file for the workflow. This parameter is not required if the ZIP archive contains only one workflow definition file, or if the main definition file is named “main”. An example path is: <code>workflow-definition/main-file.wdl</code>. </p>
            parameter_template: <p>A parameter template for the workflow. If this field is blank, Amazon Web Services HealthOmics will automatically parse the parameter template values from your workflow definition file. To override these service generated default values, provide a parameter template. To view an example of a parameter template, see <a href="https://docs.aws.amazon.com/omics/latest/dev/parameter-templates.html">Parameter template files</a> in the <i>Amazon Web Services HealthOmics User Guide</i>.</p>
            storage_capacity: <p>The default static storage capacity (in gibibytes) for runs that use this workflow or workflow version. The <code>storageCapacity</code> can be overwritten at run time. The storage capacity is not required for runs with a <code>DYNAMIC</code> storage type.</p>
            tags: <p>Tags for the workflow. You can define up to 50 tags for the workflow. For more information, see <a href="https://docs.aws.amazon.com/omics/latest/dev/add-a-tag.html">Adding a tag</a> in the <i>Amazon Web Services HealthOmics User Guide</i>.</p>
            request_id: <p>An idempotency token to ensure that duplicate workflows are not created when Amazon Web Services HealthOmics submits retry requests.</p>
            accelerators: <p>The computational accelerator specified to run the workflow.</p>
            storage_type: <p>The default storage type for runs that use this workflow. The <code>storageType</code> can be overridden at run time. <code>DYNAMIC</code> storage dynamically scales the storage up or down, based on file system utilization. <code>STATIC</code> storage allocates a fixed amount of storage. For more information about dynamic and static storage types, see <a href="https://docs.aws.amazon.com/omics/latest/dev/workflows-run-types.html">Run storage types</a> in the <i>Amazon Web Services HealthOmics User Guide</i>.</p>
            container_registry_map: <p>(Optional) Use a container registry map to specify mappings between the ECR private repository and one or more upstream registries. For more information, see <a href="https://docs.aws.amazon.com/omics/latest/dev/workflows-ecr.html">Container images</a> in the <i>Amazon Web Services HealthOmics User Guide</i>.</p>
            container_registry_map_uri: <p>(Optional) URI of the S3 location for the registry mapping file.</p>
            readme_markdown: <p>The markdown content for the workflow's README file. This provides documentation and usage information for users of the workflow.</p>
            parameter_template_path: <p>The path to the workflow parameter template JSON file within the repository. This file defines the input parameters for runs that use this workflow. If not specified, the workflow will be created without a parameter template.</p>
            readme_path: <p>The path to the workflow README markdown file within the repository. This file provides documentation and usage information for the workflow. If not specified, the <code>README.md</code> file from the root directory of the repository will be used.</p>
            definition_repository: <p>The repository information for the workflow definition. This allows you to source your workflow definition directly from a code repository.</p>
            workflow_bucket_owner_id: <p>The Amazon Web Services account ID of the expected owner of the S3 bucket that contains the workflow definition. If not specified, the service skips the validation.</p>
            readme_uri: <p>The S3 URI of the README file for the workflow. This file provides documentation and usage information for the workflow. Requirements include:</p> <ul> <li> <p>The S3 URI must begin with <code>s3://USER-OWNED-BUCKET/</code> </p> </li> <li> <p>The requester must have access to the S3 bucket and object.</p> </li> <li> <p>The max README content length is 500 KiB.</p> </li> </ul>

        Raises:
            capo_omics.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_omics.errors.conflict_exception.ConflictException: <p>The request cannot be applied to the target resource in its current state.</p>
            capo_omics.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred. Try the request again.</p>
            capo_omics.errors.request_timeout_exception.RequestTimeoutException: <p>The request timed out.</p>
            capo_omics.errors.resource_not_found_exception.ResourceNotFoundException: <p>The target resource was not found in the current Region.</p>
            capo_omics.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request exceeds a service quota.</p>
            capo_omics.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_omics.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_omics.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_omics.types.create_workflow_request.CreateWorkflowRequest]",
        ) -> AsyncOperationResponse[
            "capo_omics.types.create_workflow_response.CreateWorkflowResponse"
        ]:
            import capo_omics._operations.omics.create_workflow

            (
                output,
                http_response,
            ) = await capo_omics._operations.omics.create_workflow.async_create_workflow(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_omics.types.create_workflow_request.CreateWorkflowRequest = {
            "request_id": request_id
        }
        if name is not None:
            input_["name"] = name
        if description is not None:
            input_["description"] = description
        if engine is not None:
            input_["engine"] = engine
        if definition_zip is not None:
            input_["definition_zip"] = definition_zip
        if definition_uri is not None:
            input_["definition_uri"] = definition_uri
        if main is not None:
            input_["main"] = main
        if parameter_template is not None:
            input_["parameter_template"] = parameter_template
        if storage_capacity is not None:
            input_["storage_capacity"] = storage_capacity
        if tags is not None:
            input_["tags"] = tags
        if accelerators is not None:
            input_["accelerators"] = accelerators
        if storage_type is not None:
            input_["storage_type"] = storage_type
        if container_registry_map is not None:
            input_["container_registry_map"] = container_registry_map
        if container_registry_map_uri is not None:
            input_["container_registry_map_uri"] = container_registry_map_uri
        if readme_markdown is not None:
            input_["readme_markdown"] = readme_markdown
        if parameter_template_path is not None:
            input_["parameter_template_path"] = parameter_template_path
        if readme_path is not None:
            input_["readme_path"] = readme_path
        if definition_repository is not None:
            input_["definition_repository"] = definition_repository
        if workflow_bucket_owner_id is not None:
            input_["workflow_bucket_owner_id"] = workflow_bucket_owner_id
        if readme_uri is not None:
            input_["readme_uri"] = readme_uri

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_workflow(
        self,
        id: "capo_omics.types.workflow_id.WorkflowId",
        *,
        config_overrides: Optional[AsyncOmicsClientConfig] = None,
        type: Optional["capo_omics.types.workflow_type.WorkflowType"] = None,
        export: Optional[
            "capo_omics.types.workflow_export_list.WorkflowExportList"
        ] = None,
        workflow_owner_id: Optional[
            "capo_omics.types.workflow_owner_id.WorkflowOwnerId"
        ] = None,
    ) -> "capo_omics.types.get_workflow_response.GetWorkflowResponse":
        """<p>Gets all information about a workflow using its ID.</p> <p>If a workflow is shared with you, you cannot export the workflow.</p> <p>For more information about your workflow status, see <a href="https://docs.aws.amazon.com/omics/latest/dev/using-get-workflow.html">Verify the workflow status</a> in the <i>Amazon Web Services HealthOmics User Guide</i>.</p>

        Args:
            id: <p>The workflow's ID.</p>
            type: <p>The workflow's type.</p>
            export: <p>The export format for the workflow.</p>
            workflow_owner_id: <p>The ID of the workflow owner.</p>

        Raises:
            capo_omics.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_omics.errors.conflict_exception.ConflictException: <p>The request cannot be applied to the target resource in its current state.</p>
            capo_omics.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred. Try the request again.</p>
            capo_omics.errors.request_timeout_exception.RequestTimeoutException: <p>The request timed out.</p>
            capo_omics.errors.resource_not_found_exception.ResourceNotFoundException: <p>The target resource was not found in the current Region.</p>
            capo_omics.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request exceeds a service quota.</p>
            capo_omics.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_omics.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_omics.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_omics.types.get_workflow_request.GetWorkflowRequest]",
        ) -> AsyncOperationResponse[
            "capo_omics.types.get_workflow_response.GetWorkflowResponse"
        ]:
            import capo_omics._operations.omics.get_workflow

            (
                output,
                http_response,
            ) = await capo_omics._operations.omics.get_workflow.async_get_workflow(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_omics.types.get_workflow_request.GetWorkflowRequest = {"id": id}
        if type is not None:
            input_["type"] = type
        if export is not None:
            input_["export"] = export
        if workflow_owner_id is not None:
            input_["workflow_owner_id"] = workflow_owner_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_workflow(
        self,
        id: "capo_omics.types.workflow_id.WorkflowId",
        *,
        config_overrides: Optional[AsyncOmicsClientConfig] = None,
        name: Optional["capo_omics.types.workflow_name.WorkflowName"] = None,
        description: Optional[
            "capo_omics.types.workflow_description.WorkflowDescription"
        ] = None,
        storage_type: Optional["capo_omics.types.storage_type.StorageType"] = None,
        storage_capacity: Optional[int] = None,
        readme_markdown: Optional[
            "capo_omics.types.readme_markdown.ReadmeMarkdown"
        ] = None,
    ) -> None:
        """<p>Updates information about a workflow.</p> <p>You can update the following workflow information:</p> <ul> <li> <p>Name</p> </li> <li> <p>Description</p> </li> <li> <p>Default storage type</p> </li> <li> <p>Default storage capacity (with workflow ID)</p> </li> </ul> <p>This operation returns a response with no body if the operation is successful. You can check the workflow updates by calling the <code>GetWorkflow</code> API operation.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/omics/latest/dev/update-private-workflow.html">Update a private workflow</a> in the <i>Amazon Web Services HealthOmics User Guide</i>.</p>

        Args:
            id: <p>The workflow's ID.</p>
            name: <p>A name for the workflow.</p>
            description: <p>A description for the workflow.</p>
            storage_type: <p>The default storage type for runs that use this workflow. STATIC storage allocates a fixed amount of storage. DYNAMIC storage dynamically scales the storage up or down, based on file system utilization. For more information about static and dynamic storage, see <a href="https://docs.aws.amazon.com/omics/latest/dev/Using-workflows.html">Running workflows</a> in the <i>Amazon Web Services HealthOmics User Guide</i>. </p>
            storage_capacity: <p>The default static storage capacity (in gibibytes) for runs that use this workflow or workflow version. </p>
            readme_markdown: <p>The markdown content for the workflow's README file. This provides documentation and usage information for users of the workflow.</p>

        Raises:
            capo_omics.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_omics.errors.conflict_exception.ConflictException: <p>The request cannot be applied to the target resource in its current state.</p>
            capo_omics.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred. Try the request again.</p>
            capo_omics.errors.request_timeout_exception.RequestTimeoutException: <p>The request timed out.</p>
            capo_omics.errors.resource_not_found_exception.ResourceNotFoundException: <p>The target resource was not found in the current Region.</p>
            capo_omics.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request exceeds a service quota.</p>
            capo_omics.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_omics.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_omics.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_omics.types.update_workflow_request.UpdateWorkflowRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_omics._operations.omics.update_workflow

            (
                output,
                http_response,
            ) = await capo_omics._operations.omics.update_workflow.async_update_workflow(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_omics.types.update_workflow_request.UpdateWorkflowRequest = {
            "id": id
        }
        if name is not None:
            input_["name"] = name
        if description is not None:
            input_["description"] = description
        if storage_type is not None:
            input_["storage_type"] = storage_type
        if storage_capacity is not None:
            input_["storage_capacity"] = storage_capacity
        if readme_markdown is not None:
            input_["readme_markdown"] = readme_markdown

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_workflow(
        self,
        id: "capo_omics.types.workflow_id.WorkflowId",
        *,
        config_overrides: Optional[AsyncOmicsClientConfig] = None,
    ) -> None:
        """<p>Deletes a workflow by specifying its ID. This operation returns a response with no body if the deletion is successful.</p> <p>To verify that the workflow is deleted:</p> <ul> <li> <p>Use <code>ListWorkflows</code> to confirm the workflow no longer appears in the list.</p> </li> <li> <p>Use <code>GetWorkflow</code> to verify the workflow cannot be found.</p> </li> </ul>

        Args:
            id: <p>The workflow's ID.</p>

        Raises:
            capo_omics.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_omics.errors.conflict_exception.ConflictException: <p>The request cannot be applied to the target resource in its current state.</p>
            capo_omics.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred. Try the request again.</p>
            capo_omics.errors.request_timeout_exception.RequestTimeoutException: <p>The request timed out.</p>
            capo_omics.errors.resource_not_found_exception.ResourceNotFoundException: <p>The target resource was not found in the current Region.</p>
            capo_omics.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request exceeds a service quota.</p>
            capo_omics.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_omics.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_omics.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_omics.types.delete_workflow_request.DeleteWorkflowRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_omics._operations.omics.delete_workflow

            (
                output,
                http_response,
            ) = await capo_omics._operations.omics.delete_workflow.async_delete_workflow(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_omics.types.delete_workflow_request.DeleteWorkflowRequest = {
            "id": id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_workflows(
        self,
        *,
        config_overrides: Optional[AsyncOmicsClientConfig] = None,
        type: Optional["capo_omics.types.workflow_type.WorkflowType"] = None,
        name: Optional["capo_omics.types.workflow_name.WorkflowName"] = None,
        starting_token: Optional[
            "capo_omics.types.workflow_list_token.WorkflowListToken"
        ] = None,
        max_results: Optional[int] = None,
    ) -> "capo_omics.types.list_workflows_response.ListWorkflowsResponse":
        """<p>Retrieves a list of existing workflows. You can filter for specific workflows by their name and type. Using the type parameter, specify <code>PRIVATE</code> to retrieve a list of private workflows or specify <code>READY2RUN</code> for a list of all Ready2Run workflows. If you do not specify the type of workflow, this operation returns a list of existing workflows.</p>

        Args:
            type: <p>Filter the list by workflow type.</p>
            name: <p>Filter the list by workflow name.</p>
            starting_token: <p>Specify the pagination token from a previous request to retrieve the next page of results.</p>
            max_results: <p>The maximum number of workflows to return in one page of results.</p>

        Raises:
            capo_omics.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_omics.errors.conflict_exception.ConflictException: <p>The request cannot be applied to the target resource in its current state.</p>
            capo_omics.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred. Try the request again.</p>
            capo_omics.errors.request_timeout_exception.RequestTimeoutException: <p>The request timed out.</p>
            capo_omics.errors.resource_not_found_exception.ResourceNotFoundException: <p>The target resource was not found in the current Region.</p>
            capo_omics.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request exceeds a service quota.</p>
            capo_omics.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_omics.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_omics.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_omics.types.list_workflows_request.ListWorkflowsRequest]",
        ) -> AsyncOperationResponse[
            "capo_omics.types.list_workflows_response.ListWorkflowsResponse"
        ]:
            import capo_omics._operations.omics.list_workflows

            (
                output,
                http_response,
            ) = await capo_omics._operations.omics.list_workflows.async_list_workflows(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_omics.types.list_workflows_request.ListWorkflowsRequest = {}
        if type is not None:
            input_["type"] = type
        if name is not None:
            input_["name"] = name
        if starting_token is not None:
            input_["starting_token"] = starting_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_workflows(
        self,
        *,
        config_overrides: Optional[AsyncOmicsClientConfig] = None,
        type: Optional["capo_omics.types.workflow_type.WorkflowType"] = None,
        name: Optional["capo_omics.types.workflow_name.WorkflowName"] = None,
        starting_token: Optional[
            "capo_omics.types.workflow_list_token.WorkflowListToken"
        ] = None,
        max_results: Optional[int] = None,
    ) -> "AsyncIterator[capo_omics.types.workflow_list_item.WorkflowListItem]":
        _token = starting_token
        while True:
            _response = await self.list_workflows(
                config_overrides=config_overrides,
                type=type,
                name=name,
                starting_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def create_workflow_version(
        self,
        workflow_id: "capo_omics.types.workflow_id.WorkflowId",
        version_name: "capo_omics.types.workflow_version_name.WorkflowVersionName",
        request_id: "capo_omics.types.workflow_request_id.WorkflowRequestId",
        *,
        config_overrides: Optional[AsyncOmicsClientConfig] = None,
        definition_zip: Optional[bytes] = None,
        definition_uri: Optional[
            "capo_omics.types.workflow_definition.WorkflowDefinition"
        ] = None,
        accelerators: Optional["capo_omics.types.accelerators.Accelerators"] = None,
        description: Optional[
            "capo_omics.types.workflow_version_description.WorkflowVersionDescription"
        ] = None,
        engine: Optional["capo_omics.types.workflow_engine.WorkflowEngine"] = None,
        main: Optional["capo_omics.types.workflow_main.WorkflowMain"] = None,
        parameter_template: Optional[
            "capo_omics.types.workflow_parameter_template.WorkflowParameterTemplate"
        ] = None,
        storage_type: Optional["capo_omics.types.storage_type.StorageType"] = None,
        storage_capacity: Optional[int] = None,
        tags: Optional["capo_omics.types.tag_map.TagMap"] = None,
        workflow_bucket_owner_id: Optional[
            "capo_omics.types.workflow_bucket_owner_id.WorkflowBucketOwnerId"
        ] = None,
        container_registry_map: Optional[
            "capo_omics.types.container_registry_map.ContainerRegistryMap"
        ] = None,
        container_registry_map_uri: Optional["capo_omics.types.uri.Uri"] = None,
        readme_markdown: Optional[
            "capo_omics.types.readme_markdown.ReadmeMarkdown"
        ] = None,
        parameter_template_path: Optional[
            "capo_omics.types.parameter_template_path.ParameterTemplatePath"
        ] = None,
        readme_path: Optional["capo_omics.types.readme_path.ReadmePath"] = None,
        definition_repository: Optional[
            "capo_omics.types.definition_repository.DefinitionRepository"
        ] = None,
        readme_uri: Optional[
            "capo_omics.types.s3_uri_for_object.S3UriForObject"
        ] = None,
    ) -> "capo_omics.types.create_workflow_version_response.CreateWorkflowVersionResponse":
        """<p>Creates a new workflow version for the workflow that you specify with the <code>workflowId</code> parameter.</p> <p>When you create a new version of a workflow, you need to specify the configuration for the new version. It doesn't inherit any configuration values from the workflow.</p> <p>Provide a version name that is unique for this workflow. You cannot change the name after HealthOmics creates the version.</p> <note> <p>Don't include any personally identifiable information (PII) in the version name. Version names appear in the workflow version ARN.</p> </note> <p>For more information, see <a href="https://docs.aws.amazon.com/omics/latest/dev/workflow-versions.html">Workflow versioning in Amazon Web Services HealthOmics</a> in the <i>Amazon Web Services HealthOmics User Guide</i>.</p>

        Args:
            workflow_id: <p>The ID of the workflow where you are creating the new version. The <code>workflowId</code> is not the UUID.</p>
            version_name: <p>A name for the workflow version. Provide a version name that is unique for this workflow. You cannot change the name after HealthOmics creates the version. </p> <p>The version name must start with a letter or number and it can include upper-case and lower-case letters, numbers, hyphens, periods and underscores. The maximum length is 64 characters. You can use a simple naming scheme, such as version1, version2, version3. You can also match your workflow versions with your own internal versioning conventions, such as 2.7.0, 2.7.1, 2.7.2.</p>
            definition_zip: <p>A ZIP archive containing the main workflow definition file and dependencies that it imports for this workflow version. You can use a file with a ://fileb prefix instead of the Base64 string. For more information, see Workflow definition requirements in the <i>Amazon Web Services HealthOmics User Guide</i>.</p>
            definition_uri: <p>The S3 URI of a definition for this workflow version. The S3 bucket must be in the same region as this workflow version.</p>
            accelerators: <p>The computational accelerator for this workflow version.</p>
            description: <p>A description for this workflow version.</p>
            engine: <p>The workflow engine for this workflow version. This is only required if you have workflow definition files from more than one engine in your zip file. Otherwise, the service can detect the engine automatically from your workflow definition.</p>
            main: <p>The path of the main definition file for this workflow version. This parameter is not required if the ZIP archive contains only one workflow definition file, or if the main definition file is named “main”. An example path is: <code>workflow-definition/main-file.wdl</code>. </p>
            parameter_template: <p>A parameter template for this workflow version. If this field is blank, Amazon Web Services HealthOmics will automatically parse the parameter template values from your workflow definition file. To override these service generated default values, provide a parameter template. To view an example of a parameter template, see <a href="https://docs.aws.amazon.com/omics/latest/dev/parameter-templates.html">Parameter template files</a> in the <i>Amazon Web Services HealthOmics User Guide</i>.</p>
            request_id: <p>An idempotency token to ensure that duplicate workflows are not created when Amazon Web Services HealthOmics submits retry requests.</p>
            storage_type: <p>The default storage type for runs that use this workflow version. The <code>storageType</code> can be overridden at run time. <code>DYNAMIC</code> storage dynamically scales the storage up or down, based on file system utilization. STATIC storage allocates a fixed amount of storage. For more information about dynamic and static storage types, see <a href="https://docs.aws.amazon.com/omics/latest/dev/workflows-run-types.html">Run storage types</a> in the <i>Amazon Web Services HealthOmics User Guide</i>.</p>
            storage_capacity: <p>The default static storage capacity (in gibibytes) for runs that use this workflow version. The <code>storageCapacity</code> can be overwritten at run time. The storage capacity is not required for runs with a <code>DYNAMIC</code> storage type.</p>
            tags: <p>Tags for this workflow version. You can define up to 50 tags for the workflow. For more information, see <a href="https://docs.aws.amazon.com/omics/latest/dev/add-a-tag.html">Adding a tag</a> in the <i>Amazon Web Services HealthOmics User Guide</i>.</p>
            workflow_bucket_owner_id: <p>Amazon Web Services Id of the owner of the S3 bucket that contains the workflow definition. You need to specify this parameter if your account is not the bucket owner.</p>
            container_registry_map: <p>(Optional) Use a container registry map to specify mappings between the ECR private repository and one or more upstream registries. For more information, see <a href="https://docs.aws.amazon.com/omics/latest/dev/workflows-ecr.html">Container images</a> in the <i>Amazon Web Services HealthOmics User Guide</i>.</p>
            container_registry_map_uri: <p>(Optional) URI of the S3 location for the registry mapping file.</p>
            readme_markdown: <p>The markdown content for the workflow version's README file. This provides documentation and usage information for users of this specific workflow version.</p>
            parameter_template_path: <p>The path to the workflow version parameter template JSON file within the repository. This file defines the input parameters for runs that use this workflow version. If not specified, the workflow version will be created without a parameter template.</p>
            readme_path: <p>The path to the workflow version README markdown file within the repository. This file provides documentation and usage information for the workflow. If not specified, the <code>README.md</code> file from the root directory of the repository will be used.</p>
            definition_repository: <p>The repository information for the workflow version definition. This allows you to source your workflow version definition directly from a code repository.</p>
            readme_uri: <p>The S3 URI of the README file for the workflow version. This file provides documentation and usage information for the workflow version. Requirements include:</p> <ul> <li> <p>The S3 URI must begin with <code>s3://USER-OWNED-BUCKET/</code> </p> </li> <li> <p>The requester must have access to the S3 bucket and object.</p> </li> <li> <p>The max README content length is 500 KiB.</p> </li> </ul>

        Raises:
            capo_omics.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_omics.errors.conflict_exception.ConflictException: <p>The request cannot be applied to the target resource in its current state.</p>
            capo_omics.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred. Try the request again.</p>
            capo_omics.errors.request_timeout_exception.RequestTimeoutException: <p>The request timed out.</p>
            capo_omics.errors.resource_not_found_exception.ResourceNotFoundException: <p>The target resource was not found in the current Region.</p>
            capo_omics.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request exceeds a service quota.</p>
            capo_omics.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_omics.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_omics.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_omics.types.create_workflow_version_request.CreateWorkflowVersionRequest]",
        ) -> AsyncOperationResponse[
            "capo_omics.types.create_workflow_version_response.CreateWorkflowVersionResponse"
        ]:
            import capo_omics._operations.omics.create_workflow_version

            (
                output,
                http_response,
            ) = await capo_omics._operations.omics.create_workflow_version.async_create_workflow_version(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_omics.types.create_workflow_version_request.CreateWorkflowVersionRequest = {
            "workflow_id": workflow_id,
            "version_name": version_name,
            "request_id": request_id,
        }
        if definition_zip is not None:
            input_["definition_zip"] = definition_zip
        if definition_uri is not None:
            input_["definition_uri"] = definition_uri
        if accelerators is not None:
            input_["accelerators"] = accelerators
        if description is not None:
            input_["description"] = description
        if engine is not None:
            input_["engine"] = engine
        if main is not None:
            input_["main"] = main
        if parameter_template is not None:
            input_["parameter_template"] = parameter_template
        if storage_type is not None:
            input_["storage_type"] = storage_type
        if storage_capacity is not None:
            input_["storage_capacity"] = storage_capacity
        if tags is not None:
            input_["tags"] = tags
        if workflow_bucket_owner_id is not None:
            input_["workflow_bucket_owner_id"] = workflow_bucket_owner_id
        if container_registry_map is not None:
            input_["container_registry_map"] = container_registry_map
        if container_registry_map_uri is not None:
            input_["container_registry_map_uri"] = container_registry_map_uri
        if readme_markdown is not None:
            input_["readme_markdown"] = readme_markdown
        if parameter_template_path is not None:
            input_["parameter_template_path"] = parameter_template_path
        if readme_path is not None:
            input_["readme_path"] = readme_path
        if definition_repository is not None:
            input_["definition_repository"] = definition_repository
        if readme_uri is not None:
            input_["readme_uri"] = readme_uri

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_workflow_version(
        self,
        workflow_id: "capo_omics.types.workflow_id.WorkflowId",
        version_name: "capo_omics.types.workflow_version_name.WorkflowVersionName",
        *,
        config_overrides: Optional[AsyncOmicsClientConfig] = None,
        type: Optional["capo_omics.types.workflow_type.WorkflowType"] = None,
        export: Optional[
            "capo_omics.types.workflow_export_list.WorkflowExportList"
        ] = None,
        workflow_owner_id: Optional[
            "capo_omics.types.workflow_owner_id.WorkflowOwnerId"
        ] = None,
    ) -> "capo_omics.types.get_workflow_version_response.GetWorkflowVersionResponse":
        """<p>Gets information about a workflow version. For more information, see <a href="https://docs.aws.amazon.com/omics/latest/dev/workflow-versions.html">Workflow versioning in Amazon Web Services HealthOmics</a> in the <i>Amazon Web Services HealthOmics User Guide</i>.</p>

        Args:
            workflow_id: <p>The workflow's ID. The <code>workflowId</code> is not the UUID.</p>
            version_name: <p>The workflow version name.</p>
            type: <p>The workflow's type. </p>
            export: <p>The export format for the workflow.</p>
            workflow_owner_id: <p>The 12-digit account ID of the workflow owner. The workflow owner ID can be retrieved using the <code>GetShare</code> API operation. If you are the workflow owner, you do not need to include this ID.</p>

        Raises:
            capo_omics.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_omics.errors.conflict_exception.ConflictException: <p>The request cannot be applied to the target resource in its current state.</p>
            capo_omics.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred. Try the request again.</p>
            capo_omics.errors.request_timeout_exception.RequestTimeoutException: <p>The request timed out.</p>
            capo_omics.errors.resource_not_found_exception.ResourceNotFoundException: <p>The target resource was not found in the current Region.</p>
            capo_omics.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request exceeds a service quota.</p>
            capo_omics.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_omics.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_omics.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_omics.types.get_workflow_version_request.GetWorkflowVersionRequest]",
        ) -> AsyncOperationResponse[
            "capo_omics.types.get_workflow_version_response.GetWorkflowVersionResponse"
        ]:
            import capo_omics._operations.omics.get_workflow_version

            (
                output,
                http_response,
            ) = await capo_omics._operations.omics.get_workflow_version.async_get_workflow_version(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_omics.types.get_workflow_version_request.GetWorkflowVersionRequest = {
            "workflow_id": workflow_id,
            "version_name": version_name,
        }
        if type is not None:
            input_["type"] = type
        if export is not None:
            input_["export"] = export
        if workflow_owner_id is not None:
            input_["workflow_owner_id"] = workflow_owner_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_workflow_version(
        self,
        workflow_id: "capo_omics.types.workflow_id.WorkflowId",
        version_name: "capo_omics.types.workflow_version_name.WorkflowVersionName",
        *,
        config_overrides: Optional[AsyncOmicsClientConfig] = None,
        description: Optional[
            "capo_omics.types.workflow_version_description.WorkflowVersionDescription"
        ] = None,
        storage_type: Optional["capo_omics.types.storage_type.StorageType"] = None,
        storage_capacity: Optional[int] = None,
        readme_markdown: Optional[
            "capo_omics.types.readme_markdown.ReadmeMarkdown"
        ] = None,
    ) -> None:
        """<p>Updates information about the workflow version. For more information, see <a href="https://docs.aws.amazon.com/omics/latest/dev/workflow-versions.html">Workflow versioning in Amazon Web Services HealthOmics</a> in the <i>Amazon Web Services HealthOmics User Guide</i>.</p>

        Args:
            workflow_id: <p>The workflow's ID. The <code>workflowId</code> is not the UUID.</p>
            version_name: <p>The name of the workflow version.</p>
            description: <p>Description of the workflow version.</p>
            storage_type: <p>The default storage type for runs that use this workflow version. The <code>storageType</code> can be overridden at run time. <code>DYNAMIC</code> storage dynamically scales the storage up or down, based on file system utilization. STATIC storage allocates a fixed amount of storage. For more information about dynamic and static storage types, see <a href="https://docs.aws.amazon.com/omics/latest/dev/workflows-run-types.html">Run storage types</a> in the <i>in the <i>Amazon Web Services HealthOmics User Guide</i> </i>.</p>
            storage_capacity: <p>The default static storage capacity (in gibibytes) for runs that use this workflow version. The <code>storageCapacity</code> can be overwritten at run time. The storage capacity is not required for runs with a <code>DYNAMIC</code> storage type.</p>
            readme_markdown: <p>The markdown content for the workflow version's README file. This provides documentation and usage information for users of this specific workflow version.</p>

        Raises:
            capo_omics.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_omics.errors.conflict_exception.ConflictException: <p>The request cannot be applied to the target resource in its current state.</p>
            capo_omics.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred. Try the request again.</p>
            capo_omics.errors.request_timeout_exception.RequestTimeoutException: <p>The request timed out.</p>
            capo_omics.errors.resource_not_found_exception.ResourceNotFoundException: <p>The target resource was not found in the current Region.</p>
            capo_omics.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request exceeds a service quota.</p>
            capo_omics.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_omics.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_omics.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_omics.types.update_workflow_version_request.UpdateWorkflowVersionRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_omics._operations.omics.update_workflow_version

            (
                output,
                http_response,
            ) = await capo_omics._operations.omics.update_workflow_version.async_update_workflow_version(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_omics.types.update_workflow_version_request.UpdateWorkflowVersionRequest = {
            "workflow_id": workflow_id,
            "version_name": version_name,
        }
        if description is not None:
            input_["description"] = description
        if storage_type is not None:
            input_["storage_type"] = storage_type
        if storage_capacity is not None:
            input_["storage_capacity"] = storage_capacity
        if readme_markdown is not None:
            input_["readme_markdown"] = readme_markdown

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_workflow_version(
        self,
        workflow_id: "capo_omics.types.workflow_id.WorkflowId",
        version_name: "capo_omics.types.workflow_version_name.WorkflowVersionName",
        *,
        config_overrides: Optional[AsyncOmicsClientConfig] = None,
    ) -> None:
        """<p>Deletes a workflow version. Deleting a workflow version doesn't affect any ongoing runs that are using the workflow version.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/omics/latest/dev/workflow-versions.html">Workflow versioning in Amazon Web Services HealthOmics</a> in the <i>Amazon Web Services HealthOmics User Guide</i>.</p>

        Args:
            workflow_id: <p>The workflow's ID.</p>
            version_name: <p>The workflow version name.</p>

        Raises:
            capo_omics.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_omics.errors.conflict_exception.ConflictException: <p>The request cannot be applied to the target resource in its current state.</p>
            capo_omics.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred. Try the request again.</p>
            capo_omics.errors.request_timeout_exception.RequestTimeoutException: <p>The request timed out.</p>
            capo_omics.errors.resource_not_found_exception.ResourceNotFoundException: <p>The target resource was not found in the current Region.</p>
            capo_omics.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request exceeds a service quota.</p>
            capo_omics.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_omics.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_omics.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_omics.types.delete_workflow_version_request.DeleteWorkflowVersionRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_omics._operations.omics.delete_workflow_version

            (
                output,
                http_response,
            ) = await capo_omics._operations.omics.delete_workflow_version.async_delete_workflow_version(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_omics.types.delete_workflow_version_request.DeleteWorkflowVersionRequest = {
            "workflow_id": workflow_id,
            "version_name": version_name,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_workflow_versions(
        self,
        workflow_id: "capo_omics.types.workflow_id.WorkflowId",
        *,
        config_overrides: Optional[AsyncOmicsClientConfig] = None,
        type: Optional["capo_omics.types.workflow_type.WorkflowType"] = None,
        workflow_owner_id: Optional[
            "capo_omics.types.workflow_owner_id.WorkflowOwnerId"
        ] = None,
        starting_token: Optional[
            "capo_omics.types.workflow_version_list_token.WorkflowVersionListToken"
        ] = None,
        max_results: Optional[int] = None,
    ) -> (
        "capo_omics.types.list_workflow_versions_response.ListWorkflowVersionsResponse"
    ):
        """<p>Lists the workflow versions for the specified workflow. For more information, see <a href="https://docs.aws.amazon.com/omics/latest/dev/workflow-versions.html">Workflow versioning in Amazon Web Services HealthOmics</a> in the <i>Amazon Web Services HealthOmics User Guide</i>.</p>

        Args:
            workflow_id: <p>The workflow's ID. The <code>workflowId</code> is not the UUID.</p>
            type: <p>The workflow type.</p>
            workflow_owner_id: <p>The 12-digit account ID of the workflow owner. The workflow owner ID can be retrieved using the <code>GetShare</code> API operation. If you are the workflow owner, you do not need to include this ID.</p>
            starting_token: <p>Specify the pagination token from a previous request to retrieve the next page of results.</p>
            max_results: <p>The maximum number of workflows to return in one page of results.</p>

        Raises:
            capo_omics.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_omics.errors.conflict_exception.ConflictException: <p>The request cannot be applied to the target resource in its current state.</p>
            capo_omics.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred. Try the request again.</p>
            capo_omics.errors.request_timeout_exception.RequestTimeoutException: <p>The request timed out.</p>
            capo_omics.errors.resource_not_found_exception.ResourceNotFoundException: <p>The target resource was not found in the current Region.</p>
            capo_omics.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request exceeds a service quota.</p>
            capo_omics.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_omics.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_omics.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_omics.types.list_workflow_versions_request.ListWorkflowVersionsRequest]",
        ) -> AsyncOperationResponse[
            "capo_omics.types.list_workflow_versions_response.ListWorkflowVersionsResponse"
        ]:
            import capo_omics._operations.omics.list_workflow_versions

            (
                output,
                http_response,
            ) = await capo_omics._operations.omics.list_workflow_versions.async_list_workflow_versions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_omics.types.list_workflow_versions_request.ListWorkflowVersionsRequest = {
            "workflow_id": workflow_id
        }
        if type is not None:
            input_["type"] = type
        if workflow_owner_id is not None:
            input_["workflow_owner_id"] = workflow_owner_id
        if starting_token is not None:
            input_["starting_token"] = starting_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_workflow_versions(
        self,
        workflow_id: "capo_omics.types.workflow_id.WorkflowId",
        *,
        config_overrides: Optional[AsyncOmicsClientConfig] = None,
        type: Optional["capo_omics.types.workflow_type.WorkflowType"] = None,
        workflow_owner_id: Optional[
            "capo_omics.types.workflow_owner_id.WorkflowOwnerId"
        ] = None,
        starting_token: Optional[
            "capo_omics.types.workflow_version_list_token.WorkflowVersionListToken"
        ] = None,
        max_results: Optional[int] = None,
    ) -> "AsyncIterator[capo_omics.types.workflow_version_list_item.WorkflowVersionListItem]":
        _token = starting_token
        while True:
            _response = await self.list_workflow_versions(
                workflow_id,
                config_overrides=config_overrides,
                type=type,
                workflow_owner_id=workflow_owner_id,
                starting_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(self, exc_type: Any, exc: Any, tb: Any):
        await self._client.aclose()
