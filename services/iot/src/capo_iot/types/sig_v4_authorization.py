"""Generated from Smithy shape ``com.amazonaws.iot#SigV4Authorization``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iot.types.aws_arn
    import capo_iot.types.service_name
    import capo_iot.types.signing_region


class SigV4Authorization(TypedDict, closed=True):
    signing_region: "capo_iot.types.signing_region.SigningRegion"
    """<p>The signing region.</p>"""
    service_name: "capo_iot.types.service_name.ServiceName"
    """<p>The service name to use while signing with Sig V4.</p>"""
    role_arn: "capo_iot.types.aws_arn.AwsArn"
    """<p>The ARN of the signing role.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SigV4Authorization) -> dict:
    out: dict = {}
    out["signingRegion"] = value["signing_region"]
    out["serviceName"] = value["service_name"]
    out["roleArn"] = value["role_arn"]
    return out


def deserialize_json(data: dict) -> SigV4Authorization:
    out: SigV4Authorization = {}  # type: ignore[typeddict-item]
    if data.get("signingRegion") is not None:
        out["signing_region"] = data["signingRegion"]
    else:
        out["signing_region"] = ""
    if data.get("serviceName") is not None:
        out["service_name"] = data["serviceName"]
    else:
        out["service_name"] = ""
    if data.get("roleArn") is not None:
        out["role_arn"] = data["roleArn"]
    else:
        out["role_arn"] = ""
    return out
