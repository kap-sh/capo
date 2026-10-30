"""Generated from Smithy shape ``com.amazonaws.continuum#EnvironmentS3IntegrationSource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_continuum.types.environment_source_prefix
    import capo_continuum.types.integration_id


class EnvironmentS3IntegrationSource(TypedDict, closed=True):
    integration_id: "capo_continuum.types.integration_id.IntegrationId"
    """Identifier of an S3 integration in the caller's account. The integration supplies the bucket, the read role, and the external ID Continuum uses to read the prefixes."""
    code_prefix: NotRequired[
        "capo_continuum.types.environment_source_prefix.EnvironmentSourcePrefix"
    ]
    """Prefix containing source code. Defaults to code/ when omitted."""
    context_prefix: NotRequired[
        "capo_continuum.types.environment_source_prefix.EnvironmentSourcePrefix"
    ]
    """Prefix containing customer-authored context. Defaults to context/ when omitted."""


# --- restJson1 ser/de ---
def serialize_json(value: EnvironmentS3IntegrationSource) -> dict:
    out: dict = {}
    out["integrationId"] = value["integration_id"]
    if "code_prefix" in value:
        out["codePrefix"] = value["code_prefix"]
    if "context_prefix" in value:
        out["contextPrefix"] = value["context_prefix"]
    return out


def deserialize_json(data: dict) -> EnvironmentS3IntegrationSource:
    out: EnvironmentS3IntegrationSource = {}  # type: ignore[typeddict-item]
    if data.get("integrationId") is not None:
        out["integration_id"] = data["integrationId"]
    else:
        out["integration_id"] = ""
    if data.get("codePrefix") is not None:
        out["code_prefix"] = data["codePrefix"]
    if data.get("contextPrefix") is not None:
        out["context_prefix"] = data["contextPrefix"]
    return out
