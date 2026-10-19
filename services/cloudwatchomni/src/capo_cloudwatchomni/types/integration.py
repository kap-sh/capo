"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#Integration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_cloudwatchomni.types.auth_type
    import capo_cloudwatchomni.types.integration_arn
    import capo_cloudwatchomni.types.integration_status
    import capo_cloudwatchomni.types.integration_type
    import capo_cloudwatchomni.types.scope
    import capo_cloudwatchomni.types.string_map


class Integration(TypedDict, closed=True):
    integration_id: "str"
    """The unique identifier of the integration."""
    integration_arn: NotRequired[
        "capo_cloudwatchomni.types.integration_arn.IntegrationArn"
    ]
    """The Amazon Resource Name (ARN) of the integration."""
    integration_type: "capo_cloudwatchomni.types.integration_type.IntegrationType"
    name: "str"
    """The customer-provided name of the integration."""
    status: "capo_cloudwatchomni.types.integration_status.IntegrationStatus"
    auth_type: NotRequired["capo_cloudwatchomni.types.auth_type.AuthType"]
    credential_arn: NotRequired["str"]
    """The Amazon Resource Name (ARN) of the secret that stores the integration's credentials."""
    role_arn: NotRequired["str"]
    """The Amazon Resource Name (ARN) of the IAM role that CloudWatch assumes to access the external system."""
    integration_attributes: NotRequired[
        "capo_cloudwatchomni.types.string_map.StringMap"
    ]
    """Provider-specific key/value attributes that configure the integration."""
    authorization_url: NotRequired["str"]
    """The URL the customer visits to authorize the integration. Present while an OAuth authorization is pending."""
    error_message: NotRequired["str"]
    """A human-readable description of why the integration is in an ERROR or FAILED state. Present only when the integration has failed."""
    created_at: NotRequired["datetime.datetime"]
    """The time at which the integration was created."""
    updated_at: NotRequired["datetime.datetime"]
    """The time at which the integration was last updated."""
    scope: NotRequired["capo_cloudwatchomni.types.scope.Scope"]
    """Whether this integration is account-scoped (ACCOUNT, customer-created) or organization-scoped (ORGANIZATION, created by an org-enablement rule). Absent on legacy records is treated as ACCOUNT."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: Integration) -> dict:
    out: dict = {}
    out["integrationId"] = value["integration_id"]
    if "integration_arn" in value:
        out["integrationArn"] = value["integration_arn"]
    import capo_cloudwatchomni.types.integration_type

    out["integrationType"] = capo_cloudwatchomni.types.integration_type.serialize_cbor(
        value["integration_type"]
    )
    out["name"] = value["name"]
    import capo_cloudwatchomni.types.integration_status

    out["status"] = capo_cloudwatchomni.types.integration_status.serialize_cbor(
        value["status"]
    )
    if "auth_type" in value:
        import capo_cloudwatchomni.types.auth_type

        out["authType"] = capo_cloudwatchomni.types.auth_type.serialize_cbor(
            value["auth_type"]
        )
    if "credential_arn" in value:
        out["credentialArn"] = value["credential_arn"]
    if "role_arn" in value:
        out["roleArn"] = value["role_arn"]
    if "integration_attributes" in value:
        import capo_cloudwatchomni.types.string_map

        out["integrationAttributes"] = (
            capo_cloudwatchomni.types.string_map.serialize_cbor(
                value["integration_attributes"]
            )
        )
    if "authorization_url" in value:
        out["authorizationUrl"] = value["authorization_url"]
    if "error_message" in value:
        out["errorMessage"] = value["error_message"]
    if "created_at" in value:
        import capo_cloudwatchomni.types._prelude.timestamp

        out["createdAt"] = capo_cloudwatchomni.types._prelude.timestamp.serialize_cbor(
            value["created_at"]
        )
    if "updated_at" in value:
        import capo_cloudwatchomni.types._prelude.timestamp

        out["updatedAt"] = capo_cloudwatchomni.types._prelude.timestamp.serialize_cbor(
            value["updated_at"]
        )
    if "scope" in value:
        import capo_cloudwatchomni.types.scope

        out["scope"] = capo_cloudwatchomni.types.scope.serialize_cbor(value["scope"])
    return out


def deserialize_cbor(data: dict) -> Integration:
    out: Integration = {}  # type: ignore[typeddict-item]
    if data.get("integrationId") is not None:
        out["integration_id"] = data["integrationId"]
    else:
        out["integration_id"] = ""
    if data.get("integrationArn") is not None:
        out["integration_arn"] = data["integrationArn"]
    if data.get("integrationType") is not None:
        import capo_cloudwatchomni.types.integration_type

        out["integration_type"] = (
            capo_cloudwatchomni.types.integration_type.deserialize_cbor(
                data["integrationType"]
            )
        )
    else:
        import typing

        out["integration_type"] = typing.cast(
            "capo_cloudwatchomni.types.integration_type.IntegrationType", ""
        )
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("status") is not None:
        import capo_cloudwatchomni.types.integration_status

        out["status"] = capo_cloudwatchomni.types.integration_status.deserialize_cbor(
            data["status"]
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_cloudwatchomni.types.integration_status.IntegrationStatus", ""
        )
    if data.get("authType") is not None:
        import capo_cloudwatchomni.types.auth_type

        out["auth_type"] = capo_cloudwatchomni.types.auth_type.deserialize_cbor(
            data["authType"]
        )
    if data.get("credentialArn") is not None:
        out["credential_arn"] = data["credentialArn"]
    if data.get("roleArn") is not None:
        out["role_arn"] = data["roleArn"]
    if data.get("integrationAttributes") is not None:
        import capo_cloudwatchomni.types.string_map

        out["integration_attributes"] = (
            capo_cloudwatchomni.types.string_map.deserialize_cbor(
                data["integrationAttributes"]
            )
        )
    if data.get("authorizationUrl") is not None:
        out["authorization_url"] = data["authorizationUrl"]
    if data.get("errorMessage") is not None:
        out["error_message"] = data["errorMessage"]
    if data.get("createdAt") is not None:
        import capo_cloudwatchomni.types._prelude.timestamp

        out["created_at"] = (
            capo_cloudwatchomni.types._prelude.timestamp.deserialize_cbor(
                data["createdAt"]
            )
        )
    if data.get("updatedAt") is not None:
        import capo_cloudwatchomni.types._prelude.timestamp

        out["updated_at"] = (
            capo_cloudwatchomni.types._prelude.timestamp.deserialize_cbor(
                data["updatedAt"]
            )
        )
    if data.get("scope") is not None:
        import capo_cloudwatchomni.types.scope

        out["scope"] = capo_cloudwatchomni.types.scope.deserialize_cbor(data["scope"])
    return out
