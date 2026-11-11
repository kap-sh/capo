"""Generated from Smithy shape ``com.amazonaws.lightsail#PasswordData``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lightsail.types.resource_name
    import capo_lightsail.types.sensitive_string


class PasswordData(TypedDict, closed=True):
    ciphertext: NotRequired["capo_lightsail.types.sensitive_string.SensitiveString"]
    """<p>The encrypted password. Ciphertext will be an empty string if access to your new instance is not ready yet. When you create an instance, it can take up to 15 minutes for the instance to be ready.</p> <note> <p>If you use the default key pair (<code>LightsailDefaultKeyPair</code>), the decrypted password will be available in the password field.</p> <p>If you are using a custom key pair, you need to use your own means of decryption.</p> <p>If you change the Administrator password on the instance, Lightsail will continue to return the original ciphertext value. When accessing the instance using RDP, you need to manually enter the Administrator password after changing it from the default.</p> </note>"""
    key_pair_name: NotRequired["capo_lightsail.types.resource_name.ResourceName"]
    """<p>The name of the key pair that you used when creating your instance. If no key pair name was specified when creating the instance, Lightsail uses the default key pair (<code>LightsailDefaultKeyPair</code>).</p> <p>If you are using a custom key pair, you need to use your own means of decrypting your password using the <code>ciphertext</code>. Lightsail creates the ciphertext by encrypting your password with the public key part of this key pair.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PasswordData) -> dict:
    out: dict = {}
    if "ciphertext" in value:
        out["ciphertext"] = value["ciphertext"]
    if "key_pair_name" in value:
        out["keyPairName"] = value["key_pair_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> PasswordData:
    out: PasswordData = {}  # type: ignore[typeddict-item]
    if data.get("ciphertext") is not None:
        out["ciphertext"] = data["ciphertext"]
    if data.get("keyPairName") is not None:
        out["key_pair_name"] = data["keyPairName"]
    return out


def redact_sensitive(value: PasswordData) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "ciphertext" in value:
        out["ciphertext"] = "*** Sensitive Data Redacted ***"
    return out
