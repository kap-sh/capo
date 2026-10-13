"""Generated from Smithy shape ``com.amazonaws.secretsmanager#BatchGetSecretValueResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_secrets_manager.types.api_error_list_type
    import capo_secrets_manager.types.next_token_type
    import capo_secrets_manager.types.secret_values_type


class BatchGetSecretValueResponse(TypedDict, closed=True):
    secret_values: NotRequired[
        "capo_secrets_manager.types.secret_values_type.SecretValuesType"
    ]
    """<p>A list of secret values.</p>"""
    next_token: NotRequired["capo_secrets_manager.types.next_token_type.NextTokenType"]
    """<p>Secrets Manager includes this value if there's more output available than what is included in the current response. This can occur even when the response includes no values at all, such as when you ask for a filtered view of a long list. To get the next results, call <code>BatchGetSecretValue</code> again with this value.</p>"""
    errors: NotRequired[
        "capo_secrets_manager.types.api_error_list_type.APIErrorListType"
    ]
    """<p>A list of errors Secrets Manager encountered while attempting to retrieve individual secrets.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchGetSecretValueResponse) -> dict:
    out: dict = {}
    if "secret_values" in value:
        import capo_secrets_manager.types.secret_values_type

        out["SecretValues"] = (
            capo_secrets_manager.types.secret_values_type.serialize_aws_json_1_1(
                value["secret_values"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "errors" in value:
        import capo_secrets_manager.types.api_error_list_type

        out["Errors"] = (
            capo_secrets_manager.types.api_error_list_type.serialize_aws_json_1_1(
                value["errors"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchGetSecretValueResponse:
    out: BatchGetSecretValueResponse = {}  # type: ignore[typeddict-item]
    if data.get("SecretValues") is not None:
        import capo_secrets_manager.types.secret_values_type

        out["secret_values"] = (
            capo_secrets_manager.types.secret_values_type.deserialize_aws_json_1_1(
                data["SecretValues"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("Errors") is not None:
        import capo_secrets_manager.types.api_error_list_type

        out["errors"] = (
            capo_secrets_manager.types.api_error_list_type.deserialize_aws_json_1_1(
                data["Errors"]
            )
        )
    return out


def redact_sensitive(value: BatchGetSecretValueResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "secret_values" in value:
        import capo_secrets_manager.types.secret_values_type

        out["secret_values"] = (
            capo_secrets_manager.types.secret_values_type.redact_sensitive(
                value["secret_values"]
            )
        )
    return out
