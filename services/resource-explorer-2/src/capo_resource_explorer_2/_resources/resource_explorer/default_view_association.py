from __future__ import annotations

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
    import capo_resource_explorer_2.types.associate_default_view_input
    import capo_resource_explorer_2.types.associate_default_view_output
    from capo_resource_explorer_2._services.async_resource_explorer2 import (
        AsyncResourceExplorer2Client,
        AsyncResourceExplorer2ClientConfig,
    )
    from capo_resource_explorer_2._services.resource_explorer2 import (
        ResourceExplorer2Client,
        ResourceExplorer2ClientConfig,
    )


class DefaultViewAssociation:
    def __init__(self, service: ResourceExplorer2Client) -> None:
        self._service = service

    def put(
        self,
        view_arn: str,
        *,
        config_overrides: Optional[ResourceExplorer2ClientConfig] = None,
    ) -> "capo_resource_explorer_2.types.associate_default_view_output.AssociateDefaultViewOutput":
        """<p>Sets the specified view as the default for the Amazon Web Services Region in which you call this operation. When a user performs a <a>Search</a> that doesn't explicitly specify which view to use, then Amazon Web Services Resource Explorer automatically chooses this default view for searches performed in this Amazon Web Services Region.</p> <p>If an Amazon Web Services Region doesn't have a default view configured, then users must explicitly specify a view with every <code>Search</code> operation performed in that Region.</p>

        Args:
            view_arn: <p>The <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon resource name (ARN)</a> of the view to set as the default for the Amazon Web Services Region and Amazon Web Services account in which you call this operation. The specified view must already exist in the called Region.</p>

        Raises:
            capo_resource_explorer_2.errors.access_denied_exception.AccessDeniedException: <p>The credentials that you used to call this operation don't have the minimum required permissions.</p>
            capo_resource_explorer_2.errors.internal_server_exception.InternalServerException: <p>The request failed because of internal service error. Try your request again later.</p>
            capo_resource_explorer_2.errors.resource_not_found_exception.ResourceNotFoundException: <p>You specified a resource that doesn't exist. Check the ID or ARN that you used to identity the resource, and try again.</p>
            capo_resource_explorer_2.errors.throttling_exception.ThrottlingException: <p>The request failed because you exceeded a rate limit for this operation. For more information, see <a href="https://docs.aws.amazon.com/resource-explorer/latest/userguide/quotas.html">Quotas for Resource Explorer</a>.</p>
            capo_resource_explorer_2.errors.validation_exception.ValidationException: <p>You provided an invalid value for one of the operation's parameters. Check the syntax for the operation, and try again.</p>
            capo_resource_explorer_2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_resource_explorer_2.types.associate_default_view_input.AssociateDefaultViewInput]",
        ) -> OperationResponse[
            "capo_resource_explorer_2.types.associate_default_view_output.AssociateDefaultViewOutput"
        ]:
            import capo_resource_explorer_2._operations.resource_explorer.associate_default_view

            output, http_response = (
                capo_resource_explorer_2._operations.resource_explorer.associate_default_view.associate_default_view(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_resource_explorer_2.types.associate_default_view_input.AssociateDefaultViewInput = {
            "view_arn": view_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncDefaultViewAssociation:
    def __init__(self, service: AsyncResourceExplorer2Client) -> None:
        self._service = service

    async def put(
        self,
        view_arn: str,
        *,
        config_overrides: Optional[AsyncResourceExplorer2ClientConfig] = None,
    ) -> "capo_resource_explorer_2.types.associate_default_view_output.AssociateDefaultViewOutput":
        """<p>Sets the specified view as the default for the Amazon Web Services Region in which you call this operation. When a user performs a <a>Search</a> that doesn't explicitly specify which view to use, then Amazon Web Services Resource Explorer automatically chooses this default view for searches performed in this Amazon Web Services Region.</p> <p>If an Amazon Web Services Region doesn't have a default view configured, then users must explicitly specify a view with every <code>Search</code> operation performed in that Region.</p>

        Args:
            view_arn: <p>The <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon resource name (ARN)</a> of the view to set as the default for the Amazon Web Services Region and Amazon Web Services account in which you call this operation. The specified view must already exist in the called Region.</p>

        Raises:
            capo_resource_explorer_2.errors.access_denied_exception.AccessDeniedException: <p>The credentials that you used to call this operation don't have the minimum required permissions.</p>
            capo_resource_explorer_2.errors.internal_server_exception.InternalServerException: <p>The request failed because of internal service error. Try your request again later.</p>
            capo_resource_explorer_2.errors.resource_not_found_exception.ResourceNotFoundException: <p>You specified a resource that doesn't exist. Check the ID or ARN that you used to identity the resource, and try again.</p>
            capo_resource_explorer_2.errors.throttling_exception.ThrottlingException: <p>The request failed because you exceeded a rate limit for this operation. For more information, see <a href="https://docs.aws.amazon.com/resource-explorer/latest/userguide/quotas.html">Quotas for Resource Explorer</a>.</p>
            capo_resource_explorer_2.errors.validation_exception.ValidationException: <p>You provided an invalid value for one of the operation's parameters. Check the syntax for the operation, and try again.</p>
            capo_resource_explorer_2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_resource_explorer_2.types.associate_default_view_input.AssociateDefaultViewInput]",
        ) -> AsyncOperationResponse[
            "capo_resource_explorer_2.types.associate_default_view_output.AssociateDefaultViewOutput"
        ]:
            import capo_resource_explorer_2._operations.resource_explorer.associate_default_view

            (
                output,
                http_response,
            ) = await capo_resource_explorer_2._operations.resource_explorer.associate_default_view.async_associate_default_view(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_resource_explorer_2.types.associate_default_view_input.AssociateDefaultViewInput = {
            "view_arn": view_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
