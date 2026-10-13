"""Generated from Smithy shape ``com.amazonaws.datazone#CreateAssetFilterInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_datazone.errors import DeserializationError

if TYPE_CHECKING:
    import capo_datazone.types.asset_filter_configuration
    import capo_datazone.types.asset_id
    import capo_datazone.types.description
    import capo_datazone.types.domain_id
    import capo_datazone.types.filter_name


class CreateAssetFilterInput(TypedDict, closed=True):
    domain_identifier: "capo_datazone.types.domain_id.DomainId"
    """<p>The ID of the domain in which you want to create an asset filter.</p>"""
    asset_identifier: "capo_datazone.types.asset_id.AssetId"
    """<p>The ID of the data asset.</p>"""
    name: "capo_datazone.types.filter_name.FilterName"
    """<p>The name of the asset filter.</p>"""
    description: NotRequired["capo_datazone.types.description.Description"]
    """<p>The description of the asset filter.</p>"""
    configuration: (
        "capo_datazone.types.asset_filter_configuration.AssetFilterConfiguration"
    )
    """<p>The configuration of the asset filter.</p>"""
    client_token: NotRequired["str"]
    """<p>A unique, case-sensitive identifier that is provided to ensure the idempotency of the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateAssetFilterInput) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    import capo_datazone.types.asset_filter_configuration

    out["configuration"] = (
        capo_datazone.types.asset_filter_configuration.serialize_json(
            value["configuration"]
        )
    )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> CreateAssetFilterInput:
    out: CreateAssetFilterInput = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateAssetFilterInput.name required")
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("configuration") is not None:
        import capo_datazone.types.asset_filter_configuration

        out["configuration"] = (
            capo_datazone.types.asset_filter_configuration.deserialize_json(
                data["configuration"]
            )
        )
    else:
        raise DeserializationError("CreateAssetFilterInput.configuration required")
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    return out


def redact_sensitive(value: CreateAssetFilterInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "name" in value:
        out["name"] = "*** Sensitive Data Redacted ***"
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    return out
