"""Generated from Smithy shape ``com.amazonaws.cleanrooms#MembershipProtectedJobResultConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cleanrooms.types.membership_protected_job_output_configuration
    import capo_cleanrooms.types.role_arn


class MembershipProtectedJobResultConfiguration(TypedDict, closed=True):
    output_configuration: "capo_cleanrooms.types.membership_protected_job_output_configuration.MembershipProtectedJobOutputConfiguration"
    """<p> The output configuration for a protected job result.</p>"""
    role_arn: "capo_cleanrooms.types.role_arn.RoleArn"
    """<p>The unique ARN for an IAM role that is used by Clean Rooms to write protected job results to the result location, given by the member who can receive results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MembershipProtectedJobResultConfiguration) -> dict:
    out: dict = {}
    import capo_cleanrooms.types.membership_protected_job_output_configuration

    out["outputConfiguration"] = (
        capo_cleanrooms.types.membership_protected_job_output_configuration.serialize_json(
            value["output_configuration"]
        )
    )
    out["roleArn"] = value["role_arn"]
    return out


def deserialize_json(data: dict) -> MembershipProtectedJobResultConfiguration:
    out: MembershipProtectedJobResultConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("outputConfiguration") is not None:
        import capo_cleanrooms.types.membership_protected_job_output_configuration

        out["output_configuration"] = (
            capo_cleanrooms.types.membership_protected_job_output_configuration.deserialize_json(
                data["outputConfiguration"]
            )
        )
    else:
        out["output_configuration"] = {"$unknown": {"name": ""}}
    if data.get("roleArn") is not None:
        out["role_arn"] = data["roleArn"]
    else:
        out["role_arn"] = ""
    return out
