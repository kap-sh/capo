"""Generated from Smithy shape ``com.amazonaws.paymentcryptography#GetDefaultKeyReplicationRegionsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_payment_cryptography.types.regions


class GetDefaultKeyReplicationRegionsOutput(TypedDict, closed=True):
    enabled_replication_regions: "capo_payment_cryptography.types.regions.Regions"
    """<p>The list of regions where default key replication is currently enabled for the account.</p> <p>New keys created in this account will automatically be replicated to these regions unless explicitly configured otherwise during key creation.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetDefaultKeyReplicationRegionsOutput) -> dict:
    out: dict = {}
    import capo_payment_cryptography.types.regions

    out["EnabledReplicationRegions"] = (
        capo_payment_cryptography.types.regions.serialize_aws_json_1_0(
            value["enabled_replication_regions"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> GetDefaultKeyReplicationRegionsOutput:
    out: GetDefaultKeyReplicationRegionsOutput = {}  # type: ignore[typeddict-item]
    if data.get("EnabledReplicationRegions") is not None:
        import capo_payment_cryptography.types.regions

        out["enabled_replication_regions"] = (
            capo_payment_cryptography.types.regions.deserialize_aws_json_1_0(
                data["EnabledReplicationRegions"]
            )
        )
    else:
        out["enabled_replication_regions"] = []
    return out
