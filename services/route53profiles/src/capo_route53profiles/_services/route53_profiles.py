"""Generated from Smithy shape ``com.amazonaws.route53profiles#Route53Profiles``."""

import warnings
from collections.abc import Iterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import BaseHandler, Client

import capo_route53profiles._auth._signers
import capo_route53profiles._auth._sigv4
from capo_route53profiles._auth._identity import Credentials
from capo_route53profiles._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_route53profiles._auth._zapros_handler import AuthMiddleware
from capo_route53profiles._pagination import resolve_path as _resolve_path
from capo_route53profiles._services._aws_config import aws_config
from capo_route53profiles._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import capo_route53profiles.types.arn
    import capo_route53profiles.types.associate_profile_request
    import capo_route53profiles.types.associate_profile_response
    import capo_route53profiles.types.associate_resource_to_profile_request
    import capo_route53profiles.types.associate_resource_to_profile_response
    import capo_route53profiles.types.create_profile_request
    import capo_route53profiles.types.create_profile_response
    import capo_route53profiles.types.creator_request_id
    import capo_route53profiles.types.delete_profile_request
    import capo_route53profiles.types.delete_profile_response
    import capo_route53profiles.types.disassociate_profile_request
    import capo_route53profiles.types.disassociate_profile_response
    import capo_route53profiles.types.disassociate_resource_from_profile_request
    import capo_route53profiles.types.disassociate_resource_from_profile_response
    import capo_route53profiles.types.get_profile_association_request
    import capo_route53profiles.types.get_profile_association_response
    import capo_route53profiles.types.get_profile_request
    import capo_route53profiles.types.get_profile_resource_association_request
    import capo_route53profiles.types.get_profile_resource_association_response
    import capo_route53profiles.types.get_profile_response
    import capo_route53profiles.types.list_profile_associations_request
    import capo_route53profiles.types.list_profile_associations_response
    import capo_route53profiles.types.list_profile_resource_associations_request
    import capo_route53profiles.types.list_profile_resource_associations_response
    import capo_route53profiles.types.list_profiles_request
    import capo_route53profiles.types.list_profiles_response
    import capo_route53profiles.types.list_tags_for_resource_request
    import capo_route53profiles.types.list_tags_for_resource_response
    import capo_route53profiles.types.max_results
    import capo_route53profiles.types.name
    import capo_route53profiles.types.next_token
    import capo_route53profiles.types.profile_association
    import capo_route53profiles.types.profile_resource_association
    import capo_route53profiles.types.profile_summary
    import capo_route53profiles.types.resource_id
    import capo_route53profiles.types.resource_properties
    import capo_route53profiles.types.string
    import capo_route53profiles.types.tag_key_list
    import capo_route53profiles.types.tag_list
    import capo_route53profiles.types.tag_map
    import capo_route53profiles.types.tag_resource_request
    import capo_route53profiles.types.tag_resource_response
    import capo_route53profiles.types.untag_resource_request
    import capo_route53profiles.types.untag_resource_response
    import capo_route53profiles.types.update_profile_resource_association_request
    import capo_route53profiles.types.update_profile_resource_association_response


class Route53ProfilesClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None
    anonymous: bool | None


