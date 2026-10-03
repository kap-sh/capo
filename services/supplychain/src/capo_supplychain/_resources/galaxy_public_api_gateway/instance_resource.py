from __future__ import annotations

import uuid
from typing import TYPE_CHECKING, Optional

import capo_supplychain._auth._signers
import capo_supplychain._auth._sigv4
from capo_supplychain._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_supplychain.types.client_token
    import capo_supplychain.types.create_instance_request
    import capo_supplychain.types.create_instance_response
    import capo_supplychain.types.delete_instance_request
    import capo_supplychain.types.delete_instance_response
    import capo_supplychain.types.get_instance_request
    import capo_supplychain.types.get_instance_response
    import capo_supplychain.types.instance
    import capo_supplychain.types.instance_description
    import capo_supplychain.types.instance_max_results
    import capo_supplychain.types.instance_name
    import capo_supplychain.types.instance_name_list
    import capo_supplychain.types.instance_next_token
    import capo_supplychain.types.instance_state_list
    import capo_supplychain.types.instance_web_app_dns_domain
    import capo_supplychain.types.kms_key_arn
    import capo_supplychain.types.list_instances_request
    import capo_supplychain.types.list_instances_response
    import capo_supplychain.types.tag_map
    import capo_supplychain.types.update_instance_request
    import capo_supplychain.types.update_instance_response
    import capo_supplychain.types.uuid
    from capo_supplychain._services.async_supply_chain import (
        AsyncSupplyChainClient,
        AsyncSupplyChainClientConfig,
    )
    from capo_supplychain._services.supply_chain import (
        SupplyChainClient,
        SupplyChainClientConfig,
    )


