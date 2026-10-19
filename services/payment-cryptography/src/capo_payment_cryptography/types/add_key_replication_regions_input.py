"""Generated from Smithy shape ``com.amazonaws.paymentcryptography#AddKeyReplicationRegionsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_payment_cryptography.types.key_arn_or_key_alias_type
    import capo_payment_cryptography.types.regions


class AddKeyReplicationRegionsInput(TypedDict, closed=True):
    key_identifier: (
        "capo_payment_cryptography.types.key_arn_or_key_alias_type.KeyArnOrKeyAliasType"
    )
    """<p>The key identifier (ARN or alias) of the key for which to add replication regions.</p> <p>This key must exist and be in a valid state for replication operations.</p>"""
    replication_regions: "capo_payment_cryptography.types.regions.Regions"
    """<p>The list of Amazon Web Services Regions to add to the key's replication configuration.</p> <p>Each region must be a valid Amazon Web Services Region where Amazon Web Services Payment Cryptography is available. The key will be replicated to these regions, allowing cryptographic operations to be performed closer to your applications.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AddKeyReplicationRegionsInput) -> dict:
    out: dict = {}
    out["KeyIdentifier"] = value["key_identifier"]
    import capo_payment_cryptography.types.regions

    out["ReplicationRegions"] = (
        capo_payment_cryptography.types.regions.serialize_aws_json_1_0(
            value["replication_regions"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> AddKeyReplicationRegionsInput:
    out: AddKeyReplicationRegionsInput = {}  # type: ignore[typeddict-item]
    if data.get("KeyIdentifier") is not None:
        out["key_identifier"] = data["KeyIdentifier"]
    else:
        out["key_identifier"] = ""
    if data.get("ReplicationRegions") is not None:
        import capo_payment_cryptography.types.regions

        out["replication_regions"] = (
            capo_payment_cryptography.types.regions.deserialize_aws_json_1_0(
                data["ReplicationRegions"]
            )
        )
    else:
        out["replication_regions"] = []
    return out
