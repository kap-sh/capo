"""Generated from Smithy shape ``com.amazonaws.lambda#CapacityProviderPermissionsConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_lambda.types.role_arn


class CapacityProviderPermissionsConfig(TypedDict, closed=True):
    capacity_provider_operator_role_arn: "capo_lambda.types.role_arn.RoleArn"
    """<p>The ARN of the IAM role that the capacity provider uses to manage compute instances and other Amazon Web Services resources.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CapacityProviderPermissionsConfig) -> dict:
    out: dict = {}
    out["CapacityProviderOperatorRoleArn"] = value[
        "capacity_provider_operator_role_arn"
    ]
    return out


def deserialize_json(data: dict) -> CapacityProviderPermissionsConfig:
    out: CapacityProviderPermissionsConfig = {}  # type: ignore[typeddict-item]
    if data.get("CapacityProviderOperatorRoleArn") is not None:
        out["capacity_provider_operator_role_arn"] = data[
            "CapacityProviderOperatorRoleArn"
        ]
    else:
        out["capacity_provider_operator_role_arn"] = ""
    return out
