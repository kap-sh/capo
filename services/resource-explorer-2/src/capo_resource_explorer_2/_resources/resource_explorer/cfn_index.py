from __future__ import annotations

import uuid
from typing import TYPE_CHECKING, Optional

import capo_resource_explorer_2._auth._signers
import capo_resource_explorer_2._auth._sigv4
from capo_resource_explorer_2._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_resource_explorer_2.types.create_index_input
    import capo_resource_explorer_2.types.create_index_output
    import capo_resource_explorer_2.types.delete_index_input
    import capo_resource_explorer_2.types.delete_index_output
    import capo_resource_explorer_2.types.index
    import capo_resource_explorer_2.types.index_type
    import capo_resource_explorer_2.types.list_indexes_input
    import capo_resource_explorer_2.types.list_indexes_output
    import capo_resource_explorer_2.types.region_list
    import capo_resource_explorer_2.types.tag_map
    import capo_resource_explorer_2.types.update_index_type_input
    import capo_resource_explorer_2.types.update_index_type_output
    from capo_resource_explorer_2._services.async_resource_explorer2 import (
        AsyncResourceExplorer2Client,
        AsyncResourceExplorer2ClientConfig,
    )
    from capo_resource_explorer_2._services.resource_explorer2 import (
        ResourceExplorer2Client,
        ResourceExplorer2ClientConfig,
    )


