"""Generated from Smithy shape ``com.amazonaws.configservice#PutConnectorResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_config_service.types.amazon_resource_name


class PutConnectorResponse(TypedDict, closed=True):
    arn: "capo_config_service.types.amazon_resource_name.AmazonResourceName"
    """<p>The Amazon Resource Name (ARN) of the connector.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutConnectorResponse) -> dict:
    out: dict = {}
    out["Arn"] = value["arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> PutConnectorResponse:
    out: PutConnectorResponse = {}  # type: ignore[typeddict-item]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    else:
        out["arn"] = ""
    return out
