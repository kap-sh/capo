"""Generated from Smithy shape ``com.amazonaws.snowball#DescribeReturnShippingLabelResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_snowball.types.shipping_label_status
    import capo_snowball.types.string
    import capo_snowball.types.timestamp


class DescribeReturnShippingLabelResult(TypedDict, closed=True):
    status: NotRequired["capo_snowball.types.shipping_label_status.ShippingLabelStatus"]
    """<p>The status information of the task on a Snow device that is being returned to Amazon Web Services.</p>"""
    expiration_date: NotRequired["capo_snowball.types.timestamp.Timestamp"]
    """<p>The expiration date of the current return shipping label.</p>"""
    return_shipping_label_uri: NotRequired["capo_snowball.types.string.String"]
    """<p>The pre-signed Amazon S3 URI used to download the return shipping label.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeReturnShippingLabelResult) -> dict:
    out: dict = {}
    if "status" in value:
        import capo_snowball.types.shipping_label_status

        out["Status"] = (
            capo_snowball.types.shipping_label_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "expiration_date" in value:
        import capo_snowball.types.timestamp

        out["ExpirationDate"] = capo_snowball.types.timestamp.serialize_aws_json_1_1(
            value["expiration_date"]
        )
    if "return_shipping_label_uri" in value:
        out["ReturnShippingLabelURI"] = value["return_shipping_label_uri"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeReturnShippingLabelResult:
    out: DescribeReturnShippingLabelResult = {}  # type: ignore[typeddict-item]
    if data.get("Status") is not None:
        import capo_snowball.types.shipping_label_status

        out["status"] = (
            capo_snowball.types.shipping_label_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    if data.get("ExpirationDate") is not None:
        import capo_snowball.types.timestamp

        out["expiration_date"] = capo_snowball.types.timestamp.deserialize_aws_json_1_1(
            data["ExpirationDate"]
        )
    if data.get("ReturnShippingLabelURI") is not None:
        out["return_shipping_label_uri"] = data["ReturnShippingLabelURI"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DescribeReturnShippingLabelResult) -> dict:
    out: dict = {}
    if "status" in value:
        import capo_snowball.types.shipping_label_status

        out["Status"] = capo_snowball.types.shipping_label_status.serialize_cbor(
            value["status"]
        )
    if "expiration_date" in value:
        import capo_snowball.types.timestamp

        out["ExpirationDate"] = capo_snowball.types.timestamp.serialize_cbor(
            value["expiration_date"]
        )
    if "return_shipping_label_uri" in value:
        out["ReturnShippingLabelURI"] = value["return_shipping_label_uri"]
    return out


def deserialize_cbor(data: dict) -> DescribeReturnShippingLabelResult:
    out: DescribeReturnShippingLabelResult = {}  # type: ignore[typeddict-item]
    if data.get("Status") is not None:
        import capo_snowball.types.shipping_label_status

        out["status"] = capo_snowball.types.shipping_label_status.deserialize_cbor(
            data["Status"]
        )
    if data.get("ExpirationDate") is not None:
        import capo_snowball.types.timestamp

        out["expiration_date"] = capo_snowball.types.timestamp.deserialize_cbor(
            data["ExpirationDate"]
        )
    if data.get("ReturnShippingLabelURI") is not None:
        out["return_shipping_label_uri"] = data["ReturnShippingLabelURI"]
    return out
