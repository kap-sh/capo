"""Generated from Smithy shape ``com.amazonaws.quicksight#DataSourceCredentials``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.copy_source_arn
    import capo_quicksight.types.credential_pair
    import capo_quicksight.types.key_pair_credentials
    import capo_quicksight.types.o_auth_client_credentials
    import capo_quicksight.types.secret_arn
    import capo_quicksight.types.web_proxy_credentials


class DataSourceCredentials(TypedDict, closed=True):
    credential_pair: NotRequired["capo_quicksight.types.credential_pair.CredentialPair"]
    """<p>Credential pair. For more information, see <code> <a href="https://docs.aws.amazon.com/quicksight/latest/APIReference/API_CredentialPair.html">CredentialPair</a> </code>.</p>"""
    copy_source_arn: NotRequired["capo_quicksight.types.copy_source_arn.CopySourceArn"]
    """<p>The Amazon Resource Name (ARN) of a data source that has the credential pair that you want to use. When <code>CopySourceArn</code> is not null, the credential pair from the data source in the ARN is used as the credentials for the <code>DataSourceCredentials</code> structure.</p>"""
    secret_arn: NotRequired["capo_quicksight.types.secret_arn.SecretArn"]
    """<p>The Amazon Resource Name (ARN) of the secret associated with the data source in Amazon Secrets Manager.</p>"""
    key_pair_credentials: NotRequired[
        "capo_quicksight.types.key_pair_credentials.KeyPairCredentials"
    ]
    """<p>The credentials for connecting using key-pair.</p>"""
    web_proxy_credentials: NotRequired[
        "capo_quicksight.types.web_proxy_credentials.WebProxyCredentials"
    ]
    """<p>The credentials for connecting through a web proxy server.</p>"""
    o_auth_client_credentials: NotRequired[
        "capo_quicksight.types.o_auth_client_credentials.OAuthClientCredentials"
    ]
    """<p>The OAuth client credentials for connecting to a data source using OAuth 2.0 client credentials (2LO) authentication. For more information, see <code> <a href="https://docs.aws.amazon.com/quicksight/latest/APIReference/API_OAuthClientCredentials.html">OAuthClientCredentials</a> </code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataSourceCredentials) -> dict:
    out: dict = {}
    if "credential_pair" in value:
        import capo_quicksight.types.credential_pair

        out["CredentialPair"] = capo_quicksight.types.credential_pair.serialize_json(
            value["credential_pair"]
        )
    if "copy_source_arn" in value:
        out["CopySourceArn"] = value["copy_source_arn"]
    if "secret_arn" in value:
        out["SecretArn"] = value["secret_arn"]
    if "key_pair_credentials" in value:
        import capo_quicksight.types.key_pair_credentials

        out["KeyPairCredentials"] = (
            capo_quicksight.types.key_pair_credentials.serialize_json(
                value["key_pair_credentials"]
            )
        )
    if "web_proxy_credentials" in value:
        import capo_quicksight.types.web_proxy_credentials

        out["WebProxyCredentials"] = (
            capo_quicksight.types.web_proxy_credentials.serialize_json(
                value["web_proxy_credentials"]
            )
        )
    if "o_auth_client_credentials" in value:
        import capo_quicksight.types.o_auth_client_credentials

        out["OAuthClientCredentials"] = (
            capo_quicksight.types.o_auth_client_credentials.serialize_json(
                value["o_auth_client_credentials"]
            )
        )
    return out


def deserialize_json(data: dict) -> DataSourceCredentials:
    out: DataSourceCredentials = {}  # type: ignore[typeddict-item]
    if data.get("CredentialPair") is not None:
        import capo_quicksight.types.credential_pair

        out["credential_pair"] = capo_quicksight.types.credential_pair.deserialize_json(
            data["CredentialPair"]
        )
    if data.get("CopySourceArn") is not None:
        out["copy_source_arn"] = data["CopySourceArn"]
    if data.get("SecretArn") is not None:
        out["secret_arn"] = data["SecretArn"]
    if data.get("KeyPairCredentials") is not None:
        import capo_quicksight.types.key_pair_credentials

        out["key_pair_credentials"] = (
            capo_quicksight.types.key_pair_credentials.deserialize_json(
                data["KeyPairCredentials"]
            )
        )
    if data.get("WebProxyCredentials") is not None:
        import capo_quicksight.types.web_proxy_credentials

        out["web_proxy_credentials"] = (
            capo_quicksight.types.web_proxy_credentials.deserialize_json(
                data["WebProxyCredentials"]
            )
        )
    if data.get("OAuthClientCredentials") is not None:
        import capo_quicksight.types.o_auth_client_credentials

        out["o_auth_client_credentials"] = (
            capo_quicksight.types.o_auth_client_credentials.deserialize_json(
                data["OAuthClientCredentials"]
            )
        )
    return out
