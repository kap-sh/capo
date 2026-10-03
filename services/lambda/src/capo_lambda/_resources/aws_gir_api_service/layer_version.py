from __future__ import annotations

from typing import TYPE_CHECKING, Optional

import capo_lambda._auth._signers
import capo_lambda._auth._sigv4
from capo_lambda._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_lambda.types.add_layer_version_permission_request
    import capo_lambda.types.add_layer_version_permission_response
    import capo_lambda.types.architecture
    import capo_lambda.types.compatible_architectures
    import capo_lambda.types.compatible_runtimes
    import capo_lambda.types.delete_layer_version_request
    import capo_lambda.types.description
    import capo_lambda.types.get_layer_version_by_arn_request
    import capo_lambda.types.get_layer_version_policy_request
    import capo_lambda.types.get_layer_version_policy_response
    import capo_lambda.types.get_layer_version_request
    import capo_lambda.types.get_layer_version_response
    import capo_lambda.types.layer_name
    import capo_lambda.types.layer_permission_allowed_action
    import capo_lambda.types.layer_permission_allowed_principal
    import capo_lambda.types.layer_version_arn
    import capo_lambda.types.layer_version_content_input
    import capo_lambda.types.layer_version_number
    import capo_lambda.types.license_info
    import capo_lambda.types.list_layer_versions_request
    import capo_lambda.types.list_layer_versions_response
    import capo_lambda.types.max_layer_list_items
    import capo_lambda.types.organization_id
    import capo_lambda.types.publish_layer_version_request
    import capo_lambda.types.publish_layer_version_response
    import capo_lambda.types.remove_layer_version_permission_request
    import capo_lambda.types.runtime
    import capo_lambda.types.statement_id
    import capo_lambda.types.string
    from capo_lambda._services._lambda import LambdaClient, LambdaClientConfig
    from capo_lambda._services.async__lambda import (
        AsyncLambdaClient,
        AsyncLambdaClientConfig,
    )


