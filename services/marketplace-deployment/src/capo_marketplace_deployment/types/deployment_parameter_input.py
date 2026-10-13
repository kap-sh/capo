"""Generated from Smithy shape ``com.amazonaws.marketplacedeployment#DeploymentParameterInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_marketplace_deployment.errors import DeserializationError

if TYPE_CHECKING:
    import capo_marketplace_deployment.types.deployment_parameter_name
    import capo_marketplace_deployment.types.secret_string


class DeploymentParameterInput(TypedDict, closed=True):
    name: "capo_marketplace_deployment.types.deployment_parameter_name.DeploymentParameterName"
    """<p>The desired name of the deployment parameter. This is the identifier on which deployment parameters are keyed for a given buyer and product. If this name matches an existing deployment parameter, this request will update the existing resource.</p>"""
    secret_string: "capo_marketplace_deployment.types.secret_string.SecretString"
    """<p>The text to encrypt and store in the secret.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeploymentParameterInput) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["secretString"] = value["secret_string"]
    return out


def deserialize_json(data: dict) -> DeploymentParameterInput:
    out: DeploymentParameterInput = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("DeploymentParameterInput.name required")
    if data.get("secretString") is not None:
        out["secret_string"] = data["secretString"]
    else:
        raise DeserializationError("DeploymentParameterInput.secret_string required")
    return out


def redact_sensitive(value: DeploymentParameterInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "secret_string" in value:
        out["secret_string"] = "*** Sensitive Data Redacted ***"
    return out
