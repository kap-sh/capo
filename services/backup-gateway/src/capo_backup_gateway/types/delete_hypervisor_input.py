"""Generated from Smithy shape ``com.amazonaws.backupgateway#DeleteHypervisorInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_backup_gateway.types.server_arn


class DeleteHypervisorInput(TypedDict, closed=True):
    hypervisor_arn: "capo_backup_gateway.types.server_arn.ServerArn"
    """<p>The Amazon Resource Name (ARN) of the hypervisor to delete.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteHypervisorInput) -> dict:
    out: dict = {}
    out["HypervisorArn"] = value["hypervisor_arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteHypervisorInput:
    out: DeleteHypervisorInput = {}  # type: ignore[typeddict-item]
    if data.get("HypervisorArn") is not None:
        out["hypervisor_arn"] = data["HypervisorArn"]
    else:
        out["hypervisor_arn"] = ""
    return out
