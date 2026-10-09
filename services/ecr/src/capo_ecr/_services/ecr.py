"""Generated from Smithy shape ``com.amazonaws.ecr#AmazonEC2ContainerRegistry_V20150921``."""

import warnings
from collections.abc import Iterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import BaseHandler, Client

import capo_ecr._auth._signers
import capo_ecr._auth._sigv4
from capo_ecr._auth._identity import Credentials
from capo_ecr._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_ecr._auth._zapros_handler import AuthMiddleware
from capo_ecr._pagination import resolve_path as _resolve_path
from capo_ecr._services._aws_config import aws_config
from capo_ecr._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import capo_ecr.types.account_setting_name
    import capo_ecr.types.account_setting_value
    import capo_ecr.types.arn
    import capo_ecr.types.batch_check_layer_availability_request
    import capo_ecr.types.batch_check_layer_availability_response
    import capo_ecr.types.batch_delete_image_request
    import capo_ecr.types.batch_delete_image_response
    import capo_ecr.types.batch_get_image_request
    import capo_ecr.types.batch_get_image_response
    import capo_ecr.types.batch_get_repository_scanning_configuration_request
    import capo_ecr.types.batch_get_repository_scanning_configuration_response
    import capo_ecr.types.batched_operation_layer_digest_list
    import capo_ecr.types.complete_layer_upload_request
    import capo_ecr.types.complete_layer_upload_response
    import capo_ecr.types.create_pull_through_cache_rule_request
    import capo_ecr.types.create_pull_through_cache_rule_response
    import capo_ecr.types.create_repository_creation_template_request
    import capo_ecr.types.create_repository_creation_template_response
    import capo_ecr.types.create_repository_request
    import capo_ecr.types.create_repository_response
    import capo_ecr.types.credential_arn
    import capo_ecr.types.custom_role_arn
    import capo_ecr.types.delete_lifecycle_policy_request
    import capo_ecr.types.delete_lifecycle_policy_response
    import capo_ecr.types.delete_pull_through_cache_rule_request
    import capo_ecr.types.delete_pull_through_cache_rule_response
    import capo_ecr.types.delete_registry_policy_request
    import capo_ecr.types.delete_registry_policy_response
    import capo_ecr.types.delete_repository_creation_template_request
    import capo_ecr.types.delete_repository_creation_template_response
    import capo_ecr.types.delete_repository_policy_request
    import capo_ecr.types.delete_repository_policy_response
    import capo_ecr.types.delete_repository_request
    import capo_ecr.types.delete_repository_response
    import capo_ecr.types.delete_signing_configuration_request
    import capo_ecr.types.delete_signing_configuration_response
    import capo_ecr.types.deregister_pull_time_update_exclusion_request
    import capo_ecr.types.deregister_pull_time_update_exclusion_response
    import capo_ecr.types.describe_image_replication_status_request
    import capo_ecr.types.describe_image_replication_status_response
    import capo_ecr.types.describe_image_scan_findings_request
    import capo_ecr.types.describe_image_scan_findings_response
    import capo_ecr.types.describe_image_signing_status_request
    import capo_ecr.types.describe_image_signing_status_response
    import capo_ecr.types.describe_images_filter
    import capo_ecr.types.describe_images_request
    import capo_ecr.types.describe_images_response
    import capo_ecr.types.describe_pull_through_cache_rules_request
    import capo_ecr.types.describe_pull_through_cache_rules_response
    import capo_ecr.types.describe_registry_request
    import capo_ecr.types.describe_registry_response
    import capo_ecr.types.describe_repositories_request
    import capo_ecr.types.describe_repositories_response
    import capo_ecr.types.describe_repository_creation_templates_request
    import capo_ecr.types.describe_repository_creation_templates_response
    import capo_ecr.types.encryption_configuration
    import capo_ecr.types.encryption_configuration_for_repository_creation_template
    import capo_ecr.types.fifty_max_results
    import capo_ecr.types.force_flag
    import capo_ecr.types.get_account_setting_request
    import capo_ecr.types.get_account_setting_response
    import capo_ecr.types.get_authorization_token_registry_id_list
    import capo_ecr.types.get_authorization_token_request
    import capo_ecr.types.get_authorization_token_response
    import capo_ecr.types.get_download_url_for_layer_request
    import capo_ecr.types.get_download_url_for_layer_response
    import capo_ecr.types.get_lifecycle_policy_preview_request
    import capo_ecr.types.get_lifecycle_policy_preview_response
    import capo_ecr.types.get_lifecycle_policy_request
    import capo_ecr.types.get_lifecycle_policy_response
    import capo_ecr.types.get_registry_policy_request
    import capo_ecr.types.get_registry_policy_response
    import capo_ecr.types.get_registry_scanning_configuration_request
    import capo_ecr.types.get_registry_scanning_configuration_response
    import capo_ecr.types.get_repository_policy_request
    import capo_ecr.types.get_repository_policy_response
    import capo_ecr.types.get_signing_configuration_request
    import capo_ecr.types.get_signing_configuration_response
    import capo_ecr.types.image_detail
    import capo_ecr.types.image_digest
    import capo_ecr.types.image_identifier
    import capo_ecr.types.image_identifier_list
    import capo_ecr.types.image_manifest
    import capo_ecr.types.image_scanning_configuration
    import capo_ecr.types.image_tag
    import capo_ecr.types.image_tag_mutability
    import capo_ecr.types.image_tag_mutability_exclusion_filters
    import capo_ecr.types.initiate_layer_upload_request
    import capo_ecr.types.initiate_layer_upload_response
    import capo_ecr.types.layer_digest
    import capo_ecr.types.layer_digest_list
    import capo_ecr.types.layer_part_blob
    import capo_ecr.types.lifecycle_policy_preview_filter
    import capo_ecr.types.lifecycle_policy_preview_result
    import capo_ecr.types.lifecycle_policy_text
    import capo_ecr.types.lifecycle_policy_text_for_repository_creation_template
    import capo_ecr.types.lifecycle_preview_max_results
    import capo_ecr.types.list_image_referrers_filter
    import capo_ecr.types.list_image_referrers_request
    import capo_ecr.types.list_image_referrers_response
    import capo_ecr.types.list_images_filter
    import capo_ecr.types.list_images_request
    import capo_ecr.types.list_images_response
    import capo_ecr.types.list_pull_time_update_exclusions_request
    import capo_ecr.types.list_pull_time_update_exclusions_response
    import capo_ecr.types.list_tags_for_resource_request
    import capo_ecr.types.list_tags_for_resource_response
    import capo_ecr.types.max_results
    import capo_ecr.types.media_type
    import capo_ecr.types.media_type_list
    import capo_ecr.types.next_token
    import capo_ecr.types.part_size
    import capo_ecr.types.prefix
    import capo_ecr.types.prefix_list
    import capo_ecr.types.principal_arn
    import capo_ecr.types.pull_through_cache_rule
    import capo_ecr.types.pull_through_cache_rule_repository_prefix
    import capo_ecr.types.pull_through_cache_rule_repository_prefix_list
    import capo_ecr.types.put_account_setting_request
    import capo_ecr.types.put_account_setting_response
    import capo_ecr.types.put_image_request
    import capo_ecr.types.put_image_response
    import capo_ecr.types.put_image_scanning_configuration_request
    import capo_ecr.types.put_image_scanning_configuration_response
    import capo_ecr.types.put_image_tag_mutability_request
    import capo_ecr.types.put_image_tag_mutability_response
    import capo_ecr.types.put_lifecycle_policy_request
    import capo_ecr.types.put_lifecycle_policy_response
    import capo_ecr.types.put_registry_policy_request
    import capo_ecr.types.put_registry_policy_response
    import capo_ecr.types.put_registry_scanning_configuration_request
    import capo_ecr.types.put_registry_scanning_configuration_response
    import capo_ecr.types.put_replication_configuration_request
    import capo_ecr.types.put_replication_configuration_response
    import capo_ecr.types.put_signing_configuration_request
    import capo_ecr.types.put_signing_configuration_response
    import capo_ecr.types.rct_applied_for_list
    import capo_ecr.types.register_pull_time_update_exclusion_request
    import capo_ecr.types.register_pull_time_update_exclusion_response
    import capo_ecr.types.registry_id
    import capo_ecr.types.registry_policy_text
    import capo_ecr.types.registry_scanning_rule_list
    import capo_ecr.types.replication_configuration
    import capo_ecr.types.repository
    import capo_ecr.types.repository_creation_template
    import capo_ecr.types.repository_name
    import capo_ecr.types.repository_name_list
    import capo_ecr.types.repository_policy_text
    import capo_ecr.types.repository_template_description
    import capo_ecr.types.scan_type
    import capo_ecr.types.scanning_configuration_repository_name_list
    import capo_ecr.types.set_repository_policy_request
    import capo_ecr.types.set_repository_policy_response
    import capo_ecr.types.signing_configuration
    import capo_ecr.types.start_image_scan_request
    import capo_ecr.types.start_image_scan_response
    import capo_ecr.types.start_lifecycle_policy_preview_request
    import capo_ecr.types.start_lifecycle_policy_preview_response
    import capo_ecr.types.subject_identifier
    import capo_ecr.types.tag_key_list
    import capo_ecr.types.tag_list
    import capo_ecr.types.tag_resource_request
    import capo_ecr.types.tag_resource_response
    import capo_ecr.types.target_storage_class
    import capo_ecr.types.untag_resource_request
    import capo_ecr.types.untag_resource_response
    import capo_ecr.types.update_image_storage_class_request
    import capo_ecr.types.update_image_storage_class_response
    import capo_ecr.types.update_pull_through_cache_rule_request
    import capo_ecr.types.update_pull_through_cache_rule_response
    import capo_ecr.types.update_repository_creation_template_request
    import capo_ecr.types.update_repository_creation_template_response
    import capo_ecr.types.upload_id
    import capo_ecr.types.upload_layer_part_request
    import capo_ecr.types.upload_layer_part_response
    import capo_ecr.types.upstream_registry
    import capo_ecr.types.url
    import capo_ecr.types.validate_pull_through_cache_rule_request
    import capo_ecr.types.validate_pull_through_cache_rule_response


class ECRClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    region: str | None
    credentials_provider: IdentityProvider[Credentials] | None
    anonymous: bool | None


