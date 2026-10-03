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
    import capo_lambda.types.action
    import capo_lambda.types.add_permission_request
    import capo_lambda.types.add_permission_response
    import capo_lambda.types.arn
    import capo_lambda.types.event_source_token
    import capo_lambda.types.function_url_auth_type
    import capo_lambda.types.invoked_via_function_url
    import capo_lambda.types.namespaced_function_name
    import capo_lambda.types.namespaced_statement_id
    import capo_lambda.types.numeric_latest_published_or_alias_qualifier
    import capo_lambda.types.principal
    import capo_lambda.types.principal_org_id
    import capo_lambda.types.remove_permission_request
    import capo_lambda.types.source_owner
    import capo_lambda.types.statement_id
    import capo_lambda.types.string
    from capo_lambda._services._lambda import LambdaClient, LambdaClientConfig
    from capo_lambda._services.async__lambda import (
        AsyncLambdaClient,
        AsyncLambdaClientConfig,
    )


class Permission:
    def __init__(self, service: LambdaClient) -> None:
        self._service = service

    def add_permission(
        self,
        function_name: "capo_lambda.types.namespaced_function_name.NamespacedFunctionName",
        statement_id: "capo_lambda.types.statement_id.StatementId",
        action: "capo_lambda.types.action.Action",
        principal: "capo_lambda.types.principal.Principal",
        *,
        config_overrides: Optional[LambdaClientConfig] = None,
        source_arn: Optional["capo_lambda.types.arn.Arn"] = None,
        function_url_auth_type: Optional[
            "capo_lambda.types.function_url_auth_type.FunctionUrlAuthType"
        ] = None,
        invoked_via_function_url: Optional[
            "capo_lambda.types.invoked_via_function_url.InvokedViaFunctionUrl"
        ] = None,
        source_account: Optional["capo_lambda.types.source_owner.SourceOwner"] = None,
        event_source_token: Optional[
            "capo_lambda.types.event_source_token.EventSourceToken"
        ] = None,
        qualifier: Optional[
            "capo_lambda.types.numeric_latest_published_or_alias_qualifier.NumericLatestPublishedOrAliasQualifier"
        ] = None,
        revision_id: Optional["capo_lambda.types.string.String"] = None,
        principal_org_id: Optional[
            "capo_lambda.types.principal_org_id.PrincipalOrgID"
        ] = None,
    ) -> "capo_lambda.types.add_permission_response.AddPermissionResponse":
        """<p>Grants a <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_principal.html#Principal_specifying">principal</a> permission to use a function. You can apply the policy at the function level, or specify a qualifier to restrict access to a single version or alias. If you use a qualifier, the invoker must use the full Amazon Resource Name (ARN) of that version or alias to invoke the function. Note: Lambda does not support adding policies to version $LATEST.</p> <p>To grant permission to another account, specify the account ID as the <code>Principal</code>. To grant permission to an organization defined in Organizations, specify the organization ID as the <code>PrincipalOrgID</code>. For Amazon Web Services services, the principal is a domain-style identifier that the service defines, such as <code>s3.amazonaws.com</code> or <code>sns.amazonaws.com</code>. For Amazon Web Services services, you can also specify the ARN of the associated resource as the <code>SourceArn</code>. If you grant permission to a service principal without specifying the source, other accounts could potentially configure resources in their account to invoke your Lambda function.</p> <p>This operation adds a statement to a resource-based permissions policy for the function. For more information about function policies, see <a href="https://docs.aws.amazon.com/lambda/latest/dg/access-control-resource-based.html">Using resource-based policies for Lambda</a>.</p>

        Args:
            function_name: <p>The name or ARN of the Lambda function, version, or alias.</p> <p class="title"> <b>Name formats</b> </p> <ul> <li> <p> <b>Function name</b> – <code>my-function</code> (name-only), <code>my-function:v1</code> (with alias).</p> </li> <li> <p> <b>Function ARN</b> – <code>arn:aws:lambda:us-west-2:123456789012:function:my-function</code>.</p> </li> <li> <p> <b>Partial ARN</b> – <code>123456789012:function:my-function</code>.</p> </li> </ul> <p>You can append a version number or alias to any of the formats. The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.</p>
            statement_id: <p>A statement identifier that differentiates the statement from others in the same policy.</p>
            action: <p>The action that the principal can use on the function. For example, <code>lambda:InvokeFunction</code> or <code>lambda:GetFunction</code>.</p>
            principal: <p>The Amazon Web Services service, Amazon Web Services account, IAM user, or IAM role that invokes the function. If you specify a service, use <code>SourceArn</code> or <code>SourceAccount</code> to limit who can invoke the function through that service.</p>
            source_arn: <p>For Amazon Web Services services, the ARN of the Amazon Web Services resource that invokes the function. For example, an Amazon S3 bucket or Amazon SNS topic.</p> <p>Note that Lambda configures the comparison using the <code>StringLike</code> operator.</p>
            function_url_auth_type: <p>The type of authentication that your function URL uses. Set to <code>AWS_IAM</code> if you want to restrict access to authenticated users only. Set to <code>NONE</code> if you want to bypass IAM authentication to create a public endpoint. For more information, see <a href="https://docs.aws.amazon.com/lambda/latest/dg/urls-auth.html">Control access to Lambda function URLs</a>.</p>
            invoked_via_function_url: <p>Indicates whether the permission applies when the function is invoked through a function URL. </p>
            source_account: <p>For Amazon Web Services service, the ID of the Amazon Web Services account that owns the resource. Use this together with <code>SourceArn</code> to ensure that the specified account owns the resource. It is possible for an Amazon S3 bucket to be deleted by its owner and recreated by another account.</p>
            event_source_token: <p>For Alexa Smart Home functions, a token that the invoker must supply.</p>
            qualifier: <p>Specify a version or alias to add permissions to a published version of the function.</p>
            revision_id: <p>Update the policy only if the revision ID matches the ID that's specified. Use this option to avoid modifying a policy that has changed since you last read it.</p>
            principal_org_id: <p>The identifier for your organization in Organizations. Use this to grant permissions to all the Amazon Web Services accounts under this organization.</p>

        Raises:
            capo_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid.</p>
            capo_lambda.errors.policy_length_exceeded_exception.PolicyLengthExceededException: <p>The permissions policy for the resource is too large. For more information, see <a href="https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html">Lambda quotas</a>.</p>
            capo_lambda.errors.precondition_failed_exception.PreconditionFailedException: <p>The RevisionId provided does not match the latest RevisionId for the Lambda function or alias.</p> <ul> <li> <p> <b>For AddPermission and RemovePermission API operations:</b> Call <code>GetPolicy</code> to retrieve the latest RevisionId for your resource.</p> </li> <li> <p> <b>For all other API operations:</b> Call <code>GetFunction</code> or <code>GetAlias</code> to retrieve the latest RevisionId for your resource.</p> </li> </ul>
            capo_lambda.errors.public_policy_exception.PublicPolicyException: <p>The resource-based policy you tried to add to the Lambda resource would grant public access to it, which isn't allowed.</p>
            capo_lambda.errors.resource_conflict_exception.ResourceConflictException: <p>The resource already exists, or another operation is in progress.</p>
            capo_lambda.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request does not exist.</p>
            capo_lambda.errors.service_exception.ServiceException: <p>The Lambda service encountered an internal error.</p>
            capo_lambda.errors.too_many_requests_exception.TooManyRequestsException: <p>The request throughput limit was exceeded. For more information, see <a href="https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#api-requests">Lambda quotas</a>.</p>
            capo_lambda.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To grant Amazon S3 permission to invoke a function
            The following example adds permission for Amazon S3 to invoke a Lambda function named my-function for notifications from a bucket named my-bucket-1xpuxmplzrlbh in account 123456789012.

            >>> client.add_permission(action='lambda:InvokeFunction', function_name='my-function', principal='s3.amazonaws.com', source_account='123456789012', source_arn='arn:aws:s3:::my-bucket-1xpuxmplzrlbh/*', statement_id='s3')
            To grant another account permission to invoke a function
            The following example adds permission for account 223456789012 invoke a Lambda function named my-function.

            >>> client.add_permission(action='lambda:InvokeFunction', function_name='my-function', principal='223456789012', statement_id='xaccount')
        """

        def _handler(
            req: "OperationRequest[capo_lambda.types.add_permission_request.AddPermissionRequest]",
        ) -> OperationResponse[
            "capo_lambda.types.add_permission_response.AddPermissionResponse"
        ]:
            import capo_lambda._operations.aws_gir_api_service.add_permission

            output, http_response = (
                capo_lambda._operations.aws_gir_api_service.add_permission.add_permission(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_lambda.types.add_permission_request.AddPermissionRequest = {
            "function_name": function_name,
            "statement_id": statement_id,
            "action": action,
            "principal": principal,
        }
        if source_arn is not None:
            input_["source_arn"] = source_arn
        if function_url_auth_type is not None:
            input_["function_url_auth_type"] = function_url_auth_type
        if invoked_via_function_url is not None:
            input_["invoked_via_function_url"] = invoked_via_function_url
        if source_account is not None:
            input_["source_account"] = source_account
        if event_source_token is not None:
            input_["event_source_token"] = event_source_token
        if qualifier is not None:
            input_["qualifier"] = qualifier
        if revision_id is not None:
            input_["revision_id"] = revision_id
        if principal_org_id is not None:
            input_["principal_org_id"] = principal_org_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def remove_permission(
        self,
        function_name: "capo_lambda.types.namespaced_function_name.NamespacedFunctionName",
        statement_id: "capo_lambda.types.namespaced_statement_id.NamespacedStatementId",
        *,
        config_overrides: Optional[LambdaClientConfig] = None,
        qualifier: Optional[
            "capo_lambda.types.numeric_latest_published_or_alias_qualifier.NumericLatestPublishedOrAliasQualifier"
        ] = None,
        revision_id: Optional["capo_lambda.types.string.String"] = None,
    ) -> None:
        """<p>Revokes function-use permission from an Amazon Web Services service or another Amazon Web Services account. You can get the ID of the statement from the output of <a>GetPolicy</a>.</p>

        Args:
            function_name: <p>The name or ARN of the Lambda function, version, or alias.</p> <p class="title"> <b>Name formats</b> </p> <ul> <li> <p> <b>Function name</b> – <code>my-function</code> (name-only), <code>my-function:v1</code> (with alias).</p> </li> <li> <p> <b>Function ARN</b> – <code>arn:aws:lambda:us-west-2:123456789012:function:my-function</code>.</p> </li> <li> <p> <b>Partial ARN</b> – <code>123456789012:function:my-function</code>.</p> </li> </ul> <p>You can append a version number or alias to any of the formats. The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.</p>
            statement_id: <p>Statement ID of the permission to remove.</p>
            qualifier: <p>Specify a version or alias to remove permissions from a published version of the function.</p>
            revision_id: <p>Update the policy only if the revision ID matches the ID that's specified. Use this option to avoid modifying a policy that has changed since you last read it.</p>

        Raises:
            capo_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid.</p>
            capo_lambda.errors.precondition_failed_exception.PreconditionFailedException: <p>The RevisionId provided does not match the latest RevisionId for the Lambda function or alias.</p> <ul> <li> <p> <b>For AddPermission and RemovePermission API operations:</b> Call <code>GetPolicy</code> to retrieve the latest RevisionId for your resource.</p> </li> <li> <p> <b>For all other API operations:</b> Call <code>GetFunction</code> or <code>GetAlias</code> to retrieve the latest RevisionId for your resource.</p> </li> </ul>
            capo_lambda.errors.public_policy_exception.PublicPolicyException: <p>The resource-based policy you tried to add to the Lambda resource would grant public access to it, which isn't allowed.</p>
            capo_lambda.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request does not exist.</p>
            capo_lambda.errors.service_exception.ServiceException: <p>The Lambda service encountered an internal error.</p>
            capo_lambda.errors.too_many_requests_exception.TooManyRequestsException: <p>The request throughput limit was exceeded. For more information, see <a href="https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#api-requests">Lambda quotas</a>.</p>
            capo_lambda.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To remove a Lambda function's permissions
            The following example removes a permissions statement named xaccount from the PROD alias of a function named my-function.

            >>> client.remove_permission(function_name='my-function', qualifier='PROD', statement_id='xaccount')
        """

        def _handler(
            req: "OperationRequest[capo_lambda.types.remove_permission_request.RemovePermissionRequest]",
        ) -> OperationResponse[None]:
            import capo_lambda._operations.aws_gir_api_service.remove_permission

            output, http_response = (
                capo_lambda._operations.aws_gir_api_service.remove_permission.remove_permission(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_lambda.types.remove_permission_request.RemovePermissionRequest = {
            "function_name": function_name,
            "statement_id": statement_id,
        }
        if qualifier is not None:
            input_["qualifier"] = qualifier
        if revision_id is not None:
            input_["revision_id"] = revision_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncPermission:
    def __init__(self, service: AsyncLambdaClient) -> None:
        self._service = service

    async def add_permission(
        self,
        function_name: "capo_lambda.types.namespaced_function_name.NamespacedFunctionName",
        statement_id: "capo_lambda.types.statement_id.StatementId",
        action: "capo_lambda.types.action.Action",
        principal: "capo_lambda.types.principal.Principal",
        *,
        config_overrides: Optional[AsyncLambdaClientConfig] = None,
        source_arn: Optional["capo_lambda.types.arn.Arn"] = None,
        function_url_auth_type: Optional[
            "capo_lambda.types.function_url_auth_type.FunctionUrlAuthType"
        ] = None,
        invoked_via_function_url: Optional[
            "capo_lambda.types.invoked_via_function_url.InvokedViaFunctionUrl"
        ] = None,
        source_account: Optional["capo_lambda.types.source_owner.SourceOwner"] = None,
        event_source_token: Optional[
            "capo_lambda.types.event_source_token.EventSourceToken"
        ] = None,
        qualifier: Optional[
            "capo_lambda.types.numeric_latest_published_or_alias_qualifier.NumericLatestPublishedOrAliasQualifier"
        ] = None,
        revision_id: Optional["capo_lambda.types.string.String"] = None,
        principal_org_id: Optional[
            "capo_lambda.types.principal_org_id.PrincipalOrgID"
        ] = None,
    ) -> "capo_lambda.types.add_permission_response.AddPermissionResponse":
        """<p>Grants a <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_principal.html#Principal_specifying">principal</a> permission to use a function. You can apply the policy at the function level, or specify a qualifier to restrict access to a single version or alias. If you use a qualifier, the invoker must use the full Amazon Resource Name (ARN) of that version or alias to invoke the function. Note: Lambda does not support adding policies to version $LATEST.</p> <p>To grant permission to another account, specify the account ID as the <code>Principal</code>. To grant permission to an organization defined in Organizations, specify the organization ID as the <code>PrincipalOrgID</code>. For Amazon Web Services services, the principal is a domain-style identifier that the service defines, such as <code>s3.amazonaws.com</code> or <code>sns.amazonaws.com</code>. For Amazon Web Services services, you can also specify the ARN of the associated resource as the <code>SourceArn</code>. If you grant permission to a service principal without specifying the source, other accounts could potentially configure resources in their account to invoke your Lambda function.</p> <p>This operation adds a statement to a resource-based permissions policy for the function. For more information about function policies, see <a href="https://docs.aws.amazon.com/lambda/latest/dg/access-control-resource-based.html">Using resource-based policies for Lambda</a>.</p>

        Args:
            function_name: <p>The name or ARN of the Lambda function, version, or alias.</p> <p class="title"> <b>Name formats</b> </p> <ul> <li> <p> <b>Function name</b> – <code>my-function</code> (name-only), <code>my-function:v1</code> (with alias).</p> </li> <li> <p> <b>Function ARN</b> – <code>arn:aws:lambda:us-west-2:123456789012:function:my-function</code>.</p> </li> <li> <p> <b>Partial ARN</b> – <code>123456789012:function:my-function</code>.</p> </li> </ul> <p>You can append a version number or alias to any of the formats. The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.</p>
            statement_id: <p>A statement identifier that differentiates the statement from others in the same policy.</p>
            action: <p>The action that the principal can use on the function. For example, <code>lambda:InvokeFunction</code> or <code>lambda:GetFunction</code>.</p>
            principal: <p>The Amazon Web Services service, Amazon Web Services account, IAM user, or IAM role that invokes the function. If you specify a service, use <code>SourceArn</code> or <code>SourceAccount</code> to limit who can invoke the function through that service.</p>
            source_arn: <p>For Amazon Web Services services, the ARN of the Amazon Web Services resource that invokes the function. For example, an Amazon S3 bucket or Amazon SNS topic.</p> <p>Note that Lambda configures the comparison using the <code>StringLike</code> operator.</p>
            function_url_auth_type: <p>The type of authentication that your function URL uses. Set to <code>AWS_IAM</code> if you want to restrict access to authenticated users only. Set to <code>NONE</code> if you want to bypass IAM authentication to create a public endpoint. For more information, see <a href="https://docs.aws.amazon.com/lambda/latest/dg/urls-auth.html">Control access to Lambda function URLs</a>.</p>
            invoked_via_function_url: <p>Indicates whether the permission applies when the function is invoked through a function URL. </p>
            source_account: <p>For Amazon Web Services service, the ID of the Amazon Web Services account that owns the resource. Use this together with <code>SourceArn</code> to ensure that the specified account owns the resource. It is possible for an Amazon S3 bucket to be deleted by its owner and recreated by another account.</p>
            event_source_token: <p>For Alexa Smart Home functions, a token that the invoker must supply.</p>
            qualifier: <p>Specify a version or alias to add permissions to a published version of the function.</p>
            revision_id: <p>Update the policy only if the revision ID matches the ID that's specified. Use this option to avoid modifying a policy that has changed since you last read it.</p>
            principal_org_id: <p>The identifier for your organization in Organizations. Use this to grant permissions to all the Amazon Web Services accounts under this organization.</p>

        Raises:
            capo_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid.</p>
            capo_lambda.errors.policy_length_exceeded_exception.PolicyLengthExceededException: <p>The permissions policy for the resource is too large. For more information, see <a href="https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html">Lambda quotas</a>.</p>
            capo_lambda.errors.precondition_failed_exception.PreconditionFailedException: <p>The RevisionId provided does not match the latest RevisionId for the Lambda function or alias.</p> <ul> <li> <p> <b>For AddPermission and RemovePermission API operations:</b> Call <code>GetPolicy</code> to retrieve the latest RevisionId for your resource.</p> </li> <li> <p> <b>For all other API operations:</b> Call <code>GetFunction</code> or <code>GetAlias</code> to retrieve the latest RevisionId for your resource.</p> </li> </ul>
            capo_lambda.errors.public_policy_exception.PublicPolicyException: <p>The resource-based policy you tried to add to the Lambda resource would grant public access to it, which isn't allowed.</p>
            capo_lambda.errors.resource_conflict_exception.ResourceConflictException: <p>The resource already exists, or another operation is in progress.</p>
            capo_lambda.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request does not exist.</p>
            capo_lambda.errors.service_exception.ServiceException: <p>The Lambda service encountered an internal error.</p>
            capo_lambda.errors.too_many_requests_exception.TooManyRequestsException: <p>The request throughput limit was exceeded. For more information, see <a href="https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#api-requests">Lambda quotas</a>.</p>
            capo_lambda.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To grant Amazon S3 permission to invoke a function
            The following example adds permission for Amazon S3 to invoke a Lambda function named my-function for notifications from a bucket named my-bucket-1xpuxmplzrlbh in account 123456789012.

            >>> await client.add_permission(action='lambda:InvokeFunction', function_name='my-function', principal='s3.amazonaws.com', source_account='123456789012', source_arn='arn:aws:s3:::my-bucket-1xpuxmplzrlbh/*', statement_id='s3')
            To grant another account permission to invoke a function
            The following example adds permission for account 223456789012 invoke a Lambda function named my-function.

            >>> await client.add_permission(action='lambda:InvokeFunction', function_name='my-function', principal='223456789012', statement_id='xaccount')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lambda.types.add_permission_request.AddPermissionRequest]",
        ) -> AsyncOperationResponse[
            "capo_lambda.types.add_permission_response.AddPermissionResponse"
        ]:
            import capo_lambda._operations.aws_gir_api_service.add_permission

            (
                output,
                http_response,
            ) = await capo_lambda._operations.aws_gir_api_service.add_permission.async_add_permission(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_lambda.types.add_permission_request.AddPermissionRequest = {
            "function_name": function_name,
            "statement_id": statement_id,
            "action": action,
            "principal": principal,
        }
        if source_arn is not None:
            input_["source_arn"] = source_arn
        if function_url_auth_type is not None:
            input_["function_url_auth_type"] = function_url_auth_type
        if invoked_via_function_url is not None:
            input_["invoked_via_function_url"] = invoked_via_function_url
        if source_account is not None:
            input_["source_account"] = source_account
        if event_source_token is not None:
            input_["event_source_token"] = event_source_token
        if qualifier is not None:
            input_["qualifier"] = qualifier
        if revision_id is not None:
            input_["revision_id"] = revision_id
        if principal_org_id is not None:
            input_["principal_org_id"] = principal_org_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def remove_permission(
        self,
        function_name: "capo_lambda.types.namespaced_function_name.NamespacedFunctionName",
        statement_id: "capo_lambda.types.namespaced_statement_id.NamespacedStatementId",
        *,
        config_overrides: Optional[AsyncLambdaClientConfig] = None,
        qualifier: Optional[
            "capo_lambda.types.numeric_latest_published_or_alias_qualifier.NumericLatestPublishedOrAliasQualifier"
        ] = None,
        revision_id: Optional["capo_lambda.types.string.String"] = None,
    ) -> None:
        """<p>Revokes function-use permission from an Amazon Web Services service or another Amazon Web Services account. You can get the ID of the statement from the output of <a>GetPolicy</a>.</p>

        Args:
            function_name: <p>The name or ARN of the Lambda function, version, or alias.</p> <p class="title"> <b>Name formats</b> </p> <ul> <li> <p> <b>Function name</b> – <code>my-function</code> (name-only), <code>my-function:v1</code> (with alias).</p> </li> <li> <p> <b>Function ARN</b> – <code>arn:aws:lambda:us-west-2:123456789012:function:my-function</code>.</p> </li> <li> <p> <b>Partial ARN</b> – <code>123456789012:function:my-function</code>.</p> </li> </ul> <p>You can append a version number or alias to any of the formats. The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.</p>
            statement_id: <p>Statement ID of the permission to remove.</p>
            qualifier: <p>Specify a version or alias to remove permissions from a published version of the function.</p>
            revision_id: <p>Update the policy only if the revision ID matches the ID that's specified. Use this option to avoid modifying a policy that has changed since you last read it.</p>

        Raises:
            capo_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid.</p>
            capo_lambda.errors.precondition_failed_exception.PreconditionFailedException: <p>The RevisionId provided does not match the latest RevisionId for the Lambda function or alias.</p> <ul> <li> <p> <b>For AddPermission and RemovePermission API operations:</b> Call <code>GetPolicy</code> to retrieve the latest RevisionId for your resource.</p> </li> <li> <p> <b>For all other API operations:</b> Call <code>GetFunction</code> or <code>GetAlias</code> to retrieve the latest RevisionId for your resource.</p> </li> </ul>
            capo_lambda.errors.public_policy_exception.PublicPolicyException: <p>The resource-based policy you tried to add to the Lambda resource would grant public access to it, which isn't allowed.</p>
            capo_lambda.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request does not exist.</p>
            capo_lambda.errors.service_exception.ServiceException: <p>The Lambda service encountered an internal error.</p>
            capo_lambda.errors.too_many_requests_exception.TooManyRequestsException: <p>The request throughput limit was exceeded. For more information, see <a href="https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#api-requests">Lambda quotas</a>.</p>
            capo_lambda.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To remove a Lambda function's permissions
            The following example removes a permissions statement named xaccount from the PROD alias of a function named my-function.

            >>> await client.remove_permission(function_name='my-function', qualifier='PROD', statement_id='xaccount')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lambda.types.remove_permission_request.RemovePermissionRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_lambda._operations.aws_gir_api_service.remove_permission

            (
                output,
                http_response,
            ) = await capo_lambda._operations.aws_gir_api_service.remove_permission.async_remove_permission(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_lambda.types.remove_permission_request.RemovePermissionRequest = {
            "function_name": function_name,
            "statement_id": statement_id,
        }
        if qualifier is not None:
            input_["qualifier"] = qualifier
        if revision_id is not None:
            input_["revision_id"] = revision_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
