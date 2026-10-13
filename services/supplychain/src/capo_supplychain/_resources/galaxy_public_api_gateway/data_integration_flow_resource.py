from __future__ import annotations

from typing import TYPE_CHECKING, Any, Optional

import capo_supplychain._auth._signers
import capo_supplychain._auth._sigv4
from capo_supplychain._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationLogging,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_supplychain.types.create_data_integration_flow_request
    import capo_supplychain.types.create_data_integration_flow_response
    import capo_supplychain.types.data_integration_flow
    import capo_supplychain.types.data_integration_flow_max_results
    import capo_supplychain.types.data_integration_flow_name
    import capo_supplychain.types.data_integration_flow_next_token
    import capo_supplychain.types.data_integration_flow_source_list
    import capo_supplychain.types.data_integration_flow_target
    import capo_supplychain.types.data_integration_flow_transformation
    import capo_supplychain.types.delete_data_integration_flow_request
    import capo_supplychain.types.delete_data_integration_flow_response
    import capo_supplychain.types.get_data_integration_flow_request
    import capo_supplychain.types.get_data_integration_flow_response
    import capo_supplychain.types.list_data_integration_flows_request
    import capo_supplychain.types.list_data_integration_flows_response
    import capo_supplychain.types.tag_map
    import capo_supplychain.types.update_data_integration_flow_request
    import capo_supplychain.types.update_data_integration_flow_response
    import capo_supplychain.types.uuid
    from capo_supplychain._services.async_supply_chain import (
        AsyncSupplyChainClient,
        AsyncSupplyChainClientConfig,
    )
    from capo_supplychain._services.supply_chain import (
        SupplyChainClient,
        SupplyChainClientConfig,
    )


