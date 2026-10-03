from __future__ import annotations

import uuid
from typing import TYPE_CHECKING, Optional

from capo_opensearchserverless._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_opensearchserverless.types.client_token
    import capo_opensearchserverless.types.config_description
    import capo_opensearchserverless.types.config_name
    import capo_opensearchserverless.types.create_iam_identity_center_config_options
    import capo_opensearchserverless.types.create_security_config_request
    import capo_opensearchserverless.types.create_security_config_response
    import capo_opensearchserverless.types.delete_security_config_request
    import capo_opensearchserverless.types.delete_security_config_response
    import capo_opensearchserverless.types.get_security_config_request
    import capo_opensearchserverless.types.get_security_config_response
    import capo_opensearchserverless.types.iam_federation_config_options
    import capo_opensearchserverless.types.list_security_configs_request
    import capo_opensearchserverless.types.list_security_configs_response
    import capo_opensearchserverless.types.policy_version
    import capo_opensearchserverless.types.saml_config_options
    import capo_opensearchserverless.types.security_config_id
    import capo_opensearchserverless.types.security_config_type
    import capo_opensearchserverless.types.update_iam_identity_center_config_options
    import capo_opensearchserverless.types.update_security_config_request
    import capo_opensearchserverless.types.update_security_config_response
    from capo_opensearchserverless._services.async_open_search_serverless import (
        AsyncOpenSearchServerlessClient,
        AsyncOpenSearchServerlessClientConfig,
    )
    from capo_opensearchserverless._services.open_search_serverless import (
        OpenSearchServerlessClient,
        OpenSearchServerlessClientConfig,
    )


