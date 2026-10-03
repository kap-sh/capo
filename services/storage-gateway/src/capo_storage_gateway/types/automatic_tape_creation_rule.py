"""Generated from Smithy shape ``com.amazonaws.storagegateway#AutomaticTapeCreationRule``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_storage_gateway.errors import DeserializationError

if TYPE_CHECKING:
    import capo_storage_gateway.types.boolean2
    import capo_storage_gateway.types.minimum_num_tapes
    import capo_storage_gateway.types.pool_id
    import capo_storage_gateway.types.tape_barcode_prefix
    import capo_storage_gateway.types.tape_size


class AutomaticTapeCreationRule(TypedDict, closed=True):
    tape_barcode_prefix: (
        "capo_storage_gateway.types.tape_barcode_prefix.TapeBarcodePrefix"
    )
    """<p>A prefix that you append to the barcode of the virtual tape that you are creating. This prefix makes the barcode unique.</p> <note> <p>The prefix must be 1-4 characters in length and must be one of the uppercase letters from A to Z.</p> </note>"""
    pool_id: "capo_storage_gateway.types.pool_id.PoolId"
    """<p>The ID of the pool that you want to add your tape to for archiving. The tape in this pool is archived in the Amazon S3 storage class that is associated with the pool. When you use your backup application to eject the tape, the tape is archived directly into the storage class (S3 Glacier or S3 Glacier Deep Archive) that corresponds to the pool.</p>"""
    tape_size_in_bytes: "capo_storage_gateway.types.tape_size.TapeSize"
    """<p>The size, in bytes, of the virtual tape capacity.</p>"""
    minimum_num_tapes: "capo_storage_gateway.types.minimum_num_tapes.MinimumNumTapes"
    """<p>The minimum number of available virtual tapes that the gateway maintains at all times. If the number of tapes on the gateway goes below this value, the gateway creates as many new tapes as are needed to have <code>MinimumNumTapes</code> on the gateway. For more information about automatic tape creation, see <a href="https://docs.aws.amazon.com/storagegateway/latest/userguide/GettingStartedCreateTapes.html#CreateTapesAutomatically">Creating Tapes Automatically</a>.</p>"""
    worm: "capo_storage_gateway.types.boolean2.Boolean2"
    """<p>Set to <code>true</code> to indicate that tapes are to be archived as write-once-read-many (WORM). Set to <code>false</code> when WORM is not enabled for tapes.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AutomaticTapeCreationRule) -> dict:
    out: dict = {}
    out["TapeBarcodePrefix"] = value["tape_barcode_prefix"]
    out["PoolId"] = value["pool_id"]
    out["TapeSizeInBytes"] = value["tape_size_in_bytes"]
    out["MinimumNumTapes"] = value["minimum_num_tapes"]
    out["Worm"] = value.get("worm", False)
    return out


def deserialize_aws_json_1_1(data: dict) -> AutomaticTapeCreationRule:
    out: AutomaticTapeCreationRule = {}  # type: ignore[typeddict-item]
    if data.get("TapeBarcodePrefix") is not None:
        out["tape_barcode_prefix"] = data["TapeBarcodePrefix"]
    else:
        raise DeserializationError(
            "AutomaticTapeCreationRule.tape_barcode_prefix required"
        )
    if data.get("PoolId") is not None:
        out["pool_id"] = data["PoolId"]
    else:
        raise DeserializationError("AutomaticTapeCreationRule.pool_id required")
    if data.get("TapeSizeInBytes") is not None:
        out["tape_size_in_bytes"] = data["TapeSizeInBytes"]
    else:
        raise DeserializationError(
            "AutomaticTapeCreationRule.tape_size_in_bytes required"
        )
    if data.get("MinimumNumTapes") is not None:
        out["minimum_num_tapes"] = data["MinimumNumTapes"]
    else:
        raise DeserializationError(
            "AutomaticTapeCreationRule.minimum_num_tapes required"
        )
    if data.get("Worm") is not None:
        out["worm"] = data["Worm"]
    else:
        out["worm"] = False
    return out
