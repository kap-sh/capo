"""Generated from Smithy shape ``com.amazonaws.ecrpublic#SpencerFrontendService``."""

import warnings
from collections.abc import Iterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import BaseHandler, Client

import capo_ecr_public._auth._signers
import capo_ecr_public._auth._sigv4
from capo_ecr_public._auth._identity import Credentials
from capo_ecr_public._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_ecr_public._auth._zapros_handler import AuthMiddleware
from capo_ecr_public._pagination import resolve_path as _resolve_path
from capo_ecr_public._services._aws_config import aws_config
from capo_ecr_public._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import capo_ecr_public.types.arn
    import capo_ecr_public.types.batch_check_layer_availability_request
    import capo_ecr_public.types.batch_check_layer_availability_response
    import capo_ecr_public.types.batch_delete_image_request
    import capo_ecr_public.types.batch_delete_image_response
    import capo_ecr_public.types.batched_operation_layer_digest_list
    import capo_ecr_public.types.complete_layer_upload_request
    import capo_ecr_public.types.complete_layer_upload_response
    import capo_ecr_public.types.create_repository_request
    import capo_ecr_public.types.create_repository_response
    import capo_ecr_public.types.delete_repository_policy_request
    import capo_ecr_public.types.delete_repository_policy_response
    import capo_ecr_public.types.delete_repository_request
    import capo_ecr_public.types.delete_repository_response
    import capo_ecr_public.types.describe_image_tags_request
    import capo_ecr_public.types.describe_image_tags_response
    import capo_ecr_public.types.describe_images_request
    import capo_ecr_public.types.describe_images_response
    import capo_ecr_public.types.describe_registries_request
    import capo_ecr_public.types.describe_registries_response
    import capo_ecr_public.types.describe_repositories_request
    import capo_ecr_public.types.describe_repositories_response
    import capo_ecr_public.types.force_flag
    import capo_ecr_public.types.get_authorization_token_request
    import capo_ecr_public.types.get_authorization_token_response
    import capo_ecr_public.types.get_registry_catalog_data_request
    import capo_ecr_public.types.get_registry_catalog_data_response
    import capo_ecr_public.types.get_repository_catalog_data_request
    import capo_ecr_public.types.get_repository_catalog_data_response
    import capo_ecr_public.types.get_repository_policy_request
    import capo_ecr_public.types.get_repository_policy_response
    import capo_ecr_public.types.image_detail
    import capo_ecr_public.types.image_digest
    import capo_ecr_public.types.image_identifier_list
    import capo_ecr_public.types.image_manifest
    import capo_ecr_public.types.image_tag
    import capo_ecr_public.types.image_tag_detail
    import capo_ecr_public.types.initiate_layer_upload_request
    import capo_ecr_public.types.initiate_layer_upload_response
    import capo_ecr_public.types.layer_digest_list
    import capo_ecr_public.types.layer_part_blob
    import capo_ecr_public.types.list_tags_for_resource_request
    import capo_ecr_public.types.list_tags_for_resource_response
    import capo_ecr_public.types.max_results
    import capo_ecr_public.types.media_type
    import capo_ecr_public.types.next_token
    import capo_ecr_public.types.part_size
    import capo_ecr_public.types.put_image_request
    import capo_ecr_public.types.put_image_response
    import capo_ecr_public.types.put_registry_catalog_data_request
    import capo_ecr_public.types.put_registry_catalog_data_response
    import capo_ecr_public.types.put_repository_catalog_data_request
    import capo_ecr_public.types.put_repository_catalog_data_response
    import capo_ecr_public.types.registry
    import capo_ecr_public.types.registry_display_name
    import capo_ecr_public.types.registry_id
    import capo_ecr_public.types.registry_id_or_alias
    import capo_ecr_public.types.repository
    import capo_ecr_public.types.repository_catalog_data_input
    import capo_ecr_public.types.repository_name
    import capo_ecr_public.types.repository_name_list
    import capo_ecr_public.types.repository_policy_text
    import capo_ecr_public.types.set_repository_policy_request
    import capo_ecr_public.types.set_repository_policy_response
    import capo_ecr_public.types.tag_key_list
    import capo_ecr_public.types.tag_list
    import capo_ecr_public.types.tag_resource_request
    import capo_ecr_public.types.tag_resource_response
    import capo_ecr_public.types.untag_resource_request
    import capo_ecr_public.types.untag_resource_response
    import capo_ecr_public.types.upload_id
    import capo_ecr_public.types.upload_layer_part_request
    import capo_ecr_public.types.upload_layer_part_response


class ECRPUBLICClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None
    anonymous: bool | None


