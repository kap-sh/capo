"""Generated from Smithy shape ``com.amazonaws.lambda#CodeSigningConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_lambda.errors import DeserializationError

if TYPE_CHECKING:
    import capo_lambda.types.allowed_publishers
    import capo_lambda.types.code_signing_config_arn
    import capo_lambda.types.code_signing_config_id
    import capo_lambda.types.code_signing_policies
    import capo_lambda.types.description
    import capo_lambda.types.timestamp


class CodeSigningConfig(TypedDict, closed=True):
    code_signing_config_id: (
        "capo_lambda.types.code_signing_config_id.CodeSigningConfigId"
    )
    """<p>Unique identifer for the Code signing configuration.</p>"""
    code_signing_config_arn: (
        "capo_lambda.types.code_signing_config_arn.CodeSigningConfigArn"
    )
    """<p>The Amazon Resource Name (ARN) of the Code signing configuration.</p>"""
    description: NotRequired["capo_lambda.types.description.Description"]
    """<p>Code signing configuration description.</p>"""
    allowed_publishers: "capo_lambda.types.allowed_publishers.AllowedPublishers"
    """<p>List of allowed publishers.</p>"""
    code_signing_policies: "capo_lambda.types.code_signing_policies.CodeSigningPolicies"
    """<p>The code signing policy controls the validation failure action for signature mismatch or expiry.</p>"""
    last_modified: "capo_lambda.types.timestamp.Timestamp"
    """<p>The date and time that the Code signing configuration was last modified, in ISO-8601 format (YYYY-MM-DDThh:mm:ss.sTZD). </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CodeSigningConfig) -> dict:
    out: dict = {}
    out["CodeSigningConfigId"] = value["code_signing_config_id"]
    out["CodeSigningConfigArn"] = value["code_signing_config_arn"]
    if "description" in value:
        out["Description"] = value["description"]
    import capo_lambda.types.allowed_publishers

    out["AllowedPublishers"] = capo_lambda.types.allowed_publishers.serialize_json(
        value["allowed_publishers"]
    )
    import capo_lambda.types.code_signing_policies

    out["CodeSigningPolicies"] = capo_lambda.types.code_signing_policies.serialize_json(
        value["code_signing_policies"]
    )
    out["LastModified"] = value["last_modified"]
    return out


def deserialize_json(data: dict) -> CodeSigningConfig:
    out: CodeSigningConfig = {}  # type: ignore[typeddict-item]
    if data.get("CodeSigningConfigId") is not None:
        out["code_signing_config_id"] = data["CodeSigningConfigId"]
    else:
        out["code_signing_config_id"] = ""
    if data.get("CodeSigningConfigArn") is not None:
        out["code_signing_config_arn"] = data["CodeSigningConfigArn"]
    else:
        out["code_signing_config_arn"] = ""
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("AllowedPublishers") is not None:
        import capo_lambda.types.allowed_publishers

        out["allowed_publishers"] = (
            capo_lambda.types.allowed_publishers.deserialize_json(
                data["AllowedPublishers"]
            )
        )
    else:
        raise DeserializationError("CodeSigningConfig.allowed_publishers required")
    if data.get("CodeSigningPolicies") is not None:
        import capo_lambda.types.code_signing_policies

        out["code_signing_policies"] = (
            capo_lambda.types.code_signing_policies.deserialize_json(
                data["CodeSigningPolicies"]
            )
        )
    else:
        raise DeserializationError("CodeSigningConfig.code_signing_policies required")
    if data.get("LastModified") is not None:
        out["last_modified"] = data["LastModified"]
    else:
        out["last_modified"] = ""
    return out
