"""Generated from Smithy shape ``com.amazonaws.paymentcryptography#DisableDefaultKeyReplicationRegionsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_payment_cryptography.types.regions


class DisableDefaultKeyReplicationRegionsInput(TypedDict, closed=True):
    replication_regions: "capo_payment_cryptography.types.regions.Regions"
    """<p>The list of Amazon Web Services Regions to remove from the account's default replication regions.</p> <p>New keys created after this operation will not automatically be replicated to these regions, though existing keys with replication to these regions will be unaffected.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DisableDefaultKeyReplicationRegionsInput) -> dict:
    out: dict = {}
    import capo_payment_cryptography.types.regions

    out["ReplicationRegions"] = (
        capo_payment_cryptography.types.regions.serialize_aws_json_1_0(
            value["replication_regions"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> DisableDefaultKeyReplicationRegionsInput:
    out: DisableDefaultKeyReplicationRegionsInput = {}  # type: ignore[typeddict-item]
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