class DataIntegrationFlowResource:
    def __init__(self, service: SupplyChainClient) -> None:
        self._service = service

    def put(
        self,
        instance_id: "capo_supplychain.types.uuid.UUID",
        name: "capo_supplychain.types.data_integration_flow_name.DataIntegrationFlowName",
        sources: "capo_supplychain.types.data_integration_flow_source_list.DataIntegrationFlowSourceList",
        transformation: "capo_supplychain.types.data_integration_flow_transformation.DataIntegrationFlowTransformation",
        target: "capo_supplychain.types.data_integration_flow_target.DataIntegrationFlowTarget",
        *,
        config_overrides: Optional[SupplyChainClientConfig] = None,
        tags: Optional["capo_supplychain.types.tag_map.TagMap"] = None,
    ) -> "capo_supplychain.types.create_data_integration_flow_response.CreateDataIntegrationFlowResponse":
        """<p>Enables you to programmatically create a data pipeline to ingest data from source systems such as Amazon S3 buckets, to a predefined Amazon Web Services Supply Chain dataset (product, inbound_order) or a temporary dataset along with the data transformation query provided with the API.</p>

        Args:
            instance_id: <p>The Amazon Web Services Supply Chain instance identifier.</p>
            name: <p>Name of the DataIntegrationFlow.</p>
            sources: <p>The source configurations for DataIntegrationFlow.</p>
            transformation: <p>The transformation configurations for DataIntegrationFlow.</p>
            target: <p>The target configurations for DataIntegrationFlow.</p>
            tags: <p>The tags of the DataIntegrationFlow to be created</p>

        Raises:
            capo_supplychain.errors.access_denied_exception.AccessDeniedException: <p>You do not have the required privileges to perform this action.</p>
            capo_supplychain.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            capo_supplychain.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_supplychain.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_supplychain.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Request would cause a service quota to be exceeded.</p>
            capo_supplychain.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_supplychain.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an AWS service.</p>
            capo_supplychain.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Successful CreateDataIntegrationFlow for s3 to dataset flow

            >>> client.put(instance_id='8850c54e-e187-4fa7-89d4-6370f165174d', name='testStagingFlow', sources=[{'sourceType': 'S3', 'sourceName': 'testSourceName', 's3Source': {'bucketName': 'aws-supply-chain-data-b8c7bb28-a576-4334-b481-6d6e8e47371f', 'prefix': 'example-prefix'}}], transformation={'transformationType': 'SQL', 'sqlTransformation': {'query': 'SELECT * FROM testSourceName'}}, target={'targetType': 'DATASET', 'datasetTarget': {'datasetIdentifier': 'arn:aws:scn:us-east-1:123456789012:instance/8850c54e-e187-4fa7-89d4-6370f165174d/namespaces/default/datasets/my_staging_dataset'}}, tags={'tagKey1': 'tagValue1'})
            Successful CreateDataIntegrationFlow for dataset to dataset flow

            >>> client.put(instance_id='8850c54e-e187-4fa7-89d4-6370f165174d', name='trading-partner', sources=[{'sourceType': 'DATASET', 'sourceName': 'testSourceName1', 'datasetSource': {'datasetIdentifier': 'arn:aws:scn:us-east-1:123456789012:instance/8850c54e-e187-4fa7-89d4-6370f165174d/namespaces/default/datasets/my_staging_dataset1'}}, {'sourceType': 'DATASET', 'sourceName': 'testSourceName2', 'datasetSource': {'datasetIdentifier': 'arn:aws:scn:us-east-1:123456789012:instance/8850c54e-e187-4fa7-89d4-6370f165174d/namespaces/default/datasets/my_staging_dataset2'}}], transformation={'transformationType': 'SQL', 'sqlTransformation': {'query': 'SELECT S1.id AS id, S1.poc_org_unit_description AS description, S1.company_id AS company_id, S1.tpartner_type AS tpartner_type, S1.geo_id AS geo_id, S1.eff_start_date AS eff_start_date, S1.eff_end_date AS eff_end_date FROM testSourceName1 AS S1 LEFT JOIN testSourceName2 as S2 ON S1.id=S2.id'}}, target={'targetType': 'DATASET', 'datasetTarget': {'datasetIdentifier': 'arn:aws:scn:us-east-1:123456789012:instance/8850c54e-e187-4fa7-89d4-6370f165174d/namespaces/asc/datasets/trading_partner', 'options': {'loadType': 'REPLACE', 'dedupeRecords': True, 'dedupeStrategy': {'type': 'FIELD_PRIORITY', 'fieldPriority': {'fields': [{'name': 'eff_start_date', 'sortOrder': 'DESC'}]}}}}}, tags={'tagKey1': 'tagValue1'})
        """

        def _handler(
            req: "OperationRequest[capo_supplychain.types.create_data_integration_flow_request.CreateDataIntegrationFlowRequest]",
        ) -> OperationResponse[
            "capo_supplychain.types.create_data_integration_flow_response.CreateDataIntegrationFlowResponse"
        ]:
            import capo_supplychain._operations.galaxy_public_api_gateway.create_data_integration_flow

            output, http_response = (
                capo_supplychain._operations.galaxy_public_api_gateway.create_data_integration_flow.create_data_integration_flow(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_supplychain.types.create_data_integration_flow_request.CreateDataIntegrationFlowRequest",
        ) -> dict[str, Any]:
            import capo_supplychain.types.create_data_integration_flow_request

            return capo_supplychain.types.create_data_integration_flow_request.redact_sensitive(
                input_
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("CreateDataIntegrationFlow", redact_input=_redact_input),
        )
        input_: capo_supplychain.types.create_data_integration_flow_request.CreateDataIntegrationFlowRequest = {
            "instance_id": instance_id,
            "name": name,
            "sources": sources,
            "transformation": transformation,
            "target": target,
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

    def read(
        self,
        instance_id: "capo_supplychain.types.uuid.UUID",
        name: "capo_supplychain.types.data_integration_flow_name.DataIntegrationFlowName",
        *,
        config_overrides: Optional[SupplyChainClientConfig] = None,
    ) -> "capo_supplychain.types.get_data_integration_flow_response.GetDataIntegrationFlowResponse":
        """<p>Enables you to programmatically view a specific data pipeline for the provided Amazon Web Services Supply Chain instance and DataIntegrationFlow name.</p>

        Args:
            instance_id: <p>The Amazon Web Services Supply Chain instance identifier.</p>
            name: <p>The name of the DataIntegrationFlow created.</p>

        Raises:
            capo_supplychain.errors.access_denied_exception.AccessDeniedException: <p>You do not have the required privileges to perform this action.</p>
            capo_supplychain.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            capo_supplychain.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_supplychain.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_supplychain.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Request would cause a service quota to be exceeded.</p>
            capo_supplychain.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_supplychain.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an AWS service.</p>
            capo_supplychain.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Successful GetDataIntegrationFlow

            >>> client.read(instance_id='8850c54e-e187-4fa7-89d4-6370f165174d', name='testStagingFlow')
        """

        def _handler(
            req: "OperationRequest[capo_supplychain.types.get_data_integration_flow_request.GetDataIntegrationFlowRequest]",
        ) -> OperationResponse[
            "capo_supplychain.types.get_data_integration_flow_response.GetDataIntegrationFlowResponse"
        ]:
            import capo_supplychain._operations.galaxy_public_api_gateway.get_data_integration_flow

            output, http_response = (
                capo_supplychain._operations.galaxy_public_api_gateway.get_data_integration_flow.get_data_integration_flow(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_supplychain.types.get_data_integration_flow_response.GetDataIntegrationFlowResponse",
        ) -> dict[str, Any]:
            import capo_supplychain.types.get_data_integration_flow_response

            return capo_supplychain.types.get_data_integration_flow_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("GetDataIntegrationFlow", redact_output=_redact_output),
        )
        input_: capo_supplychain.types.get_data_integration_flow_request.GetDataIntegrationFlowRequest = {
            "instance_id": instance_id,
            "name": name,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update(
        self,
        instance_id: "capo_supplychain.types.uuid.UUID",
        name: "capo_supplychain.types.data_integration_flow_name.DataIntegrationFlowName",
        *,
        config_overrides: Optional[SupplyChainClientConfig] = None,
        sources: Optional[
            "capo_supplychain.types.data_integration_flow_source_list.DataIntegrationFlowSourceList"
        ] = None,
        transformation: Optional[
            "capo_supplychain.types.data_integration_flow_transformation.DataIntegrationFlowTransformation"
        ] = None,
        target: Optional[
            "capo_supplychain.types.data_integration_flow_target.DataIntegrationFlowTarget"
        ] = None,
    ) -> "capo_supplychain.types.update_data_integration_flow_response.UpdateDataIntegrationFlowResponse":
        """<p>Enables you to programmatically update an existing data pipeline to ingest data from the source systems such as, Amazon S3 buckets, to a predefined Amazon Web Services Supply Chain dataset (product, inbound_order) or a temporary dataset along with the data transformation query provided with the API.</p>

        Args:
            instance_id: <p>The Amazon Web Services Supply Chain instance identifier.</p>
            name: <p>The name of the DataIntegrationFlow to be updated.</p>
            sources: <p>The new source configurations for the DataIntegrationFlow.</p>
            transformation: <p>The new transformation configurations for the DataIntegrationFlow.</p>
            target: <p>The new target configurations for the DataIntegrationFlow.</p>

        Raises:
            capo_supplychain.errors.access_denied_exception.AccessDeniedException: <p>You do not have the required privileges to perform this action.</p>
            capo_supplychain.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            capo_supplychain.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_supplychain.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_supplychain.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Request would cause a service quota to be exceeded.</p>
            capo_supplychain.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_supplychain.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an AWS service.</p>
            capo_supplychain.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Successful UpdateDataIntegrationFlow for s3 to dataset flow to update SQL transformation

            >>> client.update(instance_id='8850c54e-e187-4fa7-89d4-6370f165174d', name='testStagingFlow', sources=[{'sourceType': 'S3', 'sourceName': 'testSourceName', 's3Source': {'bucketName': 'aws-supply-chain-data-b8c7bb28-a576-4334-b481-6d6e8e47371f', 'prefix': 'example-prefix'}}], transformation={'transformationType': 'SQL', 'sqlTransformation': {'query': "SELECT connection_id, bukrs AS id, txtmd AS description FROM testSourceName WHERE langu = 'E'"}}, target={'targetType': 'DATASET', 'datasetTarget': {'datasetIdentifier': 'arn:aws:scn:us-east-1:123456789012:instance/8850c54e-e187-4fa7-89d4-6370f165174d/namespaces/default/datasets/my_staging_dataset'}})
            Successful UpdateDataIntegrationFlow for dataset to dataset flow to update sources

            >>> client.update(instance_id='8850c54e-e187-4fa7-89d4-6370f165174d', name='trading-partner', sources=[{'sourceType': 'DATASET', 'sourceName': 'testSourceName1', 'datasetSource': {'datasetIdentifier': 'arn:aws:scn:us-east-1:123456789012:instance/8850c54e-e187-4fa7-89d4-6370f165174d/namespaces/default/datasets/my_staging_dataset1'}}, {'sourceType': 'DATASET', 'sourceName': 'testSourceName2', 'datasetSource': {'datasetIdentifier': 'arn:aws:scn:us-east-1:123456789012:instance/8850c54e-e187-4fa7-89d4-6370f165174d/namespaces/default/datasets/my_staging_dataset2_updated'}}], transformation={'transformationType': 'SQL', 'sqlTransformation': {'query': 'SELECT S1.id AS id, S1.poc_org_unit_description AS description, S1.company_id AS company_id, S1.tpartner_type AS tpartner_type, S1.geo_id AS geo_id, S1.eff_start_date AS eff_start_date, S1.eff_end_date AS eff_end_date FROM testSourceName1 AS S1 LEFT JOIN testSourceName2 as S2 ON S1.id=S2.id'}}, target={'targetType': 'DATASET', 'datasetTarget': {'datasetIdentifier': 'arn:aws:scn:us-east-1:123456789012:instance/8850c54e-e187-4fa7-89d4-6370f165174d/namespaces/asc/datasets/trading_partner', 'options': {'loadType': 'REPLACE', 'dedupeRecords': True, 'dedupeStrategy': {'type': 'FIELD_PRIORITY', 'fieldPriority': {'fields': [{'name': 'eff_start_date', 'sortOrder': 'ASC'}]}}}}})
        """

        def _handler(
            req: "OperationRequest[capo_supplychain.types.update_data_integration_flow_request.UpdateDataIntegrationFlowRequest]",
        ) -> OperationResponse[
            "capo_supplychain.types.update_data_integration_flow_response.UpdateDataIntegrationFlowResponse"
        ]:
            import capo_supplychain._operations.galaxy_public_api_gateway.update_data_integration_flow

            output, http_response = (
                capo_supplychain._operations.galaxy_public_api_gateway.update_data_integration_flow.update_data_integration_flow(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_supplychain.types.update_data_integration_flow_request.UpdateDataIntegrationFlowRequest",
        ) -> dict[str, Any]:
            import capo_supplychain.types.update_data_integration_flow_request

            return capo_supplychain.types.update_data_integration_flow_request.redact_sensitive(
                input_
            )

        def _redact_output(
            output: "capo_supplychain.types.update_data_integration_flow_response.UpdateDataIntegrationFlowResponse",
        ) -> dict[str, Any]:
            import capo_supplychain.types.update_data_integration_flow_response

            return capo_supplychain.types.update_data_integration_flow_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "UpdateDataIntegrationFlow",
                redact_input=_redact_input,
                redact_output=_redact_output,
            ),
        )
        input_: capo_supplychain.types.update_data_integration_flow_request.UpdateDataIntegrationFlowRequest = {
            "instance_id": instance_id,
            "name": name,
        }
        if sources is not None:
            input_["sources"] = sources
        if transformation is not None:
            input_["transformation"] = transformation
        if target is not None:
            input_["target"] = target

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete(
        self,
        instance_id: "capo_supplychain.types.uuid.UUID",
        name: "capo_supplychain.types.data_integration_flow_name.DataIntegrationFlowName",
        *,
        config_overrides: Optional[SupplyChainClientConfig] = None,
    ) -> "capo_supplychain.types.delete_data_integration_flow_response.DeleteDataIntegrationFlowResponse":
        """<p>Enable you to programmatically delete an existing data pipeline for the provided Amazon Web Services Supply Chain instance and DataIntegrationFlow name.</p>

        Args:
            instance_id: <p>The Amazon Web Services Supply Chain instance identifier.</p>
            name: <p>The name of the DataIntegrationFlow to be deleted.</p>

        Raises:
            capo_supplychain.errors.access_denied_exception.AccessDeniedException: <p>You do not have the required privileges to perform this action.</p>
            capo_supplychain.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            capo_supplychain.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_supplychain.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_supplychain.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Request would cause a service quota to be exceeded.</p>
            capo_supplychain.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_supplychain.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an AWS service.</p>
            capo_supplychain.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Successful DeleteDataIntegrationFlow

            >>> client.delete(instance_id='8850c54e-e187-4fa7-89d4-6370f165174d', name='testStagingFlow')
        """

        def _handler(
            req: "OperationRequest[capo_supplychain.types.delete_data_integration_flow_request.DeleteDataIntegrationFlowRequest]",
        ) -> OperationResponse[
            "capo_supplychain.types.delete_data_integration_flow_response.DeleteDataIntegrationFlowResponse"
        ]:
            import capo_supplychain._operations.galaxy_public_api_gateway.delete_data_integration_flow

            output, http_response = (
                capo_supplychain._operations.galaxy_public_api_gateway.delete_data_integration_flow.delete_data_integration_flow(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteDataIntegrationFlow")
        )
        input_: capo_supplychain.types.delete_data_integration_flow_request.DeleteDataIntegrationFlowRequest = {
            "instance_id": instance_id,
            "name": name,
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
        instance_id: "capo_supplychain.types.uuid.UUID",
        *,
        config_overrides: Optional[SupplyChainClientConfig] = None,
        next_token: Optional[
            "capo_supplychain.types.data_integration_flow_next_token.DataIntegrationFlowNextToken"
        ] = None,
        max_results: Optional[
            "capo_supplychain.types.data_integration_flow_max_results.DataIntegrationFlowMaxResults"
        ] = None,
    ) -> "capo_supplychain.types.list_data_integration_flows_response.ListDataIntegrationFlowsResponse":
        """<p>Enables you to programmatically list all data pipelines for the provided Amazon Web Services Supply Chain instance.</p>

        Args:
            instance_id: <p>The Amazon Web Services Supply Chain instance identifier.</p>
            next_token: <p>The pagination token to fetch the next page of the DataIntegrationFlows.</p>
            max_results: <p>Specify the maximum number of DataIntegrationFlows to fetch in one paginated request.</p>

        Raises:
            capo_supplychain.errors.access_denied_exception.AccessDeniedException: <p>You do not have the required privileges to perform this action.</p>
            capo_supplychain.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            capo_supplychain.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_supplychain.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_supplychain.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Request would cause a service quota to be exceeded.</p>
            capo_supplychain.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_supplychain.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an AWS service.</p>
            capo_supplychain.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Successful ListDataIntegrationFlow

            >>> client.list(instance_id='8850c54e-e187-4fa7-89d4-6370f165174d')
        """

        def _handler(
            req: "OperationRequest[capo_supplychain.types.list_data_integration_flows_request.ListDataIntegrationFlowsRequest]",
        ) -> OperationResponse[
            "capo_supplychain.types.list_data_integration_flows_response.ListDataIntegrationFlowsResponse"
        ]:
            import capo_supplychain._operations.galaxy_public_api_gateway.list_data_integration_flows

            output, http_response = (
                capo_supplychain._operations.galaxy_public_api_gateway.list_data_integration_flows.list_data_integration_flows(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_supplychain.types.list_data_integration_flows_response.ListDataIntegrationFlowsResponse",
        ) -> dict[str, Any]:
            import capo_supplychain.types.list_data_integration_flows_response

            return capo_supplychain.types.list_data_integration_flows_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("ListDataIntegrationFlows", redact_output=_redact_output),
        )
        input_: capo_supplychain.types.list_data_integration_flows_request.ListDataIntegrationFlowsRequest = {
            "instance_id": instance_id
        }
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


class AsyncDataIntegrationFlowResource:
    def __init__(self, service: AsyncSupplyChainClient) -> None:
        self._service = service

    async def put(
        self,
        instance_id: "capo_supplychain.types.uuid.UUID",
        name: "capo_supplychain.types.data_integration_flow_name.DataIntegrationFlowName",
        sources: "capo_supplychain.types.data_integration_flow_source_list.DataIntegrationFlowSourceList",
        transformation: "capo_supplychain.types.data_integration_flow_transformation.DataIntegrationFlowTransformation",
        target: "capo_supplychain.types.data_integration_flow_target.DataIntegrationFlowTarget",
        *,
        config_overrides: Optional[AsyncSupplyChainClientConfig] = None,
        tags: Optional["capo_supplychain.types.tag_map.TagMap"] = None,
    ) -> "capo_supplychain.types.create_data_integration_flow_response.CreateDataIntegrationFlowResponse":
        """<p>Enables you to programmatically create a data pipeline to ingest data from source systems such as Amazon S3 buckets, to a predefined Amazon Web Services Supply Chain dataset (product, inbound_order) or a temporary dataset along with the data transformation query provided with the API.</p>

        Args:
            instance_id: <p>The Amazon Web Services Supply Chain instance identifier.</p>
            name: <p>Name of the DataIntegrationFlow.</p>
            sources: <p>The source configurations for DataIntegrationFlow.</p>
            transformation: <p>The transformation configurations for DataIntegrationFlow.</p>
            target: <p>The target configurations for DataIntegrationFlow.</p>
            tags: <p>The tags of the DataIntegrationFlow to be created</p>

        Raises:
            capo_supplychain.errors.access_denied_exception.AccessDeniedException: <p>You do not have the required privileges to perform this action.</p>
            capo_supplychain.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            capo_supplychain.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_supplychain.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_supplychain.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Request would cause a service quota to be exceeded.</p>
            capo_supplychain.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_supplychain.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an AWS service.</p>
            capo_supplychain.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Successful CreateDataIntegrationFlow for s3 to dataset flow

            >>> await client.put(instance_id='8850c54e-e187-4fa7-89d4-6370f165174d', name='testStagingFlow', sources=[{'sourceType': 'S3', 'sourceName': 'testSourceName', 's3Source': {'bucketName': 'aws-supply-chain-data-b8c7bb28-a576-4334-b481-6d6e8e47371f', 'prefix': 'example-prefix'}}], transformation={'transformationType': 'SQL', 'sqlTransformation': {'query': 'SELECT * FROM testSourceName'}}, target={'targetType': 'DATASET', 'datasetTarget': {'datasetIdentifier': 'arn:aws:scn:us-east-1:123456789012:instance/8850c54e-e187-4fa7-89d4-6370f165174d/namespaces/default/datasets/my_staging_dataset'}}, tags={'tagKey1': 'tagValue1'})
            Successful CreateDataIntegrationFlow for dataset to dataset flow

            >>> await client.put(instance_id='8850c54e-e187-4fa7-89d4-6370f165174d', name='trading-partner', sources=[{'sourceType': 'DATASET', 'sourceName': 'testSourceName1', 'datasetSource': {'datasetIdentifier': 'arn:aws:scn:us-east-1:123456789012:instance/8850c54e-e187-4fa7-89d4-6370f165174d/namespaces/default/datasets/my_staging_dataset1'}}, {'sourceType': 'DATASET', 'sourceName': 'testSourceName2', 'datasetSource': {'datasetIdentifier': 'arn:aws:scn:us-east-1:123456789012:instance/8850c54e-e187-4fa7-89d4-6370f165174d/namespaces/default/datasets/my_staging_dataset2'}}], transformation={'transformationType': 'SQL', 'sqlTransformation': {'query': 'SELECT S1.id AS id, S1.poc_org_unit_description AS description, S1.company_id AS company_id, S1.tpartner_type AS tpartner_type, S1.geo_id AS geo_id, S1.eff_start_date AS eff_start_date, S1.eff_end_date AS eff_end_date FROM testSourceName1 AS S1 LEFT JOIN testSourceName2 as S2 ON S1.id=S2.id'}}, target={'targetType': 'DATASET', 'datasetTarget': {'datasetIdentifier': 'arn:aws:scn:us-east-1:123456789012:instance/8850c54e-e187-4fa7-89d4-6370f165174d/namespaces/asc/datasets/trading_partner', 'options': {'loadType': 'REPLACE', 'dedupeRecords': True, 'dedupeStrategy': {'type': 'FIELD_PRIORITY', 'fieldPriority': {'fields': [{'name': 'eff_start_date', 'sortOrder': 'DESC'}]}}}}}, tags={'tagKey1': 'tagValue1'})
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_supplychain.types.create_data_integration_flow_request.CreateDataIntegrationFlowRequest]",
        ) -> AsyncOperationResponse[
            "capo_supplychain.types.create_data_integration_flow_response.CreateDataIntegrationFlowResponse"
        ]:
            import capo_supplychain._operations.galaxy_public_api_gateway.create_data_integration_flow

            (
                output,
                http_response,
            ) = await capo_supplychain._operations.galaxy_public_api_gateway.create_data_integration_flow.async_create_data_integration_flow(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_supplychain.types.create_data_integration_flow_request.CreateDataIntegrationFlowRequest",
        ) -> dict[str, Any]:
            import capo_supplychain.types.create_data_integration_flow_request

            return capo_supplychain.types.create_data_integration_flow_request.redact_sensitive(
                input_
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("CreateDataIntegrationFlow", redact_input=_redact_input),
        )
        input_: capo_supplychain.types.create_data_integration_flow_request.CreateDataIntegrationFlowRequest = {
            "instance_id": instance_id,
            "name": name,
            "sources": sources,
            "transformation": transformation,
            "target": target,
        }
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def read(
        self,
        instance_id: "capo_supplychain.types.uuid.UUID",
        name: "capo_supplychain.types.data_integration_flow_name.DataIntegrationFlowName",
        *,
        config_overrides: Optional[AsyncSupplyChainClientConfig] = None,
    ) -> "capo_supplychain.types.get_data_integration_flow_response.GetDataIntegrationFlowResponse":
        """<p>Enables you to programmatically view a specific data pipeline for the provided Amazon Web Services Supply Chain instance and DataIntegrationFlow name.</p>

        Args:
            instance_id: <p>The Amazon Web Services Supply Chain instance identifier.</p>
            name: <p>The name of the DataIntegrationFlow created.</p>

        Raises:
            capo_supplychain.errors.access_denied_exception.AccessDeniedException: <p>You do not have the required privileges to perform this action.</p>
            capo_supplychain.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            capo_supplychain.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_supplychain.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_supplychain.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Request would cause a service quota to be exceeded.</p>
            capo_supplychain.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_supplychain.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an AWS service.</p>
            capo_supplychain.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Successful GetDataIntegrationFlow

            >>> await client.read(instance_id='8850c54e-e187-4fa7-89d4-6370f165174d', name='testStagingFlow')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_supplychain.types.get_data_integration_flow_request.GetDataIntegrationFlowRequest]",
        ) -> AsyncOperationResponse[
            "capo_supplychain.types.get_data_integration_flow_response.GetDataIntegrationFlowResponse"
        ]:
            import capo_supplychain._operations.galaxy_public_api_gateway.get_data_integration_flow

            (
                output,
                http_response,
            ) = await capo_supplychain._operations.galaxy_public_api_gateway.get_data_integration_flow.async_get_data_integration_flow(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_supplychain.types.get_data_integration_flow_response.GetDataIntegrationFlowResponse",
        ) -> dict[str, Any]:
            import capo_supplychain.types.get_data_integration_flow_response

            return capo_supplychain.types.get_data_integration_flow_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("GetDataIntegrationFlow", redact_output=_redact_output),
        )
        input_: capo_supplychain.types.get_data_integration_flow_request.GetDataIntegrationFlowRequest = {
            "instance_id": instance_id,
            "name": name,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update(
        self,
        instance_id: "capo_supplychain.types.uuid.UUID",
        name: "capo_supplychain.types.data_integration_flow_name.DataIntegrationFlowName",
        *,
        config_overrides: Optional[AsyncSupplyChainClientConfig] = None,
        sources: Optional[
            "capo_supplychain.types.data_integration_flow_source_list.DataIntegrationFlowSourceList"
        ] = None,
        transformation: Optional[
            "capo_supplychain.types.data_integration_flow_transformation.DataIntegrationFlowTransformation"
        ] = None,
        target: Optional[
            "capo_supplychain.types.data_integration_flow_target.DataIntegrationFlowTarget"
        ] = None,
    ) -> "capo_supplychain.types.update_data_integration_flow_response.UpdateDataIntegrationFlowResponse":
        """<p>Enables you to programmatically update an existing data pipeline to ingest data from the source systems such as, Amazon S3 buckets, to a predefined Amazon Web Services Supply Chain dataset (product, inbound_order) or a temporary dataset along with the data transformation query provided with the API.</p>

        Args:
            instance_id: <p>The Amazon Web Services Supply Chain instance identifier.</p>
            name: <p>The name of the DataIntegrationFlow to be updated.</p>
            sources: <p>The new source configurations for the DataIntegrationFlow.</p>
            transformation: <p>The new transformation configurations for the DataIntegrationFlow.</p>
            target: <p>The new target configurations for the DataIntegrationFlow.</p>

        Raises:
            capo_supplychain.errors.access_denied_exception.AccessDeniedException: <p>You do not have the required privileges to perform this action.</p>
            capo_supplychain.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            capo_supplychain.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_supplychain.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_supplychain.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Request would cause a service quota to be exceeded.</p>
            capo_supplychain.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_supplychain.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an AWS service.</p>
            capo_supplychain.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Successful UpdateDataIntegrationFlow for s3 to dataset flow to update SQL transformation

            >>> await client.update(instance_id='8850c54e-e187-4fa7-89d4-6370f165174d', name='testStagingFlow', sources=[{'sourceType': 'S3', 'sourceName': 'testSourceName', 's3Source': {'bucketName': 'aws-supply-chain-data-b8c7bb28-a576-4334-b481-6d6e8e47371f', 'prefix': 'example-prefix'}}], transformation={'transformationType': 'SQL', 'sqlTransformation': {'query': "SELECT connection_id, bukrs AS id, txtmd AS description FROM testSourceName WHERE langu = 'E'"}}, target={'targetType': 'DATASET', 'datasetTarget': {'datasetIdentifier': 'arn:aws:scn:us-east-1:123456789012:instance/8850c54e-e187-4fa7-89d4-6370f165174d/namespaces/default/datasets/my_staging_dataset'}})
            Successful UpdateDataIntegrationFlow for dataset to dataset flow to update sources

            >>> await client.update(instance_id='8850c54e-e187-4fa7-89d4-6370f165174d', name='trading-partner', sources=[{'sourceType': 'DATASET', 'sourceName': 'testSourceName1', 'datasetSource': {'datasetIdentifier': 'arn:aws:scn:us-east-1:123456789012:instance/8850c54e-e187-4fa7-89d4-6370f165174d/namespaces/default/datasets/my_staging_dataset1'}}, {'sourceType': 'DATASET', 'sourceName': 'testSourceName2', 'datasetSource': {'datasetIdentifier': 'arn:aws:scn:us-east-1:123456789012:instance/8850c54e-e187-4fa7-89d4-6370f165174d/namespaces/default/datasets/my_staging_dataset2_updated'}}], transformation={'transformationType': 'SQL', 'sqlTransformation': {'query': 'SELECT S1.id AS id, S1.poc_org_unit_description AS description, S1.company_id AS company_id, S1.tpartner_type AS tpartner_type, S1.geo_id AS geo_id, S1.eff_start_date AS eff_start_date, S1.eff_end_date AS eff_end_date FROM testSourceName1 AS S1 LEFT JOIN testSourceName2 as S2 ON S1.id=S2.id'}}, target={'targetType': 'DATASET', 'datasetTarget': {'datasetIdentifier': 'arn:aws:scn:us-east-1:123456789012:instance/8850c54e-e187-4fa7-89d4-6370f165174d/namespaces/asc/datasets/trading_partner', 'options': {'loadType': 'REPLACE', 'dedupeRecords': True, 'dedupeStrategy': {'type': 'FIELD_PRIORITY', 'fieldPriority': {'fields': [{'name': 'eff_start_date', 'sortOrder': 'ASC'}]}}}}})
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_supplychain.types.update_data_integration_flow_request.UpdateDataIntegrationFlowRequest]",
        ) -> AsyncOperationResponse[
            "capo_supplychain.types.update_data_integration_flow_response.UpdateDataIntegrationFlowResponse"
        ]:
            import capo_supplychain._operations.galaxy_public_api_gateway.update_data_integration_flow

            (
                output,
                http_response,
            ) = await capo_supplychain._operations.galaxy_public_api_gateway.update_data_integration_flow.async_update_data_integration_flow(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_supplychain.types.update_data_integration_flow_request.UpdateDataIntegrationFlowRequest",
        ) -> dict[str, Any]:
            import capo_supplychain.types.update_data_integration_flow_request

            return capo_supplychain.types.update_data_integration_flow_request.redact_sensitive(
                input_
            )

        def _redact_output(
            output: "capo_supplychain.types.update_data_integration_flow_response.UpdateDataIntegrationFlowResponse",
        ) -> dict[str, Any]:
            import capo_supplychain.types.update_data_integration_flow_response

            return capo_supplychain.types.update_data_integration_flow_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "UpdateDataIntegrationFlow",
                redact_input=_redact_input,
                redact_output=_redact_output,
            ),
        )
        input_: capo_supplychain.types.update_data_integration_flow_request.UpdateDataIntegrationFlowRequest = {
            "instance_id": instance_id,
            "name": name,
        }
        if sources is not None:
            input_["sources"] = sources
        if transformation is not None:
            input_["transformation"] = transformation
        if target is not None:
            input_["target"] = target

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete(
        self,
        instance_id: "capo_supplychain.types.uuid.UUID",
        name: "capo_supplychain.types.data_integration_flow_name.DataIntegrationFlowName",
        *,
        config_overrides: Optional[AsyncSupplyChainClientConfig] = None,
    ) -> "capo_supplychain.types.delete_data_integration_flow_response.DeleteDataIntegrationFlowResponse":
        """<p>Enable you to programmatically delete an existing data pipeline for the provided Amazon Web Services Supply Chain instance and DataIntegrationFlow name.</p>

        Args:
            instance_id: <p>The Amazon Web Services Supply Chain instance identifier.</p>
            name: <p>The name of the DataIntegrationFlow to be deleted.</p>

        Raises:
            capo_supplychain.errors.access_denied_exception.AccessDeniedException: <p>You do not have the required privileges to perform this action.</p>
            capo_supplychain.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            capo_supplychain.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_supplychain.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_supplychain.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Request would cause a service quota to be exceeded.</p>
            capo_supplychain.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_supplychain.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an AWS service.</p>
            capo_supplychain.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Successful DeleteDataIntegrationFlow

            >>> await client.delete(instance_id='8850c54e-e187-4fa7-89d4-6370f165174d', name='testStagingFlow')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_supplychain.types.delete_data_integration_flow_request.DeleteDataIntegrationFlowRequest]",
        ) -> AsyncOperationResponse[
            "capo_supplychain.types.delete_data_integration_flow_response.DeleteDataIntegrationFlowResponse"
        ]:
            import capo_supplychain._operations.galaxy_public_api_gateway.delete_data_integration_flow

            (
                output,
                http_response,
            ) = await capo_supplychain._operations.galaxy_public_api_gateway.delete_data_integration_flow.async_delete_data_integration_flow(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteDataIntegrationFlow")
        )
        input_: capo_supplychain.types.delete_data_integration_flow_request.DeleteDataIntegrationFlowRequest = {
            "instance_id": instance_id,
            "name": name,
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
        instance_id: "capo_supplychain.types.uuid.UUID",
        *,
        config_overrides: Optional[AsyncSupplyChainClientConfig] = None,
        next_token: Optional[
            "capo_supplychain.types.data_integration_flow_next_token.DataIntegrationFlowNextToken"
        ] = None,
        max_results: Optional[
            "capo_supplychain.types.data_integration_flow_max_results.DataIntegrationFlowMaxResults"
        ] = None,
    ) -> "capo_supplychain.types.list_data_integration_flows_response.ListDataIntegrationFlowsResponse":
        """<p>Enables you to programmatically list all data pipelines for the provided Amazon Web Services Supply Chain instance.</p>

        Args:
            instance_id: <p>The Amazon Web Services Supply Chain instance identifier.</p>
            next_token: <p>The pagination token to fetch the next page of the DataIntegrationFlows.</p>
            max_results: <p>Specify the maximum number of DataIntegrationFlows to fetch in one paginated request.</p>

        Raises:
            capo_supplychain.errors.access_denied_exception.AccessDeniedException: <p>You do not have the required privileges to perform this action.</p>
            capo_supplychain.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            capo_supplychain.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_supplychain.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_supplychain.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Request would cause a service quota to be exceeded.</p>
            capo_supplychain.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_supplychain.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an AWS service.</p>
            capo_supplychain.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Successful ListDataIntegrationFlow

            >>> await client.list(instance_id='8850c54e-e187-4fa7-89d4-6370f165174d')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_supplychain.types.list_data_integration_flows_request.ListDataIntegrationFlowsRequest]",
        ) -> AsyncOperationResponse[
            "capo_supplychain.types.list_data_integration_flows_response.ListDataIntegrationFlowsResponse"
        ]:
            import capo_supplychain._operations.galaxy_public_api_gateway.list_data_integration_flows

            (
                output,
                http_response,
            ) = await capo_supplychain._operations.galaxy_public_api_gateway.list_data_integration_flows.async_list_data_integration_flows(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_supplychain.types.list_data_integration_flows_response.ListDataIntegrationFlowsResponse",
        ) -> dict[str, Any]:
            import capo_supplychain.types.list_data_integration_flows_response

            return capo_supplychain.types.list_data_integration_flows_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("ListDataIntegrationFlows", redact_output=_redact_output),
        )
        input_: capo_supplychain.types.list_data_integration_flows_request.ListDataIntegrationFlowsRequest = {
            "instance_id": instance_id
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
