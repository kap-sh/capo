"""Generated from Smithy shape ``com.amazonaws.cloudhsm#ModifyLunaClientRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cloudhsm.types.certificate
    import capo_cloudhsm.types.client_arn


class ModifyLunaClientRequest(TypedDict, closed=True):
    client_arn: "capo_cloudhsm.types.client_arn.ClientArn"
    """<p>The ARN of the client.</p>"""
    certificate: "capo_cloudhsm.types.certificate.Certificate"
    """<p>The new certificate for the client.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ModifyLunaClientRequest) -> dict:
    out: dict = {}
    out["ClientArn"] = value["client_arn"]
    out["Certificate"] = value["certificate"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ModifyLunaClientRequest:
    out: ModifyLunaClientRequest = {}  # type: ignore[typeddict-item]
    if data.get("ClientArn") is not None:
        out["client_arn"] = data["ClientArn"]
    else:
        out["client_arn"] = ""
    if data.get("Certificate") is not None:
        out["certificate"] = data["Certificate"]
    else:
        out["certificate"] = ""
    return out
