"""Generated from Smithy shape ``com.amazonaws.appfabric#AppBundle``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appfabric.types.arn


class AppBundle(TypedDict, closed=True):
    arn: "capo_appfabric.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the app bundle.</p>"""
    customer_managed_key_arn: NotRequired["capo_appfabric.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the Key Management Service (KMS) key used to encrypt the application data.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AppBundle) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    if "customer_managed_key_arn" in value:
        out["customerManagedKeyArn"] = value["customer_managed_key_arn"]
    return out


def deserialize_json(data: dict) -> AppBundle:
    out: AppBundle = {}  # type: ignore[typeddict-item]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        out["arn"] = ""
    if data.get("customerManagedKeyArn") is not None:
        out["customer_managed_key_arn"] = data["customerManagedKeyArn"]
    return out
