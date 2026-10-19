"""Generated from Smithy shape ``com.amazonaws.wickr#CreateNetworkRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wickr.types.access_level
    import capo_wickr.types.generic_string


class CreateNetworkRequest(TypedDict, closed=True):
    network_name: "capo_wickr.types.generic_string.GenericString"
    """<p>The name for the new network. Must be between 1 and 20 characters.</p>"""
    access_level: "capo_wickr.types.access_level.AccessLevel"
    """<p>The access level for the network. Valid values are STANDARD or PREMIUM, which determine the features and capabilities available to network members.</p>"""
    enable_premium_free_trial: NotRequired["bool"]
    """<p>Specifies whether to enable a premium free trial for the network. It is optional and has a default value as false. When set to true, the network starts with premium features for a limited trial period. </p>"""
    encryption_key_arn: NotRequired["capo_wickr.types.generic_string.GenericString"]
    """<p>The ARN of the Amazon Web Services KMS customer managed key to use for encrypting sensitive data in the network.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateNetworkRequest) -> dict:
    out: dict = {}
    out["networkName"] = value["network_name"]
    import capo_wickr.types.access_level

    out["accessLevel"] = capo_wickr.types.access_level.serialize_json(
        value["access_level"]
    )
    if "enable_premium_free_trial" in value:
        out["enablePremiumFreeTrial"] = value["enable_premium_free_trial"]
    if "encryption_key_arn" in value:
        out["encryptionKeyArn"] = value["encryption_key_arn"]
    return out


def deserialize_json(data: dict) -> CreateNetworkRequest:
    out: CreateNetworkRequest = {}  # type: ignore[typeddict-item]
    if data.get("networkName") is not None:
        out["network_name"] = data["networkName"]
    else:
        out["network_name"] = ""
    if data.get("accessLevel") is not None:
        import capo_wickr.types.access_level

        out["access_level"] = capo_wickr.types.access_level.deserialize_json(
            data["accessLevel"]
        )
    else:
        import typing

        out["access_level"] = typing.cast(
            "capo_wickr.types.access_level.AccessLevel", ""
        )
    if data.get("enablePremiumFreeTrial") is not None:
        out["enable_premium_free_trial"] = data["enablePremiumFreeTrial"]
    if data.get("encryptionKeyArn") is not None:
        out["encryption_key_arn"] = data["encryptionKeyArn"]
    return out
