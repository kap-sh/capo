"""Generated from Smithy shape ``com.amazonaws.transfer#As2ConnectorConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_transfer.types.as2_async_mdn_connector_config
    import capo_transfer.types.as2_connector_secret_id
    import capo_transfer.types.compression_enum
    import capo_transfer.types.encryption_alg
    import capo_transfer.types.mdn_response
    import capo_transfer.types.mdn_signing_alg
    import capo_transfer.types.message_subject
    import capo_transfer.types.preserve_content_type
    import capo_transfer.types.profile_id
    import capo_transfer.types.signing_alg


class As2ConnectorConfig(TypedDict, closed=True):
    local_profile_id: NotRequired["capo_transfer.types.profile_id.ProfileId"]
    """<p>A unique identifier for the AS2 local profile.</p>"""
    partner_profile_id: NotRequired["capo_transfer.types.profile_id.ProfileId"]
    """<p>A unique identifier for the partner profile for the connector.</p>"""
    message_subject: NotRequired["capo_transfer.types.message_subject.MessageSubject"]
    """<p>Used as the <code>Subject</code> HTTP header attribute in AS2 messages that are being sent with the connector.</p>"""
    compression: NotRequired["capo_transfer.types.compression_enum.CompressionEnum"]
    """<p>Specifies whether the AS2 file is compressed.</p>"""
    encryption_algorithm: NotRequired[
        "capo_transfer.types.encryption_alg.EncryptionAlg"
    ]
    """<p>The algorithm that is used to encrypt the file.</p> <p>Note the following:</p> <ul> <li> <p>Do not use the <code>DES_EDE3_CBC</code> algorithm unless you must support a legacy client that requires it, as it is a weak encryption algorithm.</p> </li> <li> <p>You can only specify <code>NONE</code> if the URL for your connector uses HTTPS. Using HTTPS ensures that no traffic is sent in clear text.</p> </li> </ul>"""
    signing_algorithm: NotRequired["capo_transfer.types.signing_alg.SigningAlg"]
    """<p>The algorithm that is used to sign the AS2 messages sent with the connector.</p>"""
    mdn_signing_algorithm: NotRequired[
        "capo_transfer.types.mdn_signing_alg.MdnSigningAlg"
    ]
    """<p>The signing algorithm for the MDN response.</p> <note> <p>If set to DEFAULT (or not set at all), the value for <code>SigningAlgorithm</code> is used.</p> </note>"""
    mdn_response: NotRequired["capo_transfer.types.mdn_response.MdnResponse"]
    """<p>Used for outbound requests (from an Transfer Family connector to a partner AS2 server) to determine whether the partner response for transfers is synchronous or asynchronous. Specify either of the following values:</p> <ul> <li> <p> <code>ASYNC</code>: The system expects an asynchronous MDN response, confirming that the file was transferred successfully (or not).</p> </li> <li> <p> <code>SYNC</code>: The system expects a synchronous MDN response, confirming that the file was transferred successfully (or not).</p> </li> <li> <p> <code>NONE</code>: Specifies that no MDN response is required.</p> </li> </ul>"""
    basic_auth_secret_id: NotRequired[
        "capo_transfer.types.as2_connector_secret_id.As2ConnectorSecretId"
    ]
    """<p>Provides Basic authentication support to the AS2 Connectors API. To use Basic authentication, you must provide the name or Amazon Resource Name (ARN) of a secret in Secrets Manager.</p> <p>The default value for this parameter is <code>null</code>, which indicates that Basic authentication is not enabled for the connector.</p> <p>If the connector should use Basic authentication, the secret needs to be in the following format:</p> <p> <code>{ "Username": "user-name", "Password": "user-password" }</code> </p> <p>Replace <code>user-name</code> and <code>user-password</code> with the credentials for the actual user that is being authenticated.</p> <p>Note the following:</p> <ul> <li> <p>You are storing these credentials in Secrets Manager, <i>not passing them directly</i> into this API.</p> </li> <li> <p>If you are using the API, SDKs, or CloudFormation to configure your connector, then you must create the secret before you can enable Basic authentication. However, if you are using the Amazon Web Services management console, you can have the system create the secret for you.</p> </li> </ul> <p>If you have previously enabled Basic authentication for a connector, you can disable it by using the <code>UpdateConnector</code> API call. For example, if you are using the CLI, you can run the following command to remove Basic authentication:</p> <p> <code>update-connector --connector-id my-connector-id --as2-config 'BasicAuthSecretId=""'</code> </p>"""
    preserve_content_type: NotRequired[
        "capo_transfer.types.preserve_content_type.PreserveContentType"
    ]
    """<p>Allows you to use the Amazon S3 <code>Content-Type</code> that is associated with objects in S3 instead of having the content type mapped based on the file extension. This parameter is enabled by default when you create an AS2 connector from the console, but disabled by default when you create an AS2 connector by calling the API directly.</p>"""
    async_mdn_config: NotRequired[
        "capo_transfer.types.as2_async_mdn_connector_config.As2AsyncMdnConnectorConfig"
    ]
    """<p>Configuration settings for asynchronous Message Disposition Notification (MDN) responses. This allows you to configure where asynchronous MDN responses should be sent and which servers should handle them.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: As2ConnectorConfig) -> dict:
    out: dict = {}
    if "local_profile_id" in value:
        out["LocalProfileId"] = value["local_profile_id"]
    if "partner_profile_id" in value:
        out["PartnerProfileId"] = value["partner_profile_id"]
    if "message_subject" in value:
        out["MessageSubject"] = value["message_subject"]
    if "compression" in value:
        import capo_transfer.types.compression_enum

        out["Compression"] = (
            capo_transfer.types.compression_enum.serialize_aws_json_1_1(
                value["compression"]
            )
        )
    if "encryption_algorithm" in value:
        import capo_transfer.types.encryption_alg

        out["EncryptionAlgorithm"] = (
            capo_transfer.types.encryption_alg.serialize_aws_json_1_1(
                value["encryption_algorithm"]
            )
        )
    if "signing_algorithm" in value:
        import capo_transfer.types.signing_alg

        out["SigningAlgorithm"] = (
            capo_transfer.types.signing_alg.serialize_aws_json_1_1(
                value["signing_algorithm"]
            )
        )
    if "mdn_signing_algorithm" in value:
        import capo_transfer.types.mdn_signing_alg

        out["MdnSigningAlgorithm"] = (
            capo_transfer.types.mdn_signing_alg.serialize_aws_json_1_1(
                value["mdn_signing_algorithm"]
            )
        )
    if "mdn_response" in value:
        import capo_transfer.types.mdn_response

        out["MdnResponse"] = capo_transfer.types.mdn_response.serialize_aws_json_1_1(
            value["mdn_response"]
        )
    if "basic_auth_secret_id" in value:
        out["BasicAuthSecretId"] = value["basic_auth_secret_id"]
    if "preserve_content_type" in value:
        import capo_transfer.types.preserve_content_type

        out["PreserveContentType"] = (
            capo_transfer.types.preserve_content_type.serialize_aws_json_1_1(
                value["preserve_content_type"]
            )
        )
    if "async_mdn_config" in value:
        import capo_transfer.types.as2_async_mdn_connector_config

        out["AsyncMdnConfig"] = (
            capo_transfer.types.as2_async_mdn_connector_config.serialize_aws_json_1_1(
                value["async_mdn_config"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> As2ConnectorConfig:
    out: As2ConnectorConfig = {}  # type: ignore[typeddict-item]
    if data.get("LocalProfileId") is not None:
        out["local_profile_id"] = data["LocalProfileId"]
    if data.get("PartnerProfileId") is not None:
        out["partner_profile_id"] = data["PartnerProfileId"]
    if data.get("MessageSubject") is not None:
        out["message_subject"] = data["MessageSubject"]
    if data.get("Compression") is not None:
        import capo_transfer.types.compression_enum

        out["compression"] = (
            capo_transfer.types.compression_enum.deserialize_aws_json_1_1(
                data["Compression"]
            )
        )
    if data.get("EncryptionAlgorithm") is not None:
        import capo_transfer.types.encryption_alg

        out["encryption_algorithm"] = (
            capo_transfer.types.encryption_alg.deserialize_aws_json_1_1(
                data["EncryptionAlgorithm"]
            )
        )
    if data.get("SigningAlgorithm") is not None:
        import capo_transfer.types.signing_alg

        out["signing_algorithm"] = (
            capo_transfer.types.signing_alg.deserialize_aws_json_1_1(
                data["SigningAlgorithm"]
            )
        )
    if data.get("MdnSigningAlgorithm") is not None:
        import capo_transfer.types.mdn_signing_alg

        out["mdn_signing_algorithm"] = (
            capo_transfer.types.mdn_signing_alg.deserialize_aws_json_1_1(
                data["MdnSigningAlgorithm"]
            )
        )
    if data.get("MdnResponse") is not None:
        import capo_transfer.types.mdn_response

        out["mdn_response"] = capo_transfer.types.mdn_response.deserialize_aws_json_1_1(
            data["MdnResponse"]
        )
    if data.get("BasicAuthSecretId") is not None:
        out["basic_auth_secret_id"] = data["BasicAuthSecretId"]
    if data.get("PreserveContentType") is not None:
        import capo_transfer.types.preserve_content_type

        out["preserve_content_type"] = (
            capo_transfer.types.preserve_content_type.deserialize_aws_json_1_1(
                data["PreserveContentType"]
            )
        )
    if data.get("AsyncMdnConfig") is not None:
        import capo_transfer.types.as2_async_mdn_connector_config

        out["async_mdn_config"] = (
            capo_transfer.types.as2_async_mdn_connector_config.deserialize_aws_json_1_1(
                data["AsyncMdnConfig"]
            )
        )
    return out