class CfnIndex:
    def __init__(self, service: ResourceExplorer2Client) -> None:
        self._service = service

    def create(
        self,
        *,
        config_overrides: Optional[ResourceExplorer2ClientConfig] = None,
        client_token: Optional[str] = None,
        tags: Optional["capo_resource_explorer_2.types.tag_map.TagMap"] = None,
    ) -> "capo_resource_explorer_2.types.create_index_output.CreateIndexOutput":
        """<p>Turns on Amazon Web Services Resource Explorer in the Amazon Web Services Region in which you called this operation by creating an index. Resource Explorer begins discovering the resources in this Region and stores the details about the resources in the index so that they can be queried by using the <a>Search</a> operation. You can create only one index in a Region.</p> <note> <p>This operation creates only a <i>local</i> index. To promote the local index in one Amazon Web Services Region into the aggregator index for the Amazon Web Services account, use the <a>UpdateIndexType</a> operation. For more information, see <a href="https://docs.aws.amazon.com/resource-explorer/latest/userguide/manage-aggregator-region.html">Turning on cross-Region search by creating an aggregator index</a> in the <i>Amazon Web Services Resource Explorer User Guide</i>.</p> </note> <p>For more details about what happens when you turn on Resource Explorer in an Amazon Web Services Region, see <a href="https://docs.aws.amazon.com/resource-explorer/latest/userguide/manage-service-activate.html">Turn on Resource Explorer to index your resources in an Amazon Web Services Region</a> in the <i>Amazon Web Services Resource Explorer User Guide</i>.</p> <p>If this is the first Amazon Web Services Region in which you've created an index for Resource Explorer, then this operation also <a href="https://docs.aws.amazon.com/resource-explorer/latest/userguide/security_iam_service-linked-roles.html">creates a service-linked role</a> in your Amazon Web Services account that allows Resource Explorer to enumerate your resources to populate the index.</p> <ul> <li> <p> <b>Action</b>: <code>resource-explorer-2:CreateIndex</code> </p> <p> <b>Resource</b>: The ARN of the index (as it will exist after the operation completes) in the Amazon Web Services Region and account in which you're trying to create the index. Use the wildcard character (<code>*</code>) at the end of the string to match the eventual UUID. For example, the following <code>Resource</code> element restricts the role or user to creating an index in only the <code>us-east-2</code> Region of the specified account.</p> <p> <code>"Resource": "arn:aws:resource-explorer-2:us-west-2:<i>&lt;account-id&gt;</i>:index/*"</code> </p> <p>Alternatively, you can use <code>"Resource": "*"</code> to allow the role or user to create an index in any Region.</p> </li> <li> <p> <b>Action</b>: <code>iam:CreateServiceLinkedRole</code> </p> <p> <b>Resource</b>: No specific resource (*). </p> <p>This permission is required only the first time you create an index to turn on Resource Explorer in the account. Resource Explorer uses this to create the <a href="https://docs.aws.amazon.com/resource-explorer/latest/userguide/security_iam_service-linked-roles.html">service-linked role needed to index the resources in your account</a>. Resource Explorer uses the same service-linked role for all additional indexes you create afterwards.</p> </li> </ul>

        Args:
            client_token: <p>This value helps ensure idempotency. Resource Explorer uses this value to prevent the accidental creation of duplicate versions. We recommend that you generate a <a href="https://wikipedia.org/wiki/Universally_unique_identifier">UUID-type value</a> to ensure the uniqueness of your index.</p>
            tags: <p>The specified tags are attached only to the index created in this Amazon Web Services Region. The tags aren't attached to any of the resources listed in the index.</p>

        Raises:
            capo_resource_explorer_2.errors.access_denied_exception.AccessDeniedException: <p>The credentials that you used to call this operation don't have the minimum required permissions.</p>
            capo_resource_explorer_2.errors.conflict_exception.ConflictException: <p>If you attempted to create a view, then the request failed because either you specified parameters that didn’t match the original request, or you attempted to create a view with a name that already exists in this Amazon Web Services Region.</p> <p>If you attempted to create an index, then the request failed because either you specified parameters that didn't match the original request, or an index already exists in the current Amazon Web Services Region.</p> <p>If you attempted to update an index type to <code>AGGREGATOR</code>, then the request failed because you already have an <code>AGGREGATOR</code> index in a different Amazon Web Services Region.</p>
            capo_resource_explorer_2.errors.internal_server_exception.InternalServerException: <p>The request failed because of internal service error. Try your request again later.</p>
            capo_resource_explorer_2.errors.throttling_exception.ThrottlingException: <p>The request failed because you exceeded a rate limit for this operation. For more information, see <a href="https://docs.aws.amazon.com/resource-explorer/latest/userguide/quotas.html">Quotas for Resource Explorer</a>.</p>
            capo_resource_explorer_2.errors.validation_exception.ValidationException: <p>You provided an invalid value for one of the operation's parameters. Check the syntax for the operation, and try again.</p>
            capo_resource_explorer_2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_resource_explorer_2.types.create_index_input.CreateIndexInput]",
        ) -> OperationResponse[
            "capo_resource_explorer_2.types.create_index_output.CreateIndexOutput"
        ]:
            import capo_resource_explorer_2._operations.resource_explorer.create_index

            output, http_response = (
                capo_resource_explorer_2._operations.resource_explorer.create_index.create_index(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_resource_explorer_2.types.create_index_input.CreateIndexInput = {}
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update(
        self,
        arn: str,
        type: "capo_resource_explorer_2.types.index_type.IndexType",
        *,
        config_overrides: Optional[ResourceExplorer2ClientConfig] = None,
    ) -> (
        "capo_resource_explorer_2.types.update_index_type_output.UpdateIndexTypeOutput"
    ):
        """<p>Changes the type of the index from one of the following types to the other. For more information about indexes and the role they perform in Amazon Web Services Resource Explorer, see <a href="https://docs.aws.amazon.com/resource-explorer/latest/userguide/manage-aggregator-region.html">Turning on cross-Region search by creating an aggregator index</a> in the <i>Amazon Web Services Resource Explorer User Guide</i>.</p> <ul> <li> <p> <b> <code>AGGREGATOR</code> index type</b> </p> <p>The index contains information about resources from all Amazon Web Services Regions in the Amazon Web Services account in which you've created a Resource Explorer index. Resource information from all other Regions is replicated to this Region's index.</p> <p>When you change the index type to <code>AGGREGATOR</code>, Resource Explorer turns on replication of all discovered resource information from the other Amazon Web Services Regions in your account to this index. You can then, from this Region only, perform resource search queries that span all Amazon Web Services Regions in the Amazon Web Services account. Turning on replication from all other Regions is performed by asynchronous background tasks. You can check the status of the asynchronous tasks by using the <a>GetIndex</a> operation. When the asynchronous tasks complete, the <code>Status</code> response of that operation changes from <code>UPDATING</code> to <code>ACTIVE</code>. After that, you can start to see results from other Amazon Web Services Regions in query results. However, it can take several hours for replication from all other Regions to complete.</p> <important> <p>You can have only one aggregator index per Amazon Web Services account. Before you can promote a different index to be the aggregator index for the account, you must first demote the existing aggregator index to type <code>LOCAL</code>.</p> </important> </li> <li> <p> <b> <code>LOCAL</code> index type</b> </p> <p>The index contains information about resources in only the Amazon Web Services Region in which the index exists. If an aggregator index in another Region exists, then information in this local index is replicated to the aggregator index.</p> <p>When you change the index type to <code>LOCAL</code>, Resource Explorer turns off the replication of resource information from all other Amazon Web Services Regions in the Amazon Web Services account to this Region. The aggregator index remains in the <code>UPDATING</code> state until all replication with other Regions successfully stops. You can check the status of the asynchronous task by using the <a>GetIndex</a> operation. When Resource Explorer successfully stops all replication with other Regions, the <code>Status</code> response of that operation changes from <code>UPDATING</code> to <code>ACTIVE</code>. Separately, the resource information from other Regions that was previously stored in the index is deleted within 30 days by another background task. Until that asynchronous task completes, some results from other Regions can continue to appear in search results.</p> <important> <p>After you demote an aggregator index to a local index, you must wait 24 hours before you can promote another index to be the new aggregator index for the account.</p> </important> </li> </ul>

        Args:
            arn: <p>The <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon resource name (ARN)</a> of the index that you want to update.</p>
            type: <p>The type of the index. To understand the difference between <code>LOCAL</code> and <code>AGGREGATOR</code>, see <a href="https://docs.aws.amazon.com/resource-explorer/latest/userguide/manage-aggregator-region.html">Turning on cross-Region search</a> in the <i>Amazon Web Services Resource Explorer User Guide</i>.</p>

        Raises:
            capo_resource_explorer_2.errors.access_denied_exception.AccessDeniedException: <p>The credentials that you used to call this operation don't have the minimum required permissions.</p>
            capo_resource_explorer_2.errors.conflict_exception.ConflictException: <p>If you attempted to create a view, then the request failed because either you specified parameters that didn’t match the original request, or you attempted to create a view with a name that already exists in this Amazon Web Services Region.</p> <p>If you attempted to create an index, then the request failed because either you specified parameters that didn't match the original request, or an index already exists in the current Amazon Web Services Region.</p> <p>If you attempted to update an index type to <code>AGGREGATOR</code>, then the request failed because you already have an <code>AGGREGATOR</code> index in a different Amazon Web Services Region.</p>
            capo_resource_explorer_2.errors.internal_server_exception.InternalServerException: <p>The request failed because of internal service error. Try your request again later.</p>
            capo_resource_explorer_2.errors.resource_not_found_exception.ResourceNotFoundException: <p>You specified a resource that doesn't exist. Check the ID or ARN that you used to identity the resource, and try again.</p>
            capo_resource_explorer_2.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request failed because it exceeds a service quota.</p>
            capo_resource_explorer_2.errors.throttling_exception.ThrottlingException: <p>The request failed because you exceeded a rate limit for this operation. For more information, see <a href="https://docs.aws.amazon.com/resource-explorer/latest/userguide/quotas.html">Quotas for Resource Explorer</a>.</p>
            capo_resource_explorer_2.errors.validation_exception.ValidationException: <p>You provided an invalid value for one of the operation's parameters. Check the syntax for the operation, and try again.</p>
            capo_resource_explorer_2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_resource_explorer_2.types.update_index_type_input.UpdateIndexTypeInput]",
        ) -> OperationResponse[
            "capo_resource_explorer_2.types.update_index_type_output.UpdateIndexTypeOutput"
        ]:
            import capo_resource_explorer_2._operations.resource_explorer.update_index_type

            output, http_response = (
                capo_resource_explorer_2._operations.resource_explorer.update_index_type.update_index_type(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_resource_explorer_2.types.update_index_type_input.UpdateIndexTypeInput = {
            "arn": arn,
            "type": type,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete(
        self,
        arn: str,
        *,
        config_overrides: Optional[ResourceExplorer2ClientConfig] = None,
    ) -> "capo_resource_explorer_2.types.delete_index_output.DeleteIndexOutput":
        """<p>Deletes the specified index and turns off Amazon Web Services Resource Explorer in the specified Amazon Web Services Region. When you delete an index, Resource Explorer stops discovering and indexing resources in that Region. Resource Explorer also deletes all views in that Region. These actions occur as asynchronous background tasks. You can check to see when the actions are complete by using the <a>GetIndex</a> operation and checking the <code>Status</code> response value.</p> <note> <p>If the index you delete is the aggregator index for the Amazon Web Services account, you must wait 24 hours before you can promote another local index to be the aggregator index for the account. Users can't perform account-wide searches using Resource Explorer until another aggregator index is configured.</p> </note>

        Args:
            arn: <p>The <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon resource name (ARN)</a> of the index that you want to delete.</p>

        Raises:
            capo_resource_explorer_2.errors.access_denied_exception.AccessDeniedException: <p>The credentials that you used to call this operation don't have the minimum required permissions.</p>
            capo_resource_explorer_2.errors.internal_server_exception.InternalServerException: <p>The request failed because of internal service error. Try your request again later.</p>
            capo_resource_explorer_2.errors.resource_not_found_exception.ResourceNotFoundException: <p>You specified a resource that doesn't exist. Check the ID or ARN that you used to identity the resource, and try again.</p>
            capo_resource_explorer_2.errors.throttling_exception.ThrottlingException: <p>The request failed because you exceeded a rate limit for this operation. For more information, see <a href="https://docs.aws.amazon.com/resource-explorer/latest/userguide/quotas.html">Quotas for Resource Explorer</a>.</p>
            capo_resource_explorer_2.errors.validation_exception.ValidationException: <p>You provided an invalid value for one of the operation's parameters. Check the syntax for the operation, and try again.</p>
            capo_resource_explorer_2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_resource_explorer_2.types.delete_index_input.DeleteIndexInput]",
        ) -> OperationResponse[
            "capo_resource_explorer_2.types.delete_index_output.DeleteIndexOutput"
        ]:
            import capo_resource_explorer_2._operations.resource_explorer.delete_index

            output, http_response = (
                capo_resource_explorer_2._operations.resource_explorer.delete_index.delete_index(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_resource_explorer_2.types.delete_index_input.DeleteIndexInput = {
            "arn": arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list(
        self,
        *,
        config_overrides: Optional[ResourceExplorer2ClientConfig] = None,
        type: Optional["capo_resource_explorer_2.types.index_type.IndexType"] = None,
        regions: Optional[
            "capo_resource_explorer_2.types.region_list.RegionList"
        ] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
    ) -> "capo_resource_explorer_2.types.list_indexes_output.ListIndexesOutput":
        """<p>Retrieves a list of all of the indexes in Amazon Web Services Regions that are currently collecting resource information for Amazon Web Services Resource Explorer.</p>

        Args:
            type: <p>If specified, limits the output to only indexes of the specified Type, either <code>LOCAL</code> or <code>AGGREGATOR</code>.</p> <p>Use this option to discover the aggregator index for your account.</p>
            regions: <p>If specified, limits the response to only information about the index in the specified list of Amazon Web Services Regions.</p>
            max_results: <p>The maximum number of results that you want included on each page of the response. If you do not include this parameter, it defaults to a value appropriate to the operation. If additional items exist beyond those included in the current response, the <code>NextToken</code> response element is present and has a value (is not null). Include that value as the <code>NextToken</code> request parameter in the next call to the operation to get the next part of the results.</p> <note> <p>An API operation can return fewer results than the maximum even when there are more results available. You should check <code>NextToken</code> after every operation to ensure that you receive all of the results.</p> </note>
            next_token: <p>The parameter for receiving additional results if you receive a <code>NextToken</code> response in a previous request. A <code>NextToken</code> response indicates that more output is available. Set this parameter to the value of the previous call's <code>NextToken</code> response to indicate where the output should continue from. The pagination tokens expire after 24 hours.</p>

        Raises:
            capo_resource_explorer_2.errors.access_denied_exception.AccessDeniedException: <p>The credentials that you used to call this operation don't have the minimum required permissions.</p>
            capo_resource_explorer_2.errors.internal_server_exception.InternalServerException: <p>The request failed because of internal service error. Try your request again later.</p>
            capo_resource_explorer_2.errors.throttling_exception.ThrottlingException: <p>The request failed because you exceeded a rate limit for this operation. For more information, see <a href="https://docs.aws.amazon.com/resource-explorer/latest/userguide/quotas.html">Quotas for Resource Explorer</a>.</p>
            capo_resource_explorer_2.errors.validation_exception.ValidationException: <p>You provided an invalid value for one of the operation's parameters. Check the syntax for the operation, and try again.</p>
            capo_resource_explorer_2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_resource_explorer_2.types.list_indexes_input.ListIndexesInput]",
        ) -> OperationResponse[
            "capo_resource_explorer_2.types.list_indexes_output.ListIndexesOutput"
        ]:
            import capo_resource_explorer_2._operations.resource_explorer.list_indexes

            output, http_response = (
                capo_resource_explorer_2._operations.resource_explorer.list_indexes.list_indexes(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_resource_explorer_2.types.list_indexes_input.ListIndexesInput = {}
        if type is not None:
            input_["type"] = type
        if regions is not None:
            input_["regions"] = regions
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


class AsyncCfnIndex:
    def __init__(self, service: AsyncResourceExplorer2Client) -> None:
        self._service = service

    async def create(
        self,
        *,
        config_overrides: Optional[AsyncResourceExplorer2ClientConfig] = None,
        client_token: Optional[str] = None,
        tags: Optional["capo_resource_explorer_2.types.tag_map.TagMap"] = None,
    ) -> "capo_resource_explorer_2.types.create_index_output.CreateIndexOutput":
        """<p>Turns on Amazon Web Services Resource Explorer in the Amazon Web Services Region in which you called this operation by creating an index. Resource Explorer begins discovering the resources in this Region and stores the details about the resources in the index so that they can be queried by using the <a>Search</a> operation. You can create only one index in a Region.</p> <note> <p>This operation creates only a <i>local</i> index. To promote the local index in one Amazon Web Services Region into the aggregator index for the Amazon Web Services account, use the <a>UpdateIndexType</a> operation. For more information, see <a href="https://docs.aws.amazon.com/resource-explorer/latest/userguide/manage-aggregator-region.html">Turning on cross-Region search by creating an aggregator index</a> in the <i>Amazon Web Services Resource Explorer User Guide</i>.</p> </note> <p>For more details about what happens when you turn on Resource Explorer in an Amazon Web Services Region, see <a href="https://docs.aws.amazon.com/resource-explorer/latest/userguide/manage-service-activate.html">Turn on Resource Explorer to index your resources in an Amazon Web Services Region</a> in the <i>Amazon Web Services Resource Explorer User Guide</i>.</p> <p>If this is the first Amazon Web Services Region in which you've created an index for Resource Explorer, then this operation also <a href="https://docs.aws.amazon.com/resource-explorer/latest/userguide/security_iam_service-linked-roles.html">creates a service-linked role</a> in your Amazon Web Services account that allows Resource Explorer to enumerate your resources to populate the index.</p> <ul> <li> <p> <b>Action</b>: <code>resource-explorer-2:CreateIndex</code> </p> <p> <b>Resource</b>: The ARN of the index (as it will exist after the operation completes) in the Amazon Web Services Region and account in which you're trying to create the index. Use the wildcard character (<code>*</code>) at the end of the string to match the eventual UUID. For example, the following <code>Resource</code> element restricts the role or user to creating an index in only the <code>us-east-2</code> Region of the specified account.</p> <p> <code>"Resource": "arn:aws:resource-explorer-2:us-west-2:<i>&lt;account-id&gt;</i>:index/*"</code> </p> <p>Alternatively, you can use <code>"Resource": "*"</code> to allow the role or user to create an index in any Region.</p> </li> <li> <p> <b>Action</b>: <code>iam:CreateServiceLinkedRole</code> </p> <p> <b>Resource</b>: No specific resource (*). </p> <p>This permission is required only the first time you create an index to turn on Resource Explorer in the account. Resource Explorer uses this to create the <a href="https://docs.aws.amazon.com/resource-explorer/latest/userguide/security_iam_service-linked-roles.html">service-linked role needed to index the resources in your account</a>. Resource Explorer uses the same service-linked role for all additional indexes you create afterwards.</p> </li> </ul>

        Args:
            client_token: <p>This value helps ensure idempotency. Resource Explorer uses this value to prevent the accidental creation of duplicate versions. We recommend that you generate a <a href="https://wikipedia.org/wiki/Universally_unique_identifier">UUID-type value</a> to ensure the uniqueness of your index.</p>
            tags: <p>The specified tags are attached only to the index created in this Amazon Web Services Region. The tags aren't attached to any of the resources listed in the index.</p>

        Raises:
            capo_resource_explorer_2.errors.access_denied_exception.AccessDeniedException: <p>The credentials that you used to call this operation don't have the minimum required permissions.</p>
            capo_resource_explorer_2.errors.conflict_exception.ConflictException: <p>If you attempted to create a view, then the request failed because either you specified parameters that didn’t match the original request, or you attempted to create a view with a name that already exists in this Amazon Web Services Region.</p> <p>If you attempted to create an index, then the request failed because either you specified parameters that didn't match the original request, or an index already exists in the current Amazon Web Services Region.</p> <p>If you attempted to update an index type to <code>AGGREGATOR</code>, then the request failed because you already have an <code>AGGREGATOR</code> index in a different Amazon Web Services Region.</p>
            capo_resource_explorer_2.errors.internal_server_exception.InternalServerException: <p>The request failed because of internal service error. Try your request again later.</p>
            capo_resource_explorer_2.errors.throttling_exception.ThrottlingException: <p>The request failed because you exceeded a rate limit for this operation. For more information, see <a href="https://docs.aws.amazon.com/resource-explorer/latest/userguide/quotas.html">Quotas for Resource Explorer</a>.</p>
            capo_resource_explorer_2.errors.validation_exception.ValidationException: <p>You provided an invalid value for one of the operation's parameters. Check the syntax for the operation, and try again.</p>
            capo_resource_explorer_2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_resource_explorer_2.types.create_index_input.CreateIndexInput]",
        ) -> AsyncOperationResponse[
            "capo_resource_explorer_2.types.create_index_output.CreateIndexOutput"
        ]:
            import capo_resource_explorer_2._operations.resource_explorer.create_index

            (
                output,
                http_response,
            ) = await capo_resource_explorer_2._operations.resource_explorer.create_index.async_create_index(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_resource_explorer_2.types.create_index_input.CreateIndexInput = {}
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update(
        self,
        arn: str,
        type: "capo_resource_explorer_2.types.index_type.IndexType",
        *,
        config_overrides: Optional[AsyncResourceExplorer2ClientConfig] = None,
    ) -> (
        "capo_resource_explorer_2.types.update_index_type_output.UpdateIndexTypeOutput"
    ):
        """<p>Changes the type of the index from one of the following types to the other. For more information about indexes and the role they perform in Amazon Web Services Resource Explorer, see <a href="https://docs.aws.amazon.com/resource-explorer/latest/userguide/manage-aggregator-region.html">Turning on cross-Region search by creating an aggregator index</a> in the <i>Amazon Web Services Resource Explorer User Guide</i>.</p> <ul> <li> <p> <b> <code>AGGREGATOR</code> index type</b> </p> <p>The index contains information about resources from all Amazon Web Services Regions in the Amazon Web Services account in which you've created a Resource Explorer index. Resource information from all other Regions is replicated to this Region's index.</p> <p>When you change the index type to <code>AGGREGATOR</code>, Resource Explorer turns on replication of all discovered resource information from the other Amazon Web Services Regions in your account to this index. You can then, from this Region only, perform resource search queries that span all Amazon Web Services Regions in the Amazon Web Services account. Turning on replication from all other Regions is performed by asynchronous background tasks. You can check the status of the asynchronous tasks by using the <a>GetIndex</a> operation. When the asynchronous tasks complete, the <code>Status</code> response of that operation changes from <code>UPDATING</code> to <code>ACTIVE</code>. After that, you can start to see results from other Amazon Web Services Regions in query results. However, it can take several hours for replication from all other Regions to complete.</p> <important> <p>You can have only one aggregator index per Amazon Web Services account. Before you can promote a different index to be the aggregator index for the account, you must first demote the existing aggregator index to type <code>LOCAL</code>.</p> </important> </li> <li> <p> <b> <code>LOCAL</code> index type</b> </p> <p>The index contains information about resources in only the Amazon Web Services Region in which the index exists. If an aggregator index in another Region exists, then information in this local index is replicated to the aggregator index.</p> <p>When you change the index type to <code>LOCAL</code>, Resource Explorer turns off the replication of resource information from all other Amazon Web Services Regions in the Amazon Web Services account to this Region. The aggregator index remains in the <code>UPDATING</code> state until all replication with other Regions successfully stops. You can check the status of the asynchronous task by using the <a>GetIndex</a> operation. When Resource Explorer successfully stops all replication with other Regions, the <code>Status</code> response of that operation changes from <code>UPDATING</code> to <code>ACTIVE</code>. Separately, the resource information from other Regions that was previously stored in the index is deleted within 30 days by another background task. Until that asynchronous task completes, some results from other Regions can continue to appear in search results.</p> <important> <p>After you demote an aggregator index to a local index, you must wait 24 hours before you can promote another index to be the new aggregator index for the account.</p> </important> </li> </ul>

        Args:
            arn: <p>The <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon resource name (ARN)</a> of the index that you want to update.</p>
            type: <p>The type of the index. To understand the difference between <code>LOCAL</code> and <code>AGGREGATOR</code>, see <a href="https://docs.aws.amazon.com/resource-explorer/latest/userguide/manage-aggregator-region.html">Turning on cross-Region search</a> in the <i>Amazon Web Services Resource Explorer User Guide</i>.</p>

        Raises:
            capo_resource_explorer_2.errors.access_denied_exception.AccessDeniedException: <p>The credentials that you used to call this operation don't have the minimum required permissions.</p>
            capo_resource_explorer_2.errors.conflict_exception.ConflictException: <p>If you attempted to create a view, then the request failed because either you specified parameters that didn’t match the original request, or you attempted to create a view with a name that already exists in this Amazon Web Services Region.</p> <p>If you attempted to create an index, then the request failed because either you specified parameters that didn't match the original request, or an index already exists in the current Amazon Web Services Region.</p> <p>If you attempted to update an index type to <code>AGGREGATOR</code>, then the request failed because you already have an <code>AGGREGATOR</code> index in a different Amazon Web Services Region.</p>
            capo_resource_explorer_2.errors.internal_server_exception.InternalServerException: <p>The request failed because of internal service error. Try your request again later.</p>
            capo_resource_explorer_2.errors.resource_not_found_exception.ResourceNotFoundException: <p>You specified a resource that doesn't exist. Check the ID or ARN that you used to identity the resource, and try again.</p>
            capo_resource_explorer_2.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request failed because it exceeds a service quota.</p>
            capo_resource_explorer_2.errors.throttling_exception.ThrottlingException: <p>The request failed because you exceeded a rate limit for this operation. For more information, see <a href="https://docs.aws.amazon.com/resource-explorer/latest/userguide/quotas.html">Quotas for Resource Explorer</a>.</p>
            capo_resource_explorer_2.errors.validation_exception.ValidationException: <p>You provided an invalid value for one of the operation's parameters. Check the syntax for the operation, and try again.</p>
            capo_resource_explorer_2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_resource_explorer_2.types.update_index_type_input.UpdateIndexTypeInput]",
        ) -> AsyncOperationResponse[
            "capo_resource_explorer_2.types.update_index_type_output.UpdateIndexTypeOutput"
        ]:
            import capo_resource_explorer_2._operations.resource_explorer.update_index_type

            (
                output,
                http_response,
            ) = await capo_resource_explorer_2._operations.resource_explorer.update_index_type.async_update_index_type(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_resource_explorer_2.types.update_index_type_input.UpdateIndexTypeInput = {
            "arn": arn,
            "type": type,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete(
        self,
        arn: str,
        *,
        config_overrides: Optional[AsyncResourceExplorer2ClientConfig] = None,
    ) -> "capo_resource_explorer_2.types.delete_index_output.DeleteIndexOutput":
        """<p>Deletes the specified index and turns off Amazon Web Services Resource Explorer in the specified Amazon Web Services Region. When you delete an index, Resource Explorer stops discovering and indexing resources in that Region. Resource Explorer also deletes all views in that Region. These actions occur as asynchronous background tasks. You can check to see when the actions are complete by using the <a>GetIndex</a> operation and checking the <code>Status</code> response value.</p> <note> <p>If the index you delete is the aggregator index for the Amazon Web Services account, you must wait 24 hours before you can promote another local index to be the aggregator index for the account. Users can't perform account-wide searches using Resource Explorer until another aggregator index is configured.</p> </note>

        Args:
            arn: <p>The <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon resource name (ARN)</a> of the index that you want to delete.</p>

        Raises:
            capo_resource_explorer_2.errors.access_denied_exception.AccessDeniedException: <p>The credentials that you used to call this operation don't have the minimum required permissions.</p>
            capo_resource_explorer_2.errors.internal_server_exception.InternalServerException: <p>The request failed because of internal service error. Try your request again later.</p>
            capo_resource_explorer_2.errors.resource_not_found_exception.ResourceNotFoundException: <p>You specified a resource that doesn't exist. Check the ID or ARN that you used to identity the resource, and try again.</p>
            capo_resource_explorer_2.errors.throttling_exception.ThrottlingException: <p>The request failed because you exceeded a rate limit for this operation. For more information, see <a href="https://docs.aws.amazon.com/resource-explorer/latest/userguide/quotas.html">Quotas for Resource Explorer</a>.</p>
            capo_resource_explorer_2.errors.validation_exception.ValidationException: <p>You provided an invalid value for one of the operation's parameters. Check the syntax for the operation, and try again.</p>
            capo_resource_explorer_2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_resource_explorer_2.types.delete_index_input.DeleteIndexInput]",
        ) -> AsyncOperationResponse[
            "capo_resource_explorer_2.types.delete_index_output.DeleteIndexOutput"
        ]:
            import capo_resource_explorer_2._operations.resource_explorer.delete_index

            (
                output,
                http_response,
            ) = await capo_resource_explorer_2._operations.resource_explorer.delete_index.async_delete_index(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_resource_explorer_2.types.delete_index_input.DeleteIndexInput = {
            "arn": arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list(
        self,
        *,
        config_overrides: Optional[AsyncResourceExplorer2ClientConfig] = None,
        type: Optional["capo_resource_explorer_2.types.index_type.IndexType"] = None,
        regions: Optional[
            "capo_resource_explorer_2.types.region_list.RegionList"
        ] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
    ) -> "capo_resource_explorer_2.types.list_indexes_output.ListIndexesOutput":
        """<p>Retrieves a list of all of the indexes in Amazon Web Services Regions that are currently collecting resource information for Amazon Web Services Resource Explorer.</p>

        Args:
            type: <p>If specified, limits the output to only indexes of the specified Type, either <code>LOCAL</code> or <code>AGGREGATOR</code>.</p> <p>Use this option to discover the aggregator index for your account.</p>
            regions: <p>If specified, limits the response to only information about the index in the specified list of Amazon Web Services Regions.</p>
            max_results: <p>The maximum number of results that you want included on each page of the response. If you do not include this parameter, it defaults to a value appropriate to the operation. If additional items exist beyond those included in the current response, the <code>NextToken</code> response element is present and has a value (is not null). Include that value as the <code>NextToken</code> request parameter in the next call to the operation to get the next part of the results.</p> <note> <p>An API operation can return fewer results than the maximum even when there are more results available. You should check <code>NextToken</code> after every operation to ensure that you receive all of the results.</p> </note>
            next_token: <p>The parameter for receiving additional results if you receive a <code>NextToken</code> response in a previous request. A <code>NextToken</code> response indicates that more output is available. Set this parameter to the value of the previous call's <code>NextToken</code> response to indicate where the output should continue from. The pagination tokens expire after 24 hours.</p>

        Raises:
            capo_resource_explorer_2.errors.access_denied_exception.AccessDeniedException: <p>The credentials that you used to call this operation don't have the minimum required permissions.</p>
            capo_resource_explorer_2.errors.internal_server_exception.InternalServerException: <p>The request failed because of internal service error. Try your request again later.</p>
            capo_resource_explorer_2.errors.throttling_exception.ThrottlingException: <p>The request failed because you exceeded a rate limit for this operation. For more information, see <a href="https://docs.aws.amazon.com/resource-explorer/latest/userguide/quotas.html">Quotas for Resource Explorer</a>.</p>
            capo_resource_explorer_2.errors.validation_exception.ValidationException: <p>You provided an invalid value for one of the operation's parameters. Check the syntax for the operation, and try again.</p>
            capo_resource_explorer_2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_resource_explorer_2.types.list_indexes_input.ListIndexesInput]",
        ) -> AsyncOperationResponse[
            "capo_resource_explorer_2.types.list_indexes_output.ListIndexesOutput"
        ]:
            import capo_resource_explorer_2._operations.resource_explorer.list_indexes

            (
                output,
                http_response,
            ) = await capo_resource_explorer_2._operations.resource_explorer.list_indexes.async_list_indexes(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_resource_explorer_2.types.list_indexes_input.ListIndexesInput = {}
        if type is not None:
            input_["type"] = type
        if regions is not None:
            input_["regions"] = regions
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
