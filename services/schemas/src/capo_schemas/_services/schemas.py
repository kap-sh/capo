"""Generated from Smithy shape ``com.amazonaws.schemas#schemas``."""

import uuid
import warnings
from collections.abc import Iterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import BaseHandler, Client

import capo_schemas._auth._signers
import capo_schemas._auth._sigv4
from capo_schemas._auth._identity import Credentials
from capo_schemas._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_schemas._auth._zapros_handler import AuthMiddleware
from capo_schemas._pagination import resolve_path as _resolve_path
from capo_schemas._services._aws_config import aws_config
from capo_schemas._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import capo_schemas.types.__boolean
    import capo_schemas.types.__integer
    import capo_schemas.types.__list_of__string
    import capo_schemas.types.__list_of_get_discovered_schema_version_item_input
    import capo_schemas.types.__string
    import capo_schemas.types.__string_min0_max36
    import capo_schemas.types.__string_min0_max256
    import capo_schemas.types.__string_min1_max100000
    import capo_schemas.types.__string_min20_max1600
    import capo_schemas.types.create_discoverer_request
    import capo_schemas.types.create_discoverer_response
    import capo_schemas.types.create_registry_request
    import capo_schemas.types.create_registry_response
    import capo_schemas.types.create_schema_request
    import capo_schemas.types.create_schema_response
    import capo_schemas.types.delete_discoverer_request
    import capo_schemas.types.delete_registry_request
    import capo_schemas.types.delete_resource_policy_request
    import capo_schemas.types.delete_schema_request
    import capo_schemas.types.delete_schema_version_request
    import capo_schemas.types.describe_code_binding_request
    import capo_schemas.types.describe_code_binding_response
    import capo_schemas.types.describe_discoverer_request
    import capo_schemas.types.describe_discoverer_response
    import capo_schemas.types.describe_registry_request
    import capo_schemas.types.describe_registry_response
    import capo_schemas.types.describe_schema_request
    import capo_schemas.types.describe_schema_response
    import capo_schemas.types.discoverer_summary
    import capo_schemas.types.export_schema_request
    import capo_schemas.types.export_schema_response
    import capo_schemas.types.get_code_binding_source_request
    import capo_schemas.types.get_code_binding_source_response
    import capo_schemas.types.get_discovered_schema_request
    import capo_schemas.types.get_discovered_schema_response
    import capo_schemas.types.get_resource_policy_request
    import capo_schemas.types.get_resource_policy_response
    import capo_schemas.types.list_discoverers_request
    import capo_schemas.types.list_discoverers_response
    import capo_schemas.types.list_registries_request
    import capo_schemas.types.list_registries_response
    import capo_schemas.types.list_schema_versions_request
    import capo_schemas.types.list_schema_versions_response
    import capo_schemas.types.list_schemas_request
    import capo_schemas.types.list_schemas_response
    import capo_schemas.types.list_tags_for_resource_request
    import capo_schemas.types.list_tags_for_resource_response
    import capo_schemas.types.put_code_binding_request
    import capo_schemas.types.put_code_binding_response
    import capo_schemas.types.put_resource_policy_request
    import capo_schemas.types.put_resource_policy_response
    import capo_schemas.types.registry_summary
    import capo_schemas.types.schema_summary
    import capo_schemas.types.schema_version_summary
    import capo_schemas.types.search_schema_summary
    import capo_schemas.types.search_schemas_request
    import capo_schemas.types.search_schemas_response
    import capo_schemas.types.start_discoverer_request
    import capo_schemas.types.start_discoverer_response
    import capo_schemas.types.stop_discoverer_request
    import capo_schemas.types.stop_discoverer_response
    import capo_schemas.types.synthesized_json__string
    import capo_schemas.types.tag_resource_request
    import capo_schemas.types.tags
    import capo_schemas.types.type
    import capo_schemas.types.untag_resource_request
    import capo_schemas.types.update_discoverer_request
    import capo_schemas.types.update_discoverer_response
    import capo_schemas.types.update_registry_request
    import capo_schemas.types.update_registry_response
    import capo_schemas.types.update_schema_request
    import capo_schemas.types.update_schema_response


class schemasClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None
    anonymous: bool | None


