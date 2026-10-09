"""Generated from Smithy shape ``com.amazonaws.tnb#TNB``."""

import warnings
from collections.abc import Iterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import BaseHandler, Client

import capo_tnb._auth._signers
import capo_tnb._auth._sigv4
from capo_tnb._auth._identity import Credentials
from capo_tnb._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_tnb._auth._zapros_handler import AuthMiddleware
from capo_tnb._pagination import resolve_path as _resolve_path
from capo_tnb._services._aws_config import aws_config
from capo_tnb._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import capo_tnb.types.cancel_sol_network_operation_input
    import capo_tnb.types.create_sol_function_package_input
    import capo_tnb.types.create_sol_function_package_output
    import capo_tnb.types.create_sol_network_instance_input
    import capo_tnb.types.create_sol_network_instance_output
    import capo_tnb.types.create_sol_network_package_input
    import capo_tnb.types.create_sol_network_package_output
    import capo_tnb.types.delete_sol_function_package_input
    import capo_tnb.types.delete_sol_network_instance_input
    import capo_tnb.types.delete_sol_network_package_input
    import capo_tnb.types.descriptor_content_type
    import capo_tnb.types.get_sol_function_instance_input
    import capo_tnb.types.get_sol_function_instance_output
    import capo_tnb.types.get_sol_function_package_content_input
    import capo_tnb.types.get_sol_function_package_content_output
    import capo_tnb.types.get_sol_function_package_descriptor_input
    import capo_tnb.types.get_sol_function_package_descriptor_output
    import capo_tnb.types.get_sol_function_package_input
    import capo_tnb.types.get_sol_function_package_output
    import capo_tnb.types.get_sol_network_instance_input
    import capo_tnb.types.get_sol_network_instance_output
    import capo_tnb.types.get_sol_network_operation_input
    import capo_tnb.types.get_sol_network_operation_output
    import capo_tnb.types.get_sol_network_package_content_input
    import capo_tnb.types.get_sol_network_package_content_output
    import capo_tnb.types.get_sol_network_package_descriptor_input
    import capo_tnb.types.get_sol_network_package_descriptor_output
    import capo_tnb.types.get_sol_network_package_input
    import capo_tnb.types.get_sol_network_package_output
    import capo_tnb.types.instantiate_sol_network_instance_input
    import capo_tnb.types.instantiate_sol_network_instance_output
    import capo_tnb.types.list_sol_function_instance_info
    import capo_tnb.types.list_sol_function_instances_input
    import capo_tnb.types.list_sol_function_instances_output
    import capo_tnb.types.list_sol_function_package_info
    import capo_tnb.types.list_sol_function_packages_input
    import capo_tnb.types.list_sol_function_packages_output
    import capo_tnb.types.list_sol_network_instance_info
    import capo_tnb.types.list_sol_network_instances_input
    import capo_tnb.types.list_sol_network_instances_output
    import capo_tnb.types.list_sol_network_operations_info
    import capo_tnb.types.list_sol_network_operations_input
    import capo_tnb.types.list_sol_network_operations_output
    import capo_tnb.types.list_sol_network_package_info
    import capo_tnb.types.list_sol_network_packages_input
    import capo_tnb.types.list_sol_network_packages_output
    import capo_tnb.types.list_tags_for_resource_input
    import capo_tnb.types.list_tags_for_resource_output
    import capo_tnb.types.ns_instance_id
    import capo_tnb.types.ns_lcm_op_occ_id
    import capo_tnb.types.nsd_info_id
    import capo_tnb.types.nsd_operational_state
    import capo_tnb.types.operational_state
    import capo_tnb.types.package_content_type
    import capo_tnb.types.pagination_token
    import capo_tnb.types.put_sol_function_package_content_input
    import capo_tnb.types.put_sol_function_package_content_output
    import capo_tnb.types.put_sol_network_package_content_input
    import capo_tnb.types.put_sol_network_package_content_output
    import capo_tnb.types.sensitive_blob
    import capo_tnb.types.tag_keys
    import capo_tnb.types.tag_map
    import capo_tnb.types.tag_resource_input
    import capo_tnb.types.tag_resource_output
    import capo_tnb.types.terminate_sol_network_instance_input
    import capo_tnb.types.terminate_sol_network_instance_output
    import capo_tnb.types.tnb_resource_arn
    import capo_tnb.types.untag_resource_input
    import capo_tnb.types.untag_resource_output
    import capo_tnb.types.update_sol_function_package_input
    import capo_tnb.types.update_sol_function_package_output
    import capo_tnb.types.update_sol_network_instance_input
    import capo_tnb.types.update_sol_network_instance_output
    import capo_tnb.types.update_sol_network_modify
    import capo_tnb.types.update_sol_network_package_input
    import capo_tnb.types.update_sol_network_package_output
    import capo_tnb.types.update_sol_network_service_data
    import capo_tnb.types.update_sol_network_type
    import capo_tnb.types.validate_sol_function_package_content_input
    import capo_tnb.types.validate_sol_function_package_content_output
    import capo_tnb.types.validate_sol_network_package_content_input
    import capo_tnb.types.validate_sol_network_package_content_output
    import capo_tnb.types.vnf_instance_id
    import capo_tnb.types.vnf_pkg_id


class tnbClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None
    anonymous: bool | None


