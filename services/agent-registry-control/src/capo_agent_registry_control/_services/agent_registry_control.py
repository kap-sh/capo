"""Generated from Smithy shape ``com.amazonaws.agentregistrycontrol#AgentRegistryControl``."""

import uuid
import warnings
from collections.abc import Iterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import BaseHandler, Client

import capo_agent_registry_control._auth._signers
import capo_agent_registry_control._auth._sigv4
from capo_agent_registry_control._auth._identity import Credentials
from capo_agent_registry_control._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_agent_registry_control._auth._zapros_handler import AuthMiddleware
from capo_agent_registry_control._pagination import resolve_path as _resolve_path
from capo_agent_registry_control._resources.agent_registry_control.registry_record_resource import (
    RegistryRecordResource,
)
from capo_agent_registry_control._resources.agent_registry_control.registry_resource import (
    RegistryResource,
)
from capo_agent_registry_control._services._aws_config import aws_config
from capo_agent_registry_control._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import capo_agent_registry_control.types.approval_configuration
    import capo_agent_registry_control.types.auto_detection_configuration
    import capo_agent_registry_control.types.client_token
    import capo_agent_registry_control.types.create_registry_record_request
    import capo_agent_registry_control.types.create_registry_record_response
    import capo_agent_registry_control.types.create_registry_request
    import capo_agent_registry_control.types.create_registry_response
    import capo_agent_registry_control.types.delete_registry_record_request
    import capo_agent_registry_control.types.delete_registry_record_response
    import capo_agent_registry_control.types.delete_registry_request
    import capo_agent_registry_control.types.delete_registry_response
    import capo_agent_registry_control.types.description
    import capo_agent_registry_control.types.descriptors
    import capo_agent_registry_control.types.discovery_configuration
    import capo_agent_registry_control.types.encryption_configuration
    import capo_agent_registry_control.types.get_registry_record_request
    import capo_agent_registry_control.types.get_registry_record_response
    import capo_agent_registry_control.types.get_registry_request
    import capo_agent_registry_control.types.get_registry_response
    import capo_agent_registry_control.types.list_registries_request
    import capo_agent_registry_control.types.list_registries_response
    import capo_agent_registry_control.types.list_registry_records_request
    import capo_agent_registry_control.types.list_registry_records_response
    import capo_agent_registry_control.types.list_tags_for_resource_request
    import capo_agent_registry_control.types.list_tags_for_resource_response
    import capo_agent_registry_control.types.max_results
    import capo_agent_registry_control.types.next_token
    import capo_agent_registry_control.types.provenance_list
    import capo_agent_registry_control.types.record_identifier
    import capo_agent_registry_control.types.record_type
    import capo_agent_registry_control.types.registry_filter_list
    import capo_agent_registry_control.types.registry_identifier
    import capo_agent_registry_control.types.registry_name
    import capo_agent_registry_control.types.registry_record_display_name
    import capo_agent_registry_control.types.registry_record_filter_list
    import capo_agent_registry_control.types.registry_record_name
    import capo_agent_registry_control.types.registry_record_status
    import capo_agent_registry_control.types.registry_record_summary
    import capo_agent_registry_control.types.registry_record_version
    import capo_agent_registry_control.types.registry_summary
    import capo_agent_registry_control.types.resource_arn
    import capo_agent_registry_control.types.submit_registry_record_for_approval_request
    import capo_agent_registry_control.types.submit_registry_record_for_approval_response
    import capo_agent_registry_control.types.tag_key_list
    import capo_agent_registry_control.types.tag_resource_request
    import capo_agent_registry_control.types.tag_resource_response
    import capo_agent_registry_control.types.tags_map
    import capo_agent_registry_control.types.untag_resource_request
    import capo_agent_registry_control.types.untag_resource_response
    import capo_agent_registry_control.types.update_registry_record_request
    import capo_agent_registry_control.types.update_registry_record_response
    import capo_agent_registry_control.types.update_registry_record_status_request
    import capo_agent_registry_control.types.update_registry_record_status_response
    import capo_agent_registry_control.types.update_registry_request
    import capo_agent_registry_control.types.update_registry_response
    import capo_agent_registry_control.types.updated_approval_configuration
    import capo_agent_registry_control.types.updated_auto_detection_configuration
    import capo_agent_registry_control.types.updated_description
    import capo_agent_registry_control.types.updated_descriptors
    import capo_agent_registry_control.types.updated_discovery_configuration
    import capo_agent_registry_control.types.updated_display_name


class AgentRegistryControlClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class AgentRegistryControlClient:
    """A client for the ``AgentRegistryControl`` service.

    Args:
        http_handler: HTTP handler for sending requests. If not provided, creates a default handler.
        operation_interceptors: Interceptors that wrap every operation call. If not provided, defaults to an empty list.
        retry_max_attempts: Maximum number of times to retry a failed operation. Defaults to 3.
        region: The value of the ``AWS::Region`` endpoint parameter.
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
        self._config = AgentRegistryControlClientConfig(
            {
                "operation_interceptors": operation_interceptors or [],
                "retry_max_attempts": retry_max_attempts,
                "region": region,
                "endpoint": endpoint,
                "credentials_provider": resolved_credentials_provider,
            }
        )

        # resources
        self.registry_record_resource = RegistryRecordResource(self)
        self.registry_resource = RegistryResource(self)

    def operation_options(
        self, config_overrides: Optional[AgentRegistryControlClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: AgentRegistryControlClientConfig = config_overrides or {}
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
            endpoint=overrides.get("endpoint", self._config.get("endpoint")),
            credentials_provider=overrides.get(
                "credentials_provider", self._config.get("credentials_provider")
            ),
        )
        return interceptors_, options_

    def list_tags_for_resource(
        self,
        resource_arn: "capo_agent_registry_control.types.resource_arn.ResourceArn",
        *,
        config_overrides: Optional[AgentRegistryControlClientConfig] = None,
    ) -> "capo_agent_registry_control.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>Lists the tags associated with the specified Amazon Web Services Agent Registry resource. Returns the current tag key-value pairs on the resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource to list tags for. Supported resources include registries and registry records.</p>

        Raises:
            capo_agent_registry_control.errors.access_denied_exception.AccessDeniedException: <p>The caller is not authorized to perform the requested action.</p>
            capo_agent_registry_control.errors.internal_server_exception.InternalServerException: <p>The request failed due to an unexpected internal error; the caller may retry.</p>
            capo_agent_registry_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            capo_agent_registry_control.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling; the caller may retry after a delay.</p>
            capo_agent_registry_control.errors.validation_exception.ValidationException: <p>The request failed validation of one or more input fields.</p>
            capo_agent_registry_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_agent_registry_control.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> OperationResponse[
            "capo_agent_registry_control.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import capo_agent_registry_control._operations.agent_registry_control.list_tags_for_resource

            output, http_response = (
                capo_agent_registry_control._operations.agent_registry_control.list_tags_for_resource.list_tags_for_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_agent_registry_control.types.list_tags_for_resource_request.ListTagsForResourceRequest = {
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
        resource_arn: "capo_agent_registry_control.types.resource_arn.ResourceArn",
        tags: "capo_agent_registry_control.types.tags_map.TagsMap",
        *,
        config_overrides: Optional[AgentRegistryControlClientConfig] = None,
    ) -> "capo_agent_registry_control.types.tag_resource_response.TagResourceResponse":
        """<p>Adds or overwrites one or more tags for the specified Amazon Web Services Agent Registry resource. Tags are key-value pairs that you can use to categorize and manage Amazon Web Services resources. If a tag with the same key already exists on the resource, the service replaces its value with the value you specify.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource to tag. Supported resources include registries and registry records.</p>
            tags: <p>The tags to apply to the resource, as a map of tag keys to tag values. Tag keys must be unique within the request.</p>

        Raises:
            capo_agent_registry_control.errors.access_denied_exception.AccessDeniedException: <p>The caller is not authorized to perform the requested action.</p>
            capo_agent_registry_control.errors.internal_server_exception.InternalServerException: <p>The request failed due to an unexpected internal error; the caller may retry.</p>
            capo_agent_registry_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            capo_agent_registry_control.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would exceed a service quota.</p>
            capo_agent_registry_control.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling; the caller may retry after a delay.</p>
            capo_agent_registry_control.errors.validation_exception.ValidationException: <p>The request failed validation of one or more input fields.</p>
            capo_agent_registry_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_agent_registry_control.types.tag_resource_request.TagResourceRequest]",
        ) -> OperationResponse[
            "capo_agent_registry_control.types.tag_resource_response.TagResourceResponse"
        ]:
            import capo_agent_registry_control._operations.agent_registry_control.tag_resource

            output, http_response = (
                capo_agent_registry_control._operations.agent_registry_control.tag_resource.tag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_agent_registry_control.types.tag_resource_request.TagResourceRequest = {
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
        resource_arn: "capo_agent_registry_control.types.resource_arn.ResourceArn",
        tag_keys: "capo_agent_registry_control.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[AgentRegistryControlClientConfig] = None,
    ) -> "capo_agent_registry_control.types.untag_resource_response.UntagResourceResponse":
        """<p>Removes one or more tags from the specified Amazon Web Services Agent Registry resource. The operation removes only the tags whose keys you supply; other tags on the resource remain unchanged.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource to remove tags from. Supported resources include registries and registry records.</p>
            tag_keys: <p>The keys of the tags to remove from the resource. Tags with keys not included in this list remain on the resource.</p>

        Raises:
            capo_agent_registry_control.errors.access_denied_exception.AccessDeniedException: <p>The caller is not authorized to perform the requested action.</p>
            capo_agent_registry_control.errors.internal_server_exception.InternalServerException: <p>The request failed due to an unexpected internal error; the caller may retry.</p>
            capo_agent_registry_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            capo_agent_registry_control.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling; the caller may retry after a delay.</p>
            capo_agent_registry_control.errors.validation_exception.ValidationException: <p>The request failed validation of one or more input fields.</p>
            capo_agent_registry_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_agent_registry_control.types.untag_resource_request.UntagResourceRequest]",
        ) -> OperationResponse[
            "capo_agent_registry_control.types.untag_resource_response.UntagResourceResponse"
        ]:
            import capo_agent_registry_control._operations.agent_registry_control.untag_resource

            output, http_response = (
                capo_agent_registry_control._operations.agent_registry_control.untag_resource.untag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_agent_registry_control.types.untag_resource_request.UntagResourceRequest = {
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

    def create_registry_record(
        self,
        registry_id: "capo_agent_registry_control.types.registry_identifier.RegistryIdentifier",
        name: "capo_agent_registry_control.types.registry_record_name.RegistryRecordName",
        record_type: "capo_agent_registry_control.types.record_type.RecordType",
        descriptors: "capo_agent_registry_control.types.descriptors.Descriptors",
        *,
        config_overrides: Optional[AgentRegistryControlClientConfig] = None,
        display_name: Optional[
            "capo_agent_registry_control.types.registry_record_display_name.RegistryRecordDisplayName"
        ] = None,
        description: Optional[
            "capo_agent_registry_control.types.description.Description"
        ] = None,
        record_version: Optional[
            "capo_agent_registry_control.types.registry_record_version.RegistryRecordVersion"
        ] = None,
        client_token: Optional[
            "capo_agent_registry_control.types.client_token.ClientToken"
        ] = None,
        provenance: Optional[
            "capo_agent_registry_control.types.provenance_list.ProvenanceList"
        ] = None,
        tags: Optional["capo_agent_registry_control.types.tags_map.TagsMap"] = None,
    ) -> "capo_agent_registry_control.types.create_registry_record_response.CreateRegistryRecordResponse":
        """<p>Creates a registry record within a registry. A registry record describes a discoverable resource, such as an MCP server, an agent, an agent skill, or a custom resource. Creation is asynchronous: the record is returned with the CREATING status while it is processed.</p>

        Args:
            registry_id: <p>The identifier of the registry in which to create the record (ARN or ID)</p>
            name: <p>The name of the registry record</p>
            display_name: <p>The human-readable display name of the registry record</p>
            description: <p>The description of the registry record</p>
            record_type: <p>The type of the registry record, which determines the descriptor format</p>
            descriptors: <p>The typed descriptor content for the registry record</p>
            record_version: <p>The version of the registry record</p>
            client_token: <p>Client token for idempotency</p>
            tags: <p>Tags to associate with the registry record</p>

        Raises:
            capo_agent_registry_control.errors.access_denied_exception.AccessDeniedException: <p>The caller is not authorized to perform the requested action.</p>
            capo_agent_registry_control.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource.</p>
            capo_agent_registry_control.errors.internal_server_exception.InternalServerException: <p>The request failed due to an unexpected internal error; the caller may retry.</p>
            capo_agent_registry_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            capo_agent_registry_control.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would exceed a service quota.</p>
            capo_agent_registry_control.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling; the caller may retry after a delay.</p>
            capo_agent_registry_control.errors.validation_exception.ValidationException: <p>The request failed validation of one or more input fields.</p>
            capo_agent_registry_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_agent_registry_control.types.create_registry_record_request.CreateRegistryRecordRequest]",
        ) -> OperationResponse[
            "capo_agent_registry_control.types.create_registry_record_response.CreateRegistryRecordResponse"
        ]:
            import capo_agent_registry_control._operations.agent_registry_control.create_registry_record

            output, http_response = (
                capo_agent_registry_control._operations.agent_registry_control.create_registry_record.create_registry_record(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_agent_registry_control.types.create_registry_record_request.CreateRegistryRecordRequest = {
            "registry_id": registry_id,
            "name": name,
            "record_type": record_type,
            "descriptors": descriptors,
        }
        if display_name is not None:
            input_["display_name"] = display_name
        if description is not None:
            input_["description"] = description
        if record_version is not None:
            input_["record_version"] = record_version
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if provenance is not None:
            input_["provenance"] = provenance
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_registry_record(
        self,
        registry_id: "capo_agent_registry_control.types.registry_identifier.RegistryIdentifier",
        record_id: "capo_agent_registry_control.types.record_identifier.RecordIdentifier",
        *,
        config_overrides: Optional[AgentRegistryControlClientConfig] = None,
    ) -> "capo_agent_registry_control.types.get_registry_record_response.GetRegistryRecordResponse":
        """<p>Retrieves the details of a registry record</p>

        Args:
            registry_id: <p>The identifier of the registry containing the record (ARN or ID)</p>
            record_id: <p>The identifier of the registry record to retrieve (ARN or ID)</p>

        Raises:
            capo_agent_registry_control.errors.access_denied_exception.AccessDeniedException: <p>The caller is not authorized to perform the requested action.</p>
            capo_agent_registry_control.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource.</p>
            capo_agent_registry_control.errors.internal_server_exception.InternalServerException: <p>The request failed due to an unexpected internal error; the caller may retry.</p>
            capo_agent_registry_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            capo_agent_registry_control.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling; the caller may retry after a delay.</p>
            capo_agent_registry_control.errors.validation_exception.ValidationException: <p>The request failed validation of one or more input fields.</p>
            capo_agent_registry_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_agent_registry_control.types.get_registry_record_request.GetRegistryRecordRequest]",
        ) -> OperationResponse[
            "capo_agent_registry_control.types.get_registry_record_response.GetRegistryRecordResponse"
        ]:
            import capo_agent_registry_control._operations.agent_registry_control.get_registry_record

            output, http_response = (
                capo_agent_registry_control._operations.agent_registry_control.get_registry_record.get_registry_record(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_agent_registry_control.types.get_registry_record_request.GetRegistryRecordRequest = {
            "registry_id": registry_id,
            "record_id": record_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_registry_record(
        self,
        registry_id: "capo_agent_registry_control.types.registry_identifier.RegistryIdentifier",
        record_id: "capo_agent_registry_control.types.record_identifier.RecordIdentifier",
        *,
        config_overrides: Optional[AgentRegistryControlClientConfig] = None,
        name: Optional[
            "capo_agent_registry_control.types.registry_record_name.RegistryRecordName"
        ] = None,
        display_name: Optional[
            "capo_agent_registry_control.types.updated_display_name.UpdatedDisplayName"
        ] = None,
        description: Optional[
            "capo_agent_registry_control.types.updated_description.UpdatedDescription"
        ] = None,
        record_type: Optional[
            "capo_agent_registry_control.types.record_type.RecordType"
        ] = None,
        descriptors: Optional[
            "capo_agent_registry_control.types.updated_descriptors.UpdatedDescriptors"
        ] = None,
        record_version: Optional[
            "capo_agent_registry_control.types.registry_record_version.RegistryRecordVersion"
        ] = None,
        trigger_synchronization: Optional[bool] = None,
        provenance: Optional[
            "capo_agent_registry_control.types.provenance_list.ProvenanceList"
        ] = None,
    ) -> "capo_agent_registry_control.types.update_registry_record_response.UpdateRegistryRecordResponse":
        """<p>Updates a registry record. The update is asynchronous: the record is returned with the UPDATING status while it is processed. Fields that use update wrappers follow PATCH semantics: omit the field to leave it unchanged.</p>

        Args:
            registry_id: <p>The identifier of the registry containing the record (ARN or ID)</p>
            record_id: <p>The identifier of the registry record to update (ARN or ID)</p>
            name: <p>The updated name of the registry record. Omit to leave the name unchanged.</p>
            display_name: <p>The updated display name of the registry record. Omit to leave the display name unchanged; provide an empty wrapper to unset it.</p>
            description: <p>The updated description of the registry record. Omit to leave the description unchanged; provide an empty wrapper to unset it.</p>
            record_type: <p>The updated type of the registry record. Omit to leave the record type unchanged.</p>
            descriptors: <p>The updated typed descriptor content for the registry record. Omit to leave the descriptors unchanged.</p>
            record_version: <p>The updated version of the registry record. Omit to leave the version unchanged.</p>
            trigger_synchronization: <p>Whether to trigger synchronization of the record's descriptor content from its source</p>

        Raises:
            capo_agent_registry_control.errors.access_denied_exception.AccessDeniedException: <p>The caller is not authorized to perform the requested action.</p>
            capo_agent_registry_control.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource.</p>
            capo_agent_registry_control.errors.internal_server_exception.InternalServerException: <p>The request failed due to an unexpected internal error; the caller may retry.</p>
            capo_agent_registry_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            capo_agent_registry_control.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling; the caller may retry after a delay.</p>
            capo_agent_registry_control.errors.validation_exception.ValidationException: <p>The request failed validation of one or more input fields.</p>
            capo_agent_registry_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_agent_registry_control.types.update_registry_record_request.UpdateRegistryRecordRequest]",
        ) -> OperationResponse[
            "capo_agent_registry_control.types.update_registry_record_response.UpdateRegistryRecordResponse"
        ]:
            import capo_agent_registry_control._operations.agent_registry_control.update_registry_record

            output, http_response = (
                capo_agent_registry_control._operations.agent_registry_control.update_registry_record.update_registry_record(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_agent_registry_control.types.update_registry_record_request.UpdateRegistryRecordRequest = {
            "registry_id": registry_id,
            "record_id": record_id,
        }
        if name is not None:
            input_["name"] = name
        if display_name is not None:
            input_["display_name"] = display_name
        if description is not None:
            input_["description"] = description
        if record_type is not None:
            input_["record_type"] = record_type
        if descriptors is not None:
            input_["descriptors"] = descriptors
        if record_version is not None:
            input_["record_version"] = record_version
        if trigger_synchronization is not None:
            input_["trigger_synchronization"] = trigger_synchronization
        if provenance is not None:
            input_["provenance"] = provenance

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_registry_record(
        self,
        registry_id: "capo_agent_registry_control.types.registry_identifier.RegistryIdentifier",
        record_id: "capo_agent_registry_control.types.record_identifier.RecordIdentifier",
        *,
        config_overrides: Optional[AgentRegistryControlClientConfig] = None,
    ) -> "capo_agent_registry_control.types.delete_registry_record_response.DeleteRegistryRecordResponse":
        """<p>Deletes a registry record</p>

        Args:
            registry_id: <p>The identifier of the registry containing the record (ARN or ID)</p>
            record_id: <p>The identifier of the registry record to delete (ARN or ID)</p>

        Raises:
            capo_agent_registry_control.errors.access_denied_exception.AccessDeniedException: <p>The caller is not authorized to perform the requested action.</p>
            capo_agent_registry_control.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource.</p>
            capo_agent_registry_control.errors.internal_server_exception.InternalServerException: <p>The request failed due to an unexpected internal error; the caller may retry.</p>
            capo_agent_registry_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            capo_agent_registry_control.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling; the caller may retry after a delay.</p>
            capo_agent_registry_control.errors.validation_exception.ValidationException: <p>The request failed validation of one or more input fields.</p>
            capo_agent_registry_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_agent_registry_control.types.delete_registry_record_request.DeleteRegistryRecordRequest]",
        ) -> OperationResponse[
            "capo_agent_registry_control.types.delete_registry_record_response.DeleteRegistryRecordResponse"
        ]:
            import capo_agent_registry_control._operations.agent_registry_control.delete_registry_record

            output, http_response = (
                capo_agent_registry_control._operations.agent_registry_control.delete_registry_record.delete_registry_record(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_agent_registry_control.types.delete_registry_record_request.DeleteRegistryRecordRequest = {
            "registry_id": registry_id,
            "record_id": record_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_registry_records(
        self,
        registry_id: "capo_agent_registry_control.types.registry_identifier.RegistryIdentifier",
        *,
        config_overrides: Optional[AgentRegistryControlClientConfig] = None,
        max_results: Optional[
            "capo_agent_registry_control.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_agent_registry_control.types.next_token.NextToken"
        ] = None,
        filters: Optional[
            "capo_agent_registry_control.types.registry_record_filter_list.RegistryRecordFilterList"
        ] = None,
    ) -> "capo_agent_registry_control.types.list_registry_records_response.ListRegistryRecordsResponse":
        """<p>Lists the registry records within a registry, with optional filtering by name, status, and record type</p>

        Args:
            registry_id: <p>The identifier of the registry to list records from (ARN or ID)</p>
            max_results: <p>Maximum number of records to return</p>
            next_token: <p>Token for pagination</p>
            filters: <p>Filters to apply to the registry record list</p>

        Raises:
            capo_agent_registry_control.errors.access_denied_exception.AccessDeniedException: <p>The caller is not authorized to perform the requested action.</p>
            capo_agent_registry_control.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource.</p>
            capo_agent_registry_control.errors.internal_server_exception.InternalServerException: <p>The request failed due to an unexpected internal error; the caller may retry.</p>
            capo_agent_registry_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            capo_agent_registry_control.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling; the caller may retry after a delay.</p>
            capo_agent_registry_control.errors.validation_exception.ValidationException: <p>The request failed validation of one or more input fields.</p>
            capo_agent_registry_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_agent_registry_control.types.list_registry_records_request.ListRegistryRecordsRequest]",
        ) -> OperationResponse[
            "capo_agent_registry_control.types.list_registry_records_response.ListRegistryRecordsResponse"
        ]:
            import capo_agent_registry_control._operations.agent_registry_control.list_registry_records

            output, http_response = (
                capo_agent_registry_control._operations.agent_registry_control.list_registry_records.list_registry_records(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_agent_registry_control.types.list_registry_records_request.ListRegistryRecordsRequest = {
            "registry_id": registry_id
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if filters is not None:
            input_["filters"] = filters

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_registry_records(
        self,
        registry_id: "capo_agent_registry_control.types.registry_identifier.RegistryIdentifier",
        *,
        config_overrides: Optional[AgentRegistryControlClientConfig] = None,
        max_results: Optional[
            "capo_agent_registry_control.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_agent_registry_control.types.next_token.NextToken"
        ] = None,
        filters: Optional[
            "capo_agent_registry_control.types.registry_record_filter_list.RegistryRecordFilterList"
        ] = None,
    ) -> "Iterator[capo_agent_registry_control.types.registry_record_summary.RegistryRecordSummary]":
        _token = next_token
        while True:
            _response = self.list_registry_records(
                registry_id,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
                filters=filters,
            )
            _page = _resolve_path(_response, ("registry_records",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def submit_registry_record_for_approval(
        self,
        registry_id: "capo_agent_registry_control.types.registry_identifier.RegistryIdentifier",
        record_id: "capo_agent_registry_control.types.record_identifier.RecordIdentifier",
        *,
        config_overrides: Optional[AgentRegistryControlClientConfig] = None,
    ) -> "capo_agent_registry_control.types.submit_registry_record_for_approval_response.SubmitRegistryRecordForApprovalResponse":
        """<p>Submits a DRAFT registry record for approval, moving it into the registry's approval workflow. Depending on the registry's approval configuration, the record is either auto-approved or set to PENDING_APPROVAL for a curator to approve or reject.</p>

        Args:
            registry_id: <p>The identifier of the registry containing the record (ARN or ID)</p>
            record_id: <p>The identifier of the registry record to submit for approval (ARN or ID)</p>

        Raises:
            capo_agent_registry_control.errors.access_denied_exception.AccessDeniedException: <p>The caller is not authorized to perform the requested action.</p>
            capo_agent_registry_control.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource.</p>
            capo_agent_registry_control.errors.internal_server_exception.InternalServerException: <p>The request failed due to an unexpected internal error; the caller may retry.</p>
            capo_agent_registry_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            capo_agent_registry_control.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling; the caller may retry after a delay.</p>
            capo_agent_registry_control.errors.validation_exception.ValidationException: <p>The request failed validation of one or more input fields.</p>
            capo_agent_registry_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_agent_registry_control.types.submit_registry_record_for_approval_request.SubmitRegistryRecordForApprovalRequest]",
        ) -> OperationResponse[
            "capo_agent_registry_control.types.submit_registry_record_for_approval_response.SubmitRegistryRecordForApprovalResponse"
        ]:
            import capo_agent_registry_control._operations.agent_registry_control.submit_registry_record_for_approval

            output, http_response = (
                capo_agent_registry_control._operations.agent_registry_control.submit_registry_record_for_approval.submit_registry_record_for_approval(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_agent_registry_control.types.submit_registry_record_for_approval_request.SubmitRegistryRecordForApprovalRequest = {
            "registry_id": registry_id,
            "record_id": record_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_registry_record_status(
        self,
        registry_id: "capo_agent_registry_control.types.registry_identifier.RegistryIdentifier",
        record_id: "capo_agent_registry_control.types.record_identifier.RecordIdentifier",
        status: "capo_agent_registry_control.types.registry_record_status.RegistryRecordStatus",
        status_reason: str,
        *,
        config_overrides: Optional[AgentRegistryControlClientConfig] = None,
    ) -> "capo_agent_registry_control.types.update_registry_record_status_response.UpdateRegistryRecordStatusResponse":
        """<p>Updates the status of a registry record as part of the registry's curation workflow, for example to approve or reject a record that is pending approval, or to deprecate an approved record so that it is no longer discoverable</p>

        Args:
            registry_id: <p>The identifier of the registry containing the record (ARN or ID)</p>
            record_id: <p>The identifier of the registry record to update the status of (ARN or ID)</p>
            status: <p>The target status for the registry record</p>
            status_reason: <p>The reason for the status change, for example why the record was approved, rejected, or deprecated</p>

        Raises:
            capo_agent_registry_control.errors.access_denied_exception.AccessDeniedException: <p>The caller is not authorized to perform the requested action.</p>
            capo_agent_registry_control.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource.</p>
            capo_agent_registry_control.errors.internal_server_exception.InternalServerException: <p>The request failed due to an unexpected internal error; the caller may retry.</p>
            capo_agent_registry_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            capo_agent_registry_control.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling; the caller may retry after a delay.</p>
            capo_agent_registry_control.errors.validation_exception.ValidationException: <p>The request failed validation of one or more input fields.</p>
            capo_agent_registry_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_agent_registry_control.types.update_registry_record_status_request.UpdateRegistryRecordStatusRequest]",
        ) -> OperationResponse[
            "capo_agent_registry_control.types.update_registry_record_status_response.UpdateRegistryRecordStatusResponse"
        ]:
            import capo_agent_registry_control._operations.agent_registry_control.update_registry_record_status

            output, http_response = (
                capo_agent_registry_control._operations.agent_registry_control.update_registry_record_status.update_registry_record_status(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_agent_registry_control.types.update_registry_record_status_request.UpdateRegistryRecordStatusRequest = {
            "registry_id": registry_id,
            "record_id": record_id,
            "status": status,
            "status_reason": status_reason,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_registry(
        self,
        name: "capo_agent_registry_control.types.registry_name.RegistryName",
        *,
        config_overrides: Optional[AgentRegistryControlClientConfig] = None,
        description: Optional[
            "capo_agent_registry_control.types.description.Description"
        ] = None,
        encryption_configuration: Optional[
            "capo_agent_registry_control.types.encryption_configuration.EncryptionConfiguration"
        ] = None,
        discovery_configuration: Optional[
            "capo_agent_registry_control.types.discovery_configuration.DiscoveryConfiguration"
        ] = None,
        client_token: Optional[
            "capo_agent_registry_control.types.client_token.ClientToken"
        ] = None,
        tags: Optional["capo_agent_registry_control.types.tags_map.TagsMap"] = None,
        approval_configuration: Optional[
            "capo_agent_registry_control.types.approval_configuration.ApprovalConfiguration"
        ] = None,
        auto_detection_configuration: Optional[
            "capo_agent_registry_control.types.auto_detection_configuration.AutoDetectionConfiguration"
        ] = None,
    ) -> "capo_agent_registry_control.types.create_registry_response.CreateRegistryResponse":
        """<p>Creates a new registry, a catalog that organizes registry records and defines their discovery authorization and record approval behavior. Creation is asynchronous: the registry begins in the CREATING status and becomes usable once it reaches READY.</p>

        Args:
            name: <p>The name of the registry</p>
            description: <p>The description of the registry</p>
            encryption_configuration: <p>The optional server-side encryption configuration for the registry. When you provide this field, the specified customer-managed Amazon Web Services KMS key encrypts the registry's content. Omit this field to use an Amazon Web Services-owned encryption key. You cannot change the encryption configuration after registry creation.</p>
            discovery_configuration: <p>Discovery configuration for the registry</p>
            client_token: <p>A unique, case-sensitive identifier to ensure that the operation completes no more than one time. If this token matches a previous request, the service ignores the request, but does not return an error.</p>
            tags: <p>Tags to associate with the registry</p>
            approval_configuration: <p>Approval configuration for registry records</p>
            auto_detection_configuration: <p>The optional auto-detection configuration for the registry. When provided, the registry is automatically populated with resources discovered according to the configuration. Omit this field for registries whose records are managed exclusively through the Agent Registry Control API.</p>

        Raises:
            capo_agent_registry_control.errors.access_denied_exception.AccessDeniedException: <p>The caller is not authorized to perform the requested action.</p>
            capo_agent_registry_control.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource.</p>
            capo_agent_registry_control.errors.internal_server_exception.InternalServerException: <p>The request failed due to an unexpected internal error; the caller may retry.</p>
            capo_agent_registry_control.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would exceed a service quota.</p>
            capo_agent_registry_control.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling; the caller may retry after a delay.</p>
            capo_agent_registry_control.errors.validation_exception.ValidationException: <p>The request failed validation of one or more input fields.</p>
            capo_agent_registry_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_agent_registry_control.types.create_registry_request.CreateRegistryRequest]",
        ) -> OperationResponse[
            "capo_agent_registry_control.types.create_registry_response.CreateRegistryResponse"
        ]:
            import capo_agent_registry_control._operations.agent_registry_control.create_registry

            output, http_response = (
                capo_agent_registry_control._operations.agent_registry_control.create_registry.create_registry(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_agent_registry_control.types.create_registry_request.CreateRegistryRequest = {
            "name": name
        }
        if description is not None:
            input_["description"] = description
        if encryption_configuration is not None:
            input_["encryption_configuration"] = encryption_configuration
        if discovery_configuration is not None:
            input_["discovery_configuration"] = discovery_configuration
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if tags is not None:
            input_["tags"] = tags
        if approval_configuration is not None:
            input_["approval_configuration"] = approval_configuration
        if auto_detection_configuration is not None:
            input_["auto_detection_configuration"] = auto_detection_configuration

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_registry(
        self,
        registry_id: "capo_agent_registry_control.types.registry_identifier.RegistryIdentifier",
        *,
        config_overrides: Optional[AgentRegistryControlClientConfig] = None,
    ) -> "capo_agent_registry_control.types.get_registry_response.GetRegistryResponse":
        """<p>Gets a registry by identifier (ARN or ID)</p>

        Args:
            registry_id: <p>The identifier of the registry to retrieve (ARN or ID)</p>

        Raises:
            capo_agent_registry_control.errors.access_denied_exception.AccessDeniedException: <p>The caller is not authorized to perform the requested action.</p>
            capo_agent_registry_control.errors.internal_server_exception.InternalServerException: <p>The request failed due to an unexpected internal error; the caller may retry.</p>
            capo_agent_registry_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            capo_agent_registry_control.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling; the caller may retry after a delay.</p>
            capo_agent_registry_control.errors.validation_exception.ValidationException: <p>The request failed validation of one or more input fields.</p>
            capo_agent_registry_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_agent_registry_control.types.get_registry_request.GetRegistryRequest]",
        ) -> OperationResponse[
            "capo_agent_registry_control.types.get_registry_response.GetRegistryResponse"
        ]:
            import capo_agent_registry_control._operations.agent_registry_control.get_registry

            output, http_response = (
                capo_agent_registry_control._operations.agent_registry_control.get_registry.get_registry(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_agent_registry_control.types.get_registry_request.GetRegistryRequest = {
            "registry_id": registry_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_registry(
        self,
        registry_id: "capo_agent_registry_control.types.registry_identifier.RegistryIdentifier",
        *,
        config_overrides: Optional[AgentRegistryControlClientConfig] = None,
        name: Optional[
            "capo_agent_registry_control.types.registry_name.RegistryName"
        ] = None,
        description: Optional[
            "capo_agent_registry_control.types.updated_description.UpdatedDescription"
        ] = None,
        discovery_configuration: Optional[
            "capo_agent_registry_control.types.updated_discovery_configuration.UpdatedDiscoveryConfiguration"
        ] = None,
        approval_configuration: Optional[
            "capo_agent_registry_control.types.updated_approval_configuration.UpdatedApprovalConfiguration"
        ] = None,
        auto_detection_configuration: Optional[
            "capo_agent_registry_control.types.updated_auto_detection_configuration.UpdatedAutoDetectionConfiguration"
        ] = None,
    ) -> "capo_agent_registry_control.types.update_registry_response.UpdateRegistryResponse":
        """<p>Updates an existing registry. This operation uses PATCH semantics: specify only the fields you want to change, and omit the rest to leave them unchanged. Updates are applied asynchronously and the registry transitions to the UPDATING status while they are processed.</p>

        Args:
            registry_id: <p>The identifier of the registry to update (ARN or ID)</p>
            name: <p>The updated name of the registry</p>
            description: <p>The updated description of the registry</p>
            discovery_configuration: <p>The updated discovery configuration. Changing the discovery authorization can break existing consumers that rely on the previous authorization type.</p>
            approval_configuration: <p>The updated approval configuration. The change applies only to records that move to PENDING_APPROVAL after the update; records already in PENDING_APPROVAL are unaffected.</p>
            auto_detection_configuration: <p>The updated auto-detection configuration for the registry, with PATCH semantics. Omit this field to leave the current configuration unchanged. Supply an empty wrapper to unset it. Supply <code>optionalValue</code> to replace it.</p>

        Raises:
            capo_agent_registry_control.errors.access_denied_exception.AccessDeniedException: <p>The caller is not authorized to perform the requested action.</p>
            capo_agent_registry_control.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource.</p>
            capo_agent_registry_control.errors.internal_server_exception.InternalServerException: <p>The request failed due to an unexpected internal error; the caller may retry.</p>
            capo_agent_registry_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            capo_agent_registry_control.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would exceed a service quota.</p>
            capo_agent_registry_control.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling; the caller may retry after a delay.</p>
            capo_agent_registry_control.errors.validation_exception.ValidationException: <p>The request failed validation of one or more input fields.</p>
            capo_agent_registry_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_agent_registry_control.types.update_registry_request.UpdateRegistryRequest]",
        ) -> OperationResponse[
            "capo_agent_registry_control.types.update_registry_response.UpdateRegistryResponse"
        ]:
            import capo_agent_registry_control._operations.agent_registry_control.update_registry

            output, http_response = (
                capo_agent_registry_control._operations.agent_registry_control.update_registry.update_registry(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_agent_registry_control.types.update_registry_request.UpdateRegistryRequest = {
            "registry_id": registry_id
        }
        if name is not None:
            input_["name"] = name
        if description is not None:
            input_["description"] = description
        if discovery_configuration is not None:
            input_["discovery_configuration"] = discovery_configuration
        if approval_configuration is not None:
            input_["approval_configuration"] = approval_configuration
        if auto_detection_configuration is not None:
            input_["auto_detection_configuration"] = auto_detection_configuration

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_registry(
        self,
        registry_id: "capo_agent_registry_control.types.registry_identifier.RegistryIdentifier",
        *,
        config_overrides: Optional[AgentRegistryControlClientConfig] = None,
    ) -> "capo_agent_registry_control.types.delete_registry_response.DeleteRegistryResponse":
        """<p>Deletes a registry. Deletion is asynchronous: the registry transitions to the DELETING status and is removed along with its registry records.</p>

        Args:
            registry_id: <p>The identifier of the registry to delete (ARN or ID)</p>

        Raises:
            capo_agent_registry_control.errors.access_denied_exception.AccessDeniedException: <p>The caller is not authorized to perform the requested action.</p>
            capo_agent_registry_control.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource.</p>
            capo_agent_registry_control.errors.internal_server_exception.InternalServerException: <p>The request failed due to an unexpected internal error; the caller may retry.</p>
            capo_agent_registry_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            capo_agent_registry_control.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling; the caller may retry after a delay.</p>
            capo_agent_registry_control.errors.validation_exception.ValidationException: <p>The request failed validation of one or more input fields.</p>
            capo_agent_registry_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_agent_registry_control.types.delete_registry_request.DeleteRegistryRequest]",
        ) -> OperationResponse[
            "capo_agent_registry_control.types.delete_registry_response.DeleteRegistryResponse"
        ]:
            import capo_agent_registry_control._operations.agent_registry_control.delete_registry

            output, http_response = (
                capo_agent_registry_control._operations.agent_registry_control.delete_registry.delete_registry(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_agent_registry_control.types.delete_registry_request.DeleteRegistryRequest = {
            "registry_id": registry_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_registries(
        self,
        *,
        config_overrides: Optional[AgentRegistryControlClientConfig] = None,
        max_results: Optional[
            "capo_agent_registry_control.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_agent_registry_control.types.next_token.NextToken"
        ] = None,
        filters: Optional[
            "capo_agent_registry_control.types.registry_filter_list.RegistryFilterList"
        ] = None,
    ) -> "capo_agent_registry_control.types.list_registries_response.ListRegistriesResponse":
        """<p>Lists the registries in the caller's account and Region, with optional filtering by status and discovery authorizer type</p>

        Args:
            max_results: <p>Maximum number of results to return</p>
            next_token: <p>Token for pagination</p>
            filters: <p>Filters to apply to the registry list</p>

        Raises:
            capo_agent_registry_control.errors.access_denied_exception.AccessDeniedException: <p>The caller is not authorized to perform the requested action.</p>
            capo_agent_registry_control.errors.internal_server_exception.InternalServerException: <p>The request failed due to an unexpected internal error; the caller may retry.</p>
            capo_agent_registry_control.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling; the caller may retry after a delay.</p>
            capo_agent_registry_control.errors.validation_exception.ValidationException: <p>The request failed validation of one or more input fields.</p>
            capo_agent_registry_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_agent_registry_control.types.list_registries_request.ListRegistriesRequest]",
        ) -> OperationResponse[
            "capo_agent_registry_control.types.list_registries_response.ListRegistriesResponse"
        ]:
            import capo_agent_registry_control._operations.agent_registry_control.list_registries

            output, http_response = (
                capo_agent_registry_control._operations.agent_registry_control.list_registries.list_registries(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_agent_registry_control.types.list_registries_request.ListRegistriesRequest = {}
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if filters is not None:
            input_["filters"] = filters

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_registries(
        self,
        *,
        config_overrides: Optional[AgentRegistryControlClientConfig] = None,
        max_results: Optional[
            "capo_agent_registry_control.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_agent_registry_control.types.next_token.NextToken"
        ] = None,
        filters: Optional[
            "capo_agent_registry_control.types.registry_filter_list.RegistryFilterList"
        ] = None,
    ) -> "Iterator[capo_agent_registry_control.types.registry_summary.RegistrySummary]":
        _token = next_token
        while True:
            _response = self.list_registries(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
                filters=filters,
            )
            _page = _resolve_path(_response, ("registries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def __enter__(self) -> Self:
        return self

    def __exit__(self, exc_type: Any, exc: Any, tb: Any):
        self._client.close()
