"""Generated from Smithy shape ``com.amazonaws.paymentcryptography#DisableDefaultKeyReplicationRegionsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_payment_cryptography.types.regions


class DisableDefaultKeyReplicationRegionsOutput(TypedDict, closed=True):
    enabled_replication_regions: "capo_payment_cryptography.types.regions.Regions"
    """<p>The remaining list of regions where default key replication is still enabled for the account.</p> <p>This reflects the account's default replication configuration after removing the specified regions.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DisableDefaultKeyReplicationRegionsOutput) -> dict:
    out: dict = {}
    import capo_payment_cryptography.types.regions

    out["EnabledReplicationRegions"] = (
        capo_payment_cryptography.types.regions.serialize_aws_json_1_0(
            value["enabled_replication_regions"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> DisableDefaultKeyReplicationRegionsOutput:
    out: DisableDefaultKeyReplicationRegionsOutput = {}  # type: ignore[typeddict-item]
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
