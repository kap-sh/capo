"""Generated from Smithy shape ``com.amazonaws.paymentcryptographydata#PaymentCryptographyDataPlane``."""

import warnings
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import AsyncBaseHandler, AsyncClient

import capo_payment_cryptography_data._auth._signers
import capo_payment_cryptography_data._auth._sigv4
from capo_payment_cryptography_data._auth._identity import Credentials
from capo_payment_cryptography_data._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_payment_cryptography_data._auth._zapros_handler import AuthMiddleware
from capo_payment_cryptography_data._services._aws_config import aaws_config
from capo_payment_cryptography_data._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import capo_payment_cryptography_data.types.as2805_kek_validation_type
    import capo_payment_cryptography_data.types.as2805_pek_derivation_attributes
    import capo_payment_cryptography_data.types.auth_request_cryptogram_type
    import capo_payment_cryptography_data.types.card_generation_attributes
    import capo_payment_cryptography_data.types.card_verification_attributes
    import capo_payment_cryptography_data.types.cipher_text_type
    import capo_payment_cryptography_data.types.command_message_data_type
    import capo_payment_cryptography_data.types.cryptogram_auth_response
    import capo_payment_cryptography_data.types.decrypt_data_input
    import capo_payment_cryptography_data.types.decrypt_data_output
    import capo_payment_cryptography_data.types.derivation_method_attributes
    import capo_payment_cryptography_data.types.dukpt_attributes
    import capo_payment_cryptography_data.types.dukpt_derivation_attributes
    import capo_payment_cryptography_data.types.encrypt_data_input
    import capo_payment_cryptography_data.types.encrypt_data_output
    import capo_payment_cryptography_data.types.encrypted_pin_block_type
    import capo_payment_cryptography_data.types.encryption_decryption_attributes
    import capo_payment_cryptography_data.types.generate_as2805_kek_validation_input
    import capo_payment_cryptography_data.types.generate_as2805_kek_validation_output
    import capo_payment_cryptography_data.types.generate_auth_request_cryptogram_input
    import capo_payment_cryptography_data.types.generate_auth_request_cryptogram_output
    import capo_payment_cryptography_data.types.generate_card_validation_data_input
    import capo_payment_cryptography_data.types.generate_card_validation_data_output
    import capo_payment_cryptography_data.types.generate_mac_emv_pin_change_input
    import capo_payment_cryptography_data.types.generate_mac_emv_pin_change_output
    import capo_payment_cryptography_data.types.generate_mac_input
    import capo_payment_cryptography_data.types.generate_mac_output
    import capo_payment_cryptography_data.types.generate_pin_data_input
    import capo_payment_cryptography_data.types.generate_pin_data_output
    import capo_payment_cryptography_data.types.hex_even_length_between16_and32
    import capo_payment_cryptography_data.types.incoming_key_material
    import capo_payment_cryptography_data.types.integer_range_between3_and5_type
    import capo_payment_cryptography_data.types.integer_range_between4_and12
    import capo_payment_cryptography_data.types.integer_range_between4_and32
    import capo_payment_cryptography_data.types.key_arn_or_key_alias_type
    import capo_payment_cryptography_data.types.key_check_value_algorithm
    import capo_payment_cryptography_data.types.mac_attributes
    import capo_payment_cryptography_data.types.mac_type
    import capo_payment_cryptography_data.types.major_key_derivation_mode
    import capo_payment_cryptography_data.types.message_data_type
    import capo_payment_cryptography_data.types.outgoing_key_material
    import capo_payment_cryptography_data.types.pin_block_format_for_emv_pin_change
    import capo_payment_cryptography_data.types.pin_block_format_for_pin_data
    import capo_payment_cryptography_data.types.pin_block_length_equals16
    import capo_payment_cryptography_data.types.pin_generation_attributes
    import capo_payment_cryptography_data.types.pin_verification_attributes
    import capo_payment_cryptography_data.types.plain_text_type
    import capo_payment_cryptography_data.types.primary_account_number_type
    import capo_payment_cryptography_data.types.random_key_send_variant_mask
    import capo_payment_cryptography_data.types.re_encrypt_data_input
    import capo_payment_cryptography_data.types.re_encrypt_data_output
    import capo_payment_cryptography_data.types.re_encryption_attributes
    import capo_payment_cryptography_data.types.session_key_derivation
    import capo_payment_cryptography_data.types.transaction_data_type
    import capo_payment_cryptography_data.types.translate_key_material_input
    import capo_payment_cryptography_data.types.translate_key_material_output
    import capo_payment_cryptography_data.types.translate_pin_data_input
    import capo_payment_cryptography_data.types.translate_pin_data_output
    import capo_payment_cryptography_data.types.translation_iso_formats
    import capo_payment_cryptography_data.types.validation_data_type
    import capo_payment_cryptography_data.types.verify_auth_request_cryptogram_input
    import capo_payment_cryptography_data.types.verify_auth_request_cryptogram_output
    import capo_payment_cryptography_data.types.verify_card_validation_data_input
    import capo_payment_cryptography_data.types.verify_card_validation_data_output
    import capo_payment_cryptography_data.types.verify_mac_input
    import capo_payment_cryptography_data.types.verify_mac_output
    import capo_payment_cryptography_data.types.verify_pin_data_input
    import capo_payment_cryptography_data.types.verify_pin_data_output
    import capo_payment_cryptography_data.types.wrapped_key


class AsyncPaymentCryptographyDataClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class AsyncPaymentCryptographyDataClient:
    """A client for the ``PaymentCryptographyData`` service.

    Args:
        http_handler: HTTP handler for sending requests. If not provided, creates a default handler.
        operation_interceptors: Interceptors that wrap every operation call. If not provided, defaults to an empty list.
        retry_max_attempts: Maximum number of times to retry a failed operation. Defaults to 3.
        region: The value of the ``AWS::Region`` endpoint parameter.
        use_dual_stack: The value of the ``AWS::UseDualStack`` endpoint parameter.
        use_fips: The value of the ``AWS::UseFIPS`` endpoint parameter.
        endpoint: The value of the ``SDK::Endpoint`` endpoint parameter.
        credentials: AWS credentials for request signing.
        credentials_provider: Provider that resolves AWS credentials. Takes precedence over ``credentials``.
    """

    def __init__(
        self,
        http_handler: AsyncBaseHandler | None = None,
        operation_interceptors: Iterable[AsyncInterceptor[Any, Any]] | None = None,
        retry_max_attempts: int | None = None,
        region: str | None = None,
        use_dual_stack: bool | None = None,
        use_fips: bool | None = None,
        endpoint: str | None = None,
        credentials: Credentials | None = None,
        credentials_provider: CredentialsProvider | None = None,
    ):
        self._client = AsyncClient(http_handler).wrap_with_middleware(
            lambda next: AuthMiddleware(next)
        )
        if credentials is not None and credentials_provider is not None:
            warnings.warn(
                "Both credentials and credentials_provider given; provider takes precedence"
            )
        resolved_credentials_provider: IdentityProvider[Credentials] | None = (
            credentials_provider
        )
        if resolved_credentials_provider is None and credentials is not None:
            resolved_credentials_provider = StaticAwsCredentialsProvider(credentials)
        if resolved_credentials_provider is None and credentials is None:
            resolved_credentials_provider = default_aws_credentials_chain(
                AsyncClient(http_handler)
            )
        self._config = AsyncPaymentCryptographyDataClientConfig(
            {
                "operation_interceptors": operation_interceptors or [],
                "retry_max_attempts": retry_max_attempts,
                "region": region,
                "use_dual_stack": use_dual_stack,
                "use_fips": use_fips,
                "endpoint": endpoint,
                "credentials_provider": resolved_credentials_provider,
            }
        )

    def operation_options(
        self,
        config_overrides: Optional[AsyncPaymentCryptographyDataClientConfig] = None,
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncPaymentCryptographyDataClientConfig = config_overrides or {}
        interceptors_: list[AsyncInterceptor[Any, Any]] = [
            *overrides.get(
                "operation_interceptors", self._config.get("operation_interceptors", [])
            ),
            aaws_config(),
            aretry(),
        ]
        options_: AsyncOperationOptions = AsyncOperationOptions(
            client=self._client,
            retry_max_attempts=overrides.get(
                "retry_max_attempts", self._config.get("retry_max_attempts")
            ),
            region=overrides.get("region", self._config.get("region")),
            use_dual_stack=overrides.get(
                "use_dual_stack", self._config.get("use_dual_stack")
            ),
            use_fips=overrides.get("use_fips", self._config.get("use_fips")),
            endpoint=overrides.get("endpoint", self._config.get("endpoint")),
            credentials_provider=overrides.get(
                "credentials_provider", self._config.get("credentials_provider")
            ),
        )
        return interceptors_, options_

    async def decrypt_data(
        self,
        key_identifier: "capo_payment_cryptography_data.types.key_arn_or_key_alias_type.KeyArnOrKeyAliasType",
        cipher_text: "capo_payment_cryptography_data.types.cipher_text_type.CipherTextType",
        decryption_attributes: "capo_payment_cryptography_data.types.encryption_decryption_attributes.EncryptionDecryptionAttributes",
        *,
        config_overrides: Optional[AsyncPaymentCryptographyDataClientConfig] = None,
        wrapped_key: Optional[
            "capo_payment_cryptography_data.types.wrapped_key.WrappedKey"
        ] = None,
    ) -> "capo_payment_cryptography_data.types.decrypt_data_output.DecryptDataOutput":
        """<p>Decrypts ciphertext data to plaintext using a symmetric (TDES, AES), asymmetric (RSA), or derived (DUKPT or EMV) encryption key scheme. For more information, see <a href="https://docs.aws.amazon.com/payment-cryptography/latest/userguide/decrypt-data.html">Decrypt data</a> in the <i>Amazon Web Services Payment Cryptography User Guide</i>.</p> <p>You can use an decryption key generated within Amazon Web Services Payment Cryptography, or you can import your own decryption key by calling <a href="https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_ImportKey.html">ImportKey</a>. For this operation, the key must have <code>KeyModesOfUse</code> set to <code>Decrypt</code>. In asymmetric decryption, Amazon Web Services Payment Cryptography decrypts the ciphertext using the private component of the asymmetric encryption key pair. For data encryption outside of Amazon Web Services Payment Cryptography, you can export the public component of the asymmetric key pair by calling <a href="https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_GetPublicKeyCertificate.html">GetPublicCertificate</a>.</p> <p>This operation also supports dynamic keys, allowing you to pass a dynamic decryption key as a TR-31 WrappedKeyBlock. This can be used when key material is frequently rotated, such as during every card transaction, and there is need to avoid importing short-lived keys into Amazon Web Services Payment Cryptography. To decrypt using dynamic keys, the <code>keyARN</code> is the Key Encryption Key (KEK) of the TR-31 wrapped decryption key material. The incoming wrapped key shall have a key purpose of D0 with a mode of use of B or D. For more information, see <a href="https://docs.aws.amazon.com/payment-cryptography/latest/userguide/use-cases-acquirers-dynamickeys.html">Using Dynamic Keys</a> in the <i>Amazon Web Services Payment Cryptography User Guide</i>.</p> <p>For symmetric and DUKPT decryption, Amazon Web Services Payment Cryptography supports <code>TDES</code> and <code>AES</code> algorithms. For EMV decryption, Amazon Web Services Payment Cryptography supports <code>TDES</code> algorithms. For asymmetric decryption, Amazon Web Services Payment Cryptography supports <code>RSA</code>. </p> <p>When you use TDES or TDES DUKPT, the ciphertext data length must be a multiple of 8 bytes. For AES or AES DUKPT, the ciphertext data length must be a multiple of 16 bytes. For RSA, it sould be equal to the key size unless padding is enabled.</p> <p>For information about valid keys for this operation, see <a href="https://docs.aws.amazon.com/payment-cryptography/latest/userguide/keys-validattributes.html">Understanding key attributes</a> and <a href="https://docs.aws.amazon.com/payment-cryptography/latest/userguide/crypto-ops-validkeys-ops.html">Key types for specific data operations</a> in the <i>Amazon Web Services Payment Cryptography User Guide</i>. </p> <p> <b>Cross-account use</b>: This operation supports cross-account use when the key has a resource-based policy that grants access. For more information, see <a href="https://docs.aws.amazon.com/payment-cryptography/latest/userguide/security_iam_resource-based-policies.html">Resource-based policies</a>.</p> <p> <b>Related operations:</b> </p> <ul> <li> <p> <a>EncryptData</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_GetPublicKeyCertificate.html">GetPublicCertificate</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_ImportKey.html">ImportKey</a> </p> </li> </ul>

        Args:
            key_identifier: <p>The <code>keyARN</code> of the encryption key that Amazon Web Services Payment Cryptography uses for ciphertext decryption.</p> <p>When a WrappedKeyBlock is provided, this value will be the identifier to the key wrapping key. Otherwise, it is the key identifier used to perform the operation.</p>
            cipher_text: <p>The ciphertext to decrypt.</p>
            decryption_attributes: <p>The encryption key type and attributes for ciphertext decryption.</p>
            wrapped_key: <p>The WrappedKeyBlock containing the encryption key for ciphertext decryption.</p>

        Raises:
            capo_payment_cryptography_data.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_payment_cryptography_data.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception, or failure.</p>
            capo_payment_cryptography_data.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request was denied due to an invalid resource error.</p>
            capo_payment_cryptography_data.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_payment_cryptography_data.errors.validation_exception.ValidationException: <p>The request was denied due to an invalid request error.</p>
            capo_payment_cryptography_data.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_payment_cryptography_data.types.decrypt_data_input.DecryptDataInput]",
        ) -> AsyncOperationResponse[
            "capo_payment_cryptography_data.types.decrypt_data_output.DecryptDataOutput"
        ]:
            import capo_payment_cryptography_data._operations.payment_cryptography_data_plane.decrypt_data

            (
                output,
                http_response,
            ) = await capo_payment_cryptography_data._operations.payment_cryptography_data_plane.decrypt_data.async_decrypt_data(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_payment_cryptography_data.types.decrypt_data_input.DecryptDataInput = {
            "key_identifier": key_identifier,
            "cipher_text": cipher_text,
            "decryption_attributes": decryption_attributes,
        }
        if wrapped_key is not None:
            input_["wrapped_key"] = wrapped_key

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def encrypt_data(
        self,
        key_identifier: "capo_payment_cryptography_data.types.key_arn_or_key_alias_type.KeyArnOrKeyAliasType",
        plain_text: "capo_payment_cryptography_data.types.plain_text_type.PlainTextType",
        encryption_attributes: "capo_payment_cryptography_data.types.encryption_decryption_attributes.EncryptionDecryptionAttributes",
        *,
        config_overrides: Optional[AsyncPaymentCryptographyDataClientConfig] = None,
        wrapped_key: Optional[
            "capo_payment_cryptography_data.types.wrapped_key.WrappedKey"
        ] = None,
    ) -> "capo_payment_cryptography_data.types.encrypt_data_output.EncryptDataOutput":
        """<p>Encrypts plaintext data to ciphertext using a symmetric (TDES, AES), asymmetric (RSA), or derived (DUKPT or EMV) encryption key scheme. For more information, see <a href="https://docs.aws.amazon.com/payment-cryptography/latest/userguide/encrypt-data.html">Encrypt data</a> in the <i>Amazon Web Services Payment Cryptography User Guide</i>.</p> <p>You can generate an encryption key within Amazon Web Services Payment Cryptography by calling <a href="https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_CreateKey.html">CreateKey</a>. You can import your own encryption key by calling <a href="https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_ImportKey.html">ImportKey</a>.</p> <p>For this operation, the key must have <code>KeyModesOfUse</code> set to <code>Encrypt</code>. In asymmetric encryption, plaintext is encrypted using public component. You can import the public component of an asymmetric key pair created outside Amazon Web Services Payment Cryptography by calling <a href="https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_ImportKey.html">ImportKey</a>. </p> <p>This operation also supports dynamic keys, allowing you to pass a dynamic encryption key as a TR-31 WrappedKeyBlock. This can be used when key material is frequently rotated, such as during every card transaction, and there is need to avoid importing short-lived keys into Amazon Web Services Payment Cryptography. To encrypt using dynamic keys, the <code>keyARN</code> is the Key Encryption Key (KEK) of the TR-31 wrapped encryption key material. The incoming wrapped key shall have a key purpose of D0 with a mode of use of B or D. For more information, see <a href="https://docs.aws.amazon.com/payment-cryptography/latest/userguide/use-cases-acquirers-dynamickeys.html">Using Dynamic Keys</a> in the <i>Amazon Web Services Payment Cryptography User Guide</i>.</p> <p>For symmetric and DUKPT encryption, Amazon Web Services Payment Cryptography supports <code>TDES</code> and <code>AES</code> algorithms. For EMV encryption, Amazon Web Services Payment Cryptography supports <code>TDES</code> algorithms.For asymmetric encryption, Amazon Web Services Payment Cryptography supports <code>RSA</code>. </p> <p>When you use TDES or TDES DUKPT, the plaintext data length must be a multiple of 8 bytes. For AES or AES DUKPT, the plaintext data length must be a multiple of 16 bytes. For RSA, it sould be equal to the key size unless padding is enabled.</p> <p>To encrypt using DUKPT, you must already have a BDK (Base Derivation Key) key in your account with <code>KeyModesOfUse</code> set to <code>DeriveKey</code>, or you can generate a new DUKPT key by calling <a href="https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_CreateKey.html">CreateKey</a>. To encrypt using EMV, you must already have an IMK (Issuer Master Key) key in your account with <code>KeyModesOfUse</code> set to <code>DeriveKey</code>.</p> <p>For information about valid keys for this operation, see <a href="https://docs.aws.amazon.com/payment-cryptography/latest/userguide/keys-validattributes.html">Understanding key attributes</a> and <a href="https://docs.aws.amazon.com/payment-cryptography/latest/userguide/crypto-ops-validkeys-ops.html">Key types for specific data operations</a> in the <i>Amazon Web Services Payment Cryptography User Guide</i>.</p> <p> <b>Cross-account use</b>: This operation supports cross-account use when the key has a resource-based policy that grants access. For more information, see <a href="https://docs.aws.amazon.com/payment-cryptography/latest/userguide/security_iam_resource-based-policies.html">Resource-based policies</a>.</p> <p> <b>Related operations:</b> </p> <ul> <li> <p> <a>DecryptData</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_GetPublicKeyCertificate.html">GetPublicCertificate</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_ImportKey.html">ImportKey</a> </p> </li> <li> <p> <a>ReEncryptData</a> </p> </li> </ul>

        Args:
            key_identifier: <p>The <code>keyARN</code> of the encryption key that Amazon Web Services Payment Cryptography uses for plaintext encryption.</p> <p>When a WrappedKeyBlock is provided, this value will be the identifier to the key wrapping key. Otherwise, it is the key identifier used to perform the operation.</p>
            plain_text: <p>The plaintext to be encrypted.</p> <note> <p>For encryption using asymmetric keys, plaintext data length is constrained by encryption key strength that you define in <code>KeyAlgorithm</code> and padding type that you define in <code>AsymmetricEncryptionAttributes</code>. For more information, see <a href="https://docs.aws.amazon.com/payment-cryptography/latest/userguide/encrypt-data.html">Encrypt data</a> in the <i>Amazon Web Services Payment Cryptography User Guide</i>.</p> </note>
            encryption_attributes: <p>The encryption key type and attributes for plaintext encryption.</p>
            wrapped_key: <p>The WrappedKeyBlock containing the encryption key for plaintext encryption.</p>

        Raises:
            capo_payment_cryptography_data.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_payment_cryptography_data.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception, or failure.</p>
            capo_payment_cryptography_data.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request was denied due to an invalid resource error.</p>
            capo_payment_cryptography_data.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_payment_cryptography_data.errors.validation_exception.ValidationException: <p>The request was denied due to an invalid request error.</p>
            capo_payment_cryptography_data.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_payment_cryptography_data.types.encrypt_data_input.EncryptDataInput]",
        ) -> AsyncOperationResponse[
            "capo_payment_cryptography_data.types.encrypt_data_output.EncryptDataOutput"
        ]:
            import capo_payment_cryptography_data._operations.payment_cryptography_data_plane.encrypt_data

            (
                output,
                http_response,
            ) = await capo_payment_cryptography_data._operations.payment_cryptography_data_plane.encrypt_data.async_encrypt_data(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_payment_cryptography_data.types.encrypt_data_input.EncryptDataInput = {
            "key_identifier": key_identifier,
            "plain_text": plain_text,
            "encryption_attributes": encryption_attributes,
        }
        if wrapped_key is not None:
            input_["wrapped_key"] = wrapped_key

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def generate_as2805_kek_validation(
        self,
        key_identifier: "capo_payment_cryptography_data.types.key_arn_or_key_alias_type.KeyArnOrKeyAliasType",
        kek_validation_type: "capo_payment_cryptography_data.types.as2805_kek_validation_type.As2805KekValidationType",
        random_key_send_variant_mask: "capo_payment_cryptography_data.types.random_key_send_variant_mask.RandomKeySendVariantMask",
        *,
        config_overrides: Optional[AsyncPaymentCryptographyDataClientConfig] = None,
    ) -> "capo_payment_cryptography_data.types.generate_as2805_kek_validation_output.GenerateAs2805KekValidationOutput":
        """<p>Generates a <code>KekValidationRequest</code> or a <code>KekValidationResponse</code> for node-to-node initialization between payment processing nodes using <a href="https://docs.aws.amazon.com/payment-cryptography/latest/userguide/as2805.html">Australian Standard 2805 (AS2805)</a>.</p> <p>During node-to-node initialization, both communicating nodes must validate that they possess the correct Key Encrypting Keys (KEKs) before proceeding with session key exchange. In AS2805, the sending KEK (KEKs) of one node corresponds to the receiving KEK (KEKr) of its partner node. Each node uses its KEK to encrypt and decrypt session keys exchanged between the nodes. A KEK can be created or imported into Amazon Web Services Payment Cryptography using either the <a href="https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_CreateKey.html">CreateKey</a> or <a href="https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_ImportKey.html">ImportKey</a> operations.</p> <p>To use <code>GenerateAs2805KekValidation</code> to generate a KEK validation request, set <code>KekValidationType</code> to <code>KekValidationRequest</code>. This operation returns both <code>RandomKeySend</code> (KRs) and <code>RandomKeyReceive</code> (KRr) as response values. The partnering node receives the KRs, uses its KEKr to decrypt it, and generates a KRr which is an inverted value of KRs. The node receiving the KRr validates it against its own KRr generated during KEK validation request outside of Amazon Web Services Payment Cryptography.</p> <p>You can also use this operation to generate a KEK validation response, by setting <code>KekValidationType</code> to <code>KekValidationResponse</code> and providing the incoming KRs. This operation then calculates a KRr. To learn more about more about node-to-node initialization, see <a href="https://docs.aws.amazon.com/payment-cryptography/latest/userguide/as2805.kekvalidation.html">Validation of KEK</a> in the <i>Amazon Web Services Payment Cryptography User Guide</i>.</p> <p>For information about valid keys for this operation, see <a href="https://docs.aws.amazon.com/payment-cryptography/latest/userguide/keys-validattributes.html">Understanding key attributes</a> and <a href="https://docs.aws.amazon.com/payment-cryptography/latest/userguide/crypto-ops-validkeys-ops.html">Key types for specific data operations</a> in the <i>Amazon Web Services Payment Cryptography User Guide</i>. </p> <p> <b>Cross-account use</b>: This operation supports cross-account use when the key has a resource-based policy that grants access. For more information, see <a href="https://docs.aws.amazon.com/payment-cryptography/latest/userguide/security_iam_resource-based-policies.html">Resource-based policies</a>.</p>

        Args:
            key_identifier: <p>The <code>keyARN</code> of sending KEK that Amazon Web Services Payment Cryptography uses for node-to-node initialization</p>
            kek_validation_type: <p>Defines whether to generate a KEK validation request or KEK validation response for node-to-node initialization.</p>
            random_key_send_variant_mask: <p>The key variant to use for generating a random key for KEK validation during node-to-node initialization.</p>

        Raises:
            capo_payment_cryptography_data.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_payment_cryptography_data.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception, or failure.</p>
            capo_payment_cryptography_data.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request was denied due to an invalid resource error.</p>
            capo_payment_cryptography_data.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_payment_cryptography_data.errors.validation_exception.ValidationException: <p>The request was denied due to an invalid request error.</p>
            capo_payment_cryptography_data.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_payment_cryptography_data.types.generate_as2805_kek_validation_input.GenerateAs2805KekValidationInput]",
        ) -> AsyncOperationResponse[
            "capo_payment_cryptography_data.types.generate_as2805_kek_validation_output.GenerateAs2805KekValidationOutput"
        ]:
            import capo_payment_cryptography_data._operations.payment_cryptography_data_plane.generate_as2805_kek_validation

            (
                output,
                http_response,
            ) = await capo_payment_cryptography_data._operations.payment_cryptography_data_plane.generate_as2805_kek_validation.async_generate_as2805_kek_validation(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_payment_cryptography_data.types.generate_as2805_kek_validation_input.GenerateAs2805KekValidationInput = {
            "key_identifier": key_identifier,
            "kek_validation_type": kek_validation_type,
            "random_key_send_variant_mask": random_key_send_variant_mask,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def generate_auth_request_cryptogram(
        self,
        key_identifier: "capo_payment_cryptography_data.types.key_arn_or_key_alias_type.KeyArnOrKeyAliasType",
        transaction_data: "capo_payment_cryptography_data.types.transaction_data_type.TransactionDataType",
        major_key_derivation_mode: "capo_payment_cryptography_data.types.major_key_derivation_mode.MajorKeyDerivationMode",
        session_key_derivation_attributes: "capo_payment_cryptography_data.types.session_key_derivation.SessionKeyDerivation",
        *,
        config_overrides: Optional[AsyncPaymentCryptographyDataClientConfig] = None,
    ) -> "capo_payment_cryptography_data.types.generate_auth_request_cryptogram_output.GenerateAuthRequestCryptogramOutput":
        """<p>Generates an Authorization Request Cryptogram (ARQC) for an EMV chip payment card authorization. For more information, see <a href="https://docs.aws.amazon.com/payment-cryptography/latest/userguide/data-operations.generateauthrequestcryptogram.html">Generate auth request cryptogram</a> in the <i>Amazon Web Services Payment Cryptography User Guide</i>.</p> <p>ARQC generation uses an Issuer Master Key (IMK) for application cryptograms (TR31_E0_EMV_MKEY_APP_CRYPTOGRAMS) to derive a session key, which is then used to generate the cryptogram from the provided transaction data (when applicable). To use this operation, you must first create or import an IMK-AC key by calling <a href="https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_CreateKey.html">CreateKey</a> or <a href="https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_ImportKey.html">ImportKey</a>. The <code>KeyModesOfUse</code> should be set to <code>DeriveKey</code> for the IMK-AC encryption key.</p> <important> <p>This operation is intended for development and testing scenarios only. It is not recommended to use this operation as a substitute for card-based cryptogram generation in production payment flows.</p> </important> <p>For information about valid keys for this operation, see <a href="https://docs.aws.amazon.com/payment-cryptography/latest/userguide/keys-validattributes.html">Understanding key attributes</a> and <a href="https://docs.aws.amazon.com/payment-cryptography/latest/userguide/crypto-ops-validkeys-ops.html">Key types for specific data operations</a> in the <i>Amazon Web Services Payment Cryptography User Guide</i>. </p> <p> <b>Cross-account use</b>: This operation supports cross-account use when the key has a resource-based policy that grants access. For more information, see <a href="https://docs.aws.amazon.com/payment-cryptography/latest/userguide/security_iam_resource-based-policies.html">Resource-based policies</a>.</p> <p> <b>Related operations:</b> </p> <ul> <li> <p> <a>VerifyAuthRequestCryptogram</a> </p> </li> </ul>

        Args:
            key_identifier: <p>The <code>keyARN</code> of the IMK-AC (TR31_E0_EMV_MKEY_APP_CRYPTOGRAMS) that Amazon Web Services Payment Cryptography uses to generate the ARQC.</p>
            transaction_data: <p>The transaction data that Amazon Web Services Payment Cryptography uses for ARQC generation. The same transaction data is used for ARQC verification by the issuer using <a>VerifyAuthRequestCryptogram</a>.</p>
            major_key_derivation_mode: <p>The method to use when deriving the major encryption key for ARQC generation within Amazon Web Services Payment Cryptography.</p>
            session_key_derivation_attributes: <p>The attributes and values to use for deriving a session key for ARQC generation within Amazon Web Services Payment Cryptography.</p>

        Raises:
            capo_payment_cryptography_data.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_payment_cryptography_data.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception, or failure.</p>
            capo_payment_cryptography_data.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request was denied due to an invalid resource error.</p>
            capo_payment_cryptography_data.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_payment_cryptography_data.errors.validation_exception.ValidationException: <p>The request was denied due to an invalid request error.</p>
            capo_payment_cryptography_data.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_payment_cryptography_data.types.generate_auth_request_cryptogram_input.GenerateAuthRequestCryptogramInput]",
        ) -> AsyncOperationResponse[
            "capo_payment_cryptography_data.types.generate_auth_request_cryptogram_output.GenerateAuthRequestCryptogramOutput"
        ]:
            import capo_payment_cryptography_data._operations.payment_cryptography_data_plane.generate_auth_request_cryptogram

            (
                output,
                http_response,
            ) = await capo_payment_cryptography_data._operations.payment_cryptography_data_plane.generate_auth_request_cryptogram.async_generate_auth_request_cryptogram(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_payment_cryptography_data.types.generate_auth_request_cryptogram_input.GenerateAuthRequestCryptogramInput = {
            "key_identifier": key_identifier,
            "transaction_data": transaction_data,
            "major_key_derivation_mode": major_key_derivation_mode,
            "session_key_derivation_attributes": session_key_derivation_attributes,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def generate_card_validation_data(
        self,
        key_identifier: "capo_payment_cryptography_data.types.key_arn_or_key_alias_type.KeyArnOrKeyAliasType",
        primary_account_number: "capo_payment_cryptography_data.types.primary_account_number_type.PrimaryAccountNumberType",
        generation_attributes: "capo_payment_cryptography_data.types.card_generation_attributes.CardGenerationAttributes",
        *,
        config_overrides: Optional[AsyncPaymentCryptographyDataClientConfig] = None,
        validation_data_length: Optional[
            "capo_payment_cryptography_data.types.integer_range_between3_and5_type.IntegerRangeBetween3And5Type"
        ] = None,
    ) -> "capo_payment_cryptography_data.types.generate_card_validation_data_output.GenerateCardValidationDataOutput":
        """<p>Generates card-related validation data using algorithms such as Card Verification Values (CVV/CVV2), Dynamic Card Verification Values (dCVV/dCVV2), or Card Security Codes (CSC). For more information, see <a href="https://docs.aws.amazon.com/payment-cryptography/latest/userguide/generate-card-data.html">Generate card data</a> in the <i>Amazon Web Services Payment Cryptography User Guide</i>.</p> <p>This operation generates a CVV or CSC value that is printed on a payment credit or debit card during card production. The CVV or CSC, PAN (Primary Account Number) and expiration date of the card are required to check its validity during transaction processing. To begin this operation, a CVK (Card Verification Key) encryption key is required. You can use <a href="https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_CreateKey.html">CreateKey</a> or <a href="https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_ImportKey.html">ImportKey</a> to establish a CVK within Amazon Web Services Payment Cryptography. The <code>KeyModesOfUse</code> should be set to <code>Generate</code> and <code>Verify</code> for a CVK encryption key. </p> <p>For information about valid keys for this operation, see <a href="https://docs.aws.amazon.com/payment-cryptography/latest/userguide/keys-validattributes.html">Understanding key attributes</a> and <a href="https://docs.aws.amazon.com/payment-cryptography/latest/userguide/crypto-ops-validkeys-ops.html">Key types for specific data operations</a> in the <i>Amazon Web Services Payment Cryptography User Guide</i>. </p> <p> <b>Cross-account use</b>: This operation supports cross-account use when the key has a resource-based policy that grants access. For more information, see <a href="https://docs.aws.amazon.com/payment-cryptography/latest/userguide/security_iam_resource-based-policies.html">Resource-based policies</a>.</p> <p> <b>Related operations:</b> </p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_ImportKey.html">ImportKey</a> </p> </li> <li> <p> <a>VerifyCardValidationData</a> </p> </li> </ul>

        Args:
            key_identifier: <p>The <code>keyARN</code> of the CVK encryption key that Amazon Web Services Payment Cryptography uses to generate card data.</p>
            primary_account_number: <p>The Primary Account Number (PAN), a unique identifier for a payment credit or debit card that associates the card with a specific account holder.</p>
            generation_attributes: <p>The algorithm for generating CVV or CSC values for the card within Amazon Web Services Payment Cryptography.</p>
            validation_data_length: <p>The length of the CVV or CSC to be generated. The default value is 3.</p>

        Raises:
            capo_payment_cryptography_data.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_payment_cryptography_data.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception, or failure.</p>
            capo_payment_cryptography_data.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request was denied due to an invalid resource error.</p>
            capo_payment_cryptography_data.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_payment_cryptography_data.errors.validation_exception.ValidationException: <p>The request was denied due to an invalid request error.</p>
            capo_payment_cryptography_data.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_payment_cryptography_data.types.generate_card_validation_data_input.GenerateCardValidationDataInput]",
        ) -> AsyncOperationResponse[
            "capo_payment_cryptography_data.types.generate_card_validation_data_output.GenerateCardValidationDataOutput"
        ]:
            import capo_payment_cryptography_data._operations.payment_cryptography_data_plane.generate_card_validation_data

            (
                output,
                http_response,
            ) = await capo_payment_cryptography_data._operations.payment_cryptography_data_plane.generate_card_validation_data.async_generate_card_validation_data(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_payment_cryptography_data.types.generate_card_validation_data_input.GenerateCardValidationDataInput = {
            "key_identifier": key_identifier,
            "primary_account_number": primary_account_number,
            "generation_attributes": generation_attributes,
        }
        if validation_data_length is not None:
            input_["validation_data_length"] = validation_data_length

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def generate_mac(
        self,
        key_identifier: "capo_payment_cryptography_data.types.key_arn_or_key_alias_type.KeyArnOrKeyAliasType",
        message_data: "capo_payment_cryptography_data.types.message_data_type.MessageDataType",
        generation_attributes: "capo_payment_cryptography_data.types.mac_attributes.MacAttributes",
        *,
        config_overrides: Optional[AsyncPaymentCryptographyDataClientConfig] = None,
        mac_length: Optional[
            "capo_payment_cryptography_data.types.integer_range_between4_and32.IntegerRangeBetween4And32"
        ] = None,
    ) -> "capo_payment_cryptography_data.types.generate_mac_output.GenerateMacOutput":
        """<p>Generates a Message Authentication Code (MAC) cryptogram within Amazon Web Services Payment Cryptography. </p> <p>You can use this operation to authenticate card-related data by using known data values to generate MAC for data validation between the sending and receiving parties. This operation uses message data, a secret encryption key and MAC algorithm to generate a unique MAC value for transmission. The receiving party of the MAC must use the same message data, secret encryption key and MAC algorithm to reproduce another MAC value for comparision.</p> <p>You can use this operation to generate a DUPKT, CMAC, HMAC or EMV MAC by setting generation attributes and algorithm to the associated values. The MAC generation encryption key must have valid values for <code>KeyUsage</code> such as <code>TR31_M7_HMAC_KEY</code> for HMAC generation, and the key must have <code>KeyModesOfUse</code> set to <code>Generate</code>.</p> <p>For information about valid keys for this operation, see <a href="https://docs.aws.amazon.com/payment-cryptography/latest/userguide/keys-validattributes.html">Understanding key attributes</a> and <a href="https://docs.aws.amazon.com/payment-cryptography/latest/userguide/crypto-ops-validkeys-ops.html">Key types for specific data operations</a> in the <i>Amazon Web Services Payment Cryptography User Guide</i>. </p> <p> <b>Cross-account use</b>: This operation supports cross-account use when the key has a resource-based policy that grants access. For more information, see <a href="https://docs.aws.amazon.com/payment-cryptography/latest/userguide/security_iam_resource-based-policies.html">Resource-based policies</a>.</p> <p> <b>Related operations:</b> </p> <ul> <li> <p> <a>VerifyMac</a> </p> </li> </ul>

        Args:
            key_identifier: <p>The <code>keyARN</code> of the MAC generation encryption key.</p>
            message_data: <p>The data for which a MAC is under generation. This value must be hexBinary.</p>
            generation_attributes: <p>The attributes and data values to use for MAC generation within Amazon Web Services Payment Cryptography.</p>
            mac_length: <p>The length of a MAC under generation.</p>

        Raises:
            capo_payment_cryptography_data.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_payment_cryptography_data.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception, or failure.</p>
            capo_payment_cryptography_data.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request was denied due to an invalid resource error.</p>
            capo_payment_cryptography_data.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_payment_cryptography_data.errors.validation_exception.ValidationException: <p>The request was denied due to an invalid request error.</p>
            capo_payment_cryptography_data.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_payment_cryptography_data.types.generate_mac_input.GenerateMacInput]",
        ) -> AsyncOperationResponse[
            "capo_payment_cryptography_data.types.generate_mac_output.GenerateMacOutput"
        ]:
            import capo_payment_cryptography_data._operations.payment_cryptography_data_plane.generate_mac

            (
                output,
                http_response,
            ) = await capo_payment_cryptography_data._operations.payment_cryptography_data_plane.generate_mac.async_generate_mac(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_payment_cryptography_data.types.generate_mac_input.GenerateMacInput = {
            "key_identifier": key_identifier,
            "message_data": message_data,
            "generation_attributes": generation_attributes,
        }
        if mac_length is not None:
            input_["mac_length"] = mac_length

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def generate_mac_emv_pin_change(
        self,
        new_pin_pek_identifier: "capo_payment_cryptography_data.types.key_arn_or_key_alias_type.KeyArnOrKeyAliasType",
        new_encrypted_pin_block: "capo_payment_cryptography_data.types.pin_block_length_equals16.PinBlockLengthEquals16",
        pin_block_format: "capo_payment_cryptography_data.types.pin_block_format_for_emv_pin_change.PinBlockFormatForEmvPinChange",
        secure_messaging_integrity_key_identifier: "capo_payment_cryptography_data.types.key_arn_or_key_alias_type.KeyArnOrKeyAliasType",
        secure_messaging_confidentiality_key_identifier: "capo_payment_cryptography_data.types.key_arn_or_key_alias_type.KeyArnOrKeyAliasType",
        message_data: "capo_payment_cryptography_data.types.command_message_data_type.CommandMessageDataType",
        derivation_method_attributes: "capo_payment_cryptography_data.types.derivation_method_attributes.DerivationMethodAttributes",
        *,
        config_overrides: Optional[AsyncPaymentCryptographyDataClientConfig] = None,
    ) -> "capo_payment_cryptography_data.types.generate_mac_emv_pin_change_output.GenerateMacEmvPinChangeOutput":
        """<p>Generates an issuer script mac for EMV payment cards that use offline PINs as the cardholder verification method (CVM).</p> <p>This operation generates an authenticated issuer script response by appending the incoming message data (APDU command) with the target encrypted PIN block in ISO2 format. The command structure and method to send the issuer script update to the card is not defined by this operation and is typically determined by the applicable payment card scheme.</p> <p>The primary inputs to this operation include the incoming new encrypted pinblock, PIN encryption key (PEK), issuer master key (IMK), primary account number (PAN), and the payment card derivation method.</p> <p>The operation uses two issuer master keys - secure messaging for confidentiality (IMK-SMC) and secure messaging for integrity (IMK-SMI). The SMC key is used to internally derive a key to secure the pin, while SMI key is used to internally derive a key to authenticate the script reponse as per the <a href="https://www.emvco.com/specifications/">EMV 4.4 - Book 2 - Security and Key Management</a> specification. </p> <p>This operation supports Amex, EMV2000, EMVCommon, Mastercard and Visa derivation methods, each requiring specific input parameters. Users must follow the specific derivation method and input parameters defined by the respective payment card scheme.</p> <note> <p>Use <a>GenerateMac</a> operation when sending a script update to an EMV card that does not involve PIN change. When assigning IAM permissions, it is important to understand that <a>EncryptData</a> using EMV keys and <a>GenerateMac</a> perform similar functions to this command.</p> </note> <p> <b>Cross-account use</b>: This operation supports cross-account use when the key has a resource-based policy that grants access. For more information, see <a href="https://docs.aws.amazon.com/payment-cryptography/latest/userguide/security_iam_resource-based-policies.html">Resource-based policies</a>.</p> <p> <b>Related operations:</b> </p> <ul> <li> <p> <a>EncryptData</a> </p> </li> <li> <p> <a>GenerateMac</a> </p> </li> </ul>

        Args:
            new_pin_pek_identifier: <p>The <code>keyARN</code> of the PEK protecting the incoming new encrypted PIN block.</p>
            new_encrypted_pin_block: <p>The incoming new encrypted PIN block data for offline pin change on an EMV card.</p>
            pin_block_format: <p>The PIN encoding format of the incoming new encrypted PIN block as specified in ISO 9564.</p>
            secure_messaging_integrity_key_identifier: <p>The <code>keyARN</code> of the issuer master key (IMK-SMI) used to authenticate the issuer script response.</p>
            secure_messaging_confidentiality_key_identifier: <p>The <code>keyARN</code> of the issuer master key (IMK-SMC) used to protect the PIN block data in the issuer script response.</p>
            message_data: <p>The message data is the APDU command from the card reader or terminal. The target encrypted PIN block, after translation to ISO2 format, is appended to this message data to generate an issuer script response.</p>
            derivation_method_attributes: <p>The attributes and data values to derive payment card specific confidentiality and integrity keys.</p>

        Raises:
            capo_payment_cryptography_data.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_payment_cryptography_data.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception, or failure.</p>
            capo_payment_cryptography_data.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request was denied due to an invalid resource error.</p>
            capo_payment_cryptography_data.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_payment_cryptography_data.errors.validation_exception.ValidationException: <p>The request was denied due to an invalid request error.</p>
            capo_payment_cryptography_data.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_payment_cryptography_data.types.generate_mac_emv_pin_change_input.GenerateMacEmvPinChangeInput]",
        ) -> AsyncOperationResponse[
            "capo_payment_cryptography_data.types.generate_mac_emv_pin_change_output.GenerateMacEmvPinChangeOutput"
        ]:
            import capo_payment_cryptography_data._operations.payment_cryptography_data_plane.generate_mac_emv_pin_change

            (
                output,
                http_response,
            ) = await capo_payment_cryptography_data._operations.payment_cryptography_data_plane.generate_mac_emv_pin_change.async_generate_mac_emv_pin_change(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_payment_cryptography_data.types.generate_mac_emv_pin_change_input.GenerateMacEmvPinChangeInput = {
            "new_pin_pek_identifier": new_pin_pek_identifier,
            "new_encrypted_pin_block": new_encrypted_pin_block,
            "pin_block_format": pin_block_format,
            "secure_messaging_integrity_key_identifier": secure_messaging_integrity_key_identifier,
            "secure_messaging_confidentiality_key_identifier": secure_messaging_confidentiality_key_identifier,
            "message_data": message_data,
            "derivation_method_attributes": derivation_method_attributes,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def generate_pin_data(
        self,
        generation_key_identifier: "capo_payment_cryptography_data.types.key_arn_or_key_alias_type.KeyArnOrKeyAliasType",
        encryption_key_identifier: "capo_payment_cryptography_data.types.key_arn_or_key_alias_type.KeyArnOrKeyAliasType",
        generation_attributes: "capo_payment_cryptography_data.types.pin_generation_attributes.PinGenerationAttributes",
        pin_block_format: "capo_payment_cryptography_data.types.pin_block_format_for_pin_data.PinBlockFormatForPinData",
        *,
        config_overrides: Optional[AsyncPaymentCryptographyDataClientConfig] = None,
        pin_data_length: Optional[
            "capo_payment_cryptography_data.types.integer_range_between4_and12.IntegerRangeBetween4And12"
        ] = None,
        primary_account_number: Optional[
            "capo_payment_cryptography_data.types.primary_account_number_type.PrimaryAccountNumberType"
        ] = None,
        encryption_wrapped_key: Optional[
            "capo_payment_cryptography_data.types.wrapped_key.WrappedKey"
        ] = None,
    ) -> "capo_payment_cryptography_data.types.generate_pin_data_output.GeneratePinDataOutput":
        """<p>Generates pin-related data such as PIN, PIN Verification Value (PVV), PIN Block, and PIN Offset during new card issuance or reissuance. For more information, see <a href="https://docs.aws.amazon.com/payment-cryptography/latest/userguide/generate-pin-data.html">Generate PIN data</a> in the <i>Amazon Web Services Payment Cryptography User Guide</i>.</p> <p>PIN data is never transmitted in clear to or from Amazon Web Services Payment Cryptography. This operation generates PIN, PVV, or PIN Offset and then encrypts it using Pin Encryption Key (PEK) to create an <code>EncryptedPinBlock</code> for transmission from Amazon Web Services Payment Cryptography. This operation uses a separate Pin Verification Key (PVK) for VISA PVV generation. </p> <p>Using ECDH key exchange, you can receive cardholder selectable PINs into Amazon Web Services Payment Cryptography. The ECDH derived key protects the incoming PIN block. You can also use it for reveal PIN, wherein the generated PIN block is protected by the ECDH derived key before transmission from Amazon Web Services Payment Cryptography. For more information on establishing ECDH derived keys, see the <a href="https://docs.aws.amazon.com/payment-cryptography/latest/userguide/create-keys.html">Generating keys</a> in the <i>Amazon Web Services Payment Cryptography User Guide</i>.</p> <p>For information about valid keys for this operation, see <a href="https://docs.aws.amazon.com/payment-cryptography/latest/userguide/keys-validattributes.html">Understanding key attributes</a> and <a href="https://docs.aws.amazon.com/payment-cryptography/latest/userguide/crypto-ops-validkeys-ops.html">Key types for specific data operations</a> in the <i>Amazon Web Services Payment Cryptography User Guide</i>.</p> <p> <b>Cross-account use</b>: This operation supports cross-account use when the key has a resource-based policy that grants access. For more information, see <a href="https://docs.aws.amazon.com/payment-cryptography/latest/userguide/security_iam_resource-based-policies.html">Resource-based policies</a>.</p> <p> <b>Related operations:</b> </p> <ul> <li> <p> <a>GenerateCardValidationData</a> </p> </li> <li> <p> <a>TranslatePinData</a> </p> </li> <li> <p> <a>VerifyPinData</a> </p> </li> </ul>

        Args:
            generation_key_identifier: <p>The <code>keyARN</code> of the PEK that Amazon Web Services Payment Cryptography uses for pin data generation.</p>
            encryption_key_identifier: <p>The <code>keyARN</code> of the PEK that Amazon Web Services Payment Cryptography uses to encrypt the PIN Block. For ECDH, it is the <code>keyARN</code> of the asymmetric ECC key.</p>
            generation_attributes: <p>The attributes and values to use for PIN, PVV, or PIN Offset generation.</p>
            pin_data_length: <p>The length of PIN under generation.</p>
            primary_account_number: <p>The Primary Account Number (PAN), a unique identifier for a payment credit or debit card that associates the card with a specific account holder.</p>
            pin_block_format: <p>The PIN encoding format for pin data generation as specified in ISO 9564. Amazon Web Services Payment Cryptography supports <code>ISO_Format_0</code>, <code>ISO_Format_3</code> and <code>ISO_Format_4</code>.</p> <p>The <code>ISO_Format_0</code> PIN block format is equivalent to the ANSI X9.8, VISA-1, and ECI-1 PIN block formats. It is similar to a VISA-4 PIN block format. It supports a PIN from 4 to 12 digits in length.</p> <p>The <code>ISO_Format_3</code> PIN block format is the same as <code>ISO_Format_0</code> except that the fill digits are random values from 10 to 15.</p> <p>The <code>ISO_Format_4</code> PIN block format is the only one supporting AES encryption.</p>

        Raises:
            capo_payment_cryptography_data.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_payment_cryptography_data.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception, or failure.</p>
            capo_payment_cryptography_data.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request was denied due to an invalid resource error.</p>
            capo_payment_cryptography_data.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_payment_cryptography_data.errors.validation_exception.ValidationException: <p>The request was denied due to an invalid request error.</p>
            capo_payment_cryptography_data.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_payment_cryptography_data.types.generate_pin_data_input.GeneratePinDataInput]",
        ) -> AsyncOperationResponse[
            "capo_payment_cryptography_data.types.generate_pin_data_output.GeneratePinDataOutput"
        ]:
            import capo_payment_cryptography_data._operations.payment_cryptography_data_plane.generate_pin_data

            (
                output,
                http_response,
            ) = await capo_payment_cryptography_data._operations.payment_cryptography_data_plane.generate_pin_data.async_generate_pin_data(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_payment_cryptography_data.types.generate_pin_data_input.GeneratePinDataInput = {
            "generation_key_identifier": generation_key_identifier,
            "encryption_key_identifier": encryption_key_identifier,
            "generation_attributes": generation_attributes,
            "pin_block_format": pin_block_format,
        }
        if pin_data_length is not None:
            input_["pin_data_length"] = pin_data_length
        if primary_account_number is not None:
            input_["primary_account_number"] = primary_account_number
        if encryption_wrapped_key is not None:
            input_["encryption_wrapped_key"] = encryption_wrapped_key

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def re_encrypt_data(
        self,
        incoming_key_identifier: "capo_payment_cryptography_data.types.key_arn_or_key_alias_type.KeyArnOrKeyAliasType",
        outgoing_key_identifier: "capo_payment_cryptography_data.types.key_arn_or_key_alias_type.KeyArnOrKeyAliasType",
        cipher_text: "capo_payment_cryptography_data.types.cipher_text_type.CipherTextType",
        incoming_encryption_attributes: "capo_payment_cryptography_data.types.re_encryption_attributes.ReEncryptionAttributes",
        outgoing_encryption_attributes: "capo_payment_cryptography_data.types.re_encryption_attributes.ReEncryptionAttributes",
        *,
        config_overrides: Optional[AsyncPaymentCryptographyDataClientConfig] = None,
        incoming_wrapped_key: Optional[
            "capo_payment_cryptography_data.types.wrapped_key.WrappedKey"
        ] = None,
        outgoing_wrapped_key: Optional[
            "capo_payment_cryptography_data.types.wrapped_key.WrappedKey"
        ] = None,
    ) -> "capo_payment_cryptography_data.types.re_encrypt_data_output.ReEncryptDataOutput":
        """<p>Re-encrypts ciphertext using DUKPT, symmetric, or asymmetric data encryption keys. </p> <p>You can either generate an encryption key within Amazon Web Services Payment Cryptography by calling <a href="https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_CreateKey.html">CreateKey</a> or import your own encryption key by calling <a href="https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_ImportKey.html">ImportKey</a>. The <code>KeyArn</code> for use with this operation must be in a compatible key state with <code>KeyModesOfUse</code> set to <code>Encrypt</code>. </p> <p>This operation also supports dynamic keys, allowing you to pass a dynamic encryption key as a TR-31 WrappedKeyBlock. This can be used when key material is frequently rotated, such as during every card transaction, and there is need to avoid importing short-lived keys into Amazon Web Services Payment Cryptography. To re-encrypt using dynamic keys, the <code>keyARN</code> is the Key Encryption Key (KEK) of the TR-31 wrapped encryption key material. The incoming wrapped key shall have a key purpose of D0 with a mode of use of B or D. For more information, see <a href="https://docs.aws.amazon.com/payment-cryptography/latest/userguide/use-cases-acquirers-dynamickeys.html">Using Dynamic Keys</a> in the <i>Amazon Web Services Payment Cryptography User Guide</i>.</p> <p>Amazon Web Services Payment Cryptography supports the following encryption key schemes:</p> <ul> <li> <p> <b>DUKPT</b>: <code>TDES</code> and <code>AES</code> algorithms. To encrypt using DUKPT, a DUKPT key must already exist within your account with <code>KeyModesOfUse</code> set to <code>DeriveKey</code> or a new DUKPT can be generated by calling <a href="https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_CreateKey.html">CreateKey</a>.</p> </li> <li> <p> <b>Symmetric</b>: <code>TDES</code> and <code>AES</code> algorithms.</p> </li> <li> <p> <b>Asymmetric</b>: <code>RSA</code>. You can use an <code>RSA</code> key on either the incoming or the outgoing side, paired with a symmetric key on the other side.</p> </li> </ul> <p>For information about valid keys for this operation, see <a href="https://docs.aws.amazon.com/payment-cryptography/latest/userguide/keys-validattributes.html">Understanding key attributes</a> and <a href="https://docs.aws.amazon.com/payment-cryptography/latest/userguide/crypto-ops-validkeys-ops.html">Key types for specific data operations</a> in the <i>Amazon Web Services Payment Cryptography User Guide</i>. </p> <p> <b>Cross-account use</b>: This operation supports cross-account use when the key has a resource-based policy that grants access. For more information, see <a href="https://docs.aws.amazon.com/payment-cryptography/latest/userguide/security_iam_resource-based-policies.html">Resource-based policies</a>.</p> <p> <b>Related operations:</b> </p> <ul> <li> <p> <a>DecryptData</a> </p> </li> <li> <p> <a>EncryptData</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_GetPublicKeyCertificate.html">GetPublicCertificate</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_ImportKey.html">ImportKey</a> </p> </li> </ul>

        Args:
            incoming_key_identifier: <p>The <code>keyARN</code> of the encryption key of incoming ciphertext data.</p> <p>When a WrappedKeyBlock is provided, this value will be the identifier to the key wrapping key. Otherwise, it is the key identifier used to perform the operation.</p>
            outgoing_key_identifier: <p>The <code>keyARN</code> of the encryption key of outgoing ciphertext data after encryption by Amazon Web Services Payment Cryptography.</p>
            cipher_text: <p>Ciphertext to be encrypted. The minimum allowed length is 16 bytes and maximum allowed length is 4096 bytes.</p>
            incoming_encryption_attributes: <p>The attributes and values for incoming ciphertext.</p>
            outgoing_encryption_attributes: <p>The attributes and values for outgoing ciphertext data after encryption by Amazon Web Services Payment Cryptography.</p>
            incoming_wrapped_key: <p>The WrappedKeyBlock containing the encryption key of incoming ciphertext data.</p>
            outgoing_wrapped_key: <p>The WrappedKeyBlock containing the encryption key of outgoing ciphertext data after encryption by Amazon Web Services Payment Cryptography.</p>

        Raises:
            capo_payment_cryptography_data.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_payment_cryptography_data.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception, or failure.</p>
            capo_payment_cryptography_data.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request was denied due to an invalid resource error.</p>
            capo_payment_cryptography_data.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_payment_cryptography_data.errors.validation_exception.ValidationException: <p>The request was denied due to an invalid request error.</p>
            capo_payment_cryptography_data.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_payment_cryptography_data.types.re_encrypt_data_input.ReEncryptDataInput]",
        ) -> AsyncOperationResponse[
            "capo_payment_cryptography_data.types.re_encrypt_data_output.ReEncryptDataOutput"
        ]:
            import capo_payment_cryptography_data._operations.payment_cryptography_data_plane.re_encrypt_data

            (
                output,
                http_response,
            ) = await capo_payment_cryptography_data._operations.payment_cryptography_data_plane.re_encrypt_data.async_re_encrypt_data(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_payment_cryptography_data.types.re_encrypt_data_input.ReEncryptDataInput = {
            "incoming_key_identifier": incoming_key_identifier,
            "outgoing_key_identifier": outgoing_key_identifier,
            "cipher_text": cipher_text,
            "incoming_encryption_attributes": incoming_encryption_attributes,
            "outgoing_encryption_attributes": outgoing_encryption_attributes,
        }
        if incoming_wrapped_key is not None:
            input_["incoming_wrapped_key"] = incoming_wrapped_key
        if outgoing_wrapped_key is not None:
            input_["outgoing_wrapped_key"] = outgoing_wrapped_key

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def translate_key_material(
        self,
        incoming_key_material: "capo_payment_cryptography_data.types.incoming_key_material.IncomingKeyMaterial",
        outgoing_key_material: "capo_payment_cryptography_data.types.outgoing_key_material.OutgoingKeyMaterial",
        *,
        config_overrides: Optional[AsyncPaymentCryptographyDataClientConfig] = None,
        key_check_value_algorithm: Optional[
            "capo_payment_cryptography_data.types.key_check_value_algorithm.KeyCheckValueAlgorithm"
        ] = None,
    ) -> "capo_payment_cryptography_data.types.translate_key_material_output.TranslateKeyMaterialOutput":
        """<p>Translates an cryptographic key between different wrapping keys without importing the key into Amazon Web Services Payment Cryptography.</p> <p>This operation can be used when key material is frequently rotated, such as during every card transaction, and there is a need to avoid importing short-lived keys into Amazon Web Services Payment Cryptography. It translates short-lived transaction keys such as <a href="https://docs.aws.amazon.com/payment-cryptography/latest/userguide/terminology.html#terms.pek">PEK</a> generated for each transaction and wrapped with an <a href="https://docs.aws.amazon.com/payment-cryptography/latest/userguide/terminology.html#terms.ecdh">ECDH</a> derived wrapping key to another <a href="https://docs.aws.amazon.com/payment-cryptography/latest/userguide/terminology.html#terms.kek">KEK</a> wrapping key. </p> <p>Before using this operation, you must first request the public key certificate of the ECC key pair generated within Amazon Web Services Payment Cryptography to establish an ECDH key agreement. In <code>TranslateKeyData</code>, the service uses its own ECC key pair, public certificate of receiving ECC key pair, and the key derivation parameters to generate a derived key. The service uses this derived key to unwrap the incoming transaction key received as a TR31WrappedKeyBlock and re-wrap using a user provided KEK to generate an outgoing Tr31WrappedKeyBlock.</p> <p>For information about valid keys for this operation, see <a href="https://docs.aws.amazon.com/payment-cryptography/latest/userguide/keys-validattributes.html">Understanding key attributes</a> and <a href="https://docs.aws.amazon.com/payment-cryptography/latest/userguide/crypto-ops-validkeys-ops.html">Key types for specific data operations</a> in the <i>Amazon Web Services Payment Cryptography User Guide</i>. </p> <p> <b>Cross-account use</b>: This operation supports cross-account use when the key has a resource-based policy that grants access. For more information, see <a href="https://docs.aws.amazon.com/payment-cryptography/latest/userguide/security_iam_resource-based-policies.html">Resource-based policies</a>.</p> <p> <b>Related operations:</b> </p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_CreateKey.html">CreateKey</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_GetPublicKeyCertificate.html">GetPublicCertificate</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_ImportKey.html">ImportKey</a> </p> </li> </ul>

        Args:
            incoming_key_material: <p>Parameter information of the TR31WrappedKeyBlock containing the transaction key.</p>
            outgoing_key_material: <p>Parameter information of the wrapping key used to wrap the transaction key in the outgoing TR31WrappedKeyBlock.</p>
            key_check_value_algorithm: <p>The key check value (KCV) algorithm used for calculating the KCV of the derived key.</p>

        Raises:
            capo_payment_cryptography_data.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_payment_cryptography_data.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception, or failure.</p>
            capo_payment_cryptography_data.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request was denied due to an invalid resource error.</p>
            capo_payment_cryptography_data.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_payment_cryptography_data.errors.validation_exception.ValidationException: <p>The request was denied due to an invalid request error.</p>
            capo_payment_cryptography_data.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_payment_cryptography_data.types.translate_key_material_input.TranslateKeyMaterialInput]",
        ) -> AsyncOperationResponse[
            "capo_payment_cryptography_data.types.translate_key_material_output.TranslateKeyMaterialOutput"
        ]:
            import capo_payment_cryptography_data._operations.payment_cryptography_data_plane.translate_key_material

            (
                output,
                http_response,
            ) = await capo_payment_cryptography_data._operations.payment_cryptography_data_plane.translate_key_material.async_translate_key_material(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_payment_cryptography_data.types.translate_key_material_input.TranslateKeyMaterialInput = {
            "incoming_key_material": incoming_key_material,
            "outgoing_key_material": outgoing_key_material,
        }
        if key_check_value_algorithm is not None:
            input_["key_check_value_algorithm"] = key_check_value_algorithm

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def translate_pin_data(
        self,
        incoming_key_identifier: "capo_payment_cryptography_data.types.key_arn_or_key_alias_type.KeyArnOrKeyAliasType",
        outgoing_key_identifier: "capo_payment_cryptography_data.types.key_arn_or_key_alias_type.KeyArnOrKeyAliasType",
        incoming_translation_attributes: "capo_payment_cryptography_data.types.translation_iso_formats.TranslationIsoFormats",
        outgoing_translation_attributes: "capo_payment_cryptography_data.types.translation_iso_formats.TranslationIsoFormats",
        encrypted_pin_block: "capo_payment_cryptography_data.types.hex_even_length_between16_and32.HexEvenLengthBetween16And32",
        *,
        config_overrides: Optional[AsyncPaymentCryptographyDataClientConfig] = None,
        incoming_dukpt_attributes: Optional[
            "capo_payment_cryptography_data.types.dukpt_derivation_attributes.DukptDerivationAttributes"
        ] = None,
        outgoing_dukpt_attributes: Optional[
            "capo_payment_cryptography_data.types.dukpt_derivation_attributes.DukptDerivationAttributes"
        ] = None,
        incoming_wrapped_key: Optional[
            "capo_payment_cryptography_data.types.wrapped_key.WrappedKey"
        ] = None,
        outgoing_wrapped_key: Optional[
            "capo_payment_cryptography_data.types.wrapped_key.WrappedKey"
        ] = None,
        incoming_as2805_attributes: Optional[
            "capo_payment_cryptography_data.types.as2805_pek_derivation_attributes.As2805PekDerivationAttributes"
        ] = None,
    ) -> "capo_payment_cryptography_data.types.translate_pin_data_output.TranslatePinDataOutput":
        """<p>Translates encrypted PIN block from and to ISO 9564 formats 0,1,3,4. For more information, see <a href="https://docs.aws.amazon.com/payment-cryptography/latest/userguide/translate-pin-data.html">Translate PIN data</a> in the <i>Amazon Web Services Payment Cryptography User Guide</i>.</p> <p>PIN block translation involves changing a PIN block from one encryption key to another and optionally change its format. PIN block translation occurs entirely within the HSM boundary and PIN data never enters or leaves Amazon Web Services Payment Cryptography in clear text. The encryption key transformation can be from PEK (Pin Encryption Key) to BDK (Base Derivation Key) for DUKPT or from BDK for DUKPT to PEK.</p> <p>Amazon Web Services Payment Cryptography also supports use of dynamic keys and ECDH (Elliptic Curve Diffie-Hellman) based key exchange for this operation.</p> <p>Dynamic keys allow you to pass a PEK as a TR-31 WrappedKeyBlock. They can be used when key material is frequently rotated, such as during every card transaction, and there is need to avoid importing short-lived keys into Amazon Web Services Payment Cryptography. To translate PIN block using dynamic keys, the <code>keyARN</code> is the Key Encryption Key (KEK) of the TR-31 wrapped PEK. The incoming wrapped key shall have a key purpose of P0 with a mode of use of B or D. For more information, see <a href="https://docs.aws.amazon.com/payment-cryptography/latest/userguide/use-cases-acquirers-dynamickeys.html">Using Dynamic Keys</a> in the <i>Amazon Web Services Payment Cryptography User Guide</i>.</p> <p>Using ECDH key exchange, you can receive cardholder selectable PINs into Amazon Web Services Payment Cryptography. The ECDH derived key protects the incoming PIN block, which is translated to a PEK encrypted PIN block for use within the service. You can also use ECDH for reveal PIN, wherein the service translates the PIN block from PEK to a ECDH derived encryption key. For more information on establishing ECDH derived keys, see the <a href="https://docs.aws.amazon.com/payment-cryptography/latest/userguide/create-keys.html">Creating keys</a> in the <i>Amazon Web Services Payment Cryptography User Guide</i>.</p> <p>The allowed combinations of PIN block format translations are guided by PCI. It is important to note that not all encrypted PIN block formats (example, format 1) require PAN (Primary Account Number) as input. And as such, PIN block format that requires PAN (example, formats 0,3,4) cannot be translated to a format (format 1) that does not require a PAN for generation. </p> <p>For information about valid keys for this operation, see <a href="https://docs.aws.amazon.com/payment-cryptography/latest/userguide/keys-validattributes.html">Understanding key attributes</a> and <a href="https://docs.aws.amazon.com/payment-cryptography/latest/userguide/crypto-ops-validkeys-ops.html">Key types for specific data operations</a> in the <i>Amazon Web Services Payment Cryptography User Guide</i>.</p> <note> <p>Amazon Web Services Payment Cryptography currently supports ISO PIN block 4 translation for PIN block built using legacy PAN length. That is, PAN is the right most 12 digits excluding the check digits.</p> </note> <p> <b>Cross-account use</b>: This operation supports cross-account use when the key has a resource-based policy that grants access. For more information, see <a href="https://docs.aws.amazon.com/payment-cryptography/latest/userguide/security_iam_resource-based-policies.html">Resource-based policies</a>.</p> <p> <b>Related operations:</b> </p> <ul> <li> <p> <a>GeneratePinData</a> </p> </li> <li> <p> <a>VerifyPinData</a> </p> </li> </ul>

        Args:
            incoming_key_identifier: <p>The <code>keyARN</code> of the encryption key under which incoming PIN block data is encrypted. This key type can be PEK or BDK.</p> <p>For dynamic keys, it is the <code>keyARN</code> of KEK of the TR-31 wrapped PEK. For ECDH, it is the <code>keyARN</code> of the asymmetric ECC key.</p>
            outgoing_key_identifier: <p>The <code>keyARN</code> of the encryption key for encrypting outgoing PIN block data. This key type can be PEK or BDK.</p> <p>For ECDH, it is the <code>keyARN</code> of the asymmetric ECC key.</p>
            incoming_translation_attributes: <p>The format of the incoming PIN block data for translation within Amazon Web Services Payment Cryptography.</p>
            outgoing_translation_attributes: <p>The format of the outgoing PIN block data after translation by Amazon Web Services Payment Cryptography.</p>
            encrypted_pin_block: <p>The encrypted PIN block data that Amazon Web Services Payment Cryptography translates.</p>
            incoming_dukpt_attributes: <p>The attributes and values to use for incoming DUKPT encryption key for PIN block translation.</p>
            outgoing_dukpt_attributes: <p>The attributes and values to use for outgoing DUKPT encryption key after PIN block translation.</p>
            incoming_wrapped_key: <p>The WrappedKeyBlock containing the encryption key under which incoming PIN block data is encrypted.</p>
            outgoing_wrapped_key: <p>The WrappedKeyBlock containing the encryption key for encrypting outgoing PIN block data.</p>
            incoming_as2805_attributes: <p>The attributes and values to use for incoming AS2805 encryption key for PIN block translation.</p>

        Raises:
            capo_payment_cryptography_data.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_payment_cryptography_data.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception, or failure.</p>
            capo_payment_cryptography_data.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request was denied due to an invalid resource error.</p>
            capo_payment_cryptography_data.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_payment_cryptography_data.errors.validation_exception.ValidationException: <p>The request was denied due to an invalid request error.</p>
            capo_payment_cryptography_data.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_payment_cryptography_data.types.translate_pin_data_input.TranslatePinDataInput]",
        ) -> AsyncOperationResponse[
            "capo_payment_cryptography_data.types.translate_pin_data_output.TranslatePinDataOutput"
        ]:
            import capo_payment_cryptography_data._operations.payment_cryptography_data_plane.translate_pin_data

            (
                output,
                http_response,
            ) = await capo_payment_cryptography_data._operations.payment_cryptography_data_plane.translate_pin_data.async_translate_pin_data(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_payment_cryptography_data.types.translate_pin_data_input.TranslatePinDataInput = {
            "incoming_key_identifier": incoming_key_identifier,
            "outgoing_key_identifier": outgoing_key_identifier,
            "incoming_translation_attributes": incoming_translation_attributes,
            "outgoing_translation_attributes": outgoing_translation_attributes,
            "encrypted_pin_block": encrypted_pin_block,
        }
        if incoming_dukpt_attributes is not None:
            input_["incoming_dukpt_attributes"] = incoming_dukpt_attributes
        if outgoing_dukpt_attributes is not None:
            input_["outgoing_dukpt_attributes"] = outgoing_dukpt_attributes
        if incoming_wrapped_key is not None:
            input_["incoming_wrapped_key"] = incoming_wrapped_key
        if outgoing_wrapped_key is not None:
            input_["outgoing_wrapped_key"] = outgoing_wrapped_key
        if incoming_as2805_attributes is not None:
            input_["incoming_as2805_attributes"] = incoming_as2805_attributes

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def verify_auth_request_cryptogram(
        self,
        key_identifier: "capo_payment_cryptography_data.types.key_arn_or_key_alias_type.KeyArnOrKeyAliasType",
        transaction_data: "capo_payment_cryptography_data.types.transaction_data_type.TransactionDataType",
        auth_request_cryptogram: "capo_payment_cryptography_data.types.auth_request_cryptogram_type.AuthRequestCryptogramType",
        major_key_derivation_mode: "capo_payment_cryptography_data.types.major_key_derivation_mode.MajorKeyDerivationMode",
        session_key_derivation_attributes: "capo_payment_cryptography_data.types.session_key_derivation.SessionKeyDerivation",
        *,
        config_overrides: Optional[AsyncPaymentCryptographyDataClientConfig] = None,
        auth_response_attributes: Optional[
            "capo_payment_cryptography_data.types.cryptogram_auth_response.CryptogramAuthResponse"
        ] = None,
    ) -> "capo_payment_cryptography_data.types.verify_auth_request_cryptogram_output.VerifyAuthRequestCryptogramOutput":
        """<p>Verifies Authorization Request Cryptogram (ARQC) for a EMV chip payment card authorization. For more information, see <a href="https://docs.aws.amazon.com/payment-cryptography/latest/userguide/data-operations.verifyauthrequestcryptogram.html">Verify auth request cryptogram</a> in the <i>Amazon Web Services Payment Cryptography User Guide</i>.</p> <p>ARQC generation is done outside of Amazon Web Services Payment Cryptography and is typically generated on a point of sale terminal for an EMV chip card to obtain payment authorization during transaction time. For ARQC verification, you must first import the ARQC generated outside of Amazon Web Services Payment Cryptography by calling <a href="https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_ImportKey.html">ImportKey</a>. This operation uses the imported ARQC and an major encryption key (DUKPT) created by calling <a href="https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_CreateKey.html">CreateKey</a> to either provide a boolean ARQC verification result or provide an APRC (Authorization Response Cryptogram) response using Method 1 or Method 2. The <code>ARPC_METHOD_1</code> uses <code>AuthResponseCode</code> to generate ARPC and <code>ARPC_METHOD_2</code> uses <code>CardStatusUpdate</code> to generate ARPC. </p> <p>For information about valid keys for this operation, see <a href="https://docs.aws.amazon.com/payment-cryptography/latest/userguide/keys-validattributes.html">Understanding key attributes</a> and <a href="https://docs.aws.amazon.com/payment-cryptography/latest/userguide/crypto-ops-validkeys-ops.html">Key types for specific data operations</a> in the <i>Amazon Web Services Payment Cryptography User Guide</i>.</p> <p> <b>Cross-account use</b>: This operation supports cross-account use when the key has a resource-based policy that grants access. For more information, see <a href="https://docs.aws.amazon.com/payment-cryptography/latest/userguide/security_iam_resource-based-policies.html">Resource-based policies</a>.</p> <p> <b>Related operations:</b> </p> <ul> <li> <p> <a>VerifyCardValidationData</a> </p> </li> <li> <p> <a>VerifyPinData</a> </p> </li> </ul>

        Args:
            key_identifier: <p>The <code>keyARN</code> of the major encryption key that Amazon Web Services Payment Cryptography uses for ARQC verification.</p>
            transaction_data: <p>The transaction data that Amazon Web Services Payment Cryptography uses for ARQC verification. The same transaction is used for ARQC generation outside of Amazon Web Services Payment Cryptography.</p>
            auth_request_cryptogram: <p>The auth request cryptogram imported into Amazon Web Services Payment Cryptography for ARQC verification using a major encryption key and transaction data.</p>
            major_key_derivation_mode: <p>The method to use when deriving the major encryption key for ARQC verification within Amazon Web Services Payment Cryptography. The same key derivation mode was used for ARQC generation outside of Amazon Web Services Payment Cryptography.</p>
            session_key_derivation_attributes: <p>The attributes and values to use for deriving a session key for ARQC verification within Amazon Web Services Payment Cryptography. The same attributes were used for ARQC generation outside of Amazon Web Services Payment Cryptography.</p>
            auth_response_attributes: <p>The attributes and values for auth request cryptogram verification. These parameters are required in case using ARPC Method 1 or Method 2 for ARQC verification.</p>

        Raises:
            capo_payment_cryptography_data.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_payment_cryptography_data.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception, or failure.</p>
            capo_payment_cryptography_data.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request was denied due to an invalid resource error.</p>
            capo_payment_cryptography_data.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_payment_cryptography_data.errors.validation_exception.ValidationException: <p>The request was denied due to an invalid request error.</p>
            capo_payment_cryptography_data.errors.verification_failed_exception.VerificationFailedException: <p>This request failed verification.</p>
            capo_payment_cryptography_data.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_payment_cryptography_data.types.verify_auth_request_cryptogram_input.VerifyAuthRequestCryptogramInput]",
        ) -> AsyncOperationResponse[
            "capo_payment_cryptography_data.types.verify_auth_request_cryptogram_output.VerifyAuthRequestCryptogramOutput"
        ]:
            import capo_payment_cryptography_data._operations.payment_cryptography_data_plane.verify_auth_request_cryptogram

            (
                output,
                http_response,
            ) = await capo_payment_cryptography_data._operations.payment_cryptography_data_plane.verify_auth_request_cryptogram.async_verify_auth_request_cryptogram(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_payment_cryptography_data.types.verify_auth_request_cryptogram_input.VerifyAuthRequestCryptogramInput = {
            "key_identifier": key_identifier,
            "transaction_data": transaction_data,
            "auth_request_cryptogram": auth_request_cryptogram,
            "major_key_derivation_mode": major_key_derivation_mode,
            "session_key_derivation_attributes": session_key_derivation_attributes,
        }
        if auth_response_attributes is not None:
            input_["auth_response_attributes"] = auth_response_attributes

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def verify_card_validation_data(
        self,
        key_identifier: "capo_payment_cryptography_data.types.key_arn_or_key_alias_type.KeyArnOrKeyAliasType",
        primary_account_number: "capo_payment_cryptography_data.types.primary_account_number_type.PrimaryAccountNumberType",
        verification_attributes: "capo_payment_cryptography_data.types.card_verification_attributes.CardVerificationAttributes",
        validation_data: "capo_payment_cryptography_data.types.validation_data_type.ValidationDataType",
        *,
        config_overrides: Optional[AsyncPaymentCryptographyDataClientConfig] = None,
    ) -> "capo_payment_cryptography_data.types.verify_card_validation_data_output.VerifyCardValidationDataOutput":
        """<p>Verifies card-related validation data using algorithms such as Card Verification Values (CVV/CVV2), Dynamic Card Verification Values (dCVV/dCVV2) and Card Security Codes (CSC). For more information, see <a href="https://docs.aws.amazon.com/payment-cryptography/latest/userguide/verify-card-data.html">Verify card data</a> in the <i>Amazon Web Services Payment Cryptography User Guide</i>.</p> <p>This operation validates the CVV or CSC codes that is printed on a payment credit or debit card during card payment transaction. The input values are typically provided as part of an inbound transaction to an issuer or supporting platform partner. Amazon Web Services Payment Cryptography uses CVV or CSC, PAN (Primary Account Number) and expiration date of the card to check its validity during transaction processing. In this operation, the CVK (Card Verification Key) encryption key for use with card data verification is same as the one in used for <a>GenerateCardValidationData</a>. </p> <p>For information about valid keys for this operation, see <a href="https://docs.aws.amazon.com/payment-cryptography/latest/userguide/keys-validattributes.html">Understanding key attributes</a> and <a href="https://docs.aws.amazon.com/payment-cryptography/latest/userguide/crypto-ops-validkeys-ops.html">Key types for specific data operations</a> in the <i>Amazon Web Services Payment Cryptography User Guide</i>. </p> <p> <b>Cross-account use</b>: This operation supports cross-account use when the key has a resource-based policy that grants access. For more information, see <a href="https://docs.aws.amazon.com/payment-cryptography/latest/userguide/security_iam_resource-based-policies.html">Resource-based policies</a>.</p> <p> <b>Related operations:</b> </p> <ul> <li> <p> <a>GenerateCardValidationData</a> </p> </li> <li> <p> <a>VerifyAuthRequestCryptogram</a> </p> </li> <li> <p> <a>VerifyPinData</a> </p> </li> </ul>

        Args:
            key_identifier: <p>The <code>keyARN</code> of the CVK encryption key that Amazon Web Services Payment Cryptography uses to verify card data.</p>
            primary_account_number: <p>The Primary Account Number (PAN), a unique identifier for a payment credit or debit card that associates the card with a specific account holder.</p>
            verification_attributes: <p>The algorithm to use for verification of card data within Amazon Web Services Payment Cryptography.</p>
            validation_data: <p>The CVV or CSC value for use for card data verification within Amazon Web Services Payment Cryptography.</p>

        Raises:
            capo_payment_cryptography_data.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_payment_cryptography_data.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception, or failure.</p>
            capo_payment_cryptography_data.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request was denied due to an invalid resource error.</p>
            capo_payment_cryptography_data.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_payment_cryptography_data.errors.validation_exception.ValidationException: <p>The request was denied due to an invalid request error.</p>
            capo_payment_cryptography_data.errors.verification_failed_exception.VerificationFailedException: <p>This request failed verification.</p>
            capo_payment_cryptography_data.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_payment_cryptography_data.types.verify_card_validation_data_input.VerifyCardValidationDataInput]",
        ) -> AsyncOperationResponse[
            "capo_payment_cryptography_data.types.verify_card_validation_data_output.VerifyCardValidationDataOutput"
        ]:
            import capo_payment_cryptography_data._operations.payment_cryptography_data_plane.verify_card_validation_data

            (
                output,
                http_response,
            ) = await capo_payment_cryptography_data._operations.payment_cryptography_data_plane.verify_card_validation_data.async_verify_card_validation_data(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_payment_cryptography_data.types.verify_card_validation_data_input.VerifyCardValidationDataInput = {
            "key_identifier": key_identifier,
            "primary_account_number": primary_account_number,
            "verification_attributes": verification_attributes,
            "validation_data": validation_data,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def verify_mac(
        self,
        key_identifier: "capo_payment_cryptography_data.types.key_arn_or_key_alias_type.KeyArnOrKeyAliasType",
        message_data: "capo_payment_cryptography_data.types.message_data_type.MessageDataType",
        mac: "capo_payment_cryptography_data.types.mac_type.MacType",
        verification_attributes: "capo_payment_cryptography_data.types.mac_attributes.MacAttributes",
        *,
        config_overrides: Optional[AsyncPaymentCryptographyDataClientConfig] = None,
        mac_length: Optional[
            "capo_payment_cryptography_data.types.integer_range_between4_and32.IntegerRangeBetween4And32"
        ] = None,
    ) -> "capo_payment_cryptography_data.types.verify_mac_output.VerifyMacOutput":
        """<p>Verifies a Message Authentication Code (MAC). </p> <p>You can use this operation to verify MAC for message data authentication such as . In this operation, you must use the same message data, secret encryption key and MAC algorithm that was used to generate MAC. You can use this operation to verify a DUPKT, CMAC, HMAC or EMV MAC by setting generation attributes and algorithm to the associated values. </p> <p>For information about valid keys for this operation, see <a href="https://docs.aws.amazon.com/payment-cryptography/latest/userguide/keys-validattributes.html">Understanding key attributes</a> and <a href="https://docs.aws.amazon.com/payment-cryptography/latest/userguide/crypto-ops-validkeys-ops.html">Key types for specific data operations</a> in the <i>Amazon Web Services Payment Cryptography User Guide</i>. </p> <p> <b>Cross-account use</b>: This operation supports cross-account use when the key has a resource-based policy that grants access. For more information, see <a href="https://docs.aws.amazon.com/payment-cryptography/latest/userguide/security_iam_resource-based-policies.html">Resource-based policies</a>.</p> <p> <b>Related operations:</b> </p> <ul> <li> <p> <a>GenerateMac</a> </p> </li> </ul>

        Args:
            key_identifier: <p>The <code>keyARN</code> of the encryption key that Amazon Web Services Payment Cryptography uses to verify MAC data.</p>
            message_data: <p>The data on for which MAC is under verification. This value must be hexBinary.</p>
            mac: <p>The MAC being verified.</p>
            verification_attributes: <p>The attributes and data values to use for MAC verification within Amazon Web Services Payment Cryptography.</p>
            mac_length: <p>The length of the MAC.</p>

        Raises:
            capo_payment_cryptography_data.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_payment_cryptography_data.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception, or failure.</p>
            capo_payment_cryptography_data.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request was denied due to an invalid resource error.</p>
            capo_payment_cryptography_data.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_payment_cryptography_data.errors.validation_exception.ValidationException: <p>The request was denied due to an invalid request error.</p>
            capo_payment_cryptography_data.errors.verification_failed_exception.VerificationFailedException: <p>This request failed verification.</p>
            capo_payment_cryptography_data.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_payment_cryptography_data.types.verify_mac_input.VerifyMacInput]",
        ) -> AsyncOperationResponse[
            "capo_payment_cryptography_data.types.verify_mac_output.VerifyMacOutput"
        ]:
            import capo_payment_cryptography_data._operations.payment_cryptography_data_plane.verify_mac

            (
                output,
                http_response,
            ) = await capo_payment_cryptography_data._operations.payment_cryptography_data_plane.verify_mac.async_verify_mac(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_payment_cryptography_data.types.verify_mac_input.VerifyMacInput = {
            "key_identifier": key_identifier,
            "message_data": message_data,
            "mac": mac,
            "verification_attributes": verification_attributes,
        }
        if mac_length is not None:
            input_["mac_length"] = mac_length

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def verify_pin_data(
        self,
        verification_key_identifier: "capo_payment_cryptography_data.types.key_arn_or_key_alias_type.KeyArnOrKeyAliasType",
        encryption_key_identifier: "capo_payment_cryptography_data.types.key_arn_or_key_alias_type.KeyArnOrKeyAliasType",
        verification_attributes: "capo_payment_cryptography_data.types.pin_verification_attributes.PinVerificationAttributes",
        encrypted_pin_block: "capo_payment_cryptography_data.types.encrypted_pin_block_type.EncryptedPinBlockType",
        pin_block_format: "capo_payment_cryptography_data.types.pin_block_format_for_pin_data.PinBlockFormatForPinData",
        *,
        config_overrides: Optional[AsyncPaymentCryptographyDataClientConfig] = None,
        primary_account_number: Optional[
            "capo_payment_cryptography_data.types.primary_account_number_type.PrimaryAccountNumberType"
        ] = None,
        pin_data_length: Optional[
            "capo_payment_cryptography_data.types.integer_range_between4_and12.IntegerRangeBetween4And12"
        ] = None,
        dukpt_attributes: Optional[
            "capo_payment_cryptography_data.types.dukpt_attributes.DukptAttributes"
        ] = None,
        encryption_wrapped_key: Optional[
            "capo_payment_cryptography_data.types.wrapped_key.WrappedKey"
        ] = None,
    ) -> "capo_payment_cryptography_data.types.verify_pin_data_output.VerifyPinDataOutput":
        """<p>Verifies pin-related data such as PIN and PIN Offset using algorithms including VISA PVV and IBM3624. For more information, see <a href="https://docs.aws.amazon.com/payment-cryptography/latest/userguide/verify-pin-data.html">Verify PIN data</a> in the <i>Amazon Web Services Payment Cryptography User Guide</i>.</p> <p>This operation verifies PIN data for user payment card. A card holder PIN data is never transmitted in clear to or from Amazon Web Services Payment Cryptography. This operation uses PIN Verification Key (PVK) for PIN or PIN Offset generation and then encrypts it using PIN Encryption Key (PEK) to create an <code>EncryptedPinBlock</code> for transmission from Amazon Web Services Payment Cryptography. </p> <p>For information about valid keys for this operation, see <a href="https://docs.aws.amazon.com/payment-cryptography/latest/userguide/keys-validattributes.html">Understanding key attributes</a> and <a href="https://docs.aws.amazon.com/payment-cryptography/latest/userguide/crypto-ops-validkeys-ops.html">Key types for specific data operations</a> in the <i>Amazon Web Services Payment Cryptography User Guide</i>. </p> <p> <b>Cross-account use</b>: This operation supports cross-account use when the key has a resource-based policy that grants access. For more information, see <a href="https://docs.aws.amazon.com/payment-cryptography/latest/userguide/security_iam_resource-based-policies.html">Resource-based policies</a>.</p> <p> <b>Related operations:</b> </p> <ul> <li> <p> <a>GeneratePinData</a> </p> </li> <li> <p> <a>TranslatePinData</a> </p> </li> </ul>

        Args:
            verification_key_identifier: <p>The <code>keyARN</code> of the PIN verification key.</p>
            encryption_key_identifier: <p>The <code>keyARN</code> of the encryption key under which the PIN block data is encrypted. This key type can be PEK or BDK.</p>
            verification_attributes: <p>The attributes and values for PIN data verification.</p>
            encrypted_pin_block: <p>The encrypted PIN block data that Amazon Web Services Payment Cryptography verifies.</p>
            primary_account_number: <p>The Primary Account Number (PAN), a unique identifier for a payment credit or debit card that associates the card with a specific account holder.</p>
            pin_block_format: <p>The PIN encoding format for pin data generation as specified in ISO 9564. Amazon Web Services Payment Cryptography supports <code>ISO_Format_0</code> and <code>ISO_Format_3</code>.</p> <p>The <code>ISO_Format_0</code> PIN block format is equivalent to the ANSI X9.8, VISA-1, and ECI-1 PIN block formats. It is similar to a VISA-4 PIN block format. It supports a PIN from 4 to 12 digits in length.</p> <p>The <code>ISO_Format_3</code> PIN block format is the same as <code>ISO_Format_0</code> except that the fill digits are random values from 10 to 15.</p>
            pin_data_length: <p>The length of PIN being verified.</p>
            dukpt_attributes: <p>The attributes and values for the DUKPT encrypted PIN block data.</p>

        Raises:
            capo_payment_cryptography_data.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_payment_cryptography_data.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception, or failure.</p>
            capo_payment_cryptography_data.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request was denied due to an invalid resource error.</p>
            capo_payment_cryptography_data.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_payment_cryptography_data.errors.validation_exception.ValidationException: <p>The request was denied due to an invalid request error.</p>
            capo_payment_cryptography_data.errors.verification_failed_exception.VerificationFailedException: <p>This request failed verification.</p>
            capo_payment_cryptography_data.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_payment_cryptography_data.types.verify_pin_data_input.VerifyPinDataInput]",
        ) -> AsyncOperationResponse[
            "capo_payment_cryptography_data.types.verify_pin_data_output.VerifyPinDataOutput"
        ]:
            import capo_payment_cryptography_data._operations.payment_cryptography_data_plane.verify_pin_data

            (
                output,
                http_response,
            ) = await capo_payment_cryptography_data._operations.payment_cryptography_data_plane.verify_pin_data.async_verify_pin_data(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_payment_cryptography_data.types.verify_pin_data_input.VerifyPinDataInput = {
            "verification_key_identifier": verification_key_identifier,
            "encryption_key_identifier": encryption_key_identifier,
            "verification_attributes": verification_attributes,
            "encrypted_pin_block": encrypted_pin_block,
            "pin_block_format": pin_block_format,
        }
        if primary_account_number is not None:
            input_["primary_account_number"] = primary_account_number
        if pin_data_length is not None:
            input_["pin_data_length"] = pin_data_length
        if dukpt_attributes is not None:
            input_["dukpt_attributes"] = dukpt_attributes
        if encryption_wrapped_key is not None:
            input_["encryption_wrapped_key"] = encryption_wrapped_key

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(self, exc_type: Any, exc: Any, tb: Any):
        await self._client.aclose()
