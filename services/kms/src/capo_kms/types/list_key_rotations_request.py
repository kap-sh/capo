"""Generated from Smithy shape ``com.amazonaws.kms#ListKeyRotationsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kms.types.include_key_material
    import capo_kms.types.key_id_type
    import capo_kms.types.limit_type
    import capo_kms.types.marker_type


class ListKeyRotationsRequest(TypedDict, closed=True):
    key_id: "capo_kms.types.key_id_type.KeyIdType"
    """<p>Gets the key rotations for the specified KMS key.</p> <p>Specify the key ID or key ARN of the KMS key.</p> <p>For example:</p> <ul> <li> <p>Key ID: <code>1234abcd-12ab-34cd-56ef-1234567890ab</code> </p> </li> <li> <p>Key ARN: <code>arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab</code> </p> </li> </ul> <p>To get the key ID and key ARN for a KMS key, use <a>ListKeys</a> or <a>DescribeKey</a>.</p>"""
    include_key_material: NotRequired[
        "capo_kms.types.include_key_material.IncludeKeyMaterial"
    ]
    """<p>Use this optional parameter to control which key materials associated with this key are listed in the response. The default value of this parameter is <code>ROTATIONS_ONLY</code>. If you omit this parameter, KMS returns information on the key materials created by automatic or on-demand key rotation. When you specify a value of <code>ALL_KEY_MATERIAL</code>, KMS adds the first key material and any imported key material pending rotation to the response. This parameter can only be used with KMS keys that support automatic or on-demand key rotation. </p>"""
    limit: NotRequired["capo_kms.types.limit_type.LimitType"]
    """<p>Use this parameter to specify the maximum number of items to return. When this value is present, KMS does not return more than the specified number of items, but it might return fewer.</p> <p>This value is optional. If you include a value, it must be between 1 and 1000, inclusive. If you do not include a value, it defaults to 100.</p>"""
    marker: NotRequired["capo_kms.types.marker_type.MarkerType"]
    """<p>Use this parameter in a subsequent request after you receive a response with truncated results. Set it to the value of <code>NextMarker</code> from the truncated response you just received.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListKeyRotationsRequest) -> dict:
    out: dict = {}
    out["KeyId"] = value["key_id"]
    if "include_key_material" in value:
        import capo_kms.types.include_key_material

        out["IncludeKeyMaterial"] = (
            capo_kms.types.include_key_material.serialize_aws_json_1_1(
                value["include_key_material"]
            )
        )
    if "limit" in value:
        out["Limit"] = value["limit"]
    if "marker" in value:
        out["Marker"] = value["marker"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListKeyRotationsRequest:
    out: ListKeyRotationsRequest = {}  # type: ignore[typeddict-item]
    if data.get("KeyId") is not None:
        out["key_id"] = data["KeyId"]
    else:
        out["key_id"] = ""
    if data.get("IncludeKeyMaterial") is not None:
        import capo_kms.types.include_key_material

        out["include_key_material"] = (
            capo_kms.types.include_key_material.deserialize_aws_json_1_1(
                data["IncludeKeyMaterial"]
            )
        )
    if data.get("Limit") is not None:
        out["limit"] = data["Limit"]
    if data.get("Marker") is not None:
        out["marker"] = data["Marker"]
    return out
