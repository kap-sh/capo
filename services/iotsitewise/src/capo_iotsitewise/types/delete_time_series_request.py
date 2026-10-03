"""Generated from Smithy shape ``com.amazonaws.iotsitewise#DeleteTimeSeriesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iotsitewise.types.client_token
    import capo_iotsitewise.types.custom_id
    import capo_iotsitewise.types.property_alias
    import capo_iotsitewise.types.workspace_name


class DeleteTimeSeriesRequest(TypedDict, closed=True):
    alias: NotRequired["capo_iotsitewise.types.property_alias.PropertyAlias"]
    """<p>The alias that identifies the time series.</p>"""
    asset_id: NotRequired["capo_iotsitewise.types.custom_id.CustomID"]
    """<p>The ID of the asset in which the asset property was created. This can be either the actual ID in UUID format, or else <code>externalId:</code> followed by the external ID, if it has one. For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-id-references">Referencing objects with external IDs</a> in the <i>IoT SiteWise User Guide</i>.</p>"""
    property_id: NotRequired["capo_iotsitewise.types.custom_id.CustomID"]
    """<p>The ID of the asset property. This can be either the actual ID in UUID format, or else <code>externalId:</code> followed by the external ID, if it has one. For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-id-references">Referencing objects with external IDs</a> in the <i>IoT SiteWise User Guide</i>.</p>"""
    client_token: NotRequired["capo_iotsitewise.types.client_token.ClientToken"]
    """<p>A unique case-sensitive identifier that you can provide to ensure the idempotency of the request. Don't reuse this client token if a new idempotent request is required.</p>"""
    workspace_name: NotRequired["capo_iotsitewise.types.workspace_name.WorkspaceName"]
    """<p>The name of the workspace.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteTimeSeriesRequest) -> dict:
    out: dict = {}
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> DeleteTimeSeriesRequest:
    out: DeleteTimeSeriesRequest = {}  # type: ignore[typeddict-item]
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    return out
