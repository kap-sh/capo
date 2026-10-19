"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#UpdateProvisionedLimitRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_cognito_identity_provider.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.integer_type
    import capo_cognito_identity_provider.types.limit_definition_type


class UpdateProvisionedLimitRequest(TypedDict, closed=True):
    limit_definition: (
        "capo_cognito_identity_provider.types.limit_definition_type.LimitDefinitionType"
    )
    """<p>The limit to update. Specify the limit class and the attributes that identify the limit.</p>"""
    requested_limit_value: (
        "capo_cognito_identity_provider.types.integer_type.IntegerType"
    )
    """<p>The provisioned rate to set, in requests per second (RPS).</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateProvisionedLimitRequest) -> dict:
    out: dict = {}
    import capo_cognito_identity_provider.types.limit_definition_type

    out["LimitDefinition"] = (
        capo_cognito_identity_provider.types.limit_definition_type.serialize_aws_json_1_1(
            value["limit_definition"]
        )
    )
    out["RequestedLimitValue"] = value["requested_limit_value"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateProvisionedLimitRequest:
    out: UpdateProvisionedLimitRequest = {}  # type: ignore[typeddict-item]
    if data.get("LimitDefinition") is not None:
        import capo_cognito_identity_provider.types.limit_definition_type

        out["limit_definition"] = (
            capo_cognito_identity_provider.types.limit_definition_type.deserialize_aws_json_1_1(
                data["LimitDefinition"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateProvisionedLimitRequest.limit_definition required"
        )
    if data.get("RequestedLimitValue") is not None:
        out["requested_limit_value"] = data["RequestedLimitValue"]
    else:
        raise DeserializationError(
            "UpdateProvisionedLimitRequest.requested_limit_value required"
        )
    return out
