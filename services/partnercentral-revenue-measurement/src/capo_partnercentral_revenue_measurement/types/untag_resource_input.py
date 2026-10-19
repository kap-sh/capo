"""Generated from Smithy shape ``com.amazonaws.partnercentralrevenuemeasurement#UntagResourceInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_partnercentral_revenue_measurement.types.resource_arn
    import capo_partnercentral_revenue_measurement.types.tag_key_list


class UntagResourceInput(TypedDict, closed=True):
    resource_arn: (
        "capo_partnercentral_revenue_measurement.types.resource_arn.ResourceARN"
    )
    """<p>The Amazon Resource Name (ARN) of the resource to remove tags from.</p>"""
    tag_keys: "capo_partnercentral_revenue_measurement.types.tag_key_list.TagKeyList"
    """<p>The tag keys to remove from the resource.</p>"""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: UntagResourceInput) -> dict:
    out: dict = {}
    out["resourceArn"] = value["resource_arn"]
    import capo_partnercentral_revenue_measurement.types.tag_key_list

    out["tagKeys"] = (
        capo_partnercentral_revenue_measurement.types.tag_key_list.serialize_cbor(
            value["tag_keys"]
        )
    )
    return out


def deserialize_cbor(data: dict) -> UntagResourceInput:
    out: UntagResourceInput = {}  # type: ignore[typeddict-item]
    if data.get("resourceArn") is not None:
        out["resource_arn"] = data["resourceArn"]
    else:
        out["resource_arn"] = ""
    if data.get("tagKeys") is not None:
        import capo_partnercentral_revenue_measurement.types.tag_key_list

        out["tag_keys"] = (
            capo_partnercentral_revenue_measurement.types.tag_key_list.deserialize_cbor(
                data["tagKeys"]
            )
        )
    else:
        out["tag_keys"] = []
    return out