class LayerVersion:
    def __init__(self, service: LambdaClient) -> None:
        self._service = service

    def list(
        self,
        layer_name: "capo_lambda.types.layer_name.LayerName",
        *,
        config_overrides: Optional[LambdaClientConfig] = None,
        compatible_architecture: Optional[
            "capo_lambda.types.architecture.Architecture"
        ] = None,
        compatible_runtime: Optional["capo_lambda.types.runtime.Runtime"] = None,
        marker: Optional["capo_lambda.types.string.String"] = None,
        max_items: Optional[
            "capo_lambda.types.max_layer_list_items.MaxLayerListItems"
        ] = None,
    ) -> "capo_lambda.types.list_layer_versions_response.ListLayerVersionsResponse":
        """<p>Lists the versions of an <a href="https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html">Lambda layer</a>. Versions that have been deleted aren't listed. Specify a <a href="https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtimes.html">runtime identifier</a> to list only versions that indicate that they're compatible with that runtime. Specify a compatible architecture to include only layer versions that are compatible with that architecture.</p>

        Args:
            compatible_architecture: <p>The compatible <a href="https://docs.aws.amazon.com/lambda/latest/dg/foundation-arch.html">instruction set architecture</a>.</p>
            compatible_runtime: <p>A runtime identifier.</p> <p>The following list includes deprecated runtimes. For more information, see <a href="https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtimes.html#runtime-deprecation-levels">Runtime use after deprecation</a>.</p> <p>For a list of all currently supported runtimes, see <a href="https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtimes.html#runtimes-supported">Supported runtimes</a>.</p>
            layer_name: <p>The name or Amazon Resource Name (ARN) of the layer.</p>
            marker: <p>A pagination token returned by a previous call.</p>
            max_items: <p>The maximum number of versions to return.</p>

        Raises:
            capo_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid.</p>
            capo_lambda.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request does not exist.</p>
            capo_lambda.errors.service_exception.ServiceException: <p>The Lambda service encountered an internal error.</p>
            capo_lambda.errors.too_many_requests_exception.TooManyRequestsException: <p>The request throughput limit was exceeded. For more information, see <a href="https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#api-requests">Lambda quotas</a>.</p>
            capo_lambda.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To list versions of a layer
            The following example displays information about the versions for the layer named blank-java-lib

            >>> client.list(layer_name='blank-java-lib')
        """

        def _handler(
            req: "OperationRequest[capo_lambda.types.list_layer_versions_request.ListLayerVersionsRequest]",
        ) -> OperationResponse[
            "capo_lambda.types.list_layer_versions_response.ListLayerVersionsResponse"
        ]:
            import capo_lambda._operations.aws_gir_api_service.list_layer_versions

            output, http_response = (
                capo_lambda._operations.aws_gir_api_service.list_layer_versions.list_layer_versions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_lambda.types.list_layer_versions_request.ListLayerVersionsRequest = {
            "layer_name": layer_name
        }
        if compatible_architecture is not None:
            input_["compatible_architecture"] = compatible_architecture
        if compatible_runtime is not None:
            input_["compatible_runtime"] = compatible_runtime
        if marker is not None:
            input_["marker"] = marker
        if max_items is not None:
            input_["max_items"] = max_items

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def add_layer_version_permission(
        self,
        layer_name: "capo_lambda.types.layer_name.LayerName",
        version_number: "capo_lambda.types.layer_version_number.LayerVersionNumber",
        statement_id: "capo_lambda.types.statement_id.StatementId",
        action: "capo_lambda.types.layer_permission_allowed_action.LayerPermissionAllowedAction",
        principal: "capo_lambda.types.layer_permission_allowed_principal.LayerPermissionAllowedPrincipal",
        *,
        config_overrides: Optional[LambdaClientConfig] = None,
        organization_id: Optional[
            "capo_lambda.types.organization_id.OrganizationId"
        ] = None,
        revision_id: Optional["capo_lambda.types.string.String"] = None,
    ) -> "capo_lambda.types.add_layer_version_permission_response.AddLayerVersionPermissionResponse":
        """<p>Adds permissions to the resource-based policy of a version of an <a href="https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html">Lambda layer</a>. Use this action to grant layer usage permission to other accounts. You can grant permission to a single account, all accounts in an organization, or all Amazon Web Services accounts. </p> <p>To revoke permission, call <a>RemoveLayerVersionPermission</a> with the statement ID that you specified when you added it.</p>

        Args:
            layer_name: <p>The name or Amazon Resource Name (ARN) of the layer.</p>
            version_number: <p>The version number.</p>
            statement_id: <p>An identifier that distinguishes the policy from others on the same layer version.</p>
            action: <p>The API action that grants access to the layer. For example, <code>lambda:GetLayerVersion</code>.</p>
            principal: <p>An account ID, or <code>*</code> to grant layer usage permission to all accounts in an organization, or all Amazon Web Services accounts (if <code>organizationId</code> is not specified). For the last case, make sure that you really do want all Amazon Web Services accounts to have usage permission to this layer. </p>
            organization_id: <p>With the principal set to <code>*</code>, grant permission to all accounts in the specified organization.</p>
            revision_id: <p>Only update the policy if the revision ID matches the ID specified. Use this option to avoid modifying a policy that has changed since you last read it.</p>

        Raises:
            capo_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid.</p>
            capo_lambda.errors.policy_length_exceeded_exception.PolicyLengthExceededException: <p>The permissions policy for the resource is too large. For more information, see <a href="https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html">Lambda quotas</a>.</p>
            capo_lambda.errors.precondition_failed_exception.PreconditionFailedException: <p>The RevisionId provided does not match the latest RevisionId for the Lambda function or alias.</p> <ul> <li> <p> <b>For AddPermission and RemovePermission API operations:</b> Call <code>GetPolicy</code> to retrieve the latest RevisionId for your resource.</p> </li> <li> <p> <b>For all other API operations:</b> Call <code>GetFunction</code> or <code>GetAlias</code> to retrieve the latest RevisionId for your resource.</p> </li> </ul>
            capo_lambda.errors.resource_conflict_exception.ResourceConflictException: <p>The resource already exists, or another operation is in progress.</p>
            capo_lambda.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request does not exist.</p>
            capo_lambda.errors.service_exception.ServiceException: <p>The Lambda service encountered an internal error.</p>
            capo_lambda.errors.too_many_requests_exception.TooManyRequestsException: <p>The request throughput limit was exceeded. For more information, see <a href="https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#api-requests">Lambda quotas</a>.</p>
            capo_lambda.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To add permissions to a layer version
            The following example grants permission for the account 223456789012 to use version 1 of a layer named my-layer.

            >>> client.add_layer_version_permission(action='lambda:GetLayerVersion', layer_name='my-layer', principal='223456789012', statement_id='xaccount', version_number=1)
        """

        def _handler(
            req: "OperationRequest[capo_lambda.types.add_layer_version_permission_request.AddLayerVersionPermissionRequest]",
        ) -> OperationResponse[
            "capo_lambda.types.add_layer_version_permission_response.AddLayerVersionPermissionResponse"
        ]:
            import capo_lambda._operations.aws_gir_api_service.add_layer_version_permission

            output, http_response = (
                capo_lambda._operations.aws_gir_api_service.add_layer_version_permission.add_layer_version_permission(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_lambda.types.add_layer_version_permission_request.AddLayerVersionPermissionRequest = {
            "layer_name": layer_name,
            "version_number": version_number,
            "statement_id": statement_id,
            "action": action,
            "principal": principal,
        }
        if organization_id is not None:
            input_["organization_id"] = organization_id
        if revision_id is not None:
            input_["revision_id"] = revision_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_layer_version(
        self,
        layer_name: "capo_lambda.types.layer_name.LayerName",
        version_number: "capo_lambda.types.layer_version_number.LayerVersionNumber",
        *,
        config_overrides: Optional[LambdaClientConfig] = None,
    ) -> None:
        """<p>Deletes a version of an <a href="https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html">Lambda layer</a>. Deleted versions can no longer be viewed or added to functions. To avoid breaking functions, a copy of the version remains in Lambda until no functions refer to it.</p>

        Args:
            layer_name: <p>The name or Amazon Resource Name (ARN) of the layer.</p>
            version_number: <p>The version number.</p>

        Raises:
            capo_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid.</p>
            capo_lambda.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request does not exist.</p>
            capo_lambda.errors.service_exception.ServiceException: <p>The Lambda service encountered an internal error.</p>
            capo_lambda.errors.too_many_requests_exception.TooManyRequestsException: <p>The request throughput limit was exceeded. For more information, see <a href="https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#api-requests">Lambda quotas</a>.</p>
            capo_lambda.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To delete a version of a Lambda layer
            The following example deletes version 2 of a layer named my-layer.

            >>> client.delete_layer_version(layer_name='my-layer', version_number=2)
        """

        def _handler(
            req: "OperationRequest[capo_lambda.types.delete_layer_version_request.DeleteLayerVersionRequest]",
        ) -> OperationResponse[None]:
            import capo_lambda._operations.aws_gir_api_service.delete_layer_version

            output, http_response = (
                capo_lambda._operations.aws_gir_api_service.delete_layer_version.delete_layer_version(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_lambda.types.delete_layer_version_request.DeleteLayerVersionRequest = {
            "layer_name": layer_name,
            "version_number": version_number,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_layer_version(
        self,
        layer_name: "capo_lambda.types.layer_name.LayerName",
        version_number: "capo_lambda.types.layer_version_number.LayerVersionNumber",
        *,
        config_overrides: Optional[LambdaClientConfig] = None,
    ) -> "capo_lambda.types.get_layer_version_response.GetLayerVersionResponse":
        """<p>Returns information about a version of an <a href="https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html">Lambda layer</a>, with a link to download the layer archive that's valid for 10 minutes.</p>

        Args:
            layer_name: <p>The name or Amazon Resource Name (ARN) of the layer.</p>
            version_number: <p>The version number.</p>

        Raises:
            capo_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid.</p>
            capo_lambda.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request does not exist.</p>
            capo_lambda.errors.service_exception.ServiceException: <p>The Lambda service encountered an internal error.</p>
            capo_lambda.errors.too_many_requests_exception.TooManyRequestsException: <p>The request throughput limit was exceeded. For more information, see <a href="https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#api-requests">Lambda quotas</a>.</p>
            capo_lambda.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To get information about a Lambda layer version
            The following example returns information for version 1 of a layer named my-layer.

            >>> client.get_layer_version(layer_name='my-layer', version_number=1)
        """

        def _handler(
            req: "OperationRequest[capo_lambda.types.get_layer_version_request.GetLayerVersionRequest]",
        ) -> OperationResponse[
            "capo_lambda.types.get_layer_version_response.GetLayerVersionResponse"
        ]:
            import capo_lambda._operations.aws_gir_api_service.get_layer_version

            output, http_response = (
                capo_lambda._operations.aws_gir_api_service.get_layer_version.get_layer_version(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_lambda.types.get_layer_version_request.GetLayerVersionRequest = {
            "layer_name": layer_name,
            "version_number": version_number,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_layer_version_by_arn(
        self,
        arn: "capo_lambda.types.layer_version_arn.LayerVersionArn",
        *,
        config_overrides: Optional[LambdaClientConfig] = None,
    ) -> "capo_lambda.types.get_layer_version_response.GetLayerVersionResponse":
        """<p>Returns information about a version of an <a href="https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html">Lambda layer</a>, with a link to download the layer archive that's valid for 10 minutes.</p>

        Args:
            arn: <p>The ARN of the layer version.</p>

        Raises:
            capo_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid.</p>
            capo_lambda.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request does not exist.</p>
            capo_lambda.errors.service_exception.ServiceException: <p>The Lambda service encountered an internal error.</p>
            capo_lambda.errors.too_many_requests_exception.TooManyRequestsException: <p>The request throughput limit was exceeded. For more information, see <a href="https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#api-requests">Lambda quotas</a>.</p>
            capo_lambda.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To get information about a Lambda layer version
            The following example returns information about the layer version with the specified Amazon Resource Name (ARN).

            >>> client.get_layer_version_by_arn(arn='arn:aws:lambda:ca-central-1:123456789012:layer:blank-python-lib:3')
        """

        def _handler(
            req: "OperationRequest[capo_lambda.types.get_layer_version_by_arn_request.GetLayerVersionByArnRequest]",
        ) -> OperationResponse[
            "capo_lambda.types.get_layer_version_response.GetLayerVersionResponse"
        ]:
            import capo_lambda._operations.aws_gir_api_service.get_layer_version_by_arn

            output, http_response = (
                capo_lambda._operations.aws_gir_api_service.get_layer_version_by_arn.get_layer_version_by_arn(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_lambda.types.get_layer_version_by_arn_request.GetLayerVersionByArnRequest = {
            "arn": arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_layer_version_policy(
        self,
        layer_name: "capo_lambda.types.layer_name.LayerName",
        version_number: "capo_lambda.types.layer_version_number.LayerVersionNumber",
        *,
        config_overrides: Optional[LambdaClientConfig] = None,
    ) -> "capo_lambda.types.get_layer_version_policy_response.GetLayerVersionPolicyResponse":
        """<p>Returns the permission policy for a version of an <a href="https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html">Lambda layer</a>. For more information, see <a>AddLayerVersionPermission</a>.</p>

        Args:
            layer_name: <p>The name or Amazon Resource Name (ARN) of the layer.</p>
            version_number: <p>The version number.</p>

        Raises:
            capo_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid.</p>
            capo_lambda.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request does not exist.</p>
            capo_lambda.errors.service_exception.ServiceException: <p>The Lambda service encountered an internal error.</p>
            capo_lambda.errors.too_many_requests_exception.TooManyRequestsException: <p>The request throughput limit was exceeded. For more information, see <a href="https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#api-requests">Lambda quotas</a>.</p>
            capo_lambda.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_lambda.types.get_layer_version_policy_request.GetLayerVersionPolicyRequest]",
        ) -> OperationResponse[
            "capo_lambda.types.get_layer_version_policy_response.GetLayerVersionPolicyResponse"
        ]:
            import capo_lambda._operations.aws_gir_api_service.get_layer_version_policy

            output, http_response = (
                capo_lambda._operations.aws_gir_api_service.get_layer_version_policy.get_layer_version_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_lambda.types.get_layer_version_policy_request.GetLayerVersionPolicyRequest = {
            "layer_name": layer_name,
            "version_number": version_number,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def publish_layer_version(
        self,
        layer_name: "capo_lambda.types.layer_name.LayerName",
        content: "capo_lambda.types.layer_version_content_input.LayerVersionContentInput",
        *,
        config_overrides: Optional[LambdaClientConfig] = None,
        description: Optional["capo_lambda.types.description.Description"] = None,
        compatible_architectures: Optional[
            "capo_lambda.types.compatible_architectures.CompatibleArchitectures"
        ] = None,
        compatible_runtimes: Optional[
            "capo_lambda.types.compatible_runtimes.CompatibleRuntimes"
        ] = None,
        license_info: Optional["capo_lambda.types.license_info.LicenseInfo"] = None,
    ) -> "capo_lambda.types.publish_layer_version_response.PublishLayerVersionResponse":
        """<p>Creates an <a href="https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html">Lambda layer</a> from a ZIP archive. Each time you call <code>PublishLayerVersion</code> with the same layer name, a new version is created.</p> <p>Add layers to your function with <a>CreateFunction</a> or <a>UpdateFunctionConfiguration</a>.</p>

        Args:
            layer_name: <p>The name or Amazon Resource Name (ARN) of the layer.</p>
            description: <p>The description of the version.</p>
            content: <p>The function layer archive.</p>
            compatible_architectures: <p>A list of compatible <a href="https://docs.aws.amazon.com/lambda/latest/dg/foundation-arch.html">instruction set architectures</a>.</p>
            compatible_runtimes: <p>A list of compatible <a href="https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtimes.html">function runtimes</a>. Used for filtering with <a>ListLayers</a> and <a>ListLayerVersions</a>.</p> <p>The following list includes deprecated runtimes. For more information, see <a href="https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtimes.html#runtime-support-policy">Runtime deprecation policy</a>.</p>
            license_info: <p>The layer's software license. It can be any of the following:</p> <ul> <li> <p>An <a href="https://spdx.org/licenses/">SPDX license identifier</a>. For example, <code>MIT</code>.</p> </li> <li> <p>The URL of a license hosted on the internet. For example, <code>https://opensource.org/licenses/MIT</code>.</p> </li> <li> <p>The full text of the license.</p> </li> </ul>

        Raises:
            capo_lambda.errors.code_storage_exceeded_exception.CodeStorageExceededException: <p>Your Amazon Web Services account has exceeded its maximum total code size. For more information, see <a href="https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html">Lambda quotas</a>.</p>
            capo_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid.</p>
            capo_lambda.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request does not exist.</p>
            capo_lambda.errors.service_exception.ServiceException: <p>The Lambda service encountered an internal error.</p>
            capo_lambda.errors.too_many_requests_exception.TooManyRequestsException: <p>The request throughput limit was exceeded. For more information, see <a href="https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#api-requests">Lambda quotas</a>.</p>
            capo_lambda.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To create a Lambda layer version
            The following example creates a new Python library layer version. The command retrieves the layer content a file named layer.zip in the specified S3 bucket.

            >>> client.publish_layer_version(compatible_runtimes=['python3.6', 'python3.7'], content={'S3Bucket': 'lambda-layers-us-west-2-123456789012', 'S3Key': 'layer.zip'}, description='My Python layer', layer_name='my-layer', license_info='MIT')
        """

        def _handler(
            req: "OperationRequest[capo_lambda.types.publish_layer_version_request.PublishLayerVersionRequest]",
        ) -> OperationResponse[
            "capo_lambda.types.publish_layer_version_response.PublishLayerVersionResponse"
        ]:
            import capo_lambda._operations.aws_gir_api_service.publish_layer_version

            output, http_response = (
                capo_lambda._operations.aws_gir_api_service.publish_layer_version.publish_layer_version(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_lambda.types.publish_layer_version_request.PublishLayerVersionRequest = {
            "layer_name": layer_name,
            "content": content,
        }
        if description is not None:
            input_["description"] = description
        if compatible_architectures is not None:
            input_["compatible_architectures"] = compatible_architectures
        if compatible_runtimes is not None:
            input_["compatible_runtimes"] = compatible_runtimes
        if license_info is not None:
            input_["license_info"] = license_info

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def remove_layer_version_permission(
        self,
        layer_name: "capo_lambda.types.layer_name.LayerName",
        version_number: "capo_lambda.types.layer_version_number.LayerVersionNumber",
        statement_id: "capo_lambda.types.statement_id.StatementId",
        *,
        config_overrides: Optional[LambdaClientConfig] = None,
        revision_id: Optional["capo_lambda.types.string.String"] = None,
    ) -> None:
        """<p>Removes a statement from the permissions policy for a version of an <a href="https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html">Lambda layer</a>. For more information, see <a>AddLayerVersionPermission</a>.</p>

        Args:
            layer_name: <p>The name or Amazon Resource Name (ARN) of the layer.</p>
            version_number: <p>The version number.</p>
            statement_id: <p>The identifier that was specified when the statement was added.</p>
            revision_id: <p>Only update the policy if the revision ID matches the ID specified. Use this option to avoid modifying a policy that has changed since you last read it.</p>

        Raises:
            capo_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid.</p>
            capo_lambda.errors.precondition_failed_exception.PreconditionFailedException: <p>The RevisionId provided does not match the latest RevisionId for the Lambda function or alias.</p> <ul> <li> <p> <b>For AddPermission and RemovePermission API operations:</b> Call <code>GetPolicy</code> to retrieve the latest RevisionId for your resource.</p> </li> <li> <p> <b>For all other API operations:</b> Call <code>GetFunction</code> or <code>GetAlias</code> to retrieve the latest RevisionId for your resource.</p> </li> </ul>
            capo_lambda.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request does not exist.</p>
            capo_lambda.errors.service_exception.ServiceException: <p>The Lambda service encountered an internal error.</p>
            capo_lambda.errors.too_many_requests_exception.TooManyRequestsException: <p>The request throughput limit was exceeded. For more information, see <a href="https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#api-requests">Lambda quotas</a>.</p>
            capo_lambda.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To delete layer-version permissions
            The following example deletes permission for an account to configure a layer version.

            >>> client.remove_layer_version_permission(layer_name='my-layer', statement_id='xaccount', version_number=1)
        """

        def _handler(
            req: "OperationRequest[capo_lambda.types.remove_layer_version_permission_request.RemoveLayerVersionPermissionRequest]",
        ) -> OperationResponse[None]:
            import capo_lambda._operations.aws_gir_api_service.remove_layer_version_permission

            output, http_response = (
                capo_lambda._operations.aws_gir_api_service.remove_layer_version_permission.remove_layer_version_permission(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_lambda.types.remove_layer_version_permission_request.RemoveLayerVersionPermissionRequest = {
            "layer_name": layer_name,
            "version_number": version_number,
            "statement_id": statement_id,
        }
        if revision_id is not None:
            input_["revision_id"] = revision_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncLayerVersion:
    def __init__(self, service: AsyncLambdaClient) -> None:
        self._service = service

    async def list(
        self,
        layer_name: "capo_lambda.types.layer_name.LayerName",
        *,
        config_overrides: Optional[AsyncLambdaClientConfig] = None,
        compatible_architecture: Optional[
            "capo_lambda.types.architecture.Architecture"
        ] = None,
        compatible_runtime: Optional["capo_lambda.types.runtime.Runtime"] = None,
        marker: Optional["capo_lambda.types.string.String"] = None,
        max_items: Optional[
            "capo_lambda.types.max_layer_list_items.MaxLayerListItems"
        ] = None,
    ) -> "capo_lambda.types.list_layer_versions_response.ListLayerVersionsResponse":
        """<p>Lists the versions of an <a href="https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html">Lambda layer</a>. Versions that have been deleted aren't listed. Specify a <a href="https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtimes.html">runtime identifier</a> to list only versions that indicate that they're compatible with that runtime. Specify a compatible architecture to include only layer versions that are compatible with that architecture.</p>

        Args:
            compatible_architecture: <p>The compatible <a href="https://docs.aws.amazon.com/lambda/latest/dg/foundation-arch.html">instruction set architecture</a>.</p>
            compatible_runtime: <p>A runtime identifier.</p> <p>The following list includes deprecated runtimes. For more information, see <a href="https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtimes.html#runtime-deprecation-levels">Runtime use after deprecation</a>.</p> <p>For a list of all currently supported runtimes, see <a href="https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtimes.html#runtimes-supported">Supported runtimes</a>.</p>
            layer_name: <p>The name or Amazon Resource Name (ARN) of the layer.</p>
            marker: <p>A pagination token returned by a previous call.</p>
            max_items: <p>The maximum number of versions to return.</p>

        Raises:
            capo_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid.</p>
            capo_lambda.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request does not exist.</p>
            capo_lambda.errors.service_exception.ServiceException: <p>The Lambda service encountered an internal error.</p>
            capo_lambda.errors.too_many_requests_exception.TooManyRequestsException: <p>The request throughput limit was exceeded. For more information, see <a href="https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#api-requests">Lambda quotas</a>.</p>
            capo_lambda.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To list versions of a layer
            The following example displays information about the versions for the layer named blank-java-lib

            >>> await client.list(layer_name='blank-java-lib')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lambda.types.list_layer_versions_request.ListLayerVersionsRequest]",
        ) -> AsyncOperationResponse[
            "capo_lambda.types.list_layer_versions_response.ListLayerVersionsResponse"
        ]:
            import capo_lambda._operations.aws_gir_api_service.list_layer_versions

            (
                output,
                http_response,
            ) = await capo_lambda._operations.aws_gir_api_service.list_layer_versions.async_list_layer_versions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_lambda.types.list_layer_versions_request.ListLayerVersionsRequest = {
            "layer_name": layer_name
        }
        if compatible_architecture is not None:
            input_["compatible_architecture"] = compatible_architecture
        if compatible_runtime is not None:
            input_["compatible_runtime"] = compatible_runtime
        if marker is not None:
            input_["marker"] = marker
        if max_items is not None:
            input_["max_items"] = max_items

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def add_layer_version_permission(
        self,
        layer_name: "capo_lambda.types.layer_name.LayerName",
        version_number: "capo_lambda.types.layer_version_number.LayerVersionNumber",
        statement_id: "capo_lambda.types.statement_id.StatementId",
        action: "capo_lambda.types.layer_permission_allowed_action.LayerPermissionAllowedAction",
        principal: "capo_lambda.types.layer_permission_allowed_principal.LayerPermissionAllowedPrincipal",
        *,
        config_overrides: Optional[AsyncLambdaClientConfig] = None,
        organization_id: Optional[
            "capo_lambda.types.organization_id.OrganizationId"
        ] = None,
        revision_id: Optional["capo_lambda.types.string.String"] = None,
    ) -> "capo_lambda.types.add_layer_version_permission_response.AddLayerVersionPermissionResponse":
        """<p>Adds permissions to the resource-based policy of a version of an <a href="https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html">Lambda layer</a>. Use this action to grant layer usage permission to other accounts. You can grant permission to a single account, all accounts in an organization, or all Amazon Web Services accounts. </p> <p>To revoke permission, call <a>RemoveLayerVersionPermission</a> with the statement ID that you specified when you added it.</p>

        Args:
            layer_name: <p>The name or Amazon Resource Name (ARN) of the layer.</p>
            version_number: <p>The version number.</p>
            statement_id: <p>An identifier that distinguishes the policy from others on the same layer version.</p>
            action: <p>The API action that grants access to the layer. For example, <code>lambda:GetLayerVersion</code>.</p>
            principal: <p>An account ID, or <code>*</code> to grant layer usage permission to all accounts in an organization, or all Amazon Web Services accounts (if <code>organizationId</code> is not specified). For the last case, make sure that you really do want all Amazon Web Services accounts to have usage permission to this layer. </p>
            organization_id: <p>With the principal set to <code>*</code>, grant permission to all accounts in the specified organization.</p>
            revision_id: <p>Only update the policy if the revision ID matches the ID specified. Use this option to avoid modifying a policy that has changed since you last read it.</p>

        Raises:
            capo_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid.</p>
            capo_lambda.errors.policy_length_exceeded_exception.PolicyLengthExceededException: <p>The permissions policy for the resource is too large. For more information, see <a href="https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html">Lambda quotas</a>.</p>
            capo_lambda.errors.precondition_failed_exception.PreconditionFailedException: <p>The RevisionId provided does not match the latest RevisionId for the Lambda function or alias.</p> <ul> <li> <p> <b>For AddPermission and RemovePermission API operations:</b> Call <code>GetPolicy</code> to retrieve the latest RevisionId for your resource.</p> </li> <li> <p> <b>For all other API operations:</b> Call <code>GetFunction</code> or <code>GetAlias</code> to retrieve the latest RevisionId for your resource.</p> </li> </ul>
            capo_lambda.errors.resource_conflict_exception.ResourceConflictException: <p>The resource already exists, or another operation is in progress.</p>
            capo_lambda.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request does not exist.</p>
            capo_lambda.errors.service_exception.ServiceException: <p>The Lambda service encountered an internal error.</p>
            capo_lambda.errors.too_many_requests_exception.TooManyRequestsException: <p>The request throughput limit was exceeded. For more information, see <a href="https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#api-requests">Lambda quotas</a>.</p>
            capo_lambda.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To add permissions to a layer version
            The following example grants permission for the account 223456789012 to use version 1 of a layer named my-layer.

            >>> await client.add_layer_version_permission(action='lambda:GetLayerVersion', layer_name='my-layer', principal='223456789012', statement_id='xaccount', version_number=1)
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lambda.types.add_layer_version_permission_request.AddLayerVersionPermissionRequest]",
        ) -> AsyncOperationResponse[
            "capo_lambda.types.add_layer_version_permission_response.AddLayerVersionPermissionResponse"
        ]:
            import capo_lambda._operations.aws_gir_api_service.add_layer_version_permission

            (
                output,
                http_response,
            ) = await capo_lambda._operations.aws_gir_api_service.add_layer_version_permission.async_add_layer_version_permission(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_lambda.types.add_layer_version_permission_request.AddLayerVersionPermissionRequest = {
            "layer_name": layer_name,
            "version_number": version_number,
            "statement_id": statement_id,
            "action": action,
            "principal": principal,
        }
        if organization_id is not None:
            input_["organization_id"] = organization_id
        if revision_id is not None:
            input_["revision_id"] = revision_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_layer_version(
        self,
        layer_name: "capo_lambda.types.layer_name.LayerName",
        version_number: "capo_lambda.types.layer_version_number.LayerVersionNumber",
        *,
        config_overrides: Optional[AsyncLambdaClientConfig] = None,
    ) -> None:
        """<p>Deletes a version of an <a href="https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html">Lambda layer</a>. Deleted versions can no longer be viewed or added to functions. To avoid breaking functions, a copy of the version remains in Lambda until no functions refer to it.</p>

        Args:
            layer_name: <p>The name or Amazon Resource Name (ARN) of the layer.</p>
            version_number: <p>The version number.</p>

        Raises:
            capo_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid.</p>
            capo_lambda.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request does not exist.</p>
            capo_lambda.errors.service_exception.ServiceException: <p>The Lambda service encountered an internal error.</p>
            capo_lambda.errors.too_many_requests_exception.TooManyRequestsException: <p>The request throughput limit was exceeded. For more information, see <a href="https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#api-requests">Lambda quotas</a>.</p>
            capo_lambda.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To delete a version of a Lambda layer
            The following example deletes version 2 of a layer named my-layer.

            >>> await client.delete_layer_version(layer_name='my-layer', version_number=2)
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lambda.types.delete_layer_version_request.DeleteLayerVersionRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_lambda._operations.aws_gir_api_service.delete_layer_version

            (
                output,
                http_response,
            ) = await capo_lambda._operations.aws_gir_api_service.delete_layer_version.async_delete_layer_version(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_lambda.types.delete_layer_version_request.DeleteLayerVersionRequest = {
            "layer_name": layer_name,
            "version_number": version_number,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_layer_version(
        self,
        layer_name: "capo_lambda.types.layer_name.LayerName",
        version_number: "capo_lambda.types.layer_version_number.LayerVersionNumber",
        *,
        config_overrides: Optional[AsyncLambdaClientConfig] = None,
    ) -> "capo_lambda.types.get_layer_version_response.GetLayerVersionResponse":
        """<p>Returns information about a version of an <a href="https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html">Lambda layer</a>, with a link to download the layer archive that's valid for 10 minutes.</p>

        Args:
            layer_name: <p>The name or Amazon Resource Name (ARN) of the layer.</p>
            version_number: <p>The version number.</p>

        Raises:
            capo_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid.</p>
            capo_lambda.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request does not exist.</p>
            capo_lambda.errors.service_exception.ServiceException: <p>The Lambda service encountered an internal error.</p>
            capo_lambda.errors.too_many_requests_exception.TooManyRequestsException: <p>The request throughput limit was exceeded. For more information, see <a href="https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#api-requests">Lambda quotas</a>.</p>
            capo_lambda.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To get information about a Lambda layer version
            The following example returns information for version 1 of a layer named my-layer.

            >>> await client.get_layer_version(layer_name='my-layer', version_number=1)
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lambda.types.get_layer_version_request.GetLayerVersionRequest]",
        ) -> AsyncOperationResponse[
            "capo_lambda.types.get_layer_version_response.GetLayerVersionResponse"
        ]:
            import capo_lambda._operations.aws_gir_api_service.get_layer_version

            (
                output,
                http_response,
            ) = await capo_lambda._operations.aws_gir_api_service.get_layer_version.async_get_layer_version(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_lambda.types.get_layer_version_request.GetLayerVersionRequest = {
            "layer_name": layer_name,
            "version_number": version_number,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_layer_version_by_arn(
        self,
        arn: "capo_lambda.types.layer_version_arn.LayerVersionArn",
        *,
        config_overrides: Optional[AsyncLambdaClientConfig] = None,
    ) -> "capo_lambda.types.get_layer_version_response.GetLayerVersionResponse":
        """<p>Returns information about a version of an <a href="https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html">Lambda layer</a>, with a link to download the layer archive that's valid for 10 minutes.</p>

        Args:
            arn: <p>The ARN of the layer version.</p>

        Raises:
            capo_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid.</p>
            capo_lambda.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request does not exist.</p>
            capo_lambda.errors.service_exception.ServiceException: <p>The Lambda service encountered an internal error.</p>
            capo_lambda.errors.too_many_requests_exception.TooManyRequestsException: <p>The request throughput limit was exceeded. For more information, see <a href="https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#api-requests">Lambda quotas</a>.</p>
            capo_lambda.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To get information about a Lambda layer version
            The following example returns information about the layer version with the specified Amazon Resource Name (ARN).

            >>> await client.get_layer_version_by_arn(arn='arn:aws:lambda:ca-central-1:123456789012:layer:blank-python-lib:3')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lambda.types.get_layer_version_by_arn_request.GetLayerVersionByArnRequest]",
        ) -> AsyncOperationResponse[
            "capo_lambda.types.get_layer_version_response.GetLayerVersionResponse"
        ]:
            import capo_lambda._operations.aws_gir_api_service.get_layer_version_by_arn

            (
                output,
                http_response,
            ) = await capo_lambda._operations.aws_gir_api_service.get_layer_version_by_arn.async_get_layer_version_by_arn(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_lambda.types.get_layer_version_by_arn_request.GetLayerVersionByArnRequest = {
            "arn": arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_layer_version_policy(
        self,
        layer_name: "capo_lambda.types.layer_name.LayerName",
        version_number: "capo_lambda.types.layer_version_number.LayerVersionNumber",
        *,
        config_overrides: Optional[AsyncLambdaClientConfig] = None,
    ) -> "capo_lambda.types.get_layer_version_policy_response.GetLayerVersionPolicyResponse":
        """<p>Returns the permission policy for a version of an <a href="https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html">Lambda layer</a>. For more information, see <a>AddLayerVersionPermission</a>.</p>

        Args:
            layer_name: <p>The name or Amazon Resource Name (ARN) of the layer.</p>
            version_number: <p>The version number.</p>

        Raises:
            capo_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid.</p>
            capo_lambda.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request does not exist.</p>
            capo_lambda.errors.service_exception.ServiceException: <p>The Lambda service encountered an internal error.</p>
            capo_lambda.errors.too_many_requests_exception.TooManyRequestsException: <p>The request throughput limit was exceeded. For more information, see <a href="https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#api-requests">Lambda quotas</a>.</p>
            capo_lambda.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lambda.types.get_layer_version_policy_request.GetLayerVersionPolicyRequest]",
        ) -> AsyncOperationResponse[
            "capo_lambda.types.get_layer_version_policy_response.GetLayerVersionPolicyResponse"
        ]:
            import capo_lambda._operations.aws_gir_api_service.get_layer_version_policy

            (
                output,
                http_response,
            ) = await capo_lambda._operations.aws_gir_api_service.get_layer_version_policy.async_get_layer_version_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_lambda.types.get_layer_version_policy_request.GetLayerVersionPolicyRequest = {
            "layer_name": layer_name,
            "version_number": version_number,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def publish_layer_version(
        self,
        layer_name: "capo_lambda.types.layer_name.LayerName",
        content: "capo_lambda.types.layer_version_content_input.LayerVersionContentInput",
        *,
        config_overrides: Optional[AsyncLambdaClientConfig] = None,
        description: Optional["capo_lambda.types.description.Description"] = None,
        compatible_architectures: Optional[
            "capo_lambda.types.compatible_architectures.CompatibleArchitectures"
        ] = None,
        compatible_runtimes: Optional[
            "capo_lambda.types.compatible_runtimes.CompatibleRuntimes"
        ] = None,
        license_info: Optional["capo_lambda.types.license_info.LicenseInfo"] = None,
    ) -> "capo_lambda.types.publish_layer_version_response.PublishLayerVersionResponse":
        """<p>Creates an <a href="https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html">Lambda layer</a> from a ZIP archive. Each time you call <code>PublishLayerVersion</code> with the same layer name, a new version is created.</p> <p>Add layers to your function with <a>CreateFunction</a> or <a>UpdateFunctionConfiguration</a>.</p>

        Args:
            layer_name: <p>The name or Amazon Resource Name (ARN) of the layer.</p>
            description: <p>The description of the version.</p>
            content: <p>The function layer archive.</p>
            compatible_architectures: <p>A list of compatible <a href="https://docs.aws.amazon.com/lambda/latest/dg/foundation-arch.html">instruction set architectures</a>.</p>
            compatible_runtimes: <p>A list of compatible <a href="https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtimes.html">function runtimes</a>. Used for filtering with <a>ListLayers</a> and <a>ListLayerVersions</a>.</p> <p>The following list includes deprecated runtimes. For more information, see <a href="https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtimes.html#runtime-support-policy">Runtime deprecation policy</a>.</p>
            license_info: <p>The layer's software license. It can be any of the following:</p> <ul> <li> <p>An <a href="https://spdx.org/licenses/">SPDX license identifier</a>. For example, <code>MIT</code>.</p> </li> <li> <p>The URL of a license hosted on the internet. For example, <code>https://opensource.org/licenses/MIT</code>.</p> </li> <li> <p>The full text of the license.</p> </li> </ul>

        Raises:
            capo_lambda.errors.code_storage_exceeded_exception.CodeStorageExceededException: <p>Your Amazon Web Services account has exceeded its maximum total code size. For more information, see <a href="https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html">Lambda quotas</a>.</p>
            capo_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid.</p>
            capo_lambda.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request does not exist.</p>
            capo_lambda.errors.service_exception.ServiceException: <p>The Lambda service encountered an internal error.</p>
            capo_lambda.errors.too_many_requests_exception.TooManyRequestsException: <p>The request throughput limit was exceeded. For more information, see <a href="https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#api-requests">Lambda quotas</a>.</p>
            capo_lambda.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To create a Lambda layer version
            The following example creates a new Python library layer version. The command retrieves the layer content a file named layer.zip in the specified S3 bucket.

            >>> await client.publish_layer_version(compatible_runtimes=['python3.6', 'python3.7'], content={'S3Bucket': 'lambda-layers-us-west-2-123456789012', 'S3Key': 'layer.zip'}, description='My Python layer', layer_name='my-layer', license_info='MIT')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lambda.types.publish_layer_version_request.PublishLayerVersionRequest]",
        ) -> AsyncOperationResponse[
            "capo_lambda.types.publish_layer_version_response.PublishLayerVersionResponse"
        ]:
            import capo_lambda._operations.aws_gir_api_service.publish_layer_version

            (
                output,
                http_response,
            ) = await capo_lambda._operations.aws_gir_api_service.publish_layer_version.async_publish_layer_version(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_lambda.types.publish_layer_version_request.PublishLayerVersionRequest = {
            "layer_name": layer_name,
            "content": content,
        }
        if description is not None:
            input_["description"] = description
        if compatible_architectures is not None:
            input_["compatible_architectures"] = compatible_architectures
        if compatible_runtimes is not None:
            input_["compatible_runtimes"] = compatible_runtimes
        if license_info is not None:
            input_["license_info"] = license_info

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def remove_layer_version_permission(
        self,
        layer_name: "capo_lambda.types.layer_name.LayerName",
        version_number: "capo_lambda.types.layer_version_number.LayerVersionNumber",
        statement_id: "capo_lambda.types.statement_id.StatementId",
        *,
        config_overrides: Optional[AsyncLambdaClientConfig] = None,
        revision_id: Optional["capo_lambda.types.string.String"] = None,
    ) -> None:
        """<p>Removes a statement from the permissions policy for a version of an <a href="https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html">Lambda layer</a>. For more information, see <a>AddLayerVersionPermission</a>.</p>

        Args:
            layer_name: <p>The name or Amazon Resource Name (ARN) of the layer.</p>
            version_number: <p>The version number.</p>
            statement_id: <p>The identifier that was specified when the statement was added.</p>
            revision_id: <p>Only update the policy if the revision ID matches the ID specified. Use this option to avoid modifying a policy that has changed since you last read it.</p>

        Raises:
            capo_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid.</p>
            capo_lambda.errors.precondition_failed_exception.PreconditionFailedException: <p>The RevisionId provided does not match the latest RevisionId for the Lambda function or alias.</p> <ul> <li> <p> <b>For AddPermission and RemovePermission API operations:</b> Call <code>GetPolicy</code> to retrieve the latest RevisionId for your resource.</p> </li> <li> <p> <b>For all other API operations:</b> Call <code>GetFunction</code> or <code>GetAlias</code> to retrieve the latest RevisionId for your resource.</p> </li> </ul>
            capo_lambda.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request does not exist.</p>
            capo_lambda.errors.service_exception.ServiceException: <p>The Lambda service encountered an internal error.</p>
            capo_lambda.errors.too_many_requests_exception.TooManyRequestsException: <p>The request throughput limit was exceeded. For more information, see <a href="https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#api-requests">Lambda quotas</a>.</p>
            capo_lambda.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To delete layer-version permissions
            The following example deletes permission for an account to configure a layer version.

            >>> await client.remove_layer_version_permission(layer_name='my-layer', statement_id='xaccount', version_number=1)
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lambda.types.remove_layer_version_permission_request.RemoveLayerVersionPermissionRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_lambda._operations.aws_gir_api_service.remove_layer_version_permission

            (
                output,
                http_response,
            ) = await capo_lambda._operations.aws_gir_api_service.remove_layer_version_permission.async_remove_layer_version_permission(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_lambda.types.remove_layer_version_permission_request.RemoveLayerVersionPermissionRequest = {
            "layer_name": layer_name,
            "version_number": version_number,
            "statement_id": statement_id,
        }
        if revision_id is not None:
            input_["revision_id"] = revision_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
