"""Generated from Smithy shape ``com.amazonaws.managedblockchainquery#TietonChainQueryService``."""

import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import AsyncBaseHandler, AsyncClient

import capo_managedblockchain_query._auth._signers
import capo_managedblockchain_query._auth._sigv4
from capo_managedblockchain_query._auth._identity import Credentials
from capo_managedblockchain_query._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_managedblockchain_query._auth._zapros_handler import AuthMiddleware
from capo_managedblockchain_query._pagination import resolve_path as _resolve_path
from capo_managedblockchain_query._services._aws_config import aaws_config
from capo_managedblockchain_query._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import capo_managedblockchain_query.types.address_identifier_filter
    import capo_managedblockchain_query.types.asset_contract
    import capo_managedblockchain_query.types.batch_get_token_balance_input
    import capo_managedblockchain_query.types.batch_get_token_balance_output
    import capo_managedblockchain_query.types.blockchain_instant
    import capo_managedblockchain_query.types.chain_address
    import capo_managedblockchain_query.types.confirmation_status_filter
    import capo_managedblockchain_query.types.contract_filter
    import capo_managedblockchain_query.types.contract_identifier
    import capo_managedblockchain_query.types.get_asset_contract_input
    import capo_managedblockchain_query.types.get_asset_contract_output
    import capo_managedblockchain_query.types.get_token_balance_input
    import capo_managedblockchain_query.types.get_token_balance_input_list
    import capo_managedblockchain_query.types.get_token_balance_output
    import capo_managedblockchain_query.types.get_transaction_input
    import capo_managedblockchain_query.types.get_transaction_output
    import capo_managedblockchain_query.types.list_asset_contracts_input
    import capo_managedblockchain_query.types.list_asset_contracts_output
    import capo_managedblockchain_query.types.list_filtered_transaction_events_input
    import capo_managedblockchain_query.types.list_filtered_transaction_events_output
    import capo_managedblockchain_query.types.list_filtered_transaction_events_sort
    import capo_managedblockchain_query.types.list_token_balances_input
    import capo_managedblockchain_query.types.list_token_balances_output
    import capo_managedblockchain_query.types.list_transaction_events_input
    import capo_managedblockchain_query.types.list_transaction_events_output
    import capo_managedblockchain_query.types.list_transactions_input
    import capo_managedblockchain_query.types.list_transactions_output
    import capo_managedblockchain_query.types.list_transactions_sort
    import capo_managedblockchain_query.types.next_token
    import capo_managedblockchain_query.types.owner_filter
    import capo_managedblockchain_query.types.owner_identifier
    import capo_managedblockchain_query.types.query_network
    import capo_managedblockchain_query.types.query_transaction_hash
    import capo_managedblockchain_query.types.query_transaction_id
    import capo_managedblockchain_query.types.time_filter
    import capo_managedblockchain_query.types.token_balance
    import capo_managedblockchain_query.types.token_filter
    import capo_managedblockchain_query.types.token_identifier
    import capo_managedblockchain_query.types.transaction_event
    import capo_managedblockchain_query.types.transaction_output_item
    import capo_managedblockchain_query.types.vout_filter


class AsyncManagedBlockchainQueryClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class AsyncManagedBlockchainQueryClient:
    """A client for the ``ManagedBlockchainQuery`` service.

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
        http_handler: AsyncBaseHandler | None = None,
        operation_interceptors: Iterable[AsyncInterceptor[Any, Any]] | None = None,
        retry_max_attempts: int | None = None,
        region: str | None = None,
        use_dual_stack: bool | None = None,
        use_fips: bool | None = None,
        endpoint: str | None = None,
        credentials: Credentials | None = None,
        credentials_provider: CredentialsProvider | None = None,
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
        self._config = AsyncManagedBlockchainQueryClientConfig(
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

    def operation_options(
        self, config_overrides: Optional[AsyncManagedBlockchainQueryClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncManagedBlockchainQueryClientConfig = config_overrides or {}
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
        )
        return interceptors_, options_

    async def batch_get_token_balance(
        self,
        *,
        config_overrides: Optional[AsyncManagedBlockchainQueryClientConfig] = None,
        get_token_balance_inputs: Optional[
            "capo_managedblockchain_query.types.get_token_balance_input_list.GetTokenBalanceInputList"
        ] = None,
    ) -> "capo_managedblockchain_query.types.batch_get_token_balance_output.BatchGetTokenBalanceOutput":
        """<p>Gets the token balance for a batch of tokens by using the <code>BatchGetTokenBalance</code> action for every token in the request.</p> <note> <p>Only the native tokens BTC and ETH, and the ERC-20, ERC-721, and ERC 1155 token standards are supported.</p> </note>

        Args:
            get_token_balance_inputs: <p>An array of <code>BatchGetTokenBalanceInputItem</code> objects whose balance is being requested.</p>

        Raises:
            capo_managedblockchain_query.errors.access_denied_exception.AccessDeniedException: <p>The Amazon Web Services account doesn’t have access to this resource. </p>
            capo_managedblockchain_query.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an internal error in the service.</p>
            capo_managedblockchain_query.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource was not found.</p>
            capo_managedblockchain_query.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The service quota has been exceeded for this resource.</p>
            capo_managedblockchain_query.errors.throttling_exception.ThrottlingException: <p>The request or operation couldn't be performed because a service is throttling requests. The most common source of throttling errors is when you create resources that exceed your service limit for this resource type. Request a limit increase or delete unused resources, if possible.</p>
            capo_managedblockchain_query.errors.validation_exception.ValidationException: <p>The resource passed is invalid.</p>
            capo_managedblockchain_query.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_managedblockchain_query.types.batch_get_token_balance_input.BatchGetTokenBalanceInput]",
        ) -> AsyncOperationResponse[
            "capo_managedblockchain_query.types.batch_get_token_balance_output.BatchGetTokenBalanceOutput"
        ]:
            import capo_managedblockchain_query._operations.tieton_chain_query_service.batch_get_token_balance

            (
                output,
                http_response,
            ) = await capo_managedblockchain_query._operations.tieton_chain_query_service.batch_get_token_balance.async_batch_get_token_balance(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_managedblockchain_query.types.batch_get_token_balance_input.BatchGetTokenBalanceInput = {}
        if get_token_balance_inputs is not None:
            input_["get_token_balance_inputs"] = get_token_balance_inputs

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_asset_contract(
        self,
        contract_identifier: "capo_managedblockchain_query.types.contract_identifier.ContractIdentifier",
        *,
        config_overrides: Optional[AsyncManagedBlockchainQueryClientConfig] = None,
    ) -> "capo_managedblockchain_query.types.get_asset_contract_output.GetAssetContractOutput":
        """<p>Gets the information about a specific contract deployed on the blockchain.</p> <note> <ul> <li> <p>The Bitcoin blockchain networks do not support this operation.</p> </li> <li> <p>Metadata is currently only available for some <code>ERC-20</code> contracts. Metadata will be available for additional contracts in the future.</p> </li> </ul> </note>

        Args:
            contract_identifier: <p>Contains the blockchain address and network information about the contract.</p>

        Raises:
            capo_managedblockchain_query.errors.access_denied_exception.AccessDeniedException: <p>The Amazon Web Services account doesn’t have access to this resource. </p>
            capo_managedblockchain_query.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an internal error in the service.</p>
            capo_managedblockchain_query.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource was not found.</p>
            capo_managedblockchain_query.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The service quota has been exceeded for this resource.</p>
            capo_managedblockchain_query.errors.throttling_exception.ThrottlingException: <p>The request or operation couldn't be performed because a service is throttling requests. The most common source of throttling errors is when you create resources that exceed your service limit for this resource type. Request a limit increase or delete unused resources, if possible.</p>
            capo_managedblockchain_query.errors.validation_exception.ValidationException: <p>The resource passed is invalid.</p>
            capo_managedblockchain_query.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_managedblockchain_query.types.get_asset_contract_input.GetAssetContractInput]",
        ) -> AsyncOperationResponse[
            "capo_managedblockchain_query.types.get_asset_contract_output.GetAssetContractOutput"
        ]:
            import capo_managedblockchain_query._operations.tieton_chain_query_service.get_asset_contract

            (
                output,
                http_response,
            ) = await capo_managedblockchain_query._operations.tieton_chain_query_service.get_asset_contract.async_get_asset_contract(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_managedblockchain_query.types.get_asset_contract_input.GetAssetContractInput = {
            "contract_identifier": contract_identifier
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_token_balance(
        self,
        token_identifier: "capo_managedblockchain_query.types.token_identifier.TokenIdentifier",
        owner_identifier: "capo_managedblockchain_query.types.owner_identifier.OwnerIdentifier",
        *,
        config_overrides: Optional[AsyncManagedBlockchainQueryClientConfig] = None,
        at_blockchain_instant: Optional[
            "capo_managedblockchain_query.types.blockchain_instant.BlockchainInstant"
        ] = None,
    ) -> "capo_managedblockchain_query.types.get_token_balance_output.GetTokenBalanceOutput":
        """<p>Gets the balance of a specific token, including native tokens, for a given address (wallet or contract) on the blockchain.</p> <note> <p>Only the native tokens BTC and ETH, and the ERC-20, ERC-721, and ERC 1155 token standards are supported.</p> </note>

        Args:
            token_identifier: <p>The container for the identifier for the token, including the unique token ID and its blockchain network.</p>
            owner_identifier: <p>The container for the identifier for the owner.</p>
            at_blockchain_instant: <p>The time for when the TokenBalance is requested or the current time if a time is not provided in the request.</p> <note> <p>This time will only be recorded up to the second.</p> </note>

        Raises:
            capo_managedblockchain_query.errors.access_denied_exception.AccessDeniedException: <p>The Amazon Web Services account doesn’t have access to this resource. </p>
            capo_managedblockchain_query.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an internal error in the service.</p>
            capo_managedblockchain_query.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource was not found.</p>
            capo_managedblockchain_query.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The service quota has been exceeded for this resource.</p>
            capo_managedblockchain_query.errors.throttling_exception.ThrottlingException: <p>The request or operation couldn't be performed because a service is throttling requests. The most common source of throttling errors is when you create resources that exceed your service limit for this resource type. Request a limit increase or delete unused resources, if possible.</p>
            capo_managedblockchain_query.errors.validation_exception.ValidationException: <p>The resource passed is invalid.</p>
            capo_managedblockchain_query.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_managedblockchain_query.types.get_token_balance_input.GetTokenBalanceInput]",
        ) -> AsyncOperationResponse[
            "capo_managedblockchain_query.types.get_token_balance_output.GetTokenBalanceOutput"
        ]:
            import capo_managedblockchain_query._operations.tieton_chain_query_service.get_token_balance

            (
                output,
                http_response,
            ) = await capo_managedblockchain_query._operations.tieton_chain_query_service.get_token_balance.async_get_token_balance(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_managedblockchain_query.types.get_token_balance_input.GetTokenBalanceInput = {
            "token_identifier": token_identifier,
            "owner_identifier": owner_identifier,
        }
        if at_blockchain_instant is not None:
            input_["at_blockchain_instant"] = at_blockchain_instant

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_transaction(
        self,
        network: "capo_managedblockchain_query.types.query_network.QueryNetwork",
        *,
        config_overrides: Optional[AsyncManagedBlockchainQueryClientConfig] = None,
        transaction_hash: Optional[
            "capo_managedblockchain_query.types.query_transaction_hash.QueryTransactionHash"
        ] = None,
        transaction_id: Optional[
            "capo_managedblockchain_query.types.query_transaction_id.QueryTransactionId"
        ] = None,
    ) -> (
        "capo_managedblockchain_query.types.get_transaction_output.GetTransactionOutput"
    ):
        """<p>Gets the details of a transaction.</p> <note> <p>This action will return transaction details for all transactions that are <i>confirmed</i> on the blockchain, even if they have not reached <a href="https://docs.aws.amazon.com/managed-blockchain/latest/ambq-dg/key-concepts.html#finality">finality</a>. </p> </note>

        Args:
            transaction_hash: <p>The hash of a transaction. It is generated when a transaction is created.</p>
            transaction_id: <p>The identifier of a Bitcoin transaction. It is generated when a transaction is created.</p> <note> <p> <code>transactionId</code> is only supported on the Bitcoin networks.</p> </note>
            network: <p>The blockchain network where the transaction occurred.</p>

        Raises:
            capo_managedblockchain_query.errors.access_denied_exception.AccessDeniedException: <p>The Amazon Web Services account doesn’t have access to this resource. </p>
            capo_managedblockchain_query.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an internal error in the service.</p>
            capo_managedblockchain_query.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource was not found.</p>
            capo_managedblockchain_query.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The service quota has been exceeded for this resource.</p>
            capo_managedblockchain_query.errors.throttling_exception.ThrottlingException: <p>The request or operation couldn't be performed because a service is throttling requests. The most common source of throttling errors is when you create resources that exceed your service limit for this resource type. Request a limit increase or delete unused resources, if possible.</p>
            capo_managedblockchain_query.errors.validation_exception.ValidationException: <p>The resource passed is invalid.</p>
            capo_managedblockchain_query.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_managedblockchain_query.types.get_transaction_input.GetTransactionInput]",
        ) -> AsyncOperationResponse[
            "capo_managedblockchain_query.types.get_transaction_output.GetTransactionOutput"
        ]:
            import capo_managedblockchain_query._operations.tieton_chain_query_service.get_transaction

            (
                output,
                http_response,
            ) = await capo_managedblockchain_query._operations.tieton_chain_query_service.get_transaction.async_get_transaction(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_managedblockchain_query.types.get_transaction_input.GetTransactionInput = {
            "network": network
        }
        if transaction_hash is not None:
            input_["transaction_hash"] = transaction_hash
        if transaction_id is not None:
            input_["transaction_id"] = transaction_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_asset_contracts(
        self,
        contract_filter: "capo_managedblockchain_query.types.contract_filter.ContractFilter",
        *,
        config_overrides: Optional[AsyncManagedBlockchainQueryClientConfig] = None,
        next_token: Optional[
            "capo_managedblockchain_query.types.next_token.NextToken"
        ] = None,
        max_results: Optional[int] = None,
    ) -> "capo_managedblockchain_query.types.list_asset_contracts_output.ListAssetContractsOutput":
        """<p>Lists all the contracts for a given contract type deployed by an address (either a contract address or a wallet address).</p> <p>The Bitcoin blockchain networks do not support this operation.</p>

        Args:
            contract_filter: <p>Contains the filter parameter for the request.</p>
            next_token: <p> The pagination token that indicates the next set of results to retrieve.</p>
            max_results: <p>The maximum number of contracts to list.</p> <p>Default: <code>100</code> </p> <note> <p>Even if additional results can be retrieved, the request can return less results than <code>maxResults</code> or an empty array of results.</p> <p>To retrieve the next set of results, make another request with the returned <code>nextToken</code> value. The value of <code>nextToken</code> is <code>null</code> when there are no more results to return</p> </note>

        Raises:
            capo_managedblockchain_query.errors.access_denied_exception.AccessDeniedException: <p>The Amazon Web Services account doesn’t have access to this resource. </p>
            capo_managedblockchain_query.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an internal error in the service.</p>
            capo_managedblockchain_query.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The service quota has been exceeded for this resource.</p>
            capo_managedblockchain_query.errors.throttling_exception.ThrottlingException: <p>The request or operation couldn't be performed because a service is throttling requests. The most common source of throttling errors is when you create resources that exceed your service limit for this resource type. Request a limit increase or delete unused resources, if possible.</p>
            capo_managedblockchain_query.errors.validation_exception.ValidationException: <p>The resource passed is invalid.</p>
            capo_managedblockchain_query.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_managedblockchain_query.types.list_asset_contracts_input.ListAssetContractsInput]",
        ) -> AsyncOperationResponse[
            "capo_managedblockchain_query.types.list_asset_contracts_output.ListAssetContractsOutput"
        ]:
            import capo_managedblockchain_query._operations.tieton_chain_query_service.list_asset_contracts

            (
                output,
                http_response,
            ) = await capo_managedblockchain_query._operations.tieton_chain_query_service.list_asset_contracts.async_list_asset_contracts(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_managedblockchain_query.types.list_asset_contracts_input.ListAssetContractsInput = {
            "contract_filter": contract_filter
        }
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

    async def iter_list_asset_contracts(
        self,
        contract_filter: "capo_managedblockchain_query.types.contract_filter.ContractFilter",
        *,
        config_overrides: Optional[AsyncManagedBlockchainQueryClientConfig] = None,
        next_token: Optional[
            "capo_managedblockchain_query.types.next_token.NextToken"
        ] = None,
        max_results: Optional[int] = None,
    ) -> (
        "AsyncIterator[capo_managedblockchain_query.types.asset_contract.AssetContract]"
    ):
        _token = next_token
        while True:
            _response = await self.list_asset_contracts(
                contract_filter,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("contracts",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_filtered_transaction_events(
        self,
        network: str,
        address_identifier_filter: "capo_managedblockchain_query.types.address_identifier_filter.AddressIdentifierFilter",
        *,
        config_overrides: Optional[AsyncManagedBlockchainQueryClientConfig] = None,
        time_filter: Optional[
            "capo_managedblockchain_query.types.time_filter.TimeFilter"
        ] = None,
        vout_filter: Optional[
            "capo_managedblockchain_query.types.vout_filter.VoutFilter"
        ] = None,
        confirmation_status_filter: Optional[
            "capo_managedblockchain_query.types.confirmation_status_filter.ConfirmationStatusFilter"
        ] = None,
        sort: Optional[
            "capo_managedblockchain_query.types.list_filtered_transaction_events_sort.ListFilteredTransactionEventsSort"
        ] = None,
        next_token: Optional[
            "capo_managedblockchain_query.types.next_token.NextToken"
        ] = None,
        max_results: Optional[int] = None,
    ) -> "capo_managedblockchain_query.types.list_filtered_transaction_events_output.ListFilteredTransactionEventsOutput":
        """<p>Lists all the transaction events for an address on the blockchain.</p> <note> <p>This operation is only supported on the Bitcoin networks.</p> </note>

        Args:
            network: <p>The blockchain network where the transaction occurred.</p> <p>Valid Values: <code>BITCOIN_MAINNET</code> | <code>BITCOIN_TESTNET</code> </p>
            address_identifier_filter: <p>This is the unique public address on the blockchain for which the transaction events are being requested.</p>
            time_filter: <p>This container specifies the time frame for the transaction events returned in the response.</p>
            vout_filter: <p>This container specifies filtering attributes related to BITCOIN_VOUT event types</p>
            sort: <p>The order by which the results will be sorted.</p>
            next_token: <p>The pagination token that indicates the next set of results to retrieve.</p>
            max_results: <p>The maximum number of transaction events to list.</p> <p>Default: <code>100</code> </p> <note> <p>Even if additional results can be retrieved, the request can return less results than <code>maxResults</code> or an empty array of results.</p> <p>To retrieve the next set of results, make another request with the returned <code>nextToken</code> value. The value of <code>nextToken</code> is <code>null</code> when there are no more results to return</p> </note>

        Raises:
            capo_managedblockchain_query.errors.access_denied_exception.AccessDeniedException: <p>The Amazon Web Services account doesn’t have access to this resource. </p>
            capo_managedblockchain_query.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an internal error in the service.</p>
            capo_managedblockchain_query.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The service quota has been exceeded for this resource.</p>
            capo_managedblockchain_query.errors.throttling_exception.ThrottlingException: <p>The request or operation couldn't be performed because a service is throttling requests. The most common source of throttling errors is when you create resources that exceed your service limit for this resource type. Request a limit increase or delete unused resources, if possible.</p>
            capo_managedblockchain_query.errors.validation_exception.ValidationException: <p>The resource passed is invalid.</p>
            capo_managedblockchain_query.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_managedblockchain_query.types.list_filtered_transaction_events_input.ListFilteredTransactionEventsInput]",
        ) -> AsyncOperationResponse[
            "capo_managedblockchain_query.types.list_filtered_transaction_events_output.ListFilteredTransactionEventsOutput"
        ]:
            import capo_managedblockchain_query._operations.tieton_chain_query_service.list_filtered_transaction_events

            (
                output,
                http_response,
            ) = await capo_managedblockchain_query._operations.tieton_chain_query_service.list_filtered_transaction_events.async_list_filtered_transaction_events(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_managedblockchain_query.types.list_filtered_transaction_events_input.ListFilteredTransactionEventsInput = {
            "network": network,
            "address_identifier_filter": address_identifier_filter,
        }
        if time_filter is not None:
            input_["time_filter"] = time_filter
        if vout_filter is not None:
            input_["vout_filter"] = vout_filter
        if confirmation_status_filter is not None:
            input_["confirmation_status_filter"] = confirmation_status_filter
        if sort is not None:
            input_["sort"] = sort
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

    async def iter_list_filtered_transaction_events(
        self,
        network: str,
        address_identifier_filter: "capo_managedblockchain_query.types.address_identifier_filter.AddressIdentifierFilter",
        *,
        config_overrides: Optional[AsyncManagedBlockchainQueryClientConfig] = None,
        time_filter: Optional[
            "capo_managedblockchain_query.types.time_filter.TimeFilter"
        ] = None,
        vout_filter: Optional[
            "capo_managedblockchain_query.types.vout_filter.VoutFilter"
        ] = None,
        confirmation_status_filter: Optional[
            "capo_managedblockchain_query.types.confirmation_status_filter.ConfirmationStatusFilter"
        ] = None,
        sort: Optional[
            "capo_managedblockchain_query.types.list_filtered_transaction_events_sort.ListFilteredTransactionEventsSort"
        ] = None,
        next_token: Optional[
            "capo_managedblockchain_query.types.next_token.NextToken"
        ] = None,
        max_results: Optional[int] = None,
    ) -> "AsyncIterator[capo_managedblockchain_query.types.transaction_event.TransactionEvent]":
        _token = next_token
        while True:
            _response = await self.list_filtered_transaction_events(
                network,
                address_identifier_filter,
                config_overrides=config_overrides,
                time_filter=time_filter,
                vout_filter=vout_filter,
                confirmation_status_filter=confirmation_status_filter,
                sort=sort,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("events",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_token_balances(
        self,
        token_filter: "capo_managedblockchain_query.types.token_filter.TokenFilter",
        *,
        config_overrides: Optional[AsyncManagedBlockchainQueryClientConfig] = None,
        owner_filter: Optional[
            "capo_managedblockchain_query.types.owner_filter.OwnerFilter"
        ] = None,
        next_token: Optional[
            "capo_managedblockchain_query.types.next_token.NextToken"
        ] = None,
        max_results: Optional[int] = None,
    ) -> "capo_managedblockchain_query.types.list_token_balances_output.ListTokenBalancesOutput":
        """<p>This action returns the following for a given blockchain network:</p> <ul> <li> <p>Lists all token balances owned by an address (either a contract address or a wallet address).</p> </li> <li> <p>Lists all token balances for all tokens created by a contract.</p> </li> <li> <p>Lists all token balances for a given token.</p> </li> </ul> <note> <p>You must always specify the network property of the <code>tokenFilter</code> when using this operation.</p> </note>

        Args:
            owner_filter: <p>The contract or wallet address on the blockchain network by which to filter the request. You must specify the <code>address</code> property of the <code>ownerFilter</code> when listing balances of tokens owned by the address.</p>
            token_filter: <p>The contract address or a token identifier on the blockchain network by which to filter the request. You must specify the <code>contractAddress</code> property of this container when listing tokens minted by a contract.</p> <note> <p>You must always specify the network property of this container when using this operation.</p> </note>
            next_token: <p>The pagination token that indicates the next set of results to retrieve.</p>
            max_results: <p>The maximum number of token balances to return.</p> <p>Default: <code>100</code> </p> <note> <p>Even if additional results can be retrieved, the request can return less results than <code>maxResults</code> or an empty array of results.</p> <p>To retrieve the next set of results, make another request with the returned <code>nextToken</code> value. The value of <code>nextToken</code> is <code>null</code> when there are no more results to return</p> </note>

        Raises:
            capo_managedblockchain_query.errors.access_denied_exception.AccessDeniedException: <p>The Amazon Web Services account doesn’t have access to this resource. </p>
            capo_managedblockchain_query.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an internal error in the service.</p>
            capo_managedblockchain_query.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The service quota has been exceeded for this resource.</p>
            capo_managedblockchain_query.errors.throttling_exception.ThrottlingException: <p>The request or operation couldn't be performed because a service is throttling requests. The most common source of throttling errors is when you create resources that exceed your service limit for this resource type. Request a limit increase or delete unused resources, if possible.</p>
            capo_managedblockchain_query.errors.validation_exception.ValidationException: <p>The resource passed is invalid.</p>
            capo_managedblockchain_query.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_managedblockchain_query.types.list_token_balances_input.ListTokenBalancesInput]",
        ) -> AsyncOperationResponse[
            "capo_managedblockchain_query.types.list_token_balances_output.ListTokenBalancesOutput"
        ]:
            import capo_managedblockchain_query._operations.tieton_chain_query_service.list_token_balances

            (
                output,
                http_response,
            ) = await capo_managedblockchain_query._operations.tieton_chain_query_service.list_token_balances.async_list_token_balances(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_managedblockchain_query.types.list_token_balances_input.ListTokenBalancesInput = {
            "token_filter": token_filter
        }
        if owner_filter is not None:
            input_["owner_filter"] = owner_filter
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

    async def iter_list_token_balances(
        self,
        token_filter: "capo_managedblockchain_query.types.token_filter.TokenFilter",
        *,
        config_overrides: Optional[AsyncManagedBlockchainQueryClientConfig] = None,
        owner_filter: Optional[
            "capo_managedblockchain_query.types.owner_filter.OwnerFilter"
        ] = None,
        next_token: Optional[
            "capo_managedblockchain_query.types.next_token.NextToken"
        ] = None,
        max_results: Optional[int] = None,
    ) -> "AsyncIterator[capo_managedblockchain_query.types.token_balance.TokenBalance]":
        _token = next_token
        while True:
            _response = await self.list_token_balances(
                token_filter,
                config_overrides=config_overrides,
                owner_filter=owner_filter,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("token_balances",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_transaction_events(
        self,
        network: "capo_managedblockchain_query.types.query_network.QueryNetwork",
        *,
        config_overrides: Optional[AsyncManagedBlockchainQueryClientConfig] = None,
        transaction_hash: Optional[
            "capo_managedblockchain_query.types.query_transaction_hash.QueryTransactionHash"
        ] = None,
        transaction_id: Optional[
            "capo_managedblockchain_query.types.query_transaction_id.QueryTransactionId"
        ] = None,
        next_token: Optional[
            "capo_managedblockchain_query.types.next_token.NextToken"
        ] = None,
        max_results: Optional[int] = None,
    ) -> "capo_managedblockchain_query.types.list_transaction_events_output.ListTransactionEventsOutput":
        """<p>Lists all the transaction events for a transaction </p> <note> <p>This action will return transaction details for all transactions that are <i>confirmed</i> on the blockchain, even if they have not reached <a href="https://docs.aws.amazon.com/managed-blockchain/latest/ambq-dg/key-concepts.html#finality">finality</a>. </p> </note>

        Args:
            transaction_hash: <p>The hash of a transaction. It is generated when a transaction is created.</p>
            transaction_id: <p>The identifier of a Bitcoin transaction. It is generated when a transaction is created.</p> <note> <p> <code>transactionId</code> is only supported on the Bitcoin networks.</p> </note>
            network: <p>The blockchain network where the transaction events occurred.</p>
            next_token: <p>The pagination token that indicates the next set of results to retrieve.</p>
            max_results: <p>The maximum number of transaction events to list.</p> <p>Default: <code>100</code> </p> <note> <p>Even if additional results can be retrieved, the request can return less results than <code>maxResults</code> or an empty array of results.</p> <p>To retrieve the next set of results, make another request with the returned <code>nextToken</code> value. The value of <code>nextToken</code> is <code>null</code> when there are no more results to return</p> </note>

        Raises:
            capo_managedblockchain_query.errors.access_denied_exception.AccessDeniedException: <p>The Amazon Web Services account doesn’t have access to this resource. </p>
            capo_managedblockchain_query.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an internal error in the service.</p>
            capo_managedblockchain_query.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The service quota has been exceeded for this resource.</p>
            capo_managedblockchain_query.errors.throttling_exception.ThrottlingException: <p>The request or operation couldn't be performed because a service is throttling requests. The most common source of throttling errors is when you create resources that exceed your service limit for this resource type. Request a limit increase or delete unused resources, if possible.</p>
            capo_managedblockchain_query.errors.validation_exception.ValidationException: <p>The resource passed is invalid.</p>
            capo_managedblockchain_query.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_managedblockchain_query.types.list_transaction_events_input.ListTransactionEventsInput]",
        ) -> AsyncOperationResponse[
            "capo_managedblockchain_query.types.list_transaction_events_output.ListTransactionEventsOutput"
        ]:
            import capo_managedblockchain_query._operations.tieton_chain_query_service.list_transaction_events

            (
                output,
                http_response,
            ) = await capo_managedblockchain_query._operations.tieton_chain_query_service.list_transaction_events.async_list_transaction_events(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_managedblockchain_query.types.list_transaction_events_input.ListTransactionEventsInput = {
            "network": network
        }
        if transaction_hash is not None:
            input_["transaction_hash"] = transaction_hash
        if transaction_id is not None:
            input_["transaction_id"] = transaction_id
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

    async def iter_list_transaction_events(
        self,
        network: "capo_managedblockchain_query.types.query_network.QueryNetwork",
        *,
        config_overrides: Optional[AsyncManagedBlockchainQueryClientConfig] = None,
        transaction_hash: Optional[
            "capo_managedblockchain_query.types.query_transaction_hash.QueryTransactionHash"
        ] = None,
        transaction_id: Optional[
            "capo_managedblockchain_query.types.query_transaction_id.QueryTransactionId"
        ] = None,
        next_token: Optional[
            "capo_managedblockchain_query.types.next_token.NextToken"
        ] = None,
        max_results: Optional[int] = None,
    ) -> "AsyncIterator[capo_managedblockchain_query.types.transaction_event.TransactionEvent]":
        _token = next_token
        while True:
            _response = await self.list_transaction_events(
                network,
                config_overrides=config_overrides,
                transaction_hash=transaction_hash,
                transaction_id=transaction_id,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("events",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_transactions(
        self,
        address: "capo_managedblockchain_query.types.chain_address.ChainAddress",
        network: "capo_managedblockchain_query.types.query_network.QueryNetwork",
        *,
        config_overrides: Optional[AsyncManagedBlockchainQueryClientConfig] = None,
        from_blockchain_instant: Optional[
            "capo_managedblockchain_query.types.blockchain_instant.BlockchainInstant"
        ] = None,
        to_blockchain_instant: Optional[
            "capo_managedblockchain_query.types.blockchain_instant.BlockchainInstant"
        ] = None,
        sort: Optional[
            "capo_managedblockchain_query.types.list_transactions_sort.ListTransactionsSort"
        ] = None,
        next_token: Optional[
            "capo_managedblockchain_query.types.next_token.NextToken"
        ] = None,
        max_results: Optional[int] = None,
        confirmation_status_filter: Optional[
            "capo_managedblockchain_query.types.confirmation_status_filter.ConfirmationStatusFilter"
        ] = None,
    ) -> "capo_managedblockchain_query.types.list_transactions_output.ListTransactionsOutput":
        """<p>Lists all the transaction events for a transaction.</p>

        Args:
            address: <p>The address (either a contract or wallet), whose transactions are being requested.</p>
            network: <p>The blockchain network where the transactions occurred.</p>
            sort: <p>The order by which the results will be sorted. </p>
            next_token: <p>The pagination token that indicates the next set of results to retrieve.</p>
            max_results: <p>The maximum number of transactions to list.</p> <p>Default: <code>100</code> </p> <note> <p>Even if additional results can be retrieved, the request can return less results than <code>maxResults</code> or an empty array of results.</p> <p>To retrieve the next set of results, make another request with the returned <code>nextToken</code> value. The value of <code>nextToken</code> is <code>null</code> when there are no more results to return</p> </note>
            confirmation_status_filter: <p>This filter is used to include transactions in the response that haven't reached <a href="https://docs.aws.amazon.com/managed-blockchain/latest/ambq-dg/key-concepts.html#finality"> <i>finality</i> </a>. Transactions that have reached finality are always part of the response.</p>

        Raises:
            capo_managedblockchain_query.errors.access_denied_exception.AccessDeniedException: <p>The Amazon Web Services account doesn’t have access to this resource. </p>
            capo_managedblockchain_query.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an internal error in the service.</p>
            capo_managedblockchain_query.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The service quota has been exceeded for this resource.</p>
            capo_managedblockchain_query.errors.throttling_exception.ThrottlingException: <p>The request or operation couldn't be performed because a service is throttling requests. The most common source of throttling errors is when you create resources that exceed your service limit for this resource type. Request a limit increase or delete unused resources, if possible.</p>
            capo_managedblockchain_query.errors.validation_exception.ValidationException: <p>The resource passed is invalid.</p>
            capo_managedblockchain_query.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_managedblockchain_query.types.list_transactions_input.ListTransactionsInput]",
        ) -> AsyncOperationResponse[
            "capo_managedblockchain_query.types.list_transactions_output.ListTransactionsOutput"
        ]:
            import capo_managedblockchain_query._operations.tieton_chain_query_service.list_transactions

            (
                output,
                http_response,
            ) = await capo_managedblockchain_query._operations.tieton_chain_query_service.list_transactions.async_list_transactions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_managedblockchain_query.types.list_transactions_input.ListTransactionsInput = {
            "address": address,
            "network": network,
        }
        if from_blockchain_instant is not None:
            input_["from_blockchain_instant"] = from_blockchain_instant
        if to_blockchain_instant is not None:
            input_["to_blockchain_instant"] = to_blockchain_instant
        if sort is not None:
            input_["sort"] = sort
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if confirmation_status_filter is not None:
            input_["confirmation_status_filter"] = confirmation_status_filter

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_transactions(
        self,
        address: "capo_managedblockchain_query.types.chain_address.ChainAddress",
        network: "capo_managedblockchain_query.types.query_network.QueryNetwork",
        *,
        config_overrides: Optional[AsyncManagedBlockchainQueryClientConfig] = None,
        from_blockchain_instant: Optional[
            "capo_managedblockchain_query.types.blockchain_instant.BlockchainInstant"
        ] = None,
        to_blockchain_instant: Optional[
            "capo_managedblockchain_query.types.blockchain_instant.BlockchainInstant"
        ] = None,
        sort: Optional[
            "capo_managedblockchain_query.types.list_transactions_sort.ListTransactionsSort"
        ] = None,
        next_token: Optional[
            "capo_managedblockchain_query.types.next_token.NextToken"
        ] = None,
        max_results: Optional[int] = None,
        confirmation_status_filter: Optional[
            "capo_managedblockchain_query.types.confirmation_status_filter.ConfirmationStatusFilter"
        ] = None,
    ) -> "AsyncIterator[capo_managedblockchain_query.types.transaction_output_item.TransactionOutputItem]":
        _token = next_token
        while True:
            _response = await self.list_transactions(
                address,
                network,
                config_overrides=config_overrides,
                from_blockchain_instant=from_blockchain_instant,
                to_blockchain_instant=to_blockchain_instant,
                sort=sort,
                next_token=_token,
                max_results=max_results,
                confirmation_status_filter=confirmation_status_filter,
            )
            _page = _resolve_path(_response, ("transactions",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(self, exc_type: Any, exc: Any, tb: Any):
        await self._client.aclose()