class Route53ProfilesClient:
    """A client for the ``Route53Profiles`` service.

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
        self._config = Route53ProfilesClientConfig(
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
        self, config_overrides: Optional[Route53ProfilesClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: Route53ProfilesClientConfig = config_overrides or {}
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

    def associate_profile(
        self,
        profile_id: "capo_route53profiles.types.resource_id.ResourceId",
        resource_id: "capo_route53profiles.types.resource_id.ResourceId",
        name: "capo_route53profiles.types.name.Name",
        *,
        config_overrides: Optional[Route53ProfilesClientConfig] = None,
        tags: Optional["capo_route53profiles.types.tag_list.TagList"] = None,
    ) -> (
        "capo_route53profiles.types.associate_profile_response.AssociateProfileResponse"
    ):
        """<p> Associates a Route 53 Profiles profile with a VPC. A VPC can have only one Profile associated with it, but a Profile can be associated with 1000 of VPCs (and you can request a higher quota). For more information, see <a href="https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/DNSLimitations.html#limits-api-entities">https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/DNSLimitations.html#limits-api-entities</a>. </p>

        Args:
            profile_id: <p> ID of the Profile. </p>
            resource_id: <p> The ID of the VPC. </p>
            name: <p> A name for the association. </p>
            tags: <p> A list of the tag keys and values that you want to identify the Profile association. </p>

        Raises:
            capo_route53profiles.errors.access_denied_exception.AccessDeniedException: <p> The current account doesn't have the IAM permissions required to perform the specified operation. </p>
            capo_route53profiles.errors.conflict_exception.ConflictException: <p> The request you submitted conflicts with an existing request. </p>
            capo_route53profiles.errors.invalid_parameter_exception.InvalidParameterException: <p> One or more parameters in this request are not valid. </p>
            capo_route53profiles.errors.limit_exceeded_exception.LimitExceededException: <p> The request caused one or more limits to be exceeded. </p>
            capo_route53profiles.errors.resource_exists_exception.ResourceExistsException: <p> The resource you are trying to associate, has already been associated. </p>
            capo_route53profiles.errors.resource_not_found_exception.ResourceNotFoundException: <p> The resource you are associating is not found. </p>
            capo_route53profiles.errors.throttling_exception.ThrottlingException: <p> The request was throttled. Try again in a few minutes. </p>
            capo_route53profiles.errors.validation_exception.ValidationException: <p> You have provided an invalid command. </p>
            capo_route53profiles.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_route53profiles.types.associate_profile_request.AssociateProfileRequest]",
        ) -> OperationResponse[
            "capo_route53profiles.types.associate_profile_response.AssociateProfileResponse"
        ]:
            import capo_route53profiles._operations.route53_profiles.associate_profile

            output, http_response = (
                capo_route53profiles._operations.route53_profiles.associate_profile.associate_profile(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route53profiles.types.associate_profile_request.AssociateProfileRequest = {
            "profile_id": profile_id,
            "resource_id": resource_id,
            "name": name,
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

    def associate_resource_to_profile(
        self,
        profile_id: "capo_route53profiles.types.resource_id.ResourceId",
        resource_arn: "capo_route53profiles.types.arn.Arn",
        name: "capo_route53profiles.types.name.Name",
        *,
        config_overrides: Optional[Route53ProfilesClientConfig] = None,
        resource_properties: Optional[
            "capo_route53profiles.types.resource_properties.ResourceProperties"
        ] = None,
    ) -> "capo_route53profiles.types.associate_resource_to_profile_response.AssociateResourceToProfileResponse":
        """<p> Associates a DNS reource configuration to a Route 53 Profile. </p>

        Args:
            profile_id: <p> ID of the Profile. </p>
            resource_arn: <p> Amazon resource number, ARN, of the DNS resource. </p>
            name: <p> Name for the resource association. </p>
            resource_properties: <p> If you are adding a DNS Firewall rule group, include also a priority. The priority indicates the processing order for the rule groups, starting with the priority assinged the lowest value. </p> <p>The allowed values for priority are between 100 and 9900.</p>

        Raises:
            capo_route53profiles.errors.access_denied_exception.AccessDeniedException: <p> The current account doesn't have the IAM permissions required to perform the specified operation. </p>
            capo_route53profiles.errors.conflict_exception.ConflictException: <p> The request you submitted conflicts with an existing request. </p>
            capo_route53profiles.errors.internal_service_error_exception.InternalServiceErrorException: <p> An internal server error occured. Retry your request. </p>
            capo_route53profiles.errors.invalid_parameter_exception.InvalidParameterException: <p> One or more parameters in this request are not valid. </p>
            capo_route53profiles.errors.limit_exceeded_exception.LimitExceededException: <p> The request caused one or more limits to be exceeded. </p>
            capo_route53profiles.errors.resource_not_found_exception.ResourceNotFoundException: <p> The resource you are associating is not found. </p>
            capo_route53profiles.errors.throttling_exception.ThrottlingException: <p> The request was throttled. Try again in a few minutes. </p>
            capo_route53profiles.errors.validation_exception.ValidationException: <p> You have provided an invalid command. </p>
            capo_route53profiles.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_route53profiles.types.associate_resource_to_profile_request.AssociateResourceToProfileRequest]",
        ) -> OperationResponse[
            "capo_route53profiles.types.associate_resource_to_profile_response.AssociateResourceToProfileResponse"
        ]:
            import capo_route53profiles._operations.route53_profiles.associate_resource_to_profile

            output, http_response = (
                capo_route53profiles._operations.route53_profiles.associate_resource_to_profile.associate_resource_to_profile(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route53profiles.types.associate_resource_to_profile_request.AssociateResourceToProfileRequest = {
            "profile_id": profile_id,
            "resource_arn": resource_arn,
            "name": name,
        }
        if resource_properties is not None:
            input_["resource_properties"] = resource_properties

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_profile(
        self,
        name: "capo_route53profiles.types.name.Name",
        client_token: "capo_route53profiles.types.creator_request_id.CreatorRequestId",
        *,
        config_overrides: Optional[Route53ProfilesClientConfig] = None,
        tags: Optional["capo_route53profiles.types.tag_list.TagList"] = None,
    ) -> "capo_route53profiles.types.create_profile_response.CreateProfileResponse":
        """<p> Creates an empty Route 53 Profile. </p>

        Args:
            name: <p> A name for the Profile. </p>
            client_token: <p> <code>ClientToken</code> is an idempotency token that ensures a call to <code>CreateProfile</code> completes only once. You choose the value to pass. For example, an issue might prevent you from getting a response from <code>CreateProfile</code>. In this case, safely retry your call to <code>CreateProfile</code> by using the same <code>CreateProfile</code> parameter value. </p>
            tags: <p> A list of the tag keys and values that you want to associate with the Route 53 Profile. </p>

        Raises:
            capo_route53profiles.errors.access_denied_exception.AccessDeniedException: <p> The current account doesn't have the IAM permissions required to perform the specified operation. </p>
            capo_route53profiles.errors.invalid_parameter_exception.InvalidParameterException: <p> One or more parameters in this request are not valid. </p>
            capo_route53profiles.errors.limit_exceeded_exception.LimitExceededException: <p> The request caused one or more limits to be exceeded. </p>
            capo_route53profiles.errors.throttling_exception.ThrottlingException: <p> The request was throttled. Try again in a few minutes. </p>
            capo_route53profiles.errors.validation_exception.ValidationException: <p> You have provided an invalid command. </p>
            capo_route53profiles.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_route53profiles.types.create_profile_request.CreateProfileRequest]",
        ) -> OperationResponse[
            "capo_route53profiles.types.create_profile_response.CreateProfileResponse"
        ]:
            import capo_route53profiles._operations.route53_profiles.create_profile

            output, http_response = (
                capo_route53profiles._operations.route53_profiles.create_profile.create_profile(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route53profiles.types.create_profile_request.CreateProfileRequest = {
            "name": name,
            "client_token": client_token,
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

    def delete_profile(
        self,
        profile_id: "capo_route53profiles.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[Route53ProfilesClientConfig] = None,
    ) -> "capo_route53profiles.types.delete_profile_response.DeleteProfileResponse":
        """<p> Deletes the specified Route 53 Profile. Before you can delete a profile, you must first disassociate it from all VPCs. </p>

        Args:
            profile_id: <p> The ID of the Profile that you want to delete. </p>

        Raises:
            capo_route53profiles.errors.access_denied_exception.AccessDeniedException: <p> The current account doesn't have the IAM permissions required to perform the specified operation. </p>
            capo_route53profiles.errors.conflict_exception.ConflictException: <p> The request you submitted conflicts with an existing request. </p>
            capo_route53profiles.errors.resource_not_found_exception.ResourceNotFoundException: <p> The resource you are associating is not found. </p>
            capo_route53profiles.errors.throttling_exception.ThrottlingException: <p> The request was throttled. Try again in a few minutes. </p>
            capo_route53profiles.errors.validation_exception.ValidationException: <p> You have provided an invalid command. </p>
            capo_route53profiles.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_route53profiles.types.delete_profile_request.DeleteProfileRequest]",
        ) -> OperationResponse[
            "capo_route53profiles.types.delete_profile_response.DeleteProfileResponse"
        ]:
            import capo_route53profiles._operations.route53_profiles.delete_profile

            output, http_response = (
                capo_route53profiles._operations.route53_profiles.delete_profile.delete_profile(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route53profiles.types.delete_profile_request.DeleteProfileRequest = {
            "profile_id": profile_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def disassociate_profile(
        self,
        profile_id: "capo_route53profiles.types.resource_id.ResourceId",
        resource_id: "capo_route53profiles.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[Route53ProfilesClientConfig] = None,
    ) -> "capo_route53profiles.types.disassociate_profile_response.DisassociateProfileResponse":
        """<p> Dissociates a specified Route 53 Profile from the specified VPC. </p>

        Args:
            profile_id: <p> ID of the Profile. </p>
            resource_id: <p> The ID of the VPC. </p>

        Raises:
            capo_route53profiles.errors.access_denied_exception.AccessDeniedException: <p> The current account doesn't have the IAM permissions required to perform the specified operation. </p>
            capo_route53profiles.errors.invalid_parameter_exception.InvalidParameterException: <p> One or more parameters in this request are not valid. </p>
            capo_route53profiles.errors.limit_exceeded_exception.LimitExceededException: <p> The request caused one or more limits to be exceeded. </p>
            capo_route53profiles.errors.resource_not_found_exception.ResourceNotFoundException: <p> The resource you are associating is not found. </p>
            capo_route53profiles.errors.throttling_exception.ThrottlingException: <p> The request was throttled. Try again in a few minutes. </p>
            capo_route53profiles.errors.validation_exception.ValidationException: <p> You have provided an invalid command. </p>
            capo_route53profiles.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_route53profiles.types.disassociate_profile_request.DisassociateProfileRequest]",
        ) -> OperationResponse[
            "capo_route53profiles.types.disassociate_profile_response.DisassociateProfileResponse"
        ]:
            import capo_route53profiles._operations.route53_profiles.disassociate_profile

            output, http_response = (
                capo_route53profiles._operations.route53_profiles.disassociate_profile.disassociate_profile(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route53profiles.types.disassociate_profile_request.DisassociateProfileRequest = {
            "profile_id": profile_id,
            "resource_id": resource_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def disassociate_resource_from_profile(
        self,
        profile_id: "capo_route53profiles.types.resource_id.ResourceId",
        resource_arn: "capo_route53profiles.types.arn.Arn",
        *,
        config_overrides: Optional[Route53ProfilesClientConfig] = None,
    ) -> "capo_route53profiles.types.disassociate_resource_from_profile_response.DisassociateResourceFromProfileResponse":
        """<p> Dissoaciated a specified resource, from the Route 53 Profile. </p>

        Args:
            profile_id: <p> The ID of the Profile. </p>
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource. </p>

        Raises:
            capo_route53profiles.errors.access_denied_exception.AccessDeniedException: <p> The current account doesn't have the IAM permissions required to perform the specified operation. </p>
            capo_route53profiles.errors.conflict_exception.ConflictException: <p> The request you submitted conflicts with an existing request. </p>
            capo_route53profiles.errors.internal_service_error_exception.InternalServiceErrorException: <p> An internal server error occured. Retry your request. </p>
            capo_route53profiles.errors.invalid_parameter_exception.InvalidParameterException: <p> One or more parameters in this request are not valid. </p>
            capo_route53profiles.errors.limit_exceeded_exception.LimitExceededException: <p> The request caused one or more limits to be exceeded. </p>
            capo_route53profiles.errors.resource_not_found_exception.ResourceNotFoundException: <p> The resource you are associating is not found. </p>
            capo_route53profiles.errors.throttling_exception.ThrottlingException: <p> The request was throttled. Try again in a few minutes. </p>
            capo_route53profiles.errors.validation_exception.ValidationException: <p> You have provided an invalid command. </p>
            capo_route53profiles.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_route53profiles.types.disassociate_resource_from_profile_request.DisassociateResourceFromProfileRequest]",
        ) -> OperationResponse[
            "capo_route53profiles.types.disassociate_resource_from_profile_response.DisassociateResourceFromProfileResponse"
        ]:
            import capo_route53profiles._operations.route53_profiles.disassociate_resource_from_profile

            output, http_response = (
                capo_route53profiles._operations.route53_profiles.disassociate_resource_from_profile.disassociate_resource_from_profile(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route53profiles.types.disassociate_resource_from_profile_request.DisassociateResourceFromProfileRequest = {
            "profile_id": profile_id,
            "resource_arn": resource_arn,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_profile(
        self,
        profile_id: "capo_route53profiles.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[Route53ProfilesClientConfig] = None,
    ) -> "capo_route53profiles.types.get_profile_response.GetProfileResponse":
        """<p> Returns information about a specified Route 53 Profile, such as whether whether the Profile is shared, and the current status of the Profile. </p>

        Args:
            profile_id: <p> ID of the Profile. </p>

        Raises:
            capo_route53profiles.errors.access_denied_exception.AccessDeniedException: <p> The current account doesn't have the IAM permissions required to perform the specified operation. </p>
            capo_route53profiles.errors.resource_not_found_exception.ResourceNotFoundException: <p> The resource you are associating is not found. </p>
            capo_route53profiles.errors.throttling_exception.ThrottlingException: <p> The request was throttled. Try again in a few minutes. </p>
            capo_route53profiles.errors.validation_exception.ValidationException: <p> You have provided an invalid command. </p>
            capo_route53profiles.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_route53profiles.types.get_profile_request.GetProfileRequest]",
        ) -> OperationResponse[
            "capo_route53profiles.types.get_profile_response.GetProfileResponse"
        ]:
            import capo_route53profiles._operations.route53_profiles.get_profile

            output, http_response = (
                capo_route53profiles._operations.route53_profiles.get_profile.get_profile(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route53profiles.types.get_profile_request.GetProfileRequest = {
            "profile_id": profile_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_profile_association(
        self,
        profile_association_id: "capo_route53profiles.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[Route53ProfilesClientConfig] = None,
    ) -> "capo_route53profiles.types.get_profile_association_response.GetProfileAssociationResponse":
        """<p> Retrieves a Route 53 Profile association for a VPC. A VPC can have only one Profile association, but a Profile can be associated with up to 5000 VPCs. </p>

        Args:
            profile_association_id: <p> The identifier of the association you want to get information about. </p>

        Raises:
            capo_route53profiles.errors.access_denied_exception.AccessDeniedException: <p> The current account doesn't have the IAM permissions required to perform the specified operation. </p>
            capo_route53profiles.errors.resource_not_found_exception.ResourceNotFoundException: <p> The resource you are associating is not found. </p>
            capo_route53profiles.errors.throttling_exception.ThrottlingException: <p> The request was throttled. Try again in a few minutes. </p>
            capo_route53profiles.errors.validation_exception.ValidationException: <p> You have provided an invalid command. </p>
            capo_route53profiles.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_route53profiles.types.get_profile_association_request.GetProfileAssociationRequest]",
        ) -> OperationResponse[
            "capo_route53profiles.types.get_profile_association_response.GetProfileAssociationResponse"
        ]:
            import capo_route53profiles._operations.route53_profiles.get_profile_association

            output, http_response = (
                capo_route53profiles._operations.route53_profiles.get_profile_association.get_profile_association(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route53profiles.types.get_profile_association_request.GetProfileAssociationRequest = {
            "profile_association_id": profile_association_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_profile_resource_association(
        self,
        profile_resource_association_id: "capo_route53profiles.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[Route53ProfilesClientConfig] = None,
    ) -> "capo_route53profiles.types.get_profile_resource_association_response.GetProfileResourceAssociationResponse":
        """<p> Returns information about a specified Route 53 Profile resource association. </p>

        Args:
            profile_resource_association_id: <p> The ID of the profile resource association that you want to get information about. </p>

        Raises:
            capo_route53profiles.errors.access_denied_exception.AccessDeniedException: <p> The current account doesn't have the IAM permissions required to perform the specified operation. </p>
            capo_route53profiles.errors.invalid_parameter_exception.InvalidParameterException: <p> One or more parameters in this request are not valid. </p>
            capo_route53profiles.errors.resource_not_found_exception.ResourceNotFoundException: <p> The resource you are associating is not found. </p>
            capo_route53profiles.errors.throttling_exception.ThrottlingException: <p> The request was throttled. Try again in a few minutes. </p>
            capo_route53profiles.errors.validation_exception.ValidationException: <p> You have provided an invalid command. </p>
            capo_route53profiles.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_route53profiles.types.get_profile_resource_association_request.GetProfileResourceAssociationRequest]",
        ) -> OperationResponse[
            "capo_route53profiles.types.get_profile_resource_association_response.GetProfileResourceAssociationResponse"
        ]:
            import capo_route53profiles._operations.route53_profiles.get_profile_resource_association

            output, http_response = (
                capo_route53profiles._operations.route53_profiles.get_profile_resource_association.get_profile_resource_association(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route53profiles.types.get_profile_resource_association_request.GetProfileResourceAssociationRequest = {
            "profile_resource_association_id": profile_resource_association_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_profile_associations(
        self,
        *,
        config_overrides: Optional[Route53ProfilesClientConfig] = None,
        resource_id: Optional[
            "capo_route53profiles.types.resource_id.ResourceId"
        ] = None,
        profile_id: Optional[
            "capo_route53profiles.types.resource_id.ResourceId"
        ] = None,
        max_results: Optional[
            "capo_route53profiles.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["capo_route53profiles.types.next_token.NextToken"] = None,
    ) -> "capo_route53profiles.types.list_profile_associations_response.ListProfileAssociationsResponse":
        """<p> Lists all the VPCs that the specified Route 53 Profile is associated with. </p>

        Args:
            resource_id: <p> ID of the VPC. </p>
            profile_id: <p> ID of the Profile. </p>
            max_results: <p> The maximum number of objects that you want to return for this request. If more objects are available, in the response, a <code>NextToken</code> value, which you can use in a subsequent call to get the next batch of objects, is provided.</p> <p> If you don't specify a value for <code>MaxResults</code>, up to 100 objects are returned. </p>
            next_token: <p> For the first call to this list request, omit this value. </p> <p>When you request a list of objects, at most the number of objects specified by <code>MaxResults</code> is returned. If more objects are available for retrieval, a <code>NextToken</code> value is returned in the response. To retrieve the next batch of objects, use the token that was returned for the prior request in your next request.</p>

        Raises:
            capo_route53profiles.errors.access_denied_exception.AccessDeniedException: <p> The current account doesn't have the IAM permissions required to perform the specified operation. </p>
            capo_route53profiles.errors.invalid_next_token_exception.InvalidNextTokenException: <p> The <code>NextToken</code> you provided isn;t valid. </p>
            capo_route53profiles.errors.invalid_parameter_exception.InvalidParameterException: <p> One or more parameters in this request are not valid. </p>
            capo_route53profiles.errors.throttling_exception.ThrottlingException: <p> The request was throttled. Try again in a few minutes. </p>
            capo_route53profiles.errors.validation_exception.ValidationException: <p> You have provided an invalid command. </p>
            capo_route53profiles.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_route53profiles.types.list_profile_associations_request.ListProfileAssociationsRequest]",
        ) -> OperationResponse[
            "capo_route53profiles.types.list_profile_associations_response.ListProfileAssociationsResponse"
        ]:
            import capo_route53profiles._operations.route53_profiles.list_profile_associations

            output, http_response = (
                capo_route53profiles._operations.route53_profiles.list_profile_associations.list_profile_associations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route53profiles.types.list_profile_associations_request.ListProfileAssociationsRequest = {}
        if resource_id is not None:
            input_["resource_id"] = resource_id
        if profile_id is not None:
            input_["profile_id"] = profile_id
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

    def iter_list_profile_associations(
        self,
        *,
        config_overrides: Optional[Route53ProfilesClientConfig] = None,
        resource_id: Optional[
            "capo_route53profiles.types.resource_id.ResourceId"
        ] = None,
        profile_id: Optional[
            "capo_route53profiles.types.resource_id.ResourceId"
        ] = None,
        max_results: Optional[
            "capo_route53profiles.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["capo_route53profiles.types.next_token.NextToken"] = None,
    ) -> "Iterator[capo_route53profiles.types.profile_association.ProfileAssociation]":
        _token = next_token
        while True:
            _response = self.list_profile_associations(
                config_overrides=config_overrides,
                resource_id=resource_id,
                profile_id=profile_id,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("profile_associations",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_profile_resource_associations(
        self,
        profile_id: "capo_route53profiles.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[Route53ProfilesClientConfig] = None,
        resource_type: Optional["capo_route53profiles.types.string.String"] = None,
        max_results: Optional[
            "capo_route53profiles.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["capo_route53profiles.types.next_token.NextToken"] = None,
    ) -> "capo_route53profiles.types.list_profile_resource_associations_response.ListProfileResourceAssociationsResponse":
        """<p> Lists all the resource associations for the specified Route 53 Profile. </p>

        Args:
            profile_id: <p> The ID of the Profile. </p>
            resource_type: <p> ID of a resource if you want information on only one type. </p>
            max_results: <p> The maximum number of objects that you want to return for this request. If more objects are available, in the response, a <code>NextToken</code> value, which you can use in a subsequent call to get the next batch of objects, is provided.</p> <p> If you don't specify a value for <code>MaxResults</code>, up to 100 objects are returned. </p>
            next_token: <p> For the first call to this list request, omit this value. </p> <p>When you request a list of objects, at most the number of objects specified by <code>MaxResults</code> is returned. If more objects are available for retrieval, a <code>NextToken</code> value is returned in the response. To retrieve the next batch of objects, use the token that was returned for the prior request in your next request.</p>

        Raises:
            capo_route53profiles.errors.access_denied_exception.AccessDeniedException: <p> The current account doesn't have the IAM permissions required to perform the specified operation. </p>
            capo_route53profiles.errors.internal_service_error_exception.InternalServiceErrorException: <p> An internal server error occured. Retry your request. </p>
            capo_route53profiles.errors.invalid_next_token_exception.InvalidNextTokenException: <p> The <code>NextToken</code> you provided isn;t valid. </p>
            capo_route53profiles.errors.invalid_parameter_exception.InvalidParameterException: <p> One or more parameters in this request are not valid. </p>
            capo_route53profiles.errors.resource_not_found_exception.ResourceNotFoundException: <p> The resource you are associating is not found. </p>
            capo_route53profiles.errors.throttling_exception.ThrottlingException: <p> The request was throttled. Try again in a few minutes. </p>
            capo_route53profiles.errors.validation_exception.ValidationException: <p> You have provided an invalid command. </p>
            capo_route53profiles.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_route53profiles.types.list_profile_resource_associations_request.ListProfileResourceAssociationsRequest]",
        ) -> OperationResponse[
            "capo_route53profiles.types.list_profile_resource_associations_response.ListProfileResourceAssociationsResponse"
        ]:
            import capo_route53profiles._operations.route53_profiles.list_profile_resource_associations

            output, http_response = (
                capo_route53profiles._operations.route53_profiles.list_profile_resource_associations.list_profile_resource_associations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route53profiles.types.list_profile_resource_associations_request.ListProfileResourceAssociationsRequest = {
            "profile_id": profile_id
        }
        if resource_type is not None:
            input_["resource_type"] = resource_type
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

    def iter_list_profile_resource_associations(
        self,
        profile_id: "capo_route53profiles.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[Route53ProfilesClientConfig] = None,
        resource_type: Optional["capo_route53profiles.types.string.String"] = None,
        max_results: Optional[
            "capo_route53profiles.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["capo_route53profiles.types.next_token.NextToken"] = None,
    ) -> "Iterator[capo_route53profiles.types.profile_resource_association.ProfileResourceAssociation]":
        _token = next_token
        while True:
            _response = self.list_profile_resource_associations(
                profile_id,
                config_overrides=config_overrides,
                resource_type=resource_type,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("profile_resource_associations",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_profiles(
        self,
        *,
        config_overrides: Optional[Route53ProfilesClientConfig] = None,
        max_results: Optional[
            "capo_route53profiles.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["capo_route53profiles.types.next_token.NextToken"] = None,
    ) -> "capo_route53profiles.types.list_profiles_response.ListProfilesResponse":
        """<p> Lists all the Route 53 Profiles associated with your Amazon Web Services account. </p>

        Args:
            max_results: <p> The maximum number of objects that you want to return for this request. If more objects are available, in the response, a <code>NextToken</code> value, which you can use in a subsequent call to get the next batch of objects, is provided.</p> <p> If you don't specify a value for <code>MaxResults</code>, up to 100 objects are returned. </p>
            next_token: <p> For the first call to this list request, omit this value. </p> <p>When you request a list of objects, at most the number of objects specified by <code>MaxResults</code> is returned. If more objects are available for retrieval, a <code>NextToken</code> value is returned in the response. To retrieve the next batch of objects, use the token that was returned for the prior request in your next request.</p>

        Raises:
            capo_route53profiles.errors.access_denied_exception.AccessDeniedException: <p> The current account doesn't have the IAM permissions required to perform the specified operation. </p>
            capo_route53profiles.errors.invalid_next_token_exception.InvalidNextTokenException: <p> The <code>NextToken</code> you provided isn;t valid. </p>
            capo_route53profiles.errors.invalid_parameter_exception.InvalidParameterException: <p> One or more parameters in this request are not valid. </p>
            capo_route53profiles.errors.throttling_exception.ThrottlingException: <p> The request was throttled. Try again in a few minutes. </p>
            capo_route53profiles.errors.validation_exception.ValidationException: <p> You have provided an invalid command. </p>
            capo_route53profiles.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_route53profiles.types.list_profiles_request.ListProfilesRequest]",
        ) -> OperationResponse[
            "capo_route53profiles.types.list_profiles_response.ListProfilesResponse"
        ]:
            import capo_route53profiles._operations.route53_profiles.list_profiles

            output, http_response = (
                capo_route53profiles._operations.route53_profiles.list_profiles.list_profiles(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route53profiles.types.list_profiles_request.ListProfilesRequest = {}
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

    def iter_list_profiles(
        self,
        *,
        config_overrides: Optional[Route53ProfilesClientConfig] = None,
        max_results: Optional[
            "capo_route53profiles.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["capo_route53profiles.types.next_token.NextToken"] = None,
    ) -> "Iterator[capo_route53profiles.types.profile_summary.ProfileSummary]":
        _token = next_token
        while True:
            _response = self.list_profiles(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("profile_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_tags_for_resource(
        self,
        resource_arn: "capo_route53profiles.types.arn.Arn",
        *,
        config_overrides: Optional[Route53ProfilesClientConfig] = None,
    ) -> "capo_route53profiles.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p> Lists the tags that you associated with the specified resource. </p>

        Args:
            resource_arn: <p> The Amazon Resource Name (ARN) for the resource that you want to list the tags for. </p>

        Raises:
            capo_route53profiles.errors.access_denied_exception.AccessDeniedException: <p> The current account doesn't have the IAM permissions required to perform the specified operation. </p>
            capo_route53profiles.errors.conflict_exception.ConflictException: <p> The request you submitted conflicts with an existing request. </p>
            capo_route53profiles.errors.resource_not_found_exception.ResourceNotFoundException: <p> The resource you are associating is not found. </p>
            capo_route53profiles.errors.throttling_exception.ThrottlingException: <p> The request was throttled. Try again in a few minutes. </p>
            capo_route53profiles.errors.validation_exception.ValidationException: <p> You have provided an invalid command. </p>
            capo_route53profiles.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_route53profiles.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> OperationResponse[
            "capo_route53profiles.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import capo_route53profiles._operations.route53_profiles.list_tags_for_resource

            output, http_response = (
                capo_route53profiles._operations.route53_profiles.list_tags_for_resource.list_tags_for_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route53profiles.types.list_tags_for_resource_request.ListTagsForResourceRequest = {
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
        resource_arn: "capo_route53profiles.types.arn.Arn",
        tags: "capo_route53profiles.types.tag_map.TagMap",
        *,
        config_overrides: Optional[Route53ProfilesClientConfig] = None,
    ) -> "capo_route53profiles.types.tag_resource_response.TagResourceResponse":
        """<p> Adds one or more tags to a specified resource. </p>

        Args:
            resource_arn: <p> The Amazon Resource Name (ARN) for the resource that you want to add tags to. </p>
            tags: <p> The tags that you want to add to the specified resource. </p>

        Raises:
            capo_route53profiles.errors.access_denied_exception.AccessDeniedException: <p> The current account doesn't have the IAM permissions required to perform the specified operation. </p>
            capo_route53profiles.errors.resource_not_found_exception.ResourceNotFoundException: <p> The resource you are associating is not found. </p>
            capo_route53profiles.errors.throttling_exception.ThrottlingException: <p> The request was throttled. Try again in a few minutes. </p>
            capo_route53profiles.errors.validation_exception.ValidationException: <p> You have provided an invalid command. </p>
            capo_route53profiles.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_route53profiles.types.tag_resource_request.TagResourceRequest]",
        ) -> OperationResponse[
            "capo_route53profiles.types.tag_resource_response.TagResourceResponse"
        ]:
            import capo_route53profiles._operations.route53_profiles.tag_resource

            output, http_response = (
                capo_route53profiles._operations.route53_profiles.tag_resource.tag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route53profiles.types.tag_resource_request.TagResourceRequest = {
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
        resource_arn: "capo_route53profiles.types.arn.Arn",
        tag_keys: "capo_route53profiles.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[Route53ProfilesClientConfig] = None,
    ) -> "capo_route53profiles.types.untag_resource_response.UntagResourceResponse":
        """<p> Removes one or more tags from a specified resource. </p>

        Args:
            resource_arn: <p> The Amazon Resource Name (ARN) for the resource that you want to remove tags from. </p>
            tag_keys: <p> The tags that you want to remove to the specified resource. </p>

        Raises:
            capo_route53profiles.errors.access_denied_exception.AccessDeniedException: <p> The current account doesn't have the IAM permissions required to perform the specified operation. </p>
            capo_route53profiles.errors.conflict_exception.ConflictException: <p> The request you submitted conflicts with an existing request. </p>
            capo_route53profiles.errors.resource_not_found_exception.ResourceNotFoundException: <p> The resource you are associating is not found. </p>
            capo_route53profiles.errors.throttling_exception.ThrottlingException: <p> The request was throttled. Try again in a few minutes. </p>
            capo_route53profiles.errors.validation_exception.ValidationException: <p> You have provided an invalid command. </p>
            capo_route53profiles.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_route53profiles.types.untag_resource_request.UntagResourceRequest]",
        ) -> OperationResponse[
            "capo_route53profiles.types.untag_resource_response.UntagResourceResponse"
        ]:
            import capo_route53profiles._operations.route53_profiles.untag_resource

            output, http_response = (
                capo_route53profiles._operations.route53_profiles.untag_resource.untag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route53profiles.types.untag_resource_request.UntagResourceRequest = {
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

    def update_profile_resource_association(
        self,
        profile_resource_association_id: "capo_route53profiles.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[Route53ProfilesClientConfig] = None,
        name: Optional["capo_route53profiles.types.name.Name"] = None,
        resource_properties: Optional[
            "capo_route53profiles.types.resource_properties.ResourceProperties"
        ] = None,
    ) -> "capo_route53profiles.types.update_profile_resource_association_response.UpdateProfileResourceAssociationResponse":
        """<p> Updates the specified Route 53 Profile resourse association. </p>

        Args:
            profile_resource_association_id: <p> ID of the resource association. </p>
            name: <p> Name of the resource association. </p>
            resource_properties: <p> If you are adding a DNS Firewall rule group, include also a priority. The priority indicates the processing order for the rule groups, starting with the priority assinged the lowest value. </p> <p>The allowed values for priority are between 100 and 9900.</p>

        Raises:
            capo_route53profiles.errors.access_denied_exception.AccessDeniedException: <p> The current account doesn't have the IAM permissions required to perform the specified operation. </p>
            capo_route53profiles.errors.conflict_exception.ConflictException: <p> The request you submitted conflicts with an existing request. </p>
            capo_route53profiles.errors.internal_service_error_exception.InternalServiceErrorException: <p> An internal server error occured. Retry your request. </p>
            capo_route53profiles.errors.invalid_parameter_exception.InvalidParameterException: <p> One or more parameters in this request are not valid. </p>
            capo_route53profiles.errors.limit_exceeded_exception.LimitExceededException: <p> The request caused one or more limits to be exceeded. </p>
            capo_route53profiles.errors.resource_not_found_exception.ResourceNotFoundException: <p> The resource you are associating is not found. </p>
            capo_route53profiles.errors.throttling_exception.ThrottlingException: <p> The request was throttled. Try again in a few minutes. </p>
            capo_route53profiles.errors.validation_exception.ValidationException: <p> You have provided an invalid command. </p>
            capo_route53profiles.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_route53profiles.types.update_profile_resource_association_request.UpdateProfileResourceAssociationRequest]",
        ) -> OperationResponse[
            "capo_route53profiles.types.update_profile_resource_association_response.UpdateProfileResourceAssociationResponse"
        ]:
            import capo_route53profiles._operations.route53_profiles.update_profile_resource_association

            output, http_response = (
                capo_route53profiles._operations.route53_profiles.update_profile_resource_association.update_profile_resource_association(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route53profiles.types.update_profile_resource_association_request.UpdateProfileResourceAssociationRequest = {
            "profile_resource_association_id": profile_resource_association_id
        }
        if name is not None:
            input_["name"] = name
        if resource_properties is not None:
            input_["resource_properties"] = resource_properties

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
