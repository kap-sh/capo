"""Generated from Smithy shape ``com.amazonaws.ssm#UpdateAssociationStatusRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_ssm.errors import DeserializationError

if TYPE_CHECKING:
    import capo_ssm.types.association_status
    import capo_ssm.types.document_arn
    import capo_ssm.types.instance_id


class UpdateAssociationStatusRequest(TypedDict, closed=True):
    name: "capo_ssm.types.document_arn.DocumentARN"
    """<p>The name of the SSM document.</p>"""
    instance_id: "capo_ssm.types.instance_id.InstanceId"
    """<p>The managed node ID.</p>"""
    association_status: "capo_ssm.types.association_status.AssociationStatus"
    """<p>The association status.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateAssociationStatusRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    out["InstanceId"] = value["instance_id"]
    import capo_ssm.types.association_status

    out["AssociationStatus"] = capo_ssm.types.association_status.serialize_aws_json_1_1(
        value["association_status"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateAssociationStatusRequest:
    out: UpdateAssociationStatusRequest = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("InstanceId") is not None:
        out["instance_id"] = data["InstanceId"]
    else:
        out["instance_id"] = ""
    if data.get("AssociationStatus") is not None:
        import capo_ssm.types.association_status

        out["association_status"] = (
            capo_ssm.types.association_status.deserialize_aws_json_1_1(
                data["AssociationStatus"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateAssociationStatusRequest.association_status required"
        )
    return out
