"""Generated from Smithy shape ``com.amazonaws.mpa#PolicyVersion``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_mpa.types.iso_timestamp
    import capo_mpa.types.policy_document
    import capo_mpa.types.policy_name
    import capo_mpa.types.policy_status
    import capo_mpa.types.policy_type
    import capo_mpa.types.policy_version_id
    import capo_mpa.types.qualified_policy_arn
    import capo_mpa.types.unqualified_policy_arn


class PolicyVersion(TypedDict, closed=True):
    arn: "capo_mpa.types.qualified_policy_arn.QualifiedPolicyArn"
    """<p>Amazon Resource Name (ARN) for the team.</p>"""
    policy_arn: "capo_mpa.types.unqualified_policy_arn.UnqualifiedPolicyArn"
    """<p>Amazon Resource Name (ARN) for the policy.</p>"""
    version_id: "capo_mpa.types.policy_version_id.PolicyVersionId"
    """<p>Verison ID</p>"""
    policy_type: "capo_mpa.types.policy_type.PolicyType"
    """<p>The type of policy.</p>"""
    is_default: "bool"
    """<p>Determines if the specified policy is the default for the team.</p>"""
    name: "capo_mpa.types.policy_name.PolicyName"
    """<p>Name of the policy.</p>"""
    status: "capo_mpa.types.policy_status.PolicyStatus"
    """<p>Status for the policy. For example, if the policy is <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/id_groups_manage_attach-policy.html">attachable</a> or <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-deprecated.html">deprecated</a>.</p>"""
    creation_time: "capo_mpa.types.iso_timestamp.IsoTimestamp"
    """<p>Timestamp when the policy was created.</p>"""
    last_updated_time: "capo_mpa.types.iso_timestamp.IsoTimestamp"
    """<p>Timestamp when the policy was last updated.</p>"""
    document: "capo_mpa.types.policy_document.PolicyDocument"
    """<p>Document that contains the policy contents.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PolicyVersion) -> dict:
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
    out["Document"] = value["document"]
    return out


def deserialize_json(data: dict) -> PolicyVersion:
    out: PolicyVersion = {}  # type: ignore[typeddict-item]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    else:
        out["arn"] = ""
    if data.get("PolicyArn") is not None:
        out["policy_arn"] = data["PolicyArn"]
    else:
        out["policy_arn"] = ""
    if data.get("VersionId") is not None:
        out["version_id"] = data["VersionId"]
    else:
        out["version_id"] = 0
    if data.get("PolicyType") is not None:
        import capo_mpa.types.policy_type

        out["policy_type"] = capo_mpa.types.policy_type.deserialize_json(
            data["PolicyType"]
        )
    else:
        import typing

        out["policy_type"] = typing.cast("capo_mpa.types.policy_type.PolicyType", "")
    if data.get("IsDefault") is not None:
        out["is_default"] = data["IsDefault"]
    else:
        out["is_default"] = False
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("Status") is not None:
        import capo_mpa.types.policy_status

        out["status"] = capo_mpa.types.policy_status.deserialize_json(data["Status"])
    else:
        import typing

        out["status"] = typing.cast("capo_mpa.types.policy_status.PolicyStatus", "")
    if data.get("CreationTime") is not None:
        import capo_mpa.types.iso_timestamp

        out["creation_time"] = capo_mpa.types.iso_timestamp.deserialize_json(
            data["CreationTime"]
        )
    else:
        import datetime

        out["creation_time"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    if data.get("LastUpdatedTime") is not None:
        import capo_mpa.types.iso_timestamp

        out["last_updated_time"] = capo_mpa.types.iso_timestamp.deserialize_json(
            data["LastUpdatedTime"]
        )
    else:
        import datetime

        out["last_updated_time"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    if data.get("Document") is not None:
        out["document"] = data["Document"]
    else:
        out["document"] = ""
    return out


def redact_sensitive(value: PolicyVersion) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "document" in value:
        out["document"] = "*** Sensitive Data Redacted ***"
    return out
