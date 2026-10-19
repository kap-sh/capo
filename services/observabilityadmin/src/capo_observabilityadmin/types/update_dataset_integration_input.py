"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#UpdateDatasetIntegrationInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_observabilityadmin.types.resource_arn


class UpdateDatasetIntegrationInput(TypedDict, closed=True):
    arn: "capo_observabilityadmin.types.resource_arn.ResourceArn"
    """<p>The Amazon Resource Name (ARN) of the dataset integration to update.</p>"""
    role_arn: "capo_observabilityadmin.types.resource_arn.ResourceArn"
    """<p>The Amazon Resource Name (ARN) of the IAM role to associate with the dataset integration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateDatasetIntegrationInput) -> dict:
    out: dict = {}
    out["Arn"] = value["arn"]
    out["RoleArn"] = value["role_arn"]
    return out


def deserialize_json(data: dict) -> UpdateDatasetIntegrationInput:
    out: UpdateDatasetIntegrationInput = {}  # type: ignore[typeddict-item]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    else:
        out["arn"] = ""
    if data.get("RoleArn") is not None:
        out["role_arn"] = data["RoleArn"]
    else:
        out["role_arn"] = ""
    return out
