"""Generated from Smithy shape ``com.amazonaws.kms#DisconnectCustomKeyStoreRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_kms.types.custom_key_store_id_type


class DisconnectCustomKeyStoreRequest(TypedDict, closed=True):
    custom_key_store_id: "capo_kms.types.custom_key_store_id_type.CustomKeyStoreIdType"
    """<p>Enter the ID of the custom key store you want to disconnect. To find the ID of a custom key store, use the <a>DescribeCustomKeyStores</a> operation.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DisconnectCustomKeyStoreRequest) -> dict:
    out: dict = {}
    out["CustomKeyStoreId"] = value["custom_key_store_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DisconnectCustomKeyStoreRequest:
    out: DisconnectCustomKeyStoreRequest = {}  # type: ignore[typeddict-item]
    if data.get("CustomKeyStoreId") is not None:
        out["custom_key_store_id"] = data["CustomKeyStoreId"]
    else:
        out["custom_key_store_id"] = ""
    return out
