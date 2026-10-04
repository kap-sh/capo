"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#AcrLevelConfigType``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_cognito_identity_provider.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.acr_value_type


class AcrLevelConfigType(TypedDict, closed=True):
    acr_value: "capo_cognito_identity_provider.types.acr_value_type.AcrValueType"
    """<p>The custom name for this authentication context class reference (ACR) level. This value is the URI that Amazon Cognito reports in the <code>acr</code> token claim when a user meets this level. The name must be unique across all levels in the user pool, including default names.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AcrLevelConfigType) -> dict:
    out: dict = {}
    out["AcrValue"] = value["acr_value"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AcrLevelConfigType:
    out: AcrLevelConfigType = {}  # type: ignore[typeddict-item]
    if data.get("AcrValue") is not None:
        out["acr_value"] = data["AcrValue"]
    else:
        raise DeserializationError("AcrLevelConfigType.acr_value required")
    return out
