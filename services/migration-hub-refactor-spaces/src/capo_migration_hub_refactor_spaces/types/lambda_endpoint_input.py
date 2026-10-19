"""Generated from Smithy shape ``com.amazonaws.migrationhubrefactorspaces#LambdaEndpointInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_migration_hub_refactor_spaces.types.lambda_arn


class LambdaEndpointInput(TypedDict, closed=True):
    arn: "capo_migration_hub_refactor_spaces.types.lambda_arn.LambdaArn"
    """<p>The Amazon Resource Name (ARN) of the Lambda function or alias.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LambdaEndpointInput) -> dict:
    out: dict = {}
    out["Arn"] = value["arn"]
    return out


def deserialize_json(data: dict) -> LambdaEndpointInput:
    out: LambdaEndpointInput = {}  # type: ignore[typeddict-item]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    else:
        out["arn"] = ""
    return out