class schemasClient:
    """A client for the ``schemas`` service.

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
        self._config = schemasClientConfig(
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
        self, config_overrides: Optional[schemasClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: schemasClientConfig = config_overrides or {}
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

    def create_discoverer(
        self,
        *,
        config_overrides: Optional[schemasClientConfig] = None,
        description: Optional[
            "capo_schemas.types.__string_min0_max256.__stringMin0Max256"
        ] = None,
        source_arn: Optional[
            "capo_schemas.types.__string_min20_max1600.__stringMin20Max1600"
        ] = None,
        cross_account: Optional["capo_schemas.types.__boolean.__boolean"] = None,
        tags: Optional["capo_schemas.types.tags.Tags"] = None,
    ) -> "capo_schemas.types.create_discoverer_response.CreateDiscovererResponse":
        """<p>Creates a discoverer.</p>

        Args:
            description: <p>A description for the discoverer.</p>
            source_arn: <p>The ARN of the event bus.</p>
            cross_account: <p>Support discovery of schemas in events sent to the bus from another account. (default: true).</p>
            tags: <p>Tags associated with the resource.</p>

        Raises:
            capo_schemas.errors.bad_request_exception.BadRequestException
            capo_schemas.errors.conflict_exception.ConflictException
            capo_schemas.errors.forbidden_exception.ForbiddenException
            capo_schemas.errors.internal_server_error_exception.InternalServerErrorException
            capo_schemas.errors.service_unavailable_exception.ServiceUnavailableException
            capo_schemas.errors.unauthorized_exception.UnauthorizedException
            capo_schemas.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_schemas.types.create_discoverer_request.CreateDiscovererRequest]",
        ) -> OperationResponse[
            "capo_schemas.types.create_discoverer_response.CreateDiscovererResponse"
        ]:
            import capo_schemas._operations.schemas.create_discoverer

            output, http_response = (
                capo_schemas._operations.schemas.create_discoverer.create_discoverer(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_schemas.types.create_discoverer_request.CreateDiscovererRequest = {}
        if description is not None:
            input_["description"] = description
        if source_arn is not None:
            input_["source_arn"] = source_arn
        if cross_account is not None:
            input_["cross_account"] = cross_account
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_registry(
        self,
        registry_name: "capo_schemas.types.__string.__string",
        *,
        config_overrides: Optional[schemasClientConfig] = None,
        description: Optional[
            "capo_schemas.types.__string_min0_max256.__stringMin0Max256"
        ] = None,
        tags: Optional["capo_schemas.types.tags.Tags"] = None,
    ) -> "capo_schemas.types.create_registry_response.CreateRegistryResponse":
        """<p>Creates a registry.</p>

        Args:
            description: <p>A description of the registry to be created.</p>
            registry_name: <p>The name of the registry.</p>
            tags: <p>Tags to associate with the registry.</p>

        Raises:
            capo_schemas.errors.bad_request_exception.BadRequestException
            capo_schemas.errors.conflict_exception.ConflictException
            capo_schemas.errors.forbidden_exception.ForbiddenException
            capo_schemas.errors.internal_server_error_exception.InternalServerErrorException
            capo_schemas.errors.service_unavailable_exception.ServiceUnavailableException
            capo_schemas.errors.unauthorized_exception.UnauthorizedException
            capo_schemas.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_schemas.types.create_registry_request.CreateRegistryRequest]",
        ) -> OperationResponse[
            "capo_schemas.types.create_registry_response.CreateRegistryResponse"
        ]:
            import capo_schemas._operations.schemas.create_registry

            output, http_response = (
                capo_schemas._operations.schemas.create_registry.create_registry(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_schemas.types.create_registry_request.CreateRegistryRequest = {
            "registry_name": registry_name
        }
        if description is not None:
            input_["description"] = description
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_schema(
        self,
        registry_name: "capo_schemas.types.__string.__string",
        schema_name: "capo_schemas.types.__string.__string",
        *,
        config_overrides: Optional[schemasClientConfig] = None,
        content: Optional[
            "capo_schemas.types.__string_min1_max100000.__stringMin1Max100000"
        ] = None,
        description: Optional[
            "capo_schemas.types.__string_min0_max256.__stringMin0Max256"
        ] = None,
        tags: Optional["capo_schemas.types.tags.Tags"] = None,
        type: Optional["capo_schemas.types.type.Type"] = None,
    ) -> "capo_schemas.types.create_schema_response.CreateSchemaResponse":
        """<p>Creates a schema definition.</p> <note><p>Inactive schemas will be deleted after two years.</p></note>

        Args:
            content: <p>The source of the schema definition.</p>
            description: <p>A description of the schema.</p>
            registry_name: <p>The name of the registry.</p>
            schema_name: <p>The name of the schema.</p>
            tags: <p>Tags associated with the schema.</p>
            type: <p>The type of schema.</p>

        Raises:
            capo_schemas.errors.bad_request_exception.BadRequestException
            capo_schemas.errors.forbidden_exception.ForbiddenException
            capo_schemas.errors.internal_server_error_exception.InternalServerErrorException
            capo_schemas.errors.service_unavailable_exception.ServiceUnavailableException
            capo_schemas.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_schemas.types.create_schema_request.CreateSchemaRequest]",
        ) -> OperationResponse[
            "capo_schemas.types.create_schema_response.CreateSchemaResponse"
        ]:
            import capo_schemas._operations.schemas.create_schema

            output, http_response = (
                capo_schemas._operations.schemas.create_schema.create_schema(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_schemas.types.create_schema_request.CreateSchemaRequest = {
            "registry_name": registry_name,
            "schema_name": schema_name,
        }
        if content is not None:
            input_["content"] = content
        if description is not None:
            input_["description"] = description
        if tags is not None:
            input_["tags"] = tags
        if type is not None:
            input_["type"] = type

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_discoverer(
        self,
        discoverer_id: "capo_schemas.types.__string.__string",
        *,
        config_overrides: Optional[schemasClientConfig] = None,
    ) -> None:
        """<p>Deletes a discoverer.</p>

        Args:
            discoverer_id: <p>The ID of the discoverer.</p>

        Raises:
            capo_schemas.errors.bad_request_exception.BadRequestException
            capo_schemas.errors.forbidden_exception.ForbiddenException
            capo_schemas.errors.internal_server_error_exception.InternalServerErrorException
            capo_schemas.errors.not_found_exception.NotFoundException
            capo_schemas.errors.service_unavailable_exception.ServiceUnavailableException
            capo_schemas.errors.unauthorized_exception.UnauthorizedException
            capo_schemas.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_schemas.types.delete_discoverer_request.DeleteDiscovererRequest]",
        ) -> OperationResponse[None]:
            import capo_schemas._operations.schemas.delete_discoverer

            output, http_response = (
                capo_schemas._operations.schemas.delete_discoverer.delete_discoverer(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_schemas.types.delete_discoverer_request.DeleteDiscovererRequest = {
            "discoverer_id": discoverer_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_registry(
        self,
        registry_name: "capo_schemas.types.__string.__string",
        *,
        config_overrides: Optional[schemasClientConfig] = None,
    ) -> None:
        """<p>Deletes a Registry.</p>

        Args:
            registry_name: <p>The name of the registry.</p>

        Raises:
            capo_schemas.errors.bad_request_exception.BadRequestException
            capo_schemas.errors.forbidden_exception.ForbiddenException
            capo_schemas.errors.internal_server_error_exception.InternalServerErrorException
            capo_schemas.errors.not_found_exception.NotFoundException
            capo_schemas.errors.service_unavailable_exception.ServiceUnavailableException
            capo_schemas.errors.unauthorized_exception.UnauthorizedException
            capo_schemas.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_schemas.types.delete_registry_request.DeleteRegistryRequest]",
        ) -> OperationResponse[None]:
            import capo_schemas._operations.schemas.delete_registry

            output, http_response = (
                capo_schemas._operations.schemas.delete_registry.delete_registry(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_schemas.types.delete_registry_request.DeleteRegistryRequest = {
            "registry_name": registry_name
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_resource_policy(
        self,
        *,
        config_overrides: Optional[schemasClientConfig] = None,
        registry_name: Optional["capo_schemas.types.__string.__string"] = None,
    ) -> None:
        """<p>Delete the resource-based policy attached to the specified registry.</p>

        Args:
            registry_name: <p>The name of the registry.</p>

        Raises:
            capo_schemas.errors.bad_request_exception.BadRequestException
            capo_schemas.errors.forbidden_exception.ForbiddenException
            capo_schemas.errors.internal_server_error_exception.InternalServerErrorException
            capo_schemas.errors.not_found_exception.NotFoundException
            capo_schemas.errors.service_unavailable_exception.ServiceUnavailableException
            capo_schemas.errors.unauthorized_exception.UnauthorizedException
            capo_schemas.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_schemas.types.delete_resource_policy_request.DeleteResourcePolicyRequest]",
        ) -> OperationResponse[None]:
            import capo_schemas._operations.schemas.delete_resource_policy

            output, http_response = (
                capo_schemas._operations.schemas.delete_resource_policy.delete_resource_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_schemas.types.delete_resource_policy_request.DeleteResourcePolicyRequest = {}
        if registry_name is not None:
            input_["registry_name"] = registry_name

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_schema(
        self,
        registry_name: "capo_schemas.types.__string.__string",
        schema_name: "capo_schemas.types.__string.__string",
        *,
        config_overrides: Optional[schemasClientConfig] = None,
    ) -> None:
        """<p>Delete a schema definition.</p>

        Args:
            registry_name: <p>The name of the registry.</p>
            schema_name: <p>The name of the schema.</p>

        Raises:
            capo_schemas.errors.bad_request_exception.BadRequestException
            capo_schemas.errors.forbidden_exception.ForbiddenException
            capo_schemas.errors.internal_server_error_exception.InternalServerErrorException
            capo_schemas.errors.not_found_exception.NotFoundException
            capo_schemas.errors.service_unavailable_exception.ServiceUnavailableException
            capo_schemas.errors.unauthorized_exception.UnauthorizedException
            capo_schemas.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_schemas.types.delete_schema_request.DeleteSchemaRequest]",
        ) -> OperationResponse[None]:
            import capo_schemas._operations.schemas.delete_schema

            output, http_response = (
                capo_schemas._operations.schemas.delete_schema.delete_schema(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_schemas.types.delete_schema_request.DeleteSchemaRequest = {
            "registry_name": registry_name,
            "schema_name": schema_name,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_schema_version(
        self,
        registry_name: "capo_schemas.types.__string.__string",
        schema_name: "capo_schemas.types.__string.__string",
        schema_version: "capo_schemas.types.__string.__string",
        *,
        config_overrides: Optional[schemasClientConfig] = None,
    ) -> None:
        """<p>Delete the schema version definition</p>

        Args:
            registry_name: <p>The name of the registry.</p>
            schema_name: <p>The name of the schema.</p>
            schema_version: The version number of the schema

        Raises:
            capo_schemas.errors.bad_request_exception.BadRequestException
            capo_schemas.errors.forbidden_exception.ForbiddenException
            capo_schemas.errors.internal_server_error_exception.InternalServerErrorException
            capo_schemas.errors.not_found_exception.NotFoundException
            capo_schemas.errors.service_unavailable_exception.ServiceUnavailableException
            capo_schemas.errors.unauthorized_exception.UnauthorizedException
            capo_schemas.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_schemas.types.delete_schema_version_request.DeleteSchemaVersionRequest]",
        ) -> OperationResponse[None]:
            import capo_schemas._operations.schemas.delete_schema_version

            output, http_response = (
                capo_schemas._operations.schemas.delete_schema_version.delete_schema_version(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_schemas.types.delete_schema_version_request.DeleteSchemaVersionRequest = {
            "registry_name": registry_name,
            "schema_name": schema_name,
            "schema_version": schema_version,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_code_binding(
        self,
        language: "capo_schemas.types.__string.__string",
        registry_name: "capo_schemas.types.__string.__string",
        schema_name: "capo_schemas.types.__string.__string",
        *,
        config_overrides: Optional[schemasClientConfig] = None,
        schema_version: Optional["capo_schemas.types.__string.__string"] = None,
    ) -> (
        "capo_schemas.types.describe_code_binding_response.DescribeCodeBindingResponse"
    ):
        """<p>Describe the code binding URI.</p>

        Args:
            language: <p>The language of the code binding.</p>
            registry_name: <p>The name of the registry.</p>
            schema_name: <p>The name of the schema.</p>
            schema_version: <p>Specifying this limits the results to only this schema version.</p>

        Raises:
            capo_schemas.errors.bad_request_exception.BadRequestException
            capo_schemas.errors.forbidden_exception.ForbiddenException
            capo_schemas.errors.internal_server_error_exception.InternalServerErrorException
            capo_schemas.errors.not_found_exception.NotFoundException
            capo_schemas.errors.too_many_requests_exception.TooManyRequestsException
            capo_schemas.errors.unauthorized_exception.UnauthorizedException
            capo_schemas.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_schemas.types.describe_code_binding_request.DescribeCodeBindingRequest]",
        ) -> OperationResponse[
            "capo_schemas.types.describe_code_binding_response.DescribeCodeBindingResponse"
        ]:
            import capo_schemas._operations.schemas.describe_code_binding

            output, http_response = (
                capo_schemas._operations.schemas.describe_code_binding.describe_code_binding(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_schemas.types.describe_code_binding_request.DescribeCodeBindingRequest = {
            "language": language,
            "registry_name": registry_name,
            "schema_name": schema_name,
        }
        if schema_version is not None:
            input_["schema_version"] = schema_version

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_discoverer(
        self,
        discoverer_id: "capo_schemas.types.__string.__string",
        *,
        config_overrides: Optional[schemasClientConfig] = None,
    ) -> "capo_schemas.types.describe_discoverer_response.DescribeDiscovererResponse":
        """<p>Describes the discoverer.</p>

        Args:
            discoverer_id: <p>The ID of the discoverer.</p>

        Raises:
            capo_schemas.errors.bad_request_exception.BadRequestException
            capo_schemas.errors.forbidden_exception.ForbiddenException
            capo_schemas.errors.internal_server_error_exception.InternalServerErrorException
            capo_schemas.errors.not_found_exception.NotFoundException
            capo_schemas.errors.service_unavailable_exception.ServiceUnavailableException
            capo_schemas.errors.unauthorized_exception.UnauthorizedException
            capo_schemas.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_schemas.types.describe_discoverer_request.DescribeDiscovererRequest]",
        ) -> OperationResponse[
            "capo_schemas.types.describe_discoverer_response.DescribeDiscovererResponse"
        ]:
            import capo_schemas._operations.schemas.describe_discoverer

            output, http_response = (
                capo_schemas._operations.schemas.describe_discoverer.describe_discoverer(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_schemas.types.describe_discoverer_request.DescribeDiscovererRequest = {
            "discoverer_id": discoverer_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_registry(
        self,
        registry_name: "capo_schemas.types.__string.__string",
        *,
        config_overrides: Optional[schemasClientConfig] = None,
    ) -> "capo_schemas.types.describe_registry_response.DescribeRegistryResponse":
        """<p>Describes the registry.</p>

        Args:
            registry_name: <p>The name of the registry.</p>

        Raises:
            capo_schemas.errors.bad_request_exception.BadRequestException
            capo_schemas.errors.forbidden_exception.ForbiddenException
            capo_schemas.errors.internal_server_error_exception.InternalServerErrorException
            capo_schemas.errors.not_found_exception.NotFoundException
            capo_schemas.errors.service_unavailable_exception.ServiceUnavailableException
            capo_schemas.errors.unauthorized_exception.UnauthorizedException
            capo_schemas.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_schemas.types.describe_registry_request.DescribeRegistryRequest]",
        ) -> OperationResponse[
            "capo_schemas.types.describe_registry_response.DescribeRegistryResponse"
        ]:
            import capo_schemas._operations.schemas.describe_registry

            output, http_response = (
                capo_schemas._operations.schemas.describe_registry.describe_registry(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_schemas.types.describe_registry_request.DescribeRegistryRequest = {
            "registry_name": registry_name
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_schema(
        self,
        registry_name: "capo_schemas.types.__string.__string",
        schema_name: "capo_schemas.types.__string.__string",
        *,
        config_overrides: Optional[schemasClientConfig] = None,
        schema_version: Optional["capo_schemas.types.__string.__string"] = None,
    ) -> "capo_schemas.types.describe_schema_response.DescribeSchemaResponse":
        """<p>Retrieve the schema definition.</p>

        Args:
            registry_name: <p>The name of the registry.</p>
            schema_name: <p>The name of the schema.</p>
            schema_version: <p>Specifying this limits the results to only this schema version.</p>

        Raises:
            capo_schemas.errors.bad_request_exception.BadRequestException
            capo_schemas.errors.forbidden_exception.ForbiddenException
            capo_schemas.errors.internal_server_error_exception.InternalServerErrorException
            capo_schemas.errors.not_found_exception.NotFoundException
            capo_schemas.errors.service_unavailable_exception.ServiceUnavailableException
            capo_schemas.errors.unauthorized_exception.UnauthorizedException
            capo_schemas.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_schemas.types.describe_schema_request.DescribeSchemaRequest]",
        ) -> OperationResponse[
            "capo_schemas.types.describe_schema_response.DescribeSchemaResponse"
        ]:
            import capo_schemas._operations.schemas.describe_schema

            output, http_response = (
                capo_schemas._operations.schemas.describe_schema.describe_schema(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_schemas.types.describe_schema_request.DescribeSchemaRequest = {
            "registry_name": registry_name,
            "schema_name": schema_name,
        }
        if schema_version is not None:
            input_["schema_version"] = schema_version

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def export_schema(
        self,
        registry_name: "capo_schemas.types.__string.__string",
        schema_name: "capo_schemas.types.__string.__string",
        *,
        config_overrides: Optional[schemasClientConfig] = None,
        schema_version: Optional["capo_schemas.types.__string.__string"] = None,
        type: Optional["capo_schemas.types.__string.__string"] = None,
    ) -> "capo_schemas.types.export_schema_response.ExportSchemaResponse":
        """export_schema

        Args:
            registry_name: <p>The name of the registry.</p>
            schema_name: <p>The name of the schema.</p>
            schema_version: <p>Specifying this limits the results to only this schema version.</p>

        Raises:
            capo_schemas.errors.bad_request_exception.BadRequestException
            capo_schemas.errors.forbidden_exception.ForbiddenException
            capo_schemas.errors.internal_server_error_exception.InternalServerErrorException
            capo_schemas.errors.not_found_exception.NotFoundException
            capo_schemas.errors.service_unavailable_exception.ServiceUnavailableException
            capo_schemas.errors.too_many_requests_exception.TooManyRequestsException
            capo_schemas.errors.unauthorized_exception.UnauthorizedException
            capo_schemas.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_schemas.types.export_schema_request.ExportSchemaRequest]",
        ) -> OperationResponse[
            "capo_schemas.types.export_schema_response.ExportSchemaResponse"
        ]:
            import capo_schemas._operations.schemas.export_schema

            output, http_response = (
                capo_schemas._operations.schemas.export_schema.export_schema(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_schemas.types.export_schema_request.ExportSchemaRequest = {
            "registry_name": registry_name,
            "schema_name": schema_name,
        }
        if schema_version is not None:
            input_["schema_version"] = schema_version
        if type is not None:
            input_["type"] = type

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_code_binding_source(
        self,
        language: "capo_schemas.types.__string.__string",
        registry_name: "capo_schemas.types.__string.__string",
        schema_name: "capo_schemas.types.__string.__string",
        *,
        config_overrides: Optional[schemasClientConfig] = None,
        schema_version: Optional["capo_schemas.types.__string.__string"] = None,
    ) -> "capo_schemas.types.get_code_binding_source_response.GetCodeBindingSourceResponse":
        """<p>Get the code binding source URI.</p>

        Args:
            language: <p>The language of the code binding.</p>
            registry_name: <p>The name of the registry.</p>
            schema_name: <p>The name of the schema.</p>
            schema_version: <p>Specifying this limits the results to only this schema version.</p>

        Raises:
            capo_schemas.errors.bad_request_exception.BadRequestException
            capo_schemas.errors.forbidden_exception.ForbiddenException
            capo_schemas.errors.internal_server_error_exception.InternalServerErrorException
            capo_schemas.errors.not_found_exception.NotFoundException
            capo_schemas.errors.too_many_requests_exception.TooManyRequestsException
            capo_schemas.errors.unauthorized_exception.UnauthorizedException
            capo_schemas.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_schemas.types.get_code_binding_source_request.GetCodeBindingSourceRequest]",
        ) -> OperationResponse[
            "capo_schemas.types.get_code_binding_source_response.GetCodeBindingSourceResponse"
        ]:
            import capo_schemas._operations.schemas.get_code_binding_source

            output, http_response = (
                capo_schemas._operations.schemas.get_code_binding_source.get_code_binding_source(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_schemas.types.get_code_binding_source_request.GetCodeBindingSourceRequest = {
            "language": language,
            "registry_name": registry_name,
            "schema_name": schema_name,
        }
        if schema_version is not None:
            input_["schema_version"] = schema_version

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_discovered_schema(
        self,
        *,
        config_overrides: Optional[schemasClientConfig] = None,
        events: Optional[
            "capo_schemas.types.__list_of_get_discovered_schema_version_item_input.__listOfGetDiscoveredSchemaVersionItemInput"
        ] = None,
        type: Optional["capo_schemas.types.type.Type"] = None,
    ) -> (
        "capo_schemas.types.get_discovered_schema_response.GetDiscoveredSchemaResponse"
    ):
        """<p>Get the discovered schema that was generated based on sampled events.</p>

        Args:
            events: <p>An array of strings where each string is a JSON event. These are the events that were used to generate the schema. The array includes a single type of event and has a maximum size of 10 events.</p>
            type: <p>The type of event.</p>

        Raises:
            capo_schemas.errors.bad_request_exception.BadRequestException
            capo_schemas.errors.forbidden_exception.ForbiddenException
            capo_schemas.errors.internal_server_error_exception.InternalServerErrorException
            capo_schemas.errors.service_unavailable_exception.ServiceUnavailableException
            capo_schemas.errors.unauthorized_exception.UnauthorizedException
            capo_schemas.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_schemas.types.get_discovered_schema_request.GetDiscoveredSchemaRequest]",
        ) -> OperationResponse[
            "capo_schemas.types.get_discovered_schema_response.GetDiscoveredSchemaResponse"
        ]:
            import capo_schemas._operations.schemas.get_discovered_schema

            output, http_response = (
                capo_schemas._operations.schemas.get_discovered_schema.get_discovered_schema(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_schemas.types.get_discovered_schema_request.GetDiscoveredSchemaRequest = {}
        if events is not None:
            input_["events"] = events
        if type is not None:
            input_["type"] = type

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_resource_policy(
        self,
        *,
        config_overrides: Optional[schemasClientConfig] = None,
        registry_name: Optional["capo_schemas.types.__string.__string"] = None,
    ) -> "capo_schemas.types.get_resource_policy_response.GetResourcePolicyResponse":
        """<p>Retrieves the resource-based policy attached to a given registry.</p>

        Args:
            registry_name: <p>The name of the registry.</p>

        Raises:
            capo_schemas.errors.bad_request_exception.BadRequestException
            capo_schemas.errors.forbidden_exception.ForbiddenException
            capo_schemas.errors.internal_server_error_exception.InternalServerErrorException
            capo_schemas.errors.not_found_exception.NotFoundException
            capo_schemas.errors.service_unavailable_exception.ServiceUnavailableException
            capo_schemas.errors.unauthorized_exception.UnauthorizedException
            capo_schemas.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_schemas.types.get_resource_policy_request.GetResourcePolicyRequest]",
        ) -> OperationResponse[
            "capo_schemas.types.get_resource_policy_response.GetResourcePolicyResponse"
        ]:
            import capo_schemas._operations.schemas.get_resource_policy

            output, http_response = (
                capo_schemas._operations.schemas.get_resource_policy.get_resource_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_schemas.types.get_resource_policy_request.GetResourcePolicyRequest = {}
        if registry_name is not None:
            input_["registry_name"] = registry_name

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_discoverers(
        self,
        *,
        config_overrides: Optional[schemasClientConfig] = None,
        discoverer_id_prefix: Optional["capo_schemas.types.__string.__string"] = None,
        limit: Optional["capo_schemas.types.__integer.__integer"] = None,
        next_token: Optional["capo_schemas.types.__string.__string"] = None,
        source_arn_prefix: Optional["capo_schemas.types.__string.__string"] = None,
    ) -> "capo_schemas.types.list_discoverers_response.ListDiscoverersResponse":
        """<p>List the discoverers.</p>

        Args:
            discoverer_id_prefix: <p>Specifying this limits the results to only those discoverer IDs that start with the specified prefix.</p>
            next_token: <p>The token that specifies the next page of results to return. To request the first page, leave NextToken empty. The token will expire in 24 hours, and cannot be shared with other accounts.</p>
            source_arn_prefix: <p>Specifying this limits the results to only those ARNs that start with the specified prefix.</p>

        Raises:
            capo_schemas.errors.bad_request_exception.BadRequestException
            capo_schemas.errors.forbidden_exception.ForbiddenException
            capo_schemas.errors.internal_server_error_exception.InternalServerErrorException
            capo_schemas.errors.service_unavailable_exception.ServiceUnavailableException
            capo_schemas.errors.unauthorized_exception.UnauthorizedException
            capo_schemas.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_schemas.types.list_discoverers_request.ListDiscoverersRequest]",
        ) -> OperationResponse[
            "capo_schemas.types.list_discoverers_response.ListDiscoverersResponse"
        ]:
            import capo_schemas._operations.schemas.list_discoverers

            output, http_response = (
                capo_schemas._operations.schemas.list_discoverers.list_discoverers(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_schemas.types.list_discoverers_request.ListDiscoverersRequest = {}
        if discoverer_id_prefix is not None:
            input_["discoverer_id_prefix"] = discoverer_id_prefix
        if limit is not None:
            input_["limit"] = limit
        if next_token is not None:
            input_["next_token"] = next_token
        if source_arn_prefix is not None:
            input_["source_arn_prefix"] = source_arn_prefix

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_discoverers(
        self,
        *,
        config_overrides: Optional[schemasClientConfig] = None,
        discoverer_id_prefix: Optional["capo_schemas.types.__string.__string"] = None,
        limit: Optional["capo_schemas.types.__integer.__integer"] = None,
        next_token: Optional["capo_schemas.types.__string.__string"] = None,
        source_arn_prefix: Optional["capo_schemas.types.__string.__string"] = None,
    ) -> "Iterator[capo_schemas.types.discoverer_summary.DiscovererSummary]":
        _token = next_token
        while True:
            _response = self.list_discoverers(
                config_overrides=config_overrides,
                discoverer_id_prefix=discoverer_id_prefix,
                limit=limit,
                next_token=_token,
                source_arn_prefix=source_arn_prefix,
            )
            _page = _resolve_path(_response, ("discoverers",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_registries(
        self,
        *,
        config_overrides: Optional[schemasClientConfig] = None,
        limit: Optional["capo_schemas.types.__integer.__integer"] = None,
        next_token: Optional["capo_schemas.types.__string.__string"] = None,
        registry_name_prefix: Optional["capo_schemas.types.__string.__string"] = None,
        scope: Optional["capo_schemas.types.__string.__string"] = None,
    ) -> "capo_schemas.types.list_registries_response.ListRegistriesResponse":
        """<p>List the registries.</p>

        Args:
            next_token: <p>The token that specifies the next page of results to return. To request the first page, leave NextToken empty. The token will expire in 24 hours, and cannot be shared with other accounts.</p>
            registry_name_prefix: <p>Specifying this limits the results to only those registry names that start with the specified prefix.</p>
            scope: <p>Can be set to Local or AWS to limit responses to your custom registries, or the ones provided by AWS.</p>

        Raises:
            capo_schemas.errors.bad_request_exception.BadRequestException
            capo_schemas.errors.forbidden_exception.ForbiddenException
            capo_schemas.errors.internal_server_error_exception.InternalServerErrorException
            capo_schemas.errors.service_unavailable_exception.ServiceUnavailableException
            capo_schemas.errors.unauthorized_exception.UnauthorizedException
            capo_schemas.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_schemas.types.list_registries_request.ListRegistriesRequest]",
        ) -> OperationResponse[
            "capo_schemas.types.list_registries_response.ListRegistriesResponse"
        ]:
            import capo_schemas._operations.schemas.list_registries

            output, http_response = (
                capo_schemas._operations.schemas.list_registries.list_registries(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_schemas.types.list_registries_request.ListRegistriesRequest = {}
        if limit is not None:
            input_["limit"] = limit
        if next_token is not None:
            input_["next_token"] = next_token
        if registry_name_prefix is not None:
            input_["registry_name_prefix"] = registry_name_prefix
        if scope is not None:
            input_["scope"] = scope

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
        config_overrides: Optional[schemasClientConfig] = None,
        limit: Optional["capo_schemas.types.__integer.__integer"] = None,
        next_token: Optional["capo_schemas.types.__string.__string"] = None,
        registry_name_prefix: Optional["capo_schemas.types.__string.__string"] = None,
        scope: Optional["capo_schemas.types.__string.__string"] = None,
    ) -> "Iterator[capo_schemas.types.registry_summary.RegistrySummary]":
        _token = next_token
        while True:
            _response = self.list_registries(
                config_overrides=config_overrides,
                limit=limit,
                next_token=_token,
                registry_name_prefix=registry_name_prefix,
                scope=scope,
            )
            _page = _resolve_path(_response, ("registries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_schemas(
        self,
        registry_name: "capo_schemas.types.__string.__string",
        *,
        config_overrides: Optional[schemasClientConfig] = None,
        limit: Optional["capo_schemas.types.__integer.__integer"] = None,
        next_token: Optional["capo_schemas.types.__string.__string"] = None,
        schema_name_prefix: Optional["capo_schemas.types.__string.__string"] = None,
    ) -> "capo_schemas.types.list_schemas_response.ListSchemasResponse":
        """<p>List the schemas.</p>

        Args:
            next_token: <p>The token that specifies the next page of results to return. To request the first page, leave NextToken empty. The token will expire in 24 hours, and cannot be shared with other accounts.</p>
            registry_name: <p>The name of the registry.</p>
            schema_name_prefix: <p>Specifying this limits the results to only those schema names that start with the specified prefix.</p>

        Raises:
            capo_schemas.errors.bad_request_exception.BadRequestException
            capo_schemas.errors.forbidden_exception.ForbiddenException
            capo_schemas.errors.internal_server_error_exception.InternalServerErrorException
            capo_schemas.errors.service_unavailable_exception.ServiceUnavailableException
            capo_schemas.errors.unauthorized_exception.UnauthorizedException
            capo_schemas.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_schemas.types.list_schemas_request.ListSchemasRequest]",
        ) -> OperationResponse[
            "capo_schemas.types.list_schemas_response.ListSchemasResponse"
        ]:
            import capo_schemas._operations.schemas.list_schemas

            output, http_response = (
                capo_schemas._operations.schemas.list_schemas.list_schemas(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_schemas.types.list_schemas_request.ListSchemasRequest = {
            "registry_name": registry_name
        }
        if limit is not None:
            input_["limit"] = limit
        if next_token is not None:
            input_["next_token"] = next_token
        if schema_name_prefix is not None:
            input_["schema_name_prefix"] = schema_name_prefix

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_schemas(
        self,
        registry_name: "capo_schemas.types.__string.__string",
        *,
        config_overrides: Optional[schemasClientConfig] = None,
        limit: Optional["capo_schemas.types.__integer.__integer"] = None,
        next_token: Optional["capo_schemas.types.__string.__string"] = None,
        schema_name_prefix: Optional["capo_schemas.types.__string.__string"] = None,
    ) -> "Iterator[capo_schemas.types.schema_summary.SchemaSummary]":
        _token = next_token
        while True:
            _response = self.list_schemas(
                registry_name,
                config_overrides=config_overrides,
                limit=limit,
                next_token=_token,
                schema_name_prefix=schema_name_prefix,
            )
            _page = _resolve_path(_response, ("schemas",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_schema_versions(
        self,
        registry_name: "capo_schemas.types.__string.__string",
        schema_name: "capo_schemas.types.__string.__string",
        *,
        config_overrides: Optional[schemasClientConfig] = None,
        limit: Optional["capo_schemas.types.__integer.__integer"] = None,
        next_token: Optional["capo_schemas.types.__string.__string"] = None,
    ) -> "capo_schemas.types.list_schema_versions_response.ListSchemaVersionsResponse":
        """<p>Provides a list of the schema versions and related information.</p>

        Args:
            next_token: <p>The token that specifies the next page of results to return. To request the first page, leave NextToken empty. The token will expire in 24 hours, and cannot be shared with other accounts.</p>
            registry_name: <p>The name of the registry.</p>
            schema_name: <p>The name of the schema.</p>

        Raises:
            capo_schemas.errors.bad_request_exception.BadRequestException
            capo_schemas.errors.forbidden_exception.ForbiddenException
            capo_schemas.errors.internal_server_error_exception.InternalServerErrorException
            capo_schemas.errors.not_found_exception.NotFoundException
            capo_schemas.errors.service_unavailable_exception.ServiceUnavailableException
            capo_schemas.errors.unauthorized_exception.UnauthorizedException
            capo_schemas.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_schemas.types.list_schema_versions_request.ListSchemaVersionsRequest]",
        ) -> OperationResponse[
            "capo_schemas.types.list_schema_versions_response.ListSchemaVersionsResponse"
        ]:
            import capo_schemas._operations.schemas.list_schema_versions

            output, http_response = (
                capo_schemas._operations.schemas.list_schema_versions.list_schema_versions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_schemas.types.list_schema_versions_request.ListSchemaVersionsRequest = {
            "registry_name": registry_name,
            "schema_name": schema_name,
        }
        if limit is not None:
            input_["limit"] = limit
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_schema_versions(
        self,
        registry_name: "capo_schemas.types.__string.__string",
        schema_name: "capo_schemas.types.__string.__string",
        *,
        config_overrides: Optional[schemasClientConfig] = None,
        limit: Optional["capo_schemas.types.__integer.__integer"] = None,
        next_token: Optional["capo_schemas.types.__string.__string"] = None,
    ) -> "Iterator[capo_schemas.types.schema_version_summary.SchemaVersionSummary]":
        _token = next_token
        while True:
            _response = self.list_schema_versions(
                registry_name,
                schema_name,
                config_overrides=config_overrides,
                limit=limit,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("schema_versions",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_tags_for_resource(
        self,
        resource_arn: "capo_schemas.types.__string.__string",
        *,
        config_overrides: Optional[schemasClientConfig] = None,
    ) -> (
        "capo_schemas.types.list_tags_for_resource_response.ListTagsForResourceResponse"
    ):
        """<p>Get tags for resource.</p>

        Args:
            resource_arn: <p>The ARN of the resource.</p>

        Raises:
            capo_schemas.errors.bad_request_exception.BadRequestException
            capo_schemas.errors.forbidden_exception.ForbiddenException
            capo_schemas.errors.internal_server_error_exception.InternalServerErrorException
            capo_schemas.errors.not_found_exception.NotFoundException
            capo_schemas.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_schemas.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> OperationResponse[
            "capo_schemas.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import capo_schemas._operations.schemas.list_tags_for_resource

            output, http_response = (
                capo_schemas._operations.schemas.list_tags_for_resource.list_tags_for_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_schemas.types.list_tags_for_resource_request.ListTagsForResourceRequest = {
            "resource_arn": resource_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def put_code_binding(
        self,
        language: "capo_schemas.types.__string.__string",
        registry_name: "capo_schemas.types.__string.__string",
        schema_name: "capo_schemas.types.__string.__string",
        *,
        config_overrides: Optional[schemasClientConfig] = None,
        schema_version: Optional["capo_schemas.types.__string.__string"] = None,
    ) -> "capo_schemas.types.put_code_binding_response.PutCodeBindingResponse":
        """<p>Put code binding URI</p>

        Args:
            language: <p>The language of the code binding.</p>
            registry_name: <p>The name of the registry.</p>
            schema_name: <p>The name of the schema.</p>
            schema_version: <p>Specifying this limits the results to only this schema version.</p>

        Raises:
            capo_schemas.errors.bad_request_exception.BadRequestException
            capo_schemas.errors.forbidden_exception.ForbiddenException
            capo_schemas.errors.gone_exception.GoneException
            capo_schemas.errors.internal_server_error_exception.InternalServerErrorException
            capo_schemas.errors.not_found_exception.NotFoundException
            capo_schemas.errors.too_many_requests_exception.TooManyRequestsException
            capo_schemas.errors.unauthorized_exception.UnauthorizedException
            capo_schemas.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_schemas.types.put_code_binding_request.PutCodeBindingRequest]",
        ) -> OperationResponse[
            "capo_schemas.types.put_code_binding_response.PutCodeBindingResponse"
        ]:
            import capo_schemas._operations.schemas.put_code_binding

            output, http_response = (
                capo_schemas._operations.schemas.put_code_binding.put_code_binding(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_schemas.types.put_code_binding_request.PutCodeBindingRequest = {
            "language": language,
            "registry_name": registry_name,
            "schema_name": schema_name,
        }
        if schema_version is not None:
            input_["schema_version"] = schema_version

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def put_resource_policy(
        self,
        *,
        config_overrides: Optional[schemasClientConfig] = None,
        policy: Optional[
            "capo_schemas.types.synthesized_json__string.SynthesizedJson__string"
        ] = None,
        registry_name: Optional["capo_schemas.types.__string.__string"] = None,
        revision_id: Optional["capo_schemas.types.__string.__string"] = None,
    ) -> "capo_schemas.types.put_resource_policy_response.PutResourcePolicyResponse":
        """<p>The name of the policy.</p>

        Args:
            policy: <p>The resource-based policy.</p>
            registry_name: <p>The name of the registry.</p>
            revision_id: <p>The revision ID of the policy.</p>

        Raises:
            capo_schemas.errors.bad_request_exception.BadRequestException
            capo_schemas.errors.forbidden_exception.ForbiddenException
            capo_schemas.errors.internal_server_error_exception.InternalServerErrorException
            capo_schemas.errors.not_found_exception.NotFoundException
            capo_schemas.errors.precondition_failed_exception.PreconditionFailedException
            capo_schemas.errors.service_unavailable_exception.ServiceUnavailableException
            capo_schemas.errors.unauthorized_exception.UnauthorizedException
            capo_schemas.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_schemas.types.put_resource_policy_request.PutResourcePolicyRequest]",
        ) -> OperationResponse[
            "capo_schemas.types.put_resource_policy_response.PutResourcePolicyResponse"
        ]:
            import capo_schemas._operations.schemas.put_resource_policy

            output, http_response = (
                capo_schemas._operations.schemas.put_resource_policy.put_resource_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_schemas.types.put_resource_policy_request.PutResourcePolicyRequest = {}
        if policy is not None:
            input_["policy"] = policy
        if registry_name is not None:
            input_["registry_name"] = registry_name
        if revision_id is not None:
            input_["revision_id"] = revision_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def search_schemas(
        self,
        registry_name: "capo_schemas.types.__string.__string",
        *,
        config_overrides: Optional[schemasClientConfig] = None,
        keywords: Optional["capo_schemas.types.__string.__string"] = None,
        limit: Optional["capo_schemas.types.__integer.__integer"] = None,
        next_token: Optional["capo_schemas.types.__string.__string"] = None,
    ) -> "capo_schemas.types.search_schemas_response.SearchSchemasResponse":
        """<p>Search the schemas</p>

        Args:
            keywords: <p>Specifying this limits the results to only schemas that include the provided keywords.</p>
            next_token: <p>The token that specifies the next page of results to return. To request the first page, leave NextToken empty. The token will expire in 24 hours, and cannot be shared with other accounts.</p>
            registry_name: <p>The name of the registry.</p>

        Raises:
            capo_schemas.errors.bad_request_exception.BadRequestException
            capo_schemas.errors.forbidden_exception.ForbiddenException
            capo_schemas.errors.internal_server_error_exception.InternalServerErrorException
            capo_schemas.errors.service_unavailable_exception.ServiceUnavailableException
            capo_schemas.errors.unauthorized_exception.UnauthorizedException
            capo_schemas.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_schemas.types.search_schemas_request.SearchSchemasRequest]",
        ) -> OperationResponse[
            "capo_schemas.types.search_schemas_response.SearchSchemasResponse"
        ]:
            import capo_schemas._operations.schemas.search_schemas

            output, http_response = (
                capo_schemas._operations.schemas.search_schemas.search_schemas(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_schemas.types.search_schemas_request.SearchSchemasRequest = {
            "registry_name": registry_name
        }
        if keywords is not None:
            input_["keywords"] = keywords
        if limit is not None:
            input_["limit"] = limit
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_search_schemas(
        self,
        registry_name: "capo_schemas.types.__string.__string",
        *,
        config_overrides: Optional[schemasClientConfig] = None,
        keywords: Optional["capo_schemas.types.__string.__string"] = None,
        limit: Optional["capo_schemas.types.__integer.__integer"] = None,
        next_token: Optional["capo_schemas.types.__string.__string"] = None,
    ) -> "Iterator[capo_schemas.types.search_schema_summary.SearchSchemaSummary]":
        _token = next_token
        while True:
            _response = self.search_schemas(
                registry_name,
                config_overrides=config_overrides,
                keywords=keywords,
                limit=limit,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("schemas",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def start_discoverer(
        self,
        discoverer_id: "capo_schemas.types.__string.__string",
        *,
        config_overrides: Optional[schemasClientConfig] = None,
    ) -> "capo_schemas.types.start_discoverer_response.StartDiscovererResponse":
        """<p>Starts the discoverer</p>

        Args:
            discoverer_id: <p>The ID of the discoverer.</p>

        Raises:
            capo_schemas.errors.bad_request_exception.BadRequestException
            capo_schemas.errors.forbidden_exception.ForbiddenException
            capo_schemas.errors.internal_server_error_exception.InternalServerErrorException
            capo_schemas.errors.not_found_exception.NotFoundException
            capo_schemas.errors.service_unavailable_exception.ServiceUnavailableException
            capo_schemas.errors.unauthorized_exception.UnauthorizedException
            capo_schemas.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_schemas.types.start_discoverer_request.StartDiscovererRequest]",
        ) -> OperationResponse[
            "capo_schemas.types.start_discoverer_response.StartDiscovererResponse"
        ]:
            import capo_schemas._operations.schemas.start_discoverer

            output, http_response = (
                capo_schemas._operations.schemas.start_discoverer.start_discoverer(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_schemas.types.start_discoverer_request.StartDiscovererRequest = {
            "discoverer_id": discoverer_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def stop_discoverer(
        self,
        discoverer_id: "capo_schemas.types.__string.__string",
        *,
        config_overrides: Optional[schemasClientConfig] = None,
    ) -> "capo_schemas.types.stop_discoverer_response.StopDiscovererResponse":
        """<p>Stops the discoverer</p>

        Args:
            discoverer_id: <p>The ID of the discoverer.</p>

        Raises:
            capo_schemas.errors.bad_request_exception.BadRequestException
            capo_schemas.errors.forbidden_exception.ForbiddenException
            capo_schemas.errors.internal_server_error_exception.InternalServerErrorException
            capo_schemas.errors.not_found_exception.NotFoundException
            capo_schemas.errors.service_unavailable_exception.ServiceUnavailableException
            capo_schemas.errors.unauthorized_exception.UnauthorizedException
            capo_schemas.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_schemas.types.stop_discoverer_request.StopDiscovererRequest]",
        ) -> OperationResponse[
            "capo_schemas.types.stop_discoverer_response.StopDiscovererResponse"
        ]:
            import capo_schemas._operations.schemas.stop_discoverer

            output, http_response = (
                capo_schemas._operations.schemas.stop_discoverer.stop_discoverer(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_schemas.types.stop_discoverer_request.StopDiscovererRequest = {
            "discoverer_id": discoverer_id
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
        resource_arn: "capo_schemas.types.__string.__string",
        *,
        config_overrides: Optional[schemasClientConfig] = None,
        tags: Optional["capo_schemas.types.tags.Tags"] = None,
    ) -> None:
        """<p>Add tags to a resource.</p>

        Args:
            resource_arn: <p>The ARN of the resource.</p>
            tags: <p>Tags associated with the resource.</p>

        Raises:
            capo_schemas.errors.bad_request_exception.BadRequestException
            capo_schemas.errors.forbidden_exception.ForbiddenException
            capo_schemas.errors.internal_server_error_exception.InternalServerErrorException
            capo_schemas.errors.not_found_exception.NotFoundException
            capo_schemas.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_schemas.types.tag_resource_request.TagResourceRequest]",
        ) -> OperationResponse[None]:
            import capo_schemas._operations.schemas.tag_resource

            output, http_response = (
                capo_schemas._operations.schemas.tag_resource.tag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_schemas.types.tag_resource_request.TagResourceRequest = {
            "resource_arn": resource_arn
        }
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def untag_resource(
        self,
        resource_arn: "capo_schemas.types.__string.__string",
        *,
        config_overrides: Optional[schemasClientConfig] = None,
        tag_keys: Optional[
            "capo_schemas.types.__list_of__string.__listOf__string"
        ] = None,
    ) -> None:
        """<p>Removes tags from a resource.</p>

        Args:
            resource_arn: <p>The ARN of the resource.</p>
            tag_keys: <p>Keys of key-value pairs.</p>

        Raises:
            capo_schemas.errors.bad_request_exception.BadRequestException
            capo_schemas.errors.forbidden_exception.ForbiddenException
            capo_schemas.errors.internal_server_error_exception.InternalServerErrorException
            capo_schemas.errors.not_found_exception.NotFoundException
            capo_schemas.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_schemas.types.untag_resource_request.UntagResourceRequest]",
        ) -> OperationResponse[None]:
            import capo_schemas._operations.schemas.untag_resource

            output, http_response = (
                capo_schemas._operations.schemas.untag_resource.untag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_schemas.types.untag_resource_request.UntagResourceRequest = {
            "resource_arn": resource_arn
        }
        if tag_keys is not None:
            input_["tag_keys"] = tag_keys

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_discoverer(
        self,
        discoverer_id: "capo_schemas.types.__string.__string",
        *,
        config_overrides: Optional[schemasClientConfig] = None,
        description: Optional[
            "capo_schemas.types.__string_min0_max256.__stringMin0Max256"
        ] = None,
        cross_account: Optional["capo_schemas.types.__boolean.__boolean"] = None,
    ) -> "capo_schemas.types.update_discoverer_response.UpdateDiscovererResponse":
        """<p>Updates the discoverer</p>

        Args:
            description: <p>The description of the discoverer to update.</p>
            discoverer_id: <p>The ID of the discoverer.</p>
            cross_account: <p>Support discovery of schemas in events sent to the bus from another account. (default: true)</p>

        Raises:
            capo_schemas.errors.bad_request_exception.BadRequestException
            capo_schemas.errors.forbidden_exception.ForbiddenException
            capo_schemas.errors.internal_server_error_exception.InternalServerErrorException
            capo_schemas.errors.not_found_exception.NotFoundException
            capo_schemas.errors.service_unavailable_exception.ServiceUnavailableException
            capo_schemas.errors.unauthorized_exception.UnauthorizedException
            capo_schemas.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_schemas.types.update_discoverer_request.UpdateDiscovererRequest]",
        ) -> OperationResponse[
            "capo_schemas.types.update_discoverer_response.UpdateDiscovererResponse"
        ]:
            import capo_schemas._operations.schemas.update_discoverer

            output, http_response = (
                capo_schemas._operations.schemas.update_discoverer.update_discoverer(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_schemas.types.update_discoverer_request.UpdateDiscovererRequest = {
            "discoverer_id": discoverer_id
        }
        if description is not None:
            input_["description"] = description
        if cross_account is not None:
            input_["cross_account"] = cross_account

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_registry(
        self,
        registry_name: "capo_schemas.types.__string.__string",
        *,
        config_overrides: Optional[schemasClientConfig] = None,
        description: Optional[
            "capo_schemas.types.__string_min0_max256.__stringMin0Max256"
        ] = None,
    ) -> "capo_schemas.types.update_registry_response.UpdateRegistryResponse":
        """<p>Updates a registry.</p>

        Args:
            description: <p>The description of the registry to update.</p>
            registry_name: <p>The name of the registry.</p>

        Raises:
            capo_schemas.errors.bad_request_exception.BadRequestException
            capo_schemas.errors.forbidden_exception.ForbiddenException
            capo_schemas.errors.internal_server_error_exception.InternalServerErrorException
            capo_schemas.errors.not_found_exception.NotFoundException
            capo_schemas.errors.service_unavailable_exception.ServiceUnavailableException
            capo_schemas.errors.unauthorized_exception.UnauthorizedException
            capo_schemas.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_schemas.types.update_registry_request.UpdateRegistryRequest]",
        ) -> OperationResponse[
            "capo_schemas.types.update_registry_response.UpdateRegistryResponse"
        ]:
            import capo_schemas._operations.schemas.update_registry

            output, http_response = (
                capo_schemas._operations.schemas.update_registry.update_registry(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_schemas.types.update_registry_request.UpdateRegistryRequest = {
            "registry_name": registry_name
        }
        if description is not None:
            input_["description"] = description

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_schema(
        self,
        registry_name: "capo_schemas.types.__string.__string",
        schema_name: "capo_schemas.types.__string.__string",
        *,
        config_overrides: Optional[schemasClientConfig] = None,
        client_token_id: Optional[
            "capo_schemas.types.__string_min0_max36.__stringMin0Max36"
        ] = None,
        content: Optional[
            "capo_schemas.types.__string_min1_max100000.__stringMin1Max100000"
        ] = None,
        description: Optional[
            "capo_schemas.types.__string_min0_max256.__stringMin0Max256"
        ] = None,
        type: Optional["capo_schemas.types.type.Type"] = None,
    ) -> "capo_schemas.types.update_schema_response.UpdateSchemaResponse":
        """<p>Updates the schema definition</p> <note><p>Inactive schemas will be deleted after two years.</p></note>

        Args:
            client_token_id: <p>The ID of the client token.</p>
            content: <p>The source of the schema definition.</p>
            description: <p>The description of the schema.</p>
            registry_name: <p>The name of the registry.</p>
            schema_name: <p>The name of the schema.</p>
            type: <p>The schema type for the events schema.</p>

        Raises:
            capo_schemas.errors.bad_request_exception.BadRequestException
            capo_schemas.errors.forbidden_exception.ForbiddenException
            capo_schemas.errors.internal_server_error_exception.InternalServerErrorException
            capo_schemas.errors.not_found_exception.NotFoundException
            capo_schemas.errors.service_unavailable_exception.ServiceUnavailableException
            capo_schemas.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_schemas.types.update_schema_request.UpdateSchemaRequest]",
        ) -> OperationResponse[
            "capo_schemas.types.update_schema_response.UpdateSchemaResponse"
        ]:
            import capo_schemas._operations.schemas.update_schema

            output, http_response = (
                capo_schemas._operations.schemas.update_schema.update_schema(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_schemas.types.update_schema_request.UpdateSchemaRequest = {
            "registry_name": registry_name,
            "schema_name": schema_name,
        }
        if client_token_id is None:
            client_token_id = str(uuid.uuid4())
        input_["client_token_id"] = client_token_id
        if content is not None:
            input_["content"] = content
        if description is not None:
            input_["description"] = description
        if type is not None:
            input_["type"] = type

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
