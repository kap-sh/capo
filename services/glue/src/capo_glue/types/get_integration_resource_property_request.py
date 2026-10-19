"""Generated from Smithy shape ``com.amazonaws.glue#GetIntegrationResourcePropertyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_glue.types.string512


class GetIntegrationResourcePropertyRequest(TypedDict, closed=True):
    resource_arn: "capo_glue.types.string512.String512"
    """<p>The connection ARN of the source, or the database ARN of the target.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetIntegrationResourcePropertyRequest) -> dict:
    out: dict = {}
    out["ResourceArn"] = value["resource_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetIntegrationResourcePropertyRequest:
    out: GetIntegrationResourcePropertyRequest = {}  # type: ignore[typeddict-item]
    if data.get("ResourceArn") is not None:
        out["resource_arn"] = data["ResourceArn"]
    else:
        out["resource_arn"] = ""
    return out
