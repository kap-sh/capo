"""Generated from Smithy shape ``com.amazonaws.inspector#DescribeCrossAccountAccessRoleResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_inspector.types.arn
    import capo_inspector.types.bool
    import capo_inspector.types.timestamp


class DescribeCrossAccountAccessRoleResponse(TypedDict, closed=True):
    role_arn: "capo_inspector.types.arn.Arn"
    """<p>The ARN that specifies the IAM role that Amazon Inspector uses to access your AWS account.</p>"""
    valid: "capo_inspector.types.bool.Bool"
    """<p>A Boolean value that specifies whether the IAM role has the necessary policies attached to enable Amazon Inspector to access your AWS account.</p>"""
    registered_at: "capo_inspector.types.timestamp.Timestamp"
    """<p>The date when the cross-account access role was registered.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeCrossAccountAccessRoleResponse) -> dict:
    out: dict = {}
    out["roleArn"] = value["role_arn"]
    out["valid"] = value["valid"]
    import capo_inspector.types.timestamp

    out["registeredAt"] = capo_inspector.types.timestamp.serialize_aws_json_1_1(
        value["registered_at"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeCrossAccountAccessRoleResponse:
    out: DescribeCrossAccountAccessRoleResponse = {}  # type: ignore[typeddict-item]
    if data.get("roleArn") is not None:
        out["role_arn"] = data["roleArn"]
    else:
        out["role_arn"] = ""
    if data.get("valid") is not None:
        out["valid"] = data["valid"]
    else:
        out["valid"] = False
    if data.get("registeredAt") is not None:
        import capo_inspector.types.timestamp

        out["registered_at"] = capo_inspector.types.timestamp.deserialize_aws_json_1_1(
            data["registeredAt"]
        )
    else:
        import datetime

        out["registered_at"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    return out
