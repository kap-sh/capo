"""Generated from Smithy shape ``com.amazonaws.dataexchange#CreateJobRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_dataexchange.errors import DeserializationError

if TYPE_CHECKING:
    import capo_dataexchange.types.asset_configuration
    import capo_dataexchange.types.request_details
    import capo_dataexchange.types.type


class CreateJobRequest(TypedDict, closed=True):
    asset_configuration: NotRequired[
        "capo_dataexchange.types.asset_configuration.AssetConfiguration"
    ]
    """<p>The configuration for the asset, including tags to be applied to assets created by the job.</p>"""
    details: "capo_dataexchange.types.request_details.RequestDetails"
    """<p>The details for the CreateJob request.</p>"""
    type: "capo_dataexchange.types.type.Type"
    """<p>The type of job to be created.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateJobRequest) -> dict:
    out: dict = {}
    if "asset_configuration" in value:
        import capo_dataexchange.types.asset_configuration

        out["AssetConfiguration"] = (
            capo_dataexchange.types.asset_configuration.serialize_json(
                value["asset_configuration"]
            )
        )
    import capo_dataexchange.types.request_details

    out["Details"] = capo_dataexchange.types.request_details.serialize_json(
        value["details"]
    )
    out["Type"] = value["type"]
    return out


def deserialize_json(data: dict) -> CreateJobRequest:
    out: CreateJobRequest = {}  # type: ignore[typeddict-item]
    if data.get("AssetConfiguration") is not None:
        import capo_dataexchange.types.asset_configuration

        out["asset_configuration"] = (
            capo_dataexchange.types.asset_configuration.deserialize_json(
                data["AssetConfiguration"]
            )
        )
    if data.get("Details") is not None:
        import capo_dataexchange.types.request_details

        out["details"] = capo_dataexchange.types.request_details.deserialize_json(
            data["Details"]
        )
    else:
        raise DeserializationError("CreateJobRequest.details required")
    if data.get("Type") is not None:
        out["type"] = data["Type"]
    else:
        out["type"] = ""
    return out
