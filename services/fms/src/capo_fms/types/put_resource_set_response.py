"""Generated from Smithy shape ``com.amazonaws.fms#PutResourceSetResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_fms.errors import DeserializationError

if TYPE_CHECKING:
    import capo_fms.types.resource_arn
    import capo_fms.types.resource_set


class PutResourceSetResponse(TypedDict, closed=True):
    resource_set: "capo_fms.types.resource_set.ResourceSet"
    """<p>Details about the resource set.</p>"""
    resource_set_arn: "capo_fms.types.resource_arn.ResourceArn"
    """<p>The Amazon Resource Name (ARN) of the resource set.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutResourceSetResponse) -> dict:
    out: dict = {}
    import capo_fms.types.resource_set

    out["ResourceSet"] = capo_fms.types.resource_set.serialize_aws_json_1_1(
        value["resource_set"]
    )
    out["ResourceSetArn"] = value["resource_set_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> PutResourceSetResponse:
    out: PutResourceSetResponse = {}  # type: ignore[typeddict-item]
    if data.get("ResourceSet") is not None:
        import capo_fms.types.resource_set

        out["resource_set"] = capo_fms.types.resource_set.deserialize_aws_json_1_1(
            data["ResourceSet"]
        )
    else:
        raise DeserializationError("PutResourceSetResponse.resource_set required")
    if data.get("ResourceSetArn") is not None:
        out["resource_set_arn"] = data["ResourceSetArn"]
    else:
        out["resource_set_arn"] = ""
    return out
