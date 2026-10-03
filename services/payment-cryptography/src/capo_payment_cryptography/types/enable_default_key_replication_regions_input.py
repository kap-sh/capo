"""Generated from Smithy shape ``com.amazonaws.paymentcryptography#EnableDefaultKeyReplicationRegionsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_payment_cryptography.errors import DeserializationError

if TYPE_CHECKING:
    import capo_payment_cryptography.types.regions


class EnableDefaultKeyReplicationRegionsInput(TypedDict, closed=True):
    replication_regions: "capo_payment_cryptography.types.regions.Regions"
    """<p>The list of Amazon Web Services Regions to enable as default replication regions for the Amazon Web Services account for <a href="https://docs.aws.amazon.com/payment-cryptography/latest/userguide/keys-multi-region-replication.html">Multi-Region key replication</a>.</p> <p>New keys created in this account will automatically be replicated to these regions unless explicitly overridden during key creation.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: EnableDefaultKeyReplicationRegionsInput) -> dict:
    out: dict = {}
    import capo_payment_cryptography.types.regions

    out["ReplicationRegions"] = (
        capo_payment_cryptography.types.regions.serialize_aws_json_1_0(
            value["replication_regions"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> EnableDefaultKeyReplicationRegionsInput:
    out: EnableDefaultKeyReplicationRegionsInput = {}  # type: ignore[typeddict-item]
    if data.get("ReplicationRegions") is not None:
        import capo_payment_cryptography.types.regions

        out["replication_regions"] = (
            capo_payment_cryptography.types.regions.deserialize_aws_json_1_0(
                data["ReplicationRegions"]
            )
        )
    else:
        raise DeserializationError(
            "EnableDefaultKeyReplicationRegionsInput.replication_regions required"
        )
    return out