class ECRClient:
    """A client for the ``ECR`` service.

    Args:
        http_handler: HTTP handler for sending requests. If not provided, creates a default handler.
        operation_interceptors: Interceptors that wrap every operation call. If not provided, defaults to an empty list.
        retry_max_attempts: Maximum number of times to retry a failed operation. Defaults to 3.
        use_dual_stack: The value of the ``AWS::UseDualStack`` endpoint parameter.
        use_fips: The value of the ``AWS::UseFIPS`` endpoint parameter.
        endpoint: The value of the ``SDK::Endpoint`` endpoint parameter.
        region: The value of the ``AWS::Region`` endpoint parameter.
        credentials: AWS credentials for request signing.
        credentials_provider: Provider that resolves AWS credentials. Takes precedence over ``credentials``.
        anonymous: Send requests unsigned, without resolving credentials, even for operations that require authentication.
    """

    def __init__(
        self,
        http_handler: BaseHandler | None = None,
        operation_interceptors: Iterable[Interceptor[Any, Any]] | None = None,
        retry_max_attempts: int | None = None,
        use_dual_stack: bool | None = None,
        use_fips: bool | None = None,
        endpoint: str | None = None,
        region: str | None = None,
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
        self._config = ECRClientConfig(
            {
                "operation_interceptors": operation_interceptors or [],
                "retry_max_attempts": retry_max_attempts,
                "use_dual_stack": use_dual_stack,
                "use_fips": use_fips,
                "endpoint": endpoint,
                "region": region,
                "credentials_provider": resolved_credentials_provider,
                "anonymous": anonymous,
            }
        )

    def operation_options(
        self, config_overrides: Optional[ECRClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: ECRClientConfig = config_overrides or {}
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
            use_dual_stack=overrides.get(
                "use_dual_stack", self._config.get("use_dual_stack")
            ),
            use_fips=overrides.get("use_fips", self._config.get("use_fips")),
            endpoint=overrides.get("endpoint", self._config.get("endpoint")),
            region=overrides.get("region", self._config.get("region")),
            credentials_provider=overrides.get(
                "credentials_provider", self._config.get("credentials_provider")
            ),
            anonymous=overrides.get("anonymous", self._config.get("anonymous")),
        )
        return interceptors_, options_

    def batch_check_layer_availability(
        self,
        repository_name: "capo_ecr.types.repository_name.RepositoryName",
        layer_digests: "capo_ecr.types.batched_operation_layer_digest_list.BatchedOperationLayerDigestList",
        *,
        config_overrides: Optional[ECRClientConfig] = None,
        registry_id: Optional["capo_ecr.types.registry_id.RegistryId"] = None,
    ) -> "capo_ecr.types.batch_check_layer_availability_response.BatchCheckLayerAvailabilityResponse":
        """<p>Checks the availability of one or more image layers in a repository.</p> <p>When an image is pushed to a repository, each image layer is checked to verify if it has been uploaded before. If it has been uploaded, then the image layer is skipped.</p> <note> <p>This operation is used by the Amazon ECR proxy and is not generally used by customers for pulling and pushing images. In most cases, you should use the <code>docker</code> CLI to pull, tag, and push images.</p> </note>

        Args:
            registry_id: <p>The Amazon Web Services account ID associated with the registry that contains the image layers to check. If you do not specify a registry, the default registry is assumed.</p>
            repository_name: <p>The name of the repository that is associated with the image layers to check.</p>
            layer_digests: <p>The digests of the image layers to check.</p>

        Raises:
            capo_ecr.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter is invalid. Review the available parameters for the API request.</p>
            capo_ecr.errors.repository_not_found_exception.RepositoryNotFoundException: <p>The specified repository could not be found. Check the spelling of the specified repository and ensure that you are performing operations on the correct registry.</p>
            capo_ecr.errors.server_exception.ServerException: <p>These errors are usually caused by a server-side issue.</p>
            capo_ecr.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_ecr.types.batch_check_layer_availability_request.BatchCheckLayerAvailabilityRequest]",
        ) -> OperationResponse[
            "capo_ecr.types.batch_check_layer_availability_response.BatchCheckLayerAvailabilityResponse"
        ]:
            import capo_ecr._operations.amazon_ec2_container_registry_v20150921.batch_check_layer_availability

            output, http_response = (
                capo_ecr._operations.amazon_ec2_container_registry_v20150921.batch_check_layer_availability.batch_check_layer_availability(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ecr.types.batch_check_layer_availability_request.BatchCheckLayerAvailabilityRequest = {
            "repository_name": repository_name,
            "layer_digests": layer_digests,
        }
        if registry_id is not None:
            input_["registry_id"] = registry_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def batch_delete_image(
        self,
        repository_name: "capo_ecr.types.repository_name.RepositoryName",
        image_ids: "capo_ecr.types.image_identifier_list.ImageIdentifierList",
        *,
        config_overrides: Optional[ECRClientConfig] = None,
        registry_id: Optional["capo_ecr.types.registry_id.RegistryId"] = None,
    ) -> "capo_ecr.types.batch_delete_image_response.BatchDeleteImageResponse":
        """<p>Deletes a list of specified images within a repository. Images are specified with either an <code>imageTag</code> or <code>imageDigest</code>.</p> <p>You can remove a tag from an image by specifying the image's tag in your request. When you remove the last tag from an image, the image is deleted from your repository.</p> <p>You can completely delete an image (and all of its tags) by specifying the image's digest in your request.</p>

        Args:
            registry_id: <p>The Amazon Web Services account ID associated with the registry that contains the image to delete. If you do not specify a registry, the default registry is assumed.</p>
            repository_name: <p>The repository that contains the image to delete.</p>
            image_ids: <p>A list of image ID references that correspond to images to delete. The format of the <code>imageIds</code> reference is <code>imageTag=tag</code> or <code>imageDigest=digest</code>.</p>

        Raises:
            capo_ecr.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter is invalid. Review the available parameters for the API request.</p>
            capo_ecr.errors.repository_not_found_exception.RepositoryNotFoundException: <p>The specified repository could not be found. Check the spelling of the specified repository and ensure that you are performing operations on the correct registry.</p>
            capo_ecr.errors.server_exception.ServerException: <p>These errors are usually caused by a server-side issue.</p>
            capo_ecr.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To delete multiple images
            This example deletes images with the tags precise and trusty in a repository called ubuntu in the default registry for an account.

            >>> client.batch_delete_image(repository_name='ubuntu', image_ids=[{'imageTag': 'precise'}])
        """

        def _handler(
            req: "OperationRequest[capo_ecr.types.batch_delete_image_request.BatchDeleteImageRequest]",
        ) -> OperationResponse[
            "capo_ecr.types.batch_delete_image_response.BatchDeleteImageResponse"
        ]:
            import capo_ecr._operations.amazon_ec2_container_registry_v20150921.batch_delete_image

            output, http_response = (
                capo_ecr._operations.amazon_ec2_container_registry_v20150921.batch_delete_image.batch_delete_image(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ecr.types.batch_delete_image_request.BatchDeleteImageRequest = {
            "repository_name": repository_name,
            "image_ids": image_ids,
        }
        if registry_id is not None:
            input_["registry_id"] = registry_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def batch_get_image(
        self,
        repository_name: "capo_ecr.types.repository_name.RepositoryName",
        image_ids: "capo_ecr.types.image_identifier_list.ImageIdentifierList",
        *,
        config_overrides: Optional[ECRClientConfig] = None,
        registry_id: Optional["capo_ecr.types.registry_id.RegistryId"] = None,
        accepted_media_types: Optional[
            "capo_ecr.types.media_type_list.MediaTypeList"
        ] = None,
    ) -> "capo_ecr.types.batch_get_image_response.BatchGetImageResponse":
        """<p>Gets detailed information for an image. Images are specified with either an <code>imageTag</code> or <code>imageDigest</code>.</p> <p>When an image is pulled, the BatchGetImage API is called once to retrieve the image manifest.</p>

        Args:
            registry_id: <p>The Amazon Web Services account ID associated with the registry that contains the images to describe. If you do not specify a registry, the default registry is assumed.</p>
            repository_name: <p>The repository that contains the images to describe.</p>
            image_ids: <p>A list of image ID references that correspond to images to describe. The format of the <code>imageIds</code> reference is <code>imageTag=tag</code> or <code>imageDigest=digest</code>.</p>
            accepted_media_types: <p>The accepted media types for the request.</p> <p>Valid values: <code>application/vnd.docker.distribution.manifest.v1+json</code> | <code>application/vnd.docker.distribution.manifest.v2+json</code> | <code>application/vnd.oci.image.manifest.v1+json</code> </p>

        Raises:
            capo_ecr.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter is invalid. Review the available parameters for the API request.</p>
            capo_ecr.errors.limit_exceeded_exception.LimitExceededException: <p>The operation did not succeed because it would have exceeded a service limit for your account. For more information, see <a href="https://docs.aws.amazon.com/AmazonECR/latest/userguide/service-quotas.html">Amazon ECR service quotas</a> in the Amazon Elastic Container Registry User Guide.</p>
            capo_ecr.errors.repository_not_found_exception.RepositoryNotFoundException: <p>The specified repository could not be found. Check the spelling of the specified repository and ensure that you are performing operations on the correct registry.</p>
            capo_ecr.errors.server_exception.ServerException: <p>These errors are usually caused by a server-side issue.</p>
            capo_ecr.errors.unable_to_get_upstream_image_exception.UnableToGetUpstreamImageException: <p>The image or images were unable to be pulled using the pull through cache rule. This is usually caused because of an issue with the Secrets Manager secret containing the credentials for the upstream registry.</p>
            capo_ecr.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To obtain multiple images in a single request
            This example obtains information for an image with a specified image digest ID from the repository named ubuntu in the current account.

            >>> client.batch_get_image(repository_name='ubuntu', image_ids=[{'imageTag': 'precise'}])
        """

        def _handler(
            req: "OperationRequest[capo_ecr.types.batch_get_image_request.BatchGetImageRequest]",
        ) -> OperationResponse[
            "capo_ecr.types.batch_get_image_response.BatchGetImageResponse"
        ]:
            import capo_ecr._operations.amazon_ec2_container_registry_v20150921.batch_get_image

            output, http_response = (
                capo_ecr._operations.amazon_ec2_container_registry_v20150921.batch_get_image.batch_get_image(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ecr.types.batch_get_image_request.BatchGetImageRequest = {
            "repository_name": repository_name,
            "image_ids": image_ids,
        }
        if registry_id is not None:
            input_["registry_id"] = registry_id
        if accepted_media_types is not None:
            input_["accepted_media_types"] = accepted_media_types

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def batch_get_repository_scanning_configuration(
        self,
        repository_names: "capo_ecr.types.scanning_configuration_repository_name_list.ScanningConfigurationRepositoryNameList",
        *,
        config_overrides: Optional[ECRClientConfig] = None,
    ) -> "capo_ecr.types.batch_get_repository_scanning_configuration_response.BatchGetRepositoryScanningConfigurationResponse":
        """<p>Gets the scanning configuration for one or more repositories.</p>

        Args:
            repository_names: <p>One or more repository names to get the scanning configuration for.</p>

        Raises:
            capo_ecr.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter is invalid. Review the available parameters for the API request.</p>
            capo_ecr.errors.repository_not_found_exception.RepositoryNotFoundException: <p>The specified repository could not be found. Check the spelling of the specified repository and ensure that you are performing operations on the correct registry.</p>
            capo_ecr.errors.server_exception.ServerException: <p>These errors are usually caused by a server-side issue.</p>
            capo_ecr.errors.validation_exception.ValidationException: <p>There was an exception validating this request.</p>
            capo_ecr.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_ecr.types.batch_get_repository_scanning_configuration_request.BatchGetRepositoryScanningConfigurationRequest]",
        ) -> OperationResponse[
            "capo_ecr.types.batch_get_repository_scanning_configuration_response.BatchGetRepositoryScanningConfigurationResponse"
        ]:
            import capo_ecr._operations.amazon_ec2_container_registry_v20150921.batch_get_repository_scanning_configuration

            output, http_response = (
                capo_ecr._operations.amazon_ec2_container_registry_v20150921.batch_get_repository_scanning_configuration.batch_get_repository_scanning_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ecr.types.batch_get_repository_scanning_configuration_request.BatchGetRepositoryScanningConfigurationRequest = {
            "repository_names": repository_names
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def complete_layer_upload(
        self,
        repository_name: "capo_ecr.types.repository_name.RepositoryName",
        upload_id: "capo_ecr.types.upload_id.UploadId",
        layer_digests: "capo_ecr.types.layer_digest_list.LayerDigestList",
        *,
        config_overrides: Optional[ECRClientConfig] = None,
        registry_id: Optional["capo_ecr.types.registry_id.RegistryId"] = None,
    ) -> "capo_ecr.types.complete_layer_upload_response.CompleteLayerUploadResponse":
        """<p>Informs Amazon ECR that the image layer upload has completed for a specified registry, repository name, and upload ID. You can optionally provide a <code>sha256</code> digest of the image layer for data validation purposes.</p> <p>When an image is pushed, the CompleteLayerUpload API is called once per each new image layer to verify that the upload has completed.</p> <note> <p>This operation is used by the Amazon ECR proxy and is not generally used by customers for pulling and pushing images. In most cases, you should use the <code>docker</code> CLI to pull, tag, and push images.</p> </note>

        Args:
            registry_id: <p>The Amazon Web Services account ID associated with the registry to which to upload layers. If you do not specify a registry, the default registry is assumed.</p>
            repository_name: <p>The name of the repository to associate with the image layer.</p>
            upload_id: <p>The upload ID from a previous <a>InitiateLayerUpload</a> operation to associate with the image layer.</p>
            layer_digests: <p>The <code>sha256</code> digest of the image layer.</p>

        Raises:
            capo_ecr.errors.empty_upload_exception.EmptyUploadException: <p>The specified layer upload does not contain any layer parts.</p>
            capo_ecr.errors.invalid_layer_exception.InvalidLayerException: <p>The layer digest calculation performed by Amazon ECR upon receipt of the image layer does not match the digest specified.</p>
            capo_ecr.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter is invalid. Review the available parameters for the API request.</p>
            capo_ecr.errors.kms_exception.KmsException: <p>The operation failed due to a KMS exception.</p>
            capo_ecr.errors.layer_already_exists_exception.LayerAlreadyExistsException: <p>The image layer already exists in the associated repository.</p>
            capo_ecr.errors.layer_part_too_small_exception.LayerPartTooSmallException: <p>Layer parts must be at least 5 MiB in size.</p>
            capo_ecr.errors.repository_not_found_exception.RepositoryNotFoundException: <p>The specified repository could not be found. Check the spelling of the specified repository and ensure that you are performing operations on the correct registry.</p>
            capo_ecr.errors.server_exception.ServerException: <p>These errors are usually caused by a server-side issue.</p>
            capo_ecr.errors.upload_not_found_exception.UploadNotFoundException: <p>The upload could not be found, or the specified upload ID is not valid for this repository.</p>
            capo_ecr.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_ecr.types.complete_layer_upload_request.CompleteLayerUploadRequest]",
        ) -> OperationResponse[
            "capo_ecr.types.complete_layer_upload_response.CompleteLayerUploadResponse"
        ]:
            import capo_ecr._operations.amazon_ec2_container_registry_v20150921.complete_layer_upload

            output, http_response = (
                capo_ecr._operations.amazon_ec2_container_registry_v20150921.complete_layer_upload.complete_layer_upload(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ecr.types.complete_layer_upload_request.CompleteLayerUploadRequest = {
            "repository_name": repository_name,
            "upload_id": upload_id,
            "layer_digests": layer_digests,
        }
        if registry_id is not None:
            input_["registry_id"] = registry_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_pull_through_cache_rule(
        self,
        ecr_repository_prefix: "capo_ecr.types.pull_through_cache_rule_repository_prefix.PullThroughCacheRuleRepositoryPrefix",
        upstream_registry_url: "capo_ecr.types.url.Url",
        *,
        config_overrides: Optional[ECRClientConfig] = None,
        registry_id: Optional["capo_ecr.types.registry_id.RegistryId"] = None,
        upstream_registry: Optional[
            "capo_ecr.types.upstream_registry.UpstreamRegistry"
        ] = None,
        credential_arn: Optional["capo_ecr.types.credential_arn.CredentialArn"] = None,
        custom_role_arn: Optional[
            "capo_ecr.types.custom_role_arn.CustomRoleArn"
        ] = None,
        upstream_repository_prefix: Optional[
            "capo_ecr.types.pull_through_cache_rule_repository_prefix.PullThroughCacheRuleRepositoryPrefix"
        ] = None,
    ) -> "capo_ecr.types.create_pull_through_cache_rule_response.CreatePullThroughCacheRuleResponse":
        """<p>Creates a pull through cache rule. A pull through cache rule provides a way to cache images from an upstream registry source in your Amazon ECR private registry. For more information, see <a href="https://docs.aws.amazon.com/AmazonECR/latest/userguide/pull-through-cache.html">Using pull through cache rules</a> in the <i>Amazon Elastic Container Registry User Guide</i>.</p>

        Args:
            ecr_repository_prefix: <p>The repository name prefix to use when caching images from the source registry.</p> <important> <p>There is always an assumed <code>/</code> applied to the end of the prefix. If you specify <code>ecr-public</code> as the prefix, Amazon ECR treats that as <code>ecr-public/</code>.</p> </important>
            upstream_registry_url: <p>The registry URL of the upstream public registry to use as the source for the pull through cache rule. The following is the syntax to use for each supported upstream registry.</p> <ul> <li> <p>Amazon ECR (<code>ecr</code>) – <code><accountId>.dkr.ecr.<region>.amazonaws.com</code> </p> </li> <li> <p>Amazon ECR Public (<code>ecr-public</code>) – <code>public.ecr.aws</code> </p> </li> <li> <p>Docker Hub (<code>docker-hub</code>) – <code>registry-1.docker.io</code> </p> </li> <li> <p>GitHub Container Registry (<code>github-container-registry</code>) – <code>ghcr.io</code> </p> </li> <li> <p>GitLab Container Registry (<code>gitlab-container-registry</code>) – <code>registry.gitlab.com</code> </p> </li> <li> <p>Kubernetes (<code>k8s</code>) – <code>registry.k8s.io</code> </p> </li> <li> <p>Microsoft Azure Container Registry (<code>azure-container-registry</code>) – <code><custom>.azurecr.io</code> </p> </li> <li> <p>Quay (<code>quay</code>) – <code>quay.io</code> </p> </li> </ul>
            registry_id: <p>The Amazon Web Services account ID associated with the registry to create the pull through cache rule for. If you do not specify a registry, the default registry is assumed.</p>
            upstream_registry: <p>The name of the upstream registry.</p>
            credential_arn: <p>The Amazon Resource Name (ARN) of the Amazon Web Services Secrets Manager secret that identifies the credentials to authenticate to the upstream registry.</p>
            custom_role_arn: <p>Amazon Resource Name (ARN) of the IAM role to be assumed by Amazon ECR to authenticate to the ECR upstream registry. This role must be in the same account as the registry that you are configuring.</p>
            upstream_repository_prefix: <p>The repository name prefix of the upstream registry to match with the upstream repository name. When this field isn't specified, Amazon ECR will use the <code>ROOT</code>.</p>

        Raises:
            capo_ecr.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter is invalid. Review the available parameters for the API request.</p>
            capo_ecr.errors.limit_exceeded_exception.LimitExceededException: <p>The operation did not succeed because it would have exceeded a service limit for your account. For more information, see <a href="https://docs.aws.amazon.com/AmazonECR/latest/userguide/service-quotas.html">Amazon ECR service quotas</a> in the Amazon Elastic Container Registry User Guide.</p>
            capo_ecr.errors.pull_through_cache_rule_already_exists_exception.PullThroughCacheRuleAlreadyExistsException: <p>A pull through cache rule with these settings already exists for the private registry.</p>
            capo_ecr.errors.secret_not_found_exception.SecretNotFoundException: <p>The ARN of the secret specified in the pull through cache rule was not found. Update the pull through cache rule with a valid secret ARN and try again.</p>
            capo_ecr.errors.server_exception.ServerException: <p>These errors are usually caused by a server-side issue.</p>
            capo_ecr.errors.unable_to_access_secret_exception.UnableToAccessSecretException: <p>The secret is unable to be accessed. Verify the resource permissions for the secret and try again.</p>
            capo_ecr.errors.unable_to_decrypt_secret_value_exception.UnableToDecryptSecretValueException: <p>The secret is accessible but is unable to be decrypted. Verify the resource permisisons and try again.</p>
            capo_ecr.errors.unsupported_upstream_registry_exception.UnsupportedUpstreamRegistryException: <p>The specified upstream registry isn't supported.</p>
            capo_ecr.errors.validation_exception.ValidationException: <p>There was an exception validating this request.</p>
            capo_ecr.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_ecr.types.create_pull_through_cache_rule_request.CreatePullThroughCacheRuleRequest]",
        ) -> OperationResponse[
            "capo_ecr.types.create_pull_through_cache_rule_response.CreatePullThroughCacheRuleResponse"
        ]:
            import capo_ecr._operations.amazon_ec2_container_registry_v20150921.create_pull_through_cache_rule

            output, http_response = (
                capo_ecr._operations.amazon_ec2_container_registry_v20150921.create_pull_through_cache_rule.create_pull_through_cache_rule(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ecr.types.create_pull_through_cache_rule_request.CreatePullThroughCacheRuleRequest = {
            "ecr_repository_prefix": ecr_repository_prefix,
            "upstream_registry_url": upstream_registry_url,
        }
        if registry_id is not None:
            input_["registry_id"] = registry_id
        if upstream_registry is not None:
            input_["upstream_registry"] = upstream_registry
        if credential_arn is not None:
            input_["credential_arn"] = credential_arn
        if custom_role_arn is not None:
            input_["custom_role_arn"] = custom_role_arn
        if upstream_repository_prefix is not None:
            input_["upstream_repository_prefix"] = upstream_repository_prefix

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_repository(
        self,
        repository_name: "capo_ecr.types.repository_name.RepositoryName",
        *,
        config_overrides: Optional[ECRClientConfig] = None,
        registry_id: Optional["capo_ecr.types.registry_id.RegistryId"] = None,
        tags: Optional["capo_ecr.types.tag_list.TagList"] = None,
        image_tag_mutability: Optional[
            "capo_ecr.types.image_tag_mutability.ImageTagMutability"
        ] = None,
        image_tag_mutability_exclusion_filters: Optional[
            "capo_ecr.types.image_tag_mutability_exclusion_filters.ImageTagMutabilityExclusionFilters"
        ] = None,
        image_scanning_configuration: Optional[
            "capo_ecr.types.image_scanning_configuration.ImageScanningConfiguration"
        ] = None,
        encryption_configuration: Optional[
            "capo_ecr.types.encryption_configuration.EncryptionConfiguration"
        ] = None,
    ) -> "capo_ecr.types.create_repository_response.CreateRepositoryResponse":
        """<p>Creates a repository. For more information, see <a href="https://docs.aws.amazon.com/AmazonECR/latest/userguide/Repositories.html">Amazon ECR repositories</a> in the <i>Amazon Elastic Container Registry User Guide</i>.</p>

        Args:
            registry_id: <p>The Amazon Web Services account ID associated with the registry to create the repository. If you do not specify a registry, the default registry is assumed.</p>
            repository_name: <p>The name to use for the repository. The repository name may be specified on its own (such as <code>nginx-web-app</code>) or it can be prepended with a namespace to group the repository into a category (such as <code>project-a/nginx-web-app</code>).</p> <p>The repository name must start with a letter and can only contain lowercase letters, numbers, hyphens, underscores, and forward slashes.</p>
            tags: <p>The metadata that you apply to the repository to help you categorize and organize them. Each tag consists of a key and an optional value, both of which you define. Tag keys can have a maximum character length of 128 characters, and tag values can have a maximum length of 256 characters.</p>
            image_tag_mutability: <p>The tag mutability setting for the repository. If this parameter is omitted, the default setting of <code>MUTABLE</code> will be used which will allow image tags to be overwritten. If <code>IMMUTABLE</code> is specified, all image tags within the repository will be immutable which will prevent them from being overwritten.</p>
            image_tag_mutability_exclusion_filters: <p>A list of filters that specify which image tags should be excluded from the repository's image tag mutability setting.</p>
            image_scanning_configuration: <important> <p>The <code>imageScanningConfiguration</code> parameter is being deprecated, in favor of specifying the image scanning configuration at the registry level. For more information, see <code>PutRegistryScanningConfiguration</code>.</p> </important> <p>The image scanning configuration for the repository. This determines whether images are scanned for known vulnerabilities after being pushed to the repository.</p>
            encryption_configuration: <p>The encryption configuration for the repository. This determines how the contents of your repository are encrypted at rest.</p>

        Raises:
            capo_ecr.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter is invalid. Review the available parameters for the API request.</p>
            capo_ecr.errors.invalid_tag_parameter_exception.InvalidTagParameterException: <p>An invalid parameter has been specified. Tag keys can have a maximum character length of 128 characters, and tag values can have a maximum length of 256 characters.</p>
            capo_ecr.errors.kms_exception.KmsException: <p>The operation failed due to a KMS exception.</p>
            capo_ecr.errors.limit_exceeded_exception.LimitExceededException: <p>The operation did not succeed because it would have exceeded a service limit for your account. For more information, see <a href="https://docs.aws.amazon.com/AmazonECR/latest/userguide/service-quotas.html">Amazon ECR service quotas</a> in the Amazon Elastic Container Registry User Guide.</p>
            capo_ecr.errors.repository_already_exists_exception.RepositoryAlreadyExistsException: <p>The specified repository already exists in the specified registry.</p>
            capo_ecr.errors.server_exception.ServerException: <p>These errors are usually caused by a server-side issue.</p>
            capo_ecr.errors.too_many_tags_exception.TooManyTagsException: <p>The list of tags on the repository is over the limit. The maximum number of tags that can be applied to a repository is 50.</p>
            capo_ecr.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To create a new repository
            This example creates a repository called nginx-web-app inside the project-a namespace in the default registry for an account.

            >>> client.create_repository(repository_name='project-a/nginx-web-app')
        """

        def _handler(
            req: "OperationRequest[capo_ecr.types.create_repository_request.CreateRepositoryRequest]",
        ) -> OperationResponse[
            "capo_ecr.types.create_repository_response.CreateRepositoryResponse"
        ]:
            import capo_ecr._operations.amazon_ec2_container_registry_v20150921.create_repository

            output, http_response = (
                capo_ecr._operations.amazon_ec2_container_registry_v20150921.create_repository.create_repository(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ecr.types.create_repository_request.CreateRepositoryRequest = {
            "repository_name": repository_name
        }
        if registry_id is not None:
            input_["registry_id"] = registry_id
        if tags is not None:
            input_["tags"] = tags
        if image_tag_mutability is not None:
            input_["image_tag_mutability"] = image_tag_mutability
        if image_tag_mutability_exclusion_filters is not None:
            input_["image_tag_mutability_exclusion_filters"] = (
                image_tag_mutability_exclusion_filters
            )
        if image_scanning_configuration is not None:
            input_["image_scanning_configuration"] = image_scanning_configuration
        if encryption_configuration is not None:
            input_["encryption_configuration"] = encryption_configuration

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_repository_creation_template(
        self,
        prefix: "capo_ecr.types.prefix.Prefix",
        applied_for: "capo_ecr.types.rct_applied_for_list.RCTAppliedForList",
        *,
        config_overrides: Optional[ECRClientConfig] = None,
        description: Optional[
            "capo_ecr.types.repository_template_description.RepositoryTemplateDescription"
        ] = None,
        encryption_configuration: Optional[
            "capo_ecr.types.encryption_configuration_for_repository_creation_template.EncryptionConfigurationForRepositoryCreationTemplate"
        ] = None,
        resource_tags: Optional["capo_ecr.types.tag_list.TagList"] = None,
        image_tag_mutability: Optional[
            "capo_ecr.types.image_tag_mutability.ImageTagMutability"
        ] = None,
        image_tag_mutability_exclusion_filters: Optional[
            "capo_ecr.types.image_tag_mutability_exclusion_filters.ImageTagMutabilityExclusionFilters"
        ] = None,
        repository_policy: Optional[
            "capo_ecr.types.repository_policy_text.RepositoryPolicyText"
        ] = None,
        lifecycle_policy: Optional[
            "capo_ecr.types.lifecycle_policy_text_for_repository_creation_template.LifecyclePolicyTextForRepositoryCreationTemplate"
        ] = None,
        custom_role_arn: Optional[
            "capo_ecr.types.custom_role_arn.CustomRoleArn"
        ] = None,
    ) -> "capo_ecr.types.create_repository_creation_template_response.CreateRepositoryCreationTemplateResponse":
        """<p>Creates a repository creation template. This template is used to define the settings for repositories created by Amazon ECR on your behalf. For example, repositories created through pull through cache actions. For more information, see <a href="https://docs.aws.amazon.com/AmazonECR/latest/userguide/repository-creation-templates.html">Private repository creation templates</a> in the <i>Amazon Elastic Container Registry User Guide</i>.</p>

        Args:
            prefix: <p>The repository namespace prefix to associate with the template. All repositories created using this namespace prefix will have the settings defined in this template applied. For example, a prefix of <code>prod</code> would apply to all repositories beginning with <code>prod/</code>. Similarly, a prefix of <code>prod/team</code> would apply to all repositories beginning with <code>prod/team/</code>.</p> <p>To apply a template to all repositories in your registry that don't have an associated creation template, you can use <code>ROOT</code> as the prefix.</p> <important> <p>There is always an assumed <code>/</code> applied to the end of the prefix. If you specify <code>ecr-public</code> as the prefix, Amazon ECR treats that as <code>ecr-public/</code>. When using a pull through cache rule, the repository prefix you specify during rule creation is what you should specify as your repository creation template prefix as well.</p> </important>
            description: <p>A description for the repository creation template.</p>
            encryption_configuration: <p>The encryption configuration to use for repositories created using the template.</p>
            resource_tags: <p>The metadata to apply to the repository to help you categorize and organize. Each tag consists of a key and an optional value, both of which you define. Tag keys can have a maximum character length of 128 characters, and tag values can have a maximum length of 256 characters.</p>
            image_tag_mutability: <p>The tag mutability setting for the repository. If this parameter is omitted, the default setting of <code>MUTABLE</code> will be used which will allow image tags to be overwritten. If <code>IMMUTABLE</code> is specified, all image tags within the repository will be immutable which will prevent them from being overwritten.</p>
            image_tag_mutability_exclusion_filters: <p>A list of filters that specify which image tags should be excluded from the repository creation template's image tag mutability setting.</p>
            repository_policy: <p>The repository policy to apply to repositories created using the template. A repository policy is a permissions policy associated with a repository to control access permissions. </p>
            lifecycle_policy: <p>The lifecycle policy to use for repositories created using the template.</p>
            applied_for: <p>A list of enumerable strings representing the Amazon ECR repository creation scenarios that this template will apply towards. The supported scenarios are <code>PULL_THROUGH_CACHE</code>, <code>REPLICATION</code>, and <code>CREATE_ON_PUSH</code> </p>
            custom_role_arn: <p>The ARN of the role to be assumed by Amazon ECR. This role must be in the same account as the registry that you are configuring. Amazon ECR will assume your supplied role when the customRoleArn is specified. When this field isn't specified, Amazon ECR will use the service-linked role for the repository creation template.</p>

        Raises:
            capo_ecr.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter is invalid. Review the available parameters for the API request.</p>
            capo_ecr.errors.limit_exceeded_exception.LimitExceededException: <p>The operation did not succeed because it would have exceeded a service limit for your account. For more information, see <a href="https://docs.aws.amazon.com/AmazonECR/latest/userguide/service-quotas.html">Amazon ECR service quotas</a> in the Amazon Elastic Container Registry User Guide.</p>
            capo_ecr.errors.server_exception.ServerException: <p>These errors are usually caused by a server-side issue.</p>
            capo_ecr.errors.template_already_exists_exception.TemplateAlreadyExistsException: <p>The repository creation template already exists. Specify a unique prefix and try again.</p>
            capo_ecr.errors.validation_exception.ValidationException: <p>There was an exception validating this request.</p>
            capo_ecr.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_ecr.types.create_repository_creation_template_request.CreateRepositoryCreationTemplateRequest]",
        ) -> OperationResponse[
            "capo_ecr.types.create_repository_creation_template_response.CreateRepositoryCreationTemplateResponse"
        ]:
            import capo_ecr._operations.amazon_ec2_container_registry_v20150921.create_repository_creation_template

            output, http_response = (
                capo_ecr._operations.amazon_ec2_container_registry_v20150921.create_repository_creation_template.create_repository_creation_template(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ecr.types.create_repository_creation_template_request.CreateRepositoryCreationTemplateRequest = {
            "prefix": prefix,
            "applied_for": applied_for,
        }
        if description is not None:
            input_["description"] = description
        if encryption_configuration is not None:
            input_["encryption_configuration"] = encryption_configuration
        if resource_tags is not None:
            input_["resource_tags"] = resource_tags
        if image_tag_mutability is not None:
            input_["image_tag_mutability"] = image_tag_mutability
        if image_tag_mutability_exclusion_filters is not None:
            input_["image_tag_mutability_exclusion_filters"] = (
                image_tag_mutability_exclusion_filters
            )
        if repository_policy is not None:
            input_["repository_policy"] = repository_policy
        if lifecycle_policy is not None:
            input_["lifecycle_policy"] = lifecycle_policy
        if custom_role_arn is not None:
            input_["custom_role_arn"] = custom_role_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_lifecycle_policy(
        self,
        repository_name: "capo_ecr.types.repository_name.RepositoryName",
        *,
        config_overrides: Optional[ECRClientConfig] = None,
        registry_id: Optional["capo_ecr.types.registry_id.RegistryId"] = None,
    ) -> (
        "capo_ecr.types.delete_lifecycle_policy_response.DeleteLifecyclePolicyResponse"
    ):
        """<p>Deletes the lifecycle policy associated with the specified repository.</p>

        Args:
            registry_id: <p>The Amazon Web Services account ID associated with the registry that contains the repository. If you do not specify a registry, the default registry is assumed.</p>
            repository_name: <p>The name of the repository.</p>

        Raises:
            capo_ecr.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter is invalid. Review the available parameters for the API request.</p>
            capo_ecr.errors.lifecycle_policy_not_found_exception.LifecyclePolicyNotFoundException: <p>The lifecycle policy could not be found, and no policy is set to the repository.</p>
            capo_ecr.errors.repository_not_found_exception.RepositoryNotFoundException: <p>The specified repository could not be found. Check the spelling of the specified repository and ensure that you are performing operations on the correct registry.</p>
            capo_ecr.errors.server_exception.ServerException: <p>These errors are usually caused by a server-side issue.</p>
            capo_ecr.errors.validation_exception.ValidationException: <p>There was an exception validating this request.</p>
            capo_ecr.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_ecr.types.delete_lifecycle_policy_request.DeleteLifecyclePolicyRequest]",
        ) -> OperationResponse[
            "capo_ecr.types.delete_lifecycle_policy_response.DeleteLifecyclePolicyResponse"
        ]:
            import capo_ecr._operations.amazon_ec2_container_registry_v20150921.delete_lifecycle_policy

            output, http_response = (
                capo_ecr._operations.amazon_ec2_container_registry_v20150921.delete_lifecycle_policy.delete_lifecycle_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ecr.types.delete_lifecycle_policy_request.DeleteLifecyclePolicyRequest = {
            "repository_name": repository_name
        }
        if registry_id is not None:
            input_["registry_id"] = registry_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_pull_through_cache_rule(
        self,
        ecr_repository_prefix: "capo_ecr.types.pull_through_cache_rule_repository_prefix.PullThroughCacheRuleRepositoryPrefix",
        *,
        config_overrides: Optional[ECRClientConfig] = None,
        registry_id: Optional["capo_ecr.types.registry_id.RegistryId"] = None,
    ) -> "capo_ecr.types.delete_pull_through_cache_rule_response.DeletePullThroughCacheRuleResponse":
        """<p>Deletes a pull through cache rule.</p>

        Args:
            ecr_repository_prefix: <p>The Amazon ECR repository prefix associated with the pull through cache rule to delete.</p>
            registry_id: <p>The Amazon Web Services account ID associated with the registry that contains the pull through cache rule. If you do not specify a registry, the default registry is assumed.</p>

        Raises:
            capo_ecr.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter is invalid. Review the available parameters for the API request.</p>
            capo_ecr.errors.pull_through_cache_rule_not_found_exception.PullThroughCacheRuleNotFoundException: <p>The pull through cache rule was not found. Specify a valid pull through cache rule and try again.</p>
            capo_ecr.errors.server_exception.ServerException: <p>These errors are usually caused by a server-side issue.</p>
            capo_ecr.errors.validation_exception.ValidationException: <p>There was an exception validating this request.</p>
            capo_ecr.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_ecr.types.delete_pull_through_cache_rule_request.DeletePullThroughCacheRuleRequest]",
        ) -> OperationResponse[
            "capo_ecr.types.delete_pull_through_cache_rule_response.DeletePullThroughCacheRuleResponse"
        ]:
            import capo_ecr._operations.amazon_ec2_container_registry_v20150921.delete_pull_through_cache_rule

            output, http_response = (
                capo_ecr._operations.amazon_ec2_container_registry_v20150921.delete_pull_through_cache_rule.delete_pull_through_cache_rule(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ecr.types.delete_pull_through_cache_rule_request.DeletePullThroughCacheRuleRequest = {
            "ecr_repository_prefix": ecr_repository_prefix
        }
        if registry_id is not None:
            input_["registry_id"] = registry_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_registry_policy(
        self, *, config_overrides: Optional[ECRClientConfig] = None
    ) -> "capo_ecr.types.delete_registry_policy_response.DeleteRegistryPolicyResponse":
        """<p>Deletes the registry permissions policy.</p>

        Raises:
            capo_ecr.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter is invalid. Review the available parameters for the API request.</p>
            capo_ecr.errors.registry_policy_not_found_exception.RegistryPolicyNotFoundException: <p>The registry doesn't have an associated registry policy.</p>
            capo_ecr.errors.server_exception.ServerException: <p>These errors are usually caused by a server-side issue.</p>
            capo_ecr.errors.validation_exception.ValidationException: <p>There was an exception validating this request.</p>
            capo_ecr.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_ecr.types.delete_registry_policy_request.DeleteRegistryPolicyRequest]",
        ) -> OperationResponse[
            "capo_ecr.types.delete_registry_policy_response.DeleteRegistryPolicyResponse"
        ]:
            import capo_ecr._operations.amazon_ec2_container_registry_v20150921.delete_registry_policy

            output, http_response = (
                capo_ecr._operations.amazon_ec2_container_registry_v20150921.delete_registry_policy.delete_registry_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ecr.types.delete_registry_policy_request.DeleteRegistryPolicyRequest = {}

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_repository(
        self,
        repository_name: "capo_ecr.types.repository_name.RepositoryName",
        *,
        config_overrides: Optional[ECRClientConfig] = None,
        registry_id: Optional["capo_ecr.types.registry_id.RegistryId"] = None,
        force: Optional["capo_ecr.types.force_flag.ForceFlag"] = None,
    ) -> "capo_ecr.types.delete_repository_response.DeleteRepositoryResponse":
        """<p>Deletes a repository. If the repository isn't empty, you must either delete the contents of the repository or use the <code>force</code> option to delete the repository and have Amazon ECR delete all of its contents on your behalf.</p>

        Args:
            registry_id: <p>The Amazon Web Services account ID associated with the registry that contains the repository to delete. If you do not specify a registry, the default registry is assumed.</p>
            repository_name: <p>The name of the repository to delete.</p>
            force: <p>If true, deleting the repository force deletes the contents of the repository. If false, the repository must be empty before attempting to delete it.</p>

        Raises:
            capo_ecr.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter is invalid. Review the available parameters for the API request.</p>
            capo_ecr.errors.kms_exception.KmsException: <p>The operation failed due to a KMS exception.</p>
            capo_ecr.errors.repository_not_empty_exception.RepositoryNotEmptyException: <p>The specified repository contains images. To delete a repository that contains images, you must force the deletion with the <code>force</code> parameter.</p>
            capo_ecr.errors.repository_not_found_exception.RepositoryNotFoundException: <p>The specified repository could not be found. Check the spelling of the specified repository and ensure that you are performing operations on the correct registry.</p>
            capo_ecr.errors.server_exception.ServerException: <p>These errors are usually caused by a server-side issue.</p>
            capo_ecr.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To force delete a repository
            This example force deletes a repository named ubuntu in the default registry for an account. The force parameter is required if the repository contains images.

            >>> client.delete_repository(repository_name='ubuntu', force=True)
        """

        def _handler(
            req: "OperationRequest[capo_ecr.types.delete_repository_request.DeleteRepositoryRequest]",
        ) -> OperationResponse[
            "capo_ecr.types.delete_repository_response.DeleteRepositoryResponse"
        ]:
            import capo_ecr._operations.amazon_ec2_container_registry_v20150921.delete_repository

            output, http_response = (
                capo_ecr._operations.amazon_ec2_container_registry_v20150921.delete_repository.delete_repository(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ecr.types.delete_repository_request.DeleteRepositoryRequest = {
            "repository_name": repository_name
        }
        if registry_id is not None:
            input_["registry_id"] = registry_id
        if force is not None:
            input_["force"] = force

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_repository_creation_template(
        self,
        prefix: "capo_ecr.types.prefix.Prefix",
        *,
        config_overrides: Optional[ECRClientConfig] = None,
    ) -> "capo_ecr.types.delete_repository_creation_template_response.DeleteRepositoryCreationTemplateResponse":
        """<p>Deletes a repository creation template.</p>

        Args:
            prefix: <p>The repository namespace prefix associated with the repository creation template.</p>

        Raises:
            capo_ecr.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter is invalid. Review the available parameters for the API request.</p>
            capo_ecr.errors.server_exception.ServerException: <p>These errors are usually caused by a server-side issue.</p>
            capo_ecr.errors.template_not_found_exception.TemplateNotFoundException: <p>The specified repository creation template can't be found. Verify the registry ID and prefix and try again.</p>
            capo_ecr.errors.validation_exception.ValidationException: <p>There was an exception validating this request.</p>
            capo_ecr.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_ecr.types.delete_repository_creation_template_request.DeleteRepositoryCreationTemplateRequest]",
        ) -> OperationResponse[
            "capo_ecr.types.delete_repository_creation_template_response.DeleteRepositoryCreationTemplateResponse"
        ]:
            import capo_ecr._operations.amazon_ec2_container_registry_v20150921.delete_repository_creation_template

            output, http_response = (
                capo_ecr._operations.amazon_ec2_container_registry_v20150921.delete_repository_creation_template.delete_repository_creation_template(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ecr.types.delete_repository_creation_template_request.DeleteRepositoryCreationTemplateRequest = {
            "prefix": prefix
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_repository_policy(
        self,
        repository_name: "capo_ecr.types.repository_name.RepositoryName",
        *,
        config_overrides: Optional[ECRClientConfig] = None,
        registry_id: Optional["capo_ecr.types.registry_id.RegistryId"] = None,
    ) -> "capo_ecr.types.delete_repository_policy_response.DeleteRepositoryPolicyResponse":
        """<p>Deletes the repository policy associated with the specified repository.</p>

        Args:
            registry_id: <p>The Amazon Web Services account ID associated with the registry that contains the repository policy to delete. If you do not specify a registry, the default registry is assumed.</p>
            repository_name: <p>The name of the repository that is associated with the repository policy to delete.</p>

        Raises:
            capo_ecr.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter is invalid. Review the available parameters for the API request.</p>
            capo_ecr.errors.repository_not_found_exception.RepositoryNotFoundException: <p>The specified repository could not be found. Check the spelling of the specified repository and ensure that you are performing operations on the correct registry.</p>
            capo_ecr.errors.repository_policy_not_found_exception.RepositoryPolicyNotFoundException: <p>The specified repository and registry combination does not have an associated repository policy.</p>
            capo_ecr.errors.server_exception.ServerException: <p>These errors are usually caused by a server-side issue.</p>
            capo_ecr.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To delete the policy associated with a repository
            This example deletes the policy associated with the repository named ubuntu in the current account.

            >>> client.delete_repository_policy(repository_name='ubuntu')
        """

        def _handler(
            req: "OperationRequest[capo_ecr.types.delete_repository_policy_request.DeleteRepositoryPolicyRequest]",
        ) -> OperationResponse[
            "capo_ecr.types.delete_repository_policy_response.DeleteRepositoryPolicyResponse"
        ]:
            import capo_ecr._operations.amazon_ec2_container_registry_v20150921.delete_repository_policy

            output, http_response = (
                capo_ecr._operations.amazon_ec2_container_registry_v20150921.delete_repository_policy.delete_repository_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ecr.types.delete_repository_policy_request.DeleteRepositoryPolicyRequest = {
            "repository_name": repository_name
        }
        if registry_id is not None:
            input_["registry_id"] = registry_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_signing_configuration(
        self, *, config_overrides: Optional[ECRClientConfig] = None
    ) -> "capo_ecr.types.delete_signing_configuration_response.DeleteSigningConfigurationResponse":
        """<p>Deletes the registry's signing configuration. Images pushed after deletion of the signing configuration will no longer be automatically signed.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/AmazonECR/latest/userguide/managed-signing.html">Managed signing</a> in the <i>Amazon Elastic Container Registry User Guide</i>.</p> <note> <p>Deleting the signing configuration does not affect existing image signatures.</p> </note>

        Raises:
            capo_ecr.errors.server_exception.ServerException: <p>These errors are usually caused by a server-side issue.</p>
            capo_ecr.errors.signing_configuration_not_found_exception.SigningConfigurationNotFoundException: <p>The specified signing configuration was not found. This occurs when attempting to retrieve or delete a signing configuration that does not exist.</p>
            capo_ecr.errors.validation_exception.ValidationException: <p>There was an exception validating this request.</p>
            capo_ecr.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_ecr.types.delete_signing_configuration_request.DeleteSigningConfigurationRequest]",
        ) -> OperationResponse[
            "capo_ecr.types.delete_signing_configuration_response.DeleteSigningConfigurationResponse"
        ]:
            import capo_ecr._operations.amazon_ec2_container_registry_v20150921.delete_signing_configuration

            output, http_response = (
                capo_ecr._operations.amazon_ec2_container_registry_v20150921.delete_signing_configuration.delete_signing_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ecr.types.delete_signing_configuration_request.DeleteSigningConfigurationRequest = {}

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def deregister_pull_time_update_exclusion(
        self,
        principal_arn: "capo_ecr.types.principal_arn.PrincipalArn",
        *,
        config_overrides: Optional[ECRClientConfig] = None,
    ) -> "capo_ecr.types.deregister_pull_time_update_exclusion_response.DeregisterPullTimeUpdateExclusionResponse":
        """<p>Removes a principal from the pull time update exclusion list for a registry. Once removed, Amazon ECR will resume updating the pull time if the specified principal pulls an image.</p>

        Args:
            principal_arn: <p>The ARN of the IAM principal to remove from the pull time update exclusion list.</p>

        Raises:
            capo_ecr.errors.exclusion_not_found_exception.ExclusionNotFoundException: <p>The specified pull time update exclusion was not found.</p>
            capo_ecr.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter is invalid. Review the available parameters for the API request.</p>
            capo_ecr.errors.limit_exceeded_exception.LimitExceededException: <p>The operation did not succeed because it would have exceeded a service limit for your account. For more information, see <a href="https://docs.aws.amazon.com/AmazonECR/latest/userguide/service-quotas.html">Amazon ECR service quotas</a> in the Amazon Elastic Container Registry User Guide.</p>
            capo_ecr.errors.server_exception.ServerException: <p>These errors are usually caused by a server-side issue.</p>
            capo_ecr.errors.validation_exception.ValidationException: <p>There was an exception validating this request.</p>
            capo_ecr.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To remove a principal from the pull time exclusion list
            This example removes an IAM role from the pull time update exclusion list. Amazon ECR will resume recording image pull timestamps for this principal.

            >>> client.deregister_pull_time_update_exclusion(principal_arn='arn:aws:iam::012345678910:role/ECRAccess')
        """

        def _handler(
            req: "OperationRequest[capo_ecr.types.deregister_pull_time_update_exclusion_request.DeregisterPullTimeUpdateExclusionRequest]",
        ) -> OperationResponse[
            "capo_ecr.types.deregister_pull_time_update_exclusion_response.DeregisterPullTimeUpdateExclusionResponse"
        ]:
            import capo_ecr._operations.amazon_ec2_container_registry_v20150921.deregister_pull_time_update_exclusion

            output, http_response = (
                capo_ecr._operations.amazon_ec2_container_registry_v20150921.deregister_pull_time_update_exclusion.deregister_pull_time_update_exclusion(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ecr.types.deregister_pull_time_update_exclusion_request.DeregisterPullTimeUpdateExclusionRequest = {
            "principal_arn": principal_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_image_replication_status(
        self,
        repository_name: "capo_ecr.types.repository_name.RepositoryName",
        image_id: "capo_ecr.types.image_identifier.ImageIdentifier",
        *,
        config_overrides: Optional[ECRClientConfig] = None,
        registry_id: Optional["capo_ecr.types.registry_id.RegistryId"] = None,
    ) -> "capo_ecr.types.describe_image_replication_status_response.DescribeImageReplicationStatusResponse":
        """<p>Returns the replication status for a specified image.</p>

        Args:
            repository_name: <p>The name of the repository that the image is in.</p>
            registry_id: <p>The Amazon Web Services account ID associated with the registry. If you do not specify a registry, the default registry is assumed.</p>

        Raises:
            capo_ecr.errors.image_not_found_exception.ImageNotFoundException: <p>The image requested does not exist in the specified repository.</p>
            capo_ecr.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter is invalid. Review the available parameters for the API request.</p>
            capo_ecr.errors.repository_not_found_exception.RepositoryNotFoundException: <p>The specified repository could not be found. Check the spelling of the specified repository and ensure that you are performing operations on the correct registry.</p>
            capo_ecr.errors.server_exception.ServerException: <p>These errors are usually caused by a server-side issue.</p>
            capo_ecr.errors.validation_exception.ValidationException: <p>There was an exception validating this request.</p>
            capo_ecr.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_ecr.types.describe_image_replication_status_request.DescribeImageReplicationStatusRequest]",
        ) -> OperationResponse[
            "capo_ecr.types.describe_image_replication_status_response.DescribeImageReplicationStatusResponse"
        ]:
            import capo_ecr._operations.amazon_ec2_container_registry_v20150921.describe_image_replication_status

            output, http_response = (
                capo_ecr._operations.amazon_ec2_container_registry_v20150921.describe_image_replication_status.describe_image_replication_status(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ecr.types.describe_image_replication_status_request.DescribeImageReplicationStatusRequest = {
            "repository_name": repository_name,
            "image_id": image_id,
        }
        if registry_id is not None:
            input_["registry_id"] = registry_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_images(
        self,
        repository_name: "capo_ecr.types.repository_name.RepositoryName",
        *,
        config_overrides: Optional[ECRClientConfig] = None,
        registry_id: Optional["capo_ecr.types.registry_id.RegistryId"] = None,
        image_ids: Optional[
            "capo_ecr.types.image_identifier_list.ImageIdentifierList"
        ] = None,
        next_token: Optional["capo_ecr.types.next_token.NextToken"] = None,
        max_results: Optional["capo_ecr.types.max_results.MaxResults"] = None,
        filter: Optional[
            "capo_ecr.types.describe_images_filter.DescribeImagesFilter"
        ] = None,
    ) -> "capo_ecr.types.describe_images_response.DescribeImagesResponse":
        """<p>Returns metadata about the images in a repository.</p> <note> <p>Starting with Docker version 1.9, the Docker client compresses image layers before pushing them to a V2 Docker registry. The output of the <code>docker images</code> command shows the uncompressed image size. Therefore, Docker might return a larger image than the image shown in the Amazon Web Services Management Console.</p> </note> <important> <p>The new version of Amazon ECR <i>Basic Scanning</i> doesn't use the <a>ImageDetail$imageScanFindingsSummary</a> and <a>ImageDetail$imageScanStatus</a> attributes from the API response to return scan results. Use the <a>DescribeImageScanFindings</a> API instead. For more information about Amazon Web Services native basic scanning, see <a href="https://docs.aws.amazon.com/AmazonECR/latest/userguide/image-scanning.html"> Scan images for software vulnerabilities in Amazon ECR</a>.</p> </important>

        Args:
            registry_id: <p>The Amazon Web Services account ID associated with the registry that contains the repository in which to describe images. If you do not specify a registry, the default registry is assumed.</p>
            repository_name: <p>The repository that contains the images to describe.</p>
            image_ids: <p>The list of image IDs for the requested repository.</p>
            next_token: <p>The <code>nextToken</code> value returned from a previous paginated <code>DescribeImages</code> request where <code>maxResults</code> was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the <code>nextToken</code> value. This value is <code>null</code> when there are no more results to return. This option cannot be used when you specify images with <code>imageIds</code>.</p>
            max_results: <p>The maximum number of repository results returned by <code>DescribeImages</code> in paginated output. When this parameter is used, <code>DescribeImages</code> only returns <code>maxResults</code> results in a single page along with a <code>nextToken</code> response element. The remaining results of the initial request can be seen by sending another <code>DescribeImages</code> request with the returned <code>nextToken</code> value. This value can be between 1 and 1000. If this parameter is not used, then <code>DescribeImages</code> returns up to 100 results and a <code>nextToken</code> value, if applicable. This option cannot be used when you specify images with <code>imageIds</code>.</p>
            filter: <p>The filter key and value with which to filter your <code>DescribeImages</code> results.</p>

        Raises:
            capo_ecr.errors.image_not_found_exception.ImageNotFoundException: <p>The image requested does not exist in the specified repository.</p>
            capo_ecr.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter is invalid. Review the available parameters for the API request.</p>
            capo_ecr.errors.repository_not_found_exception.RepositoryNotFoundException: <p>The specified repository could not be found. Check the spelling of the specified repository and ensure that you are performing operations on the correct registry.</p>
            capo_ecr.errors.server_exception.ServerException: <p>These errors are usually caused by a server-side issue.</p>
            capo_ecr.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_ecr.types.describe_images_request.DescribeImagesRequest]",
        ) -> OperationResponse[
            "capo_ecr.types.describe_images_response.DescribeImagesResponse"
        ]:
            import capo_ecr._operations.amazon_ec2_container_registry_v20150921.describe_images

            output, http_response = (
                capo_ecr._operations.amazon_ec2_container_registry_v20150921.describe_images.describe_images(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ecr.types.describe_images_request.DescribeImagesRequest = {
            "repository_name": repository_name
        }
        if registry_id is not None:
            input_["registry_id"] = registry_id
        if image_ids is not None:
            input_["image_ids"] = image_ids
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if filter is not None:
            input_["filter"] = filter

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_describe_images(
        self,
        repository_name: "capo_ecr.types.repository_name.RepositoryName",
        *,
        config_overrides: Optional[ECRClientConfig] = None,
        registry_id: Optional["capo_ecr.types.registry_id.RegistryId"] = None,
        image_ids: Optional[
            "capo_ecr.types.image_identifier_list.ImageIdentifierList"
        ] = None,
        next_token: Optional["capo_ecr.types.next_token.NextToken"] = None,
        max_results: Optional["capo_ecr.types.max_results.MaxResults"] = None,
        filter: Optional[
            "capo_ecr.types.describe_images_filter.DescribeImagesFilter"
        ] = None,
    ) -> "Iterator[capo_ecr.types.image_detail.ImageDetail]":
        _token = next_token
        while True:
            _response = self.describe_images(
                repository_name,
                config_overrides=config_overrides,
                registry_id=registry_id,
                image_ids=image_ids,
                next_token=_token,
                max_results=max_results,
                filter=filter,
            )
            _page = _resolve_path(_response, ("image_details",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def describe_image_scan_findings(
        self,
        repository_name: "capo_ecr.types.repository_name.RepositoryName",
        image_id: "capo_ecr.types.image_identifier.ImageIdentifier",
        *,
        config_overrides: Optional[ECRClientConfig] = None,
        registry_id: Optional["capo_ecr.types.registry_id.RegistryId"] = None,
        next_token: Optional["capo_ecr.types.next_token.NextToken"] = None,
        max_results: Optional["capo_ecr.types.max_results.MaxResults"] = None,
    ) -> "capo_ecr.types.describe_image_scan_findings_response.DescribeImageScanFindingsResponse":
        """<p>Returns the scan findings for the specified image.</p>

        Args:
            registry_id: <p>The Amazon Web Services account ID associated with the registry that contains the repository in which to describe the image scan findings for. If you do not specify a registry, the default registry is assumed.</p>
            repository_name: <p>The repository for the image for which to describe the scan findings.</p>
            next_token: <p>The <code>nextToken</code> value returned from a previous paginated <code>DescribeImageScanFindings</code> request where <code>maxResults</code> was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the <code>nextToken</code> value. This value is null when there are no more results to return.</p>
            max_results: <p>The maximum number of image scan results returned by <code>DescribeImageScanFindings</code> in paginated output. When this parameter is used, <code>DescribeImageScanFindings</code> only returns <code>maxResults</code> results in a single page along with a <code>nextToken</code> response element. The remaining results of the initial request can be seen by sending another <code>DescribeImageScanFindings</code> request with the returned <code>nextToken</code> value. This value can be between 1 and 1000. If this parameter is not used, then <code>DescribeImageScanFindings</code> returns up to 100 results and a <code>nextToken</code> value, if applicable.</p>

        Raises:
            capo_ecr.errors.image_not_found_exception.ImageNotFoundException: <p>The image requested does not exist in the specified repository.</p>
            capo_ecr.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter is invalid. Review the available parameters for the API request.</p>
            capo_ecr.errors.repository_not_found_exception.RepositoryNotFoundException: <p>The specified repository could not be found. Check the spelling of the specified repository and ensure that you are performing operations on the correct registry.</p>
            capo_ecr.errors.scan_not_found_exception.ScanNotFoundException: <p>The specified image scan could not be found. Ensure that image scanning is enabled on the repository and try again.</p>
            capo_ecr.errors.server_exception.ServerException: <p>These errors are usually caused by a server-side issue.</p>
            capo_ecr.errors.validation_exception.ValidationException: <p>There was an exception validating this request.</p>
            capo_ecr.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_ecr.types.describe_image_scan_findings_request.DescribeImageScanFindingsRequest]",
        ) -> OperationResponse[
            "capo_ecr.types.describe_image_scan_findings_response.DescribeImageScanFindingsResponse"
        ]:
            import capo_ecr._operations.amazon_ec2_container_registry_v20150921.describe_image_scan_findings

            output, http_response = (
                capo_ecr._operations.amazon_ec2_container_registry_v20150921.describe_image_scan_findings.describe_image_scan_findings(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ecr.types.describe_image_scan_findings_request.DescribeImageScanFindingsRequest = {
            "repository_name": repository_name,
            "image_id": image_id,
        }
        if registry_id is not None:
            input_["registry_id"] = registry_id
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_describe_image_scan_findings(
        self,
        repository_name: "capo_ecr.types.repository_name.RepositoryName",
        image_id: "capo_ecr.types.image_identifier.ImageIdentifier",
        *,
        config_overrides: Optional[ECRClientConfig] = None,
        registry_id: Optional["capo_ecr.types.registry_id.RegistryId"] = None,
        next_token: Optional["capo_ecr.types.next_token.NextToken"] = None,
        max_results: Optional["capo_ecr.types.max_results.MaxResults"] = None,
    ) -> "Iterator[capo_ecr.types.describe_image_scan_findings_response.DescribeImageScanFindingsResponse]":
        _token = next_token
        while True:
            _response = self.describe_image_scan_findings(
                repository_name,
                image_id,
                config_overrides=config_overrides,
                registry_id=registry_id,
                next_token=_token,
                max_results=max_results,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def describe_image_signing_status(
        self,
        repository_name: "capo_ecr.types.repository_name.RepositoryName",
        image_id: "capo_ecr.types.image_identifier.ImageIdentifier",
        *,
        config_overrides: Optional[ECRClientConfig] = None,
        registry_id: Optional["capo_ecr.types.registry_id.RegistryId"] = None,
    ) -> "capo_ecr.types.describe_image_signing_status_response.DescribeImageSigningStatusResponse":
        """<p>Returns the signing status for a specified image. If the image matched signing rules that reference different signing profiles, a status is returned for each profile.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/AmazonECR/latest/userguide/managed-signing.html">Managed signing</a> in the <i>Amazon Elastic Container Registry User Guide</i>.</p>

        Args:
            repository_name: <p>The name of the repository that contains the image.</p>
            image_id: <p>An object containing identifying information for an image.</p>
            registry_id: <p>The Amazon Web Services account ID associated with the registry that contains the repository. If you do not specify a registry, the default registry is assumed.</p>

        Raises:
            capo_ecr.errors.image_not_found_exception.ImageNotFoundException: <p>The image requested does not exist in the specified repository.</p>
            capo_ecr.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter is invalid. Review the available parameters for the API request.</p>
            capo_ecr.errors.repository_not_found_exception.RepositoryNotFoundException: <p>The specified repository could not be found. Check the spelling of the specified repository and ensure that you are performing operations on the correct registry.</p>
            capo_ecr.errors.server_exception.ServerException: <p>These errors are usually caused by a server-side issue.</p>
            capo_ecr.errors.validation_exception.ValidationException: <p>There was an exception validating this request.</p>
            capo_ecr.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_ecr.types.describe_image_signing_status_request.DescribeImageSigningStatusRequest]",
        ) -> OperationResponse[
            "capo_ecr.types.describe_image_signing_status_response.DescribeImageSigningStatusResponse"
        ]:
            import capo_ecr._operations.amazon_ec2_container_registry_v20150921.describe_image_signing_status

            output, http_response = (
                capo_ecr._operations.amazon_ec2_container_registry_v20150921.describe_image_signing_status.describe_image_signing_status(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ecr.types.describe_image_signing_status_request.DescribeImageSigningStatusRequest = {
            "repository_name": repository_name,
            "image_id": image_id,
        }
        if registry_id is not None:
            input_["registry_id"] = registry_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_pull_through_cache_rules(
        self,
        *,
        config_overrides: Optional[ECRClientConfig] = None,
        registry_id: Optional["capo_ecr.types.registry_id.RegistryId"] = None,
        ecr_repository_prefixes: Optional[
            "capo_ecr.types.pull_through_cache_rule_repository_prefix_list.PullThroughCacheRuleRepositoryPrefixList"
        ] = None,
        next_token: Optional["capo_ecr.types.next_token.NextToken"] = None,
        max_results: Optional["capo_ecr.types.max_results.MaxResults"] = None,
    ) -> "capo_ecr.types.describe_pull_through_cache_rules_response.DescribePullThroughCacheRulesResponse":
        """<p>Returns the pull through cache rules for a registry.</p>

        Args:
            registry_id: <p>The Amazon Web Services account ID associated with the registry to return the pull through cache rules for. If you do not specify a registry, the default registry is assumed.</p>
            ecr_repository_prefixes: <p>The Amazon ECR repository prefixes associated with the pull through cache rules to return. If no repository prefix value is specified, all pull through cache rules are returned.</p>
            next_token: <p>The <code>nextToken</code> value returned from a previous paginated <code>DescribePullThroughCacheRulesRequest</code> request where <code>maxResults</code> was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the <code>nextToken</code> value. This value is null when there are no more results to return.</p>
            max_results: <p>The maximum number of pull through cache rules returned by <code>DescribePullThroughCacheRulesRequest</code> in paginated output. When this parameter is used, <code>DescribePullThroughCacheRulesRequest</code> only returns <code>maxResults</code> results in a single page along with a <code>nextToken</code> response element. The remaining results of the initial request can be seen by sending another <code>DescribePullThroughCacheRulesRequest</code> request with the returned <code>nextToken</code> value. This value can be between 1 and 1000. If this parameter is not used, then <code>DescribePullThroughCacheRulesRequest</code> returns up to 100 results and a <code>nextToken</code> value, if applicable.</p>

        Raises:
            capo_ecr.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter is invalid. Review the available parameters for the API request.</p>
            capo_ecr.errors.pull_through_cache_rule_not_found_exception.PullThroughCacheRuleNotFoundException: <p>The pull through cache rule was not found. Specify a valid pull through cache rule and try again.</p>
            capo_ecr.errors.server_exception.ServerException: <p>These errors are usually caused by a server-side issue.</p>
            capo_ecr.errors.validation_exception.ValidationException: <p>There was an exception validating this request.</p>
            capo_ecr.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_ecr.types.describe_pull_through_cache_rules_request.DescribePullThroughCacheRulesRequest]",
        ) -> OperationResponse[
            "capo_ecr.types.describe_pull_through_cache_rules_response.DescribePullThroughCacheRulesResponse"
        ]:
            import capo_ecr._operations.amazon_ec2_container_registry_v20150921.describe_pull_through_cache_rules

            output, http_response = (
                capo_ecr._operations.amazon_ec2_container_registry_v20150921.describe_pull_through_cache_rules.describe_pull_through_cache_rules(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ecr.types.describe_pull_through_cache_rules_request.DescribePullThroughCacheRulesRequest = {}
        if registry_id is not None:
            input_["registry_id"] = registry_id
        if ecr_repository_prefixes is not None:
            input_["ecr_repository_prefixes"] = ecr_repository_prefixes
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_describe_pull_through_cache_rules(
        self,
        *,
        config_overrides: Optional[ECRClientConfig] = None,
        registry_id: Optional["capo_ecr.types.registry_id.RegistryId"] = None,
        ecr_repository_prefixes: Optional[
            "capo_ecr.types.pull_through_cache_rule_repository_prefix_list.PullThroughCacheRuleRepositoryPrefixList"
        ] = None,
        next_token: Optional["capo_ecr.types.next_token.NextToken"] = None,
        max_results: Optional["capo_ecr.types.max_results.MaxResults"] = None,
    ) -> "Iterator[capo_ecr.types.pull_through_cache_rule.PullThroughCacheRule]":
        _token = next_token
        while True:
            _response = self.describe_pull_through_cache_rules(
                config_overrides=config_overrides,
                registry_id=registry_id,
                ecr_repository_prefixes=ecr_repository_prefixes,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("pull_through_cache_rules",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def describe_registry(
        self, *, config_overrides: Optional[ECRClientConfig] = None
    ) -> "capo_ecr.types.describe_registry_response.DescribeRegistryResponse":
        """<p>Describes the settings for a registry. The replication configuration for a repository can be created or updated with the <a>PutReplicationConfiguration</a> API action.</p>

        Raises:
            capo_ecr.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter is invalid. Review the available parameters for the API request.</p>
            capo_ecr.errors.server_exception.ServerException: <p>These errors are usually caused by a server-side issue.</p>
            capo_ecr.errors.validation_exception.ValidationException: <p>There was an exception validating this request.</p>
            capo_ecr.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_ecr.types.describe_registry_request.DescribeRegistryRequest]",
        ) -> OperationResponse[
            "capo_ecr.types.describe_registry_response.DescribeRegistryResponse"
        ]:
            import capo_ecr._operations.amazon_ec2_container_registry_v20150921.describe_registry

            output, http_response = (
                capo_ecr._operations.amazon_ec2_container_registry_v20150921.describe_registry.describe_registry(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ecr.types.describe_registry_request.DescribeRegistryRequest = {}

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_repositories(
        self,
        *,
        config_overrides: Optional[ECRClientConfig] = None,
        registry_id: Optional["capo_ecr.types.registry_id.RegistryId"] = None,
        repository_names: Optional[
            "capo_ecr.types.repository_name_list.RepositoryNameList"
        ] = None,
        next_token: Optional["capo_ecr.types.next_token.NextToken"] = None,
        max_results: Optional["capo_ecr.types.max_results.MaxResults"] = None,
    ) -> "capo_ecr.types.describe_repositories_response.DescribeRepositoriesResponse":
        """<p>Describes image repositories in a registry.</p>

        Args:
            registry_id: <p>The Amazon Web Services account ID associated with the registry that contains the repositories to be described. If you do not specify a registry, the default registry is assumed.</p>
            repository_names: <p>A list of repositories to describe. If this parameter is omitted, then all repositories in a registry are described.</p>
            next_token: <p>The <code>nextToken</code> value returned from a previous paginated <code>DescribeRepositories</code> request where <code>maxResults</code> was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the <code>nextToken</code> value. This value is <code>null</code> when there are no more results to return. This option cannot be used when you specify repositories with <code>repositoryNames</code>.</p> <note> <p>This token should be treated as an opaque identifier that is only used to retrieve the next items in a list and not for other programmatic purposes.</p> </note>
            max_results: <p>The maximum number of repository results returned by <code>DescribeRepositories</code> in paginated output. When this parameter is used, <code>DescribeRepositories</code> only returns <code>maxResults</code> results in a single page along with a <code>nextToken</code> response element. The remaining results of the initial request can be seen by sending another <code>DescribeRepositories</code> request with the returned <code>nextToken</code> value. This value can be between 1 and 1000. If this parameter is not used, then <code>DescribeRepositories</code> returns up to 100 results and a <code>nextToken</code> value, if applicable. This option cannot be used when you specify repositories with <code>repositoryNames</code>.</p>

        Raises:
            capo_ecr.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter is invalid. Review the available parameters for the API request.</p>
            capo_ecr.errors.repository_not_found_exception.RepositoryNotFoundException: <p>The specified repository could not be found. Check the spelling of the specified repository and ensure that you are performing operations on the correct registry.</p>
            capo_ecr.errors.server_exception.ServerException: <p>These errors are usually caused by a server-side issue.</p>
            capo_ecr.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To describe all repositories in the current account
            The following example obtains a list and description of all repositories in the default registry to which the current user has access.

            >>> client.describe_repositories()
        """

        def _handler(
            req: "OperationRequest[capo_ecr.types.describe_repositories_request.DescribeRepositoriesRequest]",
        ) -> OperationResponse[
            "capo_ecr.types.describe_repositories_response.DescribeRepositoriesResponse"
        ]:
            import capo_ecr._operations.amazon_ec2_container_registry_v20150921.describe_repositories

            output, http_response = (
                capo_ecr._operations.amazon_ec2_container_registry_v20150921.describe_repositories.describe_repositories(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ecr.types.describe_repositories_request.DescribeRepositoriesRequest = {}
        if registry_id is not None:
            input_["registry_id"] = registry_id
        if repository_names is not None:
            input_["repository_names"] = repository_names
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_describe_repositories(
        self,
        *,
        config_overrides: Optional[ECRClientConfig] = None,
        registry_id: Optional["capo_ecr.types.registry_id.RegistryId"] = None,
        repository_names: Optional[
            "capo_ecr.types.repository_name_list.RepositoryNameList"
        ] = None,
        next_token: Optional["capo_ecr.types.next_token.NextToken"] = None,
        max_results: Optional["capo_ecr.types.max_results.MaxResults"] = None,
    ) -> "Iterator[capo_ecr.types.repository.Repository]":
        _token = next_token
        while True:
            _response = self.describe_repositories(
                config_overrides=config_overrides,
                registry_id=registry_id,
                repository_names=repository_names,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("repositories",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def describe_repository_creation_templates(
        self,
        *,
        config_overrides: Optional[ECRClientConfig] = None,
        prefixes: Optional["capo_ecr.types.prefix_list.PrefixList"] = None,
        next_token: Optional["capo_ecr.types.next_token.NextToken"] = None,
        max_results: Optional["capo_ecr.types.max_results.MaxResults"] = None,
    ) -> "capo_ecr.types.describe_repository_creation_templates_response.DescribeRepositoryCreationTemplatesResponse":
        """<p>Returns details about the repository creation templates in a registry. The <code>prefixes</code> request parameter can be used to return the details for a specific repository creation template.</p>

        Args:
            prefixes: <p>The repository namespace prefixes associated with the repository creation templates to describe. If this value is not specified, all repository creation templates are returned.</p>
            next_token: <p>The <code>nextToken</code> value returned from a previous paginated <code>DescribeRepositoryCreationTemplates</code> request where <code>maxResults</code> was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the <code>nextToken</code> value. This value is <code>null</code> when there are no more results to return.</p> <note> <p>This token should be treated as an opaque identifier that is only used to retrieve the next items in a list and not for other programmatic purposes.</p> </note>
            max_results: <p>The maximum number of repository results returned by <code>DescribeRepositoryCreationTemplatesRequest</code> in paginated output. When this parameter is used, <code>DescribeRepositoryCreationTemplatesRequest</code> only returns <code>maxResults</code> results in a single page along with a <code>nextToken</code> response element. The remaining results of the initial request can be seen by sending another <code>DescribeRepositoryCreationTemplatesRequest</code> request with the returned <code>nextToken</code> value. This value can be between 1 and 1000. If this parameter is not used, then <code>DescribeRepositoryCreationTemplatesRequest</code> returns up to 100 results and a <code>nextToken</code> value, if applicable.</p>

        Raises:
            capo_ecr.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter is invalid. Review the available parameters for the API request.</p>
            capo_ecr.errors.server_exception.ServerException: <p>These errors are usually caused by a server-side issue.</p>
            capo_ecr.errors.validation_exception.ValidationException: <p>There was an exception validating this request.</p>
            capo_ecr.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_ecr.types.describe_repository_creation_templates_request.DescribeRepositoryCreationTemplatesRequest]",
        ) -> OperationResponse[
            "capo_ecr.types.describe_repository_creation_templates_response.DescribeRepositoryCreationTemplatesResponse"
        ]:
            import capo_ecr._operations.amazon_ec2_container_registry_v20150921.describe_repository_creation_templates

            output, http_response = (
                capo_ecr._operations.amazon_ec2_container_registry_v20150921.describe_repository_creation_templates.describe_repository_creation_templates(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ecr.types.describe_repository_creation_templates_request.DescribeRepositoryCreationTemplatesRequest = {}
        if prefixes is not None:
            input_["prefixes"] = prefixes
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_describe_repository_creation_templates(
        self,
        *,
        config_overrides: Optional[ECRClientConfig] = None,
        prefixes: Optional["capo_ecr.types.prefix_list.PrefixList"] = None,
        next_token: Optional["capo_ecr.types.next_token.NextToken"] = None,
        max_results: Optional["capo_ecr.types.max_results.MaxResults"] = None,
    ) -> "Iterator[capo_ecr.types.repository_creation_template.RepositoryCreationTemplate]":
        _token = next_token
        while True:
            _response = self.describe_repository_creation_templates(
                config_overrides=config_overrides,
                prefixes=prefixes,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("repository_creation_templates",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def get_account_setting(
        self,
        name: "capo_ecr.types.account_setting_name.AccountSettingName",
        *,
        config_overrides: Optional[ECRClientConfig] = None,
    ) -> "capo_ecr.types.get_account_setting_response.GetAccountSettingResponse":
        """<p>Retrieves the account setting value for the specified setting name.</p>

        Args:
            name: <p>The name of the account setting, such as <code>BASIC_SCAN_TYPE_VERSION</code>, <code>REGISTRY_POLICY_SCOPE</code>, or <code>BLOB_MOUNTING</code>.</p>

        Raises:
            capo_ecr.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter is invalid. Review the available parameters for the API request.</p>
            capo_ecr.errors.server_exception.ServerException: <p>These errors are usually caused by a server-side issue.</p>
            capo_ecr.errors.validation_exception.ValidationException: <p>There was an exception validating this request.</p>
            capo_ecr.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_ecr.types.get_account_setting_request.GetAccountSettingRequest]",
        ) -> OperationResponse[
            "capo_ecr.types.get_account_setting_response.GetAccountSettingResponse"
        ]:
            import capo_ecr._operations.amazon_ec2_container_registry_v20150921.get_account_setting

            output, http_response = (
                capo_ecr._operations.amazon_ec2_container_registry_v20150921.get_account_setting.get_account_setting(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ecr.types.get_account_setting_request.GetAccountSettingRequest = {
            "name": name
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_authorization_token(
        self,
        *,
        config_overrides: Optional[ECRClientConfig] = None,
        registry_ids: Optional[
            "capo_ecr.types.get_authorization_token_registry_id_list.GetAuthorizationTokenRegistryIdList"
        ] = None,
    ) -> (
        "capo_ecr.types.get_authorization_token_response.GetAuthorizationTokenResponse"
    ):
        """<p>Retrieves an authorization token. An authorization token represents your IAM authentication credentials and can be used to access any Amazon ECR registry that your IAM principal has access to. The authorization token is valid for 12 hours.</p> <p>The <code>authorizationToken</code> returned is a base64 encoded string that can be decoded and used in a <code>docker login</code> command to authenticate to a registry. The CLI offers an <code>get-login-password</code> command that simplifies the login process. For more information, see <a href="https://docs.aws.amazon.com/AmazonECR/latest/userguide/Registries.html#registry_auth">Registry authentication</a> in the <i>Amazon Elastic Container Registry User Guide</i>.</p>

        Args:
            registry_ids: <p>A list of Amazon Web Services account IDs that are associated with the registries for which to get AuthorizationData objects. If you do not specify a registry, the default registry is assumed.</p>

        Raises:
            capo_ecr.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter is invalid. Review the available parameters for the API request.</p>
            capo_ecr.errors.server_exception.ServerException: <p>These errors are usually caused by a server-side issue.</p>
            capo_ecr.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_ecr.types.get_authorization_token_request.GetAuthorizationTokenRequest]",
        ) -> OperationResponse[
            "capo_ecr.types.get_authorization_token_response.GetAuthorizationTokenResponse"
        ]:
            import capo_ecr._operations.amazon_ec2_container_registry_v20150921.get_authorization_token

            output, http_response = (
                capo_ecr._operations.amazon_ec2_container_registry_v20150921.get_authorization_token.get_authorization_token(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ecr.types.get_authorization_token_request.GetAuthorizationTokenRequest = {}
        if registry_ids is not None:
            input_["registry_ids"] = registry_ids

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_download_url_for_layer(
        self,
        repository_name: "capo_ecr.types.repository_name.RepositoryName",
        layer_digest: "capo_ecr.types.layer_digest.LayerDigest",
        *,
        config_overrides: Optional[ECRClientConfig] = None,
        registry_id: Optional["capo_ecr.types.registry_id.RegistryId"] = None,
    ) -> "capo_ecr.types.get_download_url_for_layer_response.GetDownloadUrlForLayerResponse":
        """<p>Retrieves the pre-signed Amazon S3 download URL corresponding to an image layer. You can only get URLs for image layers that are referenced in an image.</p> <p>When an image is pulled, the GetDownloadUrlForLayer API is called once per image layer that is not already cached.</p> <note> <p>This operation is used by the Amazon ECR proxy and is not generally used by customers for pulling and pushing images. In most cases, you should use the <code>docker</code> CLI to pull, tag, and push images.</p> </note>

        Args:
            registry_id: <p>The Amazon Web Services account ID associated with the registry that contains the image layer to download. If you do not specify a registry, the default registry is assumed.</p>
            repository_name: <p>The name of the repository that is associated with the image layer to download.</p>
            layer_digest: <p>The digest of the image layer to download.</p>

        Raises:
            capo_ecr.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter is invalid. Review the available parameters for the API request.</p>
            capo_ecr.errors.layer_inaccessible_exception.LayerInaccessibleException: <p>The specified layer is not available because it is not associated with an image. Unassociated image layers may be cleaned up at any time.</p>
            capo_ecr.errors.layers_not_found_exception.LayersNotFoundException: <p>The specified layers could not be found, or the specified layer is not valid for this repository.</p>
            capo_ecr.errors.repository_not_found_exception.RepositoryNotFoundException: <p>The specified repository could not be found. Check the spelling of the specified repository and ensure that you are performing operations on the correct registry.</p>
            capo_ecr.errors.server_exception.ServerException: <p>These errors are usually caused by a server-side issue.</p>
            capo_ecr.errors.unable_to_get_upstream_layer_exception.UnableToGetUpstreamLayerException: <p>There was an issue getting the upstream layer matching the pull through cache rule.</p>
            capo_ecr.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_ecr.types.get_download_url_for_layer_request.GetDownloadUrlForLayerRequest]",
        ) -> OperationResponse[
            "capo_ecr.types.get_download_url_for_layer_response.GetDownloadUrlForLayerResponse"
        ]:
            import capo_ecr._operations.amazon_ec2_container_registry_v20150921.get_download_url_for_layer

            output, http_response = (
                capo_ecr._operations.amazon_ec2_container_registry_v20150921.get_download_url_for_layer.get_download_url_for_layer(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ecr.types.get_download_url_for_layer_request.GetDownloadUrlForLayerRequest = {
            "repository_name": repository_name,
            "layer_digest": layer_digest,
        }
        if registry_id is not None:
            input_["registry_id"] = registry_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_lifecycle_policy(
        self,
        repository_name: "capo_ecr.types.repository_name.RepositoryName",
        *,
        config_overrides: Optional[ECRClientConfig] = None,
        registry_id: Optional["capo_ecr.types.registry_id.RegistryId"] = None,
    ) -> "capo_ecr.types.get_lifecycle_policy_response.GetLifecyclePolicyResponse":
        """<p>Retrieves the lifecycle policy for the specified repository.</p>

        Args:
            registry_id: <p>The Amazon Web Services account ID associated with the registry that contains the repository. If you do not specify a registry, the default registry is assumed.</p>
            repository_name: <p>The name of the repository.</p>

        Raises:
            capo_ecr.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter is invalid. Review the available parameters for the API request.</p>
            capo_ecr.errors.lifecycle_policy_not_found_exception.LifecyclePolicyNotFoundException: <p>The lifecycle policy could not be found, and no policy is set to the repository.</p>
            capo_ecr.errors.repository_not_found_exception.RepositoryNotFoundException: <p>The specified repository could not be found. Check the spelling of the specified repository and ensure that you are performing operations on the correct registry.</p>
            capo_ecr.errors.server_exception.ServerException: <p>These errors are usually caused by a server-side issue.</p>
            capo_ecr.errors.validation_exception.ValidationException: <p>There was an exception validating this request.</p>
            capo_ecr.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_ecr.types.get_lifecycle_policy_request.GetLifecyclePolicyRequest]",
        ) -> OperationResponse[
            "capo_ecr.types.get_lifecycle_policy_response.GetLifecyclePolicyResponse"
        ]:
            import capo_ecr._operations.amazon_ec2_container_registry_v20150921.get_lifecycle_policy

            output, http_response = (
                capo_ecr._operations.amazon_ec2_container_registry_v20150921.get_lifecycle_policy.get_lifecycle_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ecr.types.get_lifecycle_policy_request.GetLifecyclePolicyRequest = {
            "repository_name": repository_name
        }
        if registry_id is not None:
            input_["registry_id"] = registry_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_lifecycle_policy_preview(
        self,
        repository_name: "capo_ecr.types.repository_name.RepositoryName",
        *,
        config_overrides: Optional[ECRClientConfig] = None,
        registry_id: Optional["capo_ecr.types.registry_id.RegistryId"] = None,
        image_ids: Optional[
            "capo_ecr.types.image_identifier_list.ImageIdentifierList"
        ] = None,
        next_token: Optional["capo_ecr.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_ecr.types.lifecycle_preview_max_results.LifecyclePreviewMaxResults"
        ] = None,
        filter: Optional[
            "capo_ecr.types.lifecycle_policy_preview_filter.LifecyclePolicyPreviewFilter"
        ] = None,
    ) -> "capo_ecr.types.get_lifecycle_policy_preview_response.GetLifecyclePolicyPreviewResponse":
        """<p>Retrieves the results of the lifecycle policy preview request for the specified repository.</p>

        Args:
            registry_id: <p>The Amazon Web Services account ID associated with the registry that contains the repository. If you do not specify a registry, the default registry is assumed.</p>
            repository_name: <p>The name of the repository.</p>
            image_ids: <p>The list of imageIDs to be included.</p>
            next_token: <p>The <code>nextToken</code> value returned from a previous paginated <code>GetLifecyclePolicyPreviewRequest</code> request where <code>maxResults</code> was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the <code>nextToken</code> value. This value is <code>null</code> when there are no more results to return. This option cannot be used when you specify images with <code>imageIds</code>.</p>
            max_results: <p>The maximum number of repository results returned by <code>GetLifecyclePolicyPreviewRequest</code> in paginated output. When this parameter is used, <code>GetLifecyclePolicyPreviewRequest</code> only returns <code>maxResults</code> results in a single page along with a <code>nextToken</code> response element. The remaining results of the initial request can be seen by sending another <code>GetLifecyclePolicyPreviewRequest</code> request with the returned <code>nextToken</code> value. This value can be between 1 and 100. If this parameter is not used, then <code>GetLifecyclePolicyPreviewRequest</code> returns up to 100 results and a <code>nextToken</code> value, if applicable. This option cannot be used when you specify images with <code>imageIds</code>.</p>
            filter: <p>An optional parameter that filters results based on image tag status and all tags, if tagged.</p>

        Raises:
            capo_ecr.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter is invalid. Review the available parameters for the API request.</p>
            capo_ecr.errors.lifecycle_policy_preview_not_found_exception.LifecyclePolicyPreviewNotFoundException: <p>There is no dry run for this repository.</p>
            capo_ecr.errors.repository_not_found_exception.RepositoryNotFoundException: <p>The specified repository could not be found. Check the spelling of the specified repository and ensure that you are performing operations on the correct registry.</p>
            capo_ecr.errors.server_exception.ServerException: <p>These errors are usually caused by a server-side issue.</p>
            capo_ecr.errors.validation_exception.ValidationException: <p>There was an exception validating this request.</p>
            capo_ecr.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_ecr.types.get_lifecycle_policy_preview_request.GetLifecyclePolicyPreviewRequest]",
        ) -> OperationResponse[
            "capo_ecr.types.get_lifecycle_policy_preview_response.GetLifecyclePolicyPreviewResponse"
        ]:
            import capo_ecr._operations.amazon_ec2_container_registry_v20150921.get_lifecycle_policy_preview

            output, http_response = (
                capo_ecr._operations.amazon_ec2_container_registry_v20150921.get_lifecycle_policy_preview.get_lifecycle_policy_preview(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ecr.types.get_lifecycle_policy_preview_request.GetLifecyclePolicyPreviewRequest = {
            "repository_name": repository_name
        }
        if registry_id is not None:
            input_["registry_id"] = registry_id
        if image_ids is not None:
            input_["image_ids"] = image_ids
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if filter is not None:
            input_["filter"] = filter

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_get_lifecycle_policy_preview(
        self,
        repository_name: "capo_ecr.types.repository_name.RepositoryName",
        *,
        config_overrides: Optional[ECRClientConfig] = None,
        registry_id: Optional["capo_ecr.types.registry_id.RegistryId"] = None,
        image_ids: Optional[
            "capo_ecr.types.image_identifier_list.ImageIdentifierList"
        ] = None,
        next_token: Optional["capo_ecr.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_ecr.types.lifecycle_preview_max_results.LifecyclePreviewMaxResults"
        ] = None,
        filter: Optional[
            "capo_ecr.types.lifecycle_policy_preview_filter.LifecyclePolicyPreviewFilter"
        ] = None,
    ) -> "Iterator[capo_ecr.types.lifecycle_policy_preview_result.LifecyclePolicyPreviewResult]":
        _token = next_token
        while True:
            _response = self.get_lifecycle_policy_preview(
                repository_name,
                config_overrides=config_overrides,
                registry_id=registry_id,
                image_ids=image_ids,
                next_token=_token,
                max_results=max_results,
                filter=filter,
            )
            _page = _resolve_path(_response, ("preview_results",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def get_registry_policy(
        self, *, config_overrides: Optional[ECRClientConfig] = None
    ) -> "capo_ecr.types.get_registry_policy_response.GetRegistryPolicyResponse":
        """<p>Retrieves the permissions policy for a registry.</p>

        Raises:
            capo_ecr.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter is invalid. Review the available parameters for the API request.</p>
            capo_ecr.errors.registry_policy_not_found_exception.RegistryPolicyNotFoundException: <p>The registry doesn't have an associated registry policy.</p>
            capo_ecr.errors.server_exception.ServerException: <p>These errors are usually caused by a server-side issue.</p>
            capo_ecr.errors.validation_exception.ValidationException: <p>There was an exception validating this request.</p>
            capo_ecr.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_ecr.types.get_registry_policy_request.GetRegistryPolicyRequest]",
        ) -> OperationResponse[
            "capo_ecr.types.get_registry_policy_response.GetRegistryPolicyResponse"
        ]:
            import capo_ecr._operations.amazon_ec2_container_registry_v20150921.get_registry_policy

            output, http_response = (
                capo_ecr._operations.amazon_ec2_container_registry_v20150921.get_registry_policy.get_registry_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ecr.types.get_registry_policy_request.GetRegistryPolicyRequest = {}

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_registry_scanning_configuration(
        self, *, config_overrides: Optional[ECRClientConfig] = None
    ) -> "capo_ecr.types.get_registry_scanning_configuration_response.GetRegistryScanningConfigurationResponse":
        """<p>Retrieves the scanning configuration for a registry.</p>

        Raises:
            capo_ecr.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter is invalid. Review the available parameters for the API request.</p>
            capo_ecr.errors.server_exception.ServerException: <p>These errors are usually caused by a server-side issue.</p>
            capo_ecr.errors.validation_exception.ValidationException: <p>There was an exception validating this request.</p>
            capo_ecr.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_ecr.types.get_registry_scanning_configuration_request.GetRegistryScanningConfigurationRequest]",
        ) -> OperationResponse[
            "capo_ecr.types.get_registry_scanning_configuration_response.GetRegistryScanningConfigurationResponse"
        ]:
            import capo_ecr._operations.amazon_ec2_container_registry_v20150921.get_registry_scanning_configuration

            output, http_response = (
                capo_ecr._operations.amazon_ec2_container_registry_v20150921.get_registry_scanning_configuration.get_registry_scanning_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ecr.types.get_registry_scanning_configuration_request.GetRegistryScanningConfigurationRequest = {}

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_repository_policy(
        self,
        repository_name: "capo_ecr.types.repository_name.RepositoryName",
        *,
        config_overrides: Optional[ECRClientConfig] = None,
        registry_id: Optional["capo_ecr.types.registry_id.RegistryId"] = None,
    ) -> "capo_ecr.types.get_repository_policy_response.GetRepositoryPolicyResponse":
        """<p>Retrieves the repository policy for the specified repository.</p>

        Args:
            registry_id: <p>The Amazon Web Services account ID associated with the registry that contains the repository. If you do not specify a registry, the default registry is assumed.</p>
            repository_name: <p>The name of the repository with the policy to retrieve.</p>

        Raises:
            capo_ecr.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter is invalid. Review the available parameters for the API request.</p>
            capo_ecr.errors.repository_not_found_exception.RepositoryNotFoundException: <p>The specified repository could not be found. Check the spelling of the specified repository and ensure that you are performing operations on the correct registry.</p>
            capo_ecr.errors.repository_policy_not_found_exception.RepositoryPolicyNotFoundException: <p>The specified repository and registry combination does not have an associated repository policy.</p>
            capo_ecr.errors.server_exception.ServerException: <p>These errors are usually caused by a server-side issue.</p>
            capo_ecr.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To get the current policy for a repository
            This example obtains the repository policy for the repository named ubuntu.

            >>> client.get_repository_policy(repository_name='ubuntu')
        """

        def _handler(
            req: "OperationRequest[capo_ecr.types.get_repository_policy_request.GetRepositoryPolicyRequest]",
        ) -> OperationResponse[
            "capo_ecr.types.get_repository_policy_response.GetRepositoryPolicyResponse"
        ]:
            import capo_ecr._operations.amazon_ec2_container_registry_v20150921.get_repository_policy

            output, http_response = (
                capo_ecr._operations.amazon_ec2_container_registry_v20150921.get_repository_policy.get_repository_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ecr.types.get_repository_policy_request.GetRepositoryPolicyRequest = {
            "repository_name": repository_name
        }
        if registry_id is not None:
            input_["registry_id"] = registry_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_signing_configuration(
        self, *, config_overrides: Optional[ECRClientConfig] = None
    ) -> "capo_ecr.types.get_signing_configuration_response.GetSigningConfigurationResponse":
        """<p>Retrieves the registry's signing configuration, which defines rules for automatically signing images using Amazon Web Services Signer.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/AmazonECR/latest/userguide/managed-signing.html">Managed signing</a> in the <i>Amazon Elastic Container Registry User Guide</i>.</p>

        Raises:
            capo_ecr.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter is invalid. Review the available parameters for the API request.</p>
            capo_ecr.errors.server_exception.ServerException: <p>These errors are usually caused by a server-side issue.</p>
            capo_ecr.errors.signing_configuration_not_found_exception.SigningConfigurationNotFoundException: <p>The specified signing configuration was not found. This occurs when attempting to retrieve or delete a signing configuration that does not exist.</p>
            capo_ecr.errors.validation_exception.ValidationException: <p>There was an exception validating this request.</p>
            capo_ecr.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_ecr.types.get_signing_configuration_request.GetSigningConfigurationRequest]",
        ) -> OperationResponse[
            "capo_ecr.types.get_signing_configuration_response.GetSigningConfigurationResponse"
        ]:
            import capo_ecr._operations.amazon_ec2_container_registry_v20150921.get_signing_configuration

            output, http_response = (
                capo_ecr._operations.amazon_ec2_container_registry_v20150921.get_signing_configuration.get_signing_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ecr.types.get_signing_configuration_request.GetSigningConfigurationRequest = {}

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def initiate_layer_upload(
        self,
        repository_name: "capo_ecr.types.repository_name.RepositoryName",
        *,
        config_overrides: Optional[ECRClientConfig] = None,
        registry_id: Optional["capo_ecr.types.registry_id.RegistryId"] = None,
    ) -> "capo_ecr.types.initiate_layer_upload_response.InitiateLayerUploadResponse":
        """<p>Notifies Amazon ECR that you intend to upload an image layer.</p> <p>When an image is pushed, the InitiateLayerUpload API is called once per image layer that has not already been uploaded. Whether or not an image layer has been uploaded is determined by the BatchCheckLayerAvailability API action.</p> <note> <p>This operation is used by the Amazon ECR proxy and is not generally used by customers for pulling and pushing images. In most cases, you should use the <code>docker</code> CLI to pull, tag, and push images.</p> </note>

        Args:
            registry_id: <p>The Amazon Web Services account ID associated with the registry to which you intend to upload layers. If you do not specify a registry, the default registry is assumed.</p>
            repository_name: <p>The name of the repository to which you intend to upload layers.</p>

        Raises:
            capo_ecr.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter is invalid. Review the available parameters for the API request.</p>
            capo_ecr.errors.kms_exception.KmsException: <p>The operation failed due to a KMS exception.</p>
            capo_ecr.errors.repository_not_found_exception.RepositoryNotFoundException: <p>The specified repository could not be found. Check the spelling of the specified repository and ensure that you are performing operations on the correct registry.</p>
            capo_ecr.errors.server_exception.ServerException: <p>These errors are usually caused by a server-side issue.</p>
            capo_ecr.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_ecr.types.initiate_layer_upload_request.InitiateLayerUploadRequest]",
        ) -> OperationResponse[
            "capo_ecr.types.initiate_layer_upload_response.InitiateLayerUploadResponse"
        ]:
            import capo_ecr._operations.amazon_ec2_container_registry_v20150921.initiate_layer_upload

            output, http_response = (
                capo_ecr._operations.amazon_ec2_container_registry_v20150921.initiate_layer_upload.initiate_layer_upload(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ecr.types.initiate_layer_upload_request.InitiateLayerUploadRequest = {
            "repository_name": repository_name
        }
        if registry_id is not None:
            input_["registry_id"] = registry_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_image_referrers(
        self,
        repository_name: "capo_ecr.types.repository_name.RepositoryName",
        subject_id: "capo_ecr.types.subject_identifier.SubjectIdentifier",
        *,
        config_overrides: Optional[ECRClientConfig] = None,
        registry_id: Optional["capo_ecr.types.registry_id.RegistryId"] = None,
        filter: Optional[
            "capo_ecr.types.list_image_referrers_filter.ListImageReferrersFilter"
        ] = None,
        next_token: Optional["capo_ecr.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_ecr.types.fifty_max_results.FiftyMaxResults"
        ] = None,
    ) -> "capo_ecr.types.list_image_referrers_response.ListImageReferrersResponse":
        """<p>Lists the artifacts associated with a specified subject image.</p> <note> <p>The IAM principal invoking this operation must have the <code>ecr:BatchGetImage</code> permission.</p> </note>

        Args:
            registry_id: <p>The Amazon Web Services account ID associated with the registry that contains the repository in which to list image referrers. If you do not specify a registry, the default registry is assumed.</p>
            repository_name: <p>The name of the repository that contains the subject image.</p>
            subject_id: <p>An object containing the image digest of the subject image for which to retrieve associated artifacts.</p>
            filter: <p>The filter key and value with which to filter your <code>ListImageReferrers</code> results. If no filter is specified, only artifacts with <code>ACTIVE</code> status are returned.</p>
            next_token: <p>The <code>nextToken</code> value returned from a previous paginated <code>ListImageReferrers</code> request where <code>maxResults</code> was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the <code>nextToken</code> value. This value is <code>null</code> when there are no more results to return.</p> <note> <p>This token should be treated as an opaque identifier that is only used to retrieve the next items in a list and not for other programmatic purposes.</p> </note>
            max_results: <p>The maximum number of image referrer results returned by <code>ListImageReferrers</code> in paginated output. When this parameter is used, <code>ListImageReferrers</code> only returns <code>maxResults</code> results in a single page along with a <code>nextToken</code> response element. The remaining results of the initial request can be seen by sending another <code>ListImageReferrers</code> request with the returned <code>nextToken</code> value. This value can be between 1 and 50. If this parameter is not used, then <code>ListImageReferrers</code> returns up to 20 results and a <code>nextToken</code> value, if applicable.</p>

        Raises:
            capo_ecr.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter is invalid. Review the available parameters for the API request.</p>
            capo_ecr.errors.repository_not_found_exception.RepositoryNotFoundException: <p>The specified repository could not be found. Check the spelling of the specified repository and ensure that you are performing operations on the correct registry.</p>
            capo_ecr.errors.server_exception.ServerException: <p>These errors are usually caused by a server-side issue.</p>
            capo_ecr.errors.unable_to_list_upstream_image_referrers_exception.UnableToListUpstreamImageReferrersException: <p>The referrer or referrers were unable to be listed using the pull through cache rule. This is usually caused because of an issue with the Secrets Manager secret containing the credentials for the upstream registry.</p>
            capo_ecr.errors.validation_exception.ValidationException: <p>There was an exception validating this request.</p>
            capo_ecr.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To list both active and archived artifacts
            This example lists all artifacts including those that have been archived, by specifying the artifactStatus filter as ANY.

            >>> client.list_image_referrers(repository_name='sample-repo', subject_id={'imageDigest': 'sha256:943e640159415616581703a53fa4ed87e96740655fd67daf2d2146a35337bce5'}, filter={'artifactStatus': 'ANY'})
            To list artifacts associated with a subject image
            This example lists all artifacts (such as Sigstore signatures) that reference a specific container image in the sample-repo repository.

            >>> client.list_image_referrers(repository_name='sample-repo', subject_id={'imageDigest': 'sha256:943e640159415616581703a53fa4ed87e96740655fd67daf2d2146a35337bce5'})
            To list artifacts of a specific type
            This example lists only Sigstore bundle artifacts associated with a subject image by filtering on the artifact type.

            >>> client.list_image_referrers(repository_name='sample-repo', subject_id={'imageDigest': 'sha256:943e640159415616581703a53fa4ed87e96740655fd67daf2d2146a35337bce5'}, filter={'artifactTypes': ['application/vnd.dev.sigstore.bundle.v0.3+json']})
        """

        def _handler(
            req: "OperationRequest[capo_ecr.types.list_image_referrers_request.ListImageReferrersRequest]",
        ) -> OperationResponse[
            "capo_ecr.types.list_image_referrers_response.ListImageReferrersResponse"
        ]:
            import capo_ecr._operations.amazon_ec2_container_registry_v20150921.list_image_referrers

            output, http_response = (
                capo_ecr._operations.amazon_ec2_container_registry_v20150921.list_image_referrers.list_image_referrers(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ecr.types.list_image_referrers_request.ListImageReferrersRequest = {
            "repository_name": repository_name,
            "subject_id": subject_id,
        }
        if registry_id is not None:
            input_["registry_id"] = registry_id
        if filter is not None:
            input_["filter"] = filter
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_images(
        self,
        repository_name: "capo_ecr.types.repository_name.RepositoryName",
        *,
        config_overrides: Optional[ECRClientConfig] = None,
        registry_id: Optional["capo_ecr.types.registry_id.RegistryId"] = None,
        next_token: Optional["capo_ecr.types.next_token.NextToken"] = None,
        max_results: Optional["capo_ecr.types.max_results.MaxResults"] = None,
        filter: Optional["capo_ecr.types.list_images_filter.ListImagesFilter"] = None,
    ) -> "capo_ecr.types.list_images_response.ListImagesResponse":
        """<p>Lists all the image IDs for the specified repository.</p> <p>You can filter images based on whether or not they are tagged by using the <code>tagStatus</code> filter and specifying either <code>TAGGED</code>, <code>UNTAGGED</code> or <code>ANY</code>. For example, you can filter your results to return only <code>UNTAGGED</code> images and then pipe that result to a <a>BatchDeleteImage</a> operation to delete them. Or, you can filter your results to return only <code>TAGGED</code> images to list all of the tags in your repository.</p>

        Args:
            registry_id: <p>The Amazon Web Services account ID associated with the registry that contains the repository in which to list images. If you do not specify a registry, the default registry is assumed.</p>
            repository_name: <p>The repository with image IDs to be listed.</p>
            next_token: <p>The <code>nextToken</code> value returned from a previous paginated <code>ListImages</code> request where <code>maxResults</code> was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the <code>nextToken</code> value. This value is <code>null</code> when there are no more results to return.</p> <note> <p>This token should be treated as an opaque identifier that is only used to retrieve the next items in a list and not for other programmatic purposes.</p> </note>
            max_results: <p>The maximum number of image results returned by <code>ListImages</code> in paginated output. When this parameter is used, <code>ListImages</code> only returns <code>maxResults</code> results in a single page along with a <code>nextToken</code> response element. The remaining results of the initial request can be seen by sending another <code>ListImages</code> request with the returned <code>nextToken</code> value. This value can be between 1 and 1000. If this parameter is not used, then <code>ListImages</code> returns up to 100 results and a <code>nextToken</code> value, if applicable.</p>
            filter: <p>The filter key and value with which to filter your <code>ListImages</code> results.</p>

        Raises:
            capo_ecr.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter is invalid. Review the available parameters for the API request.</p>
            capo_ecr.errors.repository_not_found_exception.RepositoryNotFoundException: <p>The specified repository could not be found. Check the spelling of the specified repository and ensure that you are performing operations on the correct registry.</p>
            capo_ecr.errors.server_exception.ServerException: <p>These errors are usually caused by a server-side issue.</p>
            capo_ecr.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To list all images in a repository
            This example lists all of the images in the repository named ubuntu in the default registry in the current account.

            >>> client.list_images(repository_name='ubuntu')
        """

        def _handler(
            req: "OperationRequest[capo_ecr.types.list_images_request.ListImagesRequest]",
        ) -> OperationResponse[
            "capo_ecr.types.list_images_response.ListImagesResponse"
        ]:
            import capo_ecr._operations.amazon_ec2_container_registry_v20150921.list_images

            output, http_response = (
                capo_ecr._operations.amazon_ec2_container_registry_v20150921.list_images.list_images(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ecr.types.list_images_request.ListImagesRequest = {
            "repository_name": repository_name
        }
        if registry_id is not None:
            input_["registry_id"] = registry_id
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if filter is not None:
            input_["filter"] = filter

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_images(
        self,
        repository_name: "capo_ecr.types.repository_name.RepositoryName",
        *,
        config_overrides: Optional[ECRClientConfig] = None,
        registry_id: Optional["capo_ecr.types.registry_id.RegistryId"] = None,
        next_token: Optional["capo_ecr.types.next_token.NextToken"] = None,
        max_results: Optional["capo_ecr.types.max_results.MaxResults"] = None,
        filter: Optional["capo_ecr.types.list_images_filter.ListImagesFilter"] = None,
    ) -> "Iterator[capo_ecr.types.image_identifier.ImageIdentifier]":
        _token = next_token
        while True:
            _response = self.list_images(
                repository_name,
                config_overrides=config_overrides,
                registry_id=registry_id,
                next_token=_token,
                max_results=max_results,
                filter=filter,
            )
            _page = _resolve_path(_response, ("image_ids",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_pull_time_update_exclusions(
        self,
        *,
        config_overrides: Optional[ECRClientConfig] = None,
        max_results: Optional["capo_ecr.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_ecr.types.next_token.NextToken"] = None,
    ) -> "capo_ecr.types.list_pull_time_update_exclusions_response.ListPullTimeUpdateExclusionsResponse":
        """<p>Lists the IAM principals that are excluded from having their image pull times recorded.</p>

        Args:
            max_results: <p>The maximum number of pull time update exclusion results returned by <code>ListPullTimeUpdateExclusions</code> in paginated output. When this parameter is used, <code>ListPullTimeUpdateExclusions</code> only returns <code>maxResults</code> results in a single page along with a <code>nextToken</code> response element. The remaining results of the initial request can be seen by sending another <code>ListPullTimeUpdateExclusions</code> request with the returned <code>nextToken</code> value. This value can be between 1 and 1000. If this parameter is not used, then <code>ListPullTimeUpdateExclusions</code> returns up to 100 results and a <code>nextToken</code> value, if applicable.</p>
            next_token: <p>The <code>nextToken</code> value returned from a previous paginated <code>ListPullTimeUpdateExclusions</code> request where <code>maxResults</code> was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the <code>nextToken</code> value. This value is <code>null</code> when there are no more results to return.</p> <note> <p>This token should be treated as an opaque identifier that is only used to retrieve the next items in a list and not for other programmatic purposes.</p> </note>

        Raises:
            capo_ecr.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter is invalid. Review the available parameters for the API request.</p>
            capo_ecr.errors.limit_exceeded_exception.LimitExceededException: <p>The operation did not succeed because it would have exceeded a service limit for your account. For more information, see <a href="https://docs.aws.amazon.com/AmazonECR/latest/userguide/service-quotas.html">Amazon ECR service quotas</a> in the Amazon Elastic Container Registry User Guide.</p>
            capo_ecr.errors.server_exception.ServerException: <p>These errors are usually caused by a server-side issue.</p>
            capo_ecr.errors.validation_exception.ValidationException: <p>There was an exception validating this request.</p>
            capo_ecr.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To list all pull time update exclusions
            This example lists all IAM principals that are excluded from having their image pull timestamps recorded in the registry.

            >>> client.list_pull_time_update_exclusions()
            To list pull time update exclusions with pagination
            This example lists pull time update exclusions with pagination, requesting a maximum of 2 results per page.

            >>> client.list_pull_time_update_exclusions(max_results=2)
        """

        def _handler(
            req: "OperationRequest[capo_ecr.types.list_pull_time_update_exclusions_request.ListPullTimeUpdateExclusionsRequest]",
        ) -> OperationResponse[
            "capo_ecr.types.list_pull_time_update_exclusions_response.ListPullTimeUpdateExclusionsResponse"
        ]:
            import capo_ecr._operations.amazon_ec2_container_registry_v20150921.list_pull_time_update_exclusions

            output, http_response = (
                capo_ecr._operations.amazon_ec2_container_registry_v20150921.list_pull_time_update_exclusions.list_pull_time_update_exclusions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ecr.types.list_pull_time_update_exclusions_request.ListPullTimeUpdateExclusionsRequest = {}
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_tags_for_resource(
        self,
        resource_arn: "capo_ecr.types.arn.Arn",
        *,
        config_overrides: Optional[ECRClientConfig] = None,
    ) -> "capo_ecr.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>List the tags for an Amazon ECR resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) that identifies the resource for which to list the tags. Currently, the only supported resource is an Amazon ECR repository.</p>

        Raises:
            capo_ecr.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter is invalid. Review the available parameters for the API request.</p>
            capo_ecr.errors.repository_not_found_exception.RepositoryNotFoundException: <p>The specified repository could not be found. Check the spelling of the specified repository and ensure that you are performing operations on the correct registry.</p>
            capo_ecr.errors.server_exception.ServerException: <p>These errors are usually caused by a server-side issue.</p>
            capo_ecr.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_ecr.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> OperationResponse[
            "capo_ecr.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import capo_ecr._operations.amazon_ec2_container_registry_v20150921.list_tags_for_resource

            output, http_response = (
                capo_ecr._operations.amazon_ec2_container_registry_v20150921.list_tags_for_resource.list_tags_for_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ecr.types.list_tags_for_resource_request.ListTagsForResourceRequest = {
            "resource_arn": resource_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def put_account_setting(
        self,
        name: "capo_ecr.types.account_setting_name.AccountSettingName",
        value: "capo_ecr.types.account_setting_value.AccountSettingValue",
        *,
        config_overrides: Optional[ECRClientConfig] = None,
    ) -> "capo_ecr.types.put_account_setting_response.PutAccountSettingResponse":
        """<p>Allows you to change the basic scan type version or registry policy scope.</p>

        Args:
            name: <p>The name of the account setting, such as <code>BASIC_SCAN_TYPE_VERSION</code>, <code>REGISTRY_POLICY_SCOPE</code>, or <code>BLOB_MOUNTING</code>.</p>
            value: <p>Setting value that is specified. Valid value for basic scan type: <code>AWS_NATIVE</code>. Valid values for registry policy scope: <code>V2</code>. Valid values for blob mounting: <code>ENABLED</code> or <code>DISABLED</code>.</p>

        Raises:
            capo_ecr.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter is invalid. Review the available parameters for the API request.</p>
            capo_ecr.errors.limit_exceeded_exception.LimitExceededException: <p>The operation did not succeed because it would have exceeded a service limit for your account. For more information, see <a href="https://docs.aws.amazon.com/AmazonECR/latest/userguide/service-quotas.html">Amazon ECR service quotas</a> in the Amazon Elastic Container Registry User Guide.</p>
            capo_ecr.errors.server_exception.ServerException: <p>These errors are usually caused by a server-side issue.</p>
            capo_ecr.errors.validation_exception.ValidationException: <p>There was an exception validating this request.</p>
            capo_ecr.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_ecr.types.put_account_setting_request.PutAccountSettingRequest]",
        ) -> OperationResponse[
            "capo_ecr.types.put_account_setting_response.PutAccountSettingResponse"
        ]:
            import capo_ecr._operations.amazon_ec2_container_registry_v20150921.put_account_setting

            output, http_response = (
                capo_ecr._operations.amazon_ec2_container_registry_v20150921.put_account_setting.put_account_setting(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ecr.types.put_account_setting_request.PutAccountSettingRequest = {
            "name": name,
            "value": value,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def put_image(
        self,
        repository_name: "capo_ecr.types.repository_name.RepositoryName",
        image_manifest: "capo_ecr.types.image_manifest.ImageManifest",
        *,
        config_overrides: Optional[ECRClientConfig] = None,
        registry_id: Optional["capo_ecr.types.registry_id.RegistryId"] = None,
        image_manifest_media_type: Optional[
            "capo_ecr.types.media_type.MediaType"
        ] = None,
        image_tag: Optional["capo_ecr.types.image_tag.ImageTag"] = None,
        image_digest: Optional["capo_ecr.types.image_digest.ImageDigest"] = None,
    ) -> "capo_ecr.types.put_image_response.PutImageResponse":
        """<p>Creates or updates the image manifest and tags associated with an image.</p> <p>When an image is pushed and all new image layers have been uploaded, the PutImage API is called once to create or update the image manifest and the tags associated with the image.</p> <note> <p>This operation is used by the Amazon ECR proxy and is not generally used by customers for pulling and pushing images. In most cases, you should use the <code>docker</code> CLI to pull, tag, and push images.</p> </note>

        Args:
            registry_id: <p>The Amazon Web Services account ID associated with the registry that contains the repository in which to put the image. If you do not specify a registry, the default registry is assumed.</p>
            repository_name: <p>The name of the repository in which to put the image.</p>
            image_manifest: <p>The image manifest corresponding to the image to be uploaded.</p>
            image_manifest_media_type: <p>The media type of the image manifest. If you push an image manifest that does not contain the <code>mediaType</code> field, you must specify the <code>imageManifestMediaType</code> in the request.</p>
            image_tag: <p>The tag to associate with the image. This parameter is optional.</p>
            image_digest: <p>The image digest of the image manifest corresponding to the image.</p>

        Raises:
            capo_ecr.errors.image_already_exists_exception.ImageAlreadyExistsException: <p>The specified image has already been pushed, and there were no changes to the manifest or image tag after the last push.</p>
            capo_ecr.errors.image_digest_does_not_match_exception.ImageDigestDoesNotMatchException: <p>The specified image digest does not match the digest that Amazon ECR calculated for the image.</p>
            capo_ecr.errors.image_tag_already_exists_exception.ImageTagAlreadyExistsException: <p>The specified image is tagged with a tag that already exists. The repository is configured for tag immutability.</p>
            capo_ecr.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter is invalid. Review the available parameters for the API request.</p>
            capo_ecr.errors.kms_exception.KmsException: <p>The operation failed due to a KMS exception.</p>
            capo_ecr.errors.layers_not_found_exception.LayersNotFoundException: <p>The specified layers could not be found, or the specified layer is not valid for this repository.</p>
            capo_ecr.errors.limit_exceeded_exception.LimitExceededException: <p>The operation did not succeed because it would have exceeded a service limit for your account. For more information, see <a href="https://docs.aws.amazon.com/AmazonECR/latest/userguide/service-quotas.html">Amazon ECR service quotas</a> in the Amazon Elastic Container Registry User Guide.</p>
            capo_ecr.errors.referenced_images_not_found_exception.ReferencedImagesNotFoundException: <p>The manifest list is referencing an image that does not exist.</p>
            capo_ecr.errors.repository_not_found_exception.RepositoryNotFoundException: <p>The specified repository could not be found. Check the spelling of the specified repository and ensure that you are performing operations on the correct registry.</p>
            capo_ecr.errors.server_exception.ServerException: <p>These errors are usually caused by a server-side issue.</p>
            capo_ecr.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_ecr.types.put_image_request.PutImageRequest]",
        ) -> OperationResponse["capo_ecr.types.put_image_response.PutImageResponse"]:
            import capo_ecr._operations.amazon_ec2_container_registry_v20150921.put_image

            output, http_response = (
                capo_ecr._operations.amazon_ec2_container_registry_v20150921.put_image.put_image(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ecr.types.put_image_request.PutImageRequest = {
            "repository_name": repository_name,
            "image_manifest": image_manifest,
        }
        if registry_id is not None:
            input_["registry_id"] = registry_id
        if image_manifest_media_type is not None:
            input_["image_manifest_media_type"] = image_manifest_media_type
        if image_tag is not None:
            input_["image_tag"] = image_tag
        if image_digest is not None:
            input_["image_digest"] = image_digest

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def put_image_scanning_configuration(
        self,
        repository_name: "capo_ecr.types.repository_name.RepositoryName",
        image_scanning_configuration: "capo_ecr.types.image_scanning_configuration.ImageScanningConfiguration",
        *,
        config_overrides: Optional[ECRClientConfig] = None,
        registry_id: Optional["capo_ecr.types.registry_id.RegistryId"] = None,
    ) -> "capo_ecr.types.put_image_scanning_configuration_response.PutImageScanningConfigurationResponse":
        """<important> <p>The <code>PutImageScanningConfiguration</code> API is being deprecated, in favor of specifying the image scanning configuration at the registry level. For more information, see <a>PutRegistryScanningConfiguration</a>.</p> </important> <p>Updates the image scanning configuration for the specified repository.</p>

        Args:
            registry_id: <p>The Amazon Web Services account ID associated with the registry that contains the repository in which to update the image scanning configuration setting. If you do not specify a registry, the default registry is assumed.</p>
            repository_name: <p>The name of the repository in which to update the image scanning configuration setting.</p>
            image_scanning_configuration: <p>The image scanning configuration for the repository. This setting determines whether images are scanned for known vulnerabilities after being pushed to the repository.</p>

        Raises:
            capo_ecr.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter is invalid. Review the available parameters for the API request.</p>
            capo_ecr.errors.repository_not_found_exception.RepositoryNotFoundException: <p>The specified repository could not be found. Check the spelling of the specified repository and ensure that you are performing operations on the correct registry.</p>
            capo_ecr.errors.server_exception.ServerException: <p>These errors are usually caused by a server-side issue.</p>
            capo_ecr.errors.validation_exception.ValidationException: <p>There was an exception validating this request.</p>
            capo_ecr.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_ecr.types.put_image_scanning_configuration_request.PutImageScanningConfigurationRequest]",
        ) -> OperationResponse[
            "capo_ecr.types.put_image_scanning_configuration_response.PutImageScanningConfigurationResponse"
        ]:
            import capo_ecr._operations.amazon_ec2_container_registry_v20150921.put_image_scanning_configuration

            output, http_response = (
                capo_ecr._operations.amazon_ec2_container_registry_v20150921.put_image_scanning_configuration.put_image_scanning_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ecr.types.put_image_scanning_configuration_request.PutImageScanningConfigurationRequest = {
            "repository_name": repository_name,
            "image_scanning_configuration": image_scanning_configuration,
        }
        if registry_id is not None:
            input_["registry_id"] = registry_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def put_image_tag_mutability(
        self,
        repository_name: "capo_ecr.types.repository_name.RepositoryName",
        image_tag_mutability: "capo_ecr.types.image_tag_mutability.ImageTagMutability",
        *,
        config_overrides: Optional[ECRClientConfig] = None,
        registry_id: Optional["capo_ecr.types.registry_id.RegistryId"] = None,
        image_tag_mutability_exclusion_filters: Optional[
            "capo_ecr.types.image_tag_mutability_exclusion_filters.ImageTagMutabilityExclusionFilters"
        ] = None,
    ) -> (
        "capo_ecr.types.put_image_tag_mutability_response.PutImageTagMutabilityResponse"
    ):
        """<p>Updates the image tag mutability settings for the specified repository. For more information, see <a href="https://docs.aws.amazon.com/AmazonECR/latest/userguide/image-tag-mutability.html">Image tag mutability</a> in the <i>Amazon Elastic Container Registry User Guide</i>.</p>

        Args:
            registry_id: <p>The Amazon Web Services account ID associated with the registry that contains the repository in which to update the image tag mutability settings. If you do not specify a registry, the default registry is assumed.</p>
            repository_name: <p>The name of the repository in which to update the image tag mutability settings.</p>
            image_tag_mutability: <p>The tag mutability setting for the repository. If <code>MUTABLE</code> is specified, image tags can be overwritten. If <code>IMMUTABLE</code> is specified, all image tags within the repository will be immutable which will prevent them from being overwritten.</p>
            image_tag_mutability_exclusion_filters: <p>A list of filters that specify which image tags should be excluded from the image tag mutability setting being applied.</p>

        Raises:
            capo_ecr.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter is invalid. Review the available parameters for the API request.</p>
            capo_ecr.errors.repository_not_found_exception.RepositoryNotFoundException: <p>The specified repository could not be found. Check the spelling of the specified repository and ensure that you are performing operations on the correct registry.</p>
            capo_ecr.errors.server_exception.ServerException: <p>These errors are usually caused by a server-side issue.</p>
            capo_ecr.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_ecr.types.put_image_tag_mutability_request.PutImageTagMutabilityRequest]",
        ) -> OperationResponse[
            "capo_ecr.types.put_image_tag_mutability_response.PutImageTagMutabilityResponse"
        ]:
            import capo_ecr._operations.amazon_ec2_container_registry_v20150921.put_image_tag_mutability

            output, http_response = (
                capo_ecr._operations.amazon_ec2_container_registry_v20150921.put_image_tag_mutability.put_image_tag_mutability(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ecr.types.put_image_tag_mutability_request.PutImageTagMutabilityRequest = {
            "repository_name": repository_name,
            "image_tag_mutability": image_tag_mutability,
        }
        if registry_id is not None:
            input_["registry_id"] = registry_id
        if image_tag_mutability_exclusion_filters is not None:
            input_["image_tag_mutability_exclusion_filters"] = (
                image_tag_mutability_exclusion_filters
            )

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def put_lifecycle_policy(
        self,
        repository_name: "capo_ecr.types.repository_name.RepositoryName",
        lifecycle_policy_text: "capo_ecr.types.lifecycle_policy_text.LifecyclePolicyText",
        *,
        config_overrides: Optional[ECRClientConfig] = None,
        registry_id: Optional["capo_ecr.types.registry_id.RegistryId"] = None,
    ) -> "capo_ecr.types.put_lifecycle_policy_response.PutLifecyclePolicyResponse":
        """<p>Creates or updates the lifecycle policy for the specified repository. For more information, see <a href="https://docs.aws.amazon.com/AmazonECR/latest/userguide/LifecyclePolicies.html">Lifecycle policy template</a>.</p>

        Args:
            registry_id: <p>The Amazon Web Services account ID associated with the registry that contains the repository. If you do not specify a registry, the default registry is assumed.</p>
            repository_name: <p>The name of the repository to receive the policy.</p>
            lifecycle_policy_text: <p>The JSON repository policy text to apply to the repository.</p>

        Raises:
            capo_ecr.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter is invalid. Review the available parameters for the API request.</p>
            capo_ecr.errors.repository_not_found_exception.RepositoryNotFoundException: <p>The specified repository could not be found. Check the spelling of the specified repository and ensure that you are performing operations on the correct registry.</p>
            capo_ecr.errors.server_exception.ServerException: <p>These errors are usually caused by a server-side issue.</p>
            capo_ecr.errors.validation_exception.ValidationException: <p>There was an exception validating this request.</p>
            capo_ecr.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_ecr.types.put_lifecycle_policy_request.PutLifecyclePolicyRequest]",
        ) -> OperationResponse[
            "capo_ecr.types.put_lifecycle_policy_response.PutLifecyclePolicyResponse"
        ]:
            import capo_ecr._operations.amazon_ec2_container_registry_v20150921.put_lifecycle_policy

            output, http_response = (
                capo_ecr._operations.amazon_ec2_container_registry_v20150921.put_lifecycle_policy.put_lifecycle_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ecr.types.put_lifecycle_policy_request.PutLifecyclePolicyRequest = {
            "repository_name": repository_name,
            "lifecycle_policy_text": lifecycle_policy_text,
        }
        if registry_id is not None:
            input_["registry_id"] = registry_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def put_registry_policy(
        self,
        policy_text: "capo_ecr.types.registry_policy_text.RegistryPolicyText",
        *,
        config_overrides: Optional[ECRClientConfig] = None,
    ) -> "capo_ecr.types.put_registry_policy_response.PutRegistryPolicyResponse":
        """<p>Creates or updates the permissions policy for your registry.</p> <p>A registry policy is used to specify permissions for another Amazon Web Services account and is used when configuring cross-account replication. For more information, see <a href="https://docs.aws.amazon.com/AmazonECR/latest/userguide/registry-permissions.html">Registry permissions</a> in the <i>Amazon Elastic Container Registry User Guide</i>.</p>

        Args:
            policy_text: <p>The JSON policy text to apply to your registry. The policy text follows the same format as IAM policy text. For more information, see <a href="https://docs.aws.amazon.com/AmazonECR/latest/userguide/registry-permissions.html">Registry permissions</a> in the <i>Amazon Elastic Container Registry User Guide</i>.</p>

        Raises:
            capo_ecr.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter is invalid. Review the available parameters for the API request.</p>
            capo_ecr.errors.server_exception.ServerException: <p>These errors are usually caused by a server-side issue.</p>
            capo_ecr.errors.validation_exception.ValidationException: <p>There was an exception validating this request.</p>
            capo_ecr.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_ecr.types.put_registry_policy_request.PutRegistryPolicyRequest]",
        ) -> OperationResponse[
            "capo_ecr.types.put_registry_policy_response.PutRegistryPolicyResponse"
        ]:
            import capo_ecr._operations.amazon_ec2_container_registry_v20150921.put_registry_policy

            output, http_response = (
                capo_ecr._operations.amazon_ec2_container_registry_v20150921.put_registry_policy.put_registry_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ecr.types.put_registry_policy_request.PutRegistryPolicyRequest = {
            "policy_text": policy_text
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def put_registry_scanning_configuration(
        self,
        *,
        config_overrides: Optional[ECRClientConfig] = None,
        scan_type: Optional["capo_ecr.types.scan_type.ScanType"] = None,
        rules: Optional[
            "capo_ecr.types.registry_scanning_rule_list.RegistryScanningRuleList"
        ] = None,
    ) -> "capo_ecr.types.put_registry_scanning_configuration_response.PutRegistryScanningConfigurationResponse":
        """<p>Creates or updates the scanning configuration for your private registry.</p>

        Args:
            scan_type: <p>The scanning type to set for the registry.</p> <p>When a registry scanning configuration is not defined, by default the <code>BASIC</code> scan type is used. When basic scanning is used, you may specify filters to determine which individual repositories, or all repositories, are scanned when new images are pushed to those repositories. Alternatively, you can do manual scans of images with basic scanning.</p> <p>When the <code>ENHANCED</code> scan type is set, Amazon Inspector provides automated vulnerability scanning. You may choose between continuous scanning or scan on push and you may specify filters to determine which individual repositories, or all repositories, are scanned.</p>
            rules: <p>The scanning rules to use for the registry. A scanning rule is used to determine which repository filters are used and at what frequency scanning will occur.</p>

        Raises:
            capo_ecr.errors.blocked_by_organization_policy_exception.BlockedByOrganizationPolicyException: <p>The operation did not succeed because the account is managed by a organization policy.</p>
            capo_ecr.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter is invalid. Review the available parameters for the API request.</p>
            capo_ecr.errors.server_exception.ServerException: <p>These errors are usually caused by a server-side issue.</p>
            capo_ecr.errors.validation_exception.ValidationException: <p>There was an exception validating this request.</p>
            capo_ecr.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_ecr.types.put_registry_scanning_configuration_request.PutRegistryScanningConfigurationRequest]",
        ) -> OperationResponse[
            "capo_ecr.types.put_registry_scanning_configuration_response.PutRegistryScanningConfigurationResponse"
        ]:
            import capo_ecr._operations.amazon_ec2_container_registry_v20150921.put_registry_scanning_configuration

            output, http_response = (
                capo_ecr._operations.amazon_ec2_container_registry_v20150921.put_registry_scanning_configuration.put_registry_scanning_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ecr.types.put_registry_scanning_configuration_request.PutRegistryScanningConfigurationRequest = {}
        if scan_type is not None:
            input_["scan_type"] = scan_type
        if rules is not None:
            input_["rules"] = rules

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def put_replication_configuration(
        self,
        replication_configuration: "capo_ecr.types.replication_configuration.ReplicationConfiguration",
        *,
        config_overrides: Optional[ECRClientConfig] = None,
    ) -> "capo_ecr.types.put_replication_configuration_response.PutReplicationConfigurationResponse":
        """<p>Creates or updates the replication configuration for a registry. The existing replication configuration for a repository can be retrieved with the <a>DescribeRegistry</a> API action. The first time the PutReplicationConfiguration API is called, a service-linked IAM role is created in your account for the replication process. For more information, see <a href="https://docs.aws.amazon.com/AmazonECR/latest/userguide/using-service-linked-roles.html">Using service-linked roles for Amazon ECR</a> in the <i>Amazon Elastic Container Registry User Guide</i>. For more information on the custom role for replication, see <a href="https://docs.aws.amazon.com/AmazonECR/latest/userguide/replication-creation-templates.html#roles-creatingrole-user-console">Creating an IAM role for replication</a>.</p> <note> <p>When configuring cross-account replication, the destination account must grant the source account permission to replicate. This permission is controlled using a registry permissions policy. For more information, see <a>PutRegistryPolicy</a>.</p> </note>

        Args:
            replication_configuration: <p>An object representing the replication configuration for a registry.</p>

        Raises:
            capo_ecr.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter is invalid. Review the available parameters for the API request.</p>
            capo_ecr.errors.server_exception.ServerException: <p>These errors are usually caused by a server-side issue.</p>
            capo_ecr.errors.validation_exception.ValidationException: <p>There was an exception validating this request.</p>
            capo_ecr.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_ecr.types.put_replication_configuration_request.PutReplicationConfigurationRequest]",
        ) -> OperationResponse[
            "capo_ecr.types.put_replication_configuration_response.PutReplicationConfigurationResponse"
        ]:
            import capo_ecr._operations.amazon_ec2_container_registry_v20150921.put_replication_configuration

            output, http_response = (
                capo_ecr._operations.amazon_ec2_container_registry_v20150921.put_replication_configuration.put_replication_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ecr.types.put_replication_configuration_request.PutReplicationConfigurationRequest = {
            "replication_configuration": replication_configuration
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def put_signing_configuration(
        self,
        signing_configuration: "capo_ecr.types.signing_configuration.SigningConfiguration",
        *,
        config_overrides: Optional[ECRClientConfig] = None,
    ) -> "capo_ecr.types.put_signing_configuration_response.PutSigningConfigurationResponse":
        """<p>Creates or updates the registry's signing configuration, which defines rules for automatically signing images with Amazon Web Services Signer.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/AmazonECR/latest/userguide/managed-signing.html">Managed signing</a> in the <i>Amazon Elastic Container Registry User Guide</i>.</p> <note> <p>To successfully generate a signature, the IAM principal pushing images must have permission to sign payloads with the Amazon Web Services Signer signing profile referenced in the signing configuration.</p> </note>

        Args:
            signing_configuration: <p>The signing configuration to assign to the registry.</p>

        Raises:
            capo_ecr.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter is invalid. Review the available parameters for the API request.</p>
            capo_ecr.errors.server_exception.ServerException: <p>These errors are usually caused by a server-side issue.</p>
            capo_ecr.errors.validation_exception.ValidationException: <p>There was an exception validating this request.</p>
            capo_ecr.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_ecr.types.put_signing_configuration_request.PutSigningConfigurationRequest]",
        ) -> OperationResponse[
            "capo_ecr.types.put_signing_configuration_response.PutSigningConfigurationResponse"
        ]:
            import capo_ecr._operations.amazon_ec2_container_registry_v20150921.put_signing_configuration

            output, http_response = (
                capo_ecr._operations.amazon_ec2_container_registry_v20150921.put_signing_configuration.put_signing_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ecr.types.put_signing_configuration_request.PutSigningConfigurationRequest = {
            "signing_configuration": signing_configuration
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def register_pull_time_update_exclusion(
        self,
        principal_arn: "capo_ecr.types.principal_arn.PrincipalArn",
        *,
        config_overrides: Optional[ECRClientConfig] = None,
    ) -> "capo_ecr.types.register_pull_time_update_exclusion_response.RegisterPullTimeUpdateExclusionResponse":
        """<p>Adds an IAM principal to the pull time update exclusion list for a registry. Amazon ECR will not record the pull time if an excluded principal pulls an image.</p>

        Args:
            principal_arn: <p>The ARN of the IAM principal to exclude from having image pull times recorded.</p>

        Raises:
            capo_ecr.errors.exclusion_already_exists_exception.ExclusionAlreadyExistsException: <p>The specified pull time update exclusion already exists for the registry.</p>
            capo_ecr.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter is invalid. Review the available parameters for the API request.</p>
            capo_ecr.errors.limit_exceeded_exception.LimitExceededException: <p>The operation did not succeed because it would have exceeded a service limit for your account. For more information, see <a href="https://docs.aws.amazon.com/AmazonECR/latest/userguide/service-quotas.html">Amazon ECR service quotas</a> in the Amazon Elastic Container Registry User Guide.</p>
            capo_ecr.errors.server_exception.ServerException: <p>These errors are usually caused by a server-side issue.</p>
            capo_ecr.errors.validation_exception.ValidationException: <p>There was an exception validating this request.</p>
            capo_ecr.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_ecr.types.register_pull_time_update_exclusion_request.RegisterPullTimeUpdateExclusionRequest]",
        ) -> OperationResponse[
            "capo_ecr.types.register_pull_time_update_exclusion_response.RegisterPullTimeUpdateExclusionResponse"
        ]:
            import capo_ecr._operations.amazon_ec2_container_registry_v20150921.register_pull_time_update_exclusion

            output, http_response = (
                capo_ecr._operations.amazon_ec2_container_registry_v20150921.register_pull_time_update_exclusion.register_pull_time_update_exclusion(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ecr.types.register_pull_time_update_exclusion_request.RegisterPullTimeUpdateExclusionRequest = {
            "principal_arn": principal_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def set_repository_policy(
        self,
        repository_name: "capo_ecr.types.repository_name.RepositoryName",
        policy_text: "capo_ecr.types.repository_policy_text.RepositoryPolicyText",
        *,
        config_overrides: Optional[ECRClientConfig] = None,
        registry_id: Optional["capo_ecr.types.registry_id.RegistryId"] = None,
        force: Optional["capo_ecr.types.force_flag.ForceFlag"] = None,
    ) -> "capo_ecr.types.set_repository_policy_response.SetRepositoryPolicyResponse":
        """<p>Applies a repository policy to the specified repository to control access permissions. For more information, see <a href="https://docs.aws.amazon.com/AmazonECR/latest/userguide/repository-policies.html">Amazon ECR Repository policies</a> in the <i>Amazon Elastic Container Registry User Guide</i>.</p>

        Args:
            registry_id: <p>The Amazon Web Services account ID associated with the registry that contains the repository. If you do not specify a registry, the default registry is assumed.</p>
            repository_name: <p>The name of the repository to receive the policy.</p>
            policy_text: <p>The JSON repository policy text to apply to the repository. For more information, see <a href="https://docs.aws.amazon.com/AmazonECR/latest/userguide/repository-policy-examples.html">Amazon ECR repository policies</a> in the <i>Amazon Elastic Container Registry User Guide</i>.</p>
            force: <p>If the policy you are attempting to set on a repository policy would prevent you from setting another policy in the future, you must force the <a>SetRepositoryPolicy</a> operation. This is intended to prevent accidental repository lock outs.</p>

        Raises:
            capo_ecr.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter is invalid. Review the available parameters for the API request.</p>
            capo_ecr.errors.repository_not_found_exception.RepositoryNotFoundException: <p>The specified repository could not be found. Check the spelling of the specified repository and ensure that you are performing operations on the correct registry.</p>
            capo_ecr.errors.server_exception.ServerException: <p>These errors are usually caused by a server-side issue.</p>
            capo_ecr.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_ecr.types.set_repository_policy_request.SetRepositoryPolicyRequest]",
        ) -> OperationResponse[
            "capo_ecr.types.set_repository_policy_response.SetRepositoryPolicyResponse"
        ]:
            import capo_ecr._operations.amazon_ec2_container_registry_v20150921.set_repository_policy

            output, http_response = (
                capo_ecr._operations.amazon_ec2_container_registry_v20150921.set_repository_policy.set_repository_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ecr.types.set_repository_policy_request.SetRepositoryPolicyRequest = {
            "repository_name": repository_name,
            "policy_text": policy_text,
        }
        if registry_id is not None:
            input_["registry_id"] = registry_id
        if force is not None:
            input_["force"] = force

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def start_image_scan(
        self,
        repository_name: "capo_ecr.types.repository_name.RepositoryName",
        image_id: "capo_ecr.types.image_identifier.ImageIdentifier",
        *,
        config_overrides: Optional[ECRClientConfig] = None,
        registry_id: Optional["capo_ecr.types.registry_id.RegistryId"] = None,
    ) -> "capo_ecr.types.start_image_scan_response.StartImageScanResponse":
        """<p>Starts a basic image vulnerability scan.</p> <p> A basic image scan can only be started once per 24 hours on an individual image. This limit includes if an image was scanned on initial push. You can start up to 100,000 basic scans per 24 hours. This limit includes both scans on initial push and scans initiated by the StartImageScan API. For more information, see <a href="https://docs.aws.amazon.com/AmazonECR/latest/userguide/image-scanning-basic.html">Basic scanning</a> in the <i>Amazon Elastic Container Registry User Guide</i>.</p>

        Args:
            registry_id: <p>The Amazon Web Services account ID associated with the registry that contains the repository in which to start an image scan request. If you do not specify a registry, the default registry is assumed.</p>
            repository_name: <p>The name of the repository that contains the images to scan.</p>

        Raises:
            capo_ecr.errors.image_archived_exception.ImageArchivedException: <p>The specified image is archived and cannot be scanned.</p>
            capo_ecr.errors.image_not_found_exception.ImageNotFoundException: <p>The image requested does not exist in the specified repository.</p>
            capo_ecr.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter is invalid. Review the available parameters for the API request.</p>
            capo_ecr.errors.limit_exceeded_exception.LimitExceededException: <p>The operation did not succeed because it would have exceeded a service limit for your account. For more information, see <a href="https://docs.aws.amazon.com/AmazonECR/latest/userguide/service-quotas.html">Amazon ECR service quotas</a> in the Amazon Elastic Container Registry User Guide.</p>
            capo_ecr.errors.repository_not_found_exception.RepositoryNotFoundException: <p>The specified repository could not be found. Check the spelling of the specified repository and ensure that you are performing operations on the correct registry.</p>
            capo_ecr.errors.server_exception.ServerException: <p>These errors are usually caused by a server-side issue.</p>
            capo_ecr.errors.unsupported_image_type_exception.UnsupportedImageTypeException: <p>The image is of a type that cannot be scanned.</p>
            capo_ecr.errors.validation_exception.ValidationException: <p>There was an exception validating this request.</p>
            capo_ecr.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_ecr.types.start_image_scan_request.StartImageScanRequest]",
        ) -> OperationResponse[
            "capo_ecr.types.start_image_scan_response.StartImageScanResponse"
        ]:
            import capo_ecr._operations.amazon_ec2_container_registry_v20150921.start_image_scan

            output, http_response = (
                capo_ecr._operations.amazon_ec2_container_registry_v20150921.start_image_scan.start_image_scan(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ecr.types.start_image_scan_request.StartImageScanRequest = {
            "repository_name": repository_name,
            "image_id": image_id,
        }
        if registry_id is not None:
            input_["registry_id"] = registry_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def start_lifecycle_policy_preview(
        self,
        repository_name: "capo_ecr.types.repository_name.RepositoryName",
        *,
        config_overrides: Optional[ECRClientConfig] = None,
        registry_id: Optional["capo_ecr.types.registry_id.RegistryId"] = None,
        lifecycle_policy_text: Optional[
            "capo_ecr.types.lifecycle_policy_text.LifecyclePolicyText"
        ] = None,
    ) -> "capo_ecr.types.start_lifecycle_policy_preview_response.StartLifecyclePolicyPreviewResponse":
        """<p>Starts a preview of a lifecycle policy for the specified repository. This allows you to see the results before associating the lifecycle policy with the repository.</p>

        Args:
            registry_id: <p>The Amazon Web Services account ID associated with the registry that contains the repository. If you do not specify a registry, the default registry is assumed.</p>
            repository_name: <p>The name of the repository to be evaluated.</p>
            lifecycle_policy_text: <p>The policy to be evaluated against. If you do not specify a policy, the current policy for the repository is used.</p>

        Raises:
            capo_ecr.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter is invalid. Review the available parameters for the API request.</p>
            capo_ecr.errors.lifecycle_policy_not_found_exception.LifecyclePolicyNotFoundException: <p>The lifecycle policy could not be found, and no policy is set to the repository.</p>
            capo_ecr.errors.lifecycle_policy_preview_in_progress_exception.LifecyclePolicyPreviewInProgressException: <p>The previous lifecycle policy preview request has not completed. Wait and try again.</p>
            capo_ecr.errors.repository_not_found_exception.RepositoryNotFoundException: <p>The specified repository could not be found. Check the spelling of the specified repository and ensure that you are performing operations on the correct registry.</p>
            capo_ecr.errors.server_exception.ServerException: <p>These errors are usually caused by a server-side issue.</p>
            capo_ecr.errors.validation_exception.ValidationException: <p>There was an exception validating this request.</p>
            capo_ecr.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_ecr.types.start_lifecycle_policy_preview_request.StartLifecyclePolicyPreviewRequest]",
        ) -> OperationResponse[
            "capo_ecr.types.start_lifecycle_policy_preview_response.StartLifecyclePolicyPreviewResponse"
        ]:
            import capo_ecr._operations.amazon_ec2_container_registry_v20150921.start_lifecycle_policy_preview

            output, http_response = (
                capo_ecr._operations.amazon_ec2_container_registry_v20150921.start_lifecycle_policy_preview.start_lifecycle_policy_preview(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ecr.types.start_lifecycle_policy_preview_request.StartLifecyclePolicyPreviewRequest = {
            "repository_name": repository_name
        }
        if registry_id is not None:
            input_["registry_id"] = registry_id
        if lifecycle_policy_text is not None:
            input_["lifecycle_policy_text"] = lifecycle_policy_text

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def tag_resource(
        self,
        resource_arn: "capo_ecr.types.arn.Arn",
        tags: "capo_ecr.types.tag_list.TagList",
        *,
        config_overrides: Optional[ECRClientConfig] = None,
    ) -> "capo_ecr.types.tag_resource_response.TagResourceResponse":
        """<p>Adds specified tags to a resource with the specified ARN. Existing tags on a resource are not changed if they are not specified in the request parameters.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the the resource to which to add tags. Currently, the only supported resource is an Amazon ECR repository.</p>
            tags: <p>The tags to add to the resource. A tag is an array of key-value pairs. Tag keys can have a maximum character length of 128 characters, and tag values can have a maximum length of 256 characters.</p>

        Raises:
            capo_ecr.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter is invalid. Review the available parameters for the API request.</p>
            capo_ecr.errors.invalid_tag_parameter_exception.InvalidTagParameterException: <p>An invalid parameter has been specified. Tag keys can have a maximum character length of 128 characters, and tag values can have a maximum length of 256 characters.</p>
            capo_ecr.errors.repository_not_found_exception.RepositoryNotFoundException: <p>The specified repository could not be found. Check the spelling of the specified repository and ensure that you are performing operations on the correct registry.</p>
            capo_ecr.errors.server_exception.ServerException: <p>These errors are usually caused by a server-side issue.</p>
            capo_ecr.errors.too_many_tags_exception.TooManyTagsException: <p>The list of tags on the repository is over the limit. The maximum number of tags that can be applied to a repository is 50.</p>
            capo_ecr.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_ecr.types.tag_resource_request.TagResourceRequest]",
        ) -> OperationResponse[
            "capo_ecr.types.tag_resource_response.TagResourceResponse"
        ]:
            import capo_ecr._operations.amazon_ec2_container_registry_v20150921.tag_resource

            output, http_response = (
                capo_ecr._operations.amazon_ec2_container_registry_v20150921.tag_resource.tag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ecr.types.tag_resource_request.TagResourceRequest = {
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
        resource_arn: "capo_ecr.types.arn.Arn",
        tag_keys: "capo_ecr.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[ECRClientConfig] = None,
    ) -> "capo_ecr.types.untag_resource_response.UntagResourceResponse":
        """<p>Deletes specified tags from a resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource from which to remove tags. Currently, the only supported resource is an Amazon ECR repository.</p>
            tag_keys: <p>The keys of the tags to be removed.</p>

        Raises:
            capo_ecr.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter is invalid. Review the available parameters for the API request.</p>
            capo_ecr.errors.invalid_tag_parameter_exception.InvalidTagParameterException: <p>An invalid parameter has been specified. Tag keys can have a maximum character length of 128 characters, and tag values can have a maximum length of 256 characters.</p>
            capo_ecr.errors.repository_not_found_exception.RepositoryNotFoundException: <p>The specified repository could not be found. Check the spelling of the specified repository and ensure that you are performing operations on the correct registry.</p>
            capo_ecr.errors.server_exception.ServerException: <p>These errors are usually caused by a server-side issue.</p>
            capo_ecr.errors.too_many_tags_exception.TooManyTagsException: <p>The list of tags on the repository is over the limit. The maximum number of tags that can be applied to a repository is 50.</p>
            capo_ecr.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_ecr.types.untag_resource_request.UntagResourceRequest]",
        ) -> OperationResponse[
            "capo_ecr.types.untag_resource_response.UntagResourceResponse"
        ]:
            import capo_ecr._operations.amazon_ec2_container_registry_v20150921.untag_resource

            output, http_response = (
                capo_ecr._operations.amazon_ec2_container_registry_v20150921.untag_resource.untag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ecr.types.untag_resource_request.UntagResourceRequest = {
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

    def update_image_storage_class(
        self,
        repository_name: "capo_ecr.types.repository_name.RepositoryName",
        image_id: "capo_ecr.types.image_identifier.ImageIdentifier",
        target_storage_class: "capo_ecr.types.target_storage_class.TargetStorageClass",
        *,
        config_overrides: Optional[ECRClientConfig] = None,
        registry_id: Optional["capo_ecr.types.registry_id.RegistryId"] = None,
    ) -> "capo_ecr.types.update_image_storage_class_response.UpdateImageStorageClassResponse":
        """<p>Transitions an image between storage classes. You can transition images from Amazon ECR standard storage class to Amazon ECR archival storage class for long-term storage, or restore archived images back to Amazon ECR standard.</p>

        Args:
            registry_id: <p>The Amazon Web Services account ID associated with the registry that contains the image to transition. If you do not specify a registry, the default registry is assumed.</p>
            repository_name: <p>The name of the repository that contains the image to transition.</p>
            target_storage_class: <p>The target storage class for the image.</p>

        Raises:
            capo_ecr.errors.image_not_found_exception.ImageNotFoundException: <p>The image requested does not exist in the specified repository.</p>
            capo_ecr.errors.image_storage_class_update_not_supported_exception.ImageStorageClassUpdateNotSupportedException: <p>The requested image storage class update is not supported.</p>
            capo_ecr.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter is invalid. Review the available parameters for the API request.</p>
            capo_ecr.errors.repository_not_found_exception.RepositoryNotFoundException: <p>The specified repository could not be found. Check the spelling of the specified repository and ensure that you are performing operations on the correct registry.</p>
            capo_ecr.errors.server_exception.ServerException: <p>These errors are usually caused by a server-side issue.</p>
            capo_ecr.errors.validation_exception.ValidationException: <p>There was an exception validating this request.</p>
            capo_ecr.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To transition an image to Amazon ECR Archive
            This example transitions an image with a specific digest in the hello-repository repository to Amazon ECR Archive storage for long-term archival.

            >>> client.update_image_storage_class(registry_id='724772093679', repository_name='hello-repository', image_id={'imageDigest': 'sha256:0b1a4e0c81c434fa7928e5c4a2651a521ebabc4ff200c65f7e25b99373efca3b'}, target_storage_class='ARCHIVE')
            To restore an archived image to Amazon ECR Standard
            This example restores an archived image with a specific digest back to Amazon ECR Standard storage.

            >>> client.update_image_storage_class(registry_id='724772093679', repository_name='hello-repository', image_id={'imageDigest': 'sha256:0b1a4e0c81c434fa7928e5c4a2651a521ebabc4ff200c65f7e25b99373efca3b'}, target_storage_class='STANDARD')
        """

        def _handler(
            req: "OperationRequest[capo_ecr.types.update_image_storage_class_request.UpdateImageStorageClassRequest]",
        ) -> OperationResponse[
            "capo_ecr.types.update_image_storage_class_response.UpdateImageStorageClassResponse"
        ]:
            import capo_ecr._operations.amazon_ec2_container_registry_v20150921.update_image_storage_class

            output, http_response = (
                capo_ecr._operations.amazon_ec2_container_registry_v20150921.update_image_storage_class.update_image_storage_class(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ecr.types.update_image_storage_class_request.UpdateImageStorageClassRequest = {
            "repository_name": repository_name,
            "image_id": image_id,
            "target_storage_class": target_storage_class,
        }
        if registry_id is not None:
            input_["registry_id"] = registry_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_pull_through_cache_rule(
        self,
        ecr_repository_prefix: "capo_ecr.types.pull_through_cache_rule_repository_prefix.PullThroughCacheRuleRepositoryPrefix",
        *,
        config_overrides: Optional[ECRClientConfig] = None,
        registry_id: Optional["capo_ecr.types.registry_id.RegistryId"] = None,
        credential_arn: Optional["capo_ecr.types.credential_arn.CredentialArn"] = None,
        custom_role_arn: Optional[
            "capo_ecr.types.custom_role_arn.CustomRoleArn"
        ] = None,
    ) -> "capo_ecr.types.update_pull_through_cache_rule_response.UpdatePullThroughCacheRuleResponse":
        """<p>Updates an existing pull through cache rule.</p>

        Args:
            registry_id: <p>The Amazon Web Services account ID associated with the registry associated with the pull through cache rule. If you do not specify a registry, the default registry is assumed.</p>
            ecr_repository_prefix: <p>The repository name prefix to use when caching images from the source registry.</p>
            credential_arn: <p>The Amazon Resource Name (ARN) of the Amazon Web Services Secrets Manager secret that identifies the credentials to authenticate to the upstream registry.</p>
            custom_role_arn: <p>Amazon Resource Name (ARN) of the IAM role to be assumed by Amazon ECR to authenticate to the ECR upstream registry. This role must be in the same account as the registry that you are configuring.</p>

        Raises:
            capo_ecr.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter is invalid. Review the available parameters for the API request.</p>
            capo_ecr.errors.pull_through_cache_rule_not_found_exception.PullThroughCacheRuleNotFoundException: <p>The pull through cache rule was not found. Specify a valid pull through cache rule and try again.</p>
            capo_ecr.errors.secret_not_found_exception.SecretNotFoundException: <p>The ARN of the secret specified in the pull through cache rule was not found. Update the pull through cache rule with a valid secret ARN and try again.</p>
            capo_ecr.errors.server_exception.ServerException: <p>These errors are usually caused by a server-side issue.</p>
            capo_ecr.errors.unable_to_access_secret_exception.UnableToAccessSecretException: <p>The secret is unable to be accessed. Verify the resource permissions for the secret and try again.</p>
            capo_ecr.errors.unable_to_decrypt_secret_value_exception.UnableToDecryptSecretValueException: <p>The secret is accessible but is unable to be decrypted. Verify the resource permisisons and try again.</p>
            capo_ecr.errors.validation_exception.ValidationException: <p>There was an exception validating this request.</p>
            capo_ecr.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_ecr.types.update_pull_through_cache_rule_request.UpdatePullThroughCacheRuleRequest]",
        ) -> OperationResponse[
            "capo_ecr.types.update_pull_through_cache_rule_response.UpdatePullThroughCacheRuleResponse"
        ]:
            import capo_ecr._operations.amazon_ec2_container_registry_v20150921.update_pull_through_cache_rule

            output, http_response = (
                capo_ecr._operations.amazon_ec2_container_registry_v20150921.update_pull_through_cache_rule.update_pull_through_cache_rule(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ecr.types.update_pull_through_cache_rule_request.UpdatePullThroughCacheRuleRequest = {
            "ecr_repository_prefix": ecr_repository_prefix
        }
        if registry_id is not None:
            input_["registry_id"] = registry_id
        if credential_arn is not None:
            input_["credential_arn"] = credential_arn
        if custom_role_arn is not None:
            input_["custom_role_arn"] = custom_role_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_repository_creation_template(
        self,
        prefix: "capo_ecr.types.prefix.Prefix",
        *,
        config_overrides: Optional[ECRClientConfig] = None,
        description: Optional[
            "capo_ecr.types.repository_template_description.RepositoryTemplateDescription"
        ] = None,
        encryption_configuration: Optional[
            "capo_ecr.types.encryption_configuration_for_repository_creation_template.EncryptionConfigurationForRepositoryCreationTemplate"
        ] = None,
        resource_tags: Optional["capo_ecr.types.tag_list.TagList"] = None,
        image_tag_mutability: Optional[
            "capo_ecr.types.image_tag_mutability.ImageTagMutability"
        ] = None,
        image_tag_mutability_exclusion_filters: Optional[
            "capo_ecr.types.image_tag_mutability_exclusion_filters.ImageTagMutabilityExclusionFilters"
        ] = None,
        repository_policy: Optional[
            "capo_ecr.types.repository_policy_text.RepositoryPolicyText"
        ] = None,
        lifecycle_policy: Optional[
            "capo_ecr.types.lifecycle_policy_text_for_repository_creation_template.LifecyclePolicyTextForRepositoryCreationTemplate"
        ] = None,
        applied_for: Optional[
            "capo_ecr.types.rct_applied_for_list.RCTAppliedForList"
        ] = None,
        custom_role_arn: Optional[
            "capo_ecr.types.custom_role_arn.CustomRoleArn"
        ] = None,
    ) -> "capo_ecr.types.update_repository_creation_template_response.UpdateRepositoryCreationTemplateResponse":
        """<p>Updates an existing repository creation template.</p>

        Args:
            prefix: <p>The repository namespace prefix that matches an existing repository creation template in the registry. All repositories created using this namespace prefix will have the settings defined in this template applied. For example, a prefix of <code>prod</code> would apply to all repositories beginning with <code>prod/</code>. This includes a repository named <code>prod/team1</code> as well as a repository named <code>prod/repository1</code>.</p> <p>To apply a template to all repositories in your registry that don't have an associated creation template, you can use <code>ROOT</code> as the prefix.</p>
            description: <p>A description for the repository creation template.</p>
            resource_tags: <p>The metadata to apply to the repository to help you categorize and organize. Each tag consists of a key and an optional value, both of which you define. Tag keys can have a maximum character length of 128 characters, and tag values can have a maximum length of 256 characters.</p>
            image_tag_mutability: <p>Updates the tag mutability setting for the repository. If this parameter is omitted, the default setting of <code>MUTABLE</code> will be used which will allow image tags to be overwritten. If <code>IMMUTABLE</code> is specified, all image tags within the repository will be immutable which will prevent them from being overwritten.</p>
            image_tag_mutability_exclusion_filters: <p>A list of filters that specify which image tags should be excluded from the repository creation template's image tag mutability setting.</p>
            repository_policy: <p>Updates the repository policy created using the template. A repository policy is a permissions policy associated with a repository to control access permissions. </p>
            lifecycle_policy: <p>Updates the lifecycle policy associated with the specified repository creation template.</p>
            applied_for: <p>Updates the list of enumerable strings representing the Amazon ECR repository creation scenarios that this template will apply towards. The supported scenarios are <code>PULL_THROUGH_CACHE</code>, <code>REPLICATION</code>, and <code>CREATE_ON_PUSH</code> </p>
            custom_role_arn: <p>The ARN of the role to be assumed by Amazon ECR. This role must be in the same account as the registry that you are configuring. Amazon ECR will assume your supplied role when the customRoleArn is specified. When this field isn't specified, Amazon ECR will use the service-linked role for the repository creation template.</p>

        Raises:
            capo_ecr.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter is invalid. Review the available parameters for the API request.</p>
            capo_ecr.errors.server_exception.ServerException: <p>These errors are usually caused by a server-side issue.</p>
            capo_ecr.errors.template_not_found_exception.TemplateNotFoundException: <p>The specified repository creation template can't be found. Verify the registry ID and prefix and try again.</p>
            capo_ecr.errors.validation_exception.ValidationException: <p>There was an exception validating this request.</p>
            capo_ecr.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_ecr.types.update_repository_creation_template_request.UpdateRepositoryCreationTemplateRequest]",
        ) -> OperationResponse[
            "capo_ecr.types.update_repository_creation_template_response.UpdateRepositoryCreationTemplateResponse"
        ]:
            import capo_ecr._operations.amazon_ec2_container_registry_v20150921.update_repository_creation_template

            output, http_response = (
                capo_ecr._operations.amazon_ec2_container_registry_v20150921.update_repository_creation_template.update_repository_creation_template(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ecr.types.update_repository_creation_template_request.UpdateRepositoryCreationTemplateRequest = {
            "prefix": prefix
        }
        if description is not None:
            input_["description"] = description
        if encryption_configuration is not None:
            input_["encryption_configuration"] = encryption_configuration
        if resource_tags is not None:
            input_["resource_tags"] = resource_tags
        if image_tag_mutability is not None:
            input_["image_tag_mutability"] = image_tag_mutability
        if image_tag_mutability_exclusion_filters is not None:
            input_["image_tag_mutability_exclusion_filters"] = (
                image_tag_mutability_exclusion_filters
            )
        if repository_policy is not None:
            input_["repository_policy"] = repository_policy
        if lifecycle_policy is not None:
            input_["lifecycle_policy"] = lifecycle_policy
        if applied_for is not None:
            input_["applied_for"] = applied_for
        if custom_role_arn is not None:
            input_["custom_role_arn"] = custom_role_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def upload_layer_part(
        self,
        repository_name: "capo_ecr.types.repository_name.RepositoryName",
        upload_id: "capo_ecr.types.upload_id.UploadId",
        part_first_byte: "capo_ecr.types.part_size.PartSize",
        part_last_byte: "capo_ecr.types.part_size.PartSize",
        layer_part_blob: "capo_ecr.types.layer_part_blob.LayerPartBlob",
        *,
        config_overrides: Optional[ECRClientConfig] = None,
        registry_id: Optional["capo_ecr.types.registry_id.RegistryId"] = None,
    ) -> "capo_ecr.types.upload_layer_part_response.UploadLayerPartResponse":
        """<p>Uploads an image layer part to Amazon ECR.</p> <p>When an image is pushed, each new image layer is uploaded in parts. The maximum size of each image layer part can be 20971520 bytes (or about 20MB). The UploadLayerPart API is called once per each new image layer part.</p> <note> <p>This operation is used by the Amazon ECR proxy and is not generally used by customers for pulling and pushing images. In most cases, you should use the <code>docker</code> CLI to pull, tag, and push images.</p> </note>

        Args:
            registry_id: <p>The Amazon Web Services account ID associated with the registry to which you are uploading layer parts. If you do not specify a registry, the default registry is assumed.</p>
            repository_name: <p>The name of the repository to which you are uploading layer parts.</p>
            upload_id: <p>The upload ID from a previous <a>InitiateLayerUpload</a> operation to associate with the layer part upload.</p>
            part_first_byte: <p>The position of the first byte of the layer part witin the overall image layer.</p>
            part_last_byte: <p>The position of the last byte of the layer part within the overall image layer.</p>
            layer_part_blob: <p>The base64-encoded layer part payload.</p>

        Raises:
            capo_ecr.errors.invalid_layer_part_exception.InvalidLayerPartException: <p>The layer part size is not valid, or the first byte specified is not consecutive to the last byte of a previous layer part upload.</p>
            capo_ecr.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter is invalid. Review the available parameters for the API request.</p>
            capo_ecr.errors.kms_exception.KmsException: <p>The operation failed due to a KMS exception.</p>
            capo_ecr.errors.limit_exceeded_exception.LimitExceededException: <p>The operation did not succeed because it would have exceeded a service limit for your account. For more information, see <a href="https://docs.aws.amazon.com/AmazonECR/latest/userguide/service-quotas.html">Amazon ECR service quotas</a> in the Amazon Elastic Container Registry User Guide.</p>
            capo_ecr.errors.repository_not_found_exception.RepositoryNotFoundException: <p>The specified repository could not be found. Check the spelling of the specified repository and ensure that you are performing operations on the correct registry.</p>
            capo_ecr.errors.server_exception.ServerException: <p>These errors are usually caused by a server-side issue.</p>
            capo_ecr.errors.upload_not_found_exception.UploadNotFoundException: <p>The upload could not be found, or the specified upload ID is not valid for this repository.</p>
            capo_ecr.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_ecr.types.upload_layer_part_request.UploadLayerPartRequest]",
        ) -> OperationResponse[
            "capo_ecr.types.upload_layer_part_response.UploadLayerPartResponse"
        ]:
            import capo_ecr._operations.amazon_ec2_container_registry_v20150921.upload_layer_part

            output, http_response = (
                capo_ecr._operations.amazon_ec2_container_registry_v20150921.upload_layer_part.upload_layer_part(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ecr.types.upload_layer_part_request.UploadLayerPartRequest = {
            "repository_name": repository_name,
            "upload_id": upload_id,
            "part_first_byte": part_first_byte,
            "part_last_byte": part_last_byte,
            "layer_part_blob": layer_part_blob,
        }
        if registry_id is not None:
            input_["registry_id"] = registry_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def validate_pull_through_cache_rule(
        self,
        ecr_repository_prefix: "capo_ecr.types.pull_through_cache_rule_repository_prefix.PullThroughCacheRuleRepositoryPrefix",
        *,
        config_overrides: Optional[ECRClientConfig] = None,
        registry_id: Optional["capo_ecr.types.registry_id.RegistryId"] = None,
    ) -> "capo_ecr.types.validate_pull_through_cache_rule_response.ValidatePullThroughCacheRuleResponse":
        """<p>Validates an existing pull through cache rule for an upstream registry that requires authentication. This will retrieve the contents of the Amazon Web Services Secrets Manager secret, verify the syntax, and then validate that authentication to the upstream registry is successful.</p>

        Args:
            ecr_repository_prefix: <p>The repository name prefix associated with the pull through cache rule.</p>
            registry_id: <p>The registry ID associated with the pull through cache rule. If you do not specify a registry, the default registry is assumed.</p>

        Raises:
            capo_ecr.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter is invalid. Review the available parameters for the API request.</p>
            capo_ecr.errors.pull_through_cache_rule_not_found_exception.PullThroughCacheRuleNotFoundException: <p>The pull through cache rule was not found. Specify a valid pull through cache rule and try again.</p>
            capo_ecr.errors.server_exception.ServerException: <p>These errors are usually caused by a server-side issue.</p>
            capo_ecr.errors.validation_exception.ValidationException: <p>There was an exception validating this request.</p>
            capo_ecr.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_ecr.types.validate_pull_through_cache_rule_request.ValidatePullThroughCacheRuleRequest]",
        ) -> OperationResponse[
            "capo_ecr.types.validate_pull_through_cache_rule_response.ValidatePullThroughCacheRuleResponse"
        ]:
            import capo_ecr._operations.amazon_ec2_container_registry_v20150921.validate_pull_through_cache_rule

            output, http_response = (
                capo_ecr._operations.amazon_ec2_container_registry_v20150921.validate_pull_through_cache_rule.validate_pull_through_cache_rule(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ecr.types.validate_pull_through_cache_rule_request.ValidatePullThroughCacheRuleRequest = {
            "ecr_repository_prefix": ecr_repository_prefix
        }
        if registry_id is not None:
            input_["registry_id"] = registry_id

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
