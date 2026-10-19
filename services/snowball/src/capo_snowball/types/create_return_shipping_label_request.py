"""Generated from Smithy shape ``com.amazonaws.snowball#CreateReturnShippingLabelRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_snowball.types.job_id
    import capo_snowball.types.shipping_option


class CreateReturnShippingLabelRequest(TypedDict, closed=True):
    job_id: "capo_snowball.types.job_id.JobId"
    """<p>The ID for a job that you want to create the return shipping label for; for example, <code>JID123e4567-e89b-12d3-a456-426655440000</code>.</p>"""
    shipping_option: NotRequired["capo_snowball.types.shipping_option.ShippingOption"]
    """<p>The shipping speed for a particular job. This speed doesn't dictate how soon the device is returned to Amazon Web Services. This speed represents how quickly it moves to its destination while in transit. Regional shipping speeds are as follows:</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateReturnShippingLabelRequest) -> dict:
    out: dict = {}
    out["JobId"] = value["job_id"]
    if "shipping_option" in value:
        import capo_snowball.types.shipping_option

        out["ShippingOption"] = (
            capo_snowball.types.shipping_option.serialize_aws_json_1_1(
                value["shipping_option"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateReturnShippingLabelRequest:
    out: CreateReturnShippingLabelRequest = {}  # type: ignore[typeddict-item]
    if data.get("JobId") is not None:
        out["job_id"] = data["JobId"]
    else:
        out["job_id"] = ""
    if data.get("ShippingOption") is not None:
        import capo_snowball.types.shipping_option

        out["shipping_option"] = (
            capo_snowball.types.shipping_option.deserialize_aws_json_1_1(
                data["ShippingOption"]
            )
        )
    return out
