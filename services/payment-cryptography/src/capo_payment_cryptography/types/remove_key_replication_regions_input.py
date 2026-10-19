"""Generated from Smithy shape ``com.amazonaws.paymentcryptography#RemoveKeyReplicationRegionsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_payment_cryptography.types.key_arn_or_key_alias_type
    import capo_payment_cryptography.types.regions


class RemoveKeyReplicationRegionsInput(TypedDict, closed=True):
    key_identifier: (
        "capo_payment_cryptography.types.key_arn_or_key_alias_type.KeyArnOrKeyAliasType"
    )
    """<p>The key identifier (ARN or alias) of the key from which to remove replication regions.</p> <p>This key must exist and have replication enabled in the specified regions.</p>"""
    replication_regions: "capo_payment_cryptography.types.regions.Regions"
    """<p>The list of Amazon Web Services Regions to remove from the key's replication configuration.</p> <p>The key will no longer be available for cryptographic operations in these regions after removal. Ensure no active operations depend on the key in these regions before removal.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RemoveKeyReplicationRegionsInput) -> dict:
    out: dict = {}
    out["KeyIdentifier"] = value["key_identifier"]
    import capo_payment_cryptography.types.regions

    out["ReplicationRegions"] = (
        capo_payment_cryptography.types.regions.serialize_aws_json_1_0(
            value["replication_regions"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> RemoveKeyReplicationRegionsInput:
    out: RemoveKeyReplicationRegionsInput = {}  # type: ignore[typeddict-item]
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
