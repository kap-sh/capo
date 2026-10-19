"""Generated from Smithy shape ``com.amazonaws.licensemanager#RejectGrantRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_license_manager.types.arn


class RejectGrantRequest(TypedDict, closed=True):
    grant_arn: "capo_license_manager.types.arn.Arn"
    """<p>Amazon Resource Name (ARN) of the grant.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RejectGrantRequest) -> dict:
    out: dict = {}
    out["GrantArn"] = value["grant_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RejectGrantRequest:
    out: RejectGrantRequest = {}  # type: ignore[typeddict-item]
    if data.get("GrantArn") is not None:
        out["grant_arn"] = data["GrantArn"]
    else:
        out["grant_arn"] = ""
    return out
