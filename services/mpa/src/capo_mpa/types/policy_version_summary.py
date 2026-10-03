"""Generated from Smithy shape ``com.amazonaws.mpa#PolicyVersionSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_mpa.errors import DeserializationError

if TYPE_CHECKING:
    import capo_mpa.types.iso_timestamp
    import capo_mpa.types.policy_name
    import capo_mpa.types.policy_status
    import capo_mpa.types.policy_type
    import capo_mpa.types.policy_version_id
    import capo_mpa.types.qualified_policy_arn
    import capo_mpa.types.unqualified_policy_arn


class PolicyVersionSummary(TypedDict, closed=True):
    arn: "capo_mpa.types.qualified_policy_arn.QualifiedPolicyArn"
    """<p>Amazon Resource Name (ARN) for the team.</p>"""
    policy_arn: "capo_mpa.types.unqualified_policy_arn.UnqualifiedPolicyArn"
    """<p>Amazon Resource Name (ARN) for the policy.</p>"""
    version_id: "capo_mpa.types.policy_version_id.PolicyVersionId"
    """<p>Version ID for the policy.</p>"""
    policy_type: "capo_mpa.types.policy_type.PolicyType"
    """<p>The type of policy.</p>"""
    is_default: "bool"
    """<p>Determines if the specified policy is the default for the team.</p>"""
    name: "capo_mpa.types.policy_name.PolicyName"
    """<p>Name of the policy</p>"""
    status: "capo_mpa.types.policy_status.PolicyStatus"
    """<p>Status for the policy. For example, if the policy is <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/id_groups_manage_attach-policy.html">attachable</a> or <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-deprecated.html">deprecated</a>.</p>"""
    creation_time: "capo_mpa.types.iso_timestamp.IsoTimestamp"
    """<p>Timestamp when the policy was created.</p>"""
    last_updated_time: "capo_mpa.types.iso_timestamp.IsoTimestamp"
    """<p>Timestamp when the policy was last updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PolicyVersionSummary) -> dict:
    out: dict = {}
    out["Arn"] = value["arn"]
    out["PolicyArn"] = value["policy_arn"]
    out["VersionId"] = value["version_id"]
    import capo_mpa.types.policy_type

    out["PolicyType"] = capo_mpa.types.policy_type.serialize_json(value["policy_type"])
    out["IsDefault"] = value["is_default"]
    out["Name"] = value["name"]
    import capo_mpa.types.policy_status

    out["Status"] = capo_mpa.types.policy_status.serialize_json(value["status"])
    import capo_mpa.types.iso_timestamp

    out["CreationTime"] = capo_mpa.types.iso_timestamp.serialize_json(
        value["creation_time"]
    )
    import capo_mpa.types.iso_timestamp

    out["LastUpdatedTime"] = capo_mpa.types.iso_timestamp.serialize_json(
        value["last_updated_time"]
    )
    return out


def deserialize_json(data: dict) -> PolicyVersionSummary:
    out: PolicyVersionSummary = {}  # type: ignore[typeddict-item]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    else:
        raise DeserializationError("PolicyVersionSummary.arn required")
    if data.get("PolicyArn") is not None:
        out["policy_arn"] = data["PolicyArn"]
    else:
        raise DeserializationError("PolicyVersionSummary.policy_arn required")
    if data.get("VersionId") is not None:
        out["version_id"] = data["VersionId"]
    else:
        raise DeserializationError("PolicyVersionSummary.version_id required")
    if data.get("PolicyType") is not None:
        import capo_mpa.types.policy_type

        out["policy_type"] = capo_mpa.types.policy_type.deserialize_json(
            data["PolicyType"]
        )
    else:
        raise DeserializationError("PolicyVersionSummary.policy_type required")
    if data.get("IsDefault") is not None:
        out["is_default"] = data["IsDefault"]
    else:
        raise DeserializationError("PolicyVersionSummary.is_default required")
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("PolicyVersionSummary.name required")
    if data.get("Status") is not None:
        import capo_mpa.types.policy_status

        out["status"] = capo_mpa.types.policy_status.deserialize_json(data["Status"])
    else:
        raise DeserializationError("PolicyVersionSummary.status required")
    if data.get("CreationTime") is not None:
        import capo_mpa.types.iso_timestamp

        out["creation_time"] = capo_mpa.types.iso_timestamp.deserialize_json(
            data["CreationTime"]
        )
    else:
        raise DeserializationError("PolicyVersionSummary.creation_time required")
    if data.get("LastUpdatedTime") is not None:
        import capo_mpa.types.iso_timestamp

        out["last_updated_time"] = capo_mpa.types.iso_timestamp.deserialize_json(
            data["LastUpdatedTime"]
        )
    else:
        raise DeserializationError("PolicyVersionSummary.last_updated_time required")
    return out
