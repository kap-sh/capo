"""Generated from Smithy shape ``com.amazonaws.managedblockchain#TaigaWebService``."""

import warnings
from collections.abc import Iterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import BaseHandler, Client

import capo_managedblockchain._auth._signers
import capo_managedblockchain._auth._sigv4
from capo_managedblockchain._auth._identity import Credentials
from capo_managedblockchain._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_managedblockchain._auth._zapros_handler import AuthMiddleware
from capo_managedblockchain._pagination import resolve_path as _resolve_path
from capo_managedblockchain._services._aws_config import aws_config
from capo_managedblockchain._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import capo_managedblockchain.types.accessor_list_max_results
    import capo_managedblockchain.types.accessor_network_type
    import capo_managedblockchain.types.accessor_summary
    import capo_managedblockchain.types.accessor_type
    import capo_managedblockchain.types.arn_string
    import capo_managedblockchain.types.client_request_token_string
    import capo_managedblockchain.types.create_accessor_input
    import capo_managedblockchain.types.create_accessor_output
    import capo_managedblockchain.types.create_member_input
    import capo_managedblockchain.types.create_member_output
    import capo_managedblockchain.types.create_network_input
    import capo_managedblockchain.types.create_network_output
    import capo_managedblockchain.types.create_node_input
    import capo_managedblockchain.types.create_node_output
    import capo_managedblockchain.types.create_proposal_input
    import capo_managedblockchain.types.create_proposal_output
    import capo_managedblockchain.types.delete_accessor_input
    import capo_managedblockchain.types.delete_accessor_output
    import capo_managedblockchain.types.delete_member_input
    import capo_managedblockchain.types.delete_member_output
    import capo_managedblockchain.types.delete_node_input
    import capo_managedblockchain.types.delete_node_output
    import capo_managedblockchain.types.description_string
    import capo_managedblockchain.types.framework
    import capo_managedblockchain.types.framework_version_string
    import capo_managedblockchain.types.get_accessor_input
    import capo_managedblockchain.types.get_accessor_output
    import capo_managedblockchain.types.get_member_input
    import capo_managedblockchain.types.get_member_output
    import capo_managedblockchain.types.get_network_input
    import capo_managedblockchain.types.get_network_output
    import capo_managedblockchain.types.get_node_input
    import capo_managedblockchain.types.get_node_output
    import capo_managedblockchain.types.get_proposal_input
    import capo_managedblockchain.types.get_proposal_output
    import capo_managedblockchain.types.input_tag_map
    import capo_managedblockchain.types.is_owned
    import capo_managedblockchain.types.list_accessors_input
    import capo_managedblockchain.types.list_accessors_output
    import capo_managedblockchain.types.list_invitations_input
    import capo_managedblockchain.types.list_invitations_output
    import capo_managedblockchain.types.list_members_input
    import capo_managedblockchain.types.list_members_output
    import capo_managedblockchain.types.list_networks_input
    import capo_managedblockchain.types.list_networks_output
    import capo_managedblockchain.types.list_nodes_input
    import capo_managedblockchain.types.list_nodes_output
    import capo_managedblockchain.types.list_proposal_votes_input
    import capo_managedblockchain.types.list_proposal_votes_output
    import capo_managedblockchain.types.list_proposals_input
    import capo_managedblockchain.types.list_proposals_output
    import capo_managedblockchain.types.list_tags_for_resource_request
    import capo_managedblockchain.types.list_tags_for_resource_response
    import capo_managedblockchain.types.member_configuration
    import capo_managedblockchain.types.member_list_max_results
    import capo_managedblockchain.types.member_log_publishing_configuration
    import capo_managedblockchain.types.member_status
    import capo_managedblockchain.types.name_string
    import capo_managedblockchain.types.network_framework_configuration
    import capo_managedblockchain.types.network_list_max_results
    import capo_managedblockchain.types.network_status
    import capo_managedblockchain.types.node_configuration
    import capo_managedblockchain.types.node_list_max_results
    import capo_managedblockchain.types.node_log_publishing_configuration
    import capo_managedblockchain.types.node_status
    import capo_managedblockchain.types.pagination_token
    import capo_managedblockchain.types.proposal_actions
    import capo_managedblockchain.types.proposal_list_max_results
    import capo_managedblockchain.types.reject_invitation_input
    import capo_managedblockchain.types.reject_invitation_output
    import capo_managedblockchain.types.resource_id_string
    import capo_managedblockchain.types.string
    import capo_managedblockchain.types.tag_key_list
    import capo_managedblockchain.types.tag_resource_request
    import capo_managedblockchain.types.tag_resource_response
    import capo_managedblockchain.types.untag_resource_request
    import capo_managedblockchain.types.untag_resource_response
    import capo_managedblockchain.types.update_member_input
    import capo_managedblockchain.types.update_member_output
    import capo_managedblockchain.types.update_node_input
    import capo_managedblockchain.types.update_node_output
    import capo_managedblockchain.types.vote_on_proposal_input
    import capo_managedblockchain.types.vote_on_proposal_output
    import capo_managedblockchain.types.vote_value
    import capo_managedblockchain.types.voting_policy


class ManagedBlockchainClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None
    anonymous: bool | None


