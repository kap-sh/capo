"""Generated from Smithy shape ``com.amazonaws.shield#DisableApplicationLayerAutomaticResponseRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_shield.types.resource_arn


class DisableApplicationLayerAutomaticResponseRequest(TypedDict, closed=True):
    resource_arn: "capo_shield.types.resource_arn.ResourceArn"
    """<p>The ARN (Amazon Resource Name) of the protected resource.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: DisableApplicationLayerAutomaticResponseRequest,
) -> dict:
    out: dict = {}
    out["ResourceArn"] = value["resource_arn"]
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> DisableApplicationLayerAutomaticResponseRequest:
    out: DisableApplicationLayerAutomaticResponseRequest = {}  # type: ignore[typeddict-item]
    if data.get("ResourceArn") is not None:
        out["resource_arn"] = data["ResourceArn"]
    else:
        out["resource_arn"] = ""
    return out