class ECRPUBLICClient:
    """A client for the ``ECRPUBLIC`` service.

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
        self._config = ECRPUBLICClientConfig(
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
        self, config_overrides: Optional[ECRPUBLICClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: ECRPUBLICClientConfig = config_overrides or {}
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

    def batch_check_layer_availability(
        self,
        repository_name: "capo_ecr_public.types.repository_name.RepositoryName",
        layer_digests: "capo_ecr_public.types.batched_operation_layer_digest_list.BatchedOperationLayerDigestList",
        *,
        config_overrides: Optional[ECRPUBLICClientConfig] = None,
        registry_id: Optional[
            "capo_ecr_public.types.registry_id_or_alias.RegistryIdOrAlias"
        ] = None,
    ) -> "capo_ecr_public.types.batch_check_layer_availability_response.BatchCheckLayerAvailabilityResponse":
        """<p>Checks the availability of one or more image layers that are within a repository in a public registry. When an image is pushed to a repository, each image layer is checked to verify if it has been uploaded before. If it has been uploaded, then the image layer is skipped.</p> <note> <p>This operation is used by the Amazon ECR proxy and is not generally used by customers for pulling and pushing images. In most cases, you should use the <code>docker</code> CLI to pull, tag, and push images.</p> </note>

        Args:
            registry_id: <p>The Amazon Web Services account ID, or registry alias, associated with the public registry that contains the image layers to check. If you do not specify a registry, the default public registry is assumed.</p>
            repository_name: <p>The name of the repository that's associated with the image layers to check.</p>
            layer_digests: <p>The digests of the image layers to check.</p>

        Raises:
            capo_ecr_public.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter is invalid. Review the available parameters for the API request.</p>
            capo_ecr_public.errors.registry_not_found_exception.RegistryNotFoundException: <p>The registry doesn't exist.</p>
            capo_ecr_public.errors.repository_not_found_exception.RepositoryNotFoundException: <p>The specified repository can't be found. Check the spelling of the specified repository and ensure that you're performing operations on the correct registry.</p>
            capo_ecr_public.errors.server_exception.ServerException: <p>These errors are usually caused by a server-side issue.</p>
            capo_ecr_public.errors.unsupported_command_exception.UnsupportedCommandException: <p>The action isn't supported in this Region.</p>
            capo_ecr_public.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_ecr_public.types.batch_check_layer_availability_request.BatchCheckLayerAvailabilityRequest]",
        ) -> OperationResponse[
            "capo_ecr_public.types.batch_check_layer_availability_response.BatchCheckLayerAvailabilityResponse"
        ]:
            import capo_ecr_public._operations.spencer_frontend_service.batch_check_layer_availability

            output, http_response = (
                capo_ecr_public._operations.spencer_frontend_service.batch_check_layer_availability.batch_check_layer_availability(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ecr_public.types.batch_check_layer_availability_request.BatchCheckLayerAvailabilityRequest = {
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
        repository_name: "capo_ecr_public.types.repository_name.RepositoryName",
        image_ids: "capo_ecr_public.types.image_identifier_list.ImageIdentifierList",
        *,
        config_overrides: Optional[ECRPUBLICClientConfig] = None,
        registry_id: Optional[
            "capo_ecr_public.types.registry_id_or_alias.RegistryIdOrAlias"
        ] = None,
    ) -> "capo_ecr_public.types.batch_delete_image_response.BatchDeleteImageResponse":
        """<p>Deletes a list of specified images that are within a repository in a public registry. Images are specified with either an <code>imageTag</code> or <code>imageDigest</code>.</p> <p>You can remove a tag from an image by specifying the image's tag in your request. When you remove the last tag from an image, the image is deleted from your repository.</p> <p>You can completely delete an image (and all of its tags) by specifying the digest of the image in your request.</p>

        Args:
            registry_id: <p>The Amazon Web Services account ID, or registry alias, that's associated with the registry that contains the image to delete. If you do not specify a registry, the default public registry is assumed.</p>
            repository_name: <p>The repository in a public registry that contains the image to delete.</p>
            image_ids: <p>A list of image ID references that correspond to images to delete. The format of the <code>imageIds</code> reference is <code>imageTag=tag</code> or <code>imageDigest=digest</code>.</p>

        Raises:
            capo_ecr_public.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter is invalid. Review the available parameters for the API request.</p>
            capo_ecr_public.errors.repository_not_found_exception.RepositoryNotFoundException: <p>The specified repository can't be found. Check the spelling of the specified repository and ensure that you're performing operations on the correct registry.</p>
            capo_ecr_public.errors.server_exception.ServerException: <p>These errors are usually caused by a server-side issue.</p>
            capo_ecr_public.errors.unsupported_command_exception.UnsupportedCommandException: <p>The action isn't supported in this Region.</p>
            capo_ecr_public.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_ecr_public.types.batch_delete_image_request.BatchDeleteImageRequest]",
        ) -> OperationResponse[
            "capo_ecr_public.types.batch_delete_image_response.BatchDeleteImageResponse"
        ]:
            import capo_ecr_public._operations.spencer_frontend_service.batch_delete_image

            output, http_response = (
                capo_ecr_public._operations.spencer_frontend_service.batch_delete_image.batch_delete_image(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ecr_public.types.batch_delete_image_request.BatchDeleteImageRequest = {
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

    def complete_layer_upload(
        self,
        repository_name: "capo_ecr_public.types.repository_name.RepositoryName",
        upload_id: "capo_ecr_public.types.upload_id.UploadId",
        layer_digests: "capo_ecr_public.types.layer_digest_list.LayerDigestList",
        *,
        config_overrides: Optional[ECRPUBLICClientConfig] = None,
        registry_id: Optional[
            "capo_ecr_public.types.registry_id_or_alias.RegistryIdOrAlias"
        ] = None,
    ) -> "capo_ecr_public.types.complete_layer_upload_response.CompleteLayerUploadResponse":
        """<p>Informs Amazon ECR that the image layer upload is complete for a specified public registry, repository name, and upload ID. You can optionally provide a <code>sha256</code> digest of the image layer for data validation purposes.</p> <p>When an image is pushed, the CompleteLayerUpload API is called once for each new image layer to verify that the upload is complete.</p> <note> <p>This operation is used by the Amazon ECR proxy and is not generally used by customers for pulling and pushing images. In most cases, you should use the <code>docker</code> CLI to pull, tag, and push images.</p> </note>

        Args:
            registry_id: <p>The Amazon Web Services account ID, or registry alias, associated with the registry where layers are uploaded. If you do not specify a registry, the default public registry is assumed.</p>
            repository_name: <p>The name of the repository in a public registry to associate with the image layer.</p>
            upload_id: <p>The upload ID from a previous <a>InitiateLayerUpload</a> operation to associate with the image layer.</p>
            layer_digests: <p>The <code>sha256</code> digest of the image layer.</p>

        Raises:
            capo_ecr_public.errors.empty_upload_exception.EmptyUploadException: <p>The specified layer upload doesn't contain any layer parts.</p>
            capo_ecr_public.errors.invalid_layer_exception.InvalidLayerException: <p>The layer digest calculation performed by Amazon ECR when the image layer doesn't match the digest specified.</p>
            capo_ecr_public.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter is invalid. Review the available parameters for the API request.</p>
            capo_ecr_public.errors.layer_already_exists_exception.LayerAlreadyExistsException: <p>The image layer already exists in the associated repository.</p>
            capo_ecr_public.errors.layer_part_too_small_exception.LayerPartTooSmallException: <p>Layer parts must be at least 5 MiB in size.</p>
            capo_ecr_public.errors.registry_not_found_exception.RegistryNotFoundException: <p>The registry doesn't exist.</p>
            capo_ecr_public.errors.repository_not_found_exception.RepositoryNotFoundException: <p>The specified repository can't be found. Check the spelling of the specified repository and ensure that you're performing operations on the correct registry.</p>
            capo_ecr_public.errors.server_exception.ServerException: <p>These errors are usually caused by a server-side issue.</p>
            capo_ecr_public.errors.unsupported_command_exception.UnsupportedCommandException: <p>The action isn't supported in this Region.</p>
            capo_ecr_public.errors.upload_not_found_exception.UploadNotFoundException: <p>The upload can't be found, or the specified upload ID isn't valid for this repository.</p>
            capo_ecr_public.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_ecr_public.types.complete_layer_upload_request.CompleteLayerUploadRequest]",
        ) -> OperationResponse[
            "capo_ecr_public.types.complete_layer_upload_response.CompleteLayerUploadResponse"
        ]:
            import capo_ecr_public._operations.spencer_frontend_service.complete_layer_upload

            output, http_response = (
                capo_ecr_public._operations.spencer_frontend_service.complete_layer_upload.complete_layer_upload(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ecr_public.types.complete_layer_upload_request.CompleteLayerUploadRequest = {
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

    def create_repository(
        self,
        repository_name: "capo_ecr_public.types.repository_name.RepositoryName",
        *,
        config_overrides: Optional[ECRPUBLICClientConfig] = None,
        catalog_data: Optional[
            "capo_ecr_public.types.repository_catalog_data_input.RepositoryCatalogDataInput"
        ] = None,
        tags: Optional["capo_ecr_public.types.tag_list.TagList"] = None,
    ) -> "capo_ecr_public.types.create_repository_response.CreateRepositoryResponse":
        """<p>Creates a repository in a public registry. For more information, see <a href="https://docs.aws.amazon.com/AmazonECR/latest/userguide/Repositories.html">Amazon ECR repositories</a> in the <i>Amazon Elastic Container Registry User Guide</i>.</p>

        Args:
            repository_name: <p>The name to use for the repository. This appears publicly in the Amazon ECR Public Gallery. The repository name can be specified on its own (for example <code>nginx-web-app</code>) or prepended with a namespace to group the repository into a category (for example <code>project-a/nginx-web-app</code>).</p>
            catalog_data: <p>The details about the repository that are publicly visible in the Amazon ECR Public Gallery.</p>
            tags: <p>The metadata that you apply to each repository to help categorize and organize your repositories. Each tag consists of a key and an optional value. You define both of them. Tag keys can have a maximum character length of 128 characters, and tag values can have a maximum length of 256 characters.</p>

        Raises:
            capo_ecr_public.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter is invalid. Review the available parameters for the API request.</p>
            capo_ecr_public.errors.invalid_tag_parameter_exception.InvalidTagParameterException: <p>An invalid parameter has been specified. Tag keys can have a maximum character length of 128 characters, and tag values can have a maximum length of 256 characters.</p>
            capo_ecr_public.errors.limit_exceeded_exception.LimitExceededException: <p>The operation didn't succeed because it would have exceeded a service limit for your account. For more information, see <a href="https://docs.aws.amazon.com/AmazonECR/latest/userguide/service-quotas.html">Amazon ECR Service Quotas</a> in the Amazon Elastic Container Registry User Guide.</p>
            capo_ecr_public.errors.repository_already_exists_exception.RepositoryAlreadyExistsException: <p>The specified repository already exists in the specified registry.</p>
            capo_ecr_public.errors.server_exception.ServerException: <p>These errors are usually caused by a server-side issue.</p>
            capo_ecr_public.errors.too_many_tags_exception.TooManyTagsException: <p>The list of tags on the repository is over the limit. The maximum number of tags that can be applied to a repository is 50.</p>
            capo_ecr_public.errors.unsupported_command_exception.UnsupportedCommandException: <p>The action isn't supported in this Region.</p>
            capo_ecr_public.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_ecr_public.types.create_repository_request.CreateRepositoryRequest]",
        ) -> OperationResponse[
            "capo_ecr_public.types.create_repository_response.CreateRepositoryResponse"
        ]:
            import capo_ecr_public._operations.spencer_frontend_service.create_repository

            output, http_response = (
                capo_ecr_public._operations.spencer_frontend_service.create_repository.create_repository(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ecr_public.types.create_repository_request.CreateRepositoryRequest = {
            "repository_name": repository_name
        }
        if catalog_data is not None:
            input_["catalog_data"] = catalog_data
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_repository(
        self,
        repository_name: "capo_ecr_public.types.repository_name.RepositoryName",
        *,
        config_overrides: Optional[ECRPUBLICClientConfig] = None,
        registry_id: Optional["capo_ecr_public.types.registry_id.RegistryId"] = None,
        force: Optional["capo_ecr_public.types.force_flag.ForceFlag"] = None,
    ) -> "capo_ecr_public.types.delete_repository_response.DeleteRepositoryResponse":
        """<p>Deletes a repository in a public registry. If the repository contains images, you must either manually delete all images in the repository or use the <code>force</code> option. This option deletes all images on your behalf before deleting the repository.</p>

        Args:
            registry_id: <p>The Amazon Web Services account ID that's associated with the public registry that contains the repository to delete. If you do not specify a registry, the default public registry is assumed.</p>
            repository_name: <p>The name of the repository to delete.</p>
            force: <p> The force option can be used to delete a repository that contains images. If the force option is not used, the repository must be empty prior to deletion.</p>

        Raises:
            capo_ecr_public.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter is invalid. Review the available parameters for the API request.</p>
            capo_ecr_public.errors.repository_not_empty_exception.RepositoryNotEmptyException: <p>The specified repository contains images. To delete a repository that contains images, you must force the deletion with the <code>force</code> parameter.</p>
            capo_ecr_public.errors.repository_not_found_exception.RepositoryNotFoundException: <p>The specified repository can't be found. Check the spelling of the specified repository and ensure that you're performing operations on the correct registry.</p>
            capo_ecr_public.errors.server_exception.ServerException: <p>These errors are usually caused by a server-side issue.</p>
            capo_ecr_public.errors.unsupported_command_exception.UnsupportedCommandException: <p>The action isn't supported in this Region.</p>
            capo_ecr_public.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_ecr_public.types.delete_repository_request.DeleteRepositoryRequest]",
        ) -> OperationResponse[
            "capo_ecr_public.types.delete_repository_response.DeleteRepositoryResponse"
        ]:
            import capo_ecr_public._operations.spencer_frontend_service.delete_repository

            output, http_response = (
                capo_ecr_public._operations.spencer_frontend_service.delete_repository.delete_repository(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ecr_public.types.delete_repository_request.DeleteRepositoryRequest = {
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

    def delete_repository_policy(
        self,
        repository_name: "capo_ecr_public.types.repository_name.RepositoryName",
        *,
        config_overrides: Optional[ECRPUBLICClientConfig] = None,
        registry_id: Optional["capo_ecr_public.types.registry_id.RegistryId"] = None,
    ) -> "capo_ecr_public.types.delete_repository_policy_response.DeleteRepositoryPolicyResponse":
        """<p>Deletes the repository policy that's associated with the specified repository.</p>

        Args:
            registry_id: <p>The Amazon Web Services account ID that's associated with the public registry that contains the repository policy to delete. If you do not specify a registry, the default public registry is assumed.</p>
            repository_name: <p>The name of the repository that's associated with the repository policy to delete.</p>

        Raises:
            capo_ecr_public.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter is invalid. Review the available parameters for the API request.</p>
            capo_ecr_public.errors.repository_not_found_exception.RepositoryNotFoundException: <p>The specified repository can't be found. Check the spelling of the specified repository and ensure that you're performing operations on the correct registry.</p>
            capo_ecr_public.errors.repository_policy_not_found_exception.RepositoryPolicyNotFoundException: <p>The specified repository and registry combination doesn't have an associated repository policy.</p>
            capo_ecr_public.errors.server_exception.ServerException: <p>These errors are usually caused by a server-side issue.</p>
            capo_ecr_public.errors.unsupported_command_exception.UnsupportedCommandException: <p>The action isn't supported in this Region.</p>
            capo_ecr_public.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_ecr_public.types.delete_repository_policy_request.DeleteRepositoryPolicyRequest]",
        ) -> OperationResponse[
            "capo_ecr_public.types.delete_repository_policy_response.DeleteRepositoryPolicyResponse"
        ]:
            import capo_ecr_public._operations.spencer_frontend_service.delete_repository_policy

            output, http_response = (
                capo_ecr_public._operations.spencer_frontend_service.delete_repository_policy.delete_repository_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ecr_public.types.delete_repository_policy_request.DeleteRepositoryPolicyRequest = {
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

    def describe_images(
        self,
        repository_name: "capo_ecr_public.types.repository_name.RepositoryName",
        *,
        config_overrides: Optional[ECRPUBLICClientConfig] = None,
        registry_id: Optional["capo_ecr_public.types.registry_id.RegistryId"] = None,
        image_ids: Optional[
            "capo_ecr_public.types.image_identifier_list.ImageIdentifierList"
        ] = None,
        next_token: Optional["capo_ecr_public.types.next_token.NextToken"] = None,
        max_results: Optional["capo_ecr_public.types.max_results.MaxResults"] = None,
    ) -> "capo_ecr_public.types.describe_images_response.DescribeImagesResponse":
        """<p>Returns metadata that's related to the images in a repository in a public registry.</p> <note> <p>Beginning with Docker version 1.9, the Docker client compresses image layers before pushing them to a V2 Docker registry. The output of the <code>docker images</code> command shows the uncompressed image size. Therefore, it might return a larger image size than the image sizes that are returned by <a>DescribeImages</a>.</p> </note>

        Args:
            registry_id: <p>The Amazon Web Services account ID that's associated with the public registry that contains the repository where images are described. If you do not specify a registry, the default public registry is assumed.</p>
            repository_name: <p>The repository that contains the images to describe.</p>
            image_ids: <p>The list of image IDs for the requested repository.</p>
            next_token: <p>The <code>nextToken</code> value that's returned from a previous paginated <code>DescribeImages</code> request where <code>maxResults</code> was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the <code>nextToken</code> value. If there are no more results to return, this value is <code>null</code>. If you specify images with <code>imageIds</code>, you can't use this option.</p>
            max_results: <p>The maximum number of repository results that's returned by <code>DescribeImages</code> in paginated output. When this parameter is used, <code>DescribeImages</code> only returns <code>maxResults</code> results in a single page along with a <code>nextToken</code> response element. You can see the remaining results of the initial request by sending another <code>DescribeImages</code> request with the returned <code>nextToken</code> value. This value can be between 1 and 1000. If this parameter isn't used, then <code>DescribeImages</code> returns up to 100 results and a <code>nextToken</code> value, if applicable. If you specify images with <code>imageIds</code>, you can't use this option.</p>

        Raises:
            capo_ecr_public.errors.image_not_found_exception.ImageNotFoundException: <p>The image requested doesn't exist in the specified repository.</p>
            capo_ecr_public.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter is invalid. Review the available parameters for the API request.</p>
            capo_ecr_public.errors.repository_not_found_exception.RepositoryNotFoundException: <p>The specified repository can't be found. Check the spelling of the specified repository and ensure that you're performing operations on the correct registry.</p>
            capo_ecr_public.errors.server_exception.ServerException: <p>These errors are usually caused by a server-side issue.</p>
            capo_ecr_public.errors.unsupported_command_exception.UnsupportedCommandException: <p>The action isn't supported in this Region.</p>
            capo_ecr_public.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_ecr_public.types.describe_images_request.DescribeImagesRequest]",
        ) -> OperationResponse[
            "capo_ecr_public.types.describe_images_response.DescribeImagesResponse"
        ]:
            import capo_ecr_public._operations.spencer_frontend_service.describe_images

            output, http_response = (
                capo_ecr_public._operations.spencer_frontend_service.describe_images.describe_images(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ecr_public.types.describe_images_request.DescribeImagesRequest = {
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

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_describe_images(
        self,
        repository_name: "capo_ecr_public.types.repository_name.RepositoryName",
        *,
        config_overrides: Optional[ECRPUBLICClientConfig] = None,
        registry_id: Optional["capo_ecr_public.types.registry_id.RegistryId"] = None,
        image_ids: Optional[
            "capo_ecr_public.types.image_identifier_list.ImageIdentifierList"
        ] = None,
        next_token: Optional["capo_ecr_public.types.next_token.NextToken"] = None,
        max_results: Optional["capo_ecr_public.types.max_results.MaxResults"] = None,
    ) -> "Iterator[capo_ecr_public.types.image_detail.ImageDetail]":
        _token = next_token
        while True:
            _response = self.describe_images(
                repository_name,
                config_overrides=config_overrides,
                registry_id=registry_id,
                image_ids=image_ids,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("image_details",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def describe_image_tags(
        self,
        repository_name: "capo_ecr_public.types.repository_name.RepositoryName",
        *,
        config_overrides: Optional[ECRPUBLICClientConfig] = None,
        registry_id: Optional["capo_ecr_public.types.registry_id.RegistryId"] = None,
        next_token: Optional["capo_ecr_public.types.next_token.NextToken"] = None,
        max_results: Optional["capo_ecr_public.types.max_results.MaxResults"] = None,
    ) -> "capo_ecr_public.types.describe_image_tags_response.DescribeImageTagsResponse":
        """<p>Returns the image tag details for a repository in a public registry.</p>

        Args:
            registry_id: <p>The Amazon Web Services account ID that's associated with the public registry that contains the repository where images are described. If you do not specify a registry, the default public registry is assumed.</p>
            repository_name: <p>The name of the repository that contains the image tag details to describe.</p>
            next_token: <p>The <code>nextToken</code> value that's returned from a previous paginated <code>DescribeImageTags</code> request where <code>maxResults</code> was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the <code>nextToken</code> value. If there are no more results to return, this value is <code>null</code>. If you specify images with <code>imageIds</code>, you can't use this option.</p>
            max_results: <p>The maximum number of repository results that's returned by <code>DescribeImageTags</code> in paginated output. When this parameter is used, <code>DescribeImageTags</code> only returns <code>maxResults</code> results in a single page along with a <code>nextToken</code> response element. You can see the remaining results of the initial request by sending another <code>DescribeImageTags</code> request with the returned <code>nextToken</code> value. This value can be between 1 and 1000. If this parameter isn't used, then <code>DescribeImageTags</code> returns up to 100 results and a <code>nextToken</code> value, if applicable. If you specify images with <code>imageIds</code>, you can't use this option.</p>

        Raises:
            capo_ecr_public.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter is invalid. Review the available parameters for the API request.</p>
            capo_ecr_public.errors.repository_not_found_exception.RepositoryNotFoundException: <p>The specified repository can't be found. Check the spelling of the specified repository and ensure that you're performing operations on the correct registry.</p>
            capo_ecr_public.errors.server_exception.ServerException: <p>These errors are usually caused by a server-side issue.</p>
            capo_ecr_public.errors.unsupported_command_exception.UnsupportedCommandException: <p>The action isn't supported in this Region.</p>
            capo_ecr_public.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_ecr_public.types.describe_image_tags_request.DescribeImageTagsRequest]",
        ) -> OperationResponse[
            "capo_ecr_public.types.describe_image_tags_response.DescribeImageTagsResponse"
        ]:
            import capo_ecr_public._operations.spencer_frontend_service.describe_image_tags

            output, http_response = (
                capo_ecr_public._operations.spencer_frontend_service.describe_image_tags.describe_image_tags(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ecr_public.types.describe_image_tags_request.DescribeImageTagsRequest = {
            "repository_name": repository_name
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

    def iter_describe_image_tags(
        self,
        repository_name: "capo_ecr_public.types.repository_name.RepositoryName",
        *,
        config_overrides: Optional[ECRPUBLICClientConfig] = None,
        registry_id: Optional["capo_ecr_public.types.registry_id.RegistryId"] = None,
        next_token: Optional["capo_ecr_public.types.next_token.NextToken"] = None,
        max_results: Optional["capo_ecr_public.types.max_results.MaxResults"] = None,
    ) -> "Iterator[capo_ecr_public.types.image_tag_detail.ImageTagDetail]":
        _token = next_token
        while True:
            _response = self.describe_image_tags(
                repository_name,
                config_overrides=config_overrides,
                registry_id=registry_id,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("image_tag_details",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def describe_registries(
        self,
        *,
        config_overrides: Optional[ECRPUBLICClientConfig] = None,
        next_token: Optional["capo_ecr_public.types.next_token.NextToken"] = None,
        max_results: Optional["capo_ecr_public.types.max_results.MaxResults"] = None,
    ) -> (
        "capo_ecr_public.types.describe_registries_response.DescribeRegistriesResponse"
    ):
        """<p>Returns details for a public registry.</p>

        Args:
            next_token: <p>The <code>nextToken</code> value that's returned from a previous paginated <code>DescribeRegistries</code> request where <code>maxResults</code> was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the <code>nextToken</code> value. If there are no more results to return, this value is <code>null</code>.</p> <note> <p>This token should be treated as an opaque identifier that is only used to retrieve the next items in a list and not for other programmatic purposes.</p> </note>
            max_results: <p>The maximum number of repository results that's returned by <code>DescribeRegistries</code> in paginated output. When this parameter is used, <code>DescribeRegistries</code> only returns <code>maxResults</code> results in a single page along with a <code>nextToken</code> response element. The remaining results of the initial request can be seen by sending another <code>DescribeRegistries</code> request with the returned <code>nextToken</code> value. This value can be between 1 and 1000. If this parameter isn't used, then <code>DescribeRegistries</code> returns up to 100 results and a <code>nextToken</code> value, if applicable.</p>

        Raises:
            capo_ecr_public.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter is invalid. Review the available parameters for the API request.</p>
            capo_ecr_public.errors.server_exception.ServerException: <p>These errors are usually caused by a server-side issue.</p>
            capo_ecr_public.errors.unsupported_command_exception.UnsupportedCommandException: <p>The action isn't supported in this Region.</p>
            capo_ecr_public.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_ecr_public.types.describe_registries_request.DescribeRegistriesRequest]",
        ) -> OperationResponse[
            "capo_ecr_public.types.describe_registries_response.DescribeRegistriesResponse"
        ]:
            import capo_ecr_public._operations.spencer_frontend_service.describe_registries

            output, http_response = (
                capo_ecr_public._operations.spencer_frontend_service.describe_registries.describe_registries(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ecr_public.types.describe_registries_request.DescribeRegistriesRequest = {}
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

    def iter_describe_registries(
        self,
        *,
        config_overrides: Optional[ECRPUBLICClientConfig] = None,
        next_token: Optional["capo_ecr_public.types.next_token.NextToken"] = None,
        max_results: Optional["capo_ecr_public.types.max_results.MaxResults"] = None,
    ) -> "Iterator[capo_ecr_public.types.registry.Registry]":
        _token = next_token
        while True:
            _response = self.describe_registries(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("registries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def describe_repositories(
        self,
        *,
        config_overrides: Optional[ECRPUBLICClientConfig] = None,
        registry_id: Optional["capo_ecr_public.types.registry_id.RegistryId"] = None,
        repository_names: Optional[
            "capo_ecr_public.types.repository_name_list.RepositoryNameList"
        ] = None,
        next_token: Optional["capo_ecr_public.types.next_token.NextToken"] = None,
        max_results: Optional["capo_ecr_public.types.max_results.MaxResults"] = None,
    ) -> "capo_ecr_public.types.describe_repositories_response.DescribeRepositoriesResponse":
        """<p>Describes repositories that are in a public registry.</p>

        Args:
            registry_id: <p>The Amazon Web Services account ID that's associated with the registry that contains the repositories to be described. If you do not specify a registry, the default public registry is assumed.</p>
            repository_names: <p>A list of repositories to describe. If this parameter is omitted, then all repositories in a registry are described.</p>
            next_token: <p>The <code>nextToken</code> value that's returned from a previous paginated <code>DescribeRepositories</code> request where <code>maxResults</code> was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the <code>nextToken</code> value. If there are no more results to return, this value is <code>null</code>. If you specify repositories with <code>repositoryNames</code>, you can't use this option.</p> <note> <p>This token should be treated as an opaque identifier that is only used to retrieve the next items in a list and not for other programmatic purposes.</p> </note>
            max_results: <p>The maximum number of repository results that's returned by <code>DescribeRepositories</code> in paginated output. When this parameter is used, <code>DescribeRepositories</code> only returns <code>maxResults</code> results in a single page along with a <code>nextToken</code> response element. You can see the remaining results of the initial request by sending another <code>DescribeRepositories</code> request with the returned <code>nextToken</code> value. This value can be between 1 and 1000. If this parameter isn't used, then <code>DescribeRepositories</code> returns up to 100 results and a <code>nextToken</code> value, if applicable. If you specify repositories with <code>repositoryNames</code>, you can't use this option.</p>

        Raises:
            capo_ecr_public.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter is invalid. Review the available parameters for the API request.</p>
            capo_ecr_public.errors.repository_not_found_exception.RepositoryNotFoundException: <p>The specified repository can't be found. Check the spelling of the specified repository and ensure that you're performing operations on the correct registry.</p>
            capo_ecr_public.errors.server_exception.ServerException: <p>These errors are usually caused by a server-side issue.</p>
            capo_ecr_public.errors.unsupported_command_exception.UnsupportedCommandException: <p>The action isn't supported in this Region.</p>
            capo_ecr_public.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_ecr_public.types.describe_repositories_request.DescribeRepositoriesRequest]",
        ) -> OperationResponse[
            "capo_ecr_public.types.describe_repositories_response.DescribeRepositoriesResponse"
        ]:
            import capo_ecr_public._operations.spencer_frontend_service.describe_repositories

            output, http_response = (
                capo_ecr_public._operations.spencer_frontend_service.describe_repositories.describe_repositories(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ecr_public.types.describe_repositories_request.DescribeRepositoriesRequest = {}
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
        config_overrides: Optional[ECRPUBLICClientConfig] = None,
        registry_id: Optional["capo_ecr_public.types.registry_id.RegistryId"] = None,
        repository_names: Optional[
            "capo_ecr_public.types.repository_name_list.RepositoryNameList"
        ] = None,
        next_token: Optional["capo_ecr_public.types.next_token.NextToken"] = None,
        max_results: Optional["capo_ecr_public.types.max_results.MaxResults"] = None,
    ) -> "Iterator[capo_ecr_public.types.repository.Repository]":
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

    def get_authorization_token(
        self, *, config_overrides: Optional[ECRPUBLICClientConfig] = None
    ) -> "capo_ecr_public.types.get_authorization_token_response.GetAuthorizationTokenResponse":
        """<p>Retrieves an authorization token. An authorization token represents your IAM authentication credentials. You can use it to access any Amazon ECR registry that your IAM principal has access to. The authorization token is valid for 12 hours. This API requires the <code>ecr-public:GetAuthorizationToken</code> and <code>sts:GetServiceBearerToken</code> permissions.</p>

        Raises:
            capo_ecr_public.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter is invalid. Review the available parameters for the API request.</p>
            capo_ecr_public.errors.server_exception.ServerException: <p>These errors are usually caused by a server-side issue.</p>
            capo_ecr_public.errors.unsupported_command_exception.UnsupportedCommandException: <p>The action isn't supported in this Region.</p>
            capo_ecr_public.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_ecr_public.types.get_authorization_token_request.GetAuthorizationTokenRequest]",
        ) -> OperationResponse[
            "capo_ecr_public.types.get_authorization_token_response.GetAuthorizationTokenResponse"
        ]:
            import capo_ecr_public._operations.spencer_frontend_service.get_authorization_token

            output, http_response = (
                capo_ecr_public._operations.spencer_frontend_service.get_authorization_token.get_authorization_token(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ecr_public.types.get_authorization_token_request.GetAuthorizationTokenRequest = {}

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_registry_catalog_data(
        self, *, config_overrides: Optional[ECRPUBLICClientConfig] = None
    ) -> "capo_ecr_public.types.get_registry_catalog_data_response.GetRegistryCatalogDataResponse":
        """<p>Retrieves catalog metadata for a public registry.</p>

        Raises:
            capo_ecr_public.errors.server_exception.ServerException: <p>These errors are usually caused by a server-side issue.</p>
            capo_ecr_public.errors.unsupported_command_exception.UnsupportedCommandException: <p>The action isn't supported in this Region.</p>
            capo_ecr_public.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_ecr_public.types.get_registry_catalog_data_request.GetRegistryCatalogDataRequest]",
        ) -> OperationResponse[
            "capo_ecr_public.types.get_registry_catalog_data_response.GetRegistryCatalogDataResponse"
        ]:
            import capo_ecr_public._operations.spencer_frontend_service.get_registry_catalog_data

            output, http_response = (
                capo_ecr_public._operations.spencer_frontend_service.get_registry_catalog_data.get_registry_catalog_data(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ecr_public.types.get_registry_catalog_data_request.GetRegistryCatalogDataRequest = {}

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_repository_catalog_data(
        self,
        repository_name: "capo_ecr_public.types.repository_name.RepositoryName",
        *,
        config_overrides: Optional[ECRPUBLICClientConfig] = None,
        registry_id: Optional["capo_ecr_public.types.registry_id.RegistryId"] = None,
    ) -> "capo_ecr_public.types.get_repository_catalog_data_response.GetRepositoryCatalogDataResponse":
        """<p>Retrieve catalog metadata for a repository in a public registry. This metadata is displayed publicly in the Amazon ECR Public Gallery.</p>

        Args:
            registry_id: <p>The Amazon Web Services account ID that's associated with the registry that contains the repositories to be described. If you do not specify a registry, the default public registry is assumed.</p>
            repository_name: <p>The name of the repository to retrieve the catalog metadata for.</p>

        Raises:
            capo_ecr_public.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter is invalid. Review the available parameters for the API request.</p>
            capo_ecr_public.errors.repository_catalog_data_not_found_exception.RepositoryCatalogDataNotFoundException: <p>The repository catalog data doesn't exist.</p>
            capo_ecr_public.errors.repository_not_found_exception.RepositoryNotFoundException: <p>The specified repository can't be found. Check the spelling of the specified repository and ensure that you're performing operations on the correct registry.</p>
            capo_ecr_public.errors.server_exception.ServerException: <p>These errors are usually caused by a server-side issue.</p>
            capo_ecr_public.errors.unsupported_command_exception.UnsupportedCommandException: <p>The action isn't supported in this Region.</p>
            capo_ecr_public.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_ecr_public.types.get_repository_catalog_data_request.GetRepositoryCatalogDataRequest]",
        ) -> OperationResponse[
            "capo_ecr_public.types.get_repository_catalog_data_response.GetRepositoryCatalogDataResponse"
        ]:
            import capo_ecr_public._operations.spencer_frontend_service.get_repository_catalog_data

            output, http_response = (
                capo_ecr_public._operations.spencer_frontend_service.get_repository_catalog_data.get_repository_catalog_data(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ecr_public.types.get_repository_catalog_data_request.GetRepositoryCatalogDataRequest = {
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

    def get_repository_policy(
        self,
        repository_name: "capo_ecr_public.types.repository_name.RepositoryName",
        *,
        config_overrides: Optional[ECRPUBLICClientConfig] = None,
        registry_id: Optional["capo_ecr_public.types.registry_id.RegistryId"] = None,
    ) -> "capo_ecr_public.types.get_repository_policy_response.GetRepositoryPolicyResponse":
        """<p>Retrieves the repository policy for the specified repository.</p>

        Args:
            registry_id: <p>The Amazon Web Services account ID that's associated with the public registry that contains the repository. If you do not specify a registry, the default public registry is assumed.</p>
            repository_name: <p>The name of the repository with the policy to retrieve.</p>

        Raises:
            capo_ecr_public.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter is invalid. Review the available parameters for the API request.</p>
            capo_ecr_public.errors.repository_not_found_exception.RepositoryNotFoundException: <p>The specified repository can't be found. Check the spelling of the specified repository and ensure that you're performing operations on the correct registry.</p>
            capo_ecr_public.errors.repository_policy_not_found_exception.RepositoryPolicyNotFoundException: <p>The specified repository and registry combination doesn't have an associated repository policy.</p>
            capo_ecr_public.errors.server_exception.ServerException: <p>These errors are usually caused by a server-side issue.</p>
            capo_ecr_public.errors.unsupported_command_exception.UnsupportedCommandException: <p>The action isn't supported in this Region.</p>
            capo_ecr_public.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_ecr_public.types.get_repository_policy_request.GetRepositoryPolicyRequest]",
        ) -> OperationResponse[
            "capo_ecr_public.types.get_repository_policy_response.GetRepositoryPolicyResponse"
        ]:
            import capo_ecr_public._operations.spencer_frontend_service.get_repository_policy

            output, http_response = (
                capo_ecr_public._operations.spencer_frontend_service.get_repository_policy.get_repository_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ecr_public.types.get_repository_policy_request.GetRepositoryPolicyRequest = {
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

    def initiate_layer_upload(
        self,
        repository_name: "capo_ecr_public.types.repository_name.RepositoryName",
        *,
        config_overrides: Optional[ECRPUBLICClientConfig] = None,
        registry_id: Optional[
            "capo_ecr_public.types.registry_id_or_alias.RegistryIdOrAlias"
        ] = None,
    ) -> "capo_ecr_public.types.initiate_layer_upload_response.InitiateLayerUploadResponse":
        """<p>Notifies Amazon ECR that you intend to upload an image layer.</p> <p>When an image is pushed, the InitiateLayerUpload API is called once for each image layer that hasn't already been uploaded. Whether an image layer uploads is determined by the BatchCheckLayerAvailability API action.</p> <note> <p>This operation is used by the Amazon ECR proxy and is not generally used by customers for pulling and pushing images. In most cases, you should use the <code>docker</code> CLI to pull, tag, and push images.</p> </note>

        Args:
            registry_id: <p>The Amazon Web Services account ID, or registry alias, that's associated with the registry to which you intend to upload layers. If you do not specify a registry, the default public registry is assumed.</p>
            repository_name: <p>The name of the repository that you want to upload layers to.</p>

        Raises:
            capo_ecr_public.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter is invalid. Review the available parameters for the API request.</p>
            capo_ecr_public.errors.registry_not_found_exception.RegistryNotFoundException: <p>The registry doesn't exist.</p>
            capo_ecr_public.errors.repository_not_found_exception.RepositoryNotFoundException: <p>The specified repository can't be found. Check the spelling of the specified repository and ensure that you're performing operations on the correct registry.</p>
            capo_ecr_public.errors.server_exception.ServerException: <p>These errors are usually caused by a server-side issue.</p>
            capo_ecr_public.errors.unsupported_command_exception.UnsupportedCommandException: <p>The action isn't supported in this Region.</p>
            capo_ecr_public.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_ecr_public.types.initiate_layer_upload_request.InitiateLayerUploadRequest]",
        ) -> OperationResponse[
            "capo_ecr_public.types.initiate_layer_upload_response.InitiateLayerUploadResponse"
        ]:
            import capo_ecr_public._operations.spencer_frontend_service.initiate_layer_upload

            output, http_response = (
                capo_ecr_public._operations.spencer_frontend_service.initiate_layer_upload.initiate_layer_upload(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ecr_public.types.initiate_layer_upload_request.InitiateLayerUploadRequest = {
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

    def list_tags_for_resource(
        self,
        resource_arn: "capo_ecr_public.types.arn.Arn",
        *,
        config_overrides: Optional[ECRPUBLICClientConfig] = None,
    ) -> "capo_ecr_public.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>List the tags for an Amazon ECR Public resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) that identifies the resource to list the tags for. Currently, the supported resource is an Amazon ECR Public repository.</p>

        Raises:
            capo_ecr_public.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter is invalid. Review the available parameters for the API request.</p>
            capo_ecr_public.errors.repository_not_found_exception.RepositoryNotFoundException: <p>The specified repository can't be found. Check the spelling of the specified repository and ensure that you're performing operations on the correct registry.</p>
            capo_ecr_public.errors.server_exception.ServerException: <p>These errors are usually caused by a server-side issue.</p>
            capo_ecr_public.errors.unsupported_command_exception.UnsupportedCommandException: <p>The action isn't supported in this Region.</p>
            capo_ecr_public.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_ecr_public.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> OperationResponse[
            "capo_ecr_public.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import capo_ecr_public._operations.spencer_frontend_service.list_tags_for_resource

            output, http_response = (
                capo_ecr_public._operations.spencer_frontend_service.list_tags_for_resource.list_tags_for_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ecr_public.types.list_tags_for_resource_request.ListTagsForResourceRequest = {
            "resource_arn": resource_arn
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
        repository_name: "capo_ecr_public.types.repository_name.RepositoryName",
        image_manifest: "capo_ecr_public.types.image_manifest.ImageManifest",
        *,
        config_overrides: Optional[ECRPUBLICClientConfig] = None,
        registry_id: Optional[
            "capo_ecr_public.types.registry_id_or_alias.RegistryIdOrAlias"
        ] = None,
        image_manifest_media_type: Optional[
            "capo_ecr_public.types.media_type.MediaType"
        ] = None,
        image_tag: Optional["capo_ecr_public.types.image_tag.ImageTag"] = None,
        image_digest: Optional["capo_ecr_public.types.image_digest.ImageDigest"] = None,
    ) -> "capo_ecr_public.types.put_image_response.PutImageResponse":
        """<p>Creates or updates the image manifest and tags that are associated with an image.</p> <p>When an image is pushed and all new image layers have been uploaded, the PutImage API is called once to create or update the image manifest and the tags that are associated with the image.</p> <note> <p>This operation is used by the Amazon ECR proxy and is not generally used by customers for pulling and pushing images. In most cases, you should use the <code>docker</code> CLI to pull, tag, and push images.</p> </note>

        Args:
            registry_id: <p>The Amazon Web Services account ID, or registry alias, that's associated with the public registry that contains the repository where the image is put. If you do not specify a registry, the default public registry is assumed.</p>
            repository_name: <p>The name of the repository where the image is put.</p>
            image_manifest: <p>The image manifest that corresponds to the image to be uploaded.</p>
            image_manifest_media_type: <p>The media type of the image manifest. If you push an image manifest that doesn't contain the <code>mediaType</code> field, you must specify the <code>imageManifestMediaType</code> in the request.</p>
            image_tag: <p>The tag to associate with the image. This parameter is required for images that use the Docker Image Manifest V2 Schema 2 or Open Container Initiative (OCI) formats.</p>
            image_digest: <p>The image digest of the image manifest that corresponds to the image.</p>

        Raises:
            capo_ecr_public.errors.image_already_exists_exception.ImageAlreadyExistsException: <p>The specified image has already been pushed, and there were no changes to the manifest or image tag after the last push.</p>
            capo_ecr_public.errors.image_digest_does_not_match_exception.ImageDigestDoesNotMatchException: <p>The specified image digest doesn't match the digest that Amazon ECR calculated for the image.</p>
            capo_ecr_public.errors.image_tag_already_exists_exception.ImageTagAlreadyExistsException: <p>The specified image is tagged with a tag that already exists. The repository is configured for tag immutability.</p>
            capo_ecr_public.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter is invalid. Review the available parameters for the API request.</p>
            capo_ecr_public.errors.layers_not_found_exception.LayersNotFoundException: <p>The specified layers can't be found, or the specified layer isn't valid for this repository.</p>
            capo_ecr_public.errors.limit_exceeded_exception.LimitExceededException: <p>The operation didn't succeed because it would have exceeded a service limit for your account. For more information, see <a href="https://docs.aws.amazon.com/AmazonECR/latest/userguide/service-quotas.html">Amazon ECR Service Quotas</a> in the Amazon Elastic Container Registry User Guide.</p>
            capo_ecr_public.errors.referenced_images_not_found_exception.ReferencedImagesNotFoundException: <p>The manifest list is referencing an image that doesn't exist.</p>
            capo_ecr_public.errors.registry_not_found_exception.RegistryNotFoundException: <p>The registry doesn't exist.</p>
            capo_ecr_public.errors.repository_not_found_exception.RepositoryNotFoundException: <p>The specified repository can't be found. Check the spelling of the specified repository and ensure that you're performing operations on the correct registry.</p>
            capo_ecr_public.errors.server_exception.ServerException: <p>These errors are usually caused by a server-side issue.</p>
            capo_ecr_public.errors.unsupported_command_exception.UnsupportedCommandException: <p>The action isn't supported in this Region.</p>
            capo_ecr_public.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_ecr_public.types.put_image_request.PutImageRequest]",
        ) -> OperationResponse[
            "capo_ecr_public.types.put_image_response.PutImageResponse"
        ]:
            import capo_ecr_public._operations.spencer_frontend_service.put_image

            output, http_response = (
                capo_ecr_public._operations.spencer_frontend_service.put_image.put_image(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ecr_public.types.put_image_request.PutImageRequest = {
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

    def put_registry_catalog_data(
        self,
        *,
        config_overrides: Optional[ECRPUBLICClientConfig] = None,
        display_name: Optional[
            "capo_ecr_public.types.registry_display_name.RegistryDisplayName"
        ] = None,
    ) -> "capo_ecr_public.types.put_registry_catalog_data_response.PutRegistryCatalogDataResponse":
        """<p>Create or update the catalog data for a public registry.</p>

        Args:
            display_name: <p>The display name for a public registry. The display name is shown as the repository author in the Amazon ECR Public Gallery.</p> <note> <p>The registry display name is only publicly visible in the Amazon ECR Public Gallery for verified accounts.</p> </note>

        Raises:
            capo_ecr_public.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter is invalid. Review the available parameters for the API request.</p>
            capo_ecr_public.errors.server_exception.ServerException: <p>These errors are usually caused by a server-side issue.</p>
            capo_ecr_public.errors.unsupported_command_exception.UnsupportedCommandException: <p>The action isn't supported in this Region.</p>
            capo_ecr_public.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_ecr_public.types.put_registry_catalog_data_request.PutRegistryCatalogDataRequest]",
        ) -> OperationResponse[
            "capo_ecr_public.types.put_registry_catalog_data_response.PutRegistryCatalogDataResponse"
        ]:
            import capo_ecr_public._operations.spencer_frontend_service.put_registry_catalog_data

            output, http_response = (
                capo_ecr_public._operations.spencer_frontend_service.put_registry_catalog_data.put_registry_catalog_data(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ecr_public.types.put_registry_catalog_data_request.PutRegistryCatalogDataRequest = {}
        if display_name is not None:
            input_["display_name"] = display_name

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def put_repository_catalog_data(
        self,
        repository_name: "capo_ecr_public.types.repository_name.RepositoryName",
        catalog_data: "capo_ecr_public.types.repository_catalog_data_input.RepositoryCatalogDataInput",
        *,
        config_overrides: Optional[ECRPUBLICClientConfig] = None,
        registry_id: Optional["capo_ecr_public.types.registry_id.RegistryId"] = None,
    ) -> "capo_ecr_public.types.put_repository_catalog_data_response.PutRepositoryCatalogDataResponse":
        """<p>Creates or updates the catalog data for a repository in a public registry.</p>

        Args:
            registry_id: <p>The Amazon Web Services account ID that's associated with the public registry the repository is in. If you do not specify a registry, the default public registry is assumed.</p>
            repository_name: <p>The name of the repository to create or update the catalog data for.</p>
            catalog_data: <p>An object containing the catalog data for a repository. This data is publicly visible in the Amazon ECR Public Gallery.</p>

        Raises:
            capo_ecr_public.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter is invalid. Review the available parameters for the API request.</p>
            capo_ecr_public.errors.repository_not_found_exception.RepositoryNotFoundException: <p>The specified repository can't be found. Check the spelling of the specified repository and ensure that you're performing operations on the correct registry.</p>
            capo_ecr_public.errors.server_exception.ServerException: <p>These errors are usually caused by a server-side issue.</p>
            capo_ecr_public.errors.unsupported_command_exception.UnsupportedCommandException: <p>The action isn't supported in this Region.</p>
            capo_ecr_public.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_ecr_public.types.put_repository_catalog_data_request.PutRepositoryCatalogDataRequest]",
        ) -> OperationResponse[
            "capo_ecr_public.types.put_repository_catalog_data_response.PutRepositoryCatalogDataResponse"
        ]:
            import capo_ecr_public._operations.spencer_frontend_service.put_repository_catalog_data

            output, http_response = (
                capo_ecr_public._operations.spencer_frontend_service.put_repository_catalog_data.put_repository_catalog_data(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ecr_public.types.put_repository_catalog_data_request.PutRepositoryCatalogDataRequest = {
            "repository_name": repository_name,
            "catalog_data": catalog_data,
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

    def set_repository_policy(
        self,
        repository_name: "capo_ecr_public.types.repository_name.RepositoryName",
        policy_text: "capo_ecr_public.types.repository_policy_text.RepositoryPolicyText",
        *,
        config_overrides: Optional[ECRPUBLICClientConfig] = None,
        registry_id: Optional["capo_ecr_public.types.registry_id.RegistryId"] = None,
        force: Optional["capo_ecr_public.types.force_flag.ForceFlag"] = None,
    ) -> "capo_ecr_public.types.set_repository_policy_response.SetRepositoryPolicyResponse":
        """<p>Applies a repository policy to the specified public repository to control access permissions. For more information, see <a href="https://docs.aws.amazon.com/AmazonECR/latest/userguide/repository-policies.html">Amazon ECR Repository Policies</a> in the <i>Amazon Elastic Container Registry User Guide</i>.</p>

        Args:
            registry_id: <p>The Amazon Web Services account ID that's associated with the registry that contains the repository. If you do not specify a registry, the default public registry is assumed.</p>
            repository_name: <p>The name of the repository to receive the policy.</p>
            policy_text: <p>The JSON repository policy text to apply to the repository. For more information, see <a href="https://docs.aws.amazon.com/AmazonECR/latest/userguide/repository-policy-examples.html">Amazon ECR Repository Policies</a> in the <i>Amazon Elastic Container Registry User Guide</i>.</p>
            force: <p>If the policy that you want to set on a repository policy would prevent you from setting another policy in the future, you must force the <a>SetRepositoryPolicy</a> operation. This prevents accidental repository lockouts.</p>

        Raises:
            capo_ecr_public.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter is invalid. Review the available parameters for the API request.</p>
            capo_ecr_public.errors.repository_not_found_exception.RepositoryNotFoundException: <p>The specified repository can't be found. Check the spelling of the specified repository and ensure that you're performing operations on the correct registry.</p>
            capo_ecr_public.errors.server_exception.ServerException: <p>These errors are usually caused by a server-side issue.</p>
            capo_ecr_public.errors.unsupported_command_exception.UnsupportedCommandException: <p>The action isn't supported in this Region.</p>
            capo_ecr_public.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_ecr_public.types.set_repository_policy_request.SetRepositoryPolicyRequest]",
        ) -> OperationResponse[
            "capo_ecr_public.types.set_repository_policy_response.SetRepositoryPolicyResponse"
        ]:
            import capo_ecr_public._operations.spencer_frontend_service.set_repository_policy

            output, http_response = (
                capo_ecr_public._operations.spencer_frontend_service.set_repository_policy.set_repository_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ecr_public.types.set_repository_policy_request.SetRepositoryPolicyRequest = {
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

    def tag_resource(
        self,
        resource_arn: "capo_ecr_public.types.arn.Arn",
        tags: "capo_ecr_public.types.tag_list.TagList",
        *,
        config_overrides: Optional[ECRPUBLICClientConfig] = None,
    ) -> "capo_ecr_public.types.tag_resource_response.TagResourceResponse":
        """<p>Associates the specified tags to a resource with the specified <code>resourceArn</code>. If existing tags on a resource aren't specified in the request parameters, they aren't changed. When a resource is deleted, the tags associated with that resource are also deleted.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource to add tags to. Currently, the supported resource is an Amazon ECR Public repository.</p>
            tags: <p>The tags to add to the resource. A tag is an array of key-value pairs. Tag keys can have a maximum character length of 128 characters, and tag values can have a maximum length of 256 characters.</p>

        Raises:
            capo_ecr_public.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter is invalid. Review the available parameters for the API request.</p>
            capo_ecr_public.errors.invalid_tag_parameter_exception.InvalidTagParameterException: <p>An invalid parameter has been specified. Tag keys can have a maximum character length of 128 characters, and tag values can have a maximum length of 256 characters.</p>
            capo_ecr_public.errors.repository_not_found_exception.RepositoryNotFoundException: <p>The specified repository can't be found. Check the spelling of the specified repository and ensure that you're performing operations on the correct registry.</p>
            capo_ecr_public.errors.server_exception.ServerException: <p>These errors are usually caused by a server-side issue.</p>
            capo_ecr_public.errors.too_many_tags_exception.TooManyTagsException: <p>The list of tags on the repository is over the limit. The maximum number of tags that can be applied to a repository is 50.</p>
            capo_ecr_public.errors.unsupported_command_exception.UnsupportedCommandException: <p>The action isn't supported in this Region.</p>
            capo_ecr_public.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_ecr_public.types.tag_resource_request.TagResourceRequest]",
        ) -> OperationResponse[
            "capo_ecr_public.types.tag_resource_response.TagResourceResponse"
        ]:
            import capo_ecr_public._operations.spencer_frontend_service.tag_resource

            output, http_response = (
                capo_ecr_public._operations.spencer_frontend_service.tag_resource.tag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ecr_public.types.tag_resource_request.TagResourceRequest = {
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
        resource_arn: "capo_ecr_public.types.arn.Arn",
        tag_keys: "capo_ecr_public.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[ECRPUBLICClientConfig] = None,
    ) -> "capo_ecr_public.types.untag_resource_response.UntagResourceResponse":
        """<p>Deletes specified tags from a resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource to delete tags from. Currently, the supported resource is an Amazon ECR Public repository.</p>
            tag_keys: <p>The keys of the tags to be removed.</p>

        Raises:
            capo_ecr_public.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter is invalid. Review the available parameters for the API request.</p>
            capo_ecr_public.errors.invalid_tag_parameter_exception.InvalidTagParameterException: <p>An invalid parameter has been specified. Tag keys can have a maximum character length of 128 characters, and tag values can have a maximum length of 256 characters.</p>
            capo_ecr_public.errors.repository_not_found_exception.RepositoryNotFoundException: <p>The specified repository can't be found. Check the spelling of the specified repository and ensure that you're performing operations on the correct registry.</p>
            capo_ecr_public.errors.server_exception.ServerException: <p>These errors are usually caused by a server-side issue.</p>
            capo_ecr_public.errors.too_many_tags_exception.TooManyTagsException: <p>The list of tags on the repository is over the limit. The maximum number of tags that can be applied to a repository is 50.</p>
            capo_ecr_public.errors.unsupported_command_exception.UnsupportedCommandException: <p>The action isn't supported in this Region.</p>
            capo_ecr_public.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_ecr_public.types.untag_resource_request.UntagResourceRequest]",
        ) -> OperationResponse[
            "capo_ecr_public.types.untag_resource_response.UntagResourceResponse"
        ]:
            import capo_ecr_public._operations.spencer_frontend_service.untag_resource

            output, http_response = (
                capo_ecr_public._operations.spencer_frontend_service.untag_resource.untag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ecr_public.types.untag_resource_request.UntagResourceRequest = {
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

    def upload_layer_part(
        self,
        repository_name: "capo_ecr_public.types.repository_name.RepositoryName",
        upload_id: "capo_ecr_public.types.upload_id.UploadId",
        part_first_byte: "capo_ecr_public.types.part_size.PartSize",
        part_last_byte: "capo_ecr_public.types.part_size.PartSize",
        layer_part_blob: "capo_ecr_public.types.layer_part_blob.LayerPartBlob",
        *,
        config_overrides: Optional[ECRPUBLICClientConfig] = None,
        registry_id: Optional[
            "capo_ecr_public.types.registry_id_or_alias.RegistryIdOrAlias"
        ] = None,
    ) -> "capo_ecr_public.types.upload_layer_part_response.UploadLayerPartResponse":
        """<p>Uploads an image layer part to Amazon ECR.</p> <p>When an image is pushed, each new image layer is uploaded in parts. The maximum size of each image layer part can be 20971520 bytes (about 20MB). The UploadLayerPart API is called once for each new image layer part.</p> <note> <p>This operation is used by the Amazon ECR proxy and is not generally used by customers for pulling and pushing images. In most cases, you should use the <code>docker</code> CLI to pull, tag, and push images.</p> </note>

        Args:
            registry_id: <p>The Amazon Web Services account ID, or registry alias, that's associated with the registry that you're uploading layer parts to. If you do not specify a registry, the default public registry is assumed.</p>
            repository_name: <p>The name of the repository that you're uploading layer parts to.</p>
            upload_id: <p>The upload ID from a previous <a>InitiateLayerUpload</a> operation to associate with the layer part upload.</p>
            part_first_byte: <p>The position of the first byte of the layer part witin the overall image layer.</p>
            part_last_byte: <p>The position of the last byte of the layer part within the overall image layer.</p>
            layer_part_blob: <p>The base64-encoded layer part payload.</p>

        Raises:
            capo_ecr_public.errors.invalid_layer_part_exception.InvalidLayerPartException: <p>The layer part size isn't valid, or the first byte specified isn't consecutive to the last byte of a previous layer part upload.</p>
            capo_ecr_public.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter is invalid. Review the available parameters for the API request.</p>
            capo_ecr_public.errors.limit_exceeded_exception.LimitExceededException: <p>The operation didn't succeed because it would have exceeded a service limit for your account. For more information, see <a href="https://docs.aws.amazon.com/AmazonECR/latest/userguide/service-quotas.html">Amazon ECR Service Quotas</a> in the Amazon Elastic Container Registry User Guide.</p>
            capo_ecr_public.errors.registry_not_found_exception.RegistryNotFoundException: <p>The registry doesn't exist.</p>
            capo_ecr_public.errors.repository_not_found_exception.RepositoryNotFoundException: <p>The specified repository can't be found. Check the spelling of the specified repository and ensure that you're performing operations on the correct registry.</p>
            capo_ecr_public.errors.server_exception.ServerException: <p>These errors are usually caused by a server-side issue.</p>
            capo_ecr_public.errors.unsupported_command_exception.UnsupportedCommandException: <p>The action isn't supported in this Region.</p>
            capo_ecr_public.errors.upload_not_found_exception.UploadNotFoundException: <p>The upload can't be found, or the specified upload ID isn't valid for this repository.</p>
            capo_ecr_public.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_ecr_public.types.upload_layer_part_request.UploadLayerPartRequest]",
        ) -> OperationResponse[
            "capo_ecr_public.types.upload_layer_part_response.UploadLayerPartResponse"
        ]:
            import capo_ecr_public._operations.spencer_frontend_service.upload_layer_part

            output, http_response = (
                capo_ecr_public._operations.spencer_frontend_service.upload_layer_part.upload_layer_part(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ecr_public.types.upload_layer_part_request.UploadLayerPartRequest = {
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

    def __enter__(self) -> Self:
        return self

    def __exit__(self, exc_type: Any, exc: Any, tb: Any):
        self._client.close()
