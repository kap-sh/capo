"""Generated from Smithy shape ``com.amazonaws.mpa#Policy``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_mpa.types.policy_name
    import capo_mpa.types.policy_type
    import capo_mpa.types.policy_version_id
    import capo_mpa.types.unqualified_policy_arn


class Policy(TypedDict, closed=True):
    arn: "capo_mpa.types.unqualified_policy_arn.UnqualifiedPolicyArn"
    """<p>Amazon Resource Name (ARN) for the policy.</p>"""
    default_version: "capo_mpa.types.policy_version_id.PolicyVersionId"
    """<p>Determines if the specified policy is the default for the team.</p>"""
    policy_type: "capo_mpa.types.policy_type.PolicyType"
    """<p>The type of policy.</p>"""
    name: "capo_mpa.types.policy_name.PolicyName"
    """<p>Name of the policy.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Policy) -> dict:
    out: dict = {}
    out["Arn"] = value["arn"]
    out["DefaultVersion"] = value["default_version"]
    import capo_mpa.types.policy_type

    out["PolicyType"] = capo_mpa.types.policy_type.serialize_json(value["policy_type"])
    out["Name"] = value["name"]
    return out


def deserialize_json(data: dict) -> Policy:
    out: Policy = {}  # type: ignore[typeddict-item]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    else:
        out["arn"] = ""
    if data.get("DefaultVersion") is not None:
        out["default_version"] = data["DefaultVersion"]
    else:
        out["default_version"] = 0
    if data.get("PolicyType") is not None:
        import capo_mpa.types.policy_type

        out["policy_type"] = capo_mpa.types.policy_type.deserialize_json(
            data["PolicyType"]
        )
    else:
        import typing

        out["policy_type"] = typing.cast("capo_mpa.types.policy_type.PolicyType", "")
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    return out
