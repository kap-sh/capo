"""Generated from Smithy shape ``com.amazonaws.connect#ReplicationFinding``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.arn
    import capo_connect.types.aws_region
    import capo_connect.types.replication_finding_message
    import capo_connect.types.replication_finding_operation
    import capo_connect.types.replication_finding_reference_code
    import capo_connect.types.replication_finding_resource_name
    import capo_connect.types.replication_finding_resource_type
    import capo_connect.types.resource_id


class ReplicationFinding(TypedDict, closed=True):
    arn: "capo_connect.types.arn.ARN"
    """<p>The Amazon Resource Name (ARN) of the resource that the finding is for.</p>"""
    id: "capo_connect.types.resource_id.ResourceId"
    """<p>The identifier of the resource that the finding is for.</p>"""
    region: NotRequired["capo_connect.types.aws_region.AwsRegion"]
    """<p>The Amazon Web Services Region that the finding was detected in.</p>"""
    resource_type: "capo_connect.types.replication_finding_resource_type.ReplicationFindingResourceType"
    """<p>The type of resource that the finding is for, such as <code>QUEUE</code> or <code>ROUTING_PROFILE</code>.</p>"""
    name: NotRequired[
        "capo_connect.types.replication_finding_resource_name.ReplicationFindingResourceName"
    ]
    """<p>The name of the resource that the finding is for.</p>"""
    operation: NotRequired[
        "capo_connect.types.replication_finding_operation.ReplicationFindingOperation"
    ]
    """<p>The replication operation that produced the finding, such as a create, update, or delete of the resource.</p>"""
    reference_code: NotRequired[
        "capo_connect.types.replication_finding_reference_code.ReplicationFindingReferenceCode"
    ]
    """<p>A stable code that identifies the class of the finding. Use this code to look up the recommended steps to resolve the finding.</p>"""
    message: NotRequired[
        "capo_connect.types.replication_finding_message.ReplicationFindingMessage"
    ]
    """<p>A human-readable description of the finding and the action, if any, required to resolve it.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ReplicationFinding) -> dict:
    out: dict = {}
    out["Arn"] = value["arn"]
    out["Id"] = value["id"]
    if "region" in value:
        out["Region"] = value["region"]
    out["ResourceType"] = value["resource_type"]
    if "name" in value:
        out["Name"] = value["name"]
    if "operation" in value:
        out["Operation"] = value["operation"]
    if "reference_code" in value:
        out["ReferenceCode"] = value["reference_code"]
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> ReplicationFinding:
    out: ReplicationFinding = {}  # type: ignore[typeddict-item]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    else:
        out["arn"] = ""
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    else:
        out["id"] = ""
    if data.get("Region") is not None:
        out["region"] = data["Region"]
    if data.get("ResourceType") is not None:
        out["resource_type"] = data["ResourceType"]
    else:
        out["resource_type"] = ""
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Operation") is not None:
        out["operation"] = data["Operation"]
    if data.get("ReferenceCode") is not None:
        out["reference_code"] = data["ReferenceCode"]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    return out
