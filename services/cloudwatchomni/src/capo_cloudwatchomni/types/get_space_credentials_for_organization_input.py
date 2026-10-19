"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#GetSpaceCredentialsForOrganizationInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_cloudwatchomni.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cloudwatchomni.types.organization_credential_type
    import capo_cloudwatchomni.types.space_credential_request_context


class GetSpaceCredentialsForOrganizationInput(TypedDict, closed=True):
    context: "capo_cloudwatchomni.types.space_credential_request_context.SpaceCredentialRequestContext"
    """Context for credential resolution."""
    credential_type: "capo_cloudwatchomni.types.organization_credential_type.OrganizationCredentialType"
    """Selects which member-account credential to return. Set this to SPACE_OPERATION."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: GetSpaceCredentialsForOrganizationInput) -> dict:
    out: dict = {}
    import capo_cloudwatchomni.types.space_credential_request_context

    out["context"] = (
        capo_cloudwatchomni.types.space_credential_request_context.serialize_cbor(
            value["context"]
        )
    )
    import capo_cloudwatchomni.types.organization_credential_type

    out["credentialType"] = (
        capo_cloudwatchomni.types.organization_credential_type.serialize_cbor(
            value["credential_type"]
        )
    )
    return out


def deserialize_cbor(data: dict) -> GetSpaceCredentialsForOrganizationInput:
    out: GetSpaceCredentialsForOrganizationInput = {}  # type: ignore[typeddict-item]
    if data.get("context") is not None:
        import capo_cloudwatchomni.types.space_credential_request_context

        out["context"] = (
            capo_cloudwatchomni.types.space_credential_request_context.deserialize_cbor(
                data["context"]
            )
        )
    else:
        raise DeserializationError(
            "GetSpaceCredentialsForOrganizationInput.context required"
        )
    if data.get("credentialType") is not None:
        import capo_cloudwatchomni.types.organization_credential_type

        out["credential_type"] = (
            capo_cloudwatchomni.types.organization_credential_type.deserialize_cbor(
                data["credentialType"]
            )
        )
    else:
        import typing

        out["credential_type"] = typing.cast(
            "capo_cloudwatchomni.types.organization_credential_type.OrganizationCredentialType",
            "",
        )
    return out
