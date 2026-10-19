"""Generated from Smithy shape ``com.amazonaws.cloudhsm#DeleteHsmRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cloudhsm.types.hsm_arn


class DeleteHsmRequest(TypedDict, closed=True):
    hsm_arn: "capo_cloudhsm.types.hsm_arn.HsmArn"
    """<p>The ARN of the HSM to delete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteHsmRequest) -> dict:
    out: dict = {}
    out["HsmArn"] = value["hsm_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteHsmRequest:
    out: DeleteHsmRequest = {}  # type: ignore[typeddict-item]
    if data.get("HsmArn") is not None:
        out["hsm_arn"] = data["HsmArn"]
    else:
        out["hsm_arn"] = ""
    return out
