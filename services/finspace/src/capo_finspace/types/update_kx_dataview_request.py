"""Generated from Smithy shape ``com.amazonaws.finspace#UpdateKxDataviewRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_finspace.types.changeset_id
    import capo_finspace.types.client_token_string
    import capo_finspace.types.database_name
    import capo_finspace.types.description
    import capo_finspace.types.environment_id
    import capo_finspace.types.kx_dataview_name
    import capo_finspace.types.kx_dataview_segment_configuration_list


class UpdateKxDataviewRequest(TypedDict, closed=True):
    environment_id: "capo_finspace.types.environment_id.EnvironmentId"
    """<p>A unique identifier for the kdb environment, where you want to update the dataview.</p>"""
    database_name: "capo_finspace.types.database_name.DatabaseName"
    """<p> The name of the database.</p>"""
    dataview_name: "capo_finspace.types.kx_dataview_name.KxDataviewName"
    """<p>The name of the dataview that you want to update.</p>"""
    description: NotRequired["capo_finspace.types.description.Description"]
    """<p> The description for a dataview. </p>"""
    changeset_id: NotRequired["capo_finspace.types.changeset_id.ChangesetId"]
    """<p>A unique identifier for the changeset.</p>"""
    segment_configurations: NotRequired[
        "capo_finspace.types.kx_dataview_segment_configuration_list.KxDataviewSegmentConfigurationList"
    ]
    """<p> The configuration that contains the database path of the data that you want to place on each selected volume. Each segment must have a unique database path for each volume. If you do not explicitly specify any database path for a volume, they are accessible from the cluster through the default S3/object store segment. </p>"""
    client_token: "capo_finspace.types.client_token_string.ClientTokenString"
    """<p>A token that ensures idempotency. This token expires in 10 minutes.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateKxDataviewRequest) -> dict:
    out: dict = {}
    if "description" in value:
        out["description"] = value["description"]
    if "changeset_id" in value:
        out["changesetId"] = value["changeset_id"]
    if "segment_configurations" in value:
        import capo_finspace.types.kx_dataview_segment_configuration_list

        out["segmentConfigurations"] = (
            capo_finspace.types.kx_dataview_segment_configuration_list.serialize_json(
                value["segment_configurations"]
            )
        )
    out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> UpdateKxDataviewRequest:
    out: UpdateKxDataviewRequest = {}  # type: ignore[typeddict-item]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("changesetId") is not None:
        out["changeset_id"] = data["changesetId"]
    if data.get("segmentConfigurations") is not None:
        import capo_finspace.types.kx_dataview_segment_configuration_list

        out["segment_configurations"] = (
            capo_finspace.types.kx_dataview_segment_configuration_list.deserialize_json(
                data["segmentConfigurations"]
            )
        )
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    else:
        out["client_token"] = ""
    return out
