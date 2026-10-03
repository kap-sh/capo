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
    import capo_payment_cryptography.types.add_key_replication_regions_input
    import capo_payment_cryptography.types.add_key_replication_regions_output
    import capo_payment_cryptography.types.create_key_input
    import capo_payment_cryptography.types.create_key_output
    import capo_payment_cryptography.types.delete_key_input
    import capo_payment_cryptography.types.delete_key_output
    import capo_payment_cryptography.types.derive_key_usage
    import capo_payment_cryptography.types.get_key_input
    import capo_payment_cryptography.types.get_key_output
    import capo_payment_cryptography.types.key_arn_or_key_alias_type
    import capo_payment_cryptography.types.key_attributes
    import capo_payment_cryptography.types.key_check_value_algorithm
    import capo_payment_cryptography.types.key_state
    import capo_payment_cryptography.types.key_summary
    import capo_payment_cryptography.types.list_keys_input
    import capo_payment_cryptography.types.list_keys_output
    import capo_payment_cryptography.types.max_results
    import capo_payment_cryptography.types.next_token
    import capo_payment_cryptography.types.regions
    import capo_payment_cryptography.types.remove_key_replication_regions_input
    import capo_payment_cryptography.types.remove_key_replication_regions_output
    import capo_payment_cryptography.types.restore_key_input
    import capo_payment_cryptography.types.restore_key_output
    import capo_payment_cryptography.types.start_key_usage_input
    import capo_payment_cryptography.types.start_key_usage_output
    import capo_payment_cryptography.types.stop_key_usage_input
    import capo_payment_cryptography.types.stop_key_usage_output
    import capo_payment_cryptography.types.tags
    from capo_payment_cryptography._services.async_payment_cryptography import (
        AsyncPaymentCryptographyClient,
        AsyncPaymentCryptographyClientConfig,
    )
    from capo_payment_cryptography._services.payment_cryptography import (
        PaymentCryptographyClient,
        PaymentCryptographyClientConfig,
    )