class ManagedBlockchainClient:
    """A client for the ``ManagedBlockchain`` service.

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
        self._config = ManagedBlockchainClientConfig(
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
        self, config_overrides: Optional[ManagedBlockchainClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: ManagedBlockchainClientConfig = config_overrides or {}
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

    def create_accessor(
        self,
        client_request_token: "capo_managedblockchain.types.client_request_token_string.ClientRequestTokenString",
        accessor_type: "capo_managedblockchain.types.accessor_type.AccessorType",
        *,
        config_overrides: Optional[ManagedBlockchainClientConfig] = None,
        tags: Optional["capo_managedblockchain.types.input_tag_map.InputTagMap"] = None,
        network_type: Optional[
            "capo_managedblockchain.types.accessor_network_type.AccessorNetworkType"
        ] = None,
    ) -> "capo_managedblockchain.types.create_accessor_output.CreateAccessorOutput":
        """<p>Creates a new accessor for use with Amazon Managed Blockchain service that supports token based access. The accessor contains information required for token based access.</p>

        Args:
            client_request_token: <p>This is a unique, case-sensitive identifier that you provide to ensure the idempotency of the operation. An idempotent operation completes no more than once. This identifier is required only if you make a service request directly using an HTTP client. It is generated automatically if you use an Amazon Web Services SDK or the Amazon Web Services CLI.</p>
            accessor_type: <p>The type of accessor.</p> <note> <p>Currently, accessor type is restricted to <code>BILLING_TOKEN</code>.</p> </note>
            tags: <p>Tags to assign to the Accessor.</p> <p> Each tag consists of a key and an optional value. You can specify multiple key-value pairs in a single request with an overall maximum of 50 tags allowed per resource.</p> <p>For more information about tags, see <a href="https://docs.aws.amazon.com/managed-blockchain/latest/ethereum-dev/tagging-resources.html">Tagging Resources</a> in the <i>Amazon Managed Blockchain Ethereum Developer Guide</i>, or <a href="https://docs.aws.amazon.com/managed-blockchain/latest/hyperledger-fabric-dev/tagging-resources.html">Tagging Resources</a> in the <i>Amazon Managed Blockchain Hyperledger Fabric Developer Guide</i>.</p>
            network_type: <p>The blockchain network that the <code>Accessor</code> token is created for.</p> <note> <ul> <li> <p>Use the actual <code>networkType</code> value for the blockchain network that you are creating the <code>Accessor</code> token for.</p> </li> <li> <p>With the shut down of the <i>Ethereum Goerli</i> and <i>Polygon Mumbai Testnet</i> networks the following <code>networkType</code> values are no longer available for selection and use.</p> <ul> <li> <p> <code>ETHEREUM_MAINNET_AND_GOERLI</code> </p> </li> <li> <p> <code>ETHEREUM_GOERLI</code> </p> </li> <li> <p> <code>POLYGON_MUMBAI</code> </p> </li> </ul> <p>However, your existing <code>Accessor</code> tokens with these <code>networkType</code> values will remain unchanged.</p> </li> </ul> </note>

        Raises:
            capo_managedblockchain.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action.</p>
            capo_managedblockchain.errors.internal_service_error_exception.InternalServiceErrorException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_managedblockchain.errors.invalid_request_exception.InvalidRequestException: <p>The action or operation requested is invalid. Verify that the action is typed correctly.</p>
            capo_managedblockchain.errors.resource_already_exists_exception.ResourceAlreadyExistsException: <p>A resource request is issued for a resource that already exists.</p>
            capo_managedblockchain.errors.resource_limit_exceeded_exception.ResourceLimitExceededException: <p>The maximum number of resources of that type already exist. Ensure the resources requested are within the boundaries of the service edition and your account limits.</p>
            capo_managedblockchain.errors.throttling_exception.ThrottlingException: <p>The request or operation couldn't be performed because a service is throttling requests. The most common source of throttling errors is creating resources that exceed your service limit for this resource type. Request a limit increase or delete unused resources if possible.</p>
            capo_managedblockchain.errors.too_many_tags_exception.TooManyTagsException: <p></p>
            capo_managedblockchain.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_managedblockchain.types.create_accessor_input.CreateAccessorInput]",
        ) -> OperationResponse[
            "capo_managedblockchain.types.create_accessor_output.CreateAccessorOutput"
        ]:
            import capo_managedblockchain._operations.taiga_web_service.create_accessor

            output, http_response = (
                capo_managedblockchain._operations.taiga_web_service.create_accessor.create_accessor(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_managedblockchain.types.create_accessor_input.CreateAccessorInput = {
            "client_request_token": client_request_token,
            "accessor_type": accessor_type,
        }
        if tags is not None:
            input_["tags"] = tags
        if network_type is not None:
            input_["network_type"] = network_type

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_member(
        self,
        client_request_token: "capo_managedblockchain.types.client_request_token_string.ClientRequestTokenString",
        invitation_id: "capo_managedblockchain.types.resource_id_string.ResourceIdString",
        network_id: "capo_managedblockchain.types.resource_id_string.ResourceIdString",
        member_configuration: "capo_managedblockchain.types.member_configuration.MemberConfiguration",
        *,
        config_overrides: Optional[ManagedBlockchainClientConfig] = None,
    ) -> "capo_managedblockchain.types.create_member_output.CreateMemberOutput":
        """<p>Creates a member within a Managed Blockchain network.</p> <p>Applies only to Hyperledger Fabric.</p>

        Args:
            client_request_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the operation. An idempotent operation completes no more than one time. This identifier is required only if you make a service request directly using an HTTP client. It is generated automatically if you use an Amazon Web Services SDK or the CLI.</p>
            invitation_id: <p>The unique identifier of the invitation that is sent to the member to join the network.</p>
            network_id: <p>The unique identifier of the network in which the member is created.</p>
            member_configuration: <p>Member configuration parameters.</p>

        Raises:
            capo_managedblockchain.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action.</p>
            capo_managedblockchain.errors.internal_service_error_exception.InternalServiceErrorException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_managedblockchain.errors.invalid_request_exception.InvalidRequestException: <p>The action or operation requested is invalid. Verify that the action is typed correctly.</p>
            capo_managedblockchain.errors.resource_already_exists_exception.ResourceAlreadyExistsException: <p>A resource request is issued for a resource that already exists.</p>
            capo_managedblockchain.errors.resource_limit_exceeded_exception.ResourceLimitExceededException: <p>The maximum number of resources of that type already exist. Ensure the resources requested are within the boundaries of the service edition and your account limits.</p>
            capo_managedblockchain.errors.resource_not_found_exception.ResourceNotFoundException: <p>A requested resource doesn't exist. It may have been deleted or referenced incorrectly.</p>
            capo_managedblockchain.errors.resource_not_ready_exception.ResourceNotReadyException: <p>The requested resource exists but isn't in a status that can complete the operation.</p>
            capo_managedblockchain.errors.throttling_exception.ThrottlingException: <p>The request or operation couldn't be performed because a service is throttling requests. The most common source of throttling errors is creating resources that exceed your service limit for this resource type. Request a limit increase or delete unused resources if possible.</p>
            capo_managedblockchain.errors.too_many_tags_exception.TooManyTagsException: <p></p>
            capo_managedblockchain.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_managedblockchain.types.create_member_input.CreateMemberInput]",
        ) -> OperationResponse[
            "capo_managedblockchain.types.create_member_output.CreateMemberOutput"
        ]:
            import capo_managedblockchain._operations.taiga_web_service.create_member

            output, http_response = (
                capo_managedblockchain._operations.taiga_web_service.create_member.create_member(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_managedblockchain.types.create_member_input.CreateMemberInput = {
            "client_request_token": client_request_token,
            "invitation_id": invitation_id,
            "network_id": network_id,
            "member_configuration": member_configuration,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_network(
        self,
        client_request_token: "capo_managedblockchain.types.client_request_token_string.ClientRequestTokenString",
        name: "capo_managedblockchain.types.name_string.NameString",
        framework: "capo_managedblockchain.types.framework.Framework",
        framework_version: "capo_managedblockchain.types.framework_version_string.FrameworkVersionString",
        voting_policy: "capo_managedblockchain.types.voting_policy.VotingPolicy",
        member_configuration: "capo_managedblockchain.types.member_configuration.MemberConfiguration",
        *,
        config_overrides: Optional[ManagedBlockchainClientConfig] = None,
        description: Optional[
            "capo_managedblockchain.types.description_string.DescriptionString"
        ] = None,
        framework_configuration: Optional[
            "capo_managedblockchain.types.network_framework_configuration.NetworkFrameworkConfiguration"
        ] = None,
        tags: Optional["capo_managedblockchain.types.input_tag_map.InputTagMap"] = None,
    ) -> "capo_managedblockchain.types.create_network_output.CreateNetworkOutput":
        """<p>Creates a new blockchain network using Amazon Managed Blockchain.</p> <p>Applies only to Hyperledger Fabric.</p>

        Args:
            client_request_token: <p>This is a unique, case-sensitive identifier that you provide to ensure the idempotency of the operation. An idempotent operation completes no more than once. This identifier is required only if you make a service request directly using an HTTP client. It is generated automatically if you use an Amazon Web Services SDK or the Amazon Web Services CLI. </p>
            name: <p>The name of the network.</p>
            description: <p>An optional description for the network.</p>
            framework: <p>The blockchain framework that the network uses.</p>
            framework_version: <p>The version of the blockchain framework that the network uses.</p>
            framework_configuration: <p> Configuration properties of the blockchain framework relevant to the network configuration. </p>
            voting_policy: <p> The voting rules used by the network to determine if a proposal is approved. </p>
            member_configuration: <p>Configuration properties for the first member within the network.</p>
            tags: <p>Tags to assign to the network.</p> <p> Each tag consists of a key and an optional value. You can specify multiple key-value pairs in a single request with an overall maximum of 50 tags allowed per resource.</p> <p>For more information about tags, see <a href="https://docs.aws.amazon.com/managed-blockchain/latest/ethereum-dev/tagging-resources.html">Tagging Resources</a> in the <i>Amazon Managed Blockchain Ethereum Developer Guide</i>, or <a href="https://docs.aws.amazon.com/managed-blockchain/latest/hyperledger-fabric-dev/tagging-resources.html">Tagging Resources</a> in the <i>Amazon Managed Blockchain Hyperledger Fabric Developer Guide</i>.</p>

        Raises:
            capo_managedblockchain.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action.</p>
            capo_managedblockchain.errors.internal_service_error_exception.InternalServiceErrorException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_managedblockchain.errors.invalid_request_exception.InvalidRequestException: <p>The action or operation requested is invalid. Verify that the action is typed correctly.</p>
            capo_managedblockchain.errors.resource_already_exists_exception.ResourceAlreadyExistsException: <p>A resource request is issued for a resource that already exists.</p>
            capo_managedblockchain.errors.resource_limit_exceeded_exception.ResourceLimitExceededException: <p>The maximum number of resources of that type already exist. Ensure the resources requested are within the boundaries of the service edition and your account limits.</p>
            capo_managedblockchain.errors.throttling_exception.ThrottlingException: <p>The request or operation couldn't be performed because a service is throttling requests. The most common source of throttling errors is creating resources that exceed your service limit for this resource type. Request a limit increase or delete unused resources if possible.</p>
            capo_managedblockchain.errors.too_many_tags_exception.TooManyTagsException: <p></p>
            capo_managedblockchain.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_managedblockchain.types.create_network_input.CreateNetworkInput]",
        ) -> OperationResponse[
            "capo_managedblockchain.types.create_network_output.CreateNetworkOutput"
        ]:
            import capo_managedblockchain._operations.taiga_web_service.create_network

            output, http_response = (
                capo_managedblockchain._operations.taiga_web_service.create_network.create_network(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_managedblockchain.types.create_network_input.CreateNetworkInput = {
            "client_request_token": client_request_token,
            "name": name,
            "framework": framework,
            "framework_version": framework_version,
            "voting_policy": voting_policy,
            "member_configuration": member_configuration,
        }
        if description is not None:
            input_["description"] = description
        if framework_configuration is not None:
            input_["framework_configuration"] = framework_configuration
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_node(
        self,
        client_request_token: "capo_managedblockchain.types.client_request_token_string.ClientRequestTokenString",
        network_id: "capo_managedblockchain.types.resource_id_string.ResourceIdString",
        node_configuration: "capo_managedblockchain.types.node_configuration.NodeConfiguration",
        *,
        config_overrides: Optional[ManagedBlockchainClientConfig] = None,
        member_id: Optional[
            "capo_managedblockchain.types.resource_id_string.ResourceIdString"
        ] = None,
        tags: Optional["capo_managedblockchain.types.input_tag_map.InputTagMap"] = None,
    ) -> "capo_managedblockchain.types.create_node_output.CreateNodeOutput":
        """<p>Creates a node on the specified blockchain network.</p> <p>Applies to Hyperledger Fabric and Ethereum.</p>

        Args:
            client_request_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the operation. An idempotent operation completes no more than one time. This identifier is required only if you make a service request directly using an HTTP client. It is generated automatically if you use an Amazon Web Services SDK or the CLI.</p>
            network_id: <p>The unique identifier of the network for the node.</p> <p>Ethereum public networks have the following <code>NetworkId</code>s:</p> <ul> <li> <p> <code>n-ethereum-mainnet</code> </p> </li> </ul>
            member_id: <p>The unique identifier of the member that owns this node.</p> <p>Applies only to Hyperledger Fabric.</p>
            node_configuration: <p>The properties of a node configuration.</p>
            tags: <p>Tags to assign to the node.</p> <p> Each tag consists of a key and an optional value. You can specify multiple key-value pairs in a single request with an overall maximum of 50 tags allowed per resource.</p> <p>For more information about tags, see <a href="https://docs.aws.amazon.com/managed-blockchain/latest/ethereum-dev/tagging-resources.html">Tagging Resources</a> in the <i>Amazon Managed Blockchain Ethereum Developer Guide</i>, or <a href="https://docs.aws.amazon.com/managed-blockchain/latest/hyperledger-fabric-dev/tagging-resources.html">Tagging Resources</a> in the <i>Amazon Managed Blockchain Hyperledger Fabric Developer Guide</i>.</p>

        Raises:
            capo_managedblockchain.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action.</p>
            capo_managedblockchain.errors.internal_service_error_exception.InternalServiceErrorException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_managedblockchain.errors.invalid_request_exception.InvalidRequestException: <p>The action or operation requested is invalid. Verify that the action is typed correctly.</p>
            capo_managedblockchain.errors.resource_already_exists_exception.ResourceAlreadyExistsException: <p>A resource request is issued for a resource that already exists.</p>
            capo_managedblockchain.errors.resource_limit_exceeded_exception.ResourceLimitExceededException: <p>The maximum number of resources of that type already exist. Ensure the resources requested are within the boundaries of the service edition and your account limits.</p>
            capo_managedblockchain.errors.resource_not_found_exception.ResourceNotFoundException: <p>A requested resource doesn't exist. It may have been deleted or referenced incorrectly.</p>
            capo_managedblockchain.errors.resource_not_ready_exception.ResourceNotReadyException: <p>The requested resource exists but isn't in a status that can complete the operation.</p>
            capo_managedblockchain.errors.throttling_exception.ThrottlingException: <p>The request or operation couldn't be performed because a service is throttling requests. The most common source of throttling errors is creating resources that exceed your service limit for this resource type. Request a limit increase or delete unused resources if possible.</p>
            capo_managedblockchain.errors.too_many_tags_exception.TooManyTagsException: <p></p>
            capo_managedblockchain.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_managedblockchain.types.create_node_input.CreateNodeInput]",
        ) -> OperationResponse[
            "capo_managedblockchain.types.create_node_output.CreateNodeOutput"
        ]:
            import capo_managedblockchain._operations.taiga_web_service.create_node

            output, http_response = (
                capo_managedblockchain._operations.taiga_web_service.create_node.create_node(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_managedblockchain.types.create_node_input.CreateNodeInput = {
            "client_request_token": client_request_token,
            "network_id": network_id,
            "node_configuration": node_configuration,
        }
        if member_id is not None:
            input_["member_id"] = member_id
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_proposal(
        self,
        client_request_token: "capo_managedblockchain.types.client_request_token_string.ClientRequestTokenString",
        network_id: "capo_managedblockchain.types.resource_id_string.ResourceIdString",
        member_id: "capo_managedblockchain.types.resource_id_string.ResourceIdString",
        actions: "capo_managedblockchain.types.proposal_actions.ProposalActions",
        *,
        config_overrides: Optional[ManagedBlockchainClientConfig] = None,
        description: Optional[
            "capo_managedblockchain.types.description_string.DescriptionString"
        ] = None,
        tags: Optional["capo_managedblockchain.types.input_tag_map.InputTagMap"] = None,
    ) -> "capo_managedblockchain.types.create_proposal_output.CreateProposalOutput":
        """<p>Creates a proposal for a change to the network that other members of the network can vote on, for example, a proposal to add a new member to the network. Any member can create a proposal.</p> <p>Applies only to Hyperledger Fabric.</p>

        Args:
            client_request_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the operation. An idempotent operation completes no more than one time. This identifier is required only if you make a service request directly using an HTTP client. It is generated automatically if you use an Amazon Web Services SDK or the CLI.</p>
            network_id: <p> The unique identifier of the network for which the proposal is made.</p>
            member_id: <p>The unique identifier of the member that is creating the proposal. This identifier is especially useful for identifying the member making the proposal when multiple members exist in a single Amazon Web Services account.</p>
            actions: <p>The type of actions proposed, such as inviting a member or removing a member. The types of <code>Actions</code> in a proposal are mutually exclusive. For example, a proposal with <code>Invitations</code> actions cannot also contain <code>Removals</code> actions.</p>
            description: <p>A description for the proposal that is visible to voting members, for example, "Proposal to add Example Corp. as member."</p>
            tags: <p>Tags to assign to the proposal.</p> <p> Each tag consists of a key and an optional value. You can specify multiple key-value pairs in a single request with an overall maximum of 50 tags allowed per resource.</p> <p>For more information about tags, see <a href="https://docs.aws.amazon.com/managed-blockchain/latest/ethereum-dev/tagging-resources.html">Tagging Resources</a> in the <i>Amazon Managed Blockchain Ethereum Developer Guide</i>, or <a href="https://docs.aws.amazon.com/managed-blockchain/latest/hyperledger-fabric-dev/tagging-resources.html">Tagging Resources</a> in the <i>Amazon Managed Blockchain Hyperledger Fabric Developer Guide</i>.</p>

        Raises:
            capo_managedblockchain.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action.</p>
            capo_managedblockchain.errors.internal_service_error_exception.InternalServiceErrorException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_managedblockchain.errors.invalid_request_exception.InvalidRequestException: <p>The action or operation requested is invalid. Verify that the action is typed correctly.</p>
            capo_managedblockchain.errors.resource_not_found_exception.ResourceNotFoundException: <p>A requested resource doesn't exist. It may have been deleted or referenced incorrectly.</p>
            capo_managedblockchain.errors.resource_not_ready_exception.ResourceNotReadyException: <p>The requested resource exists but isn't in a status that can complete the operation.</p>
            capo_managedblockchain.errors.throttling_exception.ThrottlingException: <p>The request or operation couldn't be performed because a service is throttling requests. The most common source of throttling errors is creating resources that exceed your service limit for this resource type. Request a limit increase or delete unused resources if possible.</p>
            capo_managedblockchain.errors.too_many_tags_exception.TooManyTagsException: <p></p>
            capo_managedblockchain.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_managedblockchain.types.create_proposal_input.CreateProposalInput]",
        ) -> OperationResponse[
            "capo_managedblockchain.types.create_proposal_output.CreateProposalOutput"
        ]:
            import capo_managedblockchain._operations.taiga_web_service.create_proposal

            output, http_response = (
                capo_managedblockchain._operations.taiga_web_service.create_proposal.create_proposal(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_managedblockchain.types.create_proposal_input.CreateProposalInput = {
            "client_request_token": client_request_token,
            "network_id": network_id,
            "member_id": member_id,
            "actions": actions,
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

    def delete_accessor(
        self,
        accessor_id: "capo_managedblockchain.types.resource_id_string.ResourceIdString",
        *,
        config_overrides: Optional[ManagedBlockchainClientConfig] = None,
    ) -> "capo_managedblockchain.types.delete_accessor_output.DeleteAccessorOutput":
        """<p>Deletes an accessor that your Amazon Web Services account owns. An accessor object is a container that has the information required for token based access to your Ethereum nodes including, the <code>BILLING_TOKEN</code>. After an accessor is deleted, the status of the accessor changes from <code>AVAILABLE</code> to <code>PENDING_DELETION</code>. An accessor in the <code>PENDING_DELETION</code> state can’t be used for new WebSocket requests or HTTP requests. However, WebSocket connections that were initiated while the accessor was in the <code>AVAILABLE</code> state remain open until they expire (up to 2 hours).</p>

        Args:
            accessor_id: <p>The unique identifier of the accessor.</p>

        Raises:
            capo_managedblockchain.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action.</p>
            capo_managedblockchain.errors.internal_service_error_exception.InternalServiceErrorException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_managedblockchain.errors.invalid_request_exception.InvalidRequestException: <p>The action or operation requested is invalid. Verify that the action is typed correctly.</p>
            capo_managedblockchain.errors.resource_not_found_exception.ResourceNotFoundException: <p>A requested resource doesn't exist. It may have been deleted or referenced incorrectly.</p>
            capo_managedblockchain.errors.throttling_exception.ThrottlingException: <p>The request or operation couldn't be performed because a service is throttling requests. The most common source of throttling errors is creating resources that exceed your service limit for this resource type. Request a limit increase or delete unused resources if possible.</p>
            capo_managedblockchain.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_managedblockchain.types.delete_accessor_input.DeleteAccessorInput]",
        ) -> OperationResponse[
            "capo_managedblockchain.types.delete_accessor_output.DeleteAccessorOutput"
        ]:
            import capo_managedblockchain._operations.taiga_web_service.delete_accessor

            output, http_response = (
                capo_managedblockchain._operations.taiga_web_service.delete_accessor.delete_accessor(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_managedblockchain.types.delete_accessor_input.DeleteAccessorInput = {
            "accessor_id": accessor_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_member(
        self,
        network_id: "capo_managedblockchain.types.resource_id_string.ResourceIdString",
        member_id: "capo_managedblockchain.types.resource_id_string.ResourceIdString",
        *,
        config_overrides: Optional[ManagedBlockchainClientConfig] = None,
    ) -> "capo_managedblockchain.types.delete_member_output.DeleteMemberOutput":
        """<p>Deletes a member. Deleting a member removes the member and all associated resources from the network. <code>DeleteMember</code> can only be called for a specified <code>MemberId</code> if the principal performing the action is associated with the Amazon Web Services account that owns the member. In all other cases, the <code>DeleteMember</code> action is carried out as the result of an approved proposal to remove a member. If <code>MemberId</code> is the last member in a network specified by the last Amazon Web Services account, the network is deleted also.</p> <p>Applies only to Hyperledger Fabric.</p>

        Args:
            network_id: <p>The unique identifier of the network from which the member is removed.</p>
            member_id: <p>The unique identifier of the member to remove.</p>

        Raises:
            capo_managedblockchain.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action.</p>
            capo_managedblockchain.errors.internal_service_error_exception.InternalServiceErrorException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_managedblockchain.errors.invalid_request_exception.InvalidRequestException: <p>The action or operation requested is invalid. Verify that the action is typed correctly.</p>
            capo_managedblockchain.errors.resource_not_found_exception.ResourceNotFoundException: <p>A requested resource doesn't exist. It may have been deleted or referenced incorrectly.</p>
            capo_managedblockchain.errors.resource_not_ready_exception.ResourceNotReadyException: <p>The requested resource exists but isn't in a status that can complete the operation.</p>
            capo_managedblockchain.errors.throttling_exception.ThrottlingException: <p>The request or operation couldn't be performed because a service is throttling requests. The most common source of throttling errors is creating resources that exceed your service limit for this resource type. Request a limit increase or delete unused resources if possible.</p>
            capo_managedblockchain.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_managedblockchain.types.delete_member_input.DeleteMemberInput]",
        ) -> OperationResponse[
            "capo_managedblockchain.types.delete_member_output.DeleteMemberOutput"
        ]:
            import capo_managedblockchain._operations.taiga_web_service.delete_member

            output, http_response = (
                capo_managedblockchain._operations.taiga_web_service.delete_member.delete_member(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_managedblockchain.types.delete_member_input.DeleteMemberInput = {
            "network_id": network_id,
            "member_id": member_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_node(
        self,
        network_id: "capo_managedblockchain.types.resource_id_string.ResourceIdString",
        node_id: "capo_managedblockchain.types.resource_id_string.ResourceIdString",
        *,
        config_overrides: Optional[ManagedBlockchainClientConfig] = None,
        member_id: Optional[
            "capo_managedblockchain.types.resource_id_string.ResourceIdString"
        ] = None,
    ) -> "capo_managedblockchain.types.delete_node_output.DeleteNodeOutput":
        """<p>Deletes a node that your Amazon Web Services account owns. All data on the node is lost and cannot be recovered.</p> <p>Applies to Hyperledger Fabric and Ethereum.</p>

        Args:
            network_id: <p>The unique identifier of the network that the node is on.</p> <p>Ethereum public networks have the following <code>NetworkId</code>s:</p> <ul> <li> <p> <code>n-ethereum-mainnet</code> </p> </li> </ul>
            member_id: <p>The unique identifier of the member that owns this node.</p> <p>Applies only to Hyperledger Fabric and is required for Hyperledger Fabric.</p>
            node_id: <p>The unique identifier of the node.</p>

        Raises:
            capo_managedblockchain.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action.</p>
            capo_managedblockchain.errors.internal_service_error_exception.InternalServiceErrorException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_managedblockchain.errors.invalid_request_exception.InvalidRequestException: <p>The action or operation requested is invalid. Verify that the action is typed correctly.</p>
            capo_managedblockchain.errors.resource_not_found_exception.ResourceNotFoundException: <p>A requested resource doesn't exist. It may have been deleted or referenced incorrectly.</p>
            capo_managedblockchain.errors.resource_not_ready_exception.ResourceNotReadyException: <p>The requested resource exists but isn't in a status that can complete the operation.</p>
            capo_managedblockchain.errors.throttling_exception.ThrottlingException: <p>The request or operation couldn't be performed because a service is throttling requests. The most common source of throttling errors is creating resources that exceed your service limit for this resource type. Request a limit increase or delete unused resources if possible.</p>
            capo_managedblockchain.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_managedblockchain.types.delete_node_input.DeleteNodeInput]",
        ) -> OperationResponse[
            "capo_managedblockchain.types.delete_node_output.DeleteNodeOutput"
        ]:
            import capo_managedblockchain._operations.taiga_web_service.delete_node

            output, http_response = (
                capo_managedblockchain._operations.taiga_web_service.delete_node.delete_node(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_managedblockchain.types.delete_node_input.DeleteNodeInput = {
            "network_id": network_id,
            "node_id": node_id,
        }
        if member_id is not None:
            input_["member_id"] = member_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_accessor(
        self,
        accessor_id: "capo_managedblockchain.types.resource_id_string.ResourceIdString",
        *,
        config_overrides: Optional[ManagedBlockchainClientConfig] = None,
    ) -> "capo_managedblockchain.types.get_accessor_output.GetAccessorOutput":
        """<p>Returns detailed information about an accessor. An accessor object is a container that has the information required for token based access to your Ethereum nodes.</p>

        Args:
            accessor_id: <p>The unique identifier of the accessor.</p>

        Raises:
            capo_managedblockchain.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action.</p>
            capo_managedblockchain.errors.internal_service_error_exception.InternalServiceErrorException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_managedblockchain.errors.invalid_request_exception.InvalidRequestException: <p>The action or operation requested is invalid. Verify that the action is typed correctly.</p>
            capo_managedblockchain.errors.resource_not_found_exception.ResourceNotFoundException: <p>A requested resource doesn't exist. It may have been deleted or referenced incorrectly.</p>
            capo_managedblockchain.errors.throttling_exception.ThrottlingException: <p>The request or operation couldn't be performed because a service is throttling requests. The most common source of throttling errors is creating resources that exceed your service limit for this resource type. Request a limit increase or delete unused resources if possible.</p>
            capo_managedblockchain.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_managedblockchain.types.get_accessor_input.GetAccessorInput]",
        ) -> OperationResponse[
            "capo_managedblockchain.types.get_accessor_output.GetAccessorOutput"
        ]:
            import capo_managedblockchain._operations.taiga_web_service.get_accessor

            output, http_response = (
                capo_managedblockchain._operations.taiga_web_service.get_accessor.get_accessor(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_managedblockchain.types.get_accessor_input.GetAccessorInput = {
            "accessor_id": accessor_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_member(
        self,
        network_id: "capo_managedblockchain.types.resource_id_string.ResourceIdString",
        member_id: "capo_managedblockchain.types.resource_id_string.ResourceIdString",
        *,
        config_overrides: Optional[ManagedBlockchainClientConfig] = None,
    ) -> "capo_managedblockchain.types.get_member_output.GetMemberOutput":
        """<p>Returns detailed information about a member.</p> <p>Applies only to Hyperledger Fabric.</p>

        Args:
            network_id: <p>The unique identifier of the network to which the member belongs.</p>
            member_id: <p>The unique identifier of the member.</p>

        Raises:
            capo_managedblockchain.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action.</p>
            capo_managedblockchain.errors.internal_service_error_exception.InternalServiceErrorException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_managedblockchain.errors.invalid_request_exception.InvalidRequestException: <p>The action or operation requested is invalid. Verify that the action is typed correctly.</p>
            capo_managedblockchain.errors.resource_not_found_exception.ResourceNotFoundException: <p>A requested resource doesn't exist. It may have been deleted or referenced incorrectly.</p>
            capo_managedblockchain.errors.throttling_exception.ThrottlingException: <p>The request or operation couldn't be performed because a service is throttling requests. The most common source of throttling errors is creating resources that exceed your service limit for this resource type. Request a limit increase or delete unused resources if possible.</p>
            capo_managedblockchain.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_managedblockchain.types.get_member_input.GetMemberInput]",
        ) -> OperationResponse[
            "capo_managedblockchain.types.get_member_output.GetMemberOutput"
        ]:
            import capo_managedblockchain._operations.taiga_web_service.get_member

            output, http_response = (
                capo_managedblockchain._operations.taiga_web_service.get_member.get_member(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_managedblockchain.types.get_member_input.GetMemberInput = {
            "network_id": network_id,
            "member_id": member_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_network(
        self,
        network_id: "capo_managedblockchain.types.resource_id_string.ResourceIdString",
        *,
        config_overrides: Optional[ManagedBlockchainClientConfig] = None,
    ) -> "capo_managedblockchain.types.get_network_output.GetNetworkOutput":
        """<p>Returns detailed information about a network.</p> <p>Applies to Hyperledger Fabric and Ethereum.</p>

        Args:
            network_id: <p>The unique identifier of the network to get information about.</p>

        Raises:
            capo_managedblockchain.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action.</p>
            capo_managedblockchain.errors.internal_service_error_exception.InternalServiceErrorException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_managedblockchain.errors.invalid_request_exception.InvalidRequestException: <p>The action or operation requested is invalid. Verify that the action is typed correctly.</p>
            capo_managedblockchain.errors.resource_not_found_exception.ResourceNotFoundException: <p>A requested resource doesn't exist. It may have been deleted or referenced incorrectly.</p>
            capo_managedblockchain.errors.throttling_exception.ThrottlingException: <p>The request or operation couldn't be performed because a service is throttling requests. The most common source of throttling errors is creating resources that exceed your service limit for this resource type. Request a limit increase or delete unused resources if possible.</p>
            capo_managedblockchain.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_managedblockchain.types.get_network_input.GetNetworkInput]",
        ) -> OperationResponse[
            "capo_managedblockchain.types.get_network_output.GetNetworkOutput"
        ]:
            import capo_managedblockchain._operations.taiga_web_service.get_network

            output, http_response = (
                capo_managedblockchain._operations.taiga_web_service.get_network.get_network(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_managedblockchain.types.get_network_input.GetNetworkInput = {
            "network_id": network_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_node(
        self,
        network_id: "capo_managedblockchain.types.resource_id_string.ResourceIdString",
        node_id: "capo_managedblockchain.types.resource_id_string.ResourceIdString",
        *,
        config_overrides: Optional[ManagedBlockchainClientConfig] = None,
        member_id: Optional[
            "capo_managedblockchain.types.resource_id_string.ResourceIdString"
        ] = None,
    ) -> "capo_managedblockchain.types.get_node_output.GetNodeOutput":
        """<p>Returns detailed information about a node.</p> <p>Applies to Hyperledger Fabric and Ethereum.</p>

        Args:
            network_id: <p>The unique identifier of the network that the node is on.</p>
            member_id: <p>The unique identifier of the member that owns the node.</p> <p>Applies only to Hyperledger Fabric and is required for Hyperledger Fabric.</p>
            node_id: <p>The unique identifier of the node.</p>

        Raises:
            capo_managedblockchain.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action.</p>
            capo_managedblockchain.errors.internal_service_error_exception.InternalServiceErrorException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_managedblockchain.errors.invalid_request_exception.InvalidRequestException: <p>The action or operation requested is invalid. Verify that the action is typed correctly.</p>
            capo_managedblockchain.errors.resource_not_found_exception.ResourceNotFoundException: <p>A requested resource doesn't exist. It may have been deleted or referenced incorrectly.</p>
            capo_managedblockchain.errors.throttling_exception.ThrottlingException: <p>The request or operation couldn't be performed because a service is throttling requests. The most common source of throttling errors is creating resources that exceed your service limit for this resource type. Request a limit increase or delete unused resources if possible.</p>
            capo_managedblockchain.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_managedblockchain.types.get_node_input.GetNodeInput]",
        ) -> OperationResponse[
            "capo_managedblockchain.types.get_node_output.GetNodeOutput"
        ]:
            import capo_managedblockchain._operations.taiga_web_service.get_node

            output, http_response = (
                capo_managedblockchain._operations.taiga_web_service.get_node.get_node(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_managedblockchain.types.get_node_input.GetNodeInput = {
            "network_id": network_id,
            "node_id": node_id,
        }
        if member_id is not None:
            input_["member_id"] = member_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_proposal(
        self,
        network_id: "capo_managedblockchain.types.resource_id_string.ResourceIdString",
        proposal_id: "capo_managedblockchain.types.resource_id_string.ResourceIdString",
        *,
        config_overrides: Optional[ManagedBlockchainClientConfig] = None,
    ) -> "capo_managedblockchain.types.get_proposal_output.GetProposalOutput":
        """<p>Returns detailed information about a proposal.</p> <p>Applies only to Hyperledger Fabric.</p>

        Args:
            network_id: <p>The unique identifier of the network for which the proposal is made.</p>
            proposal_id: <p>The unique identifier of the proposal.</p>

        Raises:
            capo_managedblockchain.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action.</p>
            capo_managedblockchain.errors.internal_service_error_exception.InternalServiceErrorException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_managedblockchain.errors.invalid_request_exception.InvalidRequestException: <p>The action or operation requested is invalid. Verify that the action is typed correctly.</p>
            capo_managedblockchain.errors.resource_not_found_exception.ResourceNotFoundException: <p>A requested resource doesn't exist. It may have been deleted or referenced incorrectly.</p>
            capo_managedblockchain.errors.throttling_exception.ThrottlingException: <p>The request or operation couldn't be performed because a service is throttling requests. The most common source of throttling errors is creating resources that exceed your service limit for this resource type. Request a limit increase or delete unused resources if possible.</p>
            capo_managedblockchain.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_managedblockchain.types.get_proposal_input.GetProposalInput]",
        ) -> OperationResponse[
            "capo_managedblockchain.types.get_proposal_output.GetProposalOutput"
        ]:
            import capo_managedblockchain._operations.taiga_web_service.get_proposal

            output, http_response = (
                capo_managedblockchain._operations.taiga_web_service.get_proposal.get_proposal(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_managedblockchain.types.get_proposal_input.GetProposalInput = {
            "network_id": network_id,
            "proposal_id": proposal_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_accessors(
        self,
        *,
        config_overrides: Optional[ManagedBlockchainClientConfig] = None,
        max_results: Optional[
            "capo_managedblockchain.types.accessor_list_max_results.AccessorListMaxResults"
        ] = None,
        next_token: Optional[
            "capo_managedblockchain.types.pagination_token.PaginationToken"
        ] = None,
        network_type: Optional[
            "capo_managedblockchain.types.accessor_network_type.AccessorNetworkType"
        ] = None,
    ) -> "capo_managedblockchain.types.list_accessors_output.ListAccessorsOutput":
        """<p>Returns a list of the accessors and their properties. Accessor objects are containers that have the information required for token based access to your Ethereum nodes.</p>

        Args:
            max_results: <p> The maximum number of accessors to list.</p>
            next_token: <p> The pagination token that indicates the next set of results to retrieve. </p>
            network_type: <p>The blockchain network that the <code>Accessor</code> token is created for.</p> <note> <p>Use the value <code>ETHEREUM_MAINNET_AND_GOERLI</code> for all existing <code>Accessors</code> tokens that were created before the <code>networkType</code> property was introduced.</p> </note>

        Raises:
            capo_managedblockchain.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action.</p>
            capo_managedblockchain.errors.internal_service_error_exception.InternalServiceErrorException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_managedblockchain.errors.invalid_request_exception.InvalidRequestException: <p>The action or operation requested is invalid. Verify that the action is typed correctly.</p>
            capo_managedblockchain.errors.throttling_exception.ThrottlingException: <p>The request or operation couldn't be performed because a service is throttling requests. The most common source of throttling errors is creating resources that exceed your service limit for this resource type. Request a limit increase or delete unused resources if possible.</p>
            capo_managedblockchain.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_managedblockchain.types.list_accessors_input.ListAccessorsInput]",
        ) -> OperationResponse[
            "capo_managedblockchain.types.list_accessors_output.ListAccessorsOutput"
        ]:
            import capo_managedblockchain._operations.taiga_web_service.list_accessors

            output, http_response = (
                capo_managedblockchain._operations.taiga_web_service.list_accessors.list_accessors(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_managedblockchain.types.list_accessors_input.ListAccessorsInput = {}
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if network_type is not None:
            input_["network_type"] = network_type

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_accessors(
        self,
        *,
        config_overrides: Optional[ManagedBlockchainClientConfig] = None,
        max_results: Optional[
            "capo_managedblockchain.types.accessor_list_max_results.AccessorListMaxResults"
        ] = None,
        next_token: Optional[
            "capo_managedblockchain.types.pagination_token.PaginationToken"
        ] = None,
        network_type: Optional[
            "capo_managedblockchain.types.accessor_network_type.AccessorNetworkType"
        ] = None,
    ) -> "Iterator[capo_managedblockchain.types.accessor_summary.AccessorSummary]":
        _token = next_token
        while True:
            _response = self.list_accessors(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
                network_type=network_type,
            )
            _page = _resolve_path(_response, ("accessors",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_invitations(
        self,
        *,
        config_overrides: Optional[ManagedBlockchainClientConfig] = None,
        max_results: Optional[
            "capo_managedblockchain.types.proposal_list_max_results.ProposalListMaxResults"
        ] = None,
        next_token: Optional[
            "capo_managedblockchain.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "capo_managedblockchain.types.list_invitations_output.ListInvitationsOutput":
        """<p>Returns a list of all invitations for the current Amazon Web Services account.</p> <p>Applies only to Hyperledger Fabric.</p>

        Args:
            max_results: <p>The maximum number of invitations to return.</p>
            next_token: <p>The pagination token that indicates the next set of results to retrieve.</p>

        Raises:
            capo_managedblockchain.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action.</p>
            capo_managedblockchain.errors.internal_service_error_exception.InternalServiceErrorException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_managedblockchain.errors.invalid_request_exception.InvalidRequestException: <p>The action or operation requested is invalid. Verify that the action is typed correctly.</p>
            capo_managedblockchain.errors.resource_limit_exceeded_exception.ResourceLimitExceededException: <p>The maximum number of resources of that type already exist. Ensure the resources requested are within the boundaries of the service edition and your account limits.</p>
            capo_managedblockchain.errors.resource_not_found_exception.ResourceNotFoundException: <p>A requested resource doesn't exist. It may have been deleted or referenced incorrectly.</p>
            capo_managedblockchain.errors.throttling_exception.ThrottlingException: <p>The request or operation couldn't be performed because a service is throttling requests. The most common source of throttling errors is creating resources that exceed your service limit for this resource type. Request a limit increase or delete unused resources if possible.</p>
            capo_managedblockchain.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_managedblockchain.types.list_invitations_input.ListInvitationsInput]",
        ) -> OperationResponse[
            "capo_managedblockchain.types.list_invitations_output.ListInvitationsOutput"
        ]:
            import capo_managedblockchain._operations.taiga_web_service.list_invitations

            output, http_response = (
                capo_managedblockchain._operations.taiga_web_service.list_invitations.list_invitations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_managedblockchain.types.list_invitations_input.ListInvitationsInput = {}
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

    def iter_list_invitations(
        self,
        *,
        config_overrides: Optional[ManagedBlockchainClientConfig] = None,
        max_results: Optional[
            "capo_managedblockchain.types.proposal_list_max_results.ProposalListMaxResults"
        ] = None,
        next_token: Optional[
            "capo_managedblockchain.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "Iterator[capo_managedblockchain.types.list_invitations_output.ListInvitationsOutput]":
        _token = next_token
        while True:
            _response = self.list_invitations(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_members(
        self,
        network_id: "capo_managedblockchain.types.resource_id_string.ResourceIdString",
        *,
        config_overrides: Optional[ManagedBlockchainClientConfig] = None,
        name: Optional["capo_managedblockchain.types.string.String"] = None,
        status: Optional[
            "capo_managedblockchain.types.member_status.MemberStatus"
        ] = None,
        is_owned: Optional["capo_managedblockchain.types.is_owned.IsOwned"] = None,
        max_results: Optional[
            "capo_managedblockchain.types.member_list_max_results.MemberListMaxResults"
        ] = None,
        next_token: Optional[
            "capo_managedblockchain.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "capo_managedblockchain.types.list_members_output.ListMembersOutput":
        """<p>Returns a list of the members in a network and properties of their configurations.</p> <p>Applies only to Hyperledger Fabric.</p>

        Args:
            network_id: <p>The unique identifier of the network for which to list members.</p>
            name: <p>The optional name of the member to list.</p>
            status: <p>An optional status specifier. If provided, only members currently in this status are listed.</p>
            is_owned: <p>An optional Boolean value. If provided, the request is limited either to members that the current Amazon Web Services account owns (<code>true</code>) or that other Amazon Web Services accountsn own (<code>false</code>). If omitted, all members are listed.</p>
            max_results: <p>The maximum number of members to return in the request.</p>
            next_token: <p>The pagination token that indicates the next set of results to retrieve.</p>

        Raises:
            capo_managedblockchain.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action.</p>
            capo_managedblockchain.errors.internal_service_error_exception.InternalServiceErrorException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_managedblockchain.errors.invalid_request_exception.InvalidRequestException: <p>The action or operation requested is invalid. Verify that the action is typed correctly.</p>
            capo_managedblockchain.errors.throttling_exception.ThrottlingException: <p>The request or operation couldn't be performed because a service is throttling requests. The most common source of throttling errors is creating resources that exceed your service limit for this resource type. Request a limit increase or delete unused resources if possible.</p>
            capo_managedblockchain.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_managedblockchain.types.list_members_input.ListMembersInput]",
        ) -> OperationResponse[
            "capo_managedblockchain.types.list_members_output.ListMembersOutput"
        ]:
            import capo_managedblockchain._operations.taiga_web_service.list_members

            output, http_response = (
                capo_managedblockchain._operations.taiga_web_service.list_members.list_members(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_managedblockchain.types.list_members_input.ListMembersInput = {
            "network_id": network_id
        }
        if name is not None:
            input_["name"] = name
        if status is not None:
            input_["status"] = status
        if is_owned is not None:
            input_["is_owned"] = is_owned
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

    def iter_list_members(
        self,
        network_id: "capo_managedblockchain.types.resource_id_string.ResourceIdString",
        *,
        config_overrides: Optional[ManagedBlockchainClientConfig] = None,
        name: Optional["capo_managedblockchain.types.string.String"] = None,
        status: Optional[
            "capo_managedblockchain.types.member_status.MemberStatus"
        ] = None,
        is_owned: Optional["capo_managedblockchain.types.is_owned.IsOwned"] = None,
        max_results: Optional[
            "capo_managedblockchain.types.member_list_max_results.MemberListMaxResults"
        ] = None,
        next_token: Optional[
            "capo_managedblockchain.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "Iterator[capo_managedblockchain.types.list_members_output.ListMembersOutput]":
        _token = next_token
        while True:
            _response = self.list_members(
                network_id,
                config_overrides=config_overrides,
                name=name,
                status=status,
                is_owned=is_owned,
                max_results=max_results,
                next_token=_token,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_networks(
        self,
        *,
        config_overrides: Optional[ManagedBlockchainClientConfig] = None,
        name: Optional["capo_managedblockchain.types.string.String"] = None,
        framework: Optional["capo_managedblockchain.types.framework.Framework"] = None,
        status: Optional[
            "capo_managedblockchain.types.network_status.NetworkStatus"
        ] = None,
        max_results: Optional[
            "capo_managedblockchain.types.network_list_max_results.NetworkListMaxResults"
        ] = None,
        next_token: Optional[
            "capo_managedblockchain.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "capo_managedblockchain.types.list_networks_output.ListNetworksOutput":
        """<p>Returns information about the networks in which the current Amazon Web Services account participates.</p> <p>Applies to Hyperledger Fabric and Ethereum.</p>

        Args:
            name: <p>The name of the network.</p>
            framework: <p>An optional framework specifier. If provided, only networks of this framework type are listed.</p>
            status: <p>An optional status specifier. If provided, only networks currently in this status are listed.</p> <p>Applies only to Hyperledger Fabric.</p>
            max_results: <p>The maximum number of networks to list.</p>
            next_token: <p>The pagination token that indicates the next set of results to retrieve.</p>

        Raises:
            capo_managedblockchain.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action.</p>
            capo_managedblockchain.errors.internal_service_error_exception.InternalServiceErrorException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_managedblockchain.errors.invalid_request_exception.InvalidRequestException: <p>The action or operation requested is invalid. Verify that the action is typed correctly.</p>
            capo_managedblockchain.errors.throttling_exception.ThrottlingException: <p>The request or operation couldn't be performed because a service is throttling requests. The most common source of throttling errors is creating resources that exceed your service limit for this resource type. Request a limit increase or delete unused resources if possible.</p>
            capo_managedblockchain.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_managedblockchain.types.list_networks_input.ListNetworksInput]",
        ) -> OperationResponse[
            "capo_managedblockchain.types.list_networks_output.ListNetworksOutput"
        ]:
            import capo_managedblockchain._operations.taiga_web_service.list_networks

            output, http_response = (
                capo_managedblockchain._operations.taiga_web_service.list_networks.list_networks(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_managedblockchain.types.list_networks_input.ListNetworksInput = {}
        if name is not None:
            input_["name"] = name
        if framework is not None:
            input_["framework"] = framework
        if status is not None:
            input_["status"] = status
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

    def iter_list_networks(
        self,
        *,
        config_overrides: Optional[ManagedBlockchainClientConfig] = None,
        name: Optional["capo_managedblockchain.types.string.String"] = None,
        framework: Optional["capo_managedblockchain.types.framework.Framework"] = None,
        status: Optional[
            "capo_managedblockchain.types.network_status.NetworkStatus"
        ] = None,
        max_results: Optional[
            "capo_managedblockchain.types.network_list_max_results.NetworkListMaxResults"
        ] = None,
        next_token: Optional[
            "capo_managedblockchain.types.pagination_token.PaginationToken"
        ] = None,
    ) -> (
        "Iterator[capo_managedblockchain.types.list_networks_output.ListNetworksOutput]"
    ):
        _token = next_token
        while True:
            _response = self.list_networks(
                config_overrides=config_overrides,
                name=name,
                framework=framework,
                status=status,
                max_results=max_results,
                next_token=_token,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_nodes(
        self,
        network_id: "capo_managedblockchain.types.resource_id_string.ResourceIdString",
        *,
        config_overrides: Optional[ManagedBlockchainClientConfig] = None,
        member_id: Optional[
            "capo_managedblockchain.types.resource_id_string.ResourceIdString"
        ] = None,
        status: Optional["capo_managedblockchain.types.node_status.NodeStatus"] = None,
        max_results: Optional[
            "capo_managedblockchain.types.node_list_max_results.NodeListMaxResults"
        ] = None,
        next_token: Optional[
            "capo_managedblockchain.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "capo_managedblockchain.types.list_nodes_output.ListNodesOutput":
        """<p>Returns information about the nodes within a network.</p> <p>Applies to Hyperledger Fabric and Ethereum.</p>

        Args:
            network_id: <p>The unique identifier of the network for which to list nodes.</p>
            member_id: <p>The unique identifier of the member who owns the nodes to list.</p> <p>Applies only to Hyperledger Fabric and is required for Hyperledger Fabric.</p>
            status: <p>An optional status specifier. If provided, only nodes currently in this status are listed.</p>
            max_results: <p>The maximum number of nodes to list.</p>
            next_token: <p>The pagination token that indicates the next set of results to retrieve.</p>

        Raises:
            capo_managedblockchain.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action.</p>
            capo_managedblockchain.errors.internal_service_error_exception.InternalServiceErrorException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_managedblockchain.errors.invalid_request_exception.InvalidRequestException: <p>The action or operation requested is invalid. Verify that the action is typed correctly.</p>
            capo_managedblockchain.errors.throttling_exception.ThrottlingException: <p>The request or operation couldn't be performed because a service is throttling requests. The most common source of throttling errors is creating resources that exceed your service limit for this resource type. Request a limit increase or delete unused resources if possible.</p>
            capo_managedblockchain.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_managedblockchain.types.list_nodes_input.ListNodesInput]",
        ) -> OperationResponse[
            "capo_managedblockchain.types.list_nodes_output.ListNodesOutput"
        ]:
            import capo_managedblockchain._operations.taiga_web_service.list_nodes

            output, http_response = (
                capo_managedblockchain._operations.taiga_web_service.list_nodes.list_nodes(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_managedblockchain.types.list_nodes_input.ListNodesInput = {
            "network_id": network_id
        }
        if member_id is not None:
            input_["member_id"] = member_id
        if status is not None:
            input_["status"] = status
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

    def iter_list_nodes(
        self,
        network_id: "capo_managedblockchain.types.resource_id_string.ResourceIdString",
        *,
        config_overrides: Optional[ManagedBlockchainClientConfig] = None,
        member_id: Optional[
            "capo_managedblockchain.types.resource_id_string.ResourceIdString"
        ] = None,
        status: Optional["capo_managedblockchain.types.node_status.NodeStatus"] = None,
        max_results: Optional[
            "capo_managedblockchain.types.node_list_max_results.NodeListMaxResults"
        ] = None,
        next_token: Optional[
            "capo_managedblockchain.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "Iterator[capo_managedblockchain.types.list_nodes_output.ListNodesOutput]":
        _token = next_token
        while True:
            _response = self.list_nodes(
                network_id,
                config_overrides=config_overrides,
                member_id=member_id,
                status=status,
                max_results=max_results,
                next_token=_token,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_proposals(
        self,
        network_id: "capo_managedblockchain.types.resource_id_string.ResourceIdString",
        *,
        config_overrides: Optional[ManagedBlockchainClientConfig] = None,
        max_results: Optional[
            "capo_managedblockchain.types.proposal_list_max_results.ProposalListMaxResults"
        ] = None,
        next_token: Optional[
            "capo_managedblockchain.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "capo_managedblockchain.types.list_proposals_output.ListProposalsOutput":
        """<p>Returns a list of proposals for the network.</p> <p>Applies only to Hyperledger Fabric.</p>

        Args:
            network_id: <p> The unique identifier of the network. </p>
            max_results: <p> The maximum number of proposals to return. </p>
            next_token: <p> The pagination token that indicates the next set of results to retrieve. </p>

        Raises:
            capo_managedblockchain.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action.</p>
            capo_managedblockchain.errors.internal_service_error_exception.InternalServiceErrorException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_managedblockchain.errors.invalid_request_exception.InvalidRequestException: <p>The action or operation requested is invalid. Verify that the action is typed correctly.</p>
            capo_managedblockchain.errors.resource_not_found_exception.ResourceNotFoundException: <p>A requested resource doesn't exist. It may have been deleted or referenced incorrectly.</p>
            capo_managedblockchain.errors.throttling_exception.ThrottlingException: <p>The request or operation couldn't be performed because a service is throttling requests. The most common source of throttling errors is creating resources that exceed your service limit for this resource type. Request a limit increase or delete unused resources if possible.</p>
            capo_managedblockchain.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_managedblockchain.types.list_proposals_input.ListProposalsInput]",
        ) -> OperationResponse[
            "capo_managedblockchain.types.list_proposals_output.ListProposalsOutput"
        ]:
            import capo_managedblockchain._operations.taiga_web_service.list_proposals

            output, http_response = (
                capo_managedblockchain._operations.taiga_web_service.list_proposals.list_proposals(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_managedblockchain.types.list_proposals_input.ListProposalsInput = {
            "network_id": network_id
        }
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

    def iter_list_proposals(
        self,
        network_id: "capo_managedblockchain.types.resource_id_string.ResourceIdString",
        *,
        config_overrides: Optional[ManagedBlockchainClientConfig] = None,
        max_results: Optional[
            "capo_managedblockchain.types.proposal_list_max_results.ProposalListMaxResults"
        ] = None,
        next_token: Optional[
            "capo_managedblockchain.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "Iterator[capo_managedblockchain.types.list_proposals_output.ListProposalsOutput]":
        _token = next_token
        while True:
            _response = self.list_proposals(
                network_id,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_proposal_votes(
        self,
        network_id: "capo_managedblockchain.types.resource_id_string.ResourceIdString",
        proposal_id: "capo_managedblockchain.types.resource_id_string.ResourceIdString",
        *,
        config_overrides: Optional[ManagedBlockchainClientConfig] = None,
        max_results: Optional[
            "capo_managedblockchain.types.proposal_list_max_results.ProposalListMaxResults"
        ] = None,
        next_token: Optional[
            "capo_managedblockchain.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "capo_managedblockchain.types.list_proposal_votes_output.ListProposalVotesOutput":
        """<p>Returns the list of votes for a specified proposal, including the value of each vote and the unique identifier of the member that cast the vote.</p> <p>Applies only to Hyperledger Fabric.</p>

        Args:
            network_id: <p> The unique identifier of the network. </p>
            proposal_id: <p> The unique identifier of the proposal. </p>
            max_results: <p> The maximum number of votes to return. </p>
            next_token: <p> The pagination token that indicates the next set of results to retrieve. </p>

        Raises:
            capo_managedblockchain.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action.</p>
            capo_managedblockchain.errors.internal_service_error_exception.InternalServiceErrorException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_managedblockchain.errors.invalid_request_exception.InvalidRequestException: <p>The action or operation requested is invalid. Verify that the action is typed correctly.</p>
            capo_managedblockchain.errors.throttling_exception.ThrottlingException: <p>The request or operation couldn't be performed because a service is throttling requests. The most common source of throttling errors is creating resources that exceed your service limit for this resource type. Request a limit increase or delete unused resources if possible.</p>
            capo_managedblockchain.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_managedblockchain.types.list_proposal_votes_input.ListProposalVotesInput]",
        ) -> OperationResponse[
            "capo_managedblockchain.types.list_proposal_votes_output.ListProposalVotesOutput"
        ]:
            import capo_managedblockchain._operations.taiga_web_service.list_proposal_votes

            output, http_response = (
                capo_managedblockchain._operations.taiga_web_service.list_proposal_votes.list_proposal_votes(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_managedblockchain.types.list_proposal_votes_input.ListProposalVotesInput = {
            "network_id": network_id,
            "proposal_id": proposal_id,
        }
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

    def iter_list_proposal_votes(
        self,
        network_id: "capo_managedblockchain.types.resource_id_string.ResourceIdString",
        proposal_id: "capo_managedblockchain.types.resource_id_string.ResourceIdString",
        *,
        config_overrides: Optional[ManagedBlockchainClientConfig] = None,
        max_results: Optional[
            "capo_managedblockchain.types.proposal_list_max_results.ProposalListMaxResults"
        ] = None,
        next_token: Optional[
            "capo_managedblockchain.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "Iterator[capo_managedblockchain.types.list_proposal_votes_output.ListProposalVotesOutput]":
        _token = next_token
        while True:
            _response = self.list_proposal_votes(
                network_id,
                proposal_id,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_tags_for_resource(
        self,
        resource_arn: "capo_managedblockchain.types.arn_string.ArnString",
        *,
        config_overrides: Optional[ManagedBlockchainClientConfig] = None,
    ) -> "capo_managedblockchain.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>Returns a list of tags for the specified resource. Each tag consists of a key and optional value.</p> <p>For more information about tags, see <a href="https://docs.aws.amazon.com/managed-blockchain/latest/ethereum-dev/tagging-resources.html">Tagging Resources</a> in the <i>Amazon Managed Blockchain Ethereum Developer Guide</i>, or <a href="https://docs.aws.amazon.com/managed-blockchain/latest/hyperledger-fabric-dev/tagging-resources.html">Tagging Resources</a> in the <i>Amazon Managed Blockchain Hyperledger Fabric Developer Guide</i>.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource. For more information about ARNs and their format, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Names (ARNs)</a> in the <i>Amazon Web Services General Reference</i>.</p>

        Raises:
            capo_managedblockchain.errors.internal_service_error_exception.InternalServiceErrorException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_managedblockchain.errors.invalid_request_exception.InvalidRequestException: <p>The action or operation requested is invalid. Verify that the action is typed correctly.</p>
            capo_managedblockchain.errors.resource_not_found_exception.ResourceNotFoundException: <p>A requested resource doesn't exist. It may have been deleted or referenced incorrectly.</p>
            capo_managedblockchain.errors.resource_not_ready_exception.ResourceNotReadyException: <p>The requested resource exists but isn't in a status that can complete the operation.</p>
            capo_managedblockchain.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_managedblockchain.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> OperationResponse[
            "capo_managedblockchain.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import capo_managedblockchain._operations.taiga_web_service.list_tags_for_resource

            output, http_response = (
                capo_managedblockchain._operations.taiga_web_service.list_tags_for_resource.list_tags_for_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_managedblockchain.types.list_tags_for_resource_request.ListTagsForResourceRequest = {
            "resource_arn": resource_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def reject_invitation(
        self,
        invitation_id: "capo_managedblockchain.types.resource_id_string.ResourceIdString",
        *,
        config_overrides: Optional[ManagedBlockchainClientConfig] = None,
    ) -> "capo_managedblockchain.types.reject_invitation_output.RejectInvitationOutput":
        """<p>Rejects an invitation to join a network. This action can be called by a principal in an Amazon Web Services account that has received an invitation to create a member and join a network.</p> <p>Applies only to Hyperledger Fabric.</p>

        Args:
            invitation_id: <p>The unique identifier of the invitation to reject.</p>

        Raises:
            capo_managedblockchain.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action.</p>
            capo_managedblockchain.errors.illegal_action_exception.IllegalActionException: <p></p>
            capo_managedblockchain.errors.internal_service_error_exception.InternalServiceErrorException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_managedblockchain.errors.invalid_request_exception.InvalidRequestException: <p>The action or operation requested is invalid. Verify that the action is typed correctly.</p>
            capo_managedblockchain.errors.resource_not_found_exception.ResourceNotFoundException: <p>A requested resource doesn't exist. It may have been deleted or referenced incorrectly.</p>
            capo_managedblockchain.errors.throttling_exception.ThrottlingException: <p>The request or operation couldn't be performed because a service is throttling requests. The most common source of throttling errors is creating resources that exceed your service limit for this resource type. Request a limit increase or delete unused resources if possible.</p>
            capo_managedblockchain.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_managedblockchain.types.reject_invitation_input.RejectInvitationInput]",
        ) -> OperationResponse[
            "capo_managedblockchain.types.reject_invitation_output.RejectInvitationOutput"
        ]:
            import capo_managedblockchain._operations.taiga_web_service.reject_invitation

            output, http_response = (
                capo_managedblockchain._operations.taiga_web_service.reject_invitation.reject_invitation(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_managedblockchain.types.reject_invitation_input.RejectInvitationInput = {
            "invitation_id": invitation_id
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
        resource_arn: "capo_managedblockchain.types.arn_string.ArnString",
        tags: "capo_managedblockchain.types.input_tag_map.InputTagMap",
        *,
        config_overrides: Optional[ManagedBlockchainClientConfig] = None,
    ) -> "capo_managedblockchain.types.tag_resource_response.TagResourceResponse":
        """<p>Adds or overwrites the specified tags for the specified Amazon Managed Blockchain resource. Each tag consists of a key and optional value.</p> <p>When you specify a tag key that already exists, the tag value is overwritten with the new value. Use <code>UntagResource</code> to remove tag keys.</p> <p>A resource can have up to 50 tags. If you try to create more than 50 tags for a resource, your request fails and returns an error.</p> <p>For more information about tags, see <a href="https://docs.aws.amazon.com/managed-blockchain/latest/ethereum-dev/tagging-resources.html">Tagging Resources</a> in the <i>Amazon Managed Blockchain Ethereum Developer Guide</i>, or <a href="https://docs.aws.amazon.com/managed-blockchain/latest/hyperledger-fabric-dev/tagging-resources.html">Tagging Resources</a> in the <i>Amazon Managed Blockchain Hyperledger Fabric Developer Guide</i>.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource. For more information about ARNs and their format, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Names (ARNs)</a> in the <i>Amazon Web Services General Reference</i>.</p>
            tags: <p>The tags to assign to the specified resource. Tag values can be empty, for example, <code>"MyTagKey" : ""</code>. You can specify multiple key-value pairs in a single request, with an overall maximum of 50 tags added to each resource.</p>

        Raises:
            capo_managedblockchain.errors.internal_service_error_exception.InternalServiceErrorException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_managedblockchain.errors.invalid_request_exception.InvalidRequestException: <p>The action or operation requested is invalid. Verify that the action is typed correctly.</p>
            capo_managedblockchain.errors.resource_not_found_exception.ResourceNotFoundException: <p>A requested resource doesn't exist. It may have been deleted or referenced incorrectly.</p>
            capo_managedblockchain.errors.resource_not_ready_exception.ResourceNotReadyException: <p>The requested resource exists but isn't in a status that can complete the operation.</p>
            capo_managedblockchain.errors.too_many_tags_exception.TooManyTagsException: <p></p>
            capo_managedblockchain.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_managedblockchain.types.tag_resource_request.TagResourceRequest]",
        ) -> OperationResponse[
            "capo_managedblockchain.types.tag_resource_response.TagResourceResponse"
        ]:
            import capo_managedblockchain._operations.taiga_web_service.tag_resource

            output, http_response = (
                capo_managedblockchain._operations.taiga_web_service.tag_resource.tag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_managedblockchain.types.tag_resource_request.TagResourceRequest = {
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
        resource_arn: "capo_managedblockchain.types.arn_string.ArnString",
        tag_keys: "capo_managedblockchain.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[ManagedBlockchainClientConfig] = None,
    ) -> "capo_managedblockchain.types.untag_resource_response.UntagResourceResponse":
        """<p>Removes the specified tags from the Amazon Managed Blockchain resource.</p> <p>For more information about tags, see <a href="https://docs.aws.amazon.com/managed-blockchain/latest/ethereum-dev/tagging-resources.html">Tagging Resources</a> in the <i>Amazon Managed Blockchain Ethereum Developer Guide</i>, or <a href="https://docs.aws.amazon.com/managed-blockchain/latest/hyperledger-fabric-dev/tagging-resources.html">Tagging Resources</a> in the <i>Amazon Managed Blockchain Hyperledger Fabric Developer Guide</i>.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource. For more information about ARNs and their format, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Names (ARNs)</a> in the <i>Amazon Web Services General Reference</i>.</p>
            tag_keys: <p>The tag keys.</p>

        Raises:
            capo_managedblockchain.errors.internal_service_error_exception.InternalServiceErrorException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_managedblockchain.errors.invalid_request_exception.InvalidRequestException: <p>The action or operation requested is invalid. Verify that the action is typed correctly.</p>
            capo_managedblockchain.errors.resource_not_found_exception.ResourceNotFoundException: <p>A requested resource doesn't exist. It may have been deleted or referenced incorrectly.</p>
            capo_managedblockchain.errors.resource_not_ready_exception.ResourceNotReadyException: <p>The requested resource exists but isn't in a status that can complete the operation.</p>
            capo_managedblockchain.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_managedblockchain.types.untag_resource_request.UntagResourceRequest]",
        ) -> OperationResponse[
            "capo_managedblockchain.types.untag_resource_response.UntagResourceResponse"
        ]:
            import capo_managedblockchain._operations.taiga_web_service.untag_resource

            output, http_response = (
                capo_managedblockchain._operations.taiga_web_service.untag_resource.untag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_managedblockchain.types.untag_resource_request.UntagResourceRequest = {
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

    def update_member(
        self,
        network_id: "capo_managedblockchain.types.resource_id_string.ResourceIdString",
        member_id: "capo_managedblockchain.types.resource_id_string.ResourceIdString",
        *,
        config_overrides: Optional[ManagedBlockchainClientConfig] = None,
        log_publishing_configuration: Optional[
            "capo_managedblockchain.types.member_log_publishing_configuration.MemberLogPublishingConfiguration"
        ] = None,
    ) -> "capo_managedblockchain.types.update_member_output.UpdateMemberOutput":
        """<p>Updates a member configuration with new parameters.</p> <p>Applies only to Hyperledger Fabric.</p>

        Args:
            network_id: <p>The unique identifier of the Managed Blockchain network to which the member belongs.</p>
            member_id: <p>The unique identifier of the member.</p>
            log_publishing_configuration: <p>Configuration properties for publishing to Amazon CloudWatch Logs.</p>

        Raises:
            capo_managedblockchain.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action.</p>
            capo_managedblockchain.errors.internal_service_error_exception.InternalServiceErrorException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_managedblockchain.errors.invalid_request_exception.InvalidRequestException: <p>The action or operation requested is invalid. Verify that the action is typed correctly.</p>
            capo_managedblockchain.errors.resource_not_found_exception.ResourceNotFoundException: <p>A requested resource doesn't exist. It may have been deleted or referenced incorrectly.</p>
            capo_managedblockchain.errors.throttling_exception.ThrottlingException: <p>The request or operation couldn't be performed because a service is throttling requests. The most common source of throttling errors is creating resources that exceed your service limit for this resource type. Request a limit increase or delete unused resources if possible.</p>
            capo_managedblockchain.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_managedblockchain.types.update_member_input.UpdateMemberInput]",
        ) -> OperationResponse[
            "capo_managedblockchain.types.update_member_output.UpdateMemberOutput"
        ]:
            import capo_managedblockchain._operations.taiga_web_service.update_member

            output, http_response = (
                capo_managedblockchain._operations.taiga_web_service.update_member.update_member(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_managedblockchain.types.update_member_input.UpdateMemberInput = {
            "network_id": network_id,
            "member_id": member_id,
        }
        if log_publishing_configuration is not None:
            input_["log_publishing_configuration"] = log_publishing_configuration

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_node(
        self,
        network_id: "capo_managedblockchain.types.resource_id_string.ResourceIdString",
        node_id: "capo_managedblockchain.types.resource_id_string.ResourceIdString",
        *,
        config_overrides: Optional[ManagedBlockchainClientConfig] = None,
        member_id: Optional[
            "capo_managedblockchain.types.resource_id_string.ResourceIdString"
        ] = None,
        log_publishing_configuration: Optional[
            "capo_managedblockchain.types.node_log_publishing_configuration.NodeLogPublishingConfiguration"
        ] = None,
    ) -> "capo_managedblockchain.types.update_node_output.UpdateNodeOutput":
        """<p>Updates a node configuration with new parameters.</p> <p>Applies only to Hyperledger Fabric.</p>

        Args:
            network_id: <p>The unique identifier of the network that the node is on.</p>
            member_id: <p>The unique identifier of the member that owns the node.</p> <p>Applies only to Hyperledger Fabric.</p>
            node_id: <p>The unique identifier of the node.</p>
            log_publishing_configuration: <p>Configuration properties for publishing to Amazon CloudWatch Logs.</p>

        Raises:
            capo_managedblockchain.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action.</p>
            capo_managedblockchain.errors.internal_service_error_exception.InternalServiceErrorException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_managedblockchain.errors.invalid_request_exception.InvalidRequestException: <p>The action or operation requested is invalid. Verify that the action is typed correctly.</p>
            capo_managedblockchain.errors.resource_not_found_exception.ResourceNotFoundException: <p>A requested resource doesn't exist. It may have been deleted or referenced incorrectly.</p>
            capo_managedblockchain.errors.throttling_exception.ThrottlingException: <p>The request or operation couldn't be performed because a service is throttling requests. The most common source of throttling errors is creating resources that exceed your service limit for this resource type. Request a limit increase or delete unused resources if possible.</p>
            capo_managedblockchain.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_managedblockchain.types.update_node_input.UpdateNodeInput]",
        ) -> OperationResponse[
            "capo_managedblockchain.types.update_node_output.UpdateNodeOutput"
        ]:
            import capo_managedblockchain._operations.taiga_web_service.update_node

            output, http_response = (
                capo_managedblockchain._operations.taiga_web_service.update_node.update_node(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_managedblockchain.types.update_node_input.UpdateNodeInput = {
            "network_id": network_id,
            "node_id": node_id,
        }
        if member_id is not None:
            input_["member_id"] = member_id
        if log_publishing_configuration is not None:
            input_["log_publishing_configuration"] = log_publishing_configuration

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def vote_on_proposal(
        self,
        network_id: "capo_managedblockchain.types.resource_id_string.ResourceIdString",
        proposal_id: "capo_managedblockchain.types.resource_id_string.ResourceIdString",
        voter_member_id: "capo_managedblockchain.types.resource_id_string.ResourceIdString",
        vote: "capo_managedblockchain.types.vote_value.VoteValue",
        *,
        config_overrides: Optional[ManagedBlockchainClientConfig] = None,
    ) -> "capo_managedblockchain.types.vote_on_proposal_output.VoteOnProposalOutput":
        """<p>Casts a vote for a specified <code>ProposalId</code> on behalf of a member. The member to vote as, specified by <code>VoterMemberId</code>, must be in the same Amazon Web Services account as the principal that calls the action.</p> <p>Applies only to Hyperledger Fabric.</p>

        Args:
            network_id: <p> The unique identifier of the network. </p>
            proposal_id: <p> The unique identifier of the proposal. </p>
            voter_member_id: <p>The unique identifier of the member casting the vote. </p>
            vote: <p> The value of the vote. </p>

        Raises:
            capo_managedblockchain.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action.</p>
            capo_managedblockchain.errors.illegal_action_exception.IllegalActionException: <p></p>
            capo_managedblockchain.errors.internal_service_error_exception.InternalServiceErrorException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_managedblockchain.errors.invalid_request_exception.InvalidRequestException: <p>The action or operation requested is invalid. Verify that the action is typed correctly.</p>
            capo_managedblockchain.errors.resource_not_found_exception.ResourceNotFoundException: <p>A requested resource doesn't exist. It may have been deleted or referenced incorrectly.</p>
            capo_managedblockchain.errors.throttling_exception.ThrottlingException: <p>The request or operation couldn't be performed because a service is throttling requests. The most common source of throttling errors is creating resources that exceed your service limit for this resource type. Request a limit increase or delete unused resources if possible.</p>
            capo_managedblockchain.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_managedblockchain.types.vote_on_proposal_input.VoteOnProposalInput]",
        ) -> OperationResponse[
            "capo_managedblockchain.types.vote_on_proposal_output.VoteOnProposalOutput"
        ]:
            import capo_managedblockchain._operations.taiga_web_service.vote_on_proposal

            output, http_response = (
                capo_managedblockchain._operations.taiga_web_service.vote_on_proposal.vote_on_proposal(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_managedblockchain.types.vote_on_proposal_input.VoteOnProposalInput = {
            "network_id": network_id,
            "proposal_id": proposal_id,
            "voter_member_id": voter_member_id,
            "vote": vote,
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
