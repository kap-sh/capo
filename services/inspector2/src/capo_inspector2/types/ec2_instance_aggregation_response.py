"""Generated from Smithy shape ``com.amazonaws.inspector2#Ec2InstanceAggregationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_inspector2.types.ami_id
    import capo_inspector2.types.non_empty_string
    import capo_inspector2.types.severity_counts
    import capo_inspector2.types.tag_map


class Ec2InstanceAggregationResponse(TypedDict, closed=True):
    instance_id: "capo_inspector2.types.non_empty_string.NonEmptyString"
    """<p>The Amazon EC2 instance ID.</p>"""
    ami: NotRequired["capo_inspector2.types.ami_id.AmiId"]
    """<p>The Amazon Machine Image (AMI) of the Amazon EC2 instance.</p>"""
    operating_system: NotRequired["str"]
    """<p>The operating system of the Amazon EC2 instance.</p>"""
    instance_tags: NotRequired["capo_inspector2.types.tag_map.TagMap"]
    """<p>The tags attached to the instance.</p>"""
    account_id: NotRequired["str"]
    """<p>The Amazon Web Services account for the Amazon EC2 instance.</p>"""
    severity_counts: NotRequired["capo_inspector2.types.severity_counts.SeverityCounts"]
    """<p>An object that contains the count of matched findings per severity.</p>"""
    network_findings: NotRequired["int"]
    """<p>The number of network findings for the Amazon EC2 instance.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Ec2InstanceAggregationResponse) -> dict:
    out: dict = {}
    out["instanceId"] = value["instance_id"]
    if "ami" in value:
        out["ami"] = value["ami"]
    if "operating_system" in value:
        out["operatingSystem"] = value["operating_system"]
    if "instance_tags" in value:
        import capo_inspector2.types.tag_map

        out["instanceTags"] = capo_inspector2.types.tag_map.serialize_json(
            value["instance_tags"]
        )
    if "account_id" in value:
        out["accountId"] = value["account_id"]
    if "severity_counts" in value:
        import capo_inspector2.types.severity_counts

        out["severityCounts"] = capo_inspector2.types.severity_counts.serialize_json(
            value["severity_counts"]
        )
    if "network_findings" in value:
        out["networkFindings"] = value["network_findings"]
    return out


def deserialize_json(data: dict) -> Ec2InstanceAggregationResponse:
    out: Ec2InstanceAggregationResponse = {}  # type: ignore[typeddict-item]
    if data.get("instanceId") is not None:
        out["instance_id"] = data["instanceId"]
    else:
        out["instance_id"] = ""
    if data.get("ami") is not None:
        out["ami"] = data["ami"]
    if data.get("operatingSystem") is not None:
        out["operating_system"] = data["operatingSystem"]
    if data.get("instanceTags") is not None:
        import capo_inspector2.types.tag_map

        out["instance_tags"] = capo_inspector2.types.tag_map.deserialize_json(
            data["instanceTags"]
        )
    if data.get("accountId") is not None:
        out["account_id"] = data["accountId"]
    if data.get("severityCounts") is not None:
        import capo_inspector2.types.severity_counts

        out["severity_counts"] = capo_inspector2.types.severity_counts.deserialize_json(
            data["severityCounts"]
        )
    if data.get("networkFindings") is not None:
        out["network_findings"] = data["networkFindings"]
    return out
