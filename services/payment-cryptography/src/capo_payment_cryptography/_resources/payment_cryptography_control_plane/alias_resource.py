from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from capo_payment_cryptography._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_payment_cryptography.types.alias
    import capo_payment_cryptography.types.alias_name
    import capo_payment_cryptography.types.create_alias_input
    import capo_payment_cryptography.types.create_alias_output
    import capo_payment_cryptography.types.delete_alias_input
    import capo_payment_cryptography.types.delete_alias_output
    import capo_payment_cryptography.types.get_alias_input
    import capo_payment_cryptography.types.get_alias_output
    import capo_payment_cryptography.types.key_arn
    import capo_payment_cryptography.types.list_aliases_input
    import capo_payment_cryptography.types.list_aliases_output
    import capo_payment_cryptography.types.max_results
    import capo_payment_cryptography.types.next_token
    import capo_payment_cryptography.types.update_alias_input
    import capo_payment_cryptography.types.update_alias_output
    from capo_payment_cryptography._services.async_payment_cryptography import (
        AsyncPaymentCryptographyClient,
        AsyncPaymentCryptographyClientConfig,
    )
    from capo_payment_cryptography._services.payment_cryptography import (
        PaymentCryptographyClient,
        PaymentCryptographyClientConfig,
    )


class AliasResource:
    def __init__(self, service: PaymentCryptographyClient) -> None:
        self._service = service

    def put(
        self,
        alias_name: "capo_payment_cryptography.types.alias_name.AliasName",
        *,
        config_overrides: Optional[PaymentCryptographyClientConfig] = None,
        key_arn: Optional["capo_payment_cryptography.types.key_arn.KeyArn"] = None,
    ) -> "capo_payment_cryptography.types.create_alias_output.CreateAliasOutput":
        """<p>Creates an <i>alias</i>, or a friendly name, for an Amazon Web Services Payment Cryptography key. You can use an alias to identify a key in the console and when you call cryptographic operations such as <a href="https://docs.aws.amazon.com/payment-cryptography/latest/DataAPIReference/API_EncryptData.html">EncryptData</a> or <a href="https://docs.aws.amazon.com/payment-cryptography/latest/DataAPIReference/API_DecryptData.html">DecryptData</a>.</p> <p>You can associate the alias with any key in the same Amazon Web Services Region. Each alias is associated with only one key at a time, but a key can have multiple aliases. You can't create an alias without a key. The alias must be unique in the account and Amazon Web Services Region, but you can create another alias with the same name in a different Amazon Web Services Region.</p> <p>To change the key that's associated with the alias, call <a href="https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_UpdateAlias.html">UpdateAlias</a>. To delete the alias, call <a href="https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_DeleteAlias.html">DeleteAlias</a>. These operations don't affect the underlying key. To get the alias that you created, call <a href="https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_ListAliases.html">ListAliases</a>.</p> <p> <b>Cross-account use</b>: This operation can't be used across different Amazon Web Services accounts.</p> <p> <b>Related operations:</b> </p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_DeleteAlias.html">DeleteAlias</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_GetAlias.html">GetAlias</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_ListAliases.html">ListAliases</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_UpdateAlias.html">UpdateAlias</a> </p> </li> </ul>

        Args:
            alias_name: <p>A friendly name that you can use to refer to a key. An alias must begin with <code>alias/</code> followed by a name, for example <code>alias/ExampleAlias</code>. It can contain only alphanumeric characters, forward slashes (/), underscores (_), and dashes (-).</p> <important> <p>Don't include personal, confidential or sensitive information in this field. This field may be displayed in plaintext in CloudTrail logs and other output.</p> </important>
            key_arn: <p>The <code>KeyARN</code> of the key to associate with the alias.</p>

        Raises:
            capo_payment_cryptography.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p> <p>This exception is thrown when the caller lacks the necessary IAM permissions to perform the requested operation. Verify that your IAM policy includes the required permissions for the specific Amazon Web Services Payment Cryptography action you're attempting.</p>
            capo_payment_cryptography.errors.conflict_exception.ConflictException: <p>This request can cause an inconsistent state for the resource.</p> <p>The requested operation conflicts with the current state of the resource. For example, attempting to delete a key that is currently being used, or trying to create a resource that already exists.</p>
            capo_payment_cryptography.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception, or failure.</p> <p>This indicates a server-side error within the Amazon Web Services Payment Cryptography service. If this error persists, contact support for assistance.</p>
            capo_payment_cryptography.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request was denied due to resource not found.</p> <p>The specified key, alias, or other resource does not exist in your account or region. Verify that the resource identifier is correct and that the resource exists in the expected region.</p>
            capo_payment_cryptography.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>This request would cause a service quota to be exceeded.</p> <p>You have reached the maximum number of keys, aliases, or other resources allowed in your account. Review your current usage and consider deleting unused resources or requesting a quota increase.</p>
            capo_payment_cryptography.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service cannot complete the request.</p> <p>The Amazon Web Services Payment Cryptography service is temporarily unavailable. This is typically a temporary condition - retry your request after a brief delay.</p>
            capo_payment_cryptography.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p> <p>You have exceeded the rate limits for Amazon Web Services Payment Cryptography API calls. Implement exponential backoff and retry logic in your application to handle throttling gracefully.</p>
            capo_payment_cryptography.errors.validation_exception.ValidationException: <p>The request was denied due to an invalid request error.</p> <p>One or more parameters in your request are invalid. Check the parameter values, formats, and constraints specified in the API documentation.</p>
            capo_payment_cryptography.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_payment_cryptography.types.create_alias_input.CreateAliasInput]",
        ) -> OperationResponse[
            "capo_payment_cryptography.types.create_alias_output.CreateAliasOutput"
        ]:
            import capo_payment_cryptography._operations.payment_cryptography_control_plane.create_alias

            output, http_response = (
                capo_payment_cryptography._operations.payment_cryptography_control_plane.create_alias.create_alias(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_payment_cryptography.types.create_alias_input.CreateAliasInput = {
            "alias_name": alias_name
        }
        if key_arn is not None:
            input_["key_arn"] = key_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def read(
        self,
        alias_name: "capo_payment_cryptography.types.alias_name.AliasName",
        *,
        config_overrides: Optional[PaymentCryptographyClientConfig] = None,
    ) -> "capo_payment_cryptography.types.get_alias_output.GetAliasOutput":
        """<p>Gets the Amazon Web Services Payment Cryptography key associated with the alias.</p> <p> <b>Cross-account use:</b> This operation can't be used across different Amazon Web Services accounts.</p> <p> <b>Related operations:</b> </p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_CreateAlias.html">CreateAlias</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_DeleteAlias.html">DeleteAlias</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_ListAliases.html">ListAliases</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_UpdateAlias.html">UpdateAlias</a> </p> </li> </ul>

        Args:
            alias_name: <p>The alias of the Amazon Web Services Payment Cryptography key.</p>

        Raises:
            capo_payment_cryptography.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p> <p>This exception is thrown when the caller lacks the necessary IAM permissions to perform the requested operation. Verify that your IAM policy includes the required permissions for the specific Amazon Web Services Payment Cryptography action you're attempting.</p>
            capo_payment_cryptography.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception, or failure.</p> <p>This indicates a server-side error within the Amazon Web Services Payment Cryptography service. If this error persists, contact support for assistance.</p>
            capo_payment_cryptography.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request was denied due to resource not found.</p> <p>The specified key, alias, or other resource does not exist in your account or region. Verify that the resource identifier is correct and that the resource exists in the expected region.</p>
            capo_payment_cryptography.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service cannot complete the request.</p> <p>The Amazon Web Services Payment Cryptography service is temporarily unavailable. This is typically a temporary condition - retry your request after a brief delay.</p>
            capo_payment_cryptography.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p> <p>You have exceeded the rate limits for Amazon Web Services Payment Cryptography API calls. Implement exponential backoff and retry logic in your application to handle throttling gracefully.</p>
            capo_payment_cryptography.errors.validation_exception.ValidationException: <p>The request was denied due to an invalid request error.</p> <p>One or more parameters in your request are invalid. Check the parameter values, formats, and constraints specified in the API documentation.</p>
            capo_payment_cryptography.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_payment_cryptography.types.get_alias_input.GetAliasInput]",
        ) -> OperationResponse[
            "capo_payment_cryptography.types.get_alias_output.GetAliasOutput"
        ]:
            import capo_payment_cryptography._operations.payment_cryptography_control_plane.get_alias

            output, http_response = (
                capo_payment_cryptography._operations.payment_cryptography_control_plane.get_alias.get_alias(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_payment_cryptography.types.get_alias_input.GetAliasInput = {
            "alias_name": alias_name
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
        alias_name: "capo_payment_cryptography.types.alias_name.AliasName",
        *,
        config_overrides: Optional[PaymentCryptographyClientConfig] = None,
        key_arn: Optional["capo_payment_cryptography.types.key_arn.KeyArn"] = None,
    ) -> "capo_payment_cryptography.types.update_alias_output.UpdateAliasOutput":
        """<p>Associates an existing Amazon Web Services Payment Cryptography alias with a different key. Each alias is associated with only one Amazon Web Services Payment Cryptography key at a time, although a key can have multiple aliases. The alias and the Amazon Web Services Payment Cryptography key must be in the same Amazon Web Services account and Amazon Web Services Region</p> <p> <b>Cross-account use:</b> This operation can't be used across different Amazon Web Services accounts.</p> <p> <b>Related operations:</b> </p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_CreateAlias.html">CreateAlias</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_DeleteAlias.html">DeleteAlias</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_GetAlias.html">GetAlias</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_ListAliases.html">ListAliases</a> </p> </li> </ul>

        Args:
            alias_name: <p>The alias whose associated key is changing.</p>
            key_arn: <p>The <code>KeyARN</code> for the key that you are updating or removing from the alias.</p>

        Raises:
            capo_payment_cryptography.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p> <p>This exception is thrown when the caller lacks the necessary IAM permissions to perform the requested operation. Verify that your IAM policy includes the required permissions for the specific Amazon Web Services Payment Cryptography action you're attempting.</p>
            capo_payment_cryptography.errors.conflict_exception.ConflictException: <p>This request can cause an inconsistent state for the resource.</p> <p>The requested operation conflicts with the current state of the resource. For example, attempting to delete a key that is currently being used, or trying to create a resource that already exists.</p>
            capo_payment_cryptography.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception, or failure.</p> <p>This indicates a server-side error within the Amazon Web Services Payment Cryptography service. If this error persists, contact support for assistance.</p>
            capo_payment_cryptography.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request was denied due to resource not found.</p> <p>The specified key, alias, or other resource does not exist in your account or region. Verify that the resource identifier is correct and that the resource exists in the expected region.</p>
            capo_payment_cryptography.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service cannot complete the request.</p> <p>The Amazon Web Services Payment Cryptography service is temporarily unavailable. This is typically a temporary condition - retry your request after a brief delay.</p>
            capo_payment_cryptography.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p> <p>You have exceeded the rate limits for Amazon Web Services Payment Cryptography API calls. Implement exponential backoff and retry logic in your application to handle throttling gracefully.</p>
            capo_payment_cryptography.errors.validation_exception.ValidationException: <p>The request was denied due to an invalid request error.</p> <p>One or more parameters in your request are invalid. Check the parameter values, formats, and constraints specified in the API documentation.</p>
            capo_payment_cryptography.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_payment_cryptography.types.update_alias_input.UpdateAliasInput]",
        ) -> OperationResponse[
            "capo_payment_cryptography.types.update_alias_output.UpdateAliasOutput"
        ]:
            import capo_payment_cryptography._operations.payment_cryptography_control_plane.update_alias

            output, http_response = (
                capo_payment_cryptography._operations.payment_cryptography_control_plane.update_alias.update_alias(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_payment_cryptography.types.update_alias_input.UpdateAliasInput = {
            "alias_name": alias_name
        }
        if key_arn is not None:
            input_["key_arn"] = key_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete(
        self,
        alias_name: "capo_payment_cryptography.types.alias_name.AliasName",
        *,
        config_overrides: Optional[PaymentCryptographyClientConfig] = None,
    ) -> "capo_payment_cryptography.types.delete_alias_output.DeleteAliasOutput":
        """<p>Deletes the alias, but doesn't affect the underlying key.</p> <p>Each key can have multiple aliases. To get the aliases of all keys, use the <a href="https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_UpdateAlias.html">UpdateAlias</a> operation. To change the alias of a key, first use <a href="https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_DeleteAlias.html">DeleteAlias</a> to delete the current alias and then use <a href="https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_CreateAlias.html">CreateAlias</a> to create a new alias. To associate an existing alias with a different key, call <a href="https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_UpdateAlias.html">UpdateAlias</a>.</p> <p> <b>Cross-account use:</b> This operation can't be used across different Amazon Web Services accounts.</p> <p> <b>Related operations:</b> </p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_CreateAlias.html">CreateAlias</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_GetAlias.html">GetAlias</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_ListAliases.html">ListAliases</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_UpdateAlias.html">UpdateAlias</a> </p> </li> </ul>

        Args:
            alias_name: <p>A friendly name that you can use to refer Amazon Web Services Payment Cryptography key. This value must begin with <code>alias/</code> followed by a name, such as <code>alias/ExampleAlias</code>.</p>

        Raises:
            capo_payment_cryptography.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p> <p>This exception is thrown when the caller lacks the necessary IAM permissions to perform the requested operation. Verify that your IAM policy includes the required permissions for the specific Amazon Web Services Payment Cryptography action you're attempting.</p>
            capo_payment_cryptography.errors.conflict_exception.ConflictException: <p>This request can cause an inconsistent state for the resource.</p> <p>The requested operation conflicts with the current state of the resource. For example, attempting to delete a key that is currently being used, or trying to create a resource that already exists.</p>
            capo_payment_cryptography.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception, or failure.</p> <p>This indicates a server-side error within the Amazon Web Services Payment Cryptography service. If this error persists, contact support for assistance.</p>
            capo_payment_cryptography.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request was denied due to resource not found.</p> <p>The specified key, alias, or other resource does not exist in your account or region. Verify that the resource identifier is correct and that the resource exists in the expected region.</p>
            capo_payment_cryptography.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service cannot complete the request.</p> <p>The Amazon Web Services Payment Cryptography service is temporarily unavailable. This is typically a temporary condition - retry your request after a brief delay.</p>
            capo_payment_cryptography.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p> <p>You have exceeded the rate limits for Amazon Web Services Payment Cryptography API calls. Implement exponential backoff and retry logic in your application to handle throttling gracefully.</p>
            capo_payment_cryptography.errors.validation_exception.ValidationException: <p>The request was denied due to an invalid request error.</p> <p>One or more parameters in your request are invalid. Check the parameter values, formats, and constraints specified in the API documentation.</p>
            capo_payment_cryptography.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_payment_cryptography.types.delete_alias_input.DeleteAliasInput]",
        ) -> OperationResponse[
            "capo_payment_cryptography.types.delete_alias_output.DeleteAliasOutput"
        ]:
            import capo_payment_cryptography._operations.payment_cryptography_control_plane.delete_alias

            output, http_response = (
                capo_payment_cryptography._operations.payment_cryptography_control_plane.delete_alias.delete_alias(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_payment_cryptography.types.delete_alias_input.DeleteAliasInput = {
            "alias_name": alias_name
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
        config_overrides: Optional[PaymentCryptographyClientConfig] = None,
        key_arn: Optional["capo_payment_cryptography.types.key_arn.KeyArn"] = None,
        next_token: Optional[
            "capo_payment_cryptography.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "capo_payment_cryptography.types.max_results.MaxResults"
        ] = None,
    ) -> "capo_payment_cryptography.types.list_aliases_output.ListAliasesOutput":
        """<p>Lists the aliases for all keys in the caller's Amazon Web Services account and Amazon Web Services Region. You can filter the aliases by <code>keyARN</code>. For more information, see <a href="https://docs.aws.amazon.com/payment-cryptography/latest/userguide/keys-managealias.html">Using aliases</a> in the <i>Amazon Web Services Payment Cryptography User Guide</i>.</p> <p>This is a paginated operation, which means that each response might contain only a subset of all the aliases. When the response contains only a subset of aliases, it includes a <code>NextToken</code> value. Use this value in a subsequent <code>ListAliases</code> request to get more aliases. When you receive a response with no NextToken (or an empty or null value), that means there are no more aliases to get.</p> <p> <b>Cross-account use:</b> This operation can't be used across different Amazon Web Services accounts.</p> <p> <b>Related operations:</b> </p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_CreateAlias.html">CreateAlias</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_DeleteAlias.html">DeleteAlias</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_GetAlias.html">GetAlias</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_UpdateAlias.html">UpdateAlias</a> </p> </li> </ul>

        Args:
            key_arn: <p>The <code>keyARN</code> for which you want to list all aliases.</p>
            next_token: <p>Use this parameter in a subsequent request after you receive a response with truncated results. Set it to the value of <code>NextToken</code> from the truncated response you just received.</p>
            max_results: <p>Use this parameter to specify the maximum number of items to return. When this value is present, Amazon Web Services Payment Cryptography does not return more than the specified number of items, but it might return fewer.</p> <p>This value is optional. If you include a value, it must be between 1 and 100, inclusive. If you do not include a value, it defaults to 50.</p>

        Raises:
            capo_payment_cryptography.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p> <p>This exception is thrown when the caller lacks the necessary IAM permissions to perform the requested operation. Verify that your IAM policy includes the required permissions for the specific Amazon Web Services Payment Cryptography action you're attempting.</p>
            capo_payment_cryptography.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception, or failure.</p> <p>This indicates a server-side error within the Amazon Web Services Payment Cryptography service. If this error persists, contact support for assistance.</p>
            capo_payment_cryptography.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request was denied due to resource not found.</p> <p>The specified key, alias, or other resource does not exist in your account or region. Verify that the resource identifier is correct and that the resource exists in the expected region.</p>
            capo_payment_cryptography.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service cannot complete the request.</p> <p>The Amazon Web Services Payment Cryptography service is temporarily unavailable. This is typically a temporary condition - retry your request after a brief delay.</p>
            capo_payment_cryptography.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p> <p>You have exceeded the rate limits for Amazon Web Services Payment Cryptography API calls. Implement exponential backoff and retry logic in your application to handle throttling gracefully.</p>
            capo_payment_cryptography.errors.validation_exception.ValidationException: <p>The request was denied due to an invalid request error.</p> <p>One or more parameters in your request are invalid. Check the parameter values, formats, and constraints specified in the API documentation.</p>
            capo_payment_cryptography.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_payment_cryptography.types.list_aliases_input.ListAliasesInput]",
        ) -> OperationResponse[
            "capo_payment_cryptography.types.list_aliases_output.ListAliasesOutput"
        ]:
            import capo_payment_cryptography._operations.payment_cryptography_control_plane.list_aliases

            output, http_response = (
                capo_payment_cryptography._operations.payment_cryptography_control_plane.list_aliases.list_aliases(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_payment_cryptography.types.list_aliases_input.ListAliasesInput = {}
        if key_arn is not None:
            input_["key_arn"] = key_arn
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


class AsyncAliasResource:
    def __init__(self, service: AsyncPaymentCryptographyClient) -> None:
        self._service = service

    async def put(
        self,
        alias_name: "capo_payment_cryptography.types.alias_name.AliasName",
        *,
        config_overrides: Optional[AsyncPaymentCryptographyClientConfig] = None,
        key_arn: Optional["capo_payment_cryptography.types.key_arn.KeyArn"] = None,
    ) -> "capo_payment_cryptography.types.create_alias_output.CreateAliasOutput":
        """<p>Creates an <i>alias</i>, or a friendly name, for an Amazon Web Services Payment Cryptography key. You can use an alias to identify a key in the console and when you call cryptographic operations such as <a href="https://docs.aws.amazon.com/payment-cryptography/latest/DataAPIReference/API_EncryptData.html">EncryptData</a> or <a href="https://docs.aws.amazon.com/payment-cryptography/latest/DataAPIReference/API_DecryptData.html">DecryptData</a>.</p> <p>You can associate the alias with any key in the same Amazon Web Services Region. Each alias is associated with only one key at a time, but a key can have multiple aliases. You can't create an alias without a key. The alias must be unique in the account and Amazon Web Services Region, but you can create another alias with the same name in a different Amazon Web Services Region.</p> <p>To change the key that's associated with the alias, call <a href="https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_UpdateAlias.html">UpdateAlias</a>. To delete the alias, call <a href="https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_DeleteAlias.html">DeleteAlias</a>. These operations don't affect the underlying key. To get the alias that you created, call <a href="https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_ListAliases.html">ListAliases</a>.</p> <p> <b>Cross-account use</b>: This operation can't be used across different Amazon Web Services accounts.</p> <p> <b>Related operations:</b> </p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_DeleteAlias.html">DeleteAlias</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_GetAlias.html">GetAlias</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_ListAliases.html">ListAliases</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_UpdateAlias.html">UpdateAlias</a> </p> </li> </ul>

        Args:
            alias_name: <p>A friendly name that you can use to refer to a key. An alias must begin with <code>alias/</code> followed by a name, for example <code>alias/ExampleAlias</code>. It can contain only alphanumeric characters, forward slashes (/), underscores (_), and dashes (-).</p> <important> <p>Don't include personal, confidential or sensitive information in this field. This field may be displayed in plaintext in CloudTrail logs and other output.</p> </important>
            key_arn: <p>The <code>KeyARN</code> of the key to associate with the alias.</p>

        Raises:
            capo_payment_cryptography.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p> <p>This exception is thrown when the caller lacks the necessary IAM permissions to perform the requested operation. Verify that your IAM policy includes the required permissions for the specific Amazon Web Services Payment Cryptography action you're attempting.</p>
            capo_payment_cryptography.errors.conflict_exception.ConflictException: <p>This request can cause an inconsistent state for the resource.</p> <p>The requested operation conflicts with the current state of the resource. For example, attempting to delete a key that is currently being used, or trying to create a resource that already exists.</p>
            capo_payment_cryptography.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception, or failure.</p> <p>This indicates a server-side error within the Amazon Web Services Payment Cryptography service. If this error persists, contact support for assistance.</p>
            capo_payment_cryptography.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request was denied due to resource not found.</p> <p>The specified key, alias, or other resource does not exist in your account or region. Verify that the resource identifier is correct and that the resource exists in the expected region.</p>
            capo_payment_cryptography.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>This request would cause a service quota to be exceeded.</p> <p>You have reached the maximum number of keys, aliases, or other resources allowed in your account. Review your current usage and consider deleting unused resources or requesting a quota increase.</p>
            capo_payment_cryptography.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service cannot complete the request.</p> <p>The Amazon Web Services Payment Cryptography service is temporarily unavailable. This is typically a temporary condition - retry your request after a brief delay.</p>
            capo_payment_cryptography.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p> <p>You have exceeded the rate limits for Amazon Web Services Payment Cryptography API calls. Implement exponential backoff and retry logic in your application to handle throttling gracefully.</p>
            capo_payment_cryptography.errors.validation_exception.ValidationException: <p>The request was denied due to an invalid request error.</p> <p>One or more parameters in your request are invalid. Check the parameter values, formats, and constraints specified in the API documentation.</p>
            capo_payment_cryptography.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_payment_cryptography.types.create_alias_input.CreateAliasInput]",
        ) -> AsyncOperationResponse[
            "capo_payment_cryptography.types.create_alias_output.CreateAliasOutput"
        ]:
            import capo_payment_cryptography._operations.payment_cryptography_control_plane.create_alias

            (
                output,
                http_response,
            ) = await capo_payment_cryptography._operations.payment_cryptography_control_plane.create_alias.async_create_alias(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_payment_cryptography.types.create_alias_input.CreateAliasInput = {
            "alias_name": alias_name
        }
        if key_arn is not None:
            input_["key_arn"] = key_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def read(
        self,
        alias_name: "capo_payment_cryptography.types.alias_name.AliasName",
        *,
        config_overrides: Optional[AsyncPaymentCryptographyClientConfig] = None,
    ) -> "capo_payment_cryptography.types.get_alias_output.GetAliasOutput":
        """<p>Gets the Amazon Web Services Payment Cryptography key associated with the alias.</p> <p> <b>Cross-account use:</b> This operation can't be used across different Amazon Web Services accounts.</p> <p> <b>Related operations:</b> </p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_CreateAlias.html">CreateAlias</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_DeleteAlias.html">DeleteAlias</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_ListAliases.html">ListAliases</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_UpdateAlias.html">UpdateAlias</a> </p> </li> </ul>

        Args:
            alias_name: <p>The alias of the Amazon Web Services Payment Cryptography key.</p>

        Raises:
            capo_payment_cryptography.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p> <p>This exception is thrown when the caller lacks the necessary IAM permissions to perform the requested operation. Verify that your IAM policy includes the required permissions for the specific Amazon Web Services Payment Cryptography action you're attempting.</p>
            capo_payment_cryptography.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception, or failure.</p> <p>This indicates a server-side error within the Amazon Web Services Payment Cryptography service. If this error persists, contact support for assistance.</p>
            capo_payment_cryptography.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request was denied due to resource not found.</p> <p>The specified key, alias, or other resource does not exist in your account or region. Verify that the resource identifier is correct and that the resource exists in the expected region.</p>
            capo_payment_cryptography.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service cannot complete the request.</p> <p>The Amazon Web Services Payment Cryptography service is temporarily unavailable. This is typically a temporary condition - retry your request after a brief delay.</p>
            capo_payment_cryptography.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p> <p>You have exceeded the rate limits for Amazon Web Services Payment Cryptography API calls. Implement exponential backoff and retry logic in your application to handle throttling gracefully.</p>
            capo_payment_cryptography.errors.validation_exception.ValidationException: <p>The request was denied due to an invalid request error.</p> <p>One or more parameters in your request are invalid. Check the parameter values, formats, and constraints specified in the API documentation.</p>
            capo_payment_cryptography.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_payment_cryptography.types.get_alias_input.GetAliasInput]",
        ) -> AsyncOperationResponse[
            "capo_payment_cryptography.types.get_alias_output.GetAliasOutput"
        ]:
            import capo_payment_cryptography._operations.payment_cryptography_control_plane.get_alias

            (
                output,
                http_response,
            ) = await capo_payment_cryptography._operations.payment_cryptography_control_plane.get_alias.async_get_alias(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_payment_cryptography.types.get_alias_input.GetAliasInput = {
            "alias_name": alias_name
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
        alias_name: "capo_payment_cryptography.types.alias_name.AliasName",
        *,
        config_overrides: Optional[AsyncPaymentCryptographyClientConfig] = None,
        key_arn: Optional["capo_payment_cryptography.types.key_arn.KeyArn"] = None,
    ) -> "capo_payment_cryptography.types.update_alias_output.UpdateAliasOutput":
        """<p>Associates an existing Amazon Web Services Payment Cryptography alias with a different key. Each alias is associated with only one Amazon Web Services Payment Cryptography key at a time, although a key can have multiple aliases. The alias and the Amazon Web Services Payment Cryptography key must be in the same Amazon Web Services account and Amazon Web Services Region</p> <p> <b>Cross-account use:</b> This operation can't be used across different Amazon Web Services accounts.</p> <p> <b>Related operations:</b> </p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_CreateAlias.html">CreateAlias</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_DeleteAlias.html">DeleteAlias</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_GetAlias.html">GetAlias</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_ListAliases.html">ListAliases</a> </p> </li> </ul>

        Args:
            alias_name: <p>The alias whose associated key is changing.</p>
            key_arn: <p>The <code>KeyARN</code> for the key that you are updating or removing from the alias.</p>

        Raises:
            capo_payment_cryptography.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p> <p>This exception is thrown when the caller lacks the necessary IAM permissions to perform the requested operation. Verify that your IAM policy includes the required permissions for the specific Amazon Web Services Payment Cryptography action you're attempting.</p>
            capo_payment_cryptography.errors.conflict_exception.ConflictException: <p>This request can cause an inconsistent state for the resource.</p> <p>The requested operation conflicts with the current state of the resource. For example, attempting to delete a key that is currently being used, or trying to create a resource that already exists.</p>
            capo_payment_cryptography.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception, or failure.</p> <p>This indicates a server-side error within the Amazon Web Services Payment Cryptography service. If this error persists, contact support for assistance.</p>
            capo_payment_cryptography.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request was denied due to resource not found.</p> <p>The specified key, alias, or other resource does not exist in your account or region. Verify that the resource identifier is correct and that the resource exists in the expected region.</p>
            capo_payment_cryptography.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service cannot complete the request.</p> <p>The Amazon Web Services Payment Cryptography service is temporarily unavailable. This is typically a temporary condition - retry your request after a brief delay.</p>
            capo_payment_cryptography.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p> <p>You have exceeded the rate limits for Amazon Web Services Payment Cryptography API calls. Implement exponential backoff and retry logic in your application to handle throttling gracefully.</p>
            capo_payment_cryptography.errors.validation_exception.ValidationException: <p>The request was denied due to an invalid request error.</p> <p>One or more parameters in your request are invalid. Check the parameter values, formats, and constraints specified in the API documentation.</p>
            capo_payment_cryptography.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_payment_cryptography.types.update_alias_input.UpdateAliasInput]",
        ) -> AsyncOperationResponse[
            "capo_payment_cryptography.types.update_alias_output.UpdateAliasOutput"
        ]:
            import capo_payment_cryptography._operations.payment_cryptography_control_plane.update_alias

            (
                output,
                http_response,
            ) = await capo_payment_cryptography._operations.payment_cryptography_control_plane.update_alias.async_update_alias(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_payment_cryptography.types.update_alias_input.UpdateAliasInput = {
            "alias_name": alias_name
        }
        if key_arn is not None:
            input_["key_arn"] = key_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete(
        self,
        alias_name: "capo_payment_cryptography.types.alias_name.AliasName",
        *,
        config_overrides: Optional[AsyncPaymentCryptographyClientConfig] = None,
    ) -> "capo_payment_cryptography.types.delete_alias_output.DeleteAliasOutput":
        """<p>Deletes the alias, but doesn't affect the underlying key.</p> <p>Each key can have multiple aliases. To get the aliases of all keys, use the <a href="https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_UpdateAlias.html">UpdateAlias</a> operation. To change the alias of a key, first use <a href="https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_DeleteAlias.html">DeleteAlias</a> to delete the current alias and then use <a href="https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_CreateAlias.html">CreateAlias</a> to create a new alias. To associate an existing alias with a different key, call <a href="https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_UpdateAlias.html">UpdateAlias</a>.</p> <p> <b>Cross-account use:</b> This operation can't be used across different Amazon Web Services accounts.</p> <p> <b>Related operations:</b> </p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_CreateAlias.html">CreateAlias</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_GetAlias.html">GetAlias</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_ListAliases.html">ListAliases</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_UpdateAlias.html">UpdateAlias</a> </p> </li> </ul>

        Args:
            alias_name: <p>A friendly name that you can use to refer Amazon Web Services Payment Cryptography key. This value must begin with <code>alias/</code> followed by a name, such as <code>alias/ExampleAlias</code>.</p>

        Raises:
            capo_payment_cryptography.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p> <p>This exception is thrown when the caller lacks the necessary IAM permissions to perform the requested operation. Verify that your IAM policy includes the required permissions for the specific Amazon Web Services Payment Cryptography action you're attempting.</p>
            capo_payment_cryptography.errors.conflict_exception.ConflictException: <p>This request can cause an inconsistent state for the resource.</p> <p>The requested operation conflicts with the current state of the resource. For example, attempting to delete a key that is currently being used, or trying to create a resource that already exists.</p>
            capo_payment_cryptography.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception, or failure.</p> <p>This indicates a server-side error within the Amazon Web Services Payment Cryptography service. If this error persists, contact support for assistance.</p>
            capo_payment_cryptography.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request was denied due to resource not found.</p> <p>The specified key, alias, or other resource does not exist in your account or region. Verify that the resource identifier is correct and that the resource exists in the expected region.</p>
            capo_payment_cryptography.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service cannot complete the request.</p> <p>The Amazon Web Services Payment Cryptography service is temporarily unavailable. This is typically a temporary condition - retry your request after a brief delay.</p>
            capo_payment_cryptography.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p> <p>You have exceeded the rate limits for Amazon Web Services Payment Cryptography API calls. Implement exponential backoff and retry logic in your application to handle throttling gracefully.</p>
            capo_payment_cryptography.errors.validation_exception.ValidationException: <p>The request was denied due to an invalid request error.</p> <p>One or more parameters in your request are invalid. Check the parameter values, formats, and constraints specified in the API documentation.</p>
            capo_payment_cryptography.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_payment_cryptography.types.delete_alias_input.DeleteAliasInput]",
        ) -> AsyncOperationResponse[
            "capo_payment_cryptography.types.delete_alias_output.DeleteAliasOutput"
        ]:
            import capo_payment_cryptography._operations.payment_cryptography_control_plane.delete_alias

            (
                output,
                http_response,
            ) = await capo_payment_cryptography._operations.payment_cryptography_control_plane.delete_alias.async_delete_alias(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_payment_cryptography.types.delete_alias_input.DeleteAliasInput = {
            "alias_name": alias_name
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
        config_overrides: Optional[AsyncPaymentCryptographyClientConfig] = None,
        key_arn: Optional["capo_payment_cryptography.types.key_arn.KeyArn"] = None,
        next_token: Optional[
            "capo_payment_cryptography.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "capo_payment_cryptography.types.max_results.MaxResults"
        ] = None,
    ) -> "capo_payment_cryptography.types.list_aliases_output.ListAliasesOutput":
        """<p>Lists the aliases for all keys in the caller's Amazon Web Services account and Amazon Web Services Region. You can filter the aliases by <code>keyARN</code>. For more information, see <a href="https://docs.aws.amazon.com/payment-cryptography/latest/userguide/keys-managealias.html">Using aliases</a> in the <i>Amazon Web Services Payment Cryptography User Guide</i>.</p> <p>This is a paginated operation, which means that each response might contain only a subset of all the aliases. When the response contains only a subset of aliases, it includes a <code>NextToken</code> value. Use this value in a subsequent <code>ListAliases</code> request to get more aliases. When you receive a response with no NextToken (or an empty or null value), that means there are no more aliases to get.</p> <p> <b>Cross-account use:</b> This operation can't be used across different Amazon Web Services accounts.</p> <p> <b>Related operations:</b> </p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_CreateAlias.html">CreateAlias</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_DeleteAlias.html">DeleteAlias</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_GetAlias.html">GetAlias</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_UpdateAlias.html">UpdateAlias</a> </p> </li> </ul>

        Args:
            key_arn: <p>The <code>keyARN</code> for which you want to list all aliases.</p>
            next_token: <p>Use this parameter in a subsequent request after you receive a response with truncated results. Set it to the value of <code>NextToken</code> from the truncated response you just received.</p>
            max_results: <p>Use this parameter to specify the maximum number of items to return. When this value is present, Amazon Web Services Payment Cryptography does not return more than the specified number of items, but it might return fewer.</p> <p>This value is optional. If you include a value, it must be between 1 and 100, inclusive. If you do not include a value, it defaults to 50.</p>

        Raises:
            capo_payment_cryptography.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p> <p>This exception is thrown when the caller lacks the necessary IAM permissions to perform the requested operation. Verify that your IAM policy includes the required permissions for the specific Amazon Web Services Payment Cryptography action you're attempting.</p>
            capo_payment_cryptography.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception, or failure.</p> <p>This indicates a server-side error within the Amazon Web Services Payment Cryptography service. If this error persists, contact support for assistance.</p>
            capo_payment_cryptography.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request was denied due to resource not found.</p> <p>The specified key, alias, or other resource does not exist in your account or region. Verify that the resource identifier is correct and that the resource exists in the expected region.</p>
            capo_payment_cryptography.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service cannot complete the request.</p> <p>The Amazon Web Services Payment Cryptography service is temporarily unavailable. This is typically a temporary condition - retry your request after a brief delay.</p>
            capo_payment_cryptography.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p> <p>You have exceeded the rate limits for Amazon Web Services Payment Cryptography API calls. Implement exponential backoff and retry logic in your application to handle throttling gracefully.</p>
            capo_payment_cryptography.errors.validation_exception.ValidationException: <p>The request was denied due to an invalid request error.</p> <p>One or more parameters in your request are invalid. Check the parameter values, formats, and constraints specified in the API documentation.</p>
            capo_payment_cryptography.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_payment_cryptography.types.list_aliases_input.ListAliasesInput]",
        ) -> AsyncOperationResponse[
            "capo_payment_cryptography.types.list_aliases_output.ListAliasesOutput"
        ]:
            import capo_payment_cryptography._operations.payment_cryptography_control_plane.list_aliases

            (
                output,
                http_response,
            ) = await capo_payment_cryptography._operations.payment_cryptography_control_plane.list_aliases.async_list_aliases(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_payment_cryptography.types.list_aliases_input.ListAliasesInput = {}
        if key_arn is not None:
            input_["key_arn"] = key_arn
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
