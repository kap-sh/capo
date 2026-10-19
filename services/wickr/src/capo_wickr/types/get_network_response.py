"""Generated from Smithy shape ``com.amazonaws.wickr#GetNetworkResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wickr.types.access_level
    import capo_wickr.types.generic_string
    import capo_wickr.types.network_id


class GetNetworkResponse(TypedDict, closed=True):
    network_id: "capo_wickr.types.network_id.NetworkId"
    """<p>The unique identifier of the network.</p>"""
    network_name: "capo_wickr.types.generic_string.GenericString"
    """<p>The name of the network.</p>"""
    access_level: "capo_wickr.types.access_level.AccessLevel"
    """<p>The access level of the network (STANDARD or PREMIUM), which determines available features and capabilities.</p>"""
    aws_account_id: "capo_wickr.types.generic_string.GenericString"
    """<p>The Amazon Web Services account ID that owns the network.</p>"""
    network_arn: "capo_wickr.types.generic_string.GenericString"
    """<p>The Amazon Resource Name (ARN) of the network.</p>"""
    standing: NotRequired["int"]
    """<p>The current standing or status of the network.</p>"""
    free_trial_expiration: NotRequired["capo_wickr.types.generic_string.GenericString"]
    """<p>The expiration date and time for the network's free trial period, if applicable.</p>"""
    migration_state: NotRequired["int"]
    """<p>The SSO redirect URI migration state, managed by the SSO redirect migration wizard. Values: 0 (not started), 1 (in progress), or 2 (completed).</p>"""
    encryption_key_arn: NotRequired["capo_wickr.types.generic_string.GenericString"]
    """<p>The ARN of the Amazon Web Services KMS customer managed key used for encrypting sensitive data in the network.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetNetworkResponse) -> dict:
    out: dict = {}
    out["networkId"] = value["network_id"]
    out["networkName"] = value["network_name"]
    import capo_wickr.types.access_level

    out["accessLevel"] = capo_wickr.types.access_level.serialize_json(
        value["access_level"]
    )
    out["awsAccountId"] = value["aws_account_id"]
    out["networkArn"] = value["network_arn"]
    if "standing" in value:
        out["standing"] = value["standing"]
    if "free_trial_expiration" in value:
        out["freeTrialExpiration"] = value["free_trial_expiration"]
    if "migration_state" in value:
        out["migrationState"] = value["migration_state"]
    if "encryption_key_arn" in value:
        out["encryptionKeyArn"] = value["encryption_key_arn"]
    return out


def deserialize_json(data: dict) -> GetNetworkResponse:
    out: GetNetworkResponse = {}  # type: ignore[typeddict-item]
    if data.get("networkId") is not None:
        out["network_id"] = data["networkId"]
    else:
        out["network_id"] = ""
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
    if data.get("awsAccountId") is not None:
        out["aws_account_id"] = data["awsAccountId"]
    else:
        out["aws_account_id"] = ""
    if data.get("networkArn") is not None:
        out["network_arn"] = data["networkArn"]
    else:
        out["network_arn"] = ""
    if data.get("standing") is not None:
        out["standing"] = data["standing"]
    if data.get("freeTrialExpiration") is not None:
        out["free_trial_expiration"] = data["freeTrialExpiration"]
    if data.get("migrationState") is not None:
        out["migration_state"] = data["migrationState"]
    if data.get("encryptionKeyArn") is not None:
        out["encryption_key_arn"] = data["encryptionKeyArn"]
    return out
