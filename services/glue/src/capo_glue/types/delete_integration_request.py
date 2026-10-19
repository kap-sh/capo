"""Generated from Smithy shape ``com.amazonaws.glue#DeleteIntegrationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_glue.types.string128


class DeleteIntegrationRequest(TypedDict, closed=True):
    integration_identifier: "capo_glue.types.string128.String128"
    """<p>The Amazon Resource Name (ARN) for the integration.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteIntegrationRequest) -> dict:
    out: dict = {}
    out["IntegrationIdentifier"] = value["integration_identifier"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteIntegrationRequest:
    out: DeleteIntegrationRequest = {}  # type: ignore[typeddict-item]
    if data.get("IntegrationIdentifier") is not None:
        out["integration_identifier"] = data["IntegrationIdentifier"]
    else:
        out["integration_identifier"] = ""
    return out