class tnbClient:
    """A client for the ``tnb`` service.

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
        self._config = tnbClientConfig(
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
        self, config_overrides: Optional[tnbClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: tnbClientConfig = config_overrides or {}
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

    def cancel_sol_network_operation(
        self,
        ns_lcm_op_occ_id: "capo_tnb.types.ns_lcm_op_occ_id.NsLcmOpOccId",
        *,
        config_overrides: Optional[tnbClientConfig] = None,
    ) -> None:
        """<p>Cancels a network operation.</p> <p>A network operation is any operation that is done to your network, such as network instance instantiation or termination.</p>

        Args:
            ns_lcm_op_occ_id: <p>The identifier of the network operation.</p>

        Raises:
            capo_tnb.errors.access_denied_exception.AccessDeniedException: <p>Insufficient permissions to make request.</p>
            capo_tnb.errors.internal_server_exception.InternalServerException: <p>Unexpected error occurred. Problem on the server.</p>
            capo_tnb.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource that doesn't exist.</p>
            capo_tnb.errors.throttling_exception.ThrottlingException: <p>Exception caused by throttling.</p>
            capo_tnb.errors.validation_exception.ValidationException: <p>Unable to process the request because the client provided input failed to satisfy request constraints.</p>
            capo_tnb.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Cancel a in-progress Sol Network Operation.

            >>> client.cancel_sol_network_operation(ns_lcm_op_occ_id='no-0d5b823eb5c2a9241')
        """

        def _handler(
            req: "OperationRequest[capo_tnb.types.cancel_sol_network_operation_input.CancelSolNetworkOperationInput]",
        ) -> OperationResponse[None]:
            import capo_tnb._operations.tnb.cancel_sol_network_operation

            output, http_response = (
                capo_tnb._operations.tnb.cancel_sol_network_operation.cancel_sol_network_operation(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_tnb.types.cancel_sol_network_operation_input.CancelSolNetworkOperationInput = {
            "ns_lcm_op_occ_id": ns_lcm_op_occ_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_sol_function_package(
        self,
        *,
        config_overrides: Optional[tnbClientConfig] = None,
        tags: Optional["capo_tnb.types.tag_map.TagMap"] = None,
    ) -> "capo_tnb.types.create_sol_function_package_output.CreateSolFunctionPackageOutput":
        """<p>Creates a function package.</p> <p>A function package is a .zip file in CSAR (Cloud Service Archive) format that contains a network function (an ETSI standard telecommunication application) and function package descriptor that uses the TOSCA standard to describe how the network functions should run on your network. For more information, see <a href="https://docs.aws.amazon.com/tnb/latest/ug/function-packages.html">Function packages</a> in the <i>Amazon Web Services Telco Network Builder User Guide</i>. </p> <p>Creating a function package is the first step for creating a network in AWS TNB. This request creates an empty container with an ID. The next step is to upload the actual CSAR zip file into that empty container. To upload function package content, see <a href="https://docs.aws.amazon.com/tnb/latest/APIReference/API_PutSolFunctionPackageContent.html">PutSolFunctionPackageContent</a>.</p>

        Args:
            tags: <p>A tag is a label that you assign to an Amazon Web Services resource. Each tag consists of a key and an optional value. You can use tags to search and filter your resources or track your Amazon Web Services costs.</p>

        Raises:
            capo_tnb.errors.access_denied_exception.AccessDeniedException: <p>Insufficient permissions to make request.</p>
            capo_tnb.errors.internal_server_exception.InternalServerException: <p>Unexpected error occurred. Problem on the server.</p>
            capo_tnb.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Service quotas have been exceeded.</p>
            capo_tnb.errors.throttling_exception.ThrottlingException: <p>Exception caused by throttling.</p>
            capo_tnb.errors.validation_exception.ValidationException: <p>Unable to process the request because the client provided input failed to satisfy request constraints.</p>
            capo_tnb.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Create a Sol function package

            >>> client.create_sol_function_package(tags={'Name': 'Resource'})
        """

        def _handler(
            req: "OperationRequest[capo_tnb.types.create_sol_function_package_input.CreateSolFunctionPackageInput]",
        ) -> OperationResponse[
            "capo_tnb.types.create_sol_function_package_output.CreateSolFunctionPackageOutput"
        ]:
            import capo_tnb._operations.tnb.create_sol_function_package

            output, http_response = (
                capo_tnb._operations.tnb.create_sol_function_package.create_sol_function_package(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_tnb.types.create_sol_function_package_input.CreateSolFunctionPackageInput = {}
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_sol_network_instance(
        self,
        nsd_info_id: "capo_tnb.types.nsd_info_id.NsdInfoId",
        ns_name: str,
        *,
        config_overrides: Optional[tnbClientConfig] = None,
        ns_description: Optional[str] = None,
        tags: Optional["capo_tnb.types.tag_map.TagMap"] = None,
    ) -> "capo_tnb.types.create_sol_network_instance_output.CreateSolNetworkInstanceOutput":
        """<p>Creates a network instance.</p> <p>A network instance is a single network created in Amazon Web Services TNB that can be deployed and on which life-cycle operations (like terminate, update, and delete) can be performed. Creating a network instance is the third step after creating a network package. For more information about network instances, <a href="https://docs.aws.amazon.com/tnb/latest/ug/network-instances.html">Network instances</a> in the <i>Amazon Web Services Telco Network Builder User Guide</i>.</p> <p>Once you create a network instance, you can instantiate it. To instantiate a network, see <a href="https://docs.aws.amazon.com/tnb/latest/APIReference/API_InstantiateSolNetworkInstance.html">InstantiateSolNetworkInstance</a>.</p>

        Args:
            nsd_info_id: <p>ID for network service descriptor.</p>
            ns_name: <p>Network instance name.</p>
            ns_description: <p>Network instance description.</p>
            tags: <p>A tag is a label that you assign to an Amazon Web Services resource. Each tag consists of a key and an optional value. You can use tags to search and filter your resources or track your Amazon Web Services costs.</p>

        Raises:
            capo_tnb.errors.access_denied_exception.AccessDeniedException: <p>Insufficient permissions to make request.</p>
            capo_tnb.errors.internal_server_exception.InternalServerException: <p>Unexpected error occurred. Problem on the server.</p>
            capo_tnb.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource that doesn't exist.</p>
            capo_tnb.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Service quotas have been exceeded.</p>
            capo_tnb.errors.throttling_exception.ThrottlingException: <p>Exception caused by throttling.</p>
            capo_tnb.errors.validation_exception.ValidationException: <p>Unable to process the request because the client provided input failed to satisfy request constraints.</p>
            capo_tnb.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Create a Sol Network Instance

            >>> client.create_sol_network_instance(nsd_info_id='np-0d5b823eb5c2a9241', ns_name='CITY Instance', ns_description='Test network for CITY', tags={'Name': 'Resource'})
        """

        def _handler(
            req: "OperationRequest[capo_tnb.types.create_sol_network_instance_input.CreateSolNetworkInstanceInput]",
        ) -> OperationResponse[
            "capo_tnb.types.create_sol_network_instance_output.CreateSolNetworkInstanceOutput"
        ]:
            import capo_tnb._operations.tnb.create_sol_network_instance

            output, http_response = (
                capo_tnb._operations.tnb.create_sol_network_instance.create_sol_network_instance(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_tnb.types.create_sol_network_instance_input.CreateSolNetworkInstanceInput = {
            "nsd_info_id": nsd_info_id,
            "ns_name": ns_name,
        }
        if ns_description is not None:
            input_["ns_description"] = ns_description
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_sol_network_package(
        self,
        *,
        config_overrides: Optional[tnbClientConfig] = None,
        tags: Optional["capo_tnb.types.tag_map.TagMap"] = None,
    ) -> (
        "capo_tnb.types.create_sol_network_package_output.CreateSolNetworkPackageOutput"
    ):
        """<p>Creates a network package.</p> <p>A network package is a .zip file in CSAR (Cloud Service Archive) format defines the function packages you want to deploy and the Amazon Web Services infrastructure you want to deploy them on. For more information, see <a href="https://docs.aws.amazon.com/tnb/latest/ug/network-instances.html">Network instances</a> in the <i>Amazon Web Services Telco Network Builder User Guide</i>. </p> <p>A network package consists of a network service descriptor (NSD) file (required) and any additional files (optional), such as scripts specific to your needs. For example, if you have multiple function packages in your network package, you can use the NSD to define which network functions should run in certain VPCs, subnets, or EKS clusters.</p> <p>This request creates an empty network package container with an ID. Once you create a network package, you can upload the network package content using <a href="https://docs.aws.amazon.com/tnb/latest/APIReference/API_PutSolNetworkPackageContent.html">PutSolNetworkPackageContent</a>.</p>

        Args:
            tags: <p>A tag is a label that you assign to an Amazon Web Services resource. Each tag consists of a key and an optional value. You can use tags to search and filter your resources or track your Amazon Web Services costs.</p>

        Raises:
            capo_tnb.errors.access_denied_exception.AccessDeniedException: <p>Insufficient permissions to make request.</p>
            capo_tnb.errors.internal_server_exception.InternalServerException: <p>Unexpected error occurred. Problem on the server.</p>
            capo_tnb.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Service quotas have been exceeded.</p>
            capo_tnb.errors.throttling_exception.ThrottlingException: <p>Exception caused by throttling.</p>
            capo_tnb.errors.validation_exception.ValidationException: <p>Unable to process the request because the client provided input failed to satisfy request constraints.</p>
            capo_tnb.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Create a Sol network package

            >>> client.create_sol_network_package(tags={'Name': 'Resource'})
        """

        def _handler(
            req: "OperationRequest[capo_tnb.types.create_sol_network_package_input.CreateSolNetworkPackageInput]",
        ) -> OperationResponse[
            "capo_tnb.types.create_sol_network_package_output.CreateSolNetworkPackageOutput"
        ]:
            import capo_tnb._operations.tnb.create_sol_network_package

            output, http_response = (
                capo_tnb._operations.tnb.create_sol_network_package.create_sol_network_package(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_tnb.types.create_sol_network_package_input.CreateSolNetworkPackageInput = {}
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_sol_function_package(
        self,
        vnf_pkg_id: "capo_tnb.types.vnf_pkg_id.VnfPkgId",
        *,
        config_overrides: Optional[tnbClientConfig] = None,
    ) -> None:
        """<p>Deletes a function package.</p> <p>A function package is a .zip file in CSAR (Cloud Service Archive) format that contains a network function (an ETSI standard telecommunication application) and function package descriptor that uses the TOSCA standard to describe how the network functions should run on your network.</p> <p>To delete a function package, the package must be in a disabled state. To disable a function package, see <a href="https://docs.aws.amazon.com/tnb/latest/APIReference/API_UpdateSolFunctionPackage.html">UpdateSolFunctionPackage</a>. </p>

        Args:
            vnf_pkg_id: <p>ID of the function package.</p>

        Raises:
            capo_tnb.errors.access_denied_exception.AccessDeniedException: <p>Insufficient permissions to make request.</p>
            capo_tnb.errors.internal_server_exception.InternalServerException: <p>Unexpected error occurred. Problem on the server.</p>
            capo_tnb.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource that doesn't exist.</p>
            capo_tnb.errors.throttling_exception.ThrottlingException: <p>Exception caused by throttling.</p>
            capo_tnb.errors.validation_exception.ValidationException: <p>Unable to process the request because the client provided input failed to satisfy request constraints.</p>
            capo_tnb.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Delete a function package

            >>> client.delete_sol_function_package(vnf_pkg_id='fp-07aa863e53460a2a6')
        """

        def _handler(
            req: "OperationRequest[capo_tnb.types.delete_sol_function_package_input.DeleteSolFunctionPackageInput]",
        ) -> OperationResponse[None]:
            import capo_tnb._operations.tnb.delete_sol_function_package

            output, http_response = (
                capo_tnb._operations.tnb.delete_sol_function_package.delete_sol_function_package(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_tnb.types.delete_sol_function_package_input.DeleteSolFunctionPackageInput = {
            "vnf_pkg_id": vnf_pkg_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_sol_network_instance(
        self,
        ns_instance_id: "capo_tnb.types.ns_instance_id.NsInstanceId",
        *,
        config_overrides: Optional[tnbClientConfig] = None,
    ) -> None:
        """<p>Deletes a network instance.</p> <p>A network instance is a single network created in Amazon Web Services TNB that can be deployed and on which life-cycle operations (like terminate, update, and delete) can be performed.</p> <p>To delete a network instance, the instance must be in a stopped or terminated state. To terminate a network instance, see <a href="https://docs.aws.amazon.com/tnb/latest/APIReference/API_TerminateSolNetworkInstance.html">TerminateSolNetworkInstance</a>.</p>

        Args:
            ns_instance_id: <p>Network instance ID.</p>

        Raises:
            capo_tnb.errors.access_denied_exception.AccessDeniedException: <p>Insufficient permissions to make request.</p>
            capo_tnb.errors.internal_server_exception.InternalServerException: <p>Unexpected error occurred. Problem on the server.</p>
            capo_tnb.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource that doesn't exist.</p>
            capo_tnb.errors.throttling_exception.ThrottlingException: <p>Exception caused by throttling.</p>
            capo_tnb.errors.validation_exception.ValidationException: <p>Unable to process the request because the client provided input failed to satisfy request constraints.</p>
            capo_tnb.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Delete a Sol Network Instance.

            >>> client.delete_sol_network_instance(ns_instance_id='ni-07aa863e53460a2a6')
        """

        def _handler(
            req: "OperationRequest[capo_tnb.types.delete_sol_network_instance_input.DeleteSolNetworkInstanceInput]",
        ) -> OperationResponse[None]:
            import capo_tnb._operations.tnb.delete_sol_network_instance

            output, http_response = (
                capo_tnb._operations.tnb.delete_sol_network_instance.delete_sol_network_instance(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_tnb.types.delete_sol_network_instance_input.DeleteSolNetworkInstanceInput = {
            "ns_instance_id": ns_instance_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_sol_network_package(
        self,
        nsd_info_id: "capo_tnb.types.nsd_info_id.NsdInfoId",
        *,
        config_overrides: Optional[tnbClientConfig] = None,
    ) -> None:
        """<p>Deletes network package.</p> <p>A network package is a .zip file in CSAR (Cloud Service Archive) format defines the function packages you want to deploy and the Amazon Web Services infrastructure you want to deploy them on.</p> <p>To delete a network package, the package must be in a disable state. To disable a network package, see <a href="https://docs.aws.amazon.com/tnb/latest/APIReference/API_UpdateSolNetworkPackage.html">UpdateSolNetworkPackage</a>.</p>

        Args:
            nsd_info_id: <p>ID of the network service descriptor in the network package.</p>

        Raises:
            capo_tnb.errors.access_denied_exception.AccessDeniedException: <p>Insufficient permissions to make request.</p>
            capo_tnb.errors.internal_server_exception.InternalServerException: <p>Unexpected error occurred. Problem on the server.</p>
            capo_tnb.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource that doesn't exist.</p>
            capo_tnb.errors.throttling_exception.ThrottlingException: <p>Exception caused by throttling.</p>
            capo_tnb.errors.validation_exception.ValidationException: <p>Unable to process the request because the client provided input failed to satisfy request constraints.</p>
            capo_tnb.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Delete a Sol network package

            >>> client.delete_sol_network_package(nsd_info_id='np-0d5b823eb5c2a9241')
        """

        def _handler(
            req: "OperationRequest[capo_tnb.types.delete_sol_network_package_input.DeleteSolNetworkPackageInput]",
        ) -> OperationResponse[None]:
            import capo_tnb._operations.tnb.delete_sol_network_package

            output, http_response = (
                capo_tnb._operations.tnb.delete_sol_network_package.delete_sol_network_package(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_tnb.types.delete_sol_network_package_input.DeleteSolNetworkPackageInput = {
            "nsd_info_id": nsd_info_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_sol_function_instance(
        self,
        vnf_instance_id: "capo_tnb.types.vnf_instance_id.VnfInstanceId",
        *,
        config_overrides: Optional[tnbClientConfig] = None,
    ) -> "capo_tnb.types.get_sol_function_instance_output.GetSolFunctionInstanceOutput":
        """<p>Gets the details of a network function instance, including the instantiation state and metadata from the function package descriptor in the network function package.</p> <p>A network function instance is a function in a function package .</p>

        Args:
            vnf_instance_id: <p>ID of the network function.</p>

        Raises:
            capo_tnb.errors.access_denied_exception.AccessDeniedException: <p>Insufficient permissions to make request.</p>
            capo_tnb.errors.internal_server_exception.InternalServerException: <p>Unexpected error occurred. Problem on the server.</p>
            capo_tnb.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource that doesn't exist.</p>
            capo_tnb.errors.throttling_exception.ThrottlingException: <p>Exception caused by throttling.</p>
            capo_tnb.errors.validation_exception.ValidationException: <p>Unable to process the request because the client provided input failed to satisfy request constraints.</p>
            capo_tnb.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Get a Sol Network Function Instance details

            >>> client.get_sol_function_instance(vnf_instance_id='fi-b9439c34c1ef86c54')
        """

        def _handler(
            req: "OperationRequest[capo_tnb.types.get_sol_function_instance_input.GetSolFunctionInstanceInput]",
        ) -> OperationResponse[
            "capo_tnb.types.get_sol_function_instance_output.GetSolFunctionInstanceOutput"
        ]:
            import capo_tnb._operations.tnb.get_sol_function_instance

            output, http_response = (
                capo_tnb._operations.tnb.get_sol_function_instance.get_sol_function_instance(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_tnb.types.get_sol_function_instance_input.GetSolFunctionInstanceInput = {
            "vnf_instance_id": vnf_instance_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_sol_function_package(
        self,
        vnf_pkg_id: "capo_tnb.types.vnf_pkg_id.VnfPkgId",
        *,
        config_overrides: Optional[tnbClientConfig] = None,
    ) -> "capo_tnb.types.get_sol_function_package_output.GetSolFunctionPackageOutput":
        """<p>Gets the details of an individual function package, such as the operational state and whether the package is in use.</p> <p>A function package is a .zip file in CSAR (Cloud Service Archive) format that contains a network function (an ETSI standard telecommunication application) and function package descriptor that uses the TOSCA standard to describe how the network functions should run on your network..</p>

        Args:
            vnf_pkg_id: <p>ID of the function package.</p>

        Raises:
            capo_tnb.errors.access_denied_exception.AccessDeniedException: <p>Insufficient permissions to make request.</p>
            capo_tnb.errors.internal_server_exception.InternalServerException: <p>Unexpected error occurred. Problem on the server.</p>
            capo_tnb.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource that doesn't exist.</p>
            capo_tnb.errors.throttling_exception.ThrottlingException: <p>Exception caused by throttling.</p>
            capo_tnb.errors.validation_exception.ValidationException: <p>Unable to process the request because the client provided input failed to satisfy request constraints.</p>
            capo_tnb.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Describe a function package with correct vnfPkgId

            >>> client.get_sol_function_package(vnf_pkg_id='fp-07aa863e53460a2a6')
        """

        def _handler(
            req: "OperationRequest[capo_tnb.types.get_sol_function_package_input.GetSolFunctionPackageInput]",
        ) -> OperationResponse[
            "capo_tnb.types.get_sol_function_package_output.GetSolFunctionPackageOutput"
        ]:
            import capo_tnb._operations.tnb.get_sol_function_package

            output, http_response = (
                capo_tnb._operations.tnb.get_sol_function_package.get_sol_function_package(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_tnb.types.get_sol_function_package_input.GetSolFunctionPackageInput = {
            "vnf_pkg_id": vnf_pkg_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_sol_function_package_content(
        self,
        vnf_pkg_id: "capo_tnb.types.vnf_pkg_id.VnfPkgId",
        accept: "capo_tnb.types.package_content_type.PackageContentType",
        *,
        config_overrides: Optional[tnbClientConfig] = None,
    ) -> "capo_tnb.types.get_sol_function_package_content_output.GetSolFunctionPackageContentOutput":
        """<p>Gets the contents of a function package.</p> <p>A function package is a .zip file in CSAR (Cloud Service Archive) format that contains a network function (an ETSI standard telecommunication application) and function package descriptor that uses the TOSCA standard to describe how the network functions should run on your network.</p>

        Args:
            vnf_pkg_id: <p>ID of the function package.</p>
            accept: <p>The format of the package that you want to download from the function packages.</p>

        Raises:
            capo_tnb.errors.access_denied_exception.AccessDeniedException: <p>Insufficient permissions to make request.</p>
            capo_tnb.errors.internal_server_exception.InternalServerException: <p>Unexpected error occurred. Problem on the server.</p>
            capo_tnb.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource that doesn't exist.</p>
            capo_tnb.errors.throttling_exception.ThrottlingException: <p>Exception caused by throttling.</p>
            capo_tnb.errors.validation_exception.ValidationException: <p>Unable to process the request because the client provided input failed to satisfy request constraints.</p>
            capo_tnb.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Get the content of a function package

            >>> client.get_sol_function_package_content(accept='application/zip', vnf_pkg_id='fp-07aa863e53460a2a6')
        """

        def _handler(
            req: "OperationRequest[capo_tnb.types.get_sol_function_package_content_input.GetSolFunctionPackageContentInput]",
        ) -> OperationResponse[
            "capo_tnb.types.get_sol_function_package_content_output.GetSolFunctionPackageContentOutput"
        ]:
            import capo_tnb._operations.tnb.get_sol_function_package_content

            output, http_response = (
                capo_tnb._operations.tnb.get_sol_function_package_content.get_sol_function_package_content(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_tnb.types.get_sol_function_package_content_input.GetSolFunctionPackageContentInput = {
            "vnf_pkg_id": vnf_pkg_id,
            "accept": accept,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_sol_function_package_descriptor(
        self,
        vnf_pkg_id: "capo_tnb.types.vnf_pkg_id.VnfPkgId",
        accept: "capo_tnb.types.descriptor_content_type.DescriptorContentType",
        *,
        config_overrides: Optional[tnbClientConfig] = None,
    ) -> "capo_tnb.types.get_sol_function_package_descriptor_output.GetSolFunctionPackageDescriptorOutput":
        """<p>Gets a function package descriptor in a function package.</p> <p>A function package descriptor is a .yaml file in a function package that uses the TOSCA standard to describe how the network function in the function package should run on your network.</p> <p>A function package is a .zip file in CSAR (Cloud Service Archive) format that contains a network function (an ETSI standard telecommunication application) and function package descriptor that uses the TOSCA standard to describe how the network functions should run on your network.</p>

        Args:
            vnf_pkg_id: <p>ID of the function package.</p>
            accept: <p>Indicates which content types, expressed as MIME types, the client is able to understand.</p>

        Raises:
            capo_tnb.errors.access_denied_exception.AccessDeniedException: <p>Insufficient permissions to make request.</p>
            capo_tnb.errors.internal_server_exception.InternalServerException: <p>Unexpected error occurred. Problem on the server.</p>
            capo_tnb.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource that doesn't exist.</p>
            capo_tnb.errors.throttling_exception.ThrottlingException: <p>Exception caused by throttling.</p>
            capo_tnb.errors.validation_exception.ValidationException: <p>Unable to process the request because the client provided input failed to satisfy request constraints.</p>
            capo_tnb.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Get the descriptor of a function package

            >>> client.get_sol_function_package_descriptor(accept='text/plain', vnf_pkg_id='fp-07aa863e53460a2a6')
        """

        def _handler(
            req: "OperationRequest[capo_tnb.types.get_sol_function_package_descriptor_input.GetSolFunctionPackageDescriptorInput]",
        ) -> OperationResponse[
            "capo_tnb.types.get_sol_function_package_descriptor_output.GetSolFunctionPackageDescriptorOutput"
        ]:
            import capo_tnb._operations.tnb.get_sol_function_package_descriptor

            output, http_response = (
                capo_tnb._operations.tnb.get_sol_function_package_descriptor.get_sol_function_package_descriptor(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_tnb.types.get_sol_function_package_descriptor_input.GetSolFunctionPackageDescriptorInput = {
            "vnf_pkg_id": vnf_pkg_id,
            "accept": accept,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_sol_network_instance(
        self,
        ns_instance_id: "capo_tnb.types.ns_instance_id.NsInstanceId",
        *,
        config_overrides: Optional[tnbClientConfig] = None,
    ) -> "capo_tnb.types.get_sol_network_instance_output.GetSolNetworkInstanceOutput":
        """<p>Gets the details of the network instance.</p> <p>A network instance is a single network created in Amazon Web Services TNB that can be deployed and on which life-cycle operations (like terminate, update, and delete) can be performed.</p>

        Args:
            ns_instance_id: <p>ID of the network instance.</p>

        Raises:
            capo_tnb.errors.access_denied_exception.AccessDeniedException: <p>Insufficient permissions to make request.</p>
            capo_tnb.errors.internal_server_exception.InternalServerException: <p>Unexpected error occurred. Problem on the server.</p>
            capo_tnb.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource that doesn't exist.</p>
            capo_tnb.errors.throttling_exception.ThrottlingException: <p>Exception caused by throttling.</p>
            capo_tnb.errors.validation_exception.ValidationException: <p>Unable to process the request because the client provided input failed to satisfy request constraints.</p>
            capo_tnb.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Get a Sol Network Instance details

            >>> client.get_sol_network_instance(ns_instance_id='ni-07aa863e53460a2a6')
        """

        def _handler(
            req: "OperationRequest[capo_tnb.types.get_sol_network_instance_input.GetSolNetworkInstanceInput]",
        ) -> OperationResponse[
            "capo_tnb.types.get_sol_network_instance_output.GetSolNetworkInstanceOutput"
        ]:
            import capo_tnb._operations.tnb.get_sol_network_instance

            output, http_response = (
                capo_tnb._operations.tnb.get_sol_network_instance.get_sol_network_instance(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_tnb.types.get_sol_network_instance_input.GetSolNetworkInstanceInput = {
            "ns_instance_id": ns_instance_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_sol_network_operation(
        self,
        ns_lcm_op_occ_id: "capo_tnb.types.ns_lcm_op_occ_id.NsLcmOpOccId",
        *,
        config_overrides: Optional[tnbClientConfig] = None,
    ) -> "capo_tnb.types.get_sol_network_operation_output.GetSolNetworkOperationOutput":
        """<p>Gets the details of a network operation, including the tasks involved in the network operation and the status of the tasks.</p> <p>A network operation is any operation that is done to your network, such as network instance instantiation or termination.</p>

        Args:
            ns_lcm_op_occ_id: <p>The identifier of the network operation.</p>

        Raises:
            capo_tnb.errors.access_denied_exception.AccessDeniedException: <p>Insufficient permissions to make request.</p>
            capo_tnb.errors.internal_server_exception.InternalServerException: <p>Unexpected error occurred. Problem on the server.</p>
            capo_tnb.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource that doesn't exist.</p>
            capo_tnb.errors.throttling_exception.ThrottlingException: <p>Exception caused by throttling.</p>
            capo_tnb.errors.validation_exception.ValidationException: <p>Unable to process the request because the client provided input failed to satisfy request constraints.</p>
            capo_tnb.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Get Sol Network Instantiate operation

            >>> client.get_sol_network_operation(ns_lcm_op_occ_id='no-0d5b823eb5c2a9241')
            Get Sol Network Update operation

            >>> client.get_sol_network_operation(ns_lcm_op_occ_id='no-0d5b823eb5c2a9241')
            Get Sol Network Update operation

            >>> client.get_sol_network_operation(ns_lcm_op_occ_id='no-0d5b823eb5c2a9241')
            Get Sol Network Instantiate operation which has a failure

            >>> client.get_sol_network_operation(ns_lcm_op_occ_id='no-0d5b823eb5c2a9241')
        """

        def _handler(
            req: "OperationRequest[capo_tnb.types.get_sol_network_operation_input.GetSolNetworkOperationInput]",
        ) -> OperationResponse[
            "capo_tnb.types.get_sol_network_operation_output.GetSolNetworkOperationOutput"
        ]:
            import capo_tnb._operations.tnb.get_sol_network_operation

            output, http_response = (
                capo_tnb._operations.tnb.get_sol_network_operation.get_sol_network_operation(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_tnb.types.get_sol_network_operation_input.GetSolNetworkOperationInput = {
            "ns_lcm_op_occ_id": ns_lcm_op_occ_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_sol_network_package(
        self,
        nsd_info_id: "capo_tnb.types.nsd_info_id.NsdInfoId",
        *,
        config_overrides: Optional[tnbClientConfig] = None,
    ) -> "capo_tnb.types.get_sol_network_package_output.GetSolNetworkPackageOutput":
        """<p>Gets the details of a network package.</p> <p>A network package is a .zip file in CSAR (Cloud Service Archive) format defines the function packages you want to deploy and the Amazon Web Services infrastructure you want to deploy them on.</p>

        Args:
            nsd_info_id: <p>ID of the network service descriptor in the network package.</p>

        Raises:
            capo_tnb.errors.access_denied_exception.AccessDeniedException: <p>Insufficient permissions to make request.</p>
            capo_tnb.errors.internal_server_exception.InternalServerException: <p>Unexpected error occurred. Problem on the server.</p>
            capo_tnb.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource that doesn't exist.</p>
            capo_tnb.errors.throttling_exception.ThrottlingException: <p>Exception caused by throttling.</p>
            capo_tnb.errors.validation_exception.ValidationException: <p>Unable to process the request because the client provided input failed to satisfy request constraints.</p>
            capo_tnb.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Describe an individual Sol network package

            >>> client.get_sol_network_package(nsd_info_id='np-0d5b823eb5c2a9241')
        """

        def _handler(
            req: "OperationRequest[capo_tnb.types.get_sol_network_package_input.GetSolNetworkPackageInput]",
        ) -> OperationResponse[
            "capo_tnb.types.get_sol_network_package_output.GetSolNetworkPackageOutput"
        ]:
            import capo_tnb._operations.tnb.get_sol_network_package

            output, http_response = (
                capo_tnb._operations.tnb.get_sol_network_package.get_sol_network_package(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_tnb.types.get_sol_network_package_input.GetSolNetworkPackageInput = {
            "nsd_info_id": nsd_info_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_sol_network_package_content(
        self,
        nsd_info_id: "capo_tnb.types.nsd_info_id.NsdInfoId",
        accept: "capo_tnb.types.package_content_type.PackageContentType",
        *,
        config_overrides: Optional[tnbClientConfig] = None,
    ) -> "capo_tnb.types.get_sol_network_package_content_output.GetSolNetworkPackageContentOutput":
        """<p>Gets the contents of a network package.</p> <p>A network package is a .zip file in CSAR (Cloud Service Archive) format defines the function packages you want to deploy and the Amazon Web Services infrastructure you want to deploy them on.</p>

        Args:
            nsd_info_id: <p>ID of the network service descriptor in the network package.</p>
            accept: <p>The format of the package you want to download from the network package.</p>

        Raises:
            capo_tnb.errors.access_denied_exception.AccessDeniedException: <p>Insufficient permissions to make request.</p>
            capo_tnb.errors.internal_server_exception.InternalServerException: <p>Unexpected error occurred. Problem on the server.</p>
            capo_tnb.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource that doesn't exist.</p>
            capo_tnb.errors.throttling_exception.ThrottlingException: <p>Exception caused by throttling.</p>
            capo_tnb.errors.validation_exception.ValidationException: <p>Unable to process the request because the client provided input failed to satisfy request constraints.</p>
            capo_tnb.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Get a network package Content

            >>> client.get_sol_network_package_content(accept='application/zip', nsd_info_id='np-0d5b823eb5c2a9241')
        """

        def _handler(
            req: "OperationRequest[capo_tnb.types.get_sol_network_package_content_input.GetSolNetworkPackageContentInput]",
        ) -> OperationResponse[
            "capo_tnb.types.get_sol_network_package_content_output.GetSolNetworkPackageContentOutput"
        ]:
            import capo_tnb._operations.tnb.get_sol_network_package_content

            output, http_response = (
                capo_tnb._operations.tnb.get_sol_network_package_content.get_sol_network_package_content(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_tnb.types.get_sol_network_package_content_input.GetSolNetworkPackageContentInput = {
            "nsd_info_id": nsd_info_id,
            "accept": accept,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_sol_network_package_descriptor(
        self,
        nsd_info_id: "capo_tnb.types.nsd_info_id.NsdInfoId",
        *,
        config_overrides: Optional[tnbClientConfig] = None,
    ) -> "capo_tnb.types.get_sol_network_package_descriptor_output.GetSolNetworkPackageDescriptorOutput":
        """<p>Gets the content of the network service descriptor.</p> <p>A network service descriptor is a .yaml file in a network package that uses the TOSCA standard to describe the network functions you want to deploy and the Amazon Web Services infrastructure you want to deploy the network functions on.</p>

        Args:
            nsd_info_id: <p>ID of the network service descriptor in the network package.</p>

        Raises:
            capo_tnb.errors.access_denied_exception.AccessDeniedException: <p>Insufficient permissions to make request.</p>
            capo_tnb.errors.internal_server_exception.InternalServerException: <p>Unexpected error occurred. Problem on the server.</p>
            capo_tnb.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource that doesn't exist.</p>
            capo_tnb.errors.throttling_exception.ThrottlingException: <p>Exception caused by throttling.</p>
            capo_tnb.errors.validation_exception.ValidationException: <p>Unable to process the request because the client provided input failed to satisfy request constraints.</p>
            capo_tnb.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Get the descriptor of a Network Pacakge

            >>> client.get_sol_network_package_descriptor(nsd_info_id='np-0d5b823eb5c2a9241')
        """

        def _handler(
            req: "OperationRequest[capo_tnb.types.get_sol_network_package_descriptor_input.GetSolNetworkPackageDescriptorInput]",
        ) -> OperationResponse[
            "capo_tnb.types.get_sol_network_package_descriptor_output.GetSolNetworkPackageDescriptorOutput"
        ]:
            import capo_tnb._operations.tnb.get_sol_network_package_descriptor

            output, http_response = (
                capo_tnb._operations.tnb.get_sol_network_package_descriptor.get_sol_network_package_descriptor(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_tnb.types.get_sol_network_package_descriptor_input.GetSolNetworkPackageDescriptorInput = {
            "nsd_info_id": nsd_info_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def instantiate_sol_network_instance(
        self,
        ns_instance_id: "capo_tnb.types.ns_instance_id.NsInstanceId",
        *,
        config_overrides: Optional[tnbClientConfig] = None,
        dry_run: Optional[bool] = None,
        additional_params_for_ns: Optional[object] = None,
        tags: Optional["capo_tnb.types.tag_map.TagMap"] = None,
    ) -> "capo_tnb.types.instantiate_sol_network_instance_output.InstantiateSolNetworkInstanceOutput":
        """<p>Instantiates a network instance.</p> <p>A network instance is a single network created in Amazon Web Services TNB that can be deployed and on which life-cycle operations (like terminate, update, and delete) can be performed.</p> <p>Before you can instantiate a network instance, you have to create a network instance. For more information, see <a href="https://docs.aws.amazon.com/tnb/latest/APIReference/API_CreateSolNetworkInstance.html">CreateSolNetworkInstance</a>.</p>

        Args:
            ns_instance_id: <p>ID of the network instance.</p>
            dry_run: <p>A check for whether you have the required permissions for the action without actually making the request and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>
            additional_params_for_ns: <p>Provides values for the configurable properties.</p>
            tags: <p>A tag is a label that you assign to an Amazon Web Services resource. Each tag consists of a key and an optional value. When you use this API, the tags are only applied to the network operation that is created. These tags are not applied to the network instance. Use tags to search and filter your resources or track your Amazon Web Services costs.</p>

        Raises:
            capo_tnb.errors.access_denied_exception.AccessDeniedException: <p>Insufficient permissions to make request.</p>
            capo_tnb.errors.internal_server_exception.InternalServerException: <p>Unexpected error occurred. Problem on the server.</p>
            capo_tnb.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource that doesn't exist.</p>
            capo_tnb.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Service quotas have been exceeded.</p>
            capo_tnb.errors.throttling_exception.ThrottlingException: <p>Exception caused by throttling.</p>
            capo_tnb.errors.validation_exception.ValidationException: <p>Unable to process the request because the client provided input failed to satisfy request constraints.</p>
            capo_tnb.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Instantiate a Sol Network Instance

            >>> client.instantiate_sol_network_instance(ns_instance_id='ni-0d5b823eb5c2a9241', tags={'Name': 'Resource'})
            Instantiate a Sol Network Instance with Overrides

            >>> client.instantiate_sol_network_instance(ns_instance_id='ni-0d5b823eb5c2a9241', additional_params_for_ns={'cidr_block': '10.0.0.0/16', 'availability_zone': 'us-west-2a'})
        """

        def _handler(
            req: "OperationRequest[capo_tnb.types.instantiate_sol_network_instance_input.InstantiateSolNetworkInstanceInput]",
        ) -> OperationResponse[
            "capo_tnb.types.instantiate_sol_network_instance_output.InstantiateSolNetworkInstanceOutput"
        ]:
            import capo_tnb._operations.tnb.instantiate_sol_network_instance

            output, http_response = (
                capo_tnb._operations.tnb.instantiate_sol_network_instance.instantiate_sol_network_instance(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_tnb.types.instantiate_sol_network_instance_input.InstantiateSolNetworkInstanceInput = {
            "ns_instance_id": ns_instance_id
        }
        if dry_run is not None:
            input_["dry_run"] = dry_run
        if additional_params_for_ns is not None:
            input_["additional_params_for_ns"] = additional_params_for_ns
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_sol_function_instances(
        self,
        *,
        config_overrides: Optional[tnbClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional["capo_tnb.types.pagination_token.PaginationToken"] = None,
    ) -> "capo_tnb.types.list_sol_function_instances_output.ListSolFunctionInstancesOutput":
        """<p>Lists network function instances.</p> <p>A network function instance is a function in a function package .</p>

        Args:
            max_results: <p>The maximum number of results to include in the response.</p>
            next_token: <p>The token for the next page of results.</p>

        Raises:
            capo_tnb.errors.access_denied_exception.AccessDeniedException: <p>Insufficient permissions to make request.</p>
            capo_tnb.errors.internal_server_exception.InternalServerException: <p>Unexpected error occurred. Problem on the server.</p>
            capo_tnb.errors.throttling_exception.ThrottlingException: <p>Exception caused by throttling.</p>
            capo_tnb.errors.validation_exception.ValidationException: <p>Unable to process the request because the client provided input failed to satisfy request constraints.</p>
            capo_tnb.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            List Sol Function instances

            >>> client.list_sol_function_instances()
            List Sol Function Instances with nextToken and maxResults

            >>> client.list_sol_function_instances(max_results=25, next_token='')
        """

        def _handler(
            req: "OperationRequest[capo_tnb.types.list_sol_function_instances_input.ListSolFunctionInstancesInput]",
        ) -> OperationResponse[
            "capo_tnb.types.list_sol_function_instances_output.ListSolFunctionInstancesOutput"
        ]:
            import capo_tnb._operations.tnb.list_sol_function_instances

            output, http_response = (
                capo_tnb._operations.tnb.list_sol_function_instances.list_sol_function_instances(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_tnb.types.list_sol_function_instances_input.ListSolFunctionInstancesInput = {}
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

    def iter_list_sol_function_instances(
        self,
        *,
        config_overrides: Optional[tnbClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional["capo_tnb.types.pagination_token.PaginationToken"] = None,
    ) -> "Iterator[capo_tnb.types.list_sol_function_instance_info.ListSolFunctionInstanceInfo]":
        _token = next_token
        while True:
            _response = self.list_sol_function_instances(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("function_instances",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_sol_function_packages(
        self,
        *,
        config_overrides: Optional[tnbClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional["capo_tnb.types.pagination_token.PaginationToken"] = None,
    ) -> (
        "capo_tnb.types.list_sol_function_packages_output.ListSolFunctionPackagesOutput"
    ):
        """<p>Lists information about function packages.</p> <p>A function package is a .zip file in CSAR (Cloud Service Archive) format that contains a network function (an ETSI standard telecommunication application) and function package descriptor that uses the TOSCA standard to describe how the network functions should run on your network.</p>

        Args:
            max_results: <p>The maximum number of results to include in the response.</p>
            next_token: <p>The token for the next page of results.</p>

        Raises:
            capo_tnb.errors.access_denied_exception.AccessDeniedException: <p>Insufficient permissions to make request.</p>
            capo_tnb.errors.internal_server_exception.InternalServerException: <p>Unexpected error occurred. Problem on the server.</p>
            capo_tnb.errors.throttling_exception.ThrottlingException: <p>Exception caused by throttling.</p>
            capo_tnb.errors.validation_exception.ValidationException: <p>Unable to process the request because the client provided input failed to satisfy request constraints.</p>
            capo_tnb.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            List information about multiple function packages without PaginationToken

            >>> client.list_sol_function_packages(max_results=25, next_token='')
            List information about multiple function packages with PaginationToken

            >>> client.list_sol_function_packages(max_results=25, next_token='ug2E9SheCpyAmeLItmHF99a8GNI6yAHxXIvgBkdiA2ixKvqdhYpNBLWHDl6vGnWt7Y4CB6m1Dkz86gSwcDouMO1pSrN%2BlGY2kbNtfTeMgnuB6bmwP/UU12r7MkHQyPCWMYG8OuCXkDBOYeX8qjRDTJ5vxAyrwtynaB6XDNDZA2DscCjcD7kpNzf3xlPRCwd6')
            No more function packages to return

            >>> client.list_sol_function_packages(max_results=25, next_token='ug2E9SheCpyAmeLItmHF98uvZTosFhZ1wyglENkc3UZ12UuRLmtGtojRynFjRR5zW%2FycBL6QX8AU%2B1IRWL%2BVjNNL7KBiaD87KM9WcUMQzryLtOazGHexujJncJJ0YGsxSLSrmPGx7dM1EoNKX8oxYA%3D%3D')
        """

        def _handler(
            req: "OperationRequest[capo_tnb.types.list_sol_function_packages_input.ListSolFunctionPackagesInput]",
        ) -> OperationResponse[
            "capo_tnb.types.list_sol_function_packages_output.ListSolFunctionPackagesOutput"
        ]:
            import capo_tnb._operations.tnb.list_sol_function_packages

            output, http_response = (
                capo_tnb._operations.tnb.list_sol_function_packages.list_sol_function_packages(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_tnb.types.list_sol_function_packages_input.ListSolFunctionPackagesInput = {}
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

    def iter_list_sol_function_packages(
        self,
        *,
        config_overrides: Optional[tnbClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional["capo_tnb.types.pagination_token.PaginationToken"] = None,
    ) -> "Iterator[capo_tnb.types.list_sol_function_package_info.ListSolFunctionPackageInfo]":
        _token = next_token
        while True:
            _response = self.list_sol_function_packages(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("function_packages",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_sol_network_instances(
        self,
        *,
        config_overrides: Optional[tnbClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional["capo_tnb.types.pagination_token.PaginationToken"] = None,
    ) -> (
        "capo_tnb.types.list_sol_network_instances_output.ListSolNetworkInstancesOutput"
    ):
        """<p>Lists your network instances.</p> <p>A network instance is a single network created in Amazon Web Services TNB that can be deployed and on which life-cycle operations (like terminate, update, and delete) can be performed.</p>

        Args:
            max_results: <p>The maximum number of results to include in the response.</p>
            next_token: <p>The token for the next page of results.</p>

        Raises:
            capo_tnb.errors.access_denied_exception.AccessDeniedException: <p>Insufficient permissions to make request.</p>
            capo_tnb.errors.internal_server_exception.InternalServerException: <p>Unexpected error occurred. Problem on the server.</p>
            capo_tnb.errors.throttling_exception.ThrottlingException: <p>Exception caused by throttling.</p>
            capo_tnb.errors.validation_exception.ValidationException: <p>Unable to process the request because the client provided input failed to satisfy request constraints.</p>
            capo_tnb.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            List Sol Network Instantiate instances

            >>> client.list_sol_network_instances()
            List Sol Network Instances with nextToken and maxResults

            >>> client.list_sol_network_instances(max_results=25, next_token='')
        """

        def _handler(
            req: "OperationRequest[capo_tnb.types.list_sol_network_instances_input.ListSolNetworkInstancesInput]",
        ) -> OperationResponse[
            "capo_tnb.types.list_sol_network_instances_output.ListSolNetworkInstancesOutput"
        ]:
            import capo_tnb._operations.tnb.list_sol_network_instances

            output, http_response = (
                capo_tnb._operations.tnb.list_sol_network_instances.list_sol_network_instances(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_tnb.types.list_sol_network_instances_input.ListSolNetworkInstancesInput = {}
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

    def iter_list_sol_network_instances(
        self,
        *,
        config_overrides: Optional[tnbClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional["capo_tnb.types.pagination_token.PaginationToken"] = None,
    ) -> "Iterator[capo_tnb.types.list_sol_network_instance_info.ListSolNetworkInstanceInfo]":
        _token = next_token
        while True:
            _response = self.list_sol_network_instances(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("network_instances",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_sol_network_operations(
        self,
        *,
        config_overrides: Optional[tnbClientConfig] = None,
        ns_instance_id: Optional["capo_tnb.types.ns_instance_id.NsInstanceId"] = None,
        max_results: Optional[int] = None,
        next_token: Optional["capo_tnb.types.pagination_token.PaginationToken"] = None,
    ) -> "capo_tnb.types.list_sol_network_operations_output.ListSolNetworkOperationsOutput":
        """<p>Lists details for a network operation, including when the operation started and the status of the operation.</p> <p>A network operation is any operation that is done to your network, such as network instance instantiation or termination.</p>

        Args:
            ns_instance_id: <p>Network instance id filter, to retrieve network operations associated to a network instance.</p>
            max_results: <p>The maximum number of results to include in the response.</p>
            next_token: <p>The token for the next page of results.</p>

        Raises:
            capo_tnb.errors.access_denied_exception.AccessDeniedException: <p>Insufficient permissions to make request.</p>
            capo_tnb.errors.internal_server_exception.InternalServerException: <p>Unexpected error occurred. Problem on the server.</p>
            capo_tnb.errors.throttling_exception.ThrottlingException: <p>Exception caused by throttling.</p>
            capo_tnb.errors.validation_exception.ValidationException: <p>Unable to process the request because the client provided input failed to satisfy request constraints.</p>
            capo_tnb.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            List Sol Network Instantiate operations

            >>> client.list_sol_network_operations()
            List Sol Network Instantiate operations with nextToken and maxResults

            >>> client.list_sol_network_operations(max_results=25, next_token='')
            List Sol Network Update operations

            >>> client.list_sol_network_operations(ns_instance_id='ni-0d5b823eb5c2a9241')
            List Sol Network Update operations

            >>> client.list_sol_network_operations(ns_instance_id='ni-0d5b823eb5c2a9241')
        """

        def _handler(
            req: "OperationRequest[capo_tnb.types.list_sol_network_operations_input.ListSolNetworkOperationsInput]",
        ) -> OperationResponse[
            "capo_tnb.types.list_sol_network_operations_output.ListSolNetworkOperationsOutput"
        ]:
            import capo_tnb._operations.tnb.list_sol_network_operations

            output, http_response = (
                capo_tnb._operations.tnb.list_sol_network_operations.list_sol_network_operations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_tnb.types.list_sol_network_operations_input.ListSolNetworkOperationsInput = {}
        if ns_instance_id is not None:
            input_["ns_instance_id"] = ns_instance_id
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

    def iter_list_sol_network_operations(
        self,
        *,
        config_overrides: Optional[tnbClientConfig] = None,
        ns_instance_id: Optional["capo_tnb.types.ns_instance_id.NsInstanceId"] = None,
        max_results: Optional[int] = None,
        next_token: Optional["capo_tnb.types.pagination_token.PaginationToken"] = None,
    ) -> "Iterator[capo_tnb.types.list_sol_network_operations_info.ListSolNetworkOperationsInfo]":
        _token = next_token
        while True:
            _response = self.list_sol_network_operations(
                config_overrides=config_overrides,
                ns_instance_id=ns_instance_id,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("network_operations",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_sol_network_packages(
        self,
        *,
        config_overrides: Optional[tnbClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional["capo_tnb.types.pagination_token.PaginationToken"] = None,
    ) -> "capo_tnb.types.list_sol_network_packages_output.ListSolNetworkPackagesOutput":
        """<p>Lists network packages.</p> <p>A network package is a .zip file in CSAR (Cloud Service Archive) format defines the function packages you want to deploy and the Amazon Web Services infrastructure you want to deploy them on.</p>

        Args:
            max_results: <p>The maximum number of results to include in the response.</p>
            next_token: <p>The token for the next page of results.</p>

        Raises:
            capo_tnb.errors.access_denied_exception.AccessDeniedException: <p>Insufficient permissions to make request.</p>
            capo_tnb.errors.internal_server_exception.InternalServerException: <p>Unexpected error occurred. Problem on the server.</p>
            capo_tnb.errors.throttling_exception.ThrottlingException: <p>Exception caused by throttling.</p>
            capo_tnb.errors.validation_exception.ValidationException: <p>Unable to process the request because the client provided input failed to satisfy request constraints.</p>
            capo_tnb.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            List information about multiple network packages without PaginationToken

            >>> client.list_sol_network_packages(max_results=25, next_token='')
            List information about multiple network packages with PaginationToken

            >>> client.list_sol_network_packages(max_results=25, next_token='ug2E9SheCpyAmeLItmHF95t1rBBsFyzy5hsuauDTqaukll3AGHaTz%2B4utHS3OMuMcyKW6Hmk25aB6wtV%2BFxCx9Adw5fDSq9D8lVa6sr0Sq0BF7Fj0mYegd0a/XiFP4j/58ZIrtRl0M3Z55Z/wTqwIietXJVfFX84ZnIMjiEiFb3KIIdrKS8vSgMZ18t3Gj5p')
            No more network packages to return

            >>> client.list_sol_network_packages()
        """

        def _handler(
            req: "OperationRequest[capo_tnb.types.list_sol_network_packages_input.ListSolNetworkPackagesInput]",
        ) -> OperationResponse[
            "capo_tnb.types.list_sol_network_packages_output.ListSolNetworkPackagesOutput"
        ]:
            import capo_tnb._operations.tnb.list_sol_network_packages

            output, http_response = (
                capo_tnb._operations.tnb.list_sol_network_packages.list_sol_network_packages(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_tnb.types.list_sol_network_packages_input.ListSolNetworkPackagesInput = {}
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

    def iter_list_sol_network_packages(
        self,
        *,
        config_overrides: Optional[tnbClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional["capo_tnb.types.pagination_token.PaginationToken"] = None,
    ) -> "Iterator[capo_tnb.types.list_sol_network_package_info.ListSolNetworkPackageInfo]":
        _token = next_token
        while True:
            _response = self.list_sol_network_packages(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("network_packages",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_tags_for_resource(
        self,
        resource_arn: "capo_tnb.types.tnb_resource_arn.TNBResourceArn",
        *,
        config_overrides: Optional[tnbClientConfig] = None,
    ) -> "capo_tnb.types.list_tags_for_resource_output.ListTagsForResourceOutput":
        """<p>Lists tags for AWS TNB resources.</p>

        Args:
            resource_arn: <p>Resource ARN.</p>

        Raises:
            capo_tnb.errors.access_denied_exception.AccessDeniedException: <p>Insufficient permissions to make request.</p>
            capo_tnb.errors.internal_server_exception.InternalServerException: <p>Unexpected error occurred. Problem on the server.</p>
            capo_tnb.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource that doesn't exist.</p>
            capo_tnb.errors.throttling_exception.ThrottlingException: <p>Exception caused by throttling.</p>
            capo_tnb.errors.validation_exception.ValidationException: <p>Unable to process the request because the client provided input failed to satisfy request constraints.</p>
            capo_tnb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_tnb.types.list_tags_for_resource_input.ListTagsForResourceInput]",
        ) -> OperationResponse[
            "capo_tnb.types.list_tags_for_resource_output.ListTagsForResourceOutput"
        ]:
            import capo_tnb._operations.tnb.list_tags_for_resource

            output, http_response = (
                capo_tnb._operations.tnb.list_tags_for_resource.list_tags_for_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_tnb.types.list_tags_for_resource_input.ListTagsForResourceInput = {
            "resource_arn": resource_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def put_sol_function_package_content(
        self,
        vnf_pkg_id: "capo_tnb.types.vnf_pkg_id.VnfPkgId",
        file: "capo_tnb.types.sensitive_blob.SensitiveBlob",
        *,
        config_overrides: Optional[tnbClientConfig] = None,
        content_type: Optional[
            "capo_tnb.types.package_content_type.PackageContentType"
        ] = None,
    ) -> "capo_tnb.types.put_sol_function_package_content_output.PutSolFunctionPackageContentOutput":
        """<p>Uploads the contents of a function package.</p> <p>A function package is a .zip file in CSAR (Cloud Service Archive) format that contains a network function (an ETSI standard telecommunication application) and function package descriptor that uses the TOSCA standard to describe how the network functions should run on your network.</p>

        Args:
            vnf_pkg_id: <p>Function package ID.</p>
            content_type: <p>Function package content type.</p>
            file: <p>Function package file.</p>

        Raises:
            capo_tnb.errors.access_denied_exception.AccessDeniedException: <p>Insufficient permissions to make request.</p>
            capo_tnb.errors.internal_server_exception.InternalServerException: <p>Unexpected error occurred. Problem on the server.</p>
            capo_tnb.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource that doesn't exist.</p>
            capo_tnb.errors.throttling_exception.ThrottlingException: <p>Exception caused by throttling.</p>
            capo_tnb.errors.validation_exception.ValidationException: <p>Unable to process the request because the client provided input failed to satisfy request constraints.</p>
            capo_tnb.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Upload a function package content

            >>> client.put_sol_function_package_content(vnf_pkg_id='fp-07aa863e53460a2a6', content_type='application/zip', file='UEsDBBQAAAAAAPqLiVMAAAAAAAAAAAAAAAAMACAAZnJlZTVnYy1hbWYvVVQNAAcIrrJhBK')
        """

        def _handler(
            req: "OperationRequest[capo_tnb.types.put_sol_function_package_content_input.PutSolFunctionPackageContentInput]",
        ) -> OperationResponse[
            "capo_tnb.types.put_sol_function_package_content_output.PutSolFunctionPackageContentOutput"
        ]:
            import capo_tnb._operations.tnb.put_sol_function_package_content

            output, http_response = (
                capo_tnb._operations.tnb.put_sol_function_package_content.put_sol_function_package_content(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_tnb.types.put_sol_function_package_content_input.PutSolFunctionPackageContentInput = {
            "vnf_pkg_id": vnf_pkg_id,
            "file": file,
        }
        if content_type is not None:
            input_["content_type"] = content_type

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def put_sol_network_package_content(
        self,
        nsd_info_id: "capo_tnb.types.nsd_info_id.NsdInfoId",
        file: "capo_tnb.types.sensitive_blob.SensitiveBlob",
        *,
        config_overrides: Optional[tnbClientConfig] = None,
        content_type: Optional[
            "capo_tnb.types.package_content_type.PackageContentType"
        ] = None,
    ) -> "capo_tnb.types.put_sol_network_package_content_output.PutSolNetworkPackageContentOutput":
        """<p>Uploads the contents of a network package.</p> <p>A network package is a .zip file in CSAR (Cloud Service Archive) format defines the function packages you want to deploy and the Amazon Web Services infrastructure you want to deploy them on.</p>

        Args:
            nsd_info_id: <p>Network service descriptor info ID.</p>
            content_type: <p>Network package content type.</p>
            file: <p>Network package file.</p>

        Raises:
            capo_tnb.errors.access_denied_exception.AccessDeniedException: <p>Insufficient permissions to make request.</p>
            capo_tnb.errors.internal_server_exception.InternalServerException: <p>Unexpected error occurred. Problem on the server.</p>
            capo_tnb.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource that doesn't exist.</p>
            capo_tnb.errors.throttling_exception.ThrottlingException: <p>Exception caused by throttling.</p>
            capo_tnb.errors.validation_exception.ValidationException: <p>Unable to process the request because the client provided input failed to satisfy request constraints.</p>
            capo_tnb.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Upload the network package content of an NSD archive

            >>> client.put_sol_network_package_content(nsd_info_id='np-0d5b823eb5c2a9241', content_type='application/zip', file='UEsDBBQAAAAAAPqLiVMAAAAAAAAAAAAAA')
        """

        def _handler(
            req: "OperationRequest[capo_tnb.types.put_sol_network_package_content_input.PutSolNetworkPackageContentInput]",
        ) -> OperationResponse[
            "capo_tnb.types.put_sol_network_package_content_output.PutSolNetworkPackageContentOutput"
        ]:
            import capo_tnb._operations.tnb.put_sol_network_package_content

            output, http_response = (
                capo_tnb._operations.tnb.put_sol_network_package_content.put_sol_network_package_content(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_tnb.types.put_sol_network_package_content_input.PutSolNetworkPackageContentInput = {
            "nsd_info_id": nsd_info_id,
            "file": file,
        }
        if content_type is not None:
            input_["content_type"] = content_type

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def tag_resource(
        self,
        resource_arn: "capo_tnb.types.tnb_resource_arn.TNBResourceArn",
        tags: "capo_tnb.types.tag_map.TagMap",
        *,
        config_overrides: Optional[tnbClientConfig] = None,
    ) -> "capo_tnb.types.tag_resource_output.TagResourceOutput":
        """<p>Tags an AWS TNB resource.</p> <p>A tag is a label that you assign to an Amazon Web Services resource. Each tag consists of a key and an optional value. You can use tags to search and filter your resources or track your Amazon Web Services costs.</p>

        Args:
            resource_arn: <p>Resource ARN.</p>
            tags: <p>A tag is a label that you assign to an Amazon Web Services resource. Each tag consists of a key and an optional value. You can use tags to search and filter your resources or track your Amazon Web Services costs.</p>

        Raises:
            capo_tnb.errors.access_denied_exception.AccessDeniedException: <p>Insufficient permissions to make request.</p>
            capo_tnb.errors.internal_server_exception.InternalServerException: <p>Unexpected error occurred. Problem on the server.</p>
            capo_tnb.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource that doesn't exist.</p>
            capo_tnb.errors.throttling_exception.ThrottlingException: <p>Exception caused by throttling.</p>
            capo_tnb.errors.validation_exception.ValidationException: <p>Unable to process the request because the client provided input failed to satisfy request constraints.</p>
            capo_tnb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_tnb.types.tag_resource_input.TagResourceInput]",
        ) -> OperationResponse["capo_tnb.types.tag_resource_output.TagResourceOutput"]:
            import capo_tnb._operations.tnb.tag_resource

            output, http_response = capo_tnb._operations.tnb.tag_resource.tag_resource(
                req.options, req.input
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_tnb.types.tag_resource_input.TagResourceInput = {
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

    def terminate_sol_network_instance(
        self,
        ns_instance_id: "capo_tnb.types.ns_instance_id.NsInstanceId",
        *,
        config_overrides: Optional[tnbClientConfig] = None,
        tags: Optional["capo_tnb.types.tag_map.TagMap"] = None,
    ) -> "capo_tnb.types.terminate_sol_network_instance_output.TerminateSolNetworkInstanceOutput":
        """<p>Terminates a network instance.</p> <p>A network instance is a single network created in Amazon Web Services TNB that can be deployed and on which life-cycle operations (like terminate, update, and delete) can be performed.</p> <p>You must terminate a network instance before you can delete it.</p>

        Args:
            ns_instance_id: <p>ID of the network instance.</p>
            tags: <p>A tag is a label that you assign to an Amazon Web Services resource. Each tag consists of a key and an optional value. When you use this API, the tags are only applied to the network operation that is created. These tags are not applied to the network instance. Use tags to search and filter your resources or track your Amazon Web Services costs.</p>

        Raises:
            capo_tnb.errors.access_denied_exception.AccessDeniedException: <p>Insufficient permissions to make request.</p>
            capo_tnb.errors.internal_server_exception.InternalServerException: <p>Unexpected error occurred. Problem on the server.</p>
            capo_tnb.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource that doesn't exist.</p>
            capo_tnb.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Service quotas have been exceeded.</p>
            capo_tnb.errors.throttling_exception.ThrottlingException: <p>Exception caused by throttling.</p>
            capo_tnb.errors.validation_exception.ValidationException: <p>Unable to process the request because the client provided input failed to satisfy request constraints.</p>
            capo_tnb.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Terminate a Sol Network Instance

            >>> client.terminate_sol_network_instance(ns_instance_id='ni-0d5b823eb5c2a9241', tags={'Name': 'Resource'})
        """

        def _handler(
            req: "OperationRequest[capo_tnb.types.terminate_sol_network_instance_input.TerminateSolNetworkInstanceInput]",
        ) -> OperationResponse[
            "capo_tnb.types.terminate_sol_network_instance_output.TerminateSolNetworkInstanceOutput"
        ]:
            import capo_tnb._operations.tnb.terminate_sol_network_instance

            output, http_response = (
                capo_tnb._operations.tnb.terminate_sol_network_instance.terminate_sol_network_instance(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_tnb.types.terminate_sol_network_instance_input.TerminateSolNetworkInstanceInput = {
            "ns_instance_id": ns_instance_id
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
        resource_arn: "capo_tnb.types.tnb_resource_arn.TNBResourceArn",
        tag_keys: "capo_tnb.types.tag_keys.TagKeys",
        *,
        config_overrides: Optional[tnbClientConfig] = None,
    ) -> "capo_tnb.types.untag_resource_output.UntagResourceOutput":
        """<p>Untags an AWS TNB resource.</p> <p>A tag is a label that you assign to an Amazon Web Services resource. Each tag consists of a key and an optional value. You can use tags to search and filter your resources or track your Amazon Web Services costs.</p>

        Args:
            resource_arn: <p>Resource ARN.</p>
            tag_keys: <p>Tag keys.</p>

        Raises:
            capo_tnb.errors.access_denied_exception.AccessDeniedException: <p>Insufficient permissions to make request.</p>
            capo_tnb.errors.internal_server_exception.InternalServerException: <p>Unexpected error occurred. Problem on the server.</p>
            capo_tnb.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource that doesn't exist.</p>
            capo_tnb.errors.throttling_exception.ThrottlingException: <p>Exception caused by throttling.</p>
            capo_tnb.errors.validation_exception.ValidationException: <p>Unable to process the request because the client provided input failed to satisfy request constraints.</p>
            capo_tnb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_tnb.types.untag_resource_input.UntagResourceInput]",
        ) -> OperationResponse[
            "capo_tnb.types.untag_resource_output.UntagResourceOutput"
        ]:
            import capo_tnb._operations.tnb.untag_resource

            output, http_response = (
                capo_tnb._operations.tnb.untag_resource.untag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_tnb.types.untag_resource_input.UntagResourceInput = {
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

    def update_sol_function_package(
        self,
        vnf_pkg_id: "capo_tnb.types.vnf_pkg_id.VnfPkgId",
        operational_state: "capo_tnb.types.operational_state.OperationalState",
        *,
        config_overrides: Optional[tnbClientConfig] = None,
    ) -> "capo_tnb.types.update_sol_function_package_output.UpdateSolFunctionPackageOutput":
        """<p>Updates the operational state of function package.</p> <p>A function package is a .zip file in CSAR (Cloud Service Archive) format that contains a network function (an ETSI standard telecommunication application) and function package descriptor that uses the TOSCA standard to describe how the network functions should run on your network.</p>

        Args:
            vnf_pkg_id: <p>ID of the function package.</p>
            operational_state: <p>Operational state of the function package.</p>

        Raises:
            capo_tnb.errors.access_denied_exception.AccessDeniedException: <p>Insufficient permissions to make request.</p>
            capo_tnb.errors.internal_server_exception.InternalServerException: <p>Unexpected error occurred. Problem on the server.</p>
            capo_tnb.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource that doesn't exist.</p>
            capo_tnb.errors.throttling_exception.ThrottlingException: <p>Exception caused by throttling.</p>
            capo_tnb.errors.validation_exception.ValidationException: <p>Unable to process the request because the client provided input failed to satisfy request constraints.</p>
            capo_tnb.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Enable a function package's Operational State

            >>> client.update_sol_function_package(vnf_pkg_id='fp-07aa863e53460a2a6', operational_state='ENABLED')
            Disable a function package's Operational State

            >>> client.update_sol_function_package(vnf_pkg_id='fp-07aa863e53460a2a6', operational_state='DISABLED')
        """

        def _handler(
            req: "OperationRequest[capo_tnb.types.update_sol_function_package_input.UpdateSolFunctionPackageInput]",
        ) -> OperationResponse[
            "capo_tnb.types.update_sol_function_package_output.UpdateSolFunctionPackageOutput"
        ]:
            import capo_tnb._operations.tnb.update_sol_function_package

            output, http_response = (
                capo_tnb._operations.tnb.update_sol_function_package.update_sol_function_package(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_tnb.types.update_sol_function_package_input.UpdateSolFunctionPackageInput = {
            "vnf_pkg_id": vnf_pkg_id,
            "operational_state": operational_state,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_sol_network_instance(
        self,
        ns_instance_id: "capo_tnb.types.ns_instance_id.NsInstanceId",
        update_type: "capo_tnb.types.update_sol_network_type.UpdateSolNetworkType",
        *,
        config_overrides: Optional[tnbClientConfig] = None,
        modify_vnf_info_data: Optional[
            "capo_tnb.types.update_sol_network_modify.UpdateSolNetworkModify"
        ] = None,
        update_ns: Optional[
            "capo_tnb.types.update_sol_network_service_data.UpdateSolNetworkServiceData"
        ] = None,
        tags: Optional["capo_tnb.types.tag_map.TagMap"] = None,
    ) -> "capo_tnb.types.update_sol_network_instance_output.UpdateSolNetworkInstanceOutput":
        """<p>Update a network instance.</p> <p>A network instance is a single network created in Amazon Web Services TNB that can be deployed and on which life-cycle operations (like terminate, update, and delete) can be performed.</p> <p>Choose the <i>updateType</i> parameter to target the necessary update of the network instance.</p>

        Args:
            ns_instance_id: <p>ID of the network instance.</p>
            update_type: <p>The type of update.</p> <ul> <li> <p>Use the <code>MODIFY_VNF_INFORMATION</code> update type, to update a specific network function configuration, in the network instance.</p> </li> <li> <p>Use the <code>UPDATE_NS</code> update type, to update the network instance to a new network service descriptor.</p> </li> </ul>
            modify_vnf_info_data: <p>Identifies the network function information parameters and/or the configurable properties of the network function to be modified.</p> <p>Include this property only if the update type is <code>MODIFY_VNF_INFORMATION</code>.</p>
            update_ns: <p>Identifies the network service descriptor and the configurable properties of the descriptor, to be used for the update.</p> <p>Include this property only if the update type is <code>UPDATE_NS</code>.</p>
            tags: <p>A tag is a label that you assign to an Amazon Web Services resource. Each tag consists of a key and an optional value. When you use this API, the tags are only applied to the network operation that is created. These tags are not applied to the network instance. Use tags to search and filter your resources or track your Amazon Web Services costs.</p>

        Raises:
            capo_tnb.errors.access_denied_exception.AccessDeniedException: <p>Insufficient permissions to make request.</p>
            capo_tnb.errors.internal_server_exception.InternalServerException: <p>Unexpected error occurred. Problem on the server.</p>
            capo_tnb.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource that doesn't exist.</p>
            capo_tnb.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Service quotas have been exceeded.</p>
            capo_tnb.errors.throttling_exception.ThrottlingException: <p>Exception caused by throttling.</p>
            capo_tnb.errors.validation_exception.ValidationException: <p>Unable to process the request because the client provided input failed to satisfy request constraints.</p>
            capo_tnb.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Update a Sol Network Instance

            >>> client.update_sol_network_instance(ns_instance_id='ni-0d5b823eb5c2a9241', update_type='MODIFY_VNF_INFORMATION', modify_vnf_info_data={'vnfInstanceId': 'fi-0d5b823eb5c2a9241', 'vnfConfigurableProperties': {'pcf.port': '8080', 'pcf.pods': '10'}}, tags={'Name': 'Resource'})
            Update a Sol Network Instance

            >>> client.update_sol_network_instance(ns_instance_id='ni-0d5b823eb5c2a9241', update_type='UPDATE_NS', update_ns={'nsdInfoId': 'np-0d5b823eb5c2a9241', 'additionalParamsForNs': {'cidr_block': '10.0.0.0/16', 'availability_zone': 'us-west-2a'}}, tags={'Name': 'Resource'})
        """

        def _handler(
            req: "OperationRequest[capo_tnb.types.update_sol_network_instance_input.UpdateSolNetworkInstanceInput]",
        ) -> OperationResponse[
            "capo_tnb.types.update_sol_network_instance_output.UpdateSolNetworkInstanceOutput"
        ]:
            import capo_tnb._operations.tnb.update_sol_network_instance

            output, http_response = (
                capo_tnb._operations.tnb.update_sol_network_instance.update_sol_network_instance(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_tnb.types.update_sol_network_instance_input.UpdateSolNetworkInstanceInput = {
            "ns_instance_id": ns_instance_id,
            "update_type": update_type,
        }
        if modify_vnf_info_data is not None:
            input_["modify_vnf_info_data"] = modify_vnf_info_data
        if update_ns is not None:
            input_["update_ns"] = update_ns
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_sol_network_package(
        self,
        nsd_info_id: "capo_tnb.types.nsd_info_id.NsdInfoId",
        nsd_operational_state: "capo_tnb.types.nsd_operational_state.NsdOperationalState",
        *,
        config_overrides: Optional[tnbClientConfig] = None,
    ) -> (
        "capo_tnb.types.update_sol_network_package_output.UpdateSolNetworkPackageOutput"
    ):
        """<p>Updates the operational state of a network package.</p> <p>A network package is a .zip file in CSAR (Cloud Service Archive) format defines the function packages you want to deploy and the Amazon Web Services infrastructure you want to deploy them on.</p> <p>A network service descriptor is a .yaml file in a network package that uses the TOSCA standard to describe the network functions you want to deploy and the Amazon Web Services infrastructure you want to deploy the network functions on.</p>

        Args:
            nsd_info_id: <p>ID of the network service descriptor in the network package.</p>
            nsd_operational_state: <p>Operational state of the network service descriptor in the network package.</p>

        Raises:
            capo_tnb.errors.access_denied_exception.AccessDeniedException: <p>Insufficient permissions to make request.</p>
            capo_tnb.errors.internal_server_exception.InternalServerException: <p>Unexpected error occurred. Problem on the server.</p>
            capo_tnb.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource that doesn't exist.</p>
            capo_tnb.errors.throttling_exception.ThrottlingException: <p>Exception caused by throttling.</p>
            capo_tnb.errors.validation_exception.ValidationException: <p>Unable to process the request because the client provided input failed to satisfy request constraints.</p>
            capo_tnb.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Enable a network package's Operational State

            >>> client.update_sol_network_package(nsd_info_id='np-0d5b823eb5c2a9241', nsd_operational_state='ENABLED')
            Disable a network package's Operational State

            >>> client.update_sol_network_package(nsd_info_id='np-0d5b823eb5c2a9241', nsd_operational_state='DISABLED')
        """

        def _handler(
            req: "OperationRequest[capo_tnb.types.update_sol_network_package_input.UpdateSolNetworkPackageInput]",
        ) -> OperationResponse[
            "capo_tnb.types.update_sol_network_package_output.UpdateSolNetworkPackageOutput"
        ]:
            import capo_tnb._operations.tnb.update_sol_network_package

            output, http_response = (
                capo_tnb._operations.tnb.update_sol_network_package.update_sol_network_package(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_tnb.types.update_sol_network_package_input.UpdateSolNetworkPackageInput = {
            "nsd_info_id": nsd_info_id,
            "nsd_operational_state": nsd_operational_state,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def validate_sol_function_package_content(
        self,
        vnf_pkg_id: "capo_tnb.types.vnf_pkg_id.VnfPkgId",
        file: "capo_tnb.types.sensitive_blob.SensitiveBlob",
        *,
        config_overrides: Optional[tnbClientConfig] = None,
        content_type: Optional[
            "capo_tnb.types.package_content_type.PackageContentType"
        ] = None,
    ) -> "capo_tnb.types.validate_sol_function_package_content_output.ValidateSolFunctionPackageContentOutput":
        """<p>Validates function package content. This can be used as a dry run before uploading function package content with <a href="https://docs.aws.amazon.com/tnb/latest/APIReference/API_PutSolFunctionPackageContent.html">PutSolFunctionPackageContent</a>.</p> <p>A function package is a .zip file in CSAR (Cloud Service Archive) format that contains a network function (an ETSI standard telecommunication application) and function package descriptor that uses the TOSCA standard to describe how the network functions should run on your network.</p>

        Args:
            vnf_pkg_id: <p>Function package ID.</p>
            content_type: <p>Function package content type.</p>
            file: <p>Function package file.</p>

        Raises:
            capo_tnb.errors.access_denied_exception.AccessDeniedException: <p>Insufficient permissions to make request.</p>
            capo_tnb.errors.internal_server_exception.InternalServerException: <p>Unexpected error occurred. Problem on the server.</p>
            capo_tnb.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource that doesn't exist.</p>
            capo_tnb.errors.throttling_exception.ThrottlingException: <p>Exception caused by throttling.</p>
            capo_tnb.errors.validation_exception.ValidationException: <p>Unable to process the request because the client provided input failed to satisfy request constraints.</p>
            capo_tnb.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Validate a Function Package content

            >>> client.validate_sol_function_package_content(vnf_pkg_id='fp-07aa863e53460a2a6', content_type='application/zip', file='UEsDBBQAAAAAAPqLiVMAAAAAAAAAAAAAAAAMACAAZnJlZTVnYy1hbWYvVVQNAAcIrrJhBK')
        """

        def _handler(
            req: "OperationRequest[capo_tnb.types.validate_sol_function_package_content_input.ValidateSolFunctionPackageContentInput]",
        ) -> OperationResponse[
            "capo_tnb.types.validate_sol_function_package_content_output.ValidateSolFunctionPackageContentOutput"
        ]:
            import capo_tnb._operations.tnb.validate_sol_function_package_content

            output, http_response = (
                capo_tnb._operations.tnb.validate_sol_function_package_content.validate_sol_function_package_content(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_tnb.types.validate_sol_function_package_content_input.ValidateSolFunctionPackageContentInput = {
            "vnf_pkg_id": vnf_pkg_id,
            "file": file,
        }
        if content_type is not None:
            input_["content_type"] = content_type

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def validate_sol_network_package_content(
        self,
        nsd_info_id: "capo_tnb.types.nsd_info_id.NsdInfoId",
        file: "capo_tnb.types.sensitive_blob.SensitiveBlob",
        *,
        config_overrides: Optional[tnbClientConfig] = None,
        content_type: Optional[
            "capo_tnb.types.package_content_type.PackageContentType"
        ] = None,
    ) -> "capo_tnb.types.validate_sol_network_package_content_output.ValidateSolNetworkPackageContentOutput":
        """<p>Validates network package content. This can be used as a dry run before uploading network package content with <a href="https://docs.aws.amazon.com/tnb/latest/APIReference/API_PutSolNetworkPackageContent.html">PutSolNetworkPackageContent</a>.</p> <p>A network package is a .zip file in CSAR (Cloud Service Archive) format defines the function packages you want to deploy and the Amazon Web Services infrastructure you want to deploy them on.</p>

        Args:
            nsd_info_id: <p>Network service descriptor file.</p>
            content_type: <p>Network package content type.</p>
            file: <p>Network package file.</p>

        Raises:
            capo_tnb.errors.access_denied_exception.AccessDeniedException: <p>Insufficient permissions to make request.</p>
            capo_tnb.errors.internal_server_exception.InternalServerException: <p>Unexpected error occurred. Problem on the server.</p>
            capo_tnb.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource that doesn't exist.</p>
            capo_tnb.errors.throttling_exception.ThrottlingException: <p>Exception caused by throttling.</p>
            capo_tnb.errors.validation_exception.ValidationException: <p>Unable to process the request because the client provided input failed to satisfy request constraints.</p>
            capo_tnb.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Validate the network package content of a NSD archive

            >>> client.validate_sol_network_package_content(nsd_info_id='np-0d5b823eb5c2a9241', content_type='application/zip', file='UEsDBBQAAAAAAPqLiVMAAAAAAAAAAAAAA')
        """

        def _handler(
            req: "OperationRequest[capo_tnb.types.validate_sol_network_package_content_input.ValidateSolNetworkPackageContentInput]",
        ) -> OperationResponse[
            "capo_tnb.types.validate_sol_network_package_content_output.ValidateSolNetworkPackageContentOutput"
        ]:
            import capo_tnb._operations.tnb.validate_sol_network_package_content

            output, http_response = (
                capo_tnb._operations.tnb.validate_sol_network_package_content.validate_sol_network_package_content(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_tnb.types.validate_sol_network_package_content_input.ValidateSolNetworkPackageContentInput = {
            "nsd_info_id": nsd_info_id,
            "file": file,
        }
        if content_type is not None:
            input_["content_type"] = content_type

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
