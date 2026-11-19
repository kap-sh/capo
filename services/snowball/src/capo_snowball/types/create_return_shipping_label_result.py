"""Generated from Smithy shape ``com.amazonaws.snowball#CreateReturnShippingLabelResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_snowball.types.shipping_label_status


class CreateReturnShippingLabelResult(TypedDict, closed=True):
    status: NotRequired["capo_snowball.types.shipping_label_status.ShippingLabelStatus"]
    """<p>The status information of the task on a Snow device that is being returned to Amazon Web Services.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateReturnShippingLabelResult) -> dict:
    out: dict = {}
    if "status" in value:
        import capo_snowball.types.shipping_label_status

        out["Status"] = (
            capo_snowball.types.shipping_label_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateReturnShippingLabelResult:
    out: CreateReturnShippingLabelResult = {}  # type: ignore[typeddict-item]
    if data.get("Status") is not None:
        import capo_snowball.types.shipping_label_status

        out["status"] = (
            capo_snowball.types.shipping_label_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: CreateReturnShippingLabelResult) -> dict:
    out: dict = {}
    if "status" in value:
        import capo_snowball.types.shipping_label_status

        out["Status"] = capo_snowball.types.shipping_label_status.serialize_cbor(
            value["status"]
        )
    return out


def deserialize_cbor(data: dict) -> CreateReturnShippingLabelResult:
    out: CreateReturnShippingLabelResult = {}  # type: ignore[typeddict-item]
    if data.get("Status") is not None:
        import capo_snowball.types.shipping_label_status

        out["status"] = capo_snowball.types.shipping_label_status.deserialize_cbor(
            data["Status"]
        )
    return out
