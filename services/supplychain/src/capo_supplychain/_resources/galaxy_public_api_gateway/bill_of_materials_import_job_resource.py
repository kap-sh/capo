from __future__ import annotations

import uuid
from typing import TYPE_CHECKING, Optional

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
    import capo_supplychain.types.client_token
    import capo_supplychain.types.configuration_s3_uri
    import capo_supplychain.types.create_bill_of_materials_import_job_request
    import capo_supplychain.types.create_bill_of_materials_import_job_response
    import capo_supplychain.types.get_bill_of_materials_import_job_request
    import capo_supplychain.types.get_bill_of_materials_import_job_response
    import capo_supplychain.types.uuid
    from capo_supplychain._services.async_supply_chain import (
        AsyncSupplyChainClient,
        AsyncSupplyChainClientConfig,
    )
    from capo_supplychain._services.supply_chain import (
        SupplyChainClient,
        SupplyChainClientConfig,
    )


class BillOfMaterialsImportJobResource:
    def __init__(self, service: SupplyChainClient) -> None:
        self._service = service

    def create(
        self,
        instance_id: "capo_supplychain.types.uuid.UUID",
        s3uri: "capo_supplychain.types.configuration_s3_uri.ConfigurationS3Uri",
        *,
        config_overrides: Optional[SupplyChainClientConfig] = None,
        client_token: Optional[
            "capo_supplychain.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_supplychain.types.create_bill_of_materials_import_job_response.CreateBillOfMaterialsImportJobResponse":
        """<p>CreateBillOfMaterialsImportJob creates an import job for the Product Bill Of Materials (BOM) entity. For information on the product_bom entity, see the AWS Supply Chain User Guide.</p> <p>The CSV file must be located in an Amazon S3 location accessible to AWS Supply Chain. It is recommended to use the same Amazon S3 bucket created during your AWS Supply Chain instance creation.</p>

        Args:
            instance_id: <p>The AWS Supply Chain instance identifier.</p>
            s3uri: <p>The S3 URI of the CSV file to be imported. The bucket must grant permissions for AWS Supply Chain to read the file.</p>
            client_token: <p>An idempotency token ensures the API request is only completed no more than once. This way, retrying the request will not trigger the operation multiple times. A client token is a unique, case-sensitive string of 33 to 128 ASCII characters. To make an idempotent API request, specify a client token in the request. You should not reuse the same client token for other requests. If you retry a successful request with the same client token, the request will succeed with no further actions being taken, and you will receive the same API response as the original successful request.</p>

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
            Invoke CreateBillOfMaterialsImportJob

            >>> client.create(instance_id='60f82bbd-71f7-4fcd-a941-472f574c5243', s3uri='s3://mybucketname/pathelemene/file.csv', client_token='550e8400-e29b-41d4-a716-446655440000')
        """

        def _handler(
            req: "OperationRequest[capo_supplychain.types.create_bill_of_materials_import_job_request.CreateBillOfMaterialsImportJobRequest]",
        ) -> OperationResponse[
            "capo_supplychain.types.create_bill_of_materials_import_job_response.CreateBillOfMaterialsImportJobResponse"
        ]:
            import capo_supplychain._operations.galaxy_public_api_gateway.create_bill_of_materials_import_job

            output, http_response = (
                capo_supplychain._operations.galaxy_public_api_gateway.create_bill_of_materials_import_job.create_bill_of_materials_import_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("CreateBillOfMaterialsImportJob")
        )
        input_: capo_supplychain.types.create_bill_of_materials_import_job_request.CreateBillOfMaterialsImportJobRequest = {
            "instance_id": instance_id,
            "s3uri": s3uri,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token

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
        job_id: "capo_supplychain.types.uuid.UUID",
        *,
        config_overrides: Optional[SupplyChainClientConfig] = None,
    ) -> "capo_supplychain.types.get_bill_of_materials_import_job_response.GetBillOfMaterialsImportJobResponse":
        """<p>Get status and details of a BillOfMaterialsImportJob.</p>

        Args:
            instance_id: <p>The AWS Supply Chain instance identifier.</p>
            job_id: <p>The BillOfMaterialsImportJob identifier.</p>

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
            Invoke GetBillOfMaterialsImportJob for a successful job

            >>> client.read(instance_id='60f82bbd-71f7-4fcd-a941-472f574c5243', job_id='f79b359b-1515-4436-a3bf-bae7b33e47b4')
            Invoke GetBillOfMaterialsImportJob for an in-progress job

            >>> client.read(instance_id='60f82bbd-71f7-4fcd-a941-472f574c5243', job_id='f79b359b-1515-4436-a3bf-bae7b33e47b4')
        """

        def _handler(
            req: "OperationRequest[capo_supplychain.types.get_bill_of_materials_import_job_request.GetBillOfMaterialsImportJobRequest]",
        ) -> OperationResponse[
            "capo_supplychain.types.get_bill_of_materials_import_job_response.GetBillOfMaterialsImportJobResponse"
        ]:
            import capo_supplychain._operations.galaxy_public_api_gateway.get_bill_of_materials_import_job

            output, http_response = (
                capo_supplychain._operations.galaxy_public_api_gateway.get_bill_of_materials_import_job.get_bill_of_materials_import_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetBillOfMaterialsImportJob")
        )
        input_: capo_supplychain.types.get_bill_of_materials_import_job_request.GetBillOfMaterialsImportJobRequest = {
            "instance_id": instance_id,
            "job_id": job_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncBillOfMaterialsImportJobResource:
    def __init__(self, service: AsyncSupplyChainClient) -> None:
        self._service = service

    async def create(
        self,
        instance_id: "capo_supplychain.types.uuid.UUID",
        s3uri: "capo_supplychain.types.configuration_s3_uri.ConfigurationS3Uri",
        *,
        config_overrides: Optional[AsyncSupplyChainClientConfig] = None,
        client_token: Optional[
            "capo_supplychain.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_supplychain.types.create_bill_of_materials_import_job_response.CreateBillOfMaterialsImportJobResponse":
        """<p>CreateBillOfMaterialsImportJob creates an import job for the Product Bill Of Materials (BOM) entity. For information on the product_bom entity, see the AWS Supply Chain User Guide.</p> <p>The CSV file must be located in an Amazon S3 location accessible to AWS Supply Chain. It is recommended to use the same Amazon S3 bucket created during your AWS Supply Chain instance creation.</p>

        Args:
            instance_id: <p>The AWS Supply Chain instance identifier.</p>
            s3uri: <p>The S3 URI of the CSV file to be imported. The bucket must grant permissions for AWS Supply Chain to read the file.</p>
            client_token: <p>An idempotency token ensures the API request is only completed no more than once. This way, retrying the request will not trigger the operation multiple times. A client token is a unique, case-sensitive string of 33 to 128 ASCII characters. To make an idempotent API request, specify a client token in the request. You should not reuse the same client token for other requests. If you retry a successful request with the same client token, the request will succeed with no further actions being taken, and you will receive the same API response as the original successful request.</p>

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
            Invoke CreateBillOfMaterialsImportJob

            >>> await client.create(instance_id='60f82bbd-71f7-4fcd-a941-472f574c5243', s3uri='s3://mybucketname/pathelemene/file.csv', client_token='550e8400-e29b-41d4-a716-446655440000')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_supplychain.types.create_bill_of_materials_import_job_request.CreateBillOfMaterialsImportJobRequest]",
        ) -> AsyncOperationResponse[
            "capo_supplychain.types.create_bill_of_materials_import_job_response.CreateBillOfMaterialsImportJobResponse"
        ]:
            import capo_supplychain._operations.galaxy_public_api_gateway.create_bill_of_materials_import_job

            (
                output,
                http_response,
            ) = await capo_supplychain._operations.galaxy_public_api_gateway.create_bill_of_materials_import_job.async_create_bill_of_materials_import_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("CreateBillOfMaterialsImportJob")
        )
        input_: capo_supplychain.types.create_bill_of_materials_import_job_request.CreateBillOfMaterialsImportJobRequest = {
            "instance_id": instance_id,
            "s3uri": s3uri,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token

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
        job_id: "capo_supplychain.types.uuid.UUID",
        *,
        config_overrides: Optional[AsyncSupplyChainClientConfig] = None,
    ) -> "capo_supplychain.types.get_bill_of_materials_import_job_response.GetBillOfMaterialsImportJobResponse":
        """<p>Get status and details of a BillOfMaterialsImportJob.</p>

        Args:
            instance_id: <p>The AWS Supply Chain instance identifier.</p>
            job_id: <p>The BillOfMaterialsImportJob identifier.</p>

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
            Invoke GetBillOfMaterialsImportJob for a successful job

            >>> await client.read(instance_id='60f82bbd-71f7-4fcd-a941-472f574c5243', job_id='f79b359b-1515-4436-a3bf-bae7b33e47b4')
            Invoke GetBillOfMaterialsImportJob for an in-progress job

            >>> await client.read(instance_id='60f82bbd-71f7-4fcd-a941-472f574c5243', job_id='f79b359b-1515-4436-a3bf-bae7b33e47b4')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_supplychain.types.get_bill_of_materials_import_job_request.GetBillOfMaterialsImportJobRequest]",
        ) -> AsyncOperationResponse[
            "capo_supplychain.types.get_bill_of_materials_import_job_response.GetBillOfMaterialsImportJobResponse"
        ]:
            import capo_supplychain._operations.galaxy_public_api_gateway.get_bill_of_materials_import_job

            (
                output,
                http_response,
            ) = await capo_supplychain._operations.galaxy_public_api_gateway.get_bill_of_materials_import_job.async_get_bill_of_materials_import_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetBillOfMaterialsImportJob")
        )
        input_: capo_supplychain.types.get_bill_of_materials_import_job_request.GetBillOfMaterialsImportJobRequest = {
            "instance_id": instance_id,
            "job_id": job_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
