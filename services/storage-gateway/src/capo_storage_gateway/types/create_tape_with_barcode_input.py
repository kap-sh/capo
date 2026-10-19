"""Generated from Smithy shape ``com.amazonaws.storagegateway#CreateTapeWithBarcodeInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_storage_gateway.errors import DeserializationError

if TYPE_CHECKING:
    import capo_storage_gateway.types.boolean
    import capo_storage_gateway.types.boolean2
    import capo_storage_gateway.types.gateway_arn
    import capo_storage_gateway.types.kms_key
    import capo_storage_gateway.types.pool_id
    import capo_storage_gateway.types.tags
    import capo_storage_gateway.types.tape_barcode
    import capo_storage_gateway.types.tape_size


class CreateTapeWithBarcodeInput(TypedDict, closed=True):
    gateway_arn: "capo_storage_gateway.types.gateway_arn.GatewayARN"
    """<p>The unique Amazon Resource Name (ARN) that represents the gateway to associate the virtual tape with. Use the <a>ListGateways</a> operation to return a list of gateways for your account and Amazon Web Services Region.</p>"""
    tape_size_in_bytes: "capo_storage_gateway.types.tape_size.TapeSize"
    """<p>The size, in bytes, of the virtual tape that you want to create.</p> <note> <p>The size must be aligned by gigabyte (1024*1024*1024 bytes).</p> </note>"""
    tape_barcode: "capo_storage_gateway.types.tape_barcode.TapeBarcode"
    """<p>The barcode that you want to assign to the tape.</p> <note> <p>Barcodes cannot be reused. This includes barcodes used for tapes that have been deleted.</p> </note>"""
    kms_encrypted: NotRequired["capo_storage_gateway.types.boolean.Boolean"]
    """<p>Set to <code>true</code> to use Amazon S3 server-side encryption with your own KMS key, or <code>false</code> to use a key managed by Amazon S3. Optional.</p> <p>Valid Values: <code>true</code> | <code>false</code> </p>"""
    kms_key: NotRequired["capo_storage_gateway.types.kms_key.KMSKey"]
    """<p>The Amazon Resource Name (ARN) of a symmetric customer master key (CMK) used for Amazon S3 server-side encryption. Storage Gateway does not support asymmetric CMKs. This value can only be set when <code>KMSEncrypted</code> is <code>true</code>. Optional.</p>"""
    pool_id: NotRequired["capo_storage_gateway.types.pool_id.PoolId"]
    """<p>The ID of the pool that you want to add your tape to for archiving. The tape in this pool is archived in the S3 storage class that is associated with the pool. When you use your backup application to eject the tape, the tape is archived directly into the storage class (S3 Glacier or S3 Deep Archive) that corresponds to the pool.</p>"""
    worm: NotRequired["capo_storage_gateway.types.boolean2.Boolean2"]
    """<p>Set to <code>TRUE</code> if the tape you are creating is to be configured as a write-once-read-many (WORM) tape.</p>"""
    tags: NotRequired["capo_storage_gateway.types.tags.Tags"]
    """<p>A list of up to 50 tags that can be assigned to a virtual tape that has a barcode. Each tag is a key-value pair.</p> <note> <p>Valid characters for key and value are letters, spaces, and numbers representable in UTF-8 format, and the following special characters: + - = . _ : / @. The maximum length of a tag's key is 128 characters, and the maximum length for a tag's value is 256.</p> </note>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateTapeWithBarcodeInput) -> dict:
    out: dict = {}
    out["GatewayARN"] = value["gateway_arn"]
    out["TapeSizeInBytes"] = value["tape_size_in_bytes"]
    out["TapeBarcode"] = value["tape_barcode"]
    if "kms_encrypted" in value:
        out["KMSEncrypted"] = value["kms_encrypted"]
    if "kms_key" in value:
        out["KMSKey"] = value["kms_key"]
    if "pool_id" in value:
        out["PoolId"] = value["pool_id"]
    if "worm" in value:
        out["Worm"] = value["worm"]
    if "tags" in value:
        import capo_storage_gateway.types.tags

        out["Tags"] = capo_storage_gateway.types.tags.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateTapeWithBarcodeInput:
    out: CreateTapeWithBarcodeInput = {}  # type: ignore[typeddict-item]
    if data.get("GatewayARN") is not None:
        out["gateway_arn"] = data["GatewayARN"]
    else:
        raise DeserializationError("CreateTapeWithBarcodeInput.gateway_arn required")
    if data.get("TapeSizeInBytes") is not None:
        out["tape_size_in_bytes"] = data["TapeSizeInBytes"]
    else:
        raise DeserializationError(
            "CreateTapeWithBarcodeInput.tape_size_in_bytes required"
        )
    if data.get("TapeBarcode") is not None:
        out["tape_barcode"] = data["TapeBarcode"]
    else:
        raise DeserializationError("CreateTapeWithBarcodeInput.tape_barcode required")
    if data.get("KMSEncrypted") is not None:
        out["kms_encrypted"] = data["KMSEncrypted"]
    if data.get("KMSKey") is not None:
        out["kms_key"] = data["KMSKey"]
    if data.get("PoolId") is not None:
        out["pool_id"] = data["PoolId"]
    if data.get("Worm") is not None:
        out["worm"] = data["Worm"]
    if data.get("Tags") is not None:
        import capo_storage_gateway.types.tags

        out["tags"] = capo_storage_gateway.types.tags.deserialize_aws_json_1_1(
            data["Tags"]
        )
    return out