class KeyResource:
    def __init__(self, service: PaymentCryptographyClient) -> None:
        self._service = service

    def create(
        self,
        key_attributes: "capo_payment_cryptography.types.key_attributes.KeyAttributes",
        exportable: bool,
        *,
        config_overrides: Optional[PaymentCryptographyClientConfig] = None,
        key_check_value_algorithm: Optional[
            "capo_payment_cryptography.types.key_check_value_algorithm.KeyCheckValueAlgorithm"
        ] = None,
        enabled: Optional[bool] = None,
        tags: Optional["capo_payment_cryptography.types.tags.Tags"] = None,
        derive_key_usage: Optional[
            "capo_payment_cryptography.types.derive_key_usage.DeriveKeyUsage"
        ] = None,
        replication_regions: Optional[
            "capo_payment_cryptography.types.regions.Regions"
        ] = None,
    ) -> "capo_payment_cryptography.types.create_key_output.CreateKeyOutput":
        """<p>Creates an Amazon Web Services Payment Cryptography key, a logical representation of a cryptographic key, that is unique in your account and Amazon Web Services Region. You use keys for cryptographic functions such as encryption and decryption. </p> <p>In addition to the key material used in cryptographic operations, an Amazon Web Services Payment Cryptography key includes metadata such as the key ARN, key usage, key origin, creation date, description, and key state.</p> <p>When you create a key, you specify both immutable and mutable data about the key. The immutable data contains key attributes that define the scope and cryptographic operations that you can perform using the key, for example key class (example: <code>SYMMETRIC_KEY</code>), key algorithm (example: <code>TDES_2KEY</code>), key usage (example: <code>TR31_P0_PIN_ENCRYPTION_KEY</code>) and key modes of use (example: <code>Encrypt</code>). Amazon Web Services Payment Cryptography binds key attributes to keys using key blocks when you store or export them. Amazon Web Services Payment Cryptography stores the key contents wrapped and never stores or transmits them in the clear.</p> <p>For information about valid combinations of key attributes, see <a href="https://docs.aws.amazon.com/payment-cryptography/latest/userguide/keys-validattributes.html">Understanding key attributes</a> in the <i>Amazon Web Services Payment Cryptography User Guide</i>. The mutable data contained within a key includes usage timestamp and key deletion timestamp and can be modified after creation.</p> <p>You can use the <code>CreateKey</code> operation to generate an ECC (Elliptic Curve Cryptography) key pair used for establishing an ECDH (Elliptic Curve Diffie-Hellman) key agreement between two parties. In the ECDH key agreement process, both parties generate their own ECC key pair with key usage K3 and exchange the public keys. Each party then use their private key, the received public key from the other party, and the key derivation parameters including key derivation function, hash algorithm, derivation data, and key algorithm to derive a shared key.</p> <p>To maintain the single-use principle of cryptographic keys in payments, ECDH derived keys should not be used for multiple purposes, such as a <code>TR31_P0_PIN_ENCRYPTION_KEY</code> and <code>TR31_K1_KEY_BLOCK_PROTECTION_KEY</code>. When creating ECC key pairs in Amazon Web Services Payment Cryptography you can optionally set the <code>DeriveKeyUsage</code> parameter, which defines the key usage bound to the symmetric key that will be derived using the ECC key pair.</p> <p> <b>Cross-account use</b>: This operation can't be used across different Amazon Web Services accounts.</p> <p> <b>Related operations:</b> </p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_DeleteKey.html">DeleteKey</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_GetKey.html">GetKey</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_ListKeys.html">ListKeys</a> </p> </li> </ul>

        Args:
            key_attributes: <p>The role of the key, the algorithm it supports, and the cryptographic operations allowed with the key. This data is immutable after the key is created.</p>
            key_check_value_algorithm: <p>The algorithm that Amazon Web Services Payment Cryptography uses to calculate the key check value (KCV). It is used to validate the key integrity.</p> <p>For TDES keys, the KCV is computed by encrypting 8 bytes, each with value of zero, with the key to be checked and retaining the 3 highest order bytes of the encrypted result. For AES keys, the KCV is computed using a CMAC algorithm where the input data is 16 bytes of zero and retaining the 3 highest order bytes of the encrypted result. For HMAC keys, the KCV is computed using the hash selected at key creation on a zero-length message, taking the leftmost 3 bytes.</p>
            exportable: <p>Specifies whether the key is exportable from the service.</p>
            enabled: <p>Specifies whether to enable the key. If the key is enabled, it is activated for use within the service. If the key is not enabled, then it is created but not activated. The default value is enabled.</p>
            tags: <p>Assigns one or more tags to the Amazon Web Services Payment Cryptography key. Use this parameter to tag a key when it is created. To tag an existing Amazon Web Services Payment Cryptography key, use the <a href="https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_TagResource.html">TagResource</a> operation.</p> <p>Each tag consists of a tag key and a tag value. Both the tag key and the tag value are required, but the tag value can be an empty (null) string. You can't have more than one tag on an Amazon Web Services Payment Cryptography key with the same tag key. </p> <important> <p>Don't include personal, confidential or sensitive information in this field. This field may be displayed in plaintext in CloudTrail logs and other output.</p> </important> <note> <p>Tagging or untagging an Amazon Web Services Payment Cryptography key can allow or deny permission to the key.</p> </note>
            derive_key_usage: <p>The intended cryptographic usage of keys derived from the ECC key pair to be created.</p> <p>After creating an ECC key pair, you cannot change the intended cryptographic usage of keys derived from it using ECDH.</p>

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
            req: "OperationRequest[capo_payment_cryptography.types.create_key_input.CreateKeyInput]",
        ) -> OperationResponse[
            "capo_payment_cryptography.types.create_key_output.CreateKeyOutput"
        ]:
            import capo_payment_cryptography._operations.payment_cryptography_control_plane.create_key

            output, http_response = (
                capo_payment_cryptography._operations.payment_cryptography_control_plane.create_key.create_key(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_payment_cryptography.types.create_key_input.CreateKeyInput = {
            "key_attributes": key_attributes,
            "exportable": exportable,
        }
        if key_check_value_algorithm is not None:
            input_["key_check_value_algorithm"] = key_check_value_algorithm
        if enabled is not None:
            input_["enabled"] = enabled
        if tags is not None:
            input_["tags"] = tags
        if derive_key_usage is not None:
            input_["derive_key_usage"] = derive_key_usage
        if replication_regions is not None:
            input_["replication_regions"] = replication_regions

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def read(
        self,
        key_identifier: "capo_payment_cryptography.types.key_arn_or_key_alias_type.KeyArnOrKeyAliasType",
        *,
        config_overrides: Optional[PaymentCryptographyClientConfig] = None,
    ) -> "capo_payment_cryptography.types.get_key_output.GetKeyOutput":
        """<p>Gets the key metadata for an Amazon Web Services Payment Cryptography key, including the immutable and mutable attributes specified when the key was created. Returns key metadata including attributes, state, and timestamps, but does not return the actual cryptographic key material.</p> <p> <b>Cross-account use:</b> This operation supports cross-account use when the key has a resource-based policy that grants access. For more information, see <a href="https://docs.aws.amazon.com/payment-cryptography/latest/userguide/security_iam_resource-based-policies.html">Resource-based policies</a>.</p> <p> <b>Related operations:</b> </p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_CreateKey.html">CreateKey</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_DeleteKey.html">DeleteKey</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_ListKeys.html">ListKeys</a> </p> </li> </ul>

        Args:
            key_identifier: <p>The <code>KeyARN</code> of the Amazon Web Services Payment Cryptography key.</p>

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
            req: "OperationRequest[capo_payment_cryptography.types.get_key_input.GetKeyInput]",
        ) -> OperationResponse[
            "capo_payment_cryptography.types.get_key_output.GetKeyOutput"
        ]:
            import capo_payment_cryptography._operations.payment_cryptography_control_plane.get_key

            output, http_response = (
                capo_payment_cryptography._operations.payment_cryptography_control_plane.get_key.get_key(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_payment_cryptography.types.get_key_input.GetKeyInput = {
            "key_identifier": key_identifier
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
        key_identifier: "capo_payment_cryptography.types.key_arn_or_key_alias_type.KeyArnOrKeyAliasType",
        *,
        config_overrides: Optional[PaymentCryptographyClientConfig] = None,
        delete_key_in_days: Optional[int] = None,
    ) -> "capo_payment_cryptography.types.delete_key_output.DeleteKeyOutput":
        """<p>Deletes the key material and metadata associated with Amazon Web Services Payment Cryptography key.</p> <p>Key deletion is irreversible. After a key is deleted, you can't perform cryptographic operations using the key. For example, you can't decrypt data that was encrypted by a deleted Amazon Web Services Payment Cryptography key, and the data may become unrecoverable. Because key deletion is destructive, Amazon Web Services Payment Cryptography has a safety mechanism to prevent accidental deletion of a key. When you call this operation, Amazon Web Services Payment Cryptography disables the specified key but doesn't delete it until after a waiting period set using <code>DeleteKeyInDays</code>. The default waiting period is 7 days. During the waiting period, the <code>KeyState</code> is <code>DELETE_PENDING</code>. After the key is deleted, the <code>KeyState</code> is <code>DELETE_COMPLETE</code>.</p> <p>You should delete a key only when you are sure that you don't need to use it anymore and no other parties are utilizing this key. If you aren't sure, consider deactivating it instead by calling <a href="https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_StopKeyUsage.html">StopKeyUsage</a>.</p> <p> <b>Cross-account use:</b> This operation supports cross-account use when the key has a resource-based policy that grants access. For more information, see <a href="https://docs.aws.amazon.com/payment-cryptography/latest/userguide/security_iam_resource-based-policies.html">Resource-based policies</a>.</p> <p> <b>Related operations:</b> </p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_RestoreKey.html">RestoreKey</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_StartKeyUsage.html">StartKeyUsage</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_StopKeyUsage.html">StopKeyUsage</a> </p> </li> </ul>

        Args:
            key_identifier: <p>The <code>KeyARN</code> of the key that is scheduled for deletion.</p>
            delete_key_in_days: <p>The waiting period for key deletion. The default value is seven days.</p>

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
            req: "OperationRequest[capo_payment_cryptography.types.delete_key_input.DeleteKeyInput]",
        ) -> OperationResponse[
            "capo_payment_cryptography.types.delete_key_output.DeleteKeyOutput"
        ]:
            import capo_payment_cryptography._operations.payment_cryptography_control_plane.delete_key

            output, http_response = (
                capo_payment_cryptography._operations.payment_cryptography_control_plane.delete_key.delete_key(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_payment_cryptography.types.delete_key_input.DeleteKeyInput = {
            "key_identifier": key_identifier
        }
        if delete_key_in_days is not None:
            input_["delete_key_in_days"] = delete_key_in_days

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
        key_state: Optional[
            "capo_payment_cryptography.types.key_state.KeyState"
        ] = None,
        next_token: Optional[
            "capo_payment_cryptography.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "capo_payment_cryptography.types.max_results.MaxResults"
        ] = None,
    ) -> "capo_payment_cryptography.types.list_keys_output.ListKeysOutput":
        """<p>Lists the keys in the caller's Amazon Web Services account and Amazon Web Services Region. You can filter the list of keys.</p> <p>This is a paginated operation, which means that each response might contain only a subset of all the keys. When the response contains only a subset of keys, it includes a <code>NextToken</code> value. Use this value in a subsequent <code>ListKeys</code> request to get more keys. When you receive a response with no NextToken (or an empty or null value), that means there are no more keys to get.</p> <p> <b>Cross-account use:</b> This operation can't be used across different Amazon Web Services accounts.</p> <p> <b>Related operations:</b> </p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_CreateKey.html">CreateKey</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_DeleteKey.html">DeleteKey</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_GetKey.html">GetKey</a> </p> </li> </ul>

        Args:
            key_state: <p>The key state of the keys you want to list.</p>
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
            req: "OperationRequest[capo_payment_cryptography.types.list_keys_input.ListKeysInput]",
        ) -> OperationResponse[
            "capo_payment_cryptography.types.list_keys_output.ListKeysOutput"
        ]:
            import capo_payment_cryptography._operations.payment_cryptography_control_plane.list_keys

            output, http_response = (
                capo_payment_cryptography._operations.payment_cryptography_control_plane.list_keys.list_keys(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_payment_cryptography.types.list_keys_input.ListKeysInput = {}
        if key_state is not None:
            input_["key_state"] = key_state
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

    def add_key_replication_regions(
        self,
        key_identifier: "capo_payment_cryptography.types.key_arn_or_key_alias_type.KeyArnOrKeyAliasType",
        replication_regions: "capo_payment_cryptography.types.regions.Regions",
        *,
        config_overrides: Optional[PaymentCryptographyClientConfig] = None,
    ) -> "capo_payment_cryptography.types.add_key_replication_regions_output.AddKeyReplicationRegionsOutput":
        """<p>Adds replication Amazon Web Services Regions to an existing Amazon Web Services Payment Cryptography key, enabling the key to be used for cryptographic operations in additional Amazon Web Services Regions.</p> <p> <a href="https://docs.aws.amazon.com/payment-cryptography/latest/userguide/keys-multi-region-replication.html">Multi-Region key replication</a> allow you to use the same key material across multiple Amazon Web Services Regions, providing lower latency for applications distributed across regions. When you add Replication Regions, Amazon Web Services Payment Cryptography securely replicates the key material to the specified Amazon Web Services Regions.</p> <p>The key must be in an active state to add Replication Regions. You can add multiple regions in a single operation, and the key will be available for use in those regions once replication is complete.</p> <p> <b>Cross-account use:</b> This operation supports cross-account use when the key has a resource-based policy that grants access. For more information, see <a href="https://docs.aws.amazon.com/payment-cryptography/latest/userguide/security_iam_resource-based-policies.html">Resource-based policies</a>.</p> <p> <b>Related operations:</b> </p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_RemoveKeyReplicationRegions.html">RemoveKeyReplicationRegions</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_EnableDefaultKeyReplicationRegions.html">EnableDefaultKeyReplicationRegions</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_GetDefaultKeyReplicationRegions.html">GetDefaultKeyReplicationRegions</a> </p> </li> </ul>

        Args:
            key_identifier: <p>The key identifier (ARN or alias) of the key for which to add replication regions.</p> <p>This key must exist and be in a valid state for replication operations.</p>
            replication_regions: <p>The list of Amazon Web Services Regions to add to the key's replication configuration.</p> <p>Each region must be a valid Amazon Web Services Region where Amazon Web Services Payment Cryptography is available. The key will be replicated to these regions, allowing cryptographic operations to be performed closer to your applications.</p>

        Raises:
            capo_payment_cryptography.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p> <p>This exception is thrown when the caller lacks the necessary IAM permissions to perform the requested operation. Verify that your IAM policy includes the required permissions for the specific Amazon Web Services Payment Cryptography action you're attempting.</p>
            capo_payment_cryptography.errors.conflict_exception.ConflictException: <p>This request can cause an inconsistent state for the resource.</p> <p>The requested operation conflicts with the current state of the resource. For example, attempting to delete a key that is currently being used, or trying to create a resource that already exists.</p>
            capo_payment_cryptography.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception, or failure.</p> <p>This indicates a server-side error within the Amazon Web Services Payment Cryptography service. If this error persists, contact support for assistance.</p>
            capo_payment_cryptography.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request was denied due to resource not found.</p> <p>The specified key, alias, or other resource does not exist in your account or region. Verify that the resource identifier is correct and that the resource exists in the expected region.</p>
            capo_payment_cryptography.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>This request would cause a service quota to be exceeded.</p> <p>You have reached the maximum number of keys, aliases, or other resources allowed in your account. Review your current usage and consider deleting unused resources or requesting a quota increase.</p>
            capo_payment_cryptography.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p> <p>You have exceeded the rate limits for Amazon Web Services Payment Cryptography API calls. Implement exponential backoff and retry logic in your application to handle throttling gracefully.</p>
            capo_payment_cryptography.errors.validation_exception.ValidationException: <p>The request was denied due to an invalid request error.</p> <p>One or more parameters in your request are invalid. Check the parameter values, formats, and constraints specified in the API documentation.</p>
            capo_payment_cryptography.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_payment_cryptography.types.add_key_replication_regions_input.AddKeyReplicationRegionsInput]",
        ) -> OperationResponse[
            "capo_payment_cryptography.types.add_key_replication_regions_output.AddKeyReplicationRegionsOutput"
        ]:
            import capo_payment_cryptography._operations.payment_cryptography_control_plane.add_key_replication_regions

            output, http_response = (
                capo_payment_cryptography._operations.payment_cryptography_control_plane.add_key_replication_regions.add_key_replication_regions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_payment_cryptography.types.add_key_replication_regions_input.AddKeyReplicationRegionsInput = {
            "key_identifier": key_identifier,
            "replication_regions": replication_regions,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def remove_key_replication_regions(
        self,
        key_identifier: "capo_payment_cryptography.types.key_arn_or_key_alias_type.KeyArnOrKeyAliasType",
        replication_regions: "capo_payment_cryptography.types.regions.Regions",
        *,
        config_overrides: Optional[PaymentCryptographyClientConfig] = None,
    ) -> "capo_payment_cryptography.types.remove_key_replication_regions_output.RemoveKeyReplicationRegionsOutput":
        """<p>Removes Replication Regions from an existing Amazon Web Services Payment Cryptography key, disabling the key's availability for cryptographic operations in the specified Amazon Web Services Regions.</p> <p>When you remove Replication Regions, the key material is securely deleted from those regions and can no longer be used for cryptographic operations there. This operation is irreversible for the specified Amazon Web Services Regions. For more information, see <a href="https://docs.aws.amazon.com/payment-cryptography/latest/userguide/keys-multi-region-replication.html">Multi-Region key replication</a>.</p> <important> <p>Ensure that no active cryptographic operations or applications depend on the key in the regions you're removing before performing this operation.</p> </important> <p> <b>Cross-account use:</b> This operation supports cross-account use when the key has a resource-based policy that grants access. For more information, see <a href="https://docs.aws.amazon.com/payment-cryptography/latest/userguide/security_iam_resource-based-policies.html">Resource-based policies</a>.</p> <p> <b>Related operations:</b> </p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_AddKeyReplicationRegions.html">AddKeyReplicationRegions</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_DisableDefaultKeyReplicationRegions.html">DisableDefaultKeyReplicationRegions</a> </p> </li> </ul>

        Args:
            key_identifier: <p>The key identifier (ARN or alias) of the key from which to remove replication regions.</p> <p>This key must exist and have replication enabled in the specified regions.</p>
            replication_regions: <p>The list of Amazon Web Services Regions to remove from the key's replication configuration.</p> <p>The key will no longer be available for cryptographic operations in these regions after removal. Ensure no active operations depend on the key in these regions before removal.</p>

        Raises:
            capo_payment_cryptography.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p> <p>This exception is thrown when the caller lacks the necessary IAM permissions to perform the requested operation. Verify that your IAM policy includes the required permissions for the specific Amazon Web Services Payment Cryptography action you're attempting.</p>
            capo_payment_cryptography.errors.conflict_exception.ConflictException: <p>This request can cause an inconsistent state for the resource.</p> <p>The requested operation conflicts with the current state of the resource. For example, attempting to delete a key that is currently being used, or trying to create a resource that already exists.</p>
            capo_payment_cryptography.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception, or failure.</p> <p>This indicates a server-side error within the Amazon Web Services Payment Cryptography service. If this error persists, contact support for assistance.</p>
            capo_payment_cryptography.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request was denied due to resource not found.</p> <p>The specified key, alias, or other resource does not exist in your account or region. Verify that the resource identifier is correct and that the resource exists in the expected region.</p>
            capo_payment_cryptography.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>This request would cause a service quota to be exceeded.</p> <p>You have reached the maximum number of keys, aliases, or other resources allowed in your account. Review your current usage and consider deleting unused resources or requesting a quota increase.</p>
            capo_payment_cryptography.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p> <p>You have exceeded the rate limits for Amazon Web Services Payment Cryptography API calls. Implement exponential backoff and retry logic in your application to handle throttling gracefully.</p>
            capo_payment_cryptography.errors.validation_exception.ValidationException: <p>The request was denied due to an invalid request error.</p> <p>One or more parameters in your request are invalid. Check the parameter values, formats, and constraints specified in the API documentation.</p>
            capo_payment_cryptography.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_payment_cryptography.types.remove_key_replication_regions_input.RemoveKeyReplicationRegionsInput]",
        ) -> OperationResponse[
            "capo_payment_cryptography.types.remove_key_replication_regions_output.RemoveKeyReplicationRegionsOutput"
        ]:
            import capo_payment_cryptography._operations.payment_cryptography_control_plane.remove_key_replication_regions

            output, http_response = (
                capo_payment_cryptography._operations.payment_cryptography_control_plane.remove_key_replication_regions.remove_key_replication_regions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_payment_cryptography.types.remove_key_replication_regions_input.RemoveKeyReplicationRegionsInput = {
            "key_identifier": key_identifier,
            "replication_regions": replication_regions,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def restore_key(
        self,
        key_identifier: "capo_payment_cryptography.types.key_arn_or_key_alias_type.KeyArnOrKeyAliasType",
        *,
        config_overrides: Optional[PaymentCryptographyClientConfig] = None,
    ) -> "capo_payment_cryptography.types.restore_key_output.RestoreKeyOutput":
        """<p>Cancels a scheduled key deletion during the waiting period. Use this operation to restore a <code>Key</code> that is scheduled for deletion.</p> <p>During the waiting period, the <code>KeyState</code> is <code>DELETE_PENDING</code> and <code>deletePendingTimestamp</code> contains the date and time after which the <code>Key</code> will be deleted. After <code>Key</code> is restored, the <code>KeyState</code> is <code>CREATE_COMPLETE</code>, and the value for <code>deletePendingTimestamp</code> is removed.</p> <p> <b>Cross-account use:</b> This operation supports cross-account use when the key has a resource-based policy that grants access. For more information, see <a href="https://docs.aws.amazon.com/payment-cryptography/latest/userguide/security_iam_resource-based-policies.html">Resource-based policies</a>.</p> <p> <b>Related operations:</b> </p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_DeleteKey.html">DeleteKey</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_StartKeyUsage.html">StartKeyUsage</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_StopKeyUsage.html">StopKeyUsage</a> </p> </li> </ul>

        Args:
            key_identifier: <p>The <code>KeyARN</code> of the key to be restored within Amazon Web Services Payment Cryptography.</p>

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
            req: "OperationRequest[capo_payment_cryptography.types.restore_key_input.RestoreKeyInput]",
        ) -> OperationResponse[
            "capo_payment_cryptography.types.restore_key_output.RestoreKeyOutput"
        ]:
            import capo_payment_cryptography._operations.payment_cryptography_control_plane.restore_key

            output, http_response = (
                capo_payment_cryptography._operations.payment_cryptography_control_plane.restore_key.restore_key(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_payment_cryptography.types.restore_key_input.RestoreKeyInput = {
            "key_identifier": key_identifier
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def start_key_usage(
        self,
        key_identifier: "capo_payment_cryptography.types.key_arn_or_key_alias_type.KeyArnOrKeyAliasType",
        *,
        config_overrides: Optional[PaymentCryptographyClientConfig] = None,
    ) -> "capo_payment_cryptography.types.start_key_usage_output.StartKeyUsageOutput":
        """<p>Enables an Amazon Web Services Payment Cryptography key, which makes it active for cryptographic operations within Amazon Web Services Payment Cryptography</p> <p> <b>Cross-account use:</b> This operation supports cross-account use when the key has a resource-based policy that grants access. For more information, see <a href="https://docs.aws.amazon.com/payment-cryptography/latest/userguide/security_iam_resource-based-policies.html">Resource-based policies</a>.</p> <p> <b>Related operations:</b> </p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_StopKeyUsage.html">StopKeyUsage</a> </p> </li> </ul>

        Args:
            key_identifier: <p>The <code>KeyArn</code> of the key.</p>

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
            req: "OperationRequest[capo_payment_cryptography.types.start_key_usage_input.StartKeyUsageInput]",
        ) -> OperationResponse[
            "capo_payment_cryptography.types.start_key_usage_output.StartKeyUsageOutput"
        ]:
            import capo_payment_cryptography._operations.payment_cryptography_control_plane.start_key_usage

            output, http_response = (
                capo_payment_cryptography._operations.payment_cryptography_control_plane.start_key_usage.start_key_usage(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_payment_cryptography.types.start_key_usage_input.StartKeyUsageInput = {
            "key_identifier": key_identifier
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def stop_key_usage(
        self,
        key_identifier: "capo_payment_cryptography.types.key_arn_or_key_alias_type.KeyArnOrKeyAliasType",
        *,
        config_overrides: Optional[PaymentCryptographyClientConfig] = None,
    ) -> "capo_payment_cryptography.types.stop_key_usage_output.StopKeyUsageOutput":
        """<p>Disables an Amazon Web Services Payment Cryptography key, which makes it inactive within Amazon Web Services Payment Cryptography.</p> <p>You can use this operation instead of <a href="https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_DeleteKey.html">DeleteKey</a> to deactivate a key. You can enable the key in the future by calling <a href="https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_StartKeyUsage.html">StartKeyUsage</a>.</p> <p> <b>Cross-account use:</b> This operation supports cross-account use when the key has a resource-based policy that grants access. For more information, see <a href="https://docs.aws.amazon.com/payment-cryptography/latest/userguide/security_iam_resource-based-policies.html">Resource-based policies</a>.</p> <p> <b>Related operations:</b> </p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_DeleteKey.html">DeleteKey</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_StartKeyUsage.html">StartKeyUsage</a> </p> </li> </ul>

        Args:
            key_identifier: <p>The <code>KeyArn</code> of the key.</p>

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
            req: "OperationRequest[capo_payment_cryptography.types.stop_key_usage_input.StopKeyUsageInput]",
        ) -> OperationResponse[
            "capo_payment_cryptography.types.stop_key_usage_output.StopKeyUsageOutput"
        ]:
            import capo_payment_cryptography._operations.payment_cryptography_control_plane.stop_key_usage

            output, http_response = (
                capo_payment_cryptography._operations.payment_cryptography_control_plane.stop_key_usage.stop_key_usage(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_payment_cryptography.types.stop_key_usage_input.StopKeyUsageInput = {
            "key_identifier": key_identifier
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncKeyResource:
    def __init__(self, service: AsyncPaymentCryptographyClient) -> None:
        self._service = service

    async def create(
        self,
        key_attributes: "capo_payment_cryptography.types.key_attributes.KeyAttributes",
        exportable: bool,
        *,
        config_overrides: Optional[AsyncPaymentCryptographyClientConfig] = None,
        key_check_value_algorithm: Optional[
            "capo_payment_cryptography.types.key_check_value_algorithm.KeyCheckValueAlgorithm"
        ] = None,
        enabled: Optional[bool] = None,
        tags: Optional["capo_payment_cryptography.types.tags.Tags"] = None,
        derive_key_usage: Optional[
            "capo_payment_cryptography.types.derive_key_usage.DeriveKeyUsage"
        ] = None,
        replication_regions: Optional[
            "capo_payment_cryptography.types.regions.Regions"
        ] = None,
    ) -> "capo_payment_cryptography.types.create_key_output.CreateKeyOutput":
        """<p>Creates an Amazon Web Services Payment Cryptography key, a logical representation of a cryptographic key, that is unique in your account and Amazon Web Services Region. You use keys for cryptographic functions such as encryption and decryption. </p> <p>In addition to the key material used in cryptographic operations, an Amazon Web Services Payment Cryptography key includes metadata such as the key ARN, key usage, key origin, creation date, description, and key state.</p> <p>When you create a key, you specify both immutable and mutable data about the key. The immutable data contains key attributes that define the scope and cryptographic operations that you can perform using the key, for example key class (example: <code>SYMMETRIC_KEY</code>), key algorithm (example: <code>TDES_2KEY</code>), key usage (example: <code>TR31_P0_PIN_ENCRYPTION_KEY</code>) and key modes of use (example: <code>Encrypt</code>). Amazon Web Services Payment Cryptography binds key attributes to keys using key blocks when you store or export them. Amazon Web Services Payment Cryptography stores the key contents wrapped and never stores or transmits them in the clear.</p> <p>For information about valid combinations of key attributes, see <a href="https://docs.aws.amazon.com/payment-cryptography/latest/userguide/keys-validattributes.html">Understanding key attributes</a> in the <i>Amazon Web Services Payment Cryptography User Guide</i>. The mutable data contained within a key includes usage timestamp and key deletion timestamp and can be modified after creation.</p> <p>You can use the <code>CreateKey</code> operation to generate an ECC (Elliptic Curve Cryptography) key pair used for establishing an ECDH (Elliptic Curve Diffie-Hellman) key agreement between two parties. In the ECDH key agreement process, both parties generate their own ECC key pair with key usage K3 and exchange the public keys. Each party then use their private key, the received public key from the other party, and the key derivation parameters including key derivation function, hash algorithm, derivation data, and key algorithm to derive a shared key.</p> <p>To maintain the single-use principle of cryptographic keys in payments, ECDH derived keys should not be used for multiple purposes, such as a <code>TR31_P0_PIN_ENCRYPTION_KEY</code> and <code>TR31_K1_KEY_BLOCK_PROTECTION_KEY</code>. When creating ECC key pairs in Amazon Web Services Payment Cryptography you can optionally set the <code>DeriveKeyUsage</code> parameter, which defines the key usage bound to the symmetric key that will be derived using the ECC key pair.</p> <p> <b>Cross-account use</b>: This operation can't be used across different Amazon Web Services accounts.</p> <p> <b>Related operations:</b> </p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_DeleteKey.html">DeleteKey</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_GetKey.html">GetKey</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_ListKeys.html">ListKeys</a> </p> </li> </ul>

        Args:
            key_attributes: <p>The role of the key, the algorithm it supports, and the cryptographic operations allowed with the key. This data is immutable after the key is created.</p>
            key_check_value_algorithm: <p>The algorithm that Amazon Web Services Payment Cryptography uses to calculate the key check value (KCV). It is used to validate the key integrity.</p> <p>For TDES keys, the KCV is computed by encrypting 8 bytes, each with value of zero, with the key to be checked and retaining the 3 highest order bytes of the encrypted result. For AES keys, the KCV is computed using a CMAC algorithm where the input data is 16 bytes of zero and retaining the 3 highest order bytes of the encrypted result. For HMAC keys, the KCV is computed using the hash selected at key creation on a zero-length message, taking the leftmost 3 bytes.</p>
            exportable: <p>Specifies whether the key is exportable from the service.</p>
            enabled: <p>Specifies whether to enable the key. If the key is enabled, it is activated for use within the service. If the key is not enabled, then it is created but not activated. The default value is enabled.</p>
            tags: <p>Assigns one or more tags to the Amazon Web Services Payment Cryptography key. Use this parameter to tag a key when it is created. To tag an existing Amazon Web Services Payment Cryptography key, use the <a href="https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_TagResource.html">TagResource</a> operation.</p> <p>Each tag consists of a tag key and a tag value. Both the tag key and the tag value are required, but the tag value can be an empty (null) string. You can't have more than one tag on an Amazon Web Services Payment Cryptography key with the same tag key. </p> <important> <p>Don't include personal, confidential or sensitive information in this field. This field may be displayed in plaintext in CloudTrail logs and other output.</p> </important> <note> <p>Tagging or untagging an Amazon Web Services Payment Cryptography key can allow or deny permission to the key.</p> </note>
            derive_key_usage: <p>The intended cryptographic usage of keys derived from the ECC key pair to be created.</p> <p>After creating an ECC key pair, you cannot change the intended cryptographic usage of keys derived from it using ECDH.</p>

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
            req: "AsyncOperationRequest[capo_payment_cryptography.types.create_key_input.CreateKeyInput]",
        ) -> AsyncOperationResponse[
            "capo_payment_cryptography.types.create_key_output.CreateKeyOutput"
        ]:
            import capo_payment_cryptography._operations.payment_cryptography_control_plane.create_key

            (
                output,
                http_response,
            ) = await capo_payment_cryptography._operations.payment_cryptography_control_plane.create_key.async_create_key(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_payment_cryptography.types.create_key_input.CreateKeyInput = {
            "key_attributes": key_attributes,
            "exportable": exportable,
        }
        if key_check_value_algorithm is not None:
            input_["key_check_value_algorithm"] = key_check_value_algorithm
        if enabled is not None:
            input_["enabled"] = enabled
        if tags is not None:
            input_["tags"] = tags
        if derive_key_usage is not None:
            input_["derive_key_usage"] = derive_key_usage
        if replication_regions is not None:
            input_["replication_regions"] = replication_regions

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def read(
        self,
        key_identifier: "capo_payment_cryptography.types.key_arn_or_key_alias_type.KeyArnOrKeyAliasType",
        *,
        config_overrides: Optional[AsyncPaymentCryptographyClientConfig] = None,
    ) -> "capo_payment_cryptography.types.get_key_output.GetKeyOutput":
        """<p>Gets the key metadata for an Amazon Web Services Payment Cryptography key, including the immutable and mutable attributes specified when the key was created. Returns key metadata including attributes, state, and timestamps, but does not return the actual cryptographic key material.</p> <p> <b>Cross-account use:</b> This operation supports cross-account use when the key has a resource-based policy that grants access. For more information, see <a href="https://docs.aws.amazon.com/payment-cryptography/latest/userguide/security_iam_resource-based-policies.html">Resource-based policies</a>.</p> <p> <b>Related operations:</b> </p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_CreateKey.html">CreateKey</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_DeleteKey.html">DeleteKey</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_ListKeys.html">ListKeys</a> </p> </li> </ul>

        Args:
            key_identifier: <p>The <code>KeyARN</code> of the Amazon Web Services Payment Cryptography key.</p>

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
            req: "AsyncOperationRequest[capo_payment_cryptography.types.get_key_input.GetKeyInput]",
        ) -> AsyncOperationResponse[
            "capo_payment_cryptography.types.get_key_output.GetKeyOutput"
        ]:
            import capo_payment_cryptography._operations.payment_cryptography_control_plane.get_key

            (
                output,
                http_response,
            ) = await capo_payment_cryptography._operations.payment_cryptography_control_plane.get_key.async_get_key(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_payment_cryptography.types.get_key_input.GetKeyInput = {
            "key_identifier": key_identifier
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
        key_identifier: "capo_payment_cryptography.types.key_arn_or_key_alias_type.KeyArnOrKeyAliasType",
        *,
        config_overrides: Optional[AsyncPaymentCryptographyClientConfig] = None,
        delete_key_in_days: Optional[int] = None,
    ) -> "capo_payment_cryptography.types.delete_key_output.DeleteKeyOutput":
        """<p>Deletes the key material and metadata associated with Amazon Web Services Payment Cryptography key.</p> <p>Key deletion is irreversible. After a key is deleted, you can't perform cryptographic operations using the key. For example, you can't decrypt data that was encrypted by a deleted Amazon Web Services Payment Cryptography key, and the data may become unrecoverable. Because key deletion is destructive, Amazon Web Services Payment Cryptography has a safety mechanism to prevent accidental deletion of a key. When you call this operation, Amazon Web Services Payment Cryptography disables the specified key but doesn't delete it until after a waiting period set using <code>DeleteKeyInDays</code>. The default waiting period is 7 days. During the waiting period, the <code>KeyState</code> is <code>DELETE_PENDING</code>. After the key is deleted, the <code>KeyState</code> is <code>DELETE_COMPLETE</code>.</p> <p>You should delete a key only when you are sure that you don't need to use it anymore and no other parties are utilizing this key. If you aren't sure, consider deactivating it instead by calling <a href="https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_StopKeyUsage.html">StopKeyUsage</a>.</p> <p> <b>Cross-account use:</b> This operation supports cross-account use when the key has a resource-based policy that grants access. For more information, see <a href="https://docs.aws.amazon.com/payment-cryptography/latest/userguide/security_iam_resource-based-policies.html">Resource-based policies</a>.</p> <p> <b>Related operations:</b> </p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_RestoreKey.html">RestoreKey</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_StartKeyUsage.html">StartKeyUsage</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_StopKeyUsage.html">StopKeyUsage</a> </p> </li> </ul>

        Args:
            key_identifier: <p>The <code>KeyARN</code> of the key that is scheduled for deletion.</p>
            delete_key_in_days: <p>The waiting period for key deletion. The default value is seven days.</p>

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
            req: "AsyncOperationRequest[capo_payment_cryptography.types.delete_key_input.DeleteKeyInput]",
        ) -> AsyncOperationResponse[
            "capo_payment_cryptography.types.delete_key_output.DeleteKeyOutput"
        ]:
            import capo_payment_cryptography._operations.payment_cryptography_control_plane.delete_key

            (
                output,
                http_response,
            ) = await capo_payment_cryptography._operations.payment_cryptography_control_plane.delete_key.async_delete_key(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_payment_cryptography.types.delete_key_input.DeleteKeyInput = {
            "key_identifier": key_identifier
        }
        if delete_key_in_days is not None:
            input_["delete_key_in_days"] = delete_key_in_days

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
        key_state: Optional[
            "capo_payment_cryptography.types.key_state.KeyState"
        ] = None,
        next_token: Optional[
            "capo_payment_cryptography.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "capo_payment_cryptography.types.max_results.MaxResults"
        ] = None,
    ) -> "capo_payment_cryptography.types.list_keys_output.ListKeysOutput":
        """<p>Lists the keys in the caller's Amazon Web Services account and Amazon Web Services Region. You can filter the list of keys.</p> <p>This is a paginated operation, which means that each response might contain only a subset of all the keys. When the response contains only a subset of keys, it includes a <code>NextToken</code> value. Use this value in a subsequent <code>ListKeys</code> request to get more keys. When you receive a response with no NextToken (or an empty or null value), that means there are no more keys to get.</p> <p> <b>Cross-account use:</b> This operation can't be used across different Amazon Web Services accounts.</p> <p> <b>Related operations:</b> </p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_CreateKey.html">CreateKey</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_DeleteKey.html">DeleteKey</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_GetKey.html">GetKey</a> </p> </li> </ul>

        Args:
            key_state: <p>The key state of the keys you want to list.</p>
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
            req: "AsyncOperationRequest[capo_payment_cryptography.types.list_keys_input.ListKeysInput]",
        ) -> AsyncOperationResponse[
            "capo_payment_cryptography.types.list_keys_output.ListKeysOutput"
        ]:
            import capo_payment_cryptography._operations.payment_cryptography_control_plane.list_keys

            (
                output,
                http_response,
            ) = await capo_payment_cryptography._operations.payment_cryptography_control_plane.list_keys.async_list_keys(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_payment_cryptography.types.list_keys_input.ListKeysInput = {}
        if key_state is not None:
            input_["key_state"] = key_state
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

    async def add_key_replication_regions(
        self,
        key_identifier: "capo_payment_cryptography.types.key_arn_or_key_alias_type.KeyArnOrKeyAliasType",
        replication_regions: "capo_payment_cryptography.types.regions.Regions",
        *,
        config_overrides: Optional[AsyncPaymentCryptographyClientConfig] = None,
    ) -> "capo_payment_cryptography.types.add_key_replication_regions_output.AddKeyReplicationRegionsOutput":
        """<p>Adds replication Amazon Web Services Regions to an existing Amazon Web Services Payment Cryptography key, enabling the key to be used for cryptographic operations in additional Amazon Web Services Regions.</p> <p> <a href="https://docs.aws.amazon.com/payment-cryptography/latest/userguide/keys-multi-region-replication.html">Multi-Region key replication</a> allow you to use the same key material across multiple Amazon Web Services Regions, providing lower latency for applications distributed across regions. When you add Replication Regions, Amazon Web Services Payment Cryptography securely replicates the key material to the specified Amazon Web Services Regions.</p> <p>The key must be in an active state to add Replication Regions. You can add multiple regions in a single operation, and the key will be available for use in those regions once replication is complete.</p> <p> <b>Cross-account use:</b> This operation supports cross-account use when the key has a resource-based policy that grants access. For more information, see <a href="https://docs.aws.amazon.com/payment-cryptography/latest/userguide/security_iam_resource-based-policies.html">Resource-based policies</a>.</p> <p> <b>Related operations:</b> </p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_RemoveKeyReplicationRegions.html">RemoveKeyReplicationRegions</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_EnableDefaultKeyReplicationRegions.html">EnableDefaultKeyReplicationRegions</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_GetDefaultKeyReplicationRegions.html">GetDefaultKeyReplicationRegions</a> </p> </li> </ul>

        Args:
            key_identifier: <p>The key identifier (ARN or alias) of the key for which to add replication regions.</p> <p>This key must exist and be in a valid state for replication operations.</p>
            replication_regions: <p>The list of Amazon Web Services Regions to add to the key's replication configuration.</p> <p>Each region must be a valid Amazon Web Services Region where Amazon Web Services Payment Cryptography is available. The key will be replicated to these regions, allowing cryptographic operations to be performed closer to your applications.</p>

        Raises:
            capo_payment_cryptography.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p> <p>This exception is thrown when the caller lacks the necessary IAM permissions to perform the requested operation. Verify that your IAM policy includes the required permissions for the specific Amazon Web Services Payment Cryptography action you're attempting.</p>
            capo_payment_cryptography.errors.conflict_exception.ConflictException: <p>This request can cause an inconsistent state for the resource.</p> <p>The requested operation conflicts with the current state of the resource. For example, attempting to delete a key that is currently being used, or trying to create a resource that already exists.</p>
            capo_payment_cryptography.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception, or failure.</p> <p>This indicates a server-side error within the Amazon Web Services Payment Cryptography service. If this error persists, contact support for assistance.</p>
            capo_payment_cryptography.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request was denied due to resource not found.</p> <p>The specified key, alias, or other resource does not exist in your account or region. Verify that the resource identifier is correct and that the resource exists in the expected region.</p>
            capo_payment_cryptography.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>This request would cause a service quota to be exceeded.</p> <p>You have reached the maximum number of keys, aliases, or other resources allowed in your account. Review your current usage and consider deleting unused resources or requesting a quota increase.</p>
            capo_payment_cryptography.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p> <p>You have exceeded the rate limits for Amazon Web Services Payment Cryptography API calls. Implement exponential backoff and retry logic in your application to handle throttling gracefully.</p>
            capo_payment_cryptography.errors.validation_exception.ValidationException: <p>The request was denied due to an invalid request error.</p> <p>One or more parameters in your request are invalid. Check the parameter values, formats, and constraints specified in the API documentation.</p>
            capo_payment_cryptography.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_payment_cryptography.types.add_key_replication_regions_input.AddKeyReplicationRegionsInput]",
        ) -> AsyncOperationResponse[
            "capo_payment_cryptography.types.add_key_replication_regions_output.AddKeyReplicationRegionsOutput"
        ]:
            import capo_payment_cryptography._operations.payment_cryptography_control_plane.add_key_replication_regions

            (
                output,
                http_response,
            ) = await capo_payment_cryptography._operations.payment_cryptography_control_plane.add_key_replication_regions.async_add_key_replication_regions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_payment_cryptography.types.add_key_replication_regions_input.AddKeyReplicationRegionsInput = {
            "key_identifier": key_identifier,
            "replication_regions": replication_regions,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def remove_key_replication_regions(
        self,
        key_identifier: "capo_payment_cryptography.types.key_arn_or_key_alias_type.KeyArnOrKeyAliasType",
        replication_regions: "capo_payment_cryptography.types.regions.Regions",
        *,
        config_overrides: Optional[AsyncPaymentCryptographyClientConfig] = None,
    ) -> "capo_payment_cryptography.types.remove_key_replication_regions_output.RemoveKeyReplicationRegionsOutput":
        """<p>Removes Replication Regions from an existing Amazon Web Services Payment Cryptography key, disabling the key's availability for cryptographic operations in the specified Amazon Web Services Regions.</p> <p>When you remove Replication Regions, the key material is securely deleted from those regions and can no longer be used for cryptographic operations there. This operation is irreversible for the specified Amazon Web Services Regions. For more information, see <a href="https://docs.aws.amazon.com/payment-cryptography/latest/userguide/keys-multi-region-replication.html">Multi-Region key replication</a>.</p> <important> <p>Ensure that no active cryptographic operations or applications depend on the key in the regions you're removing before performing this operation.</p> </important> <p> <b>Cross-account use:</b> This operation supports cross-account use when the key has a resource-based policy that grants access. For more information, see <a href="https://docs.aws.amazon.com/payment-cryptography/latest/userguide/security_iam_resource-based-policies.html">Resource-based policies</a>.</p> <p> <b>Related operations:</b> </p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_AddKeyReplicationRegions.html">AddKeyReplicationRegions</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_DisableDefaultKeyReplicationRegions.html">DisableDefaultKeyReplicationRegions</a> </p> </li> </ul>

        Args:
            key_identifier: <p>The key identifier (ARN or alias) of the key from which to remove replication regions.</p> <p>This key must exist and have replication enabled in the specified regions.</p>
            replication_regions: <p>The list of Amazon Web Services Regions to remove from the key's replication configuration.</p> <p>The key will no longer be available for cryptographic operations in these regions after removal. Ensure no active operations depend on the key in these regions before removal.</p>

        Raises:
            capo_payment_cryptography.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p> <p>This exception is thrown when the caller lacks the necessary IAM permissions to perform the requested operation. Verify that your IAM policy includes the required permissions for the specific Amazon Web Services Payment Cryptography action you're attempting.</p>
            capo_payment_cryptography.errors.conflict_exception.ConflictException: <p>This request can cause an inconsistent state for the resource.</p> <p>The requested operation conflicts with the current state of the resource. For example, attempting to delete a key that is currently being used, or trying to create a resource that already exists.</p>
            capo_payment_cryptography.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception, or failure.</p> <p>This indicates a server-side error within the Amazon Web Services Payment Cryptography service. If this error persists, contact support for assistance.</p>
            capo_payment_cryptography.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request was denied due to resource not found.</p> <p>The specified key, alias, or other resource does not exist in your account or region. Verify that the resource identifier is correct and that the resource exists in the expected region.</p>
            capo_payment_cryptography.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>This request would cause a service quota to be exceeded.</p> <p>You have reached the maximum number of keys, aliases, or other resources allowed in your account. Review your current usage and consider deleting unused resources or requesting a quota increase.</p>
            capo_payment_cryptography.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p> <p>You have exceeded the rate limits for Amazon Web Services Payment Cryptography API calls. Implement exponential backoff and retry logic in your application to handle throttling gracefully.</p>
            capo_payment_cryptography.errors.validation_exception.ValidationException: <p>The request was denied due to an invalid request error.</p> <p>One or more parameters in your request are invalid. Check the parameter values, formats, and constraints specified in the API documentation.</p>
            capo_payment_cryptography.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_payment_cryptography.types.remove_key_replication_regions_input.RemoveKeyReplicationRegionsInput]",
        ) -> AsyncOperationResponse[
            "capo_payment_cryptography.types.remove_key_replication_regions_output.RemoveKeyReplicationRegionsOutput"
        ]:
            import capo_payment_cryptography._operations.payment_cryptography_control_plane.remove_key_replication_regions

            (
                output,
                http_response,
            ) = await capo_payment_cryptography._operations.payment_cryptography_control_plane.remove_key_replication_regions.async_remove_key_replication_regions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_payment_cryptography.types.remove_key_replication_regions_input.RemoveKeyReplicationRegionsInput = {
            "key_identifier": key_identifier,
            "replication_regions": replication_regions,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def restore_key(
        self,
        key_identifier: "capo_payment_cryptography.types.key_arn_or_key_alias_type.KeyArnOrKeyAliasType",
        *,
        config_overrides: Optional[AsyncPaymentCryptographyClientConfig] = None,
    ) -> "capo_payment_cryptography.types.restore_key_output.RestoreKeyOutput":
        """<p>Cancels a scheduled key deletion during the waiting period. Use this operation to restore a <code>Key</code> that is scheduled for deletion.</p> <p>During the waiting period, the <code>KeyState</code> is <code>DELETE_PENDING</code> and <code>deletePendingTimestamp</code> contains the date and time after which the <code>Key</code> will be deleted. After <code>Key</code> is restored, the <code>KeyState</code> is <code>CREATE_COMPLETE</code>, and the value for <code>deletePendingTimestamp</code> is removed.</p> <p> <b>Cross-account use:</b> This operation supports cross-account use when the key has a resource-based policy that grants access. For more information, see <a href="https://docs.aws.amazon.com/payment-cryptography/latest/userguide/security_iam_resource-based-policies.html">Resource-based policies</a>.</p> <p> <b>Related operations:</b> </p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_DeleteKey.html">DeleteKey</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_StartKeyUsage.html">StartKeyUsage</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_StopKeyUsage.html">StopKeyUsage</a> </p> </li> </ul>

        Args:
            key_identifier: <p>The <code>KeyARN</code> of the key to be restored within Amazon Web Services Payment Cryptography.</p>

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
            req: "AsyncOperationRequest[capo_payment_cryptography.types.restore_key_input.RestoreKeyInput]",
        ) -> AsyncOperationResponse[
            "capo_payment_cryptography.types.restore_key_output.RestoreKeyOutput"
        ]:
            import capo_payment_cryptography._operations.payment_cryptography_control_plane.restore_key

            (
                output,
                http_response,
            ) = await capo_payment_cryptography._operations.payment_cryptography_control_plane.restore_key.async_restore_key(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_payment_cryptography.types.restore_key_input.RestoreKeyInput = {
            "key_identifier": key_identifier
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def start_key_usage(
        self,
        key_identifier: "capo_payment_cryptography.types.key_arn_or_key_alias_type.KeyArnOrKeyAliasType",
        *,
        config_overrides: Optional[AsyncPaymentCryptographyClientConfig] = None,
    ) -> "capo_payment_cryptography.types.start_key_usage_output.StartKeyUsageOutput":
        """<p>Enables an Amazon Web Services Payment Cryptography key, which makes it active for cryptographic operations within Amazon Web Services Payment Cryptography</p> <p> <b>Cross-account use:</b> This operation supports cross-account use when the key has a resource-based policy that grants access. For more information, see <a href="https://docs.aws.amazon.com/payment-cryptography/latest/userguide/security_iam_resource-based-policies.html">Resource-based policies</a>.</p> <p> <b>Related operations:</b> </p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_StopKeyUsage.html">StopKeyUsage</a> </p> </li> </ul>

        Args:
            key_identifier: <p>The <code>KeyArn</code> of the key.</p>

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
            req: "AsyncOperationRequest[capo_payment_cryptography.types.start_key_usage_input.StartKeyUsageInput]",
        ) -> AsyncOperationResponse[
            "capo_payment_cryptography.types.start_key_usage_output.StartKeyUsageOutput"
        ]:
            import capo_payment_cryptography._operations.payment_cryptography_control_plane.start_key_usage

            (
                output,
                http_response,
            ) = await capo_payment_cryptography._operations.payment_cryptography_control_plane.start_key_usage.async_start_key_usage(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_payment_cryptography.types.start_key_usage_input.StartKeyUsageInput = {
            "key_identifier": key_identifier
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def stop_key_usage(
        self,
        key_identifier: "capo_payment_cryptography.types.key_arn_or_key_alias_type.KeyArnOrKeyAliasType",
        *,
        config_overrides: Optional[AsyncPaymentCryptographyClientConfig] = None,
    ) -> "capo_payment_cryptography.types.stop_key_usage_output.StopKeyUsageOutput":
        """<p>Disables an Amazon Web Services Payment Cryptography key, which makes it inactive within Amazon Web Services Payment Cryptography.</p> <p>You can use this operation instead of <a href="https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_DeleteKey.html">DeleteKey</a> to deactivate a key. You can enable the key in the future by calling <a href="https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_StartKeyUsage.html">StartKeyUsage</a>.</p> <p> <b>Cross-account use:</b> This operation supports cross-account use when the key has a resource-based policy that grants access. For more information, see <a href="https://docs.aws.amazon.com/payment-cryptography/latest/userguide/security_iam_resource-based-policies.html">Resource-based policies</a>.</p> <p> <b>Related operations:</b> </p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_DeleteKey.html">DeleteKey</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_StartKeyUsage.html">StartKeyUsage</a> </p> </li> </ul>

        Args:
            key_identifier: <p>The <code>KeyArn</code> of the key.</p>

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
            req: "AsyncOperationRequest[capo_payment_cryptography.types.stop_key_usage_input.StopKeyUsageInput]",
        ) -> AsyncOperationResponse[
            "capo_payment_cryptography.types.stop_key_usage_output.StopKeyUsageOutput"
        ]:
            import capo_payment_cryptography._operations.payment_cryptography_control_plane.stop_key_usage

            (
                output,
                http_response,
            ) = await capo_payment_cryptography._operations.payment_cryptography_control_plane.stop_key_usage.async_stop_key_usage(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_payment_cryptography.types.stop_key_usage_input.StopKeyUsageInput = {
            "key_identifier": key_identifier
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