class InstanceResource:
    def __init__(self, service: SupplyChainClient) -> None:
        self._service = service

    def create(
        self,
        *,
        config_overrides: Optional[SupplyChainClientConfig] = None,
        instance_name: Optional[
            "capo_supplychain.types.instance_name.InstanceName"
        ] = None,
        instance_description: Optional[
            "capo_supplychain.types.instance_description.InstanceDescription"
        ] = None,
        kms_key_arn: Optional["capo_supplychain.types.kms_key_arn.KmsKeyArn"] = None,
        web_app_dns_domain: Optional[
            "capo_supplychain.types.instance_web_app_dns_domain.InstanceWebAppDnsDomain"
        ] = None,
        tags: Optional["capo_supplychain.types.tag_map.TagMap"] = None,
        client_token: Optional[
            "capo_supplychain.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_supplychain.types.create_instance_response.CreateInstanceResponse":
        """<p>Enables you to programmatically create an Amazon Web Services Supply Chain instance by applying KMS keys and relevant information associated with the API without using the Amazon Web Services console.</p> <p>This is an asynchronous operation. Upon receiving a CreateInstance request, Amazon Web Services Supply Chain immediately returns the instance resource, instance ID, and the initializing state while simultaneously creating all required Amazon Web Services resources for an instance creation. You can use GetInstance to check the status of the instance. If the instance results in an unhealthy state, you need to check the error message, delete the current instance, and recreate a new one based on the mitigation from the error message.</p>

        Args:
            instance_name: <p>The AWS Supply Chain instance name.</p>
            instance_description: <p>The AWS Supply Chain instance description.</p>
            kms_key_arn: <p>The ARN (Amazon Resource Name) of the Key Management Service (KMS) key you provide for encryption. This is required if you do not want to use the Amazon Web Services owned KMS key. If you don't provide anything here, AWS Supply Chain uses the Amazon Web Services owned KMS key.</p>
            web_app_dns_domain: <p>The DNS subdomain of the web app. This would be "example" in the URL "example.scn.global.on.aws". You can set this to a custom value, as long as the domain isn't already being used by someone else. The name may only include alphanumeric characters and hyphens.</p>
            tags: <p>The Amazon Web Services tags of an instance to be created.</p>
            client_token: <p>The client token for idempotency.</p>

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
            Successful CreateInstance request with all input data

            >>> client.create(instance_name='example instance name', instance_description='example instance description', kms_key_arn='arn:aws:kms:us-west-2:123456789012:key/b14ffc39-b7d4-45ab-991a-6257a7f0d24d', tags={'tagKey1': 'tagValue1'})
            Successful CreateInstance request with no input data

            >>> client.create()
        """

        def _handler(
            req: "OperationRequest[capo_supplychain.types.create_instance_request.CreateInstanceRequest]",
        ) -> OperationResponse[
            "capo_supplychain.types.create_instance_response.CreateInstanceResponse"
        ]:
            import capo_supplychain._operations.galaxy_public_api_gateway.create_instance

            output, http_response = (
                capo_supplychain._operations.galaxy_public_api_gateway.create_instance.create_instance(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_supplychain.types.create_instance_request.CreateInstanceRequest = {}
        if instance_name is not None:
            input_["instance_name"] = instance_name
        if instance_description is not None:
            input_["instance_description"] = instance_description
        if kms_key_arn is not None:
            input_["kms_key_arn"] = kms_key_arn
        if web_app_dns_domain is not None:
            input_["web_app_dns_domain"] = web_app_dns_domain
        if tags is not None:
            input_["tags"] = tags
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
        *,
        config_overrides: Optional[SupplyChainClientConfig] = None,
    ) -> "capo_supplychain.types.get_instance_response.GetInstanceResponse":
        """<p>Enables you to programmatically retrieve the information related to an Amazon Web Services Supply Chain instance ID.</p>

        Args:
            instance_id: <p>The AWS Supply Chain instance identifier</p>

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
            Successful GetInstance request

            >>> client.read(instance_id='9e193580-7cc5-45f7-9609-c43ba0ada793')
            Successful GetInstance request with error message

            >>> client.read(instance_id='9e193580-7cc5-45f7-9609-c43ba0ada793')
        """

        def _handler(
            req: "OperationRequest[capo_supplychain.types.get_instance_request.GetInstanceRequest]",
        ) -> OperationResponse[
            "capo_supplychain.types.get_instance_response.GetInstanceResponse"
        ]:
            import capo_supplychain._operations.galaxy_public_api_gateway.get_instance

            output, http_response = (
                capo_supplychain._operations.galaxy_public_api_gateway.get_instance.get_instance(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_supplychain.types.get_instance_request.GetInstanceRequest = {
            "instance_id": instance_id
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
        *,
        config_overrides: Optional[SupplyChainClientConfig] = None,
        instance_name: Optional[
            "capo_supplychain.types.instance_name.InstanceName"
        ] = None,
        instance_description: Optional[
            "capo_supplychain.types.instance_description.InstanceDescription"
        ] = None,
    ) -> "capo_supplychain.types.update_instance_response.UpdateInstanceResponse":
        """<p>Enables you to programmatically update an Amazon Web Services Supply Chain instance description by providing all the relevant information such as account ID, instance ID and so on without using the AWS console.</p>

        Args:
            instance_id: <p>The AWS Supply Chain instance identifier.</p>
            instance_name: <p>The AWS Supply Chain instance name.</p>
            instance_description: <p>The AWS Supply Chain instance description.</p>

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
            Successful UpdateInstance request

            >>> client.update(instance_id='9e193580-7cc5-45f7-9609-c43ba0ada793', instance_name='updated example instance name', instance_description='updated example instance description')
        """

        def _handler(
            req: "OperationRequest[capo_supplychain.types.update_instance_request.UpdateInstanceRequest]",
        ) -> OperationResponse[
            "capo_supplychain.types.update_instance_response.UpdateInstanceResponse"
        ]:
            import capo_supplychain._operations.galaxy_public_api_gateway.update_instance

            output, http_response = (
                capo_supplychain._operations.galaxy_public_api_gateway.update_instance.update_instance(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_supplychain.types.update_instance_request.UpdateInstanceRequest = {
            "instance_id": instance_id
        }
        if instance_name is not None:
            input_["instance_name"] = instance_name
        if instance_description is not None:
            input_["instance_description"] = instance_description

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
        *,
        config_overrides: Optional[SupplyChainClientConfig] = None,
    ) -> "capo_supplychain.types.delete_instance_response.DeleteInstanceResponse":
        """<p>Enables you to programmatically delete an Amazon Web Services Supply Chain instance by deleting the KMS keys and relevant information associated with the API without using the Amazon Web Services console.</p> <p>This is an asynchronous operation. Upon receiving a DeleteInstance request, Amazon Web Services Supply Chain immediately returns a response with the instance resource, delete state while cleaning up all Amazon Web Services resources created during the instance creation process. You can use the GetInstance action to check the instance status.</p>

        Args:
            instance_id: <p>The AWS Supply Chain instance identifier.</p>

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
            Successful DeleteInstance request

            >>> client.delete(instance_id='9e193580-7cc5-45f7-9609-c43ba0ada793')
        """

        def _handler(
            req: "OperationRequest[capo_supplychain.types.delete_instance_request.DeleteInstanceRequest]",
        ) -> OperationResponse[
            "capo_supplychain.types.delete_instance_response.DeleteInstanceResponse"
        ]:
            import capo_supplychain._operations.galaxy_public_api_gateway.delete_instance

            output, http_response = (
                capo_supplychain._operations.galaxy_public_api_gateway.delete_instance.delete_instance(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_supplychain.types.delete_instance_request.DeleteInstanceRequest = {
            "instance_id": instance_id
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
        config_overrides: Optional[SupplyChainClientConfig] = None,
        next_token: Optional[
            "capo_supplychain.types.instance_next_token.InstanceNextToken"
        ] = None,
        max_results: Optional[
            "capo_supplychain.types.instance_max_results.InstanceMaxResults"
        ] = None,
        instance_name_filter: Optional[
            "capo_supplychain.types.instance_name_list.InstanceNameList"
        ] = None,
        instance_state_filter: Optional[
            "capo_supplychain.types.instance_state_list.InstanceStateList"
        ] = None,
    ) -> "capo_supplychain.types.list_instances_response.ListInstancesResponse":
        """<p>List all Amazon Web Services Supply Chain instances for a specific account. Enables you to programmatically list all Amazon Web Services Supply Chain instances based on their account ID, instance name, and state of the instance (active or delete).</p>

        Args:
            next_token: <p>The pagination token to fetch the next page of instances.</p>
            max_results: <p>Specify the maximum number of instances to fetch in this paginated request.</p>
            instance_name_filter: <p>The filter to ListInstances based on their names.</p>
            instance_state_filter: <p>The filter to ListInstances based on their state.</p>

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
            Successful ListInstance request with no input data

            >>> client.list()
            Successful ListInstance request with filters

            >>> client.list(instance_name_filter=['example instance name'], instance_state_filter=['Active'])
            Successful ListInstance request with maxResult override

            >>> client.list(max_results=1)
            Successful ListInstance request with nextToken

            >>> client.list(next_token='AAQA-EFRSURBSGhtcng0c0dxbENwUHdnckVIbkFYNU1QVjRTZWN2ak5iMFVicC8zemlHOVF3SEpjSC9WTWJVVXBMV2Z1N3ZvZlQ0WEFBQUFmakI4QmdrcWhraUc5dzBCQndhZ2J6QnRBZ0VBTUdnR0NTcUdTSWIzRFFFSEFUQWVCZ2xnaGtnQlpRTUVBUzR3RVFRTTJibW9LemgrSWZTY0RaZEdBZ0VRZ0R2dDhsQnVGbGJ0dnFTZityWmNSWEVPbG93emJoSjhxOGNMbGQ1UGMvY0VRbWlTR3pQUFd4N2RraXY5Y0ovcS9vSmFYZVBGdWVHaU0zWmd0dz09n-rC1ejA5--7ltJxpDT2xP_i8xGqDPMOZfjpp8q6l5NuP9_bnBURvwwYhdqDriMK5_f96LuPEnPbuML-ItfgEiCcUy0p2tApvpZkZqOG5fbqP-4C5aDYPTffHLyq-MMqvfrGVJzL1nvkpZcnTkVR9VJsu5b8I0qqDW0H8EMKGgTo78U9lr4sj3Usi9VMwZxgKCBmr03HhFLYXOW--XMbIx0CTZF0fYIcRxmA_sVS6J7gpaB9yMcnzs5VUKokoA5JTcAPY5d1Y1VyE8KKxv51cfPgXw8OYCDbFQncw8mZPmE-VqxjFbksmk_FmghpPn9j2Ppoe-zr0LQ%3D', max_results=1)
        """

        def _handler(
            req: "OperationRequest[capo_supplychain.types.list_instances_request.ListInstancesRequest]",
        ) -> OperationResponse[
            "capo_supplychain.types.list_instances_response.ListInstancesResponse"
        ]:
            import capo_supplychain._operations.galaxy_public_api_gateway.list_instances

            output, http_response = (
                capo_supplychain._operations.galaxy_public_api_gateway.list_instances.list_instances(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_supplychain.types.list_instances_request.ListInstancesRequest = {}
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if instance_name_filter is not None:
            input_["instance_name_filter"] = instance_name_filter
        if instance_state_filter is not None:
            input_["instance_state_filter"] = instance_state_filter

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncInstanceResource:
    def __init__(self, service: AsyncSupplyChainClient) -> None:
        self._service = service

    async def create(
        self,
        *,
        config_overrides: Optional[AsyncSupplyChainClientConfig] = None,
        instance_name: Optional[
            "capo_supplychain.types.instance_name.InstanceName"
        ] = None,
        instance_description: Optional[
            "capo_supplychain.types.instance_description.InstanceDescription"
        ] = None,
        kms_key_arn: Optional["capo_supplychain.types.kms_key_arn.KmsKeyArn"] = None,
        web_app_dns_domain: Optional[
            "capo_supplychain.types.instance_web_app_dns_domain.InstanceWebAppDnsDomain"
        ] = None,
        tags: Optional["capo_supplychain.types.tag_map.TagMap"] = None,
        client_token: Optional[
            "capo_supplychain.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_supplychain.types.create_instance_response.CreateInstanceResponse":
        """<p>Enables you to programmatically create an Amazon Web Services Supply Chain instance by applying KMS keys and relevant information associated with the API without using the Amazon Web Services console.</p> <p>This is an asynchronous operation. Upon receiving a CreateInstance request, Amazon Web Services Supply Chain immediately returns the instance resource, instance ID, and the initializing state while simultaneously creating all required Amazon Web Services resources for an instance creation. You can use GetInstance to check the status of the instance. If the instance results in an unhealthy state, you need to check the error message, delete the current instance, and recreate a new one based on the mitigation from the error message.</p>

        Args:
            instance_name: <p>The AWS Supply Chain instance name.</p>
            instance_description: <p>The AWS Supply Chain instance description.</p>
            kms_key_arn: <p>The ARN (Amazon Resource Name) of the Key Management Service (KMS) key you provide for encryption. This is required if you do not want to use the Amazon Web Services owned KMS key. If you don't provide anything here, AWS Supply Chain uses the Amazon Web Services owned KMS key.</p>
            web_app_dns_domain: <p>The DNS subdomain of the web app. This would be "example" in the URL "example.scn.global.on.aws". You can set this to a custom value, as long as the domain isn't already being used by someone else. The name may only include alphanumeric characters and hyphens.</p>
            tags: <p>The Amazon Web Services tags of an instance to be created.</p>
            client_token: <p>The client token for idempotency.</p>

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
            Successful CreateInstance request with all input data

            >>> await client.create(instance_name='example instance name', instance_description='example instance description', kms_key_arn='arn:aws:kms:us-west-2:123456789012:key/b14ffc39-b7d4-45ab-991a-6257a7f0d24d', tags={'tagKey1': 'tagValue1'})
            Successful CreateInstance request with no input data

            >>> await client.create()
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_supplychain.types.create_instance_request.CreateInstanceRequest]",
        ) -> AsyncOperationResponse[
            "capo_supplychain.types.create_instance_response.CreateInstanceResponse"
        ]:
            import capo_supplychain._operations.galaxy_public_api_gateway.create_instance

            (
                output,
                http_response,
            ) = await capo_supplychain._operations.galaxy_public_api_gateway.create_instance.async_create_instance(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_supplychain.types.create_instance_request.CreateInstanceRequest = {}
        if instance_name is not None:
            input_["instance_name"] = instance_name
        if instance_description is not None:
            input_["instance_description"] = instance_description
        if kms_key_arn is not None:
            input_["kms_key_arn"] = kms_key_arn
        if web_app_dns_domain is not None:
            input_["web_app_dns_domain"] = web_app_dns_domain
        if tags is not None:
            input_["tags"] = tags
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
        *,
        config_overrides: Optional[AsyncSupplyChainClientConfig] = None,
    ) -> "capo_supplychain.types.get_instance_response.GetInstanceResponse":
        """<p>Enables you to programmatically retrieve the information related to an Amazon Web Services Supply Chain instance ID.</p>

        Args:
            instance_id: <p>The AWS Supply Chain instance identifier</p>

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
            Successful GetInstance request

            >>> await client.read(instance_id='9e193580-7cc5-45f7-9609-c43ba0ada793')
            Successful GetInstance request with error message

            >>> await client.read(instance_id='9e193580-7cc5-45f7-9609-c43ba0ada793')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_supplychain.types.get_instance_request.GetInstanceRequest]",
        ) -> AsyncOperationResponse[
            "capo_supplychain.types.get_instance_response.GetInstanceResponse"
        ]:
            import capo_supplychain._operations.galaxy_public_api_gateway.get_instance

            (
                output,
                http_response,
            ) = await capo_supplychain._operations.galaxy_public_api_gateway.get_instance.async_get_instance(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_supplychain.types.get_instance_request.GetInstanceRequest = {
            "instance_id": instance_id
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
        *,
        config_overrides: Optional[AsyncSupplyChainClientConfig] = None,
        instance_name: Optional[
            "capo_supplychain.types.instance_name.InstanceName"
        ] = None,
        instance_description: Optional[
            "capo_supplychain.types.instance_description.InstanceDescription"
        ] = None,
    ) -> "capo_supplychain.types.update_instance_response.UpdateInstanceResponse":
        """<p>Enables you to programmatically update an Amazon Web Services Supply Chain instance description by providing all the relevant information such as account ID, instance ID and so on without using the AWS console.</p>

        Args:
            instance_id: <p>The AWS Supply Chain instance identifier.</p>
            instance_name: <p>The AWS Supply Chain instance name.</p>
            instance_description: <p>The AWS Supply Chain instance description.</p>

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
            Successful UpdateInstance request

            >>> await client.update(instance_id='9e193580-7cc5-45f7-9609-c43ba0ada793', instance_name='updated example instance name', instance_description='updated example instance description')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_supplychain.types.update_instance_request.UpdateInstanceRequest]",
        ) -> AsyncOperationResponse[
            "capo_supplychain.types.update_instance_response.UpdateInstanceResponse"
        ]:
            import capo_supplychain._operations.galaxy_public_api_gateway.update_instance

            (
                output,
                http_response,
            ) = await capo_supplychain._operations.galaxy_public_api_gateway.update_instance.async_update_instance(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_supplychain.types.update_instance_request.UpdateInstanceRequest = {
            "instance_id": instance_id
        }
        if instance_name is not None:
            input_["instance_name"] = instance_name
        if instance_description is not None:
            input_["instance_description"] = instance_description

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
        *,
        config_overrides: Optional[AsyncSupplyChainClientConfig] = None,
    ) -> "capo_supplychain.types.delete_instance_response.DeleteInstanceResponse":
        """<p>Enables you to programmatically delete an Amazon Web Services Supply Chain instance by deleting the KMS keys and relevant information associated with the API without using the Amazon Web Services console.</p> <p>This is an asynchronous operation. Upon receiving a DeleteInstance request, Amazon Web Services Supply Chain immediately returns a response with the instance resource, delete state while cleaning up all Amazon Web Services resources created during the instance creation process. You can use the GetInstance action to check the instance status.</p>

        Args:
            instance_id: <p>The AWS Supply Chain instance identifier.</p>

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
            Successful DeleteInstance request

            >>> await client.delete(instance_id='9e193580-7cc5-45f7-9609-c43ba0ada793')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_supplychain.types.delete_instance_request.DeleteInstanceRequest]",
        ) -> AsyncOperationResponse[
            "capo_supplychain.types.delete_instance_response.DeleteInstanceResponse"
        ]:
            import capo_supplychain._operations.galaxy_public_api_gateway.delete_instance

            (
                output,
                http_response,
            ) = await capo_supplychain._operations.galaxy_public_api_gateway.delete_instance.async_delete_instance(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_supplychain.types.delete_instance_request.DeleteInstanceRequest = {
            "instance_id": instance_id
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
        config_overrides: Optional[AsyncSupplyChainClientConfig] = None,
        next_token: Optional[
            "capo_supplychain.types.instance_next_token.InstanceNextToken"
        ] = None,
        max_results: Optional[
            "capo_supplychain.types.instance_max_results.InstanceMaxResults"
        ] = None,
        instance_name_filter: Optional[
            "capo_supplychain.types.instance_name_list.InstanceNameList"
        ] = None,
        instance_state_filter: Optional[
            "capo_supplychain.types.instance_state_list.InstanceStateList"
        ] = None,
    ) -> "capo_supplychain.types.list_instances_response.ListInstancesResponse":
        """<p>List all Amazon Web Services Supply Chain instances for a specific account. Enables you to programmatically list all Amazon Web Services Supply Chain instances based on their account ID, instance name, and state of the instance (active or delete).</p>

        Args:
            next_token: <p>The pagination token to fetch the next page of instances.</p>
            max_results: <p>Specify the maximum number of instances to fetch in this paginated request.</p>
            instance_name_filter: <p>The filter to ListInstances based on their names.</p>
            instance_state_filter: <p>The filter to ListInstances based on their state.</p>

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
            Successful ListInstance request with no input data

            >>> await client.list()
            Successful ListInstance request with filters

            >>> await client.list(instance_name_filter=['example instance name'], instance_state_filter=['Active'])
            Successful ListInstance request with maxResult override

            >>> await client.list(max_results=1)
            Successful ListInstance request with nextToken

            >>> await client.list(next_token='AAQA-EFRSURBSGhtcng0c0dxbENwUHdnckVIbkFYNU1QVjRTZWN2ak5iMFVicC8zemlHOVF3SEpjSC9WTWJVVXBMV2Z1N3ZvZlQ0WEFBQUFmakI4QmdrcWhraUc5dzBCQndhZ2J6QnRBZ0VBTUdnR0NTcUdTSWIzRFFFSEFUQWVCZ2xnaGtnQlpRTUVBUzR3RVFRTTJibW9LemgrSWZTY0RaZEdBZ0VRZ0R2dDhsQnVGbGJ0dnFTZityWmNSWEVPbG93emJoSjhxOGNMbGQ1UGMvY0VRbWlTR3pQUFd4N2RraXY5Y0ovcS9vSmFYZVBGdWVHaU0zWmd0dz09n-rC1ejA5--7ltJxpDT2xP_i8xGqDPMOZfjpp8q6l5NuP9_bnBURvwwYhdqDriMK5_f96LuPEnPbuML-ItfgEiCcUy0p2tApvpZkZqOG5fbqP-4C5aDYPTffHLyq-MMqvfrGVJzL1nvkpZcnTkVR9VJsu5b8I0qqDW0H8EMKGgTo78U9lr4sj3Usi9VMwZxgKCBmr03HhFLYXOW--XMbIx0CTZF0fYIcRxmA_sVS6J7gpaB9yMcnzs5VUKokoA5JTcAPY5d1Y1VyE8KKxv51cfPgXw8OYCDbFQncw8mZPmE-VqxjFbksmk_FmghpPn9j2Ppoe-zr0LQ%3D', max_results=1)
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_supplychain.types.list_instances_request.ListInstancesRequest]",
        ) -> AsyncOperationResponse[
            "capo_supplychain.types.list_instances_response.ListInstancesResponse"
        ]:
            import capo_supplychain._operations.galaxy_public_api_gateway.list_instances

            (
                output,
                http_response,
            ) = await capo_supplychain._operations.galaxy_public_api_gateway.list_instances.async_list_instances(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_supplychain.types.list_instances_request.ListInstancesRequest = {}
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if instance_name_filter is not None:
            input_["instance_name_filter"] = instance_name_filter
        if instance_state_filter is not None:
            input_["instance_state_filter"] = instance_state_filter

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