class SecurityConfig:
    def __init__(self, service: OpenSearchServerlessClient) -> None:
        self._service = service

    def create(
        self,
        type: "capo_opensearchserverless.types.security_config_type.SecurityConfigType",
        name: "capo_opensearchserverless.types.config_name.ConfigName",
        *,
        config_overrides: Optional[OpenSearchServerlessClientConfig] = None,
        description: Optional[
            "capo_opensearchserverless.types.config_description.ConfigDescription"
        ] = None,
        saml_options: Optional[
            "capo_opensearchserverless.types.saml_config_options.SamlConfigOptions"
        ] = None,
        iam_identity_center_options: Optional[
            "capo_opensearchserverless.types.create_iam_identity_center_config_options.CreateIamIdentityCenterConfigOptions"
        ] = None,
        iam_federation_options: Optional[
            "capo_opensearchserverless.types.iam_federation_config_options.IamFederationConfigOptions"
        ] = None,
        client_token: Optional[
            "capo_opensearchserverless.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_opensearchserverless.types.create_security_config_response.CreateSecurityConfigResponse":
        """<p>Specifies a security configuration for OpenSearch Serverless. For more information, see <a href="https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-saml.html">SAML authentication for Amazon OpenSearch Serverless</a>.</p>

        Args:
            type: <p>The type of security configuration.</p>
            name: <p>The name of the security configuration.</p>
            description: <p>A description of the security configuration.</p>
            saml_options: <p>Describes SAML options in the form of a key-value map. This field is required if you specify <code>SAML</code> for the <code>type</code> parameter.</p>
            iam_identity_center_options: <p>Describes IAM Identity Center options in the form of a key-value map. This field is required if you specify <code>iamidentitycenter</code> for the <code>type</code> parameter.</p>
            iam_federation_options: <p>Describes IAM federation options in the form of a key-value map. This field is required if you specify <code>iamFederation</code> for the <code>type</code> parameter.</p>
            client_token: <p>Unique, case-sensitive identifier to ensure idempotency of the request.</p>

        Raises:
            capo_opensearchserverless.errors.conflict_exception.ConflictException: <p>When creating a resource, thrown when a resource with the same name already exists or is being created. When deleting a resource, thrown when the resource is not in the ACTIVE, FAILED, or UPDATE_FAILED state.</p>
            capo_opensearchserverless.errors.internal_server_exception.InternalServerException: <p>Thrown when an error internal to the service occurs while processing a request.</p>
            capo_opensearchserverless.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Thrown when you attempt to create more resources than the service allows based on service quotas.</p>
            capo_opensearchserverless.errors.validation_exception.ValidationException: <p>Thrown when the HTTP request contains invalid input or is missing required input.</p>
            capo_opensearchserverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_opensearchserverless.types.create_security_config_request.CreateSecurityConfigRequest]",
        ) -> OperationResponse[
            "capo_opensearchserverless.types.create_security_config_response.CreateSecurityConfigResponse"
        ]:
            import capo_opensearchserverless._operations.open_search_serverless.create_security_config

            output, http_response = (
                capo_opensearchserverless._operations.open_search_serverless.create_security_config.create_security_config(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_opensearchserverless.types.create_security_config_request.CreateSecurityConfigRequest = {
            "type": type,
            "name": name,
        }
        if description is not None:
            input_["description"] = description
        if saml_options is not None:
            input_["saml_options"] = saml_options
        if iam_identity_center_options is not None:
            input_["iam_identity_center_options"] = iam_identity_center_options
        if iam_federation_options is not None:
            input_["iam_federation_options"] = iam_federation_options
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
        id: "capo_opensearchserverless.types.security_config_id.SecurityConfigId",
        *,
        config_overrides: Optional[OpenSearchServerlessClientConfig] = None,
    ) -> "capo_opensearchserverless.types.get_security_config_response.GetSecurityConfigResponse":
        """<p>Returns information about an OpenSearch Serverless security configuration. For more information, see <a href="https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-saml.html">SAML authentication for Amazon OpenSearch Serverless</a>.</p>

        Args:
            id: <p>The unique identifier of the security configuration.</p>

        Raises:
            capo_opensearchserverless.errors.internal_server_exception.InternalServerException: <p>Thrown when an error internal to the service occurs while processing a request.</p>
            capo_opensearchserverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>Thrown when accessing or deleting a resource that does not exist.</p>
            capo_opensearchserverless.errors.validation_exception.ValidationException: <p>Thrown when the HTTP request contains invalid input or is missing required input.</p>
            capo_opensearchserverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_opensearchserverless.types.get_security_config_request.GetSecurityConfigRequest]",
        ) -> OperationResponse[
            "capo_opensearchserverless.types.get_security_config_response.GetSecurityConfigResponse"
        ]:
            import capo_opensearchserverless._operations.open_search_serverless.get_security_config

            output, http_response = (
                capo_opensearchserverless._operations.open_search_serverless.get_security_config.get_security_config(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_opensearchserverless.types.get_security_config_request.GetSecurityConfigRequest = {
            "id": id
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
        id: "capo_opensearchserverless.types.security_config_id.SecurityConfigId",
        config_version: "capo_opensearchserverless.types.policy_version.PolicyVersion",
        *,
        config_overrides: Optional[OpenSearchServerlessClientConfig] = None,
        description: Optional[
            "capo_opensearchserverless.types.config_description.ConfigDescription"
        ] = None,
        saml_options: Optional[
            "capo_opensearchserverless.types.saml_config_options.SamlConfigOptions"
        ] = None,
        iam_identity_center_options_updates: Optional[
            "capo_opensearchserverless.types.update_iam_identity_center_config_options.UpdateIamIdentityCenterConfigOptions"
        ] = None,
        iam_federation_options: Optional[
            "capo_opensearchserverless.types.iam_federation_config_options.IamFederationConfigOptions"
        ] = None,
        client_token: Optional[
            "capo_opensearchserverless.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_opensearchserverless.types.update_security_config_response.UpdateSecurityConfigResponse":
        """<p>Updates a security configuration for OpenSearch Serverless. For more information, see <a href="https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-saml.html">SAML authentication for Amazon OpenSearch Serverless</a>.</p>

        Args:
            id: <p>The security configuration identifier. For SAML the ID will be <code>saml/&lt;accountId&gt;/&lt;idpProviderName&gt;</code>. For example, <code>saml/123456789123/OKTADev</code>.</p>
            config_version: <p>The version of the security configuration to be updated. You can find the most recent version of a security configuration using the <code>GetSecurityPolicy</code> command.</p>
            description: <p>A description of the security configuration.</p>
            saml_options: <p>SAML options in in the form of a key-value map.</p>
            iam_identity_center_options_updates: <p>Describes IAM Identity Center options in the form of a key-value map.</p>
            iam_federation_options: <p>Describes IAM federation options in the form of a key-value map for updating an existing security configuration. Use this field to modify IAM federation settings for the security configuration.</p>
            client_token: <p>Unique, case-sensitive identifier to ensure idempotency of the request.</p>

        Raises:
            capo_opensearchserverless.errors.conflict_exception.ConflictException: <p>When creating a resource, thrown when a resource with the same name already exists or is being created. When deleting a resource, thrown when the resource is not in the ACTIVE, FAILED, or UPDATE_FAILED state.</p>
            capo_opensearchserverless.errors.internal_server_exception.InternalServerException: <p>Thrown when an error internal to the service occurs while processing a request.</p>
            capo_opensearchserverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>Thrown when accessing or deleting a resource that does not exist.</p>
            capo_opensearchserverless.errors.validation_exception.ValidationException: <p>Thrown when the HTTP request contains invalid input or is missing required input.</p>
            capo_opensearchserverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_opensearchserverless.types.update_security_config_request.UpdateSecurityConfigRequest]",
        ) -> OperationResponse[
            "capo_opensearchserverless.types.update_security_config_response.UpdateSecurityConfigResponse"
        ]:
            import capo_opensearchserverless._operations.open_search_serverless.update_security_config

            output, http_response = (
                capo_opensearchserverless._operations.open_search_serverless.update_security_config.update_security_config(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_opensearchserverless.types.update_security_config_request.UpdateSecurityConfigRequest = {
            "id": id,
            "config_version": config_version,
        }
        if description is not None:
            input_["description"] = description
        if saml_options is not None:
            input_["saml_options"] = saml_options
        if iam_identity_center_options_updates is not None:
            input_["iam_identity_center_options_updates"] = (
                iam_identity_center_options_updates
            )
        if iam_federation_options is not None:
            input_["iam_federation_options"] = iam_federation_options
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

    def delete(
        self,
        id: "capo_opensearchserverless.types.security_config_id.SecurityConfigId",
        *,
        config_overrides: Optional[OpenSearchServerlessClientConfig] = None,
        client_token: Optional[
            "capo_opensearchserverless.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_opensearchserverless.types.delete_security_config_response.DeleteSecurityConfigResponse":
        """<p>Deletes a security configuration for OpenSearch Serverless. For more information, see <a href="https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-saml.html">SAML authentication for Amazon OpenSearch Serverless</a>.</p>

        Args:
            id: <p>The security configuration identifier. For SAML the ID will be <code>saml/&lt;accountId&gt;/&lt;idpProviderName&gt;</code>. For example, <code>saml/123456789123/OKTADev</code>.</p>
            client_token: <p>Unique, case-sensitive identifier to ensure idempotency of the request.</p>

        Raises:
            capo_opensearchserverless.errors.conflict_exception.ConflictException: <p>When creating a resource, thrown when a resource with the same name already exists or is being created. When deleting a resource, thrown when the resource is not in the ACTIVE, FAILED, or UPDATE_FAILED state.</p>
            capo_opensearchserverless.errors.internal_server_exception.InternalServerException: <p>Thrown when an error internal to the service occurs while processing a request.</p>
            capo_opensearchserverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>Thrown when accessing or deleting a resource that does not exist.</p>
            capo_opensearchserverless.errors.validation_exception.ValidationException: <p>Thrown when the HTTP request contains invalid input or is missing required input.</p>
            capo_opensearchserverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_opensearchserverless.types.delete_security_config_request.DeleteSecurityConfigRequest]",
        ) -> OperationResponse[
            "capo_opensearchserverless.types.delete_security_config_response.DeleteSecurityConfigResponse"
        ]:
            import capo_opensearchserverless._operations.open_search_serverless.delete_security_config

            output, http_response = (
                capo_opensearchserverless._operations.open_search_serverless.delete_security_config.delete_security_config(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_opensearchserverless.types.delete_security_config_request.DeleteSecurityConfigRequest = {
            "id": id
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

    def list(
        self,
        type: "capo_opensearchserverless.types.security_config_type.SecurityConfigType",
        *,
        config_overrides: Optional[OpenSearchServerlessClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
    ) -> "capo_opensearchserverless.types.list_security_configs_response.ListSecurityConfigsResponse":
        """<p>Returns information about configured OpenSearch Serverless security configurations. For more information, see <a href="https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-saml.html">SAML authentication for Amazon OpenSearch Serverless</a>.</p>

        Args:
            type: <p>The type of security configuration.</p>
            next_token: <p>If your initial <code>ListSecurityConfigs</code> operation returns a <code>nextToken</code>, you can include the returned <code>nextToken</code> in subsequent <code>ListSecurityConfigs</code> operations, which returns results in the next page.</p>
            max_results: <p>An optional parameter that specifies the maximum number of results to return. You can use <code>nextToken</code> to get the next page of results. The default is 20.</p>

        Raises:
            capo_opensearchserverless.errors.internal_server_exception.InternalServerException: <p>Thrown when an error internal to the service occurs while processing a request.</p>
            capo_opensearchserverless.errors.validation_exception.ValidationException: <p>Thrown when the HTTP request contains invalid input or is missing required input.</p>
            capo_opensearchserverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_opensearchserverless.types.list_security_configs_request.ListSecurityConfigsRequest]",
        ) -> OperationResponse[
            "capo_opensearchserverless.types.list_security_configs_response.ListSecurityConfigsResponse"
        ]:
            import capo_opensearchserverless._operations.open_search_serverless.list_security_configs

            output, http_response = (
                capo_opensearchserverless._operations.open_search_serverless.list_security_configs.list_security_configs(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_opensearchserverless.types.list_security_configs_request.ListSecurityConfigsRequest = {
            "type": type
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


class AsyncSecurityConfig:
    def __init__(self, service: AsyncOpenSearchServerlessClient) -> None:
        self._service = service

    async def create(
        self,
        type: "capo_opensearchserverless.types.security_config_type.SecurityConfigType",
        name: "capo_opensearchserverless.types.config_name.ConfigName",
        *,
        config_overrides: Optional[AsyncOpenSearchServerlessClientConfig] = None,
        description: Optional[
            "capo_opensearchserverless.types.config_description.ConfigDescription"
        ] = None,
        saml_options: Optional[
            "capo_opensearchserverless.types.saml_config_options.SamlConfigOptions"
        ] = None,
        iam_identity_center_options: Optional[
            "capo_opensearchserverless.types.create_iam_identity_center_config_options.CreateIamIdentityCenterConfigOptions"
        ] = None,
        iam_federation_options: Optional[
            "capo_opensearchserverless.types.iam_federation_config_options.IamFederationConfigOptions"
        ] = None,
        client_token: Optional[
            "capo_opensearchserverless.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_opensearchserverless.types.create_security_config_response.CreateSecurityConfigResponse":
        """<p>Specifies a security configuration for OpenSearch Serverless. For more information, see <a href="https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-saml.html">SAML authentication for Amazon OpenSearch Serverless</a>.</p>

        Args:
            type: <p>The type of security configuration.</p>
            name: <p>The name of the security configuration.</p>
            description: <p>A description of the security configuration.</p>
            saml_options: <p>Describes SAML options in the form of a key-value map. This field is required if you specify <code>SAML</code> for the <code>type</code> parameter.</p>
            iam_identity_center_options: <p>Describes IAM Identity Center options in the form of a key-value map. This field is required if you specify <code>iamidentitycenter</code> for the <code>type</code> parameter.</p>
            iam_federation_options: <p>Describes IAM federation options in the form of a key-value map. This field is required if you specify <code>iamFederation</code> for the <code>type</code> parameter.</p>
            client_token: <p>Unique, case-sensitive identifier to ensure idempotency of the request.</p>

        Raises:
            capo_opensearchserverless.errors.conflict_exception.ConflictException: <p>When creating a resource, thrown when a resource with the same name already exists or is being created. When deleting a resource, thrown when the resource is not in the ACTIVE, FAILED, or UPDATE_FAILED state.</p>
            capo_opensearchserverless.errors.internal_server_exception.InternalServerException: <p>Thrown when an error internal to the service occurs while processing a request.</p>
            capo_opensearchserverless.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Thrown when you attempt to create more resources than the service allows based on service quotas.</p>
            capo_opensearchserverless.errors.validation_exception.ValidationException: <p>Thrown when the HTTP request contains invalid input or is missing required input.</p>
            capo_opensearchserverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_opensearchserverless.types.create_security_config_request.CreateSecurityConfigRequest]",
        ) -> AsyncOperationResponse[
            "capo_opensearchserverless.types.create_security_config_response.CreateSecurityConfigResponse"
        ]:
            import capo_opensearchserverless._operations.open_search_serverless.create_security_config

            (
                output,
                http_response,
            ) = await capo_opensearchserverless._operations.open_search_serverless.create_security_config.async_create_security_config(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_opensearchserverless.types.create_security_config_request.CreateSecurityConfigRequest = {
            "type": type,
            "name": name,
        }
        if description is not None:
            input_["description"] = description
        if saml_options is not None:
            input_["saml_options"] = saml_options
        if iam_identity_center_options is not None:
            input_["iam_identity_center_options"] = iam_identity_center_options
        if iam_federation_options is not None:
            input_["iam_federation_options"] = iam_federation_options
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
        id: "capo_opensearchserverless.types.security_config_id.SecurityConfigId",
        *,
        config_overrides: Optional[AsyncOpenSearchServerlessClientConfig] = None,
    ) -> "capo_opensearchserverless.types.get_security_config_response.GetSecurityConfigResponse":
        """<p>Returns information about an OpenSearch Serverless security configuration. For more information, see <a href="https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-saml.html">SAML authentication for Amazon OpenSearch Serverless</a>.</p>

        Args:
            id: <p>The unique identifier of the security configuration.</p>

        Raises:
            capo_opensearchserverless.errors.internal_server_exception.InternalServerException: <p>Thrown when an error internal to the service occurs while processing a request.</p>
            capo_opensearchserverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>Thrown when accessing or deleting a resource that does not exist.</p>
            capo_opensearchserverless.errors.validation_exception.ValidationException: <p>Thrown when the HTTP request contains invalid input or is missing required input.</p>
            capo_opensearchserverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_opensearchserverless.types.get_security_config_request.GetSecurityConfigRequest]",
        ) -> AsyncOperationResponse[
            "capo_opensearchserverless.types.get_security_config_response.GetSecurityConfigResponse"
        ]:
            import capo_opensearchserverless._operations.open_search_serverless.get_security_config

            (
                output,
                http_response,
            ) = await capo_opensearchserverless._operations.open_search_serverless.get_security_config.async_get_security_config(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_opensearchserverless.types.get_security_config_request.GetSecurityConfigRequest = {
            "id": id
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
        id: "capo_opensearchserverless.types.security_config_id.SecurityConfigId",
        config_version: "capo_opensearchserverless.types.policy_version.PolicyVersion",
        *,
        config_overrides: Optional[AsyncOpenSearchServerlessClientConfig] = None,
        description: Optional[
            "capo_opensearchserverless.types.config_description.ConfigDescription"
        ] = None,
        saml_options: Optional[
            "capo_opensearchserverless.types.saml_config_options.SamlConfigOptions"
        ] = None,
        iam_identity_center_options_updates: Optional[
            "capo_opensearchserverless.types.update_iam_identity_center_config_options.UpdateIamIdentityCenterConfigOptions"
        ] = None,
        iam_federation_options: Optional[
            "capo_opensearchserverless.types.iam_federation_config_options.IamFederationConfigOptions"
        ] = None,
        client_token: Optional[
            "capo_opensearchserverless.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_opensearchserverless.types.update_security_config_response.UpdateSecurityConfigResponse":
        """<p>Updates a security configuration for OpenSearch Serverless. For more information, see <a href="https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-saml.html">SAML authentication for Amazon OpenSearch Serverless</a>.</p>

        Args:
            id: <p>The security configuration identifier. For SAML the ID will be <code>saml/&lt;accountId&gt;/&lt;idpProviderName&gt;</code>. For example, <code>saml/123456789123/OKTADev</code>.</p>
            config_version: <p>The version of the security configuration to be updated. You can find the most recent version of a security configuration using the <code>GetSecurityPolicy</code> command.</p>
            description: <p>A description of the security configuration.</p>
            saml_options: <p>SAML options in in the form of a key-value map.</p>
            iam_identity_center_options_updates: <p>Describes IAM Identity Center options in the form of a key-value map.</p>
            iam_federation_options: <p>Describes IAM federation options in the form of a key-value map for updating an existing security configuration. Use this field to modify IAM federation settings for the security configuration.</p>
            client_token: <p>Unique, case-sensitive identifier to ensure idempotency of the request.</p>

        Raises:
            capo_opensearchserverless.errors.conflict_exception.ConflictException: <p>When creating a resource, thrown when a resource with the same name already exists or is being created. When deleting a resource, thrown when the resource is not in the ACTIVE, FAILED, or UPDATE_FAILED state.</p>
            capo_opensearchserverless.errors.internal_server_exception.InternalServerException: <p>Thrown when an error internal to the service occurs while processing a request.</p>
            capo_opensearchserverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>Thrown when accessing or deleting a resource that does not exist.</p>
            capo_opensearchserverless.errors.validation_exception.ValidationException: <p>Thrown when the HTTP request contains invalid input or is missing required input.</p>
            capo_opensearchserverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_opensearchserverless.types.update_security_config_request.UpdateSecurityConfigRequest]",
        ) -> AsyncOperationResponse[
            "capo_opensearchserverless.types.update_security_config_response.UpdateSecurityConfigResponse"
        ]:
            import capo_opensearchserverless._operations.open_search_serverless.update_security_config

            (
                output,
                http_response,
            ) = await capo_opensearchserverless._operations.open_search_serverless.update_security_config.async_update_security_config(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_opensearchserverless.types.update_security_config_request.UpdateSecurityConfigRequest = {
            "id": id,
            "config_version": config_version,
        }
        if description is not None:
            input_["description"] = description
        if saml_options is not None:
            input_["saml_options"] = saml_options
        if iam_identity_center_options_updates is not None:
            input_["iam_identity_center_options_updates"] = (
                iam_identity_center_options_updates
            )
        if iam_federation_options is not None:
            input_["iam_federation_options"] = iam_federation_options
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

    async def delete(
        self,
        id: "capo_opensearchserverless.types.security_config_id.SecurityConfigId",
        *,
        config_overrides: Optional[AsyncOpenSearchServerlessClientConfig] = None,
        client_token: Optional[
            "capo_opensearchserverless.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_opensearchserverless.types.delete_security_config_response.DeleteSecurityConfigResponse":
        """<p>Deletes a security configuration for OpenSearch Serverless. For more information, see <a href="https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-saml.html">SAML authentication for Amazon OpenSearch Serverless</a>.</p>

        Args:
            id: <p>The security configuration identifier. For SAML the ID will be <code>saml/&lt;accountId&gt;/&lt;idpProviderName&gt;</code>. For example, <code>saml/123456789123/OKTADev</code>.</p>
            client_token: <p>Unique, case-sensitive identifier to ensure idempotency of the request.</p>

        Raises:
            capo_opensearchserverless.errors.conflict_exception.ConflictException: <p>When creating a resource, thrown when a resource with the same name already exists or is being created. When deleting a resource, thrown when the resource is not in the ACTIVE, FAILED, or UPDATE_FAILED state.</p>
            capo_opensearchserverless.errors.internal_server_exception.InternalServerException: <p>Thrown when an error internal to the service occurs while processing a request.</p>
            capo_opensearchserverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>Thrown when accessing or deleting a resource that does not exist.</p>
            capo_opensearchserverless.errors.validation_exception.ValidationException: <p>Thrown when the HTTP request contains invalid input or is missing required input.</p>
            capo_opensearchserverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_opensearchserverless.types.delete_security_config_request.DeleteSecurityConfigRequest]",
        ) -> AsyncOperationResponse[
            "capo_opensearchserverless.types.delete_security_config_response.DeleteSecurityConfigResponse"
        ]:
            import capo_opensearchserverless._operations.open_search_serverless.delete_security_config

            (
                output,
                http_response,
            ) = await capo_opensearchserverless._operations.open_search_serverless.delete_security_config.async_delete_security_config(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_opensearchserverless.types.delete_security_config_request.DeleteSecurityConfigRequest = {
            "id": id
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

    async def list(
        self,
        type: "capo_opensearchserverless.types.security_config_type.SecurityConfigType",
        *,
        config_overrides: Optional[AsyncOpenSearchServerlessClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
    ) -> "capo_opensearchserverless.types.list_security_configs_response.ListSecurityConfigsResponse":
        """<p>Returns information about configured OpenSearch Serverless security configurations. For more information, see <a href="https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-saml.html">SAML authentication for Amazon OpenSearch Serverless</a>.</p>

        Args:
            type: <p>The type of security configuration.</p>
            next_token: <p>If your initial <code>ListSecurityConfigs</code> operation returns a <code>nextToken</code>, you can include the returned <code>nextToken</code> in subsequent <code>ListSecurityConfigs</code> operations, which returns results in the next page.</p>
            max_results: <p>An optional parameter that specifies the maximum number of results to return. You can use <code>nextToken</code> to get the next page of results. The default is 20.</p>

        Raises:
            capo_opensearchserverless.errors.internal_server_exception.InternalServerException: <p>Thrown when an error internal to the service occurs while processing a request.</p>
            capo_opensearchserverless.errors.validation_exception.ValidationException: <p>Thrown when the HTTP request contains invalid input or is missing required input.</p>
            capo_opensearchserverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_opensearchserverless.types.list_security_configs_request.ListSecurityConfigsRequest]",
        ) -> AsyncOperationResponse[
            "capo_opensearchserverless.types.list_security_configs_response.ListSecurityConfigsResponse"
        ]:
            import capo_opensearchserverless._operations.open_search_serverless.list_security_configs

            (
                output,
                http_response,
            ) = await capo_opensearchserverless._operations.open_search_serverless.list_security_configs.async_list_security_configs(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_opensearchserverless.types.list_security_configs_request.ListSecurityConfigsRequest = {
            "type": type
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
