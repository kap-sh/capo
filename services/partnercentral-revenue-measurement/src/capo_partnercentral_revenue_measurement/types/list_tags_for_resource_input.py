"""Generated from Smithy shape ``com.amazonaws.partnercentralrevenuemeasurement#ListTagsForResourceInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_partnercentral_revenue_measurement.types.resource_arn


class ListTagsForResourceInput(TypedDict, closed=True):
    resource_arn: (
        "capo_partnercentral_revenue_measurement.types.resource_arn.ResourceARN"
    )
    """<p>The Amazon Resource Name (ARN) of the resource to list tags for.</p>"""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListTagsForResourceInput) -> dict:
    out: dict = {}
    out["resourceArn"] = value["resource_arn"]
    return out


def deserialize_cbor(data: dict) -> ListTagsForResourceInput:
    out: ListTagsForResourceInput = {}  # type: ignore[typeddict-item]
    if data.get("resourceArn") is not None:
        out["resource_arn"] = data["resourceArn"]
    else:
        out["resource_arn"] = ""
    return out
