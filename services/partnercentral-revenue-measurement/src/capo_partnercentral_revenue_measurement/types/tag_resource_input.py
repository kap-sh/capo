"""Generated from Smithy shape ``com.amazonaws.partnercentralrevenuemeasurement#TagResourceInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_partnercentral_revenue_measurement.types.resource_arn
    import capo_partnercentral_revenue_measurement.types.tag_list


class TagResourceInput(TypedDict, closed=True):
    resource_arn: (
        "capo_partnercentral_revenue_measurement.types.resource_arn.ResourceARN"
    )
    """<p>The Amazon Resource Name (ARN) of the resource to tag.</p>"""
    tags: "capo_partnercentral_revenue_measurement.types.tag_list.TagList"
    """<p>The tags to add to the resource.</p>"""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: TagResourceInput) -> dict:
    out: dict = {}
    out["resourceArn"] = value["resource_arn"]
    import capo_partnercentral_revenue_measurement.types.tag_list

    out["tags"] = capo_partnercentral_revenue_measurement.types.tag_list.serialize_cbor(
        value["tags"]
    )
    return out


def deserialize_cbor(data: dict) -> TagResourceInput:
    out: TagResourceInput = {}  # type: ignore[typeddict-item]
    if data.get("resourceArn") is not None:
        out["resource_arn"] = data["resourceArn"]
    else:
        out["resource_arn"] = ""
    if data.get("tags") is not None:
        import capo_partnercentral_revenue_measurement.types.tag_list

        out["tags"] = (
            capo_partnercentral_revenue_measurement.types.tag_list.deserialize_cbor(
                data["tags"]
            )
        )
    else:
        out["tags"] = []
    return out
